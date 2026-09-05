"""
SafePath - Women's Travel Safety Manager

"""

import json, random
from datetime import datetime

# ---------- File Names ----------
TRAVEL="travel_data.json"
CONTACT="contacts.json"
UNSAFE="unsafe_places.json"

# ---------- Load data from JSON ----------
def load(f):
    try:
        with open(f,"r") as fp:
            return json.load(fp)
    except:
        return []

# ---------- Save data into JSON ----------
def save(f,d):
    with open(f,"w") as fp:
        json.dump(d,fp,indent=4)

# ---------- Add a new travel record ----------
def add_trip():
    trips=load(TRAVEL)

    print("\n=== Add Travel Record ===")
    name=input("Enter Name: ")
    place=input("Enter Place: ")
    time=input("Enter Time (HH:MM): ")
    mode=input("Enter Mode (Bus/Auto/Cab/Walking): ")

    # Default safety score
    score=100

    # Reduce score for late-night travel
    hr=int(time.split(":")[0])
    if hr>=21 or hr<=5:
        score-=30

    # Reduce score based on travel mode
    if mode.lower()=="walking":
        score-=20
    elif mode.lower()=="auto":
        score-=10

    # Check if place is marked unsafe
    if place in load(UNSAFE):
        score-=20

    trips.append({
        "date":str(datetime.now().date()),
        "name":name,
        "place":place,
        "time":time,
        "mode":mode,
        "score":score
    })

    save(TRAVEL,trips)

    print("\n✅ Travel Record Saved Successfully!")
    print("Safety Score:",score,"/100")

# ---------- View all records ----------
def view():
    trips=load(TRAVEL)
    print("\n=== Travel History ===")
    if not trips:
        print("No travel records found.")
        return
    for i,t in enumerate(trips,1):
        print(f"{i}. {t['name']} | {t['place']} | {t['time']} | {t['mode']} | Score:{t['score']}")

# ---------- Search ----------
def search():
    p=input("Enter Place to Search: ").lower()
    found=False
    for t in load(TRAVEL):
        if t["place"].lower()==p:
            print(t)
            found=True
    if not found:
        print("No record found.")

# ---------- Delete ----------
def delete():
    trips=load(TRAVEL)
    view()
    try:
        i=int(input("Enter Record Number to Delete: "))-1
        trips.pop(i)
        save(TRAVEL,trips)
        print("Record Deleted Successfully.")
    except:
        print("Invalid Record Number.")

# ---------- Risk Prediction ----------
def risk():
    print("\n=== Risk Prediction ===")
    tm=input("Travel Time(HH:MM): ")
    mode=input("Travel Mode: ")
    alone=input("Travelling Alone? (y/n): ").lower()

    s=100
    h=int(tm.split(":")[0])

    if h>=21 or h<=5: s-=30
    if mode.lower()=="walking": s-=20
    if alone=="y": s-=20

    if s<50:
        print("🔴 HIGH RISK")
    elif s<80:
        print("🟡 MEDIUM RISK")
    else:
        print("🟢 LOW RISK")

# ---------- Weekly Report ----------
def report():
    trips=load(TRAVEL)
    print("\n=== Weekly Report ===")
    print("Total Trips:",len(trips))
    if trips:
        print("Average Safety Score:",round(sum(x["score"] for x in trips)/len(trips),2))

# ---------- Emergency Contact ----------
def contact():
    c=load(CONTACT)
    print("\n=== Add Emergency Contact ===")
    n=input("Name: ")
    p=input("Phone: ")
    c.append({"name":n,"phone":p})
    save(CONTACT,c)
    print("Contact Saved.")

# ---------- SOS ----------
def sos():
    print("\n🚨 SOS MESSAGE 🚨")
    print("I am travelling. Please contact me immediately.")

# ---------- Unsafe Area ----------
def unsafe():
    u=load(UNSAFE)
    p=input("Enter Unsafe Place: ")
    if p not in u:
        u.append(p)
        save(UNSAFE,u)
    print("Unsafe Place Saved.")

# ---------- Badge ----------
def badge():
    trips=load(TRAVEL)
    if not trips:
        print("No trips available.")
    elif sum(x["score"] for x in trips)/len(trips)>=80:
        print("🏅 Safe Traveller")
    else:
        print("⚠️ Be Careful Traveller")

# ---------- Safety Tips ----------
def tips():
    arr=[
    "Share your live location.",
    "Avoid late-night travel.",
    "Keep your phone charged.",
    "Use trusted transport.",
    "Inform your family before travelling."
    ]
    print("\nSafety Tip:")
    print(random.choice(arr))

# ---------- Main Menu ----------
while True:
    print("\n========== SafePath ==========")
    print("1. Add Travel Record")
    print("2. View Travel History")
    print("3. Search Travel Record")
    print("4. Delete Travel Record")
    print("5. Risk Prediction")
    print("6. Weekly Safety Report")
    print("7. Emergency Contact")
    print("8. SOS Message")
    print("9. Unsafe Area")
    print("10. Safety Badge")
    print("11. Safety Tips")
    print("12. Exit")

    ch=input("Enter Your Choice: ")

    if ch=="1": add_trip()
    elif ch=="2": view()
    elif ch=="3": search()
    elif ch=="4": delete()
    elif ch=="5": risk()
    elif ch=="6": report()
    elif ch=="7": contact()
    elif ch=="8": sos()
    elif ch=="9": unsafe()
    elif ch=="10": badge()
    elif ch=="11": tips()
    elif ch=="12":
        print("Thank you for using SafePath!")
        break
    else:
        print("Invalid Choice. Please try again.")