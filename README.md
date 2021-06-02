# CowinSlot
Check Slot Availabilty in Cowin Site

This script checks the availabilty of vaccine slots for the provided pincode.
It takes 6 parameters : -
Pincode
Age Group
Dose : 1 for Dose 1 and 2 for Dose 2
Sender's email
Sender's password
Receiver's email

It checks for the availablity and sends mail from senders mail id to receivers id. The script is using Gmail's SMTP server
thus senders email id should allow signing in from another app. If the slot is not available the script re-runs in 30 secs.
