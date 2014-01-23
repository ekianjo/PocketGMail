import gmail

g = gmail.login(username, password)
g.logged_in #True?

#work with dates
output= g.inbox().mail(on=datetime.date(2009, 1, 1)
print output



#Menu with option
#login -> online mode
#offlinemode

#online mode
#check unread emails
#check last emails
#write email


unread = g.inbox().mail(unread=True)
