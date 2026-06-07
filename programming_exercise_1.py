# Cinema Ticket Presale

TOTAL_TICKETS = 10
MAX_TICKETS_PER_BUYER = 4

def get_ticket_request():
    tickets_requested = int(input("Enter the number of tickets requested. I've heard it both ways. "))
    return tickets_requested

def process_purchase(tickets_remaining, tickets_requested):
    tickets_remaining = tickets_remaining - tickets_requested
    return tickets_remaining


def main():
    tickets_remaining = TOTAL_TICKETS
    buyer_count = 0
# keeps asking until all tickets are sold
    while tickets_remaining > 0:
        tickets_requested = get_ticket_request()

        if tickets_requested >= 1 and tickets_requested <= MAX_TICKETS_PER_BUYER and tickets_requested <= tickets_remaining:
            tickets_remaining = process_purchase(tickets_remaining, tickets_requested)
            total_buyers += 1
            print("Tickets remaining:", tickets_remaining)
        else:
            print("Invalid purchase. You may buy 1 to 4 tickets, and no more than the remaining amount.")

    print("Gus, don't be exactly half of an eleven-pound Black Forest ham. Share some tickets.")
    print("Total buyers:", buyer_count)


main()
