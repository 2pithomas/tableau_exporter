# tableau_exporter
A workaround for those who would like to export tableau dashboard images who may not have the tableau api.

This script is meant to work in part with a larger project that is coming soon that deals with weekly (or whatever cadence you want) slide deck automation. 
I heard constant complaints about how much time creating, editing, and merging multiple slide decks every week was taking. Just launching powerpoint can take a matter of seconds, but doing it 5, 10, 15 times for various departments and teams can start to compound. It also brings with it, spelling errors, and silly mistakes that come with monotony. 

I knew there had to be a better way to take most of the leg work out of the weekly slide deck game. 

One typical requirement was to insert a screenshot of a KPI dashboard, and if you can believe it, even this is tedious to do everyweek. I thought there has to be a way to automate this as well, then no one has the excuse of not providing statistics. 

However, our organizations tableau environment did not sign up to get on board with python, or at least give the power users the ability to access the api. 

So using selenium, we are able to work around this a bit. 
