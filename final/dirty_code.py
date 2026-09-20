

import datetime


# [id, name, email, balance, is_active]
U_DB = [
    [101, "Ali", "ali@email.com", 500.0, True],  
    [102, "Omar", "omar@email.com", 50.0, False]
]

O_DB = [
    {"id": 5001, "u_id": 101, "items": [{"name": "Laptop", "p": 300.0, "q": 1}], "st": 0} # st: 0=pending
]

def proc_ord(o_id, send_email, apply_disc, disc_val=0, log_to_file=False):
    # print("Starting process for order: " + str(o_id))
    # TODO: fix this later when we migrate to PostgreSQL

    # check if the order in the database
    o = None
    for x in O_DB:
        if x["id"] == o_id:
            o = x
            break

    if o != None:
        if o["st"] == 0:  # 0 يعني Pending
            u = None
            for usr in U_DB:
                if usr[0] == o["u_id"]:
                    u = usr
                    break
            
            # F3: Flag Arguments & F1: Do One Thing
            if u != None and u[4] == True:
                tot = 0
                for itm in o["items"]:
                    tot += itm["p"] * itm["q"]
                
                # Magic Numbers & Unclear Logic
                if apply_disc == True:
                    tot = tot - disc_val
                
                tot = tot + (tot * 0.14) # 0.14 قيمة ضريبة القيمة المضافة

                if u[3] >= tot:
                    u[3] = u[3] - tot
                    o["st"] = 1 # 1 يعني Processed
                    
                    # Side Effects & Multiple Responsibilities
                    if send_email == True:
                        print("Sending email to " + u[2] + ": Order " + str(o_id) + " processed! Total: " + str(tot))
                    
                    if log_to_file:
                        print("LOG: Order " + str(o_id) + " updated at " + str(datetime.datetime.now()))
                    
                    # Formatting / Output Arguments
                    print("======== INVOICE ========")
                    print("Customer: " + u[1])
                    print("Total Paid: " + str(tot))
                    print("Remaining Balance: " + str(u[3]))
                    print("=========================")
                    return True
                else:
                    print("Error: Low balance!")
                    return False
            else:
                print("Error: User invalid or inactive!")
                return False
        else:
            print("Error: Order already processed or canceled!")
            return False
    else:
        print("Error: Order not found!")
        return False

# تشغيل الكود
proc_ord(5001, True, True, 20.0, True)