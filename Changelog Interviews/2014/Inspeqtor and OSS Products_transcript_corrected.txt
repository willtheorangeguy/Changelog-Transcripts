[0.00 → 14.46] welcome back everyone this is the changelog and I'm your host Adam stekowiak this is episode
[14.46 → 21.34] 130 jarred and I talked to mike par ham he's back again just like sidekick he's got inspector now
[21.34 → 28.48] another open source slash pro version of software out there for you to use this one is application
[28.48 → 33.20] infrastructure monitoring reimagined it's called inspector now let me talk about that we also
[33.20 → 38.60] talked about other fun ways he's making money as an open source developer so great conversation there
[38.60 → 44.96] we've got some awesome sponsors for this show code ship hired.com and digital ocean we'll tell
[44.96 → 49.90] you a bit more about hired.com and digital ocean later in the show but our friends at code ship
[49.90 → 54.62] is a hosted continuous deployment service that just works you can easily set up continuous
[54.62 → 59.34] integration for your application in just a few steps and automatically deploy all your code
[59.34 → 64.80] when your tests pass code ship has great support for lots of languages test frameworks as well as
[64.80 → 69.84] notification services they integrate with GitHub and Bitbucket and can deploy your code to cloud
[69.84 → 76.72] services like Heroku AWS notice google app engine or even your own servers' setup takes just three
[76.72 → 82.52] minutes get started today with their free plan and make sure you use our code the changelog podcast
[82.52 → 89.66] again that code is the changelog podcast, and you will get a 20 discount for three months on any
[89.66 → 94.10] plan you choose head to codeship.io and now on to the show
[94.10 → 102.34] welcome back everyone we're uh we're joined here with a guest that's no uh stranger to the show mike
[102.34 → 107.32] parameter and mike you're also not a stranger to the changelog we've covered all sorts of stuff that you've
[107.32 → 114.20] done over the years everything from dolly to sidekick to launch yum launch lunch I'm not sure
[114.20 → 119.98] if i which it's launchy I think we pronounce it's spelled launch though right yeah it is yeah
[119.98 → 126.76] there's already a gym called launch so I couldn't, I couldn't squat on that name right so I'm here Mike's
[126.76 → 133.86] here jarred's here jarred say hello hey we uh we've been waiting to I think maybe about a month or two to
[133.86 → 138.32] to have this conversation you've been working on something brand new so maybe the best way to start
[138.32 → 144.40] would be to just you know get you know tell us what's going on what you do brand now sure um for
[144.40 → 148.46] the last four months I've been working on a top secret project uh which I just announced yesterday
[148.46 → 156.68] and it's called inspector um it's my fresh take on application infrastructure monitoring
[156.68 → 164.40] uh that is to say all the moving parts of a server-side application um a little tool which
[164.40 → 169.54] allows you to monitor all those moving parts to make sure everything is healthy and if anything
[169.54 → 177.10] looks out of the ordinary inspector will immediately send out alerts to uh to where you wherever you have
[177.10 → 184.82] configured to say hey this doesn't look right uh so it's really helpful in terms of uh just you don't
[184.82 → 189.86] have to watch a dashboard all day or something like that you just you know watch your inbox and
[189.86 → 197.52] and if something shows up that then you know to investigate, so inspector comes into a space that's
[197.52 → 203.38] you know has uh some offerings I think you're no stranger to that as sidekick of course famously um
[203.38 → 211.78] was you know rescue um you know done right or done better um inspector has competition with
[211.78 → 220.70] Mont with god with uh what's the python one um uh supervisor d yeah, so there are a few others
[220.70 → 226.98] blue pill was one I was thinking of, so there's there are other players in this space what's inspector's
[226.98 → 233.04] unique take and what does the value add there right so you know if you know anything about Mont
[233.04 → 241.32] uh it's its pretty obvious that Mont is the main yeah um the main influence in the way
[241.32 → 247.10] inspector works uh I've used Mont for the last five years and I've just always been frustrated
[247.10 → 252.64] with some of its quirks, and so i I really wanted to build for the last few years I really wanted to
[252.64 → 260.76] build something that was like sort of Mont plus or my take on Mont and so as i
[260.76 → 264.62] really got serious about doing this a few months ago i I really started looking at the Mont feature
[264.62 → 272.22] set and just sort of what did I want uh in terms of um you know my previous job was
[272.22 → 277.98] director of infrastructure or director of technical operations whatever you want to call it
[277.98 → 283.18] but basically if the site had problems i I was the guy who had to whose head was on the line
[283.18 → 291.54] um so this kind of tool uh was critical for my job I had to know when something was acting up
[291.54 → 299.38] uh so, so yeah I mean I went through uh monit's feature set and pared down all the different
[299.38 → 304.72] features that I thought were not useful uh from an application monitoring point of view
[304.72 → 312.98] and added new features that I thought were critical that Mont didn't have and so that's that's what
[312.98 → 321.20] became inspector um inspector has made some interesting choices in terms of its design that some people
[321.20 → 328.76] aren't going to necessarily like for instance well it doesn't monitor unit d legacy unit d services
[328.76 → 336.00] really and that's by choice um part of application monitoring is I'm trying to
[336.68 → 342.92] guide people on how to build a reliable application right inspector is going to tell you if something is
[342.92 → 350.74] not, not working reliably, but it also wants to guide you to build better applications
[350.74 → 357.48] and part of that is using a proper modern unit system like upstart like system like run it
[357.48 → 366.82] and so uh unit d one of the problems with unit d is you there's no sort of central demon that you can
[366.82 → 374.48] query for the status of a process or a service um and everything's kind of rolled into this just big
[374.48 → 381.24] hairy bash script in Etsy and Etsy and so when I realized this a couple of months ago I realized that
[381.24 → 386.80] this was a sort of a decision point in the design here that was going to be fundamental to the way
[386.80 → 396.36] inspector works so do I want to support this legacy um ball of mud or do I want to make a hard stop here
[396.36 → 405.36] and ask people hey or guide people or try to educate people about why this is a problem and and and it's not that
[405.36 → 412.80] hard to learn the new systems and thereby get a more reliable uh setup for your application components
[412.80 → 420.34] so that's that's kind of what I did I was going to say the um so just to kind of give the listeners
[420.34 → 424.90] who listen to this to kind of maybe a outline of what we think this show might be about this time
[424.90 → 430.28] uh in traditional fashion of the changelog we want to go deep we want to figure out all the details of
[430.28 → 435.06] inspector but I think a neat part of this transition for you which you had said this you didn't want
[435.06 → 439.80] to um you had to make a choice of uh supporting that ball of what was your word
[439.80 → 448.86] ball of mud um so you had to make this choice of doing that or something else and um episode 92
[448.86 → 454.16] we had you on talking about sidekick you had some success with side sidekick pros so for the listener's
[454.16 → 458.74] sake what we want to do is we want to talk deeply obviously about the insides and the innards so to
[458.74 → 465.08] speak of inspector and what you did there but specifically you've seemed to hit this um the nail
[465.08 → 470.96] in the head so to speak of success when it comes to delivering open source the right way but also
[470.96 → 477.44] making a living because you've got your wife you've got uh you've got a beautiful uh little boy a furry
[477.44 → 484.12] cat to take care of you know it's not just mike everybody Mike's Mike's mike, but he's got you know
[484.12 → 489.60] family you know so you got to make money, and you found this really cool way to do this so can you
[489.60 → 496.34] take us through some of the journey to kind of get to uh making the choice of supporting that uh ball
[496.34 → 506.78] of mud or not sure um yeah I mean at this point in my career um I love writing open source but I'm also
[506.78 → 514.88] i I've also had to make the decision that I'm not a charity um that I'm an experienced engineer and
[514.88 → 522.12] part of that experience is that I write um ideally i I have the experience to make
[522.12 → 533.42] well-designed software um reliable software so um I have to um i I've decided to have a business model
[533.42 → 539.16] where I have both an open source product and a commercial product on top of that that open source
[539.16 → 547.08] core and that that commercial product is closed source and you know of course there's
[547.08 → 553.40] some people that really don't like this model but I think uh by and large everybody understands that
[553.40 → 558.72] people have to make a living and I can either work for a corporation that is paying me a salary
[558.72 → 564.96] to work on full-time open source or I can do it on my own um there's a lot of different business
[564.96 → 570.40] models you can have of course um yeah oh another popular one is to have services so you do
[570.40 → 578.08] consulting for your product um I think this the sense guys do that um they do some sense I think is
[578.08 → 584.24] some sort of monitoring system uh it's a very complex monitoring system built on top of rabbit me if i
[584.24 → 588.10] recall similar to ROC too they do the same thing where they have a commercial based version and they
[588.10 → 595.66] have support and right it's its a model that is kind of it has its pros and cons too yeah exactly
[595.66 → 601.92] and flexibility maybe be one of them you know where it's a corporation multiple people and again you
[601.92 → 608.28] seem like you're you're uh not a rogue you know lone rogue agent, but you're you know you like doing
[608.28 → 616.46] things the mic way well and I've specifically tried to avoid the type of business where I would need to
[616.46 → 624.18] build this giant thing and have dozens of employees and take on venture funding and all this kind of
[624.18 → 635.52] stuff um I'm I'm more focused on smaller focused tools like sidekick like inspector that uh i I can
[635.52 → 642.24] create a commercial product for I can support it as a single person and make enough money to provide for
[642.24 → 648.94] my family so uh so was yeah contributed systems is one person bootstraps no, no funding at all
[648.94 → 655.66] that's awesome yeah yeah for sure so when you first made this decision back with sidekick
[655.66 → 661.20] was it at conception that you said I'm going to have sidekick and sidekick pro or did you start off
[661.20 → 666.46] saying I'm going to do uh you know a threaded version of rescue, and then it got popular, and then you thought
[666.46 → 673.44] oh I could turn this into a living when I first started out it was more of just a vague notion of
[673.44 → 681.20] well I'm starting my 10th open source project here and I'm going to work on this for another year
[681.20 → 687.50] and uh there go my nights and weekends so how can I actually make some money for this so that I've
[687.50 → 695.36] justified to my wife um so that's why i initially uh just had sidekick it was just the open source
[695.36 → 703.68] product I actually sold commercial licenses for sidekick and that did not bring in a ton of money
[703.68 → 710.16] it brought in it brought in like 1500 or something like that over the course of six months but um it
[710.16 → 714.90] didn't bring in nearly enough to justify my time you know when you when you took all the
[714.90 → 721.60] hours that I was spending on sidekick I was making minimum wage in terms of uh you know right
[721.60 → 727.28] selling licenses right hours to dollars yeah right so you know that's that's when I said
[727.28 → 732.22] okay I've got this sidekick thing it's moderately successful at this point we're six months in
[732.22 → 739.08] why don't I do a commercial product on top of it and sell that for 10 times as much money
[739.08 → 746.36] um and to see if I can get people not, not just to pay you know because their lawyers tell them
[746.36 → 751.78] but because they want to buy actual useful functionality and so that's when I started
[751.78 → 759.16] I spent about a month building a sidekick pro and uh and then started selling it, and you know it is
[759.16 → 765.20] ramped up slowly but surely uh when i first threw it out there and announced it I had no idea if
[765.20 → 770.50] anybody would buy this thing um you know it's a ruby gem people are used to just saying gem install
[770.50 → 778.24] and not having to put in a credit card um, but sales were slow at first, but they've
[778.24 → 785.94] ramped up to the point now where I can, I've got a good income that provides for my family just based
[785.94 → 791.34] on those sales alone so I want to touch on before we move on jarred I want to touch on one thing that
[791.34 → 797.20] the listeners might be thinking about in episode 92 we talked to you um about this very topic here but
[797.20 → 801.06] one question that came up that you don't have to go back into but I just want to at least touch on
[801.06 → 806.92] it quickly which is um you know what's stopping somebody from since it's open source taking side
[806.92 → 811.92] pro psychic pro features and putting them in the open source version um that's sort of a hurdle you
[811.92 → 816.78] had to get over how do you prevent that just a quick note on that it's the show it's I don't prevent
[816.78 → 823.78] it and I have no interest really in preventing it um if somebody wants to reproduce a feature
[823.78 → 831.90] fork sidekick and put it in their own version of sidekick there's legally nothing stopping them
[831.90 → 841.46] from doing that um sidekick itself is LGPL they can fork it, and they can add a feature to it as long
[841.46 → 847.82] as that feature remains open source in their fork they can do whatever they want with it the
[847.82 → 853.50] thing that people are paying for is long-term support they're paying for a roadmap they're paying to know
[853.50 → 859.30] that someone is constantly going to be ensuring that rails 4.2 is going to work with it that rails 5
[859.30 → 866.38] is going to work with it that ruby 2.2 is going to work with it that um they're also paying for taste
[866.38 → 874.90] that i as a project dictator I have the good taste to know which features are good which features will
[874.90 → 882.42] uh add instability to the product um you know that that sort of thing so they're they're paying for
[882.42 → 889.64] the experience and the oversight of the project to continue um so yeah there's nothing legally
[889.64 → 894.76] stopping people from doing that you know just same thing with inspector um if people want to fork
[894.76 → 903.34] inspector it's GPL they can add their own feature which copies it um but again I think I'm here for the
[903.34 → 907.68] long run I'm getting I've got a product which is paying me to support this for the next few years
[907.68 → 912.82] if they just fork it and add a feature are they going to maintain it for the next two years
[912.82 → 918.00] right that's a good point you know are they I'm constantly going to be adding new features to the
[918.00 → 922.84] open source and the commercial version are they going to be constantly pulling in those upstream changes
[922.84 → 929.36] you know businesses don't want to deal with that hassle um they just want to buy something that
[929.36 → 934.98] that they know will work and will be there for the next you know in years that they can count on
[934.98 → 942.26] well even the dev UX too like i you know a fellow developer who would use your open source version but
[942.26 → 948.04] once their business you know they might be fine with using let's say sidekick open source on their
[948.04 → 954.36] personal projects but for their you know work they do at their day job or whatever they're doing
[954.36 → 959.28] they want something that has that support so they might use the pro version at work so your
[959.28 → 964.52] customers are still like me and jarred you know and the listeners of the show, but they just happen to
[964.52 → 969.12] work somewhere else and they and you're right though I think that was a perfect point of I don't think
[969.12 → 974.56] you said it like you did in 92 so maybe you perfected your language around it because that sounded so much
[974.56 → 978.98] better than well not so much better like in a bad way but like it sounded perfect it was a good point
[978.98 → 982.20] to make that you know you're they're paying for the roadmap they're paying for your taste
[982.20 → 988.80] and they're paying for this you know support along the way not just like day-to-day support like
[988.80 → 994.82] helping with an issue but like that rails for you know 4.2 is going to work and other versions
[994.82 → 1000.92] and legacy and that kind of stuff so you weren't sure if people were going to buy this though but
[1000.92 → 1006.44] recently you were you released a post where you said uh some of your numbers which was quite gracious
[1006.44 → 1011.56] yeah uh exposing those I know that's kind of a private thing for a lot of people but I think in the
[1011.56 → 1016.62] post you say why and I think it's super helpful for us to see that sidekick pro sales what you said
[1016.62 → 1025.34] for the last three months of 2012 were uh 7500 bucks in 2013 they totalled 85 grand and this year sales
[1025.34 → 1032.28] should top 175 000 those are pretty good numbers yes um especially since congratulations on that
[1032.28 → 1038.92] especially since they are a subscription you know it's no longer a one-time fee so yeah right you charge
[1038.92 → 1046.46] is it 750 bucks a year for the sidekick pro yeah, so ideally that is a that I mean that's essentially
[1046.46 → 1052.92] what is paying for inspector right is that reoccurring income that I know is going to be there
[1052.92 → 1059.22] so that I can do things like work for four months on a brand-new product that I have no idea if anybody's
[1059.22 → 1065.52] going to buy yeah how much time do you have to continue to work on sidekick uh sidekick generally takes
[1065.52 → 1072.66] 10 to 20 hours a week right now so significant it's significant I mean I'm I'm answering a lot of
[1072.66 → 1080.28] emails um people still put in issues all the time although typically 90 of those issues are some sort
[1080.28 → 1087.12] of application issue um and then I'm constantly on stack overflow you know if someone posts a sidekick
[1087.12 → 1094.98] tagged question I'm usually answering it within 24 hours so um so yeah I mean it's its 90
[1094.98 → 1100.48] support at this point um I did just add a feature to psychic pro which I'm going to be
[1100.48 → 1106.22] rolling out in the next version um so you know I am still doing a little bit of feature work but for
[1106.22 → 1111.70] the most part it's mostly support at this point so you're pretty, pretty happy with your sales um
[1111.70 → 1117.14] interesting that you decided then to say okay I'm going to start this new thing same model I mean that
[1117.14 → 1121.82] makes a lot of sense, but you know at your current rates if we're doing our math right maybe that's
[1121.82 → 1129.12] 200 250 customers you know you perhaps you could just focus on turning that into a thousand customers
[1129.12 → 1135.46] right um focus on sidekick pro right which is obviously a winner as far as being viable in the
[1135.46 → 1143.46] market what made you decide I'm going to add a second product diversification okay is that ball of
[1143.46 → 1148.54] mud it's no we wanted to fix the problem think about finances right in risk you always talk about
[1148.54 → 1156.58] diversifying your investments right yeah you know you have to diversify um your time and uh and your
[1156.58 → 1162.04] investments and what I've done over the last two three years is invested a lot in the ruby community
[1162.04 → 1169.06] and invest a lot in sidekick however um if you take a step back and look at the general
[1169.06 → 1177.10] tech world ruby is two percent three percent of the tech world if you want a wider customer base
[1177.10 → 1183.22] you've got to go with a more generic product and that's exactly what inspector is inspector is
[1183.22 → 1191.76] useful to anybody using Linux you know it doesn't care if you've got a python app a PHP app um uh you
[1191.76 → 1200.90] know a Haskell app if you're a neck beard uh it, it's um it's diversification in the sense that
[1200.90 → 1206.92] if something better than sidekick comes along tomorrow then uh oh what am I going to do
[1206.92 → 1214.82] well now I've got two different products which have slightly overlapping audiences but the Venn diagram
[1214.82 → 1221.60] is still significantly different um that is there's not there's a huge new open territory for me
[1221.60 → 1228.94] to uh to find customers in now this is a prime place too because I mean you'd said earlier in the show
[1228.94 → 1234.88] that this is inspired by to a degree uh from mana you know, so there's some inspiration there you also
[1234.88 → 1239.78] talked about the ball of mud that you got sick of dealing with, so obviously there's something some
[1239.78 → 1244.90] some competitors in the space that weren't cutting the know cutting the cheese so to speak I don't
[1244.90 → 1249.62] know if that's the right way to say that or not cutting the mustard cutting the mustard there you go
[1249.62 → 1255.60] my bad you all um it's probably my Texas uh my Texas ways or something just
[1255.60 → 1260.26] the off colour cutting the brisket but yeah you know yeah cutting the brisket that's a better way
[1260.26 → 1266.12] to say it for Texas style so I mean obviously there's something happening there, and you like
[1266.12 → 1271.44] you said earlier they're paying for taste so you have taste and why not do it better well and in
[1271.44 → 1278.38] fact a lot of the Linux lower level open source monitoring tools are they're either a decade old
[1278.38 → 1284.30] so they've got a lot of accumulated cruft, or they're just I don't know I mean I hate to use
[1284.30 → 1288.94] the term over and over I don't know if it's pejorative or not, but they're very neck beard
[1288.94 → 1295.64] oriented they're just not easy to use they're very unfriendly they're very tech-heavy um you know I was
[1295.64 → 1301.04] looking someone brought up uh collected as a possible competitor and I looked at collected and
[1301.04 → 1313.00] and its syntax is just terrible um it's just hard to use it's its ugly yeah I mean I don't know if
[1313.00 → 1319.02] Linux people care about this stuff but I do and I want things to be easy to use so i I do my
[1319.02 → 1326.28] utmost to pare things down to the bare minimum to get sort of a zen they get the uh you know the
[1326.28 → 1331.66] kiss principle in action keep it as simple as humanly possible and so that's why when you look
[1331.66 → 1337.58] at inspectors configuration files they look stupid simple um, but they're they're they're the bare
[1337.58 → 1345.04] minimum I needed to achieve what I wanted to achieve and uh you know I hope people uh appreciate that
[1345.04 → 1351.64] let's pause the show for a minute give a shout-out to a sponsor digital ocean simple cloud hosting
[1351.64 → 1358.64] built for developers in 55 seconds you'll have a cloud server with full root access and it just
[1358.64 → 1364.34] doesn't get any easier than that pricing plan started only five bucks a month for half a ram
[1364.34 → 1372.98] 20 gigs of SSD drive space one CPU and one terabyte of transfer that's a lot for five bucks a month
[1372.98 → 1380.54] digital ocean also has data centres all across the world New York San Francisco Amsterdam Singapore and
[1380.54 → 1385.62] their newest region London you can easily migrate your data between those regions making your
[1385.62 → 1393.26] data always closest to your users use the promo code changelog November in lowercase it's important
[1393.26 → 1398.84] that you use lowercase changelog November to get a ten dollar hosting credit when you sign up
[1398.84 → 1402.70] head to digital ocean.com right now to get started and back to the show
[1402.70 → 1410.52] um so I see some patterns here um of you taking a thing and like you said inspector is kind of
[1410.52 → 1415.84] Monet plus sidekick was kind of rescue plus in the same post where you gave your numbers
[1415.84 → 1419.58] which everybody should probably go out and read that it's a great post we'll put in the show notes
[1419.58 → 1423.74] for sure so check out the show notes yeah in there you actually give these repeatable steps that you've
[1423.74 → 1428.42] taken obviously we can kind of see the pattern um but could you walk through the steps you took
[1428.42 → 1435.70] as far as how to come to a successful open source slash commercial product and then perhaps as a
[1435.70 → 1439.74] follow-up give examples of things that you haven't taken on that maybe somebody else sure
[1439.74 → 1446.62] um so step one is to find a tool that is non-trivial and important to your current system or workflow
[1446.62 → 1454.00] that goes right back to if you write a tiny hundred line gem nobody's going to care people can it has to
[1454.00 → 1458.92] be non-trivial it has to be something that will take a lot of time right it has to be something that
[1458.92 → 1467.50] is worthy of someone's consideration to use to outsource or to actually buy from you um so
[1467.50 → 1475.02] yeah there and and and ideally like you say you want to find something that is a bit painful to use
[1475.02 → 1481.62] maybe it's overly complex or has a lot of features that you don't want um think about Microsoft Word
[1481.62 → 1487.14] and look at all the text editors out there that are just there's no competition for word and word's not
[1487.14 → 1492.42] competition for them word is just this giant set of features of which you know you use maybe
[1492.42 → 1500.20] five percent of those features so you know there is there a market for a word processor that is just
[1500.20 → 1507.30] much, much simpler and I would argue something like a markdown editor is a perfect example where
[1507.30 → 1513.20] you take the essence of word which is writing a formatted document but kind of twisting it so that
[1513.20 → 1520.96] it's much simpler uh and it but is non-trivial to author and is something that people would pay for
[1520.96 → 1528.82] um so it's its sort of a different take on a word processor so step two is plans out how you can make
[1528.82 → 1533.64] it better simplify it so you're taking Microsoft Word, and you're going down, and you're saying I don't
[1533.64 → 1539.96] need all these toolbars I don't need hundreds of ribbon commands or menu commands or whatever
[1539.96 → 1546.38] um people just want to write formatted nicely formatted documents uh so you're discarding that
[1546.38 → 1552.42] that superfluous functionality, and you're adding your own useful functionality at this point
[1552.42 → 1559.12] uh I like to think about um how am I going to divide the functionality how am I going to make a
[1559.12 → 1564.44] business model out of this thing you've got to you've got to draw a line where you tell customers
[1564.44 → 1570.62] here's what's available to you for free but if you want more you've got to pay for it and um
[1570.62 → 1577.84] and I think like I said 90 of people understand that um and that this is your full-time job and so
[1577.84 → 1582.88] therefore that's just a line you have to draw and then uh, and then you're going to build the thing
[1582.88 → 1589.84] and see what happens um you've got to evangelize it you've got to market it you've got to support it
[1589.84 → 1595.88] it's not just code open source is a process software is a process it's not just a bunch of
[1595.88 → 1603.70] bits that you pound out in vim over a couple of weeks so um you've got to build that
[1603.70 → 1610.66] thing, and then you've got to support it and evangelize it over the course of months and see
[1610.66 → 1617.26] how that goes and uh and that's that was sort of the sidekick model um and then once it takes off
[1617.26 → 1622.84] you build the commercial version of it and start selling it to your open source user base
[1622.84 → 1630.56] and there will be a small percentage of people that will upgrade and so you know it who knows
[1630.56 → 1635.70] how much money that's going to be that could be beer money or that could be enough to make a living
[1635.70 → 1642.54] money but um, but that's where you need to start tweaking your pricing you need to start tweaking the
[1642.54 → 1646.88] functionality you know there 's's no right answer here, but you'll, you'll need to
[1646.88 → 1655.26] experiment, but those are the those are the five steps okay so uh a few examples obviously you chose
[1655.26 → 1660.32] background jobs, and then you chose monitoring are there any other uh pain points that you see out
[1660.32 → 1664.84] there that you know you'd, you'd take on if you didn't have you know two successful projects you're
[1664.84 → 1669.18] already when I was writing this blog post i I was actually thinking oh maybe I should give them an
[1669.18 → 1676.58] example of something that is has room for you know exactly this business model uh, but you didn't I
[1676.58 → 1685.50] I didn't because um I came up with one idea but I wasn't sure I wanted people to sort of think
[1685.50 → 1693.30] on their own about it the one that I came up with was uh HTML to PDF conversion um there's a ton of
[1693.30 → 1701.46] services out there that do that and literally every single business wants this tool and literally no
[1701.46 → 1708.06] open source people want it so what that means is that you've got a very business friendly very
[1708.06 → 1715.24] commercial friendly possible product the one in the ruby space that I'm familiar with is called
[1715.24 → 1727.56] wicked PDF it's a gem that wraps um the WebKit HTML to PDF uh binary um, and it's old and crufty
[1727.56 → 1735.72] and I'm not sure how well it's supported, but that's definitely a tool that if somebody was
[1735.72 → 1744.10] kind of more in the PDF space maybe they knew WebKit better than I do it's something that people might
[1744.10 → 1751.48] consider doing um it's like I said every business I've worked out in the last five years has
[1751.48 → 1757.36] wanted to use that tool for some reason or another, and generally they would have no problem paying
[1757.36 → 1765.32] you know 25 bucks a month or whatever for a tool which does that, and then you multiply that by a
[1765.32 → 1773.30] thousand businesses that need it now you've got 25 000 a month in reoccurring income yeah there's um
[1773.30 → 1779.50] there's a formula that goes 30 uh 30 by 500 and I didn't make that up that's Amy hoy's thing and
[1779.50 → 1785.06] Alex Hillman's thing um but where if you can get 500 customers to give you 30 bucks a month
[1785.06 → 1791.38] you will have a business that makes roughly 150 000 a year you know so if you kind of break it down
[1791.38 → 1797.46] like you have to these achievable uh yet still hard you know it's not like it got any easier but
[1797.46 → 1802.48] they become more achievable once you break it down to these five steps you've kind of given here
[1802.48 → 1808.36] um and I think your model has legs like obviously it's got legs because you you you got 175k in the
[1808.36 → 1813.86] bank that proves that it works well yeah exactly and the wonderful thing about
[1813.86 → 1820.00] software in general is that you can do it in your spare time you know you can do it in nights you
[1820.00 → 1823.86] can do it in weekends as long as your employer is somewhat friendly to you sort of moonlighting
[1823.86 → 1828.38] as long as your employment contract doesn't have issues there of course legally you'll want to you'll
[1828.38 → 1834.82] want to verify that but um you want to make sure you're in the clear long term um, but you know i
[1834.82 → 1843.32] wrote sidekick pro and have been working full-time for the climb for the last two years right and
[1843.32 → 1848.48] the last two and a half years I was working on sidekick and sidekick pro and bringing in I was
[1848.48 → 1853.18] bringing in a hundred thousand dollars through sidekick while also having a full-time job making
[1853.18 → 1860.12] six figures so you can build all this stuff without much investment you know next to no investment aside
[1860.12 → 1867.40] from some time um you know time is a luxury to a lot of people um but if you've got that you can
[1867.40 → 1875.82] invest that time into you know your own possible future career be patient too I mean it seems like
[1875.82 → 1880.96] you've been sitting on some patience honestly like you didn't seem like uh you were in a rush to jump
[1880.96 → 1886.70] ship and like you know the moment you had success with psychic pro basically you weren't like oh I'm out
[1886.70 → 1891.40] you know it so can you talk maybe a little bit about that and I think maybe jarred's got some other
[1891.40 → 1895.22] questions I don't want to stomp on your questions jarred but can you talk a bit about the patience
[1895.22 → 1904.86] aspect of what you've done sure yeah I mean uh having a nice salary makes it much harder to
[1904.86 → 1912.58] determine when am I going to jump ship here you know my salary is a nice steady flat stream of income
[1912.58 → 1920.00] and then my sidekick pro income was constantly sort of slowly but surely rising up and there was an
[1920.00 → 1926.72] inflection point where the two actually met and I was making as much or more every month from sidekick
[1926.72 → 1934.40] pro than I was my salary that's when I started saying okay how long do I hold on here and continue
[1934.40 → 1941.76] to draw a salary before I just say I'm going to do this full-time it worked out to about uh six months
[1941.76 → 1950.80] about in January about January uh this year when uh the two sort of met and I said well you know if
[1950.80 → 1955.28] this thing keeps going I there's no reason I need to be working full-time at all for somebody else
[1955.28 → 1962.40] when I can be doing my own thing and so you know a couple of months ago uh the business came to me and
[1962.40 → 1967.94] said we've got some opportunities here and uh one of those opportunities was for me to leave
[1967.94 → 1976.96] with a very nice severance package and I elected that and uh and in doing so that severance
[1976.96 → 1984.46] package effectively subsidized the building of inspector so uh so yeah it's its it's worked out
[1984.46 → 1989.74] really well um and if you're patient you can time this stuff so that it works out the best for you
[1989.74 → 1996.32] so I think one of those other hard decisions I mean I'm looking at this as like a viable thing
[1996.32 → 2002.30] to possibly do and I think another place where it's difficult obviously this is a business decision
[2002.30 → 2006.94] is like where do you actually draw the line in the sand for pro features versus the open source
[2006.94 → 2012.02] features you've done this twice now, and you probably felt it out with sidekick and I think you're
[2012.02 → 2016.82] probably you may be a little more confident with inspector um can you kind of speak generally and
[2016.82 → 2021.94] then we'll get into inspector details after that yeah that's a common question I mean almost literally
[2021.94 → 2030.24] the first question everybody asks me there's no easy answer um what I've done with inspector is
[2030.24 → 2038.04] tried to say okay what's what's an quote-unquote enterprise feature what does a team feature what I've
[2038.04 → 2045.12] tried to do with inspector is make the open source functionality be the features that an individual
[2045.12 → 2050.08] would want if they were a hobbyist and just sort of built their own server-side application
[2050.08 → 2058.02] without a team inspector pro on the other hand has a bunch of functionality so that you can route
[2058.02 → 2064.88] alerts to different people you can set owners of different components so you know Bob owns the
[2064.88 → 2073.36] database, but Mike owns the background processing system and Ted over here owns nginx or Apache or
[2073.36 → 2081.18] the app server or whatever and so that way if any of these components misbehave the alerts are routed to
[2081.18 → 2089.32] the team members that know them best so that's that's one approach that I've taken is again what's an
[2089.32 → 2096.74] enterprise feature what's a team type feature and uh and that's that's really all I have in terms of
[2096.74 → 2103.22] advice it's its not an easy question to answer, and it's just something that you have to judge for
[2103.22 → 2109.72] yourself um I'm I'm I'm I've got about five or six different features that I want to add to inspector
[2109.72 → 2115.58] right now, and it's really tough trying to figure out all right which of these should go into pro and
[2115.58 → 2120.48] be sort of locked away from the majority of users that's that's really that's a really painful decision
[2120.48 → 2125.84] to make because I want to give all the functionality to everybody but I know that that's just not a viable
[2125.84 → 2136.82] viable uh solution yeah I'm curious how that affects your open source contributions when uh not just
[2136.82 → 2141.94] okay that you know people actually getting involved in your open source projects but then also like
[2141.94 → 2147.32] the kinds of uh pull requests that you'll actually accept and then do you decide wow that's a great
[2147.32 → 2153.02] feature thanks I'm going to put it in my pro well I can't do that I mean that you can't do that right
[2153.02 → 2160.56] their license okay so that I mean if somebody is submitting a PR to me um that that's yeah i i I see
[2160.56 → 2169.22] that as their code and when I pull it in it's licensed to me sort of based on the um contribution
[2169.22 → 2174.58] guidelines but I would not take somebody's code and then just make it a pro feature that's that's
[2174.58 → 2180.70] immoral or unethical uh in my opinion agreed so what if you're what if you're thinking about
[2180.70 → 2184.96] implementing that and then somebody does it for you, I guess you just tell them you know I'm going
[2184.96 → 2189.44] to build it myself or yeah I mean that's that's sort of the discussion that needs to be had
[2189.44 → 2195.08] is um yeah is there a common ground that we can reach here maybe there's some subset of the
[2195.08 → 2199.96] functionality that we can put into open source that's still useful but i have a different
[2199.96 → 2207.70] vision for the way this feature is going to work um, or you know do I just close it out right and say
[2207.70 → 2212.02] no I'm gonna I'm going to put this is the type of thing that properly belongs in pro
[2212.02 → 2221.24] i I don't want to do that, but you know that's the that's the worst possible outcome in my opinion
[2221.24 → 2225.54] something that comes to mind in that uh in that regard is what twitter did with their API they kind
[2225.54 → 2231.20] of said to API developers like don't hang out in these areas these are danger areas these areas are
[2231.20 → 2235.32] okay for you to hang out in we won't stomp on you, but these areas are kind of areas we're heading
[2235.32 → 2241.64] towards or things we're doing differently and they kind of like to a degree somewhat road mapped
[2241.64 → 2247.68] what was safe and what wasn't safe yeah I mean that's a that's a great analogy um they've they've
[2247.68 → 2254.02] had to walk a really fine line because they're not a pipe they're not just purely a pipe
[2254.02 → 2259.96] for tweets to flow down you know they also want to control the glass the way that people see
[2259.96 → 2266.34] tweets so that they control the ads that people see and uh and that really has hit their third
[2266.34 → 2275.08] party client uh ecosystem pretty hard and so in your case third party clients are you know PRS
[2275.08 → 2280.22] contributions open source developers kind of helping you sustain the open source side but at the same
[2280.22 → 2284.90] time keep it progressing keep it moving forward yeah there I mean there's always a there's always a
[2284.90 → 2291.72] tension there um where you have something free and then something paid on top of that um nobody
[2291.72 → 2297.64] begrudges twitter for having to make a living I know that i myself I would prefer to pay twitter uh
[2297.64 → 2304.14] you know a dollar a month you know a dollar a month is I would be happy to pay and if app.net man if
[2304.14 → 2311.20] they take their uh their users right exactly um they take their hundred million users and
[2311.20 → 2315.50] I charge them a dollar a month you know you got a hundred million a month coming in that that pays
[2315.50 → 2322.80] for a lot of office space in San Francisco um but yeah i I also understand that a social network is
[2322.80 → 2328.90] is based on the size of the network and uh and the vast majority of people don't want to have to pay
[2328.90 → 2335.68] for something if they can just see ads instead which is unfortunate yeah the hundred million users
[2335.68 → 2341.18] you know drops to 350 000 or something like that and now your network is not as valuable
[2341.18 → 2348.20] exactly, exactly let's pause the show for a minute give a shout-out to a sponsor hired.com is sponsoring
[2348.20 → 2356.28] the show this week and the URL you need to go to is hired.com slash changelog podcast again hired.com
[2356.28 → 2362.40] slash changelog podcast and when you go there uh they're going to give you a're going to double
[2362.40 → 2367.62] the signing bonus that they give you if you accept a job on hired.com from two thousand dollars
[2367.62 → 2374.20] to four thousand dollars every week on hired uh thousands of tech companies in San Francisco new
[2374.20 → 2380.98] York Seattle and la uh bid on hiring awesome developers providing the salary and equity up
[2380.98 → 2388.64] front some of their most in-demand jobs are web and mobile developers DevOps UI UX and even some
[2388.64 → 2395.60] product managers the average developer gets about five to fifteen offers with equity with salary all that
[2395.60 → 2401.04] up front uh and even if you're not looking for a job, but you might know someone who is you can revert
[2401.04 → 2406.64] you can refer them to hired and get an awesome bonus as well if they accept the job and the amount of
[2406.64 → 2412.76] that one is one thousand three hundred and thirty-seven dollars total leet so go to hired.com slash
[2412.76 → 2418.82] changelog podcast and get hired.com so thinking about contributions I was just looking at sidekick here
[2418.82 → 2426.62] as you're talking in uh 713 forks 242 contributors over its lifespan I would say that the model maybe
[2426.62 → 2431.02] some of that was before you had the pro version, but it seems like there was no barrier for people
[2431.02 → 2436.52] wanting to hop in and help out there so that's good were you concerned about that especially with
[2436.52 → 2442.38] inspector I mean it's only been out for a day, but you know one fork so far um my main concern with
[2442.38 → 2448.00] inspector is just the fact that it's using go so that it's a relatively new language um yeah so
[2448.00 → 2455.60] you know Mont is written in c and uses I think they're on Bitbucket so they're they're just kind
[2455.60 → 2460.18] of in a different ecosystem so I'm not sure if people find Bitbucket easy to contribute to or not
[2460.18 → 2466.24] I know that I don't I've never really used Bitbucket before, but hopefully it's its on GitHub it's written
[2466.24 → 2472.40] in go it's easier for people to contribute than something like Mont but um but also keep in mind that
[2472.40 → 2477.98] inspector is different from sidekick in that it's not something that tightly integrates
[2477.98 → 2483.56] with your application you know people sidekick is a framework right people are interacting with
[2483.56 → 2491.04] sidekick APIs their code is running within the sidekick process so you're just you've got a lot
[2491.04 → 2496.96] more moving parts interacting with your app code, and so I think it's natural for people to interact
[2496.96 → 2506.92] with sidekick a lot more so I don't necessarily see as much contribution and as much activity
[2506.92 → 2511.98] around uh people contributing to inspector is kind of a black box where
[2511.98 → 2519.08] you install it you set it up to monitor your components and then that's it um you know we'll
[2519.08 → 2523.20] see we'll see what happens that could be completely wrong, but that's kind of my feel for it so far
[2523.20 → 2530.88] cool so let's talk about inspector then so uh you said that you had uh Mont was a tool that you use
[2530.88 → 2538.30] um not super happy with it but useful um you decided to dig in see how you could make Mont better
[2538.30 → 2543.74] and you said two things first of all removing features that you don't need and then secondly
[2543.74 → 2550.42] adding in some stuff that is more modern or that you think that you do need so you may reiterate a
[2550.42 → 2555.52] little bit but could you enumerate a few on either side sure of what you've done so you are the first one
[2555.52 → 2561.26] was removing functionality um right which unit d you mentioned is a big piece of that yeah there
[2561.26 → 2568.44] what I did with inspector is sort of make the decision that inspector will not start and stop
[2568.44 → 2580.54] processes directly so Mont and god and blue pill they all have a way to start a process stop a process
[2580.54 → 2589.28] to set the user that it runs at as to set the group that it runs as all this boilerplate
[2589.28 → 2594.62] to start and stop processes and what I realized is that's the job of your unit system all of these
[2594.62 → 2602.32] you're the machine that you're using exists to run your application components are the
[2602.32 → 2607.84] most important thing running on that machine and the most reliable way you can ensure that your
[2607.84 → 2615.40] components are running is to integrate them with your operating systems unit system and that in Ubuntu is
[2615.40 → 2625.76] upstart um in core OS or uh CentOS 7 that is system d and future up future Ubuntu are going to be using
[2625.76 → 2635.90] system d also so uh inspector defers the start and stop of processes to the unit system to upstart
[2635.90 → 2645.58] system d run it and uh launch d you know s10 so uh what I try what I'm trying to guide people to do is
[2645.58 → 2653.62] is to integrate their application components into their unit system so that they have something reliable
[2653.62 → 2662.18] that is always there to start and stop these things you know inspector itself uh people shouldn't
[2662.18 → 2667.04] necessarily rely on to ensure that this thing that you're the components are started you know inspector
[2667.04 → 2672.92] can crash but the one thing that can't crash on your operating system is your unit system if it crashes
[2672.92 → 2680.00] the machine crashes so uh so yeah if you want your components to be up you want to integrate them
[2680.00 → 2686.92] with that unit system so when I made this decision I realized that cutting out the starting and stopping
[2686.92 → 2695.22] your processes is a big bulk of the configuration you know every Mont recipe every god recipe
[2695.22 → 2702.10] has um four or five lines devoted to how do i start this thing how do i stop it what user does it run as
[2702.10 → 2707.98] all this kind of stuff so that dramatically simplified um inspector because i don't have to deal with
[2707.98 → 2715.36] that a couple other features that Mont had for instance are things like monitoring uh files
[2715.36 → 2720.78] and directories to make sure that they have the correct permissions to make sure that they have
[2720.78 → 2727.82] the correct uh Shaw so that the file contents haven't changed that to me is not something I've ever seen
[2727.82 → 2734.38] anybody ever use um having been an application engineer using Mont to monitor the various demons
[2734.38 → 2741.18] it doesn't make any sense to me to monitor file shares and directory permissions and that sort of thing
[2741.18 → 2744.74] seems like more of a security concern than a monitoring concern correct
[2744.74 → 2749.00] if you want uh if you want something like that you're going to be using either a read-only file
[2749.00 → 2756.78] system, or you're going to be using some sort of um IDs intrusion detection system so yeah that
[2756.78 → 2763.30] seemed like a kind of poor man's security thing and really no reason for it so that's that's
[2763.30 → 2768.12] another example of a feature that i just completely lopped off and had no interest in rebuilding
[2768.12 → 2774.72] so what about the installation story i mean as i said in email I'm a Mont user have been for
[2774.72 → 2782.50] a long time I'm a Debian usually um you know i can just app get install Mont um inspector written
[2782.50 → 2788.10] in go we can talk about that as well go kind of has this great uh story around dropping a binary
[2788.10 → 2793.34] somewhere um how easy is it to get inspector on your machine maybe speak to the open source and
[2793.34 → 2799.40] the pro versions i I'm sad to say that inspector is two times as heavyweight as Mont you have to run
[2799.40 → 2806.80] two commands not one command oh man so twice as many yeah it in inspector i would imagine in the
[2806.80 → 2813.82] future will be integrated directly into the various operating systems package repositories but right
[2813.82 → 2819.00] now it being brand new i have to distribute it myself so can you do that with your pro version too
[2819.00 → 2824.84] though down the road or not uh yes i do the pro version is ready for people to buy it's its
[2824.84 → 2833.44] available um it is i run my own package repo that um i control um through basic auth just who can access
[2833.44 → 2841.30] it and uh and so when you buy inspector pro you get instructions on how to set up the repo access
[2841.30 → 2848.48] and then from there it's just app get inspector pro cool so yeah inspector itself is distributed
[2848.48 → 2855.74] through this great service called package cloud uh and they provide a sort of package distribution
[2855.74 → 2863.84] in the cloud as the name might indicate and uh so the know you have to run one command to set up
[2863.84 → 2872.08] their repo on your machine and then from there it's just apt get install inspector not too bad not
[2872.08 → 2880.26] too bad it's as simple as i could possibly make it but yeah i mean i worked for probably a month to get
[2880.26 → 2887.32] Debian and rpm distribution working it is ridiculous how hard that stuff is to get working
[2887.32 → 2894.38] was this your first big go project yep yeah in fact uh the reason why it took me
[2894.38 → 2901.94] uh you know four months of full-time work was because that i was learning go, and so i would write
[2901.94 → 2906.92] a bit of functionality and then a couple of days later I'd read through that functionality and say this
[2906.92 → 2911.94] code is terrible I've got to rewrite it write it again yeah and so yeah i mean i've rewritten inspector
[2911.94 → 2920.42] probably two or three times in uh all of it i mean i rewrote all of it probably you know two or
[2920.42 → 2926.54] three times uh just because i ramped up on go pretty quickly, but you know it still takes a couple
[2926.54 → 2931.62] months to get a feeling for what does idiomatic code look like um what is a proper error
[2931.62 → 2937.28] handling you know where do you use interfaces and pointers and value objects and all that kind
[2937.28 → 2944.20] of stuff so was that fun for was that fun for you or was that frustrating it was fun striating
[2944.20 → 2951.46] okay and i make up a word yeah i think you just did it was uh it was fun and frustrating it's its
[2951.46 → 2957.62] always frustrating because you want to just be able to do something, so there's this cognitive
[2957.62 → 2965.44] dissonance as you try to write ruby code and go right um, but again it's one of those one of those
[2965.44 → 2971.54] paths where i realize you've got to walk down this path to get to the destination which is
[2971.54 → 2978.64] being a journeyman programmer not a beginning programmer in this thing, and so i enjoy that i enjoy that
[2978.64 → 2983.86] process so uh yeah it did take me a couple of months and for the first month i was definitely really
[2983.86 → 2989.24] frustrated you know things like how do i take a string and split it up by commas and get an array
[2989.24 → 2994.64] of those strings and how do i convert a byte array into a string and how do i convert this type into
[2994.64 → 3000.14] this other type, and you know that's stuff that you rarely ever need to do in ruby, but it's its
[3000.14 → 3007.40] it's critical and go and so that was stuff that i had to learn all new yeah i just wrote my my my
[3007.40 → 3013.56] first production go it's a small API for a customer and uh long time ruby and JavaScript
[3013.56 → 3017.52] developer so you know you get things ingrained in your fingers you know maybe you have to have the
[3017.52 → 3022.52] docs open if you forget an API, but you're not like searching how do i do this in JavaScript or in ruby
[3022.52 → 3029.04] and I've just found my Google search like astronomically increased you know with go over the last month and
[3029.04 → 3035.78] a half um there's a great site called gobyexample.com which is it's like i know how to program just tell me
[3035.78 → 3040.02] how to do this and go he has a great just like here's how you do Jason parsing here's how you do
[3040.02 → 3046.80] right you know x y or z and this kind of sites are super valuable why did you pick go over you know
[3046.80 → 3053.36] your bread and butter that's a good question so um so blue pill and god are both written in ruby
[3053.36 → 3064.78] um so i have always used Monet and shied away from them because to me a monitoring package needs to
[3064.78 → 3074.16] be as robust and as simple as humanly possible for reliability purposes and i don't want my
[3074.16 → 3080.46] application written in the same stack that is monitoring if it's that's a know you've got
[3080.46 → 3086.18] possibility of them both dying for some reason you know if your ruby's VM somehow breaks
[3086.18 → 3094.60] well now your monitoring solution breaks too um i always loved the Monet simplicity you know the fact
[3094.60 → 3098.86] that it only used a couple megabytes of memory uh the fact that it was just a single binary
[3098.86 → 3107.70] to start and uh, and so i wanted that type of simplicity in inspector what i didn't want to
[3107.70 → 3114.94] do is write it in c or c plus so when something like go or rust came along i said well these are
[3114.94 → 3120.70] perfect next generation system languages that i can use to build this type of infrastructure
[3120.70 → 3127.24] without having to deal with um you know memory management and pointers and all that kind of
[3127.24 → 3133.16] stuff directly so uh that's why i that's why uh that's one of the reasons i did it and go the other
[3133.16 → 3140.16] reason i did it and go is it's simply because the language has a really strong standard library where
[3140.16 → 3148.76] i didn't need to pull in any third party packages at all to implement it so uh inspector has no
[3148.76 → 3154.86] runtime dependencies aside from the linux kernel you know it's just a single, but it doesn't
[3154.86 → 3163.52] even use LBC so you think that choice has paid off so far well we'll see um i have you know at the
[3163.52 → 3169.68] very least I've invested in learning go and become an uh not a beginner go programmer anymore, but you know
[3169.68 → 3176.64] I'd say a journeyman go programmer um so in terms of investing in myself you know it's paid off
[3176.64 → 3182.74] but uh you know there's uh it remains to be seen how well the commercial product sells and how
[3182.74 → 3189.78] well the open source project is taken up you know it's still early days having been launched 24 hours
[3189.78 → 3196.64] ago it's its often that um whenever you try something new like this whenever you go from ruby to go
[3196.64 → 3202.02] that you often compare can you give us a comparison of uh what you love about both or what you love more
[3202.02 → 3208.02] about ruby or what you love more about go now that you're um experiencing the awesomeness that it
[3208.02 → 3218.72] is sure um ruby is fantastic for building a big thing if you can leverage like rails you know you just
[3218.72 → 3225.88] you really can't beat building a website in rails it's still it's still the best thing out there as far
[3225.88 → 3232.04] as I'm concerned i would not want to build a large website and go i think that would be inappropriate
[3232.04 → 3241.02] I think the ruby flexibility and prototyping speed is still um much faster than goes speed
[3241.02 → 3246.36] where go shines is where you've got something very simple very focused that you want to build
[3246.36 → 3254.50] and you can, you know sort of hold the code in your head and just build it out really quick um you know
[3254.50 → 3263.28] go's speed is it goes runtime speed is really um really nice for sure uh running my test suite you
[3263.28 → 3268.52] know takes tenth of a second you know of course ruby can do some of that if you structure the
[3268.52 → 3274.08] code correctly but yeah i think ruby has points where it shines in terms of these
[3274.08 → 3280.06] frameworks like rails like sidekick where you can build these large-scale apps pretty quickly
[3280.06 → 3287.68] and uh and go is more of a sort of sharp focus tool for building uh you know smaller lower level
[3287.68 → 3294.98] things is typically how I think of it in your uh in your list mentioning uh the introduction to
[3294.98 → 3298.54] inspector you've got several things that you kind of have on the plate that you're that you're
[3298.54 → 3303.64] supporting in terms of like writing alerts to Slack hip chat campfire flow doc some of the
[3303.64 → 3310.00] common hit lists of popular kind of collaboration tools you also mentioned that it's brand new
[3310.00 → 3316.26] it's not 1.0 yeah can you talk about um since it's since this is new and for those listening
[3316.26 → 3321.00] you're probably listening as much as maybe five days after the recording of this so when we say
[3321.00 → 3324.96] it was released one day ago it was actually like six days ago technically depending upon when you
[3324.96 → 3331.98] listen to this but um can you talk a bit about you know this early version not 1.0 version um
[3331.98 → 3337.74] in terms of feature set which you've put in it and like maybe where you see things going and
[3337.74 → 3346.04] and possibly even how um how actually using go supports some of the the the lifespan you see for
[3346.04 → 3355.06] this so the uh the base inspector the open source version of inspector uh will monitor any
[3355.06 → 3361.58] service that's integrated with your unit system uh it will monitor daemon specific metrics so it'll it
[3361.58 → 3367.64] knows it understands my sequel it understands nginx Regis geocached those are the four I launched
[3367.64 → 3373.72] with I see there are tons of opportunity to for people to contribute their own daemon specific
[3373.72 → 3381.16] metrics uh things like um Cassandra Kafka you know there's a there's a whole world of like java
[3381.16 → 3386.44] infrastructure for instance that isn't covered at all but I'd love to have integration with just
[3386.44 → 3393.14] more infrastructure that people use to build their apps those happen to be the four things that I use
[3393.14 → 3399.72] um that the ruby community often uses but um you know maybe python folks maybe uh for instance like
[3399.72 → 3407.46] celery or rabbit me uh would be more examples, so daemon specific metrics are in the open source
[3407.46 → 3413.90] version uh what else is there so you're gonna you're going to monitor your CPU and your memory of
[3413.90 → 3421.50] your process your daemon specific metrics you can monitor the host metrics things like swap disk space usage
[3421.50 → 3429.48] CPU usage and then oh you can also you can also get an overview of all the status of all the services that
[3429.48 → 3436.46] it's inspecting at a given moment, and you can also see a graph of a metric in the console so if you're is
[3436.46 → 3442.88] you're at the terminal and something uh an alert fires you can actually see the history of the metric right in
[3442.88 → 3448.00] your console without having to open up and find a graph or something like that which is pretty nice
[3448.00 → 3457.10] uh now in terms of uh, uh the commercial version pro has the ability to monitor unit d the old
[3457.10 → 3463.34] legacy stuff that ball of mud that I referred to um that's so you didn't want to do it, but you'll
[3463.34 → 3470.82] do it for money exactly, exactly I like that that's a good one jarred well that's that's a that's an
[3470.82 → 3477.18] example where if people have legacy services if they're an enterprise and they just don't want to
[3477.18 → 3483.34] touch the thing, but they do want to use uh inspector to monitor you pay the money and the problem is
[3483.34 → 3488.72] solved um yeah I mean part of this hard line that I'm having to take with features is trying to
[3488.72 → 3495.04] guide people to author better applications and sometimes that means i you know I'm not going to
[3495.04 → 3500.42] support the old way of doing something because i really genuinely feel it's not the right way to do
[3500.42 → 3506.00] things now if people want to pay me money to so that they continue to continue to do it the old way
[3506.00 → 3512.26] then that's that's their choice, but you know I'm I'm taking a stand here and saying that unit d is not
[3512.26 → 3520.00] the right thing to do any more um so uh yeah so unit d is supported in pro um and then yeah as you said
[3520.00 → 3526.88] chat rooms for teams who want alerts to be piped into their shared chat room where maybe they've got
[3526.88 → 3531.82] people in the chat room 24 7 that's a perfect example where you can sort of cut down noise in
[3531.82 → 3540.20] your inbox by directing uh the alerts into the chat rooms and then uh the final feature in pro right
[3540.20 → 3547.40] now is the uh ownership so you can give ownership to various components you can say I want alerts for
[3547.40 → 3553.40] this thing to go to this particular team or this particular person because inspector itself the open
[3553.40 → 3561.08] source version you can only send alerts to a single email address that's it now what's coming down
[3561.08 → 3566.26] the pipe uh yeah I've got a bunch of ideas one thing I want to put in the open source version
[3566.26 → 3574.18] is monitoring cron jobs to ensure that cron jobs are running uh if you have a cron job that runs hourly
[3574.18 → 3581.40] and you deploy your code and that code change breaks that cron job how do you know
[3581.40 → 3588.22] oftentimes the job will just start silently failing, and you won't know until a customer calls
[3588.22 → 3593.40] customer emails, or maybe you don't receive a report the next day or something like that
[3593.40 → 3602.44] but having something that that that notifies what I want to do is have a way for the cron job to
[3602.44 → 3608.36] notify inspector that hey I just ran and then inspector will say if I haven't received a notification within
[3608.36 → 3614.68] the last hour or within the last day to fire off an alert to say hey this cron job didn't fire
[3614.68 → 3622.08] let me just say as a longtime Monet user and relatively happy Monet user if you do that feature
[3622.08 → 3627.26] I will immediately switch I was going to say you seem like you're lamenting with the pain like I can almost
[3627.26 → 3632.14] audibly hear the pain you felt from not having that feature yeah I've looked for solutions there's
[3632.14 → 3638.12] some online services where you can uh you know do your cron job, and then you know do ampersand
[3638.12 → 3643.92] and then hit some API that just says I did it right that it actually succeeded, and then they'll send you
[3643.92 → 3650.68] emails and stuff if it fails um tried those there's other you know things where you can just pipe it to
[3650.68 → 3657.44] an email address if it fails anyway they all suck right well mine's going to suck right mine's going to suck
[3657.44 → 3667.06] just as much oh, oh well yeah so in a better way though maybe yeah so that was one idea I had for
[3667.06 → 3672.44] another feature um you know the other obvious feature would be sort of a web interface to see an
[3672.44 → 3678.62] overview of the different metrics you're tracking and to see pretty graphs um yeah that that would
[3678.62 → 3685.28] probably be a pro um feature I'm not sure uh but yeah anything that's sort of team or
[3685.28 → 3692.96] collaborative is definitely uh going to be lean toward pro things like cron jobs though you know I can
[3692.96 → 3699.58] see individuals wanting those as part of their applications and so putting a cron job checker uh
[3699.58 → 3707.20] seems like a natural fit yeah I'm for it cool I'll count that as a plus one on the issue then
[3707.20 → 3715.90] there you go well cool mike um we uh we tend to ask a few questions at the end of the show but
[3715.90 → 3719.20] we're going to ask one simple question because that's that's the way we're going to roll around
[3719.20 → 3725.90] here but um inspectors new it's you know let's say it's you know barely a day old in terms of release
[3725.90 → 3734.48] um can you kind of give the listeners a way that you're looking for engagement you know is there
[3734.48 → 3738.92] a feature set like you'd mentioned earlier you know supporting different systems Debian and
[3738.92 → 3743.18] were some of the ones that you'd mentioned that you use so you're supporting those are there a
[3743.18 → 3749.82] hit list that you have a road map how can people jump in and help you launch the open source side
[3749.82 → 3756.86] and right and uh maybe even how to buy the pro side well i what I would love what I need right now
[3756.86 → 3761.66] is just users you know it's a brand you know it is a brand-new project so I would love people to
[3761.66 → 3768.92] download it try it out um I'm definitely not strong in terms of the operating system packaging
[3768.92 → 3775.12] so deb support rpm support i I spent probably a month trying to polish it and get it working
[3775.12 → 3780.12] but I'm sure that there's uh plenty of room for improvement there so maybe some code review on
[3780.12 → 3785.40] certain areas yeah exactly I mean if there's an if you know you got more of a Debian guy or more of a
[3785.40 → 3796.26] um a fedora guy uh wants to or girl for that matter uh agenda is not an issue um if is
[3796.26 → 3803.12] anyone wants to come in and uh and help me out there I'm happy to have that uh I've cobbled together
[3803.12 → 3807.54] what I have right now but I'm sure there's room for improvement and the other thing is just use it
[3807.54 → 3815.04] and give me ideas for features um send PRS and uh and remember the there's that demon
[3815.04 → 3820.16] specific feature where you know i want inspector to know about as many of these popular
[3820.16 → 3828.74] different application components as possible and so getting uh PRS to add more and more of them
[3828.74 → 3834.98] would be awesome so yeah that's that's definitely ripe for uh for some for uh PRS
[3834.98 → 3840.92] well awesome well is there anything else that you want to cover mike and in closing before we uh
[3840.92 → 3846.58] take the show out not really I just want to thank you guys for giving me the opportunity to come on
[3846.58 → 3852.72] and uh ramble on a bit cool well uh we'll have all the links in the show notes so if uh
[3852.72 → 3857.90] uh we'll mention here on the air but uh mp arum on Twitter if you want to follow mike, but we'll have
[3857.90 → 3863.66] some links in the show notes to back to the code back to um your uh your company site we'll even
[3863.66 → 3870.38] link that blog post that jarred mentioned this uh this fantastic way to have this path of
[3870.38 → 3875.32] success like mike has found for sure so mike thanks for coming on the show um we had some awesome
[3875.32 → 3879.36] sponsors for this show so as you might know not only are we member supported, but we're also
[3879.36 → 3883.82] sponsor supported because we work with some really, really cool companies one of those cool companies
[3883.82 → 3889.90] is code ship love code ship those guys are awesome hired.com uh and also digital ocean we're
[3889.90 → 3893.90] hosting on digital ocean we love digital ocean, and we think you should too if you're not using them
[3893.90 → 3898.86] then I just make a sad face and that's just that's just how it goes, but that's it for this uh this
[3898.86 → 3904.92] week's of changelog, and we'll be back as soon as you want to hear us let's say goodbye bye
[3904.92 → 3905.88] bye
[3905.88 → 3909.88] you
[3909.88 → 3913.88] you
[3913.88 → 3915.88] you
[3915.88 → 3917.88] you
[3917.88 → 3919.88] you
[3919.88 → 3921.88] you
[3921.88 → 3923.88] you
