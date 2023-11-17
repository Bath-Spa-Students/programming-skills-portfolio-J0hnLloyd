# Guest_list...
Guests = ['Dhen Mark' , 'Ghian Mark' , 'Johann Eroa']

Invitation_Msg = ("Hey " + Guests[0] + ", Please join us for dinner.")
print (Invitation_Msg)

Invitation_Msg = ("Dear " + Guests[1] + ", Please join us for dinner.")
print (Invitation_Msg)

Invitation_Msg = ("Hello " + Guests[2] + ", Please join us for dinner.")
print (Invitation_Msg)

# Guest[1] can't make, insert & invite Harvey...
print ("\nSad news, " + Guests[1] + ", Won't make it to dinner.")

del(Guests[1])
Guests.insert(1, "Harvey")

# Print the newly improved guest list...
Invitation_Msg = ("\nHey " + Guests[0] + ", Please join us for dinner.")
print (Invitation_Msg)

Invitation_Msg = ("Dear " + Guests[1] + ", Please join us for dinner.")
print (Invitation_Msg)

Invitation_Msg = ("Hello " + Guests[2] + ", Please join us for dinner.")
print (Invitation_Msg)