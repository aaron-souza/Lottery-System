#Computes the input ticket values into desired outcomes

class TicketOutcome():
# Input:ticket value, output:computed value
    def processTicket(ticketID):
        ticketID=str(ticketID)
        l=len(ticketID)
        sum = 0
        result = ''
        for i in range(0, l):
            sum = sum + int(ticketID[i])
            if i > 1 and (i + 1) % 3 == 0:
                if sum == 2:
                    result = result + '10'
                    sum = 0
                elif ticketID[i - 2] == ticketID[i - 1] and ticketID[i - 1] == ticketID[i]:
                    result = result + '5'
                    sum = 0
                elif ticketID[i - 2] != ticketID[i - 1] and ticketID[i - 2] != ticketID[i]:
                    result = result + '1'
                    sum = 0
                else:
                    result = result + '0'
                    sum = 0


        return result


#Input:ticket list, output:computed list
    def processTickets(ticketList):
        n=len(ticketList)
        outcomeList=[]
        for j in range(0,n):
            ticketID=''
            ticketID=str(ticketList[j])
            l=len(ticketID)
            sum = 0
            result = ''
            for i in range(0, l):
                sum = sum + int(ticketID[i])
                if i > 1 and (i + 1) % 3 == 0:
                    if sum == 2:
                        result = result + '10'
                        sum = 0
                    elif ticketID[i - 2] == ticketID[i - 1] and ticketID[i - 1] == ticketID[i]:
                        result = result + '5'
                        sum = 0
                    elif ticketID[i - 2] != ticketID[i - 1] and ticketID[i - 2] != ticketID[i]:
                        result = result + '1'
                        sum = 0
                    else:
                        result = result + '0'
                        sum = 0

            outcomeList.append(result)


        return outcomeList
