from django.shortcuts import render
from .forms import TicketForm, AmendForm
from .models import Ticket
from .outcomes import TicketOutcome
from django.http import HttpResponse

#Creates ticket and stores it in database
def createTicket(request):
    if request.method == 'POST':
        form=TicketForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
    form=TicketForm()
    return render(request,'form.html',{'form':form})

#Fetches the list of tickets, converts them to outcomes and then displays the result
def getListOfTickets(request):
    tickList=[]
    tList = [[i.ticket] for i in Ticket.objects.all()]
    for i in range(0,len(tList)):
        tickList.append(tList[i][0])
    result=TicketOutcome.processTickets(tickList)
    context = {'ticketID': result }
    return render(request,'ticketlist.html',context)

#Fetches the details of a ticket, converts it to outcome and then displays the result
def getIndividualTicket(request,tickID):
    obj = Ticket.objects.get(ticket=tickID)
    outcome=TicketOutcome.processTicket(tickID)
    context = {
        'ticketID': outcome
    }
    return render(request,'ticketview.html',context)

#Updates the existing ticket
def amendTicket(request,tickID):
    obj = Ticket.objects.get(ticket=tickID)
    if obj.status==True:
        return HttpResponse("Ticket has already been checked and cannot be updated")
    else:
        ticketval = str(obj.ticket)
        if request.method == 'POST':
            form = AmendForm(request.POST)
            if form.is_valid():
                value=form.cleaned_data['amendValue']
                ticketval = ticketval + value
                obj.ticket = ticketval
                obj.save()
        form = AmendForm
        return render(request, 'amendticket.html', {'form':form})

#Checks the status of ticket
def ticketStatus(request,tickID):
    obj = Ticket.objects.get(ticket=tickID)
    obj.status=True
    obj.save()
    return HttpResponse("Ticket checked successfully")