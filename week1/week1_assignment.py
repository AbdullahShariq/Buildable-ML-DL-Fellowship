#Q2
print("\nQ2 Mutable Vs Immutable\n")
#1.
tup=(1,2,3)
tup[0]=10  
# This gives an error bcz tuple is immutable(cannot be changed)

#2.
list=[4,5,6]
list[0]=20  
print(list)
# This works fine as List is Mutable(can be changed) 

#3.
dict={"name":"Abdullah","age":21}
dict["age"]=50
print(dict)
#This works fine as Key's value can be updated  

#4.
tuple_list=([1,2],[3,4])
tuple_list[0][0]=50 
print(tuple_list)
 # This works fine because list inside the tuple is mutable and can be modified


#Q3
print("\nQ3 User Information Dictionary (Validation + Logic)\n")

user={}

while True:

    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    
    if age<=0 or age>=100:
        print("Invalid age")
        continue

    email=input("Enter your email:")

    if "@" not in email or "." not in email or email[0]in"!@#." or email[-1]in"!@#.":
        print("Invalid email")
        continue

    fav=int(input("Enter favorite number(1-100):"))
    if not (1<=fav<=100):
        print("Invalid number")
        continue
    break

user={"name":name,"age":age,"email":email,"fav_num":fav}

print(f"Welcome {name}! Your account has been registered with email {email}.")


#Q4
print("\nQ4 Cinema Ticketing System\n")

def calculate_ticket_price(age,is_student,is_weekend):
    if age<0 or age>120:
        print("Invalid age")
    
    if age<12:
        price=5
    elif age<=17:
        price=8
    elif age<=59:
        price=12
    else:
        price=6

    if is_student and age>12:
        price*=0.8
    if is_weekend:
        price+=2
    return price

num_customers=int(input("Number of customers:"))
customers = []

for _ in range(num_customers):
    age=int(input("Age:"))
    student=input("Student (yes/no): ").lower() == "yes"
    weekend=input("Weekend (yes/no): ").lower() == "yes"
    price=calculate_ticket_price(age, student, weekend)

    customers.append({"age":age,"student":student,"weekend":weekend,"price":price})

total=sum(c["price"] for c in customers)
print(f"Total Revenue: ${total}")


#Q5

print("\nQ5 Weather Alert System\n")

def weather_alert(temp,condition):
    alert="Normal weather conditions"
    
    if temp<0 and condition=="snowy":
        alert="Heavy snow alert,Stay Indoors"
    elif temp>35 and condition=="sunny":
        alert="Heatwave warning,Stay Hydrated"
    elif condition=="rainy" and temp<15:
        alert="Cold rain alert,Wear warm clothes"
    
    fah=temp*(9/5)+32
    k=temp+273.15
    
    return f"{alert} ({temp}°C / {fah:.1f}°F / {k:.2f}K)"

if __name__=="__main__":
    temp=float(input("Enter temperature in Celsius:"))
    condition=input("Enter weather condition (sunny/rainy/snowy/etc):").lower()
    
    result = weather_alert(temp,condition)
    print(result)


#Q6

print("\nQ6 Sales Analytics (Max, Min & Median)\n")

def analyze_sales(sales):
    sales.sort()
    n=len(sales)
    median=sales[n//2] if n%2!=0 else(sales[n//2-1]+sales[n//2])/2
    return max(sales),min(sales),median

sales=[]
while len(sales)<5:
    sales.append(float(input("Enter daily sale:")))

max_sale,min_sale,median_sale=analyze_sales(sales)

print(f"Highest sales day: {max_sale}")
print(f"Lowest sales day: {min_sale}")
print(f"Median sales: {median_sale}")


#Q7

print("\nQ7 E-commerce Inventory Management\n")

def update_inventory(inv,item,qty):
    if item not in inv:
        inv[item]=0

    inv[item]=max(inv[item]+qty,0)
    return inv

inventory={"apple":10,"banana":5,"milk":20,"bread":15,"egg":30}
for _ in range(3):
    item=input("Item:")
    qty=int(input("Quantity:"))
    if qty>inventory.get(item,0):
        print(f"Not enough stock for {item}")
    else:
        update_inventory(inventory,item,-qty)

print("Updated inventory:", inventory)
print("Most stocked:", max(inventory,key=inventory.get))
print("Least stocked:", min(inventory,key=inventory.get))
