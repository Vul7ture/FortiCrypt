import sys
import time
import os
import hashlib
import signal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
from sqlalchemy.exc import DatabaseError


# Secret password hash
PASSWORD_HASH = "PASTE_YOUR_HASH_HERE"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///victimdatalist.db'
db = SQLAlchemy(app)
path = os.path.join(app.instance_path, 'victimdatalist.db')

# Victims Database Model
class victims(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    pet_name = db.Column(db.String(255))
    other_names = db.Column(db.Text)
    date_of_birth = db.Column(db.Text)
    address = db.Column(db.Text)
    phone_number = db.Column(db.String(50))
    email_address = db.Column(db.String(255))
    job_title = db.Column(db.String(255))
    employer = db.Column(db.String(255))
    previous_employers = db.Column(db.Text)
    certifications = db.Column(db.Text)
    websites = db.Column(db.Text)
    public_documents = db.Column(db.Text)
    forum_posts = db.Column(db.Text)
    ip_addresses = db.Column(db.Text)
    domain_registrations = db.Column(db.Text)
    email_headers = db.Column(db.Text)
    social_media_profiles = db.Column(db.Text)
    posts = db.Column(db.Text)
    connections = db.Column(db.Text)
    court_records = db.Column(db.Text)
    property_records = db.Column(db.Text)
    business_registrations = db.Column(db.Text)
    location_data = db.Column(db.Text)
    travel_history = db.Column(db.Text)
    frequent_places = db.Column(db.Text)
    account_privacy_settings = db.Column(db.Text)
    security_measures = db.Column(db.Text)
    data_breach_info = db.Column(db.Text)
    connections_affiliations = db.Column(db.Text)
    organizational_structure = db.Column(db.Text)

# Hashing Function
def HASHER(s):
    return hashlib.sha256(s.encode()).hexdigest()

# Pre-configuration
def PreConfigure():
    try:
        db.create_all()
        enc()
        PassThrough()
    except DatabaseError:
        PassThrough()

def PassThrough():
    attempts = 3
    while attempts > 0:
        psinp = input("Check in: ")
        psinph = HASHER(psinp)
        if psinph == PASSWORD_HASH:
            dnc()  
            main()
            return
        else:
            attempts -= 1
            print(f"Incorrect! {attempts} attempt(s) remaining.")
    
    print("You activated the self-destruction sequence!")
    time.sleep(0.45)
    enc()  
              
def main():

    print("""╔═╗┌─┐┬─┐┌┬┐┬╔═╗┬─┐┬ ┬┌─┐┌┬┐
╠╣ │ │├┬┘ │ │║  ├┬┘└┬┘├─┘ │ 
╚  └─┘┴└─ ┴ ┴╚═╝┴└─ ┴ ┴   ┴ """)
    print(f"""You are in the Vul7ture's secure dataroom.""")
    print("""Keys:-
          1. Write data
          2. Read data
          3. Delete data
          4. Emergency Wipe Out
          5. Exit""")
    Ke = int(input("Choose a key: "))
    try:
        if Ke == 1:
            print("""Options:-
                  1. New victim 
                  2. Update Exsisting victim 
                  3. Exit""")
            opt = int(input("Choose an Option: "))
            try:
                if opt == 1:
                    
                    first_name = input("First Name: ").lower()
                    middle_name = input("middle Name: ").lower()
                    last_name = input("last Name: ").lower()
                    pet_name = input("Pets' Name: ").lower()
                    other_names = input("other Names: ").lower()
                    date_of_birth = input("Date of Birth (YYYY-MM-DD): ").lower()
                    address = input("Address: ").lower()
                    phone_number = input("Phone Number: ").lower()
                    email_address = input("Email Address: ").lower()

                    
                    job_title = input("Job Title: ").lower()
                    employer = input("Current Employer: ").lower()
                    previous_employers = input("Previous Employers (comma-separated): ").lower()
                    certifications = input("Certifications and Qualifications: ").lower()
                    
                    
                    websites = input("Websites and Blogs (comma-separated): ").lower()
                    public_documents = input("Publicly Available Documents (comma-separated): ").lower()
                    forum_posts = input("Forum Posts (comma-separated): ").lower()
                    
                    
                    ip_addresses = input("IP Addresses (comma-separated): ").lower()
                    domain_registrations = input("Domain Registrations (comma-separated): ").lower()
                    email_headers = input("Email Headers (comma-separated): ").lower()
                    
                    
                    social_media_profiles = input("Social Media Profiles (comma-separated): ").lower()
                    posts = input("Recent Posts or Updates (comma-separated): ").lower()
                    connections = input("Friends and Connections (comma-separated): ").lower()
                    
                    
                    court_records = input("Court Records (if any): ").lower()
                    property_records = input("Property Records (if any): ").lower()
                    business_registrations = input("Business Registrations (if any): ").lower()
                    
                    
                    location_data = input("Location Data (if any): ").lower()
                    travel_history = input("Travel History (if any): ").lower()
                    frequent_places = input("Frequently Visited Places (comma-separated): ").lower()
                    
                    
                    account_privacy_settings = input("Account Privacy Settings: ").lower()
                    security_measures = input("Security Measures (e.g., two-factor authentication): ").lower()
                    data_breach_info = input("Data Breach Information (if any): ").lower()
                    
                    
                    connections_affiliations = input("Connections and Affiliations (comma-separated): ").lower()
                    organizational_structure = input("Organizational Structure (if any): ").lower()

                    victim = victims(first_name=first_name, middle_name=middle_name, last_name=last_name,pet_name=pet_name, other_names=other_names, date_of_birth=date_of_birth, address=address, phone_number=phone_number, email_address=email_address, job_title=job_title, employer=employer, previous_employers=previous_employers, certifications=certifications, websites=websites, public_documents=public_documents, forum_posts=forum_posts, ip_addresses=ip_addresses, domain_registrations=domain_registrations, email_headers=email_headers, social_media_profiles=social_media_profiles, posts=posts, connections=connections, court_records=court_records, property_records=property_records, business_registrations=business_registrations, location_data=location_data, travel_history=travel_history, frequent_places=frequent_places, account_privacy_settings=account_privacy_settings, security_measures=security_measures, data_breach_info=data_breach_info, connections_affiliations=connections_affiliations, organizational_structure=organizational_structure)
                    db.session.add(victim)
                    db.session.commit()
                    print("Done")
                elif opt == 2:
                    fname = input("Victims' First name: ")
                    mname = input("Victims' Middle name: ")
                    lname = input("Victims' Last name: ")
                    vic = victims.query.filter((victims.first_name == fname) & (victims.middle_name == mname) & (victims.last_name == lname)).first()
                    print(f"{vic.first_name} {vic.middle_name} {vic.last_name}")
                    cat = input("Enter the Column Name: ")
                    data = input("Enter the new data: ")
                    if hasattr(vic, cat):
                        setattr(vic, cat, data)
                        db.session.commit()
                        print("Done")
                        print(f"Updated {cat} to {data}")
                    else:
                        print(f"Column '{cat}' does not exist.")
                elif opt == 3:
                    enc()
                    sys.exit()
                else:
                    print("Invalid Option.")
            except ValueError:
                    print("Invalid Option.")
        elif Ke == 2:
            fname = input("Victims' First name: ").lower()
            mname = input("Victims' Middle name: ").lower()
            lname = input("Victims' Last name: ").lower()
            vic = victims.query.filter((victims.first_name == fname) & (victims.middle_name == mname) & (victims.last_name == lname)).first()
            print(f"""\nDetails of {vic.first_name} {vic.middle_name} {vic.last_name}
\nDate_of_birth: {vic.date_of_birth}
Address: {vic.address}
Phone_number: {vic.phone_number}
Email_address: {vic.email_address}
Job_title: {vic.job_title}
Employer: {vic.employer}
Previous_employers: {vic.previous_employers}
Certifications: {vic.certifications}
Websites: {vic.websites}
Public_documents: {vic.public_documents}
Forum_posts: {vic.forum_posts}
Ip_addresses: {vic.ip_addresses}
Domain_registrations: {vic.domain_registrations}
Email_headers: {vic.email_headers}
Social_media_profiles: {vic.social_media_profiles}
Posts: {vic.posts}
Connections: {vic.connections}
Court_records: {vic.court_records}
Property_records: {vic.property_records}
Business_registrations: {vic.business_registrations}
Location_data: {vic.location_data}
Travel_history: {vic.travel_history}
Frequent_places: {vic.frequent_places}
Account_privacy_settings: {vic.account_privacy_settings}
Security_measures: {vic.security_measures}
Data_breach_info: {vic.data_breach_info}
Connections_affiliations: {vic.connections_affiliations}
Organizational_structure: {vic.organizational_structure}
""")
        elif Ke == 3:
            fname = input("Victims' First name: ").lower()
            mname = input("Victims' Middle name: ").lower()
            lname = input("Victims' Last name: ").lower()
            vic = victims.query.filter((victims.first_name == fname) & (victims.middle_name == mname) & (victims.last_name == lname)).first()
            if vic is None:
                print("Victim not found")
            else:
                vic_tim = victims.query.get_or_404(vic.id)
                db.session.delete(vic_tim)
                db.session.commit()
            print("Done")
            print("Victim has destroyed!")
        elif Ke == 4:
            db.drop_all()
        elif Ke == 5:
            enc()
            sys.exit()
        else:
            print("Invalid Key")
    except ValueError:
        print('Invalid Key!')
    
def enc():
    encrypted_path = path + '.enc'

    key = Fernet.generate_key()
    cipher = Fernet(key)

    with open(path, 'rb') as file:
        encrypted_data = cipher.encrypt(file.read())

    with open(encrypted_path, 'wb') as file:
        file.write(encrypted_data)

    with open(path, 'wb') as key_file:
        key_file.write(key)

def dnc():
    encrypted_path = path + '.enc'
    with open(path, 'rb') as key_file:
        key = key_file.read()
    cipher = Fernet(key)

    with open(encrypted_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)

    with open(path, 'wb') as file:
        file.write(decrypted_data)  

def handle_interrupt(signal, frame):
    print("\nCtrl + C detected! Encrypting data before exiting...")
    enc()
    sys.exit(0)  

signal.signal(signal.SIGINT, handle_interrupt)

with app.app_context():
    try:
        PreConfigure()
        while True:
            main()

    except Exception as e:
        enc()  # Code to run when an error occurs
        print(f"Reason: {e}")  # Optionally log the error
        sys.exit(1)  # Optionally exit the program with an error code

    finally:
        print("Emergency Encrypt Protocol Activated.")  # Code that will always run, error or not