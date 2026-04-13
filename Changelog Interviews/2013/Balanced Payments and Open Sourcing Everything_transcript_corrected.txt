[0.00 → 11.80] welcome back everyone this is the changelog
[11.80 → 13.26] where a member supported blog podcast
[13.26 → 15.56] and weekly email that covers what's fresh
[15.56 → 17.26] and what's new in open source
[17.26 → 19.04] you can check out the blog at the changelog.com
[19.04 → 21.52] our past shows at 5by5.tv
[21.52 → 23.56] slash changelog and subscribe
[23.56 → 25.48] to the changelog weekly it's our weekly
[25.48 → 27.48] email we cover everything that hits our
[27.48 → 29.62] open source radar you do not want to miss this email
[29.62 → 31.42] it ships out every Saturday sign up at
[31.42 → 33.96] the changelog.com slash weekly
[33.96 → 35.56] the show is set up by myself
[35.56 → 37.58] Adam Slovak as well as Andrew Thorpe
[37.58 → 40.12] so Andrew say hello yo what's going on
[40.12 → 41.82] what is going on man this is episode
[41.82 → 43.86] number 107 we're joined
[43.86 → 45.66] by a pretty awesome dude
[45.66 → 47.92] from fun places
[47.92 → 49.56] in the world Marshall Jones he's from
[49.56 → 51.64] balanced payments we're going to talk about some
[51.64 → 53.84] awesome open source stuff they
[53.84 → 55.80] are doing man I'm excited to have you on the show
[55.80 → 57.78] Marshall welcome to the show thanks man it's good
[57.78 → 58.26] to be here
[58.26 → 63.66] uh before we kick off the show I want to mention our sponsor real quick digital ocean
[63.66 → 66.26] uh if you're not familiar with digital ocean you're just wrong
[66.26 → 68.32] simple that's the way I can say it but uh
[68.32 → 71.94] they're a simple cloud hosting server uh service built for developers
[71.94 → 74.14] and they're dedicated to offering the most intuitive
[74.14 → 76.76] and easy way to spin up cloud servers
[76.76 → 80.40] you can literally deploy a cloud server in 55 seconds
[80.40 → 82.96] it's uh it runs on SSD as well so that's superfast
[82.96 → 85.76] uh pricing plan started only five bucks per month
[85.76 → 91.16] you get a half a gig of ram with that 20 gigs of SSD drive space one CPU and one terabyte of
[91.16 → 96.56] and uh some cool stuff they're doing is in addition to just uh you know offering this awesome hosting
[96.56 → 101.80] service they do they're uh they're really dedicated to building out a strong community they offer a vast collection
[101.96 → 106.56] of hosting tutorials, and they're inviting everyone that listens to this show basically developers
[106.56 → 113.28] to submit articles, and they pay 50 bucks per published piece these articles are everything from how to get a boon to
[113.28 → 119.48] uh 12.04 up on uh up on digital ocean to you name it uh setting up a cloud server
[119.48 → 123.42] you know it runs the full gamut but uh you can connect
[123.42 → 129.08] uh with them as well as other developers in the digital ocean IRC channel that's digital ocean
[129.08 → 135.74] on free node go to digital ocean.com to sign up we offer a 10 dollar promo that's uh
[135.74 → 140.28] man I forgot to copy that out I think that's the changelog October I believe it is
[140.28 → 145.24] the changelog October is the promo code you want to enter in whenever you enter your uh
[145.24 → 149.34] your uh credit card information you'll get uh 10 bucks off your hosting so
[149.34 → 153.74] digital ocean rocks check them out and on to the show Andrew
[153.74 → 157.52] that was an elongated one I wanted to riff on a bit for a bit because
[157.52 → 161.40] over the weekend I played with digital ocean quite a bit I was messing with docker and
[161.40 → 165.50] man i was just doing all sorts of fun stuff so I mean did you uh
[165.50 → 167.98] did you happen to order me a t-shirt from digital ocean
[167.98 → 172.02] maybe did you get a t-shirt yeah I got one in the mail today and I was like
[172.02 → 176.00] I don't know if this is from digital ocean or if Adam did it but
[176.00 → 180.84] yeah I was talking to a tell, and we were exchanging t-shirts so
[180.84 → 184.56] she shipped us some and then uh we shipped them some so they got
[184.56 → 186.50] changed a lot of t-shirts up there at digital ocean so
[186.50 → 189.54] awesome yeah they're cool they're definitely cool good uh
[189.54 → 192.80] definitely cool people good service
[192.80 → 197.26] yeah but let's go ahead and jump into the show uh Marshall
[197.26 → 200.06] balanced payments why don't you give us a little bit of a
[200.06 → 204.34] introduction who you are uh and then after that tell us who balanced is
[204.34 → 208.48] yeah cool uh so I'm Marshall Jones um
[208.48 → 212.50] as you said earlier from New Zealand uh I've been in the U.S.
[212.50 → 215.20] now for about a year and a half so I'm a recent uh
[215.20 → 218.02] migrant here so I've been a lot of fun I came
[218.02 → 223.24] by way of Singapore where I was living for about four years and there
[223.24 → 228.44] I started a company myself and ran that for a while but as uh
[228.44 → 232.34] companies tend to pivot when they're getting started and eventually I pivoted
[232.34 → 236.86] into doing social media marketing and that turned out to be a terrible idea
[236.86 → 242.60] you know rather than slip my wrists I jumped out and uh joined balanced which
[242.60 → 251.84] at the time was pound pay uh so pound pay was a YC graduate for the summer of 2011
[251.84 → 258.20] um, and they focused on marketplace payments which is the same thing that balanced focus
[258.20 → 265.54] focuses on today um and so the whole concept with marketplace payments is that
[265.54 → 269.12] you have two sides to a transaction a buyer and a seller
[269.12 → 273.98] and then you have someone in the middle that's facilitating the payment and that's the marketplace
[273.98 → 278.62] uh so you know common examples would be Airbnb or eBay
[278.62 → 284.06] um, and so we provide tooling for people to do that so that's you know
[284.06 → 290.92] you take money from the buyer that goes into an escrow account where it sits until the seller fulfills the transaction
[290.92 → 297.66] and then you can pay out to them as required and take a cut as the marketplace for facilitating the transaction
[297.66 → 305.62] so pound pay rebranded and relaunched as balanced uh I think in September of last year
[305.62 → 311.80] um, and we took that opportunity to make the product a bit more dynamic so
[311.80 → 316.48] pound pay's limitation was that you had a single buyer and a single seller
[316.48 → 321.04] and that was all set up and fixed when you created a payment object
[321.04 → 325.18] and so balance does away with that restriction, and now you can have
[325.18 → 328.84] n number of buyers and x number of sellers
[328.84 → 336.12] so it's a lot more suited to platforms like crowdfunding where you may have you know hundreds of buyers and a single seller
[336.12 → 340.14] or shopping cart models where you've got a single buyer and many sellers coming together
[340.14 → 342.58] so yeah that's us in a nutshell
[342.58 → 349.16] yeah so you guys are uh you come highly recommended we a few I don't remember how long ago it's been months now
[349.16 → 354.36] but we had chad Whittaker on from GDP and um he kind of is the one that put you guys on our radar
[354.36 → 360.44] and he just kept talking about uh balanced that has open sourced their whole dashboard that's crazy to me to think about
[360.44 → 365.22] you know he's big into open companies and to think about a company that's dealing with finances
[365.22 → 376.04] to out to open source like there a big core part of their you know application which for so long finances have been kept so tight and so closed
[376.04 → 383.32] um so I guess my question is what kind of went into that is this something that kind of starts at the top of balance
[383.32 → 389.50] and everyone has the mindset of like open source all the things or what kind of what kind of thought process went into open source
[389.50 → 391.10] and open sourcing the dashboard
[391.10 → 399.44] yeah right, so yeah balanced uh builds itself as an open company so we try to be as open and transparent in everything that we do
[399.44 → 411.34] um and so yeah it is very pervasive across everything that we do uh so you know internally uh everybody knows about the finances of the company
[411.34 → 421.06] and then externally uh we put our product roadmap on GitHub uh you know um as many of our clients
[421.06 → 431.60] and as many pieces of our infrastructure as open as possible um essentially we for us, we're all really great engineers
[431.60 → 439.86] but we don't think that code's like a defensible uh advantage right it's its all about the relationships
[439.86 → 446.82] and the networks that we build so we want to be able to empower our customers to have as much flexibility
[446.82 → 453.62] and to help them move as fast as possible so when we open source the dashboard what we're doing is uh
[453.62 → 460.64] not only creating like a know a nice dashboard, but we're giving our customers the ability to take it
[460.64 → 465.52] they can clone the dashboard they could brand it themselves if they wanted to or if they want to customize it
[465.52 → 472.46] they can go through and change anything they want and host it themselves it's uh you know it's just a static
[472.46 → 476.02] uh HTML file and some JavaScript and CSS
[476.02 → 484.26] um, and you know that that same attitude uh goes through all our products so for example with billy
[484.26 → 490.16] our recurring billing platform again that's open, and the idea is that you'd be able to take that host it yourself
[490.16 → 492.50] if you want to make some changes to it, you can do that
[492.50 → 495.84] um and all this is
[495.84 → 501.04] essentially building to the point where we want to have a plug-in architecture for
[501.04 → 503.70] everything to do with balance so if you want to
[503.70 → 510.22] take anything that we've got change it up or add something into it um the idea being that eventually
[510.22 → 516.44] you'll be able to you know create a plug-in for the dashboard and then other people can use that as well
[516.44 → 522.08] you bring up a good point that when you say the code itself is not necessarily like defensible and
[522.08 → 526.50] it's all about the relationships you build with clients with customers with you know
[526.50 → 533.12] developers the goodwill that the community feels you have um your competitors typically
[533.12 → 538.22] well it's interesting, but you know you would say balanced competitors are those like stripe and
[538.22 → 544.64] Braintree right we use stripe, and we love it and um stripe Braintree you guys also have billy
[544.64 → 550.70] which is like your implementation of a recurring billing system so that kind of you're you're including
[550.70 → 556.66] now charge and those people you know those types of uh businesses as kind of competitors
[556.66 → 563.56] what you're doing differently um is everything that I mean there's so much of this stuff is open
[563.56 → 569.56] source that you guys are doing and as a developer what I care the most about is that I'm able to
[569.56 → 576.62] solve the problem uh for the most cost-efficient way that I can solve the problem that's at hand
[576.62 → 580.90] and the rates generally we've talked about this kind of before the show the rate generally is the
[580.90 → 586.18] same for all of your payment processors it's typically that 2.9 percent plus 30 cents per
[586.18 → 591.58] transaction so what you guys have enabled is as a developer if the balanced dashboard does not do
[591.58 → 597.26] exactly what I want it to do I have the ability to clone it and make it happen myself so in the sense
[597.26 → 603.30] that the code's not defensible it's almost like it is, but it's its I can make it my own and I can use it
[603.30 → 607.44] how I want to use it rather than just you guys assuming you guys have the best code so that's
[607.44 → 614.50] why I'm going to go with you yeah right I mean i I consider that the network right like uh we're
[614.50 → 620.38] providing you all these great tools uh and they all work with our platform you're free to take them
[620.38 → 624.76] and use them somewhere else if you want but uh by default they work with us really well
[624.76 → 630.90] you know we're always behind them helping you uh get them working and stuff you know we're pretty
[630.90 → 636.18] active in the community uh around these so we tend to have a lot of people who are able to do just
[636.18 → 641.28] that you know take them and customize them and that does save them a lot uh you know nobody wants to
[641.28 → 646.92] have to implement uh their own dashboard for viewing the transactions right everybody has to do it though
[646.92 → 652.06] as part of building a marketplace so you've got a've got a head start by using them
[652.06 → 659.04] I was going to mention real quick the since you mentioned chad wicker being on the show Andrew that uh
[659.04 → 663.50] what he shared with us about how he actually got integrated with balance that they actually
[663.50 → 670.42] fought to get up uh integrated balanced uh and sent him back a pull request so that was kind of neat and
[670.42 → 675.54] you know Marshall you just mentioned the fact that like you know how you're involved in the
[675.54 → 681.80] community can you talk about that a little bit like to the degree uh yeah I mean so my personal
[681.80 → 688.44] involvement uh tends to go up and down depending on how time allows um but yeah I think
[688.44 → 693.98] actually get it was uh probably the first kind of major open source contribution that I ever made
[693.98 → 701.40] um before that I've been limited to kind of you know uh minor bug fixes or just kind of pointing out
[701.40 → 708.48] uh spelling mistakes and whatnot but yeah um so lateen our CEO I think was the one that um
[708.48 → 718.02] was looking at uh the get it repo, and he saw the open uh issue that chad had
[718.02 → 723.40] created about finding a new payment processor because he'd uh he was getting kicked off stripe
[723.40 → 727.88] he'd just been picked off I think it was a samurai payments or something like that I can't remember
[727.88 → 734.38] exactly um but yeah so he saw the issue, and he was like well you know this is a great way for us to
[734.38 → 740.68] make an impact and help out um so we did exactly that we jumped in and um I think it took me about
[740.68 → 746.46] two days of writing some code and uh creating a pull request and uh chad was really appreciative
[746.46 → 751.50] of it and uh we just worked with him to get everything working didn't take long and uh yeah
[751.50 → 760.12] he was uh processing within a week um so that was cool, and so we do the same thing with uh all our
[760.12 → 768.20] repos now uh sorry we don't like to help everyone but um you know we are um if anyone's having integration
[768.20 → 775.30] problems with anything where um our support guys are really uh react uh proactive and whatnot in
[775.30 → 780.56] terms of jumping in, and you know helping write snippets and showing people how it's done um I find the
[780.56 → 786.86] whole open source thing really fun and satisfying as an engineer it's um you know I mean it's like a
[786.86 → 794.42] awesome uh CV stuffer um and just having people use your code and uh you know being able to discuss
[794.42 → 802.26] it with them and stuff so did you say CD stuffer CV sorry CV okay CV I was like CD stuffer is that
[802.26 → 809.48] like swag okay so it's crazy the one thing that, so obviously the dashboard is the most popular
[809.48 → 815.04] open source project you guys have um but the thing that's interesting to me is all these client libraries
[815.04 → 822.00] you have typically you'll see with a lot of our guests just because of the community we're in we'll
[822.00 → 827.96] see ruby, and then we'll see python JavaScript kind of you sometimes know and then that's usually just
[827.96 → 834.26] about it right but balanced has python ruby java PHP JavaScript c sharp node like all these different
[834.26 → 838.78] you have your iOS uh wrappers so all these different like libraries for different clients
[838.78 → 843.74] well kind of what why did you guys decide just to go ahead and do it for all of them and uh
[843.74 → 849.96] and what do you think is the uh in your what do you see as the most uh popular one so far
[849.96 → 857.26] um so the I mean the ruby client's the most popular for sure um probably followed by the PHP but um
[857.26 → 863.94] the interesting thing is that we didn't write all those clients um the node client specifically I think
[863.94 → 870.66] maybe three or four customers uh wrote their own versions of the node client and at some point we
[870.66 → 877.50] were like wow we have to we have to jump in and help uh you know and choose an official one and um
[877.50 → 883.80] really put some weight behind it, so people stop reinventing the wheel um so I don't think we wrote
[883.80 → 889.40] the first version of the node client we adopted someone else's that they'd uh published on GitHub and
[889.40 → 896.66] uh basically brought it into the fold and yeah uh help, help them build it out and take it on ourselves
[896.66 → 902.76] and uh I think there's a new revision of the node client coming in again uh we're not building that but
[902.76 → 908.94] someone else is building it so you guys are kind of just like bringing it into your uh organization
[908.94 → 915.16] on GitHub and offering kind of your support for it more than anything um yeah so I mean people
[915.16 → 922.72] like have no problem with creating the initial client but um then a lot of the hard work comes in
[922.72 → 929.82] writing all the code snippets and samples for the documentation um so we tend to do a lot of that
[929.82 → 936.30] um or at least laid the groundwork for it um so it's uniform with everything else that we provide
[936.30 → 943.40] um yeah so speaking of documentation which is also open source to all of your documentation
[943.40 → 948.84] um how often do people contribute to that that kind of your that kind of repository like how often do
[948.84 → 959.24] people other than your company work on the documentation um it depends on the level of the uh the size of
[959.24 → 967.56] the task that needs to be done uh you know typos and stuff we get requests every day for them uh
[967.56 → 973.30] then you know it yeah so it depends on the size of the task if there's a task that's going to take
[973.30 → 980.08] someone several hours to complete it's uh it's not going to be as contributed as often as you know
[980.08 → 985.78] a typo or something will be um it's hard it's hard to give you exact stats to be honest but I'm sure
[985.78 → 992.68] you could uh just look at the stats page on GitHub very near the repos to see them uh actually our
[992.68 → 998.94] websites are open source as well that's probably one of the more uh popular repos that tends to get
[998.94 → 1003.92] updated just randomly so we have all these different things that are open source we could obviously spend
[1003.92 → 1009.08] days just talking about how many open source projects you guys have but let's kind of dig down
[1009.08 → 1014.26] into what's probably the most popular which is the dashboard right so um why don't you what is the
[1014.26 → 1020.88] balanced dashboard what like what part of balanced is in the dashboard and what is it right
[1020.88 → 1027.76] so the dashboard's just another client like the node client or the python ruby client um the difference
[1027.76 → 1034.92] is that it displays everything to you in a browser but yeah that's that's all it is it's an it lets you
[1034.92 → 1039.60] create transactions the same as you could through any client lets you uh view and list transactions
[1039.60 → 1047.46] same as you could through any client um so we host if it's available at dashboard.balancepayments.com
[1047.46 → 1054.62] you can see it up there and running um it's at ember JS application so originally we started with a python
[1054.62 → 1061.10] app and the issue with the python app was that it was a bit slow because all the requests are made in
[1061.10 → 1068.62] serial uh so moving to ember, and you know to JavaScript where everything's an async request basically
[1068.62 → 1076.94] sped everything up uh for free without any major re-architecting of anything um yeah so
[1076.94 → 1082.22] i I'm just kind of I feel like I'm overwhelmed with all the different things we can talk about
[1082.22 → 1089.32] here with balanced um billy it is a recurring billing system what point and which so balance started you
[1089.32 → 1093.42] said it was pound pay which is one thing we can get into with the coma here that's another I think
[1093.42 → 1098.36] you guys might be the first company we've had on and correct me if I'm wrong Adam because I wasn't
[1098.36 → 1102.14] here in the beginning but have we had anyone that was that started at Y Combinator on the changelog
[1102.14 → 1108.62] I'm sure yeah uh whether they mentioned it or I don't know I don't keep a list of the alumni but
[1108.62 → 1113.44] yeah so we can maybe let's talk about that I'm not sure if you were there when it happened but
[1113.44 → 1119.12] uh first let's talk about billy this is at some point at balance you guys decided the marketplace is
[1119.12 → 1125.18] cool, but we want to support uh recurring billing so give it what is billy and when did the
[1125.18 → 1132.16] business decision happen to start supporting this um so like most of the features that we
[1132.16 → 1139.88] tend to develop uh there was a lot of uh demand on GitHub so we have a balanced API repo on GitHub
[1139.88 → 1147.88] which basically documents and talks about uh just balanced in general and so you know people are free
[1147.88 → 1153.62] to create issues up there, and you know popular example of issues are like ACH debits international
[1153.62 → 1160.42] payments recurring billing right, and so we've knocked off ACH debits we haven't done international
[1160.42 → 1166.68] yet, but we started working on recurring billing after we got about a billion requests for it
[1166.68 → 1175.46] um and so billy is basically just you know it's a cron job essentially um I guess the main difference
[1175.46 → 1181.12] that you'd see between it and like something like charge which you mentioned earlier is that
[1181.12 → 1187.26] billy just hooks into the balanced API so again it's another client right so doesn't have any special
[1187.26 → 1193.80] access that anyone else doesn't have to that balanced API and what it does is it lets you
[1193.80 → 1202.50] do both the credit and the debit side of things as a recurring job so you could uh schedule charging
[1202.50 → 1211.32] cards, but you can also schedule paying people out right um and we took guidance on that by just asking
[1211.32 → 1217.60] feedback from customers you know uh for existing customers how would you use it you know what features
[1217.60 → 1224.60] must it have in order for you to uh start using it and so chad from get it was one of the people that
[1224.60 → 1230.44] kind of jumped in on the uh issues for the repository, and he was like this is my use case, and it's like
[1230.44 → 1236.64] right okay so now we've got a concrete use case we can sit down and make sure that we satisfy that
[1236.64 → 1244.24] use case as part of the development process uh billy's interesting actually the lead engineer on that's
[1244.24 → 1251.36] based in Taiwan so he's you know another one of these guys that kind of just started contributing to it
[1251.36 → 1259.24] and eventually we uh started bringing him into balanced um and interestingly just to diverge a bit
[1259.24 → 1267.20] uh same thing with uh the iOS and the android clients uh Ben who's uh one of our he's uh
[1267.20 → 1275.70] uh sorry he's like the support engineer and IRC that helps everyone get integrated um he came to us
[1275.70 → 1283.86] again through you know just doing little uh pull requests and stuff on different parts of our open
[1283.86 → 1290.90] source projects and after a while we were like man this guy's like super talented super useful uh
[1290.90 → 1296.50] time to hire him yeah yeah exactly we sent him a t-shirt and uh just kind of got a conversation
[1296.50 → 1302.70] started and then next thing you know he's working for us uh so he works out of Utah, and he's uh in our
[1302.70 → 1308.12] chat room every day conversing with us and doing everything that needs to be done on uh on the
[1308.12 → 1314.34] billy repo and the README you say in beta stage use it at your own risk does anybody ever uh I mean
[1314.34 → 1319.16] open source you tend to have some squawkers out there so anybody open up an issue like whoa this
[1319.16 → 1328.28] doesn't work, or you know anything bad happen uh no horror stories so um part of what we're
[1328.28 → 1334.12] doing like you say it's in beta at the moment I wouldn't call it a mature product at all um so
[1334.12 → 1341.32] we're actually ripping out that invoicing out of the core of balanced at the moment and implementing
[1341.32 → 1349.02] it in billy um to ensure you know I think between GDP and ourselves if it can handle that can handle
[1349.02 → 1354.74] pretty much anything we've got some uh reasonably complex invoicing uh logic that we need to deal with
[1354.74 → 1362.60] so how much of balanced is closed and how much is open like what we're looking at the code here for
[1362.60 → 1367.72] the dashboard and billy and the docs and the website and all that how much of the secret sauce do you
[1367.72 → 1374.70] keep hidden um so at the moment to be honest like a lot of the code is closed uh we've built some
[1374.70 → 1382.02] really nice frameworks on top of flask and sequel alchemy uh which we use to implement balance
[1382.02 → 1389.56] um but the reason for them being closed is only a lack of time to actually implement them uh to
[1389.56 → 1395.18] expose them to the world I've found it's a lot easier to begin a project when as an open source
[1395.18 → 1401.12] project than it is to take a closed project and turn it into an open source project if only because
[1401.12 → 1407.40] you have to go through and remove all the swear words and profanity the comments yeah right well plus
[1407.40 → 1411.90] I mean it's got to be a hit to your business too I mean sure you're you're supportive of open
[1411.90 → 1420.14] source and supportive of the community, but it's got to take a hit to people's time and just lack
[1420.14 → 1424.94] of burnout I guess to have to put everything out there in the open because when especially as you
[1424.94 → 1431.12] gain more and more uh popularity over time you know it only affects your ability to support the
[1431.12 → 1439.50] community too to have to put everything out there uh I'm I don't know um I mean the reason why I say
[1439.50 → 1444.58] that is because um you know we've Andrew you and I've talked to people on the show recently that they've
[1444.58 → 1450.60] experienced burnout we talked about uh node.j's maintainer original maintainer uh Ryan doll you know
[1450.60 → 1458.78] burnout there, and it just eventually comes to play if you have to you know I guess build your business
[1458.78 → 1463.68] on top of open source but also support what you've put out there to just put into the ecosystem of
[1463.68 → 1469.42] open source to either better for you or for the world yeah we like not surprisingly we've had a
[1469.42 → 1474.12] couple of people recently that said their call to arms like the thing they would like the community to
[1474.12 → 1479.82] help out with is just like responding to issues just somebody that you know just being an issue i
[1479.82 → 1485.08] forget what the word the terminology is maybe an issue secretary or something like yeah just they
[1485.08 → 1489.84] they've got all this which is something interesting you guys have so many projects out there do you
[1489.84 → 1496.34] have somebody specifically you know dedicated to each project or like if is a bunch of issues start
[1496.34 → 1500.56] cropping up on all the different projects then what do you guys how do you respond to them like how do
[1500.56 → 1507.10] you make sure you respond to all of them in a timely fashion uh to be honest I don't think we have
[1507.10 → 1516.84] a formal process um obviously you know bugs where things are actually broken get top priority um but
[1516.84 → 1523.24] discussion can stay discussion until we have a concrete solution for things um I mean you're right
[1523.24 → 1529.76] it does there is are people who are spending a lot of time like managing the dashboard just in
[1529.76 → 1535.92] terms of like merging pull requests uh for a lot of the smaller pull requests you have to sit there and
[1535.92 → 1542.02] kind of um and ah do I need to go back to the sky and ask him to re-architect this piece of code or
[1542.02 → 1548.44] will it be just quicker for me to make the change and then merge it in myself um but yeah I don't think
[1548.44 → 1553.72] we've got any formal process for that at the moment it's just kind of a case of failing it out as the
[1553.72 → 1564.90] project grows um yeah I guess since we're on the subject um you've got 146 open issues on balanced uh on the
[1564.90 → 1569.60] balanced dashboard right now and just a small handful on billy so I mean you say you don't have a formal
[1569.60 → 1575.78] process what is then the process to either handle close out settle respond to whatever you
[1575.78 → 1585.12] want to call it these issues on balanced dashboard um so for the balanced API periodically
[1585.12 → 1594.60] we go through and uh just figure out which issues uh still open you know occasionally we'll change the
[1594.60 → 1600.62] API in such a way that you know issues are no longer relevant um so that that'll happen every couple of
[1600.62 → 1608.80] months um but any anything that needs to be dealt with uh that's going to take a long time and needs to
[1608.80 → 1614.58] be done internally generally we'll bring it into Trello uh which is what we use internally for managing work
[1614.58 → 1623.00] and that if it comes into Trello then generally it's got an engineer internally focused on it uh
[1623.00 → 1628.04] if it's not in Trello then that means that there's nobody internally tasked to doing it
[1628.04 → 1633.62] I almost feel like there's been a couple of people on the show Andrew that mentioned Trello almost like
[1633.62 → 1638.74] there's going to be something to start uh synchronizing GitHub issues to Trello somehow you know
[1638.74 → 1644.40] yeah this it's gotta happen I'm sure it's out there we actually started to write one at
[1644.40 → 1650.82] some point uh there you go, but we felt like it was going to be an it was a smell that we were
[1650.82 → 1656.94] potentially doing something wrong uh I think for the majority of tasks they should either live
[1656.94 → 1663.14] in GitHub, or they should live in Trello if you're just mirroring one with the other uh something
[1663.14 → 1669.02] something doesn't sound right there yeah let's talk about your you brought up the balanced API
[1669.02 → 1674.72] you told me that you recently switched from Markdown to uh like Jason so kind of talk about that
[1674.72 → 1683.38] right so Jason API is a basically a schema format I guess you would call it uh so it's kind of like an
[1683.38 → 1690.94] XSD um, and it lets you basically say this is what the response or a request for a certain endpoint
[1690.94 → 1698.48] should look like um so originally what we did is we wrote everything in Markdown and then the next
[1698.48 → 1703.20] step was for us to go through and annotate our code base so that we had a tool which generated the
[1703.20 → 1708.90] markdown and that um solved a bunch of issues for us with you know documentation and
[1708.90 → 1717.48] specifications getting out of sync um, but it was still possible for us to break our uh API interface
[1717.48 → 1724.12] unintentionally uh so the great thing about Jason API is that you can make a request and then you
[1724.12 → 1731.54] can compare it against the Jason API schema and be like does it validate yes or no right so this
[1731.54 → 1737.30] has been a pretty big win for us uh in terms of having a lot more certainty about when things change
[1737.30 → 1745.70] uh which is definitely the main advantage for us so far uh beyond that I mean Jason API has uh other
[1745.70 → 1751.76] technical advantages like the fact that you can have an envelope for your payload so you can uh
[1751.76 → 1756.90] you know return more than one item at a time when you do a get kind of thing you can return related
[1756.90 → 1765.08] resources in the same payload uh and in the current or the uh original revision of the dashboard uh sorry
[1765.08 → 1773.12] the API um we would nest items and that starts to break down as you have like large collections of
[1773.12 → 1780.60] items being returned at the same time gotcha we actually covered Jason API on the blog um I guess
[1780.60 → 1787.22] was that who covered that that was Steve Planck Steve Planck is one of the guys that was helping to
[1787.22 → 1793.52] work on it right that's right yeah he uh he wrote a post called Jason API uh I guess Jason API however you
[1793.52 → 1800.66] want to pronounce it uh has a mime type, and he talked about how he and Yehuda have been uh, uh pursuing to
[1800.66 → 1806.94] help standardize the API and this was something that came out of their work on ember data and
[1806.94 → 1811.44] active model serialized so it's something he covered on the changelog we actually have a tag on the blog
[1811.44 → 1817.68] that's I think it's just uh you know Jason dash API so if you follow our tag on the changelog you can
[1817.68 → 1822.74] kind of watch that I'm sure Steve will cover more as well yeah so it's its cool to actually see
[1822.74 → 1826.94] things like that become implemented so you said that was a big win for you guys when you how long did it
[1826.94 → 1833.76] take to kind of make that switch and uh I mean have you it's been a month now since the switch
[1833.76 → 1843.24] happened is that right uh no so we deployed the Jason API revision uh maybe two weeks ago um but
[1843.24 → 1849.80] we've still we still maintain the current revision of the API which is just planned Jason uh, and you know
[1849.80 → 1854.50] the vast majority of people are using that we haven't uh finished documenting the Jason API revision
[1854.50 → 1862.82] so uh it's not getting widespread usage but uh yeah interesting I mean we're using so we use ember.js
[1862.82 → 1870.80] for the dashboard uh and when we started implementing the ember as the framework for the dashboard we
[1870.80 → 1879.50] actually initially tried to use ember data and uh we had a horrible time with it um, and so we ended up
[1879.50 → 1885.16] writing our own data layer uh and our own serializes and whatnot, and we're currently in the process of
[1885.16 → 1891.02] uh ripping that out and trying to replace it with ember data and uh we've got a guy in the office who
[1891.02 → 1898.34] just finished writing an ember data Jason API adapter uh to help us with that so hopefully we'll have that
[1898.34 → 1903.38] change in the dashboard very soon uh that'll be one of the first consumers of the new revision
[1903.38 → 1909.58] so you said you wanted to kind of talk about what you guys plan on open sourcing in the
[1909.58 → 1915.92] future is that uh earlier you said it was easier to start with open source than to convert stuff so
[1915.92 → 1920.16] obviously to me that means you're probably going through the process of converting some stuff right
[1920.16 → 1923.48] now but I want to talk about that a little bit what else what's coming in the future from
[1923.48 → 1930.54] balanced uh, so probably the next thing out the door will be uh the framework that we've written on top
[1930.54 → 1939.94] of flask um so we've experimented with a bunch of uh libraries that were designed to make building
[1939.94 → 1947.24] APIs and python easier so we're a python shop uh for the majority of our code, and we experimented with
[1947.24 → 1955.22] a bunch of them but uh didn't really find any that clicked for us um so we started from scratch
[1955.22 → 1961.12] just using flask, and we've built up on top of that uh over the last kind of year and a half or two
[1961.12 → 1967.76] years and what we've got now is pretty polished so I don't know what name that's going to be
[1967.76 → 1974.10] launched under you'll probably be looking out for a project called hype or lube um but yeah that's i
[1974.10 → 1979.42] think that's going to be really powerful for people that want to write uh APIs in python um
[1979.42 → 1984.38] that's can you say those names again one more time hype h-y-p-e
[1984.38 → 1997.64] or lube l-o-o-b oh l-0-0-0-b internally nice, so flask is and I'm not sure are you familiar with
[1997.64 → 2003.68] Sinatra in ruby uh vaguely I mean I dabbled in ruby i I wouldn't say I'm like strong in it
[2003.68 → 2008.52] gotcha I think flask has been compared I'm not familiar with flask I've never actually used it but i
[2008.52 → 2014.72] think flask has been compared to Sinatra and um Rena rails obviously gets compared to Django so i
[2014.72 → 2019.32] was wondering if the one you guys are working on is kind of the pairing-esque uh version of the
[2019.32 → 2025.30] uh python but yeah I guess we will have to find that out somewhere else I'm going to put a link to
[2025.30 → 2030.12] flask in the show notes too so if you're listening to this check out the show notes um, and we'll have
[2030.12 → 2034.10] a link to flask and a bunch of other stuff we're talking about on the show too so what's a yeah
[2034.10 → 2041.00] what's a day in the life of a balanced developer look like uh hectic at the moment uh we're super
[2041.00 → 2049.22] we're super busy um but yeah I mean so for me uh I spend a lot of time just managing uh you know
[2049.22 → 2059.12] issues and stuff on GitHub um and then depending on the different engineers I mean just working on
[2059.12 → 2064.42] static sites but the majority of the stuff we do is you know accounting and payments based so
[2064.42 → 2072.50] we spend a lot of time integrating uh other banks and uh I believe martin our CEO uh describes it most
[2072.50 → 2080.36] succinctly when he calls it abstracting the shit away so we provide you with a nice API uh when
[2080.36 → 2087.24] really underneath you know it's dealing with ftp servers and file formats that are 20 years out of date
[2087.24 → 2090.54] uh no, thanks
[2090.54 → 2100.90] so it's kind of hectic how where is your team located you said you had one guy in Utah where is
[2100.90 → 2104.88] the uh where is the rest of the team located you guys are pretty new you've only been around for
[2104.88 → 2112.22] about a year in this format right as balanced yes uh just over a year um originally the office was
[2112.22 → 2116.50] in San Francisco then it moved down to Palo auto now it's back up in uh San Francisco
[2116.50 → 2123.24] and soma um so that's that's where the majority of us are but yeah like you said Ben's in Utah
[2123.24 → 2129.62] and then we've got a guy in Taiwan uh i myself started off in Singapore and worked remotely from
[2129.62 → 2137.06] there for a while before making the jump over to the U.S. so you talked about just different I guess
[2137.06 → 2142.10] competitors I guess that's probably the easiest way to talk about it um a little earlier in the show
[2142.10 → 2148.08] like what are some of this the hurdles in the way of balanced payments you know we've got
[2148.08 → 2154.28] the big guys like PayPal which almost every developer is pretty much against these days I think
[2154.28 → 2158.52] they're trying to win us back but you guys stripe, and then you've got a number of others that
[2158.52 → 2164.88] have propped up like what is it that is the hurdle for you guys in terms of doing your mission in
[2164.88 → 2176.00] payments uh it's a great question I don't know to be honest um I mean we're just strapped for time at
[2176.00 → 2180.68] the moment uh from an engineering point of view you always want more hours in the day
[2180.68 → 2188.98] um so you can see that it's pervasive in a lot of uh the solutions that we build uh we're very heavy
[2188.98 → 2195.62] on automation and stuff um simply because with a small team of engineers I mean I think stripes
[2195.62 → 2201.88] got like 40 engineers where we've got five uh don't quote me on the exact numbers there but
[2201.88 → 2208.12] that's that's the ballpark anyway um you know we have to make sure that everything we write
[2208.12 → 2215.34] is really robust um, and you know you only want to solve a problem once if you can help it because
[2215.34 → 2221.00] if you have to keep coming back and solving the same problems over and over it's uh it's definitely
[2221.00 → 2227.52] not going to scale when you've got a small team you guys are I think just on the note of mentioning
[2227.52 → 2231.56] how many engineers you have I think you're also looking to right this would be a good time to
[2231.56 → 2239.24] mention to the world who and what yeah I mean we're looking for smart engineers primarily uh we don't
[2239.24 → 2246.50] we don't care what languages you know, or you don't know um from the people that I've interviewed so
[2246.50 → 2253.06] far I've found that people that are good problem solvers are infinitely more useful than people that
[2253.06 → 2261.54] uh python pros, or you know perfect in a certain language um I quickly threw together a little teaser
[2261.54 → 2271.02] if anyone wants to give it a go you can find it at a just.GitHub.com slash MJ all day when we've
[2271.02 → 2277.40] created a small hangman client if anyone wants to try their hand at writing an uh restful client that
[2277.40 → 2283.36] can consume this hangman app uh and show us what you've got I'd love to see it yeah we're going to link
[2283.36 → 2288.74] out to the show it's kind of neat you got uh you're curling the balanced hangman Heroku app I think
[2288.74 → 2294.52] yeah that on Heroku race you guys are probably hands up fans of Heroku i suppose uh I mean
[2294.52 → 2301.02] if you want to throw a service up in half an hour um then that's the way to go for sure right um we
[2301.02 → 2307.14] we host like our example marketplaces so we've got a couple of open source marketplaces that you can
[2307.14 → 2311.94] see on our GitHub again you know uh they're all called rent my bike, and then they're implemented in
[2311.94 → 2317.44] different languages, and they get hosted on Heroku just because it's so simple to get something up and
[2317.44 → 2322.10] running really quickly so for I guess for that person that might be listening I don't want to
[2322.10 → 2326.40] drag out the hire too much longer but I just want to give you a final call arms on that one is uh
[2326.40 → 2331.02] what is it about balance that makes you love being there and why would somebody want to join the team
[2331.02 → 2338.92] um so for me, I love hard problems like I was saying before I got uh I pivoted into social media marketing
[2338.92 → 2346.80] and selling makeup to people just doesn't float my boat but here I'm solving like what I consider to
[2346.80 → 2351.80] be hard problems because if I send someone a hundred dollars too much or I don't send them a hundred
[2351.80 → 2357.20] dollars somebody's going to come looking for me and let me know um you know there's a real world consequence
[2357.20 → 2363.58] when you're moving money around and I think just having that challenge over your head is uh it's really fun
[2363.58 → 2370.94] um so yeah I mean the people that we want would thrive in that kind of environment you know um
[2370.94 → 2379.42] trying to do zero downtime migrations if we go down then our clients go down and so this kind of
[2379.42 → 2384.26] constraints like real world side effects to everything that you do and that kind of high
[2384.26 → 2390.40] pressure environment I just find super exciting to work in yeah I mean it's an environment that
[2390.40 → 2398.38] definitely it if you enjoy I don't know we ask our kind of our set three questions at the end of
[2398.38 → 2404.78] every episode and if you enjoy doing like seeing real world things right that like we're developers
[2404.78 → 2409.92] and we have the tendency as developers to work on websites which most like most of what you're
[2409.92 → 2413.42] talking about social media marketing that's what you did right so what you did when you were
[2413.42 → 2417.58] doing that is all web-based right and the ROIs and all your measurements and all your analytics and
[2417.58 → 2421.96] stuff that's that's all you're just measuring web-based stuff that you're providing other people
[2421.96 → 2427.86] to be more successful with their brick and mortar with their real hands-on things you know so if
[2427.86 → 2434.02] you're dealing with money that's one of the things that as a developer you can um you can spend a lot
[2434.02 → 2439.16] of time and know that what you're doing is actually affecting and contributing to a real
[2439.16 → 2445.32] life hands-on problem so in my career when I found myself on at different jobs working on financial
[2445.32 → 2449.44] aspects I've enjoyed it because of that I think it gives you that little edge that a lot of
[2449.44 → 2455.70] times you don't get absolutely so as I mentioned we ask the same questions at the end of every episode
[2455.70 → 2461.26] um so we'll go ahead and ask you now the first one is for a call to arms so you guys have so many
[2461.26 → 2467.26] I'm almost afraid to ask you guys have so many projects out there um so don't open the uh the fire
[2467.26 → 2471.04] hose on us but kind of give us a call to arms of what you'd like to see the community help out with
[2471.04 → 2477.94] um yeah like you said any open GitHub issue that can be closed off uh is a big win in my book
[2477.94 → 2484.82] um I think the most interesting thing that uh someone could start on today if they wanted to
[2484.82 → 2489.26] give it a go would be to convert our current python client to consume the Jason API revision
[2489.26 → 2495.04] um I think that's going to be a lot of fun to try and figure out uh I don't know if there's like a
[2495.04 → 2502.00] a canonical Jason API python client at the moment so we could definitely do something with that
[2502.00 → 2509.28] awesome so you heard it you can forever be etched in python glory if you are the first to build this
[2509.28 → 2516.26] exactly awesome so if you weren't doing what you're doing now uh what would you be doing i
[2516.26 → 2520.30] got to figure out a better way to ask that question Adam mark that down we need to write it I'll do it
[2520.30 → 2524.70] I'm writing it down now if you weren't doing this what would you be doing uh I'd want to be
[2524.70 → 2530.50] working from a beach in Indonesia somewhere, and you are a world traveller I don't know if we talked
[2530.50 → 2536.82] about it, but you're from New Zealand right and you yep where else have you lived at besides Singapore
[2536.82 → 2543.24] and now San Francisco that's a just the three of them uh and I'm pretty happy here for the moment so
[2543.24 → 2550.20] hopefully I don't have to find another place that I like uh in the near future gotcha so you'd be you'd
[2550.20 → 2555.00] be working on the beach in Indonesia does that mean that you like beaches you like surfing what is it
[2555.00 → 2563.78] about Indonesia oh no it's its just that island lifestyle like um Singapore is such a small country
[2563.78 → 2569.04] that you know if you want a weekend away you end up flying to another country which is your know 10
[2569.04 → 2576.20] minutes by plane or 20 minutes by plane or taking a boat to uh Malaysia or something like that and I had
[2576.20 → 2581.94] some friends that were software engineers and this was their setup right so they were based in
[2581.94 → 2588.84] Singapore but then during the week they would uh go to Indonesia or Malaysia or whatever and they
[2588.84 → 2594.20] would sit on a beach, and they would program and i just always thought that was like a fantastic way
[2594.20 → 2600.26] to work uh if you could is you could withstand the distractions that are around you but yeah i never i
[2600.26 → 2605.40] never quite managed to do it for any prolonged period of time certainly would beat uh go into a
[2605.40 → 2610.76] co-working space or even to a coffee shop when you say Andrew yeah I mean just to kind of throw my
[2610.76 → 2618.86] own uh fuel into the fire a few weeks ago um I was in the outer banks in North Carolina and I just sat
[2618.86 → 2622.78] on the beach and worked at my normal job every day and that was incredible I mean just sitting on the
[2622.78 → 2628.26] beach and in that environment it's like so nice to not be sitting in my office working so I totally am
[2628.26 → 2633.92] with you on that one uh that might be the first time we've heard Indonesia though so yeah I think so
[2633.92 → 2639.08] cool though but then the last question that we like to ask is for a programmer hero so somebody
[2639.08 → 2646.98] uh in your life that has been influential uh so in terms of programming I don't have any heroes uh
[2646.98 → 2652.56] i I try to be as sponge-like as possible and just soak up what I consider to be the good bits of
[2652.56 → 2659.62] everybody but uh in terms of like just general life heroes I definitely appreciate my wife for kind of
[2659.62 → 2665.16] bearing with me is we've done this travel and quitting her job and then finding new jobs every
[2665.16 → 2671.46] time we do move around so definitely her gotcha so you heard it here first Marshall would be a sponge
[2671.46 → 2679.60] on the beach if you had the chance exactly your crazy man so that's uh I guess that's the show huh
[2679.60 → 2684.88] I mean uh all three questions we got pretty much everything we can get out uh everything we can get
[2684.88 → 2689.80] out of you Marshall, so the thing is balanced is an open company so it's there's so much information
[2689.80 → 2694.96] that's out there if you know i I have a feeling that the amount of time Marshall just spent with
[2694.96 → 2698.56] us he'd be willing to spend with you if you just wanted to ask him about the company because their
[2698.56 → 2704.54] their mindset is to give so much back into the community that there's not much that's hidden so
[2704.54 → 2708.66] I encourage you if you're interested in balance you're interested in payments the next time you start
[2708.66 → 2714.78] to uh I'm not trying to pull uh people away from any other platforms but the next time you sit
[2714.78 → 2719.40] down to make a decision on uh you know payment processing you should check out balance check out
[2719.40 → 2724.44] the company and see if they fit for you for sure yeah I recommend uh people either open an issue on
[2724.44 → 2732.38] GitHub if they've got a technical uh issue or jump on irc.freenode.net and hash balanced where
[2732.38 → 2738.04] most of the engineers in the company are always idling and happy to talk about anything that anybody
[2738.04 → 2742.06] would like to know that's cool to see that feedback too I mean that's that's something
[2742.06 → 2747.40] we mentioned digital ocean too just kind of mentioned uh you know meshing yourself into the
[2747.40 → 2752.92] community and kind of being there to hear you know that that kind of real-time feedback too like if
[2752.92 → 2757.42] you've got questions hop in IRC we'll taunt you we're there waiting for you basically yeah we try and
[2757.42 → 2765.96] be responsive uh 20 hours a day I don't know if we get to 24, but we get close let me try well all right uh
[2765.96 → 2769.88] yeah Marshall thank you so much for taking the time to come on the show today it's certainly been
[2769.88 → 2775.58] a blast chatting with you about uh just open source open products how you guys are building balanced and
[2775.58 → 2779.68] what it is that you love about your job there and why somebody should come and work with you if they
[2779.68 → 2785.40] are uh are in the mood to do something like that so uh I want to give a quick shout out again to our
[2785.40 → 2790.88] sponsor for the show digital ocean uh deploy your SSD cloud server today at digital ocean.com you can use
[2790.88 → 2797.52] our promo code it's um a new one so if you listen to the past few shows that uh that will still work
[2797.52 → 2803.14] I believe, but this is the new code we're promoting for the next month and that code is the changelog
[2803.14 → 2808.76] October so use that when you sign up there's a little promo code field pop that in there and click
[2808.76 → 2814.22] save, and you'll be good to go to save 10 bucks when you sign up for digital ocean and Andrew you
[2814.22 → 2818.54] mentioned getting a t-shirt so I'm not sure if they're sending t-shirts but if you do want to
[2818.54 → 2824.84] decorate your laptop you can email Barry at digital ocean.com to get some free uh stickers
[2824.84 → 2828.66] and other stuff I'm not sure what they're sending out but just email Barry tell me your
[2828.66 → 2832.64] tell me your mailing address, and he's going to send you some awesome digital ocean stuff so if you're
[2832.64 → 2840.28] a fan of digital ocean uh do that that's uh that's it for this show uh Marshall again thank you
[2840.28 → 2844.54] Andrew thank you for teeing this one up and for you the listener for listening but the let's say goodbye
[2844.54 → 2846.78] thanks guys I really appreciate it
[2846.78 → 2860.96] so
[2860.96 → 2890.94] We'll be right back.
