[0.00 → 16.74] let's do if it's go time welcome to go time your source for wide-ranging discussions from all
[16.74 → 23.40] around the go community check us out on the web at go time.fm there you'll find lists of
[23.40 → 28.86] recommended and popular episodes unpopular opinion clips and a request form so you can
[28.86 → 35.28] let us know what you want to hear about on the pod big thanks to our partners at fly.io over 3 million
[35.28 → 42.82] apps have launched on fly deploy yours in five minutes learn how at fly.io okay here we go
[42.82 → 55.74] what's up friends I'm here with kyle barberry CTO at coder.com so kyle I've known coder as the IDE
[55.74 → 61.68] in the cloud and over time you've iterated to become a fully open source cloud development
[61.68 → 68.20] environment a CDE how do you explain what coder is and what it does coder is a platform to provision
[68.20 → 72.78] you a development environment on any cloud infrastructure that might be in a VM that
[72.78 → 77.48] might be inside a container, but coder is kind of a developer's route to provision infrastructure
[77.48 → 82.60] for them to write software inside we started with the IDE which is kind of like putting VS Code
[82.60 → 86.58] in the browser which is what most people are certainly familiar with us for and we kind of
[86.58 → 91.00] funnelled that into more of a platform where people provision the infrastructure and a lot of people
[91.00 → 97.12] do use a we bide with coder a lot of people use a local IDE and just connect in let's laser focus in on
[97.12 → 103.44] the platform engineer it is that team's job to provide the best infrastructure the best platform
[103.44 → 110.72] for their given applications for their teams what are some signs or signals for platform engineers to
[110.72 → 115.34] think about when it might be time to consider a cloud development environment like coder.com
[115.34 → 120.90] so as a platform engineer developers might constantly be opening like it tickets that their
[120.90 → 125.76] computer isn't working properly they might constantly want to update dependencies, but that's
[125.76 → 131.56] a big mess you constantly have to email people across your team to say hey Adam could we update from
[131.56 → 137.10] java 17 to java 18 those are the kinds of problems that people typically have that's the status quo you
[137.10 → 142.08] ship people more powerful laptops to improve the build times of your projects you try to reduce the
[142.08 → 147.38] complexity of your products instead of simply you know leveraging better hardware we believe that the
[147.38 → 152.56] future is leveraging the cloud for a lot of these things you can get more powerful instances in GCP or
[152.56 → 157.44] AWS that can make the build times faster instantly you can let one developer create a standardized
[157.44 → 162.24] environment and then distribute it to a thousand so that when you're updating from java 17 to 18
[162.24 → 167.88] it's just a simple pull request you can co-locate your servers right next to something like s3 or a
[167.88 → 172.50] database that you're using in development so that you get immediate data transfers, and it's not slow
[172.50 → 177.48] many of our customers which is a crazy thing to say, but they use absolutely massive monorepos and they
[177.48 → 182.54] get clones that go from like 10 minutes or 20 minutes or an hour to simply like a minute or 30 seconds
[182.54 → 188.20] it's just a lot simpler when all of your engineers are standardized on one centralized piece of
[188.20 → 193.38] infrastructure and then one person can impact the lives of hundreds of engineers and with that
[193.38 → 197.38] we don't believe that everything belongs in the cloud we think that some workloads are really amazing
[197.38 → 202.80] for it and some are absolutely terrible coders should be a self-serve offering to your engineers it should
[202.80 → 208.04] not be prescriptive where you migrate all pieces of software development into the cloud only the things
[208.04 → 212.44] that really get a lot better by running them in this cloud native way do we really promote moving
[212.44 → 218.84] well it might be time to consider a cloud development environment and open source is awesome
[218.84 → 227.80] and coder is fully open source you can go to coder.com get a demo or try it right now or even start a 30-day
[227.80 → 235.84] trial of coder enterprise once again coder.com that's c-o-d-e-r.com coder.com
[235.84 → 261.80] hello hello hello and welcome back to another episode of go time today I am joined by some lovely co-hosts to
[261.80 → 269.74] discuss an I don't know I'm going to withhold from applying any adjectives to this piece of work
[269.74 → 278.58] that we're here to discuss called founder mode and how that applies when to us as engineers and us as
[278.58 → 284.78] a product owner and people who build software for a living how does that apply to us when we
[284.78 → 291.58] ourselves are not the founders that's a slight um bend to the topic there but uh please
[291.58 → 299.04] help me um welcome uh angelica hill how are you doing angelica I'm good I'm good I'm uh enjoying
[299.04 → 305.98] being inside I'm not one for heat somewhat of an English rose and that if you apply too much heat
[305.98 → 312.56] I will wither so I'm enjoying being inside nice staying away from the heat yeah it's that time
[312.56 → 318.38] of the year for on the east on the east coast awesome chris Mr Chris Brandon how are you
[318.38 → 323.70] I'm doing good also avoiding the heat you know like last week it was like 16 it was beautiful
[323.70 → 329.58] now it's hot again and I don't like this, and it needs to stop its fall it's fall we should have
[329.58 → 336.34] fall weather bring back the fall weather look at us defying stereotypes engineers that don't go outside
[336.34 → 337.98] what a phenomenon
[337.98 → 348.98] what uh man all right so let's let's let's get into this because I think I must, I'm going to assume
[348.98 → 355.50] that uh because of the sheer popularity of this essay for by Mr Paul Graham of Y Combinator fame
[355.50 → 364.20] that um most of us and probably uh at least a few of us listening to this episode have uh heard of
[364.20 → 370.36] the whole founder mode at least you've seen some memes on the internet about founder mode
[370.36 → 375.94] and sort of the implications but just to sort of uh um make sure that we're all on the same page
[375.94 → 381.32] here a quick summary of what founder mode is what the essay is about so I asked chad GPT to provide
[381.32 → 386.26] me a summary so I'm going to read the bullet points real quick so uh Paul Graham's founder mode
[386.26 → 391.84] discusses the difference between managing companies as a founder versus a professional manager
[391.84 → 398.26] founders often receive uh bad advice on scaling like focusing on delegation which can harm companies
[398.26 → 403.10] a founder's involvement in details and personal engagement are key to success unlike traditional
[403.10 → 408.70] management's handoff approach founder mode leverages a deep connection to the company's mission
[408.70 → 414.50] breaking away from typical management models this approach remains uh underexplored but is essential
[414.50 → 421.66] to effective leadership particularly in scaling startups, so this is in effect about startup world
[421.66 → 427.78] founders and scale-ups as they call them these days and all these things however I saw an opportunity
[427.78 → 434.12] to kind of apply sort of those of us who are not founders at a company perhaps not currently
[434.12 → 441.22] right how do we how do we take so the spirit right of the essay I believe it is to sort of stay in
[441.22 → 446.02] touch right stay connected with the mission with the with whatever it is that you're building and working
[446.02 → 451.16] on or engineering every day staying connected to it and not sort of losing touch not delegating too much
[451.16 → 454.48] kind of thing right and that's going to apply to us more so depending on where we are in that sort of
[454.48 → 458.64] engineering ladder if you're is you're a staff engineer above at a larger company maybe you don't touch
[458.64 → 462.80] code anymore or if you're you're a junior engineer or senior engineer still writing code
[462.80 → 468.60] right how do these things all right how does that spirit right apply to you right as a software engineer
[468.60 → 474.68] who is not who doesn't have the same incentives as a founder right to you know deliver a product or a solution
[474.68 → 479.66] so that's the scope right that's the setting that we're about to discuss here so I want to get a sort
[479.66 → 485.96] of a gut reaction right uh perhaps starting with your angelica like what did you kind of feel or react to
[485.96 → 495.36] when you came across found the mode I mean my initial reaction if I'm honest was twofold one was
[495.36 → 503.78] this kind of just sounds like thoughtful micromanagement where you are micromanaging, but you're making sure no one
[503.78 → 515.92] feels micromanaged but then the other side of me really felt excited about the idea of it being a positive
[515.92 → 524.80] to be very in touch with the kind of day-to-day on-the-ground operations especially for those who
[524.80 → 532.04] are at higher levels because I think one of my core pain points sometimes as I look at like my engineering
[532.04 → 538.56] teams is that when there is a disconnect between the kind of boots on the ground engineers
[538.56 → 543.84] in the weeds building the code and the let's say principal engineer who might be the tech lead or
[543.84 → 550.12] the overseeing architect that's just a recipe for disaster where delegation is happening but because
[550.12 → 557.62] there isn't that almost one person who is keeping tabs on like where is everything how's it going
[557.62 → 562.94] and doesn't have that in the weeds' knowledge to be able to gut check are we moving in the right
[562.94 → 568.14] direction or I'll be completely going off in a tangent letting people go off for months on end on
[568.14 → 576.62] supervised I think a lot of it just questions of balance okay, okay but I liked it overall you liked
[576.62 → 582.60] it okay, okay yeah you can see where uh Mr Paul Graham was coming from okay yes i I do in fact have a
[582.60 → 593.08] take this is once again you know VC Silicon Valley stumbling via the Socratic method on something
[593.08 → 599.48] that business people have known for decades basically founder mode is like a really weird way of saying
[599.48 → 607.02] quality leadership I think that the problem is the essay sets up a false dichotomy right
[607.02 → 613.06] and it is does this fascinating sleight of hand where it's like oh the advice that you get
[613.06 → 619.80] when you're a founder is that you should hire good people and give them autonomy and then they kind of
[619.80 → 625.06] say okay well that's the advice you get, but then you hire all these people that are like basically liars
[625.06 → 629.74] and swindlers and all of that I think the problem with that is that those aren't good people those aren't
[629.74 → 634.30] people that are good at their they're not great they're they're bad uh the fact that you cannot detect
[634.30 → 641.02] that they're bad yes that is a problem that is a problem we need to solve, but the advice isn't bad
[641.02 → 646.56] just because you didn't do it properly right like the advice of actually hiring good people and giving
[646.56 → 654.82] them autonomy is very well researched very well-founded and extremely effective I think where the
[654.82 → 661.24] problem comes in is that we as an industry and I would say to a degree the larger business world
[661.24 → 668.24] is very very very obsessed with not doing leadership as leadership needs to be done I think
[668.24 → 674.44] when people hear the word leadership they hear decision maker and that is very much not what
[674.44 → 680.84] leadership is and that's a very bad way of going about leadership so I think what he's trying to get
[680.84 → 687.84] at in this essay is we shouldn't be doing this type of top-down management of things we shouldn't
[687.84 → 693.76] we definitely shouldn't be looking at different parts of the org below you as black boxes I think
[693.76 → 698.94] he's definitely right about that part that's a very poor way to manage any type of endeavour I think
[698.94 → 707.12] where things go awry though is this assumption that leaders make decisions I feel like I probably said
[707.12 → 713.70] this on the podcast before but a good way to think about leadership as far as I frame it from studying
[713.70 → 720.62] and doing this stuff for decades at this point is a leader is someone who enables decisions to be made
[720.62 → 725.80] they don't necessarily make decisions and I think that's where the autonomy part comes in so you hire
[725.80 → 733.58] great people, and you say you need to have that you need to produce a decision about this thing, and you can
[733.58 → 740.46] delegate that decision-making down further but at the same time that person at the top or whoever you are
[740.46 → 744.70] still needs to go and talk to people and still needs a pulse on the entire organization I think if
[744.70 → 751.54] there's a takeaway from this essay it's that leaders need to be connected into their orgs and i definitely
[751.54 → 756.22] agree with that no matter what type of leader you are you need to be going out and talking to people
[756.22 → 761.76] and connecting with them, I think that the whole idea around skip levels that's in this essay is that
[761.76 → 768.04] that's correct like you shouldn't just be talking to your executive leadership team or like if you want to
[768.04 → 773.46] apply this to like yourself as like an engineer you shouldn't just be talking to your own local team
[773.46 → 777.36] you should be going out and saying oh I have information and someone over there hasn't I'm
[777.36 → 781.76] going to go talk to that person over there and I think that's where this stuff can start to apply in
[781.76 → 789.26] but that is all just pretty basic level leadership stuff I don't think it's we don't I don't I just don't
[789.26 → 793.34] think we need to give it a special name I don't think we need to call it founder mode I think what he
[793.34 → 798.58] describes as manager mode is really just poor management and I know what's really popular and
[798.58 → 802.84] a lot of companies try and do it a lot of business schools push people to do it, but it's just not a
[802.84 → 808.66] good way to run an organization so I think we should go look at the literature that already exists that
[808.66 → 812.88] explains these concepts extremely well that's where I also disagree with him when he said there's no
[812.88 → 817.36] documentation of this there's lots of documentation of this but in general if you kind of strip away the
[817.36 → 824.22] name and kind of the other annoyances I think the idea is a good one for anybody because again it's
[824.22 → 830.70] based leadership it's based being connected in with a group of people and really localizing decisions
[830.70 → 836.14] where it makes sense for those decisions to be made I don't quite know if that I feel like part of
[836.14 → 840.90] founder mode is you're still the decision maker and I think that's the part that needs to kind of
[840.90 → 847.10] not happen but other than that I think that the substance of it is
[847.36 → 856.08] okay is given all those caveats I put out there okay i I think it is contextual meaning
[856.08 → 861.22] depending on the size of the startup you are right it's going to require a different style
[861.22 → 866.34] leadership a different style of ownership right so I think rather than focusing on the leadership
[866.34 → 873.50] in the management perhaps the better way of making this relatable to everybody
[873.50 → 878.44] right um to all of our listeners is perhaps to call it ownership because I think part of this
[878.44 → 884.68] the key takeaway for me in reading this and in trying to apply it right to software engineering as a
[884.68 → 890.24] whole is basically you know it's just boiled down to that term like ownership right so the style of
[890.24 → 897.42] ownership you have is gonna very much be impacted by sort of where you are on the engineering ladder
[897.42 → 903.58] right if you are a junior engineer who perhaps doesn't own a lot all right again all this depends
[903.58 → 908.16] on the size of company the culture and everything else and I think that's that's perhaps sort of glossed
[908.16 → 914.16] over and sort of not really given a fair light right in the article right but the article sort of talks
[914.16 → 919.56] about sort of um you know having skip levels and everything else that imply that already implies a
[919.56 → 924.48] certain size of a company right when you have to have skip levels right that means the company is a
[924.48 → 930.20] scale up as we call it it's its growing there's a lot of people right you know, and you start to
[930.20 → 935.20] delegate things and the delegates then start to delegate things so you start having hierarchy and
[935.20 → 940.02] different people doing different things right but in a much smaller setting where say you have a
[940.02 → 945.04] know say it truly is a small startup and say you have at most a dozen people and you have a
[945.04 → 950.58] generally a flat hierarchy or rather there is no hierarchy it's just a flat structure where there is
[950.58 → 956.10] there is an expect expectation right that different people are going to own different parts of a product
[956.10 → 962.94] right I think that's a much more sort of relatable setting or context right so if we talk about
[962.94 → 969.34] ownership in that sense you know that can apply to you know the code you're writing right can apply to
[969.34 → 975.64] the area of the product that you own it can apply to you know and that can apply to a product manager
[975.64 → 980.86] right uh, and it can apply to a project manager not the same things right, but there's a different
[980.86 → 987.86] different people owning right different aspects of a product right and basically being staying in touch
[987.86 → 996.14] with that so with that sort of framing if again is you're not a founder right you are you say you just got
[996.14 → 1001.82] hired right a couple of months ago, and it's a relatively small team you're excited you're passionate about
[1001.82 → 1009.10] about the product, and you start writing code and you're not incentivized really by perhaps
[1009.10 → 1013.82] monetarily you know if you're a junior engineer you're probably a sort of you know
[1013.82 → 1019.76] starting pretty low on the composition ladder as it were so you know it's more you know you're
[1019.76 → 1024.08] coming in just more interested in learning about sort of getting experience all these things
[1024.08 → 1030.54] how should you see and look at ownership I don't know if I agree with the framing of ownership
[1030.54 → 1039.74] because I think that implies something around like once again like making decisions about something
[1039.74 → 1043.82] whereas I think like at least in my mind when I think about leadership like it's something that
[1043.82 → 1048.46] anybody can do so if you're a junior engineer right and I guess this is where like you can use this
[1048.46 → 1055.50] definition of own where it's like you can own getting something done even if you're in a smaller part
[1055.50 → 1060.08] of the org and I think that's also where like skip level is kind of a misnomer because it doesn't just
[1060.08 → 1067.26] mean up and down, but also side to side right so I think that is a concrete thing that is helpful
[1067.26 → 1073.40] I think to literally everybody is not be afraid to go out and talk to other people that are outside
[1073.40 → 1079.42] of your direct sphere and try and get things done if you need to get things done right because I feel
[1079.42 → 1086.14] like part of the problem with lots of hierarchies is that you wind up with being like oh well I need
[1086.14 → 1091.70] something is blocking me, and usually you have to like to throw something up a hierarchy or whatnot or go
[1091.70 → 1097.60] around something a good form of leadership or that idea of like founder mode would be to just go talk to
[1097.60 → 1102.62] the people on the other team and see if you can like to come to a resolution or figure out a path forward
[1102.62 → 1108.66] maybe that does need to include other people in the hierarchy but I think like that's a very
[1108.66 → 1114.72] important first step on the journey to being more of that okay the word owner is growing on me the
[1114.72 → 1121.82] more the more like an owner of things or a founder of things or really just a leader right it's not
[1121.82 → 1126.48] like you might not have the ability to make the ultimate decision at the end of the day that might
[1126.48 → 1132.22] still need to get made by a VP or by a director or by a tech lead or by somebody else, but that doesn't
[1132.22 → 1138.28] mean you can't shepherd the conversation or clear the path for that happening and I think that's the type of
[1138.28 → 1144.68] leadership that is implied in this essay and I think that does apply to you know you could have
[1144.68 → 1149.04] just started last week and these are things that you can be doing obviously you know mind the politics
[1149.04 → 1157.14] of your org lots of orgs get very unhappy if people freely communicate for usually bad reasons but if
[1157.14 → 1160.94] you're in an org where people where it's okay to just freely communicate which I think small startups
[1160.94 → 1167.40] usually are just go talk to people like don't be afraid to go out and facilitate action and
[1167.40 → 1168.52] movement of things
[1168.52 → 1183.96] okay friends I'm here in the breaks with Annie sexton over at fly, and you know we use fly here at
[1183.96 → 1189.32] changelog we love to fly it is such an awesome platform, and we love building on it but for those who don't
[1189.32 → 1196.76] know much about fly what's special about building on fly gives you a lot of flexibility like a lot
[1196.76 → 1202.52] of flexibility on multiple fronts and on top of that you get so I've talked a lot about the
[1202.52 → 1208.16] networking and that's obviously one thing, but there are various data stores that we partner with
[1208.16 → 1214.60] that are really easy to use um actually one of my favourite partners is Tigris I can't say enough good
[1214.60 → 1219.76] things about them when it comes to object storage I've i never in my life thought I would have so many
[1219.76 → 1225.64] opinions about object storage but I do now Tigris is a partner of fly, and it's s3 compatible object
[1225.64 → 1231.94] storage that basically seems like it's a CDN but is not it's basically object storage that's globally
[1231.94 → 1237.38] distributed without needing to actually set up a CDN at all it's its like automatically distributed
[1237.38 → 1243.34] around the world um, and it's also incredibly easy to use and set up like creating a bucket is literally
[1243.34 → 1249.28] one command so it's partners like that I think are this sort of extra icing on top of fly that
[1249.28 → 1254.54] really makes it sort of the platform that has everything that you need so we use Tigris here at
[1254.54 → 1260.28] changelog are they built on top of fly is this one of those examples of being able to build on fly
[1260.28 → 1264.94] yeah so Tigris is built on top of fly's infrastructure and that's what allows it to be
[1264.94 → 1271.08] globally distributed I do have a video on this but basically the way it works is whenever like let's say
[1271.08 → 1278.06] a user uploads an asset to a particular bucket well that gets uploaded directly to the region closest
[1278.06 → 1282.40] to the user whereas with a CDN there's sort of like a centralized place where assets need to get
[1282.40 → 1286.20] copied to and then eventually they get sort of trickled out to all the different global
[1286.20 → 1291.06] locations whereas with Tigris the moment you upload something it's available in that region instantly
[1291.06 → 1296.06] and then it's eventually cached in all the other regions as well as it's requested in fact with
[1296.06 → 1300.98] Tigris you don't even have to select which regions things are stored in you just get these regions for
[1300.98 → 1307.38] free and then on top of that it is so much easier to work with i I feel like the way they manage
[1307.38 → 1313.36] permissions the way they handle bucket creation making things public or private is just so much
[1313.36 → 1318.70] simpler than other solutions um and the good news is that you don't actually need to change your code
[1318.70 → 1323.80] if you're already using s3 it's s3 compatible so like whatever SDK you're using is probably just fine
[1323.80 → 1329.68] and all you got to do is update the credentials so it's super easy very cool thanks Annie so fly has
[1329.68 → 1335.82] everything you need over 3 million applications including ours here at changelog multiple applications
[1335.82 → 1343.16] have launched on fly boosted by global any cast load balancing zero configuration private networking
[1343.16 → 1350.10] hardware isolation instant wire guard VPN connections push button deployments that scale to thousands of instances
[1350.10 → 1358.56] it's all there for you right now deploy your app in five minutes go to fly.io again fly.io
[1358.56 → 1369.42] so angelica you manage teams of engineers like where do you have the same expectation of
[1369.42 → 1374.38] ownership right for juniors as you do with say people higher up the the the ladder you know like
[1374.38 → 1378.82] the seniors and the principals like do you have the same expectation of ownership I mean there is an
[1378.82 → 1386.74] expectation that if I delegate a specific problem to them that they take full ownership of that problem
[1386.74 → 1392.88] and they do all they can kind of as Chris alluded to like drive that problem forward
[1392.88 → 1400.64] pulling in the right people as they need it but I do think the spaces that I delegate
[1400.64 → 1407.04] ownership to various people do change like I would not I would delegate ownership of perhaps a smaller
[1407.04 → 1413.98] less complex problem to a more junior engineer I would delegate a larger more complex to a more senior
[1413.98 → 1420.78] principal engineer so I think the expectation of ownership is agnostic of levelling like there is an
[1420.78 → 1425.70] expectation you take ownership of your work, and you care about it, and you invest in it and that's kind of
[1425.70 → 1431.18] reading between the lines I may have misinterpreted but just by like when I saw founder mode that was
[1431.18 → 1435.30] what kind of excited me I was like yes like a founder is deeply invested they're excited they feel
[1435.30 → 1439.72] ownership in what they're doing, and they're invested so they want to see it through till the end
[1439.72 → 1447.12] so I think there is an expectation of ownership at every level but the space and the level of ownership
[1447.12 → 1454.34] I think changes a lot so i kind of I think it's more shared ownership as opposed to, and it's changing
[1454.34 → 1461.02] ownership I like at the beginning of a project i as the technical product manager I own that space
[1461.02 → 1466.70] I am defining it I am accountable for making taking ownership of like finding out what the problem is
[1466.70 → 1473.66] finding out how we can best solve it in a business sense I then delegate ownership of the problem to
[1473.66 → 1481.62] perhaps a tech lead to take ownership of how we technically solution and that tech lead might choose
[1481.62 → 1487.96] to share ownership of that decision with bringing in a dig analyst a data analyst bringing in a more junior
[1487.96 → 1492.36] engineer bringing in a fellow kind of Chris you've talked about this a little bit like lateral leadership
[1492.36 → 1498.82] bring in another engineer from a different team so I think it's its very fluid but I do think
[1498.82 → 1506.54] the idea of feeling ownership of your work and seeing it through and not just kind of throwing the buck over
[1506.54 → 1515.22] over the fence is really important i when I give ownership to my tech lead I am not relinquishing
[1515.22 → 1521.54] ownership entirely like I'm not going oh this is your problem now it's not mine I remain engaged I remind i
[1521.54 → 1527.80] I share in that ownership, but the core driver almost like the steward of that thing
[1527.80 → 1535.06] perhaps is a better word does change but I do think there is an ultimate and to your point Chris I think
[1535.06 → 1543.06] there is ultimately a decision maker i it might be deeply informed by you've stewarded you've had a lot of
[1543.06 → 1548.80] people steward the problem input a lot of decisions have sub decisions have been made but if there is a
[1548.80 → 1558.40] concrete decision to be made around like okay do we implement this in AWS or GCP and there's not you
[1558.40 → 1566.68] can't come to alignment perhaps it is the principal engineer who owns that decision or okay we want to
[1566.68 → 1576.12] build scheduling capabilities for push notifications or integration of images into emails ultimately like
[1576.12 → 1582.70] i might be the decision maker on that or i might be like both of these things are amazing i have to go
[1582.70 → 1589.20] upwards and be like hey i need a decision i need you to tell me which of these two you want my team to
[1589.20 → 1595.90] work on because i think they're both similarly valuable but I'm taking ownership of like i don't
[1595.90 → 1600.04] want to make this decision I'm not ready to make this decision I'm going to own the fact that i need
[1600.04 → 1608.22] of like input from above or from senior management so you're scoping, so there's a scope okay so what
[1608.22 → 1615.10] I'm hearing is yes ownership, but there's a there's a level right there's a scoping right to the ownership
[1615.10 → 1620.44] so I'm not going to expect the junior engineer that i just hired two weeks ago to be making decision
[1620.44 → 1626.26] you know to do multi-cloud or not all right that's not that's not a know ownership i want to give
[1626.26 → 1631.38] them right one they might not have enough context they might have the experience I've met some
[1631.38 → 1635.74] incredible junior engineers in my time, but they might have some context and experience for it but
[1635.74 → 1640.50] that is not a decision i want them to own sort of politically right um to use that term loosely
[1640.50 → 1647.16] within the organization right because i don't want them getting flack for if you know by some definition
[1647.16 → 1652.08] of wrong the wrong decision is made and the wrong sort of service provider is used like there are
[1652.08 → 1658.56] certain things that i as sort of the first on the defence for them right and some sort of
[1658.56 → 1664.28] hierarchy or some sort of structure i don't want them getting heat right for something that they
[1664.28 → 1670.26] shouldn't right so the decision the ownership I'm going to give them has to be scoped right to their
[1670.26 → 1676.78] level of responsibility so and therein there therein lies the the the i think there's a subtle
[1676.78 → 1682.12] contradiction happening here when when when I'm reading found them when I'm reading people and a
[1682.12 → 1688.12] lot of people are sort of chiming in online saying oh yeah like it wasn't my job to do x y and z and i
[1688.12 → 1694.46] just did it anyway you know found them out hashtag right so it's like you know people are like choosing
[1694.46 → 1701.82] like especially in a smaller startup environment where many people wear many hats right and it is
[1701.82 → 1706.44] you know lauded right to be able to sort of pickup a something and do something and that you
[1706.44 → 1710.66] weren't quote unquote hired to do, and you know basically you know being able to do like in that
[1710.66 → 1718.70] environment where seemingly scope and ownership seem to not like ownership carries more weight than scope
[1718.70 → 1724.94] does right so depending on where you are and what the culture of the organization is like I'm torn between
[1724.94 → 1730.92] sort of letting not having decision makers to use you know terminology we've been using before right I'm torn
[1730.92 → 1737.70] between sort of giving too much or not not not having i don't want to use term control but not
[1737.70 → 1744.52] having any sort of guardrails rights or guidance or sandbox right for figuring out what to do
[1744.52 → 1750.58] right like i can't have that and just let somebody you know perhaps shoot themselves in the
[1750.58 → 1755.70] foot because they're running you know and moving fast breaking things and broke the wrong thing ended up
[1755.70 → 1760.16] you know harming the business in some way right so i think it has to be it has to go hand in hand
[1760.16 → 1767.02] scoping of responsibility and ownership right have to go hand in hand and then being really clear
[1767.02 → 1772.96] when you give someone ownership that they understand the scope, and then you actually let them
[1772.96 → 1779.18] like let like you say hey this is your problem to be to solve these are the lines are my expectations
[1779.18 → 1787.06] these are the lines in which you can draw go crazy within these lines do you but then also once you
[1787.06 → 1793.26] say that don't then come in and start like getting in there and robbing stuff out within the books like
[1793.26 → 1799.40] set those really clear expectations and then let them do them and give them that ownership so i think
[1799.40 → 1806.72] i think there's a there's a little bit of a fall not fallacy category error maybe happening here like
[1806.72 → 1813.80] there is a difference between who owns something from a leadership perspective and who makes a decision
[1813.80 → 1820.48] and i think for any decision decisions always need to be made by the person who i think as you said
[1820.48 → 1826.52] johnny has the most context or like is the most affected or will do the work so if you're trying to
[1826.52 → 1832.70] make a decision between cloud providers that decision needs to be made by your operations team
[1832.70 → 1838.30] because those are the people that are going to be effectuating that decision, and so they need to
[1838.30 → 1844.98] own that decision, but they don't need to lead the process of coming to that decision, so these are
[1844.98 → 1850.34] two separate things that are very, very important especially as you move higher up in organizations like
[1850.34 → 1856.88] i think a failure of the manager model is that it tries to do this idea that i don't really know where
[1856.88 → 1861.16] it comes from i think this is how people think like the military works or something where like the people
[1861.16 → 1867.84] at the top make the decisions and communicate them down um, but you know once again if you read books
[1867.84 → 1873.76] on leadership like i do what you learn is that the command and control style of leadership yeah it
[1873.76 → 1878.84] doesn't work and the thing that you should do uh is you want to push decisions down and have
[1878.84 → 1884.66] communication flow up uh like this is how modern militaries work the people at the top aren't making
[1884.66 → 1890.18] decisions about you know what strategic things to do at like an action level those are the people on the
[1890.18 → 1894.80] ground that are doing it those are the squad leaders that are on the ground actually going to
[1894.80 → 1899.82] do the work the generals are just making sure the information is flowing so that those people that
[1899.82 → 1904.42] have to make the decision have all the information that they need to make that decision properly
[1904.42 → 1910.72] and i think that that is the type of dichotomy that we need to have within our companies and within
[1910.72 → 1916.26] like any type of you know decision-making capacity so even if like say because of org structure
[1916.26 → 1921.56] you are someone that ultimately has the decision-making authority because of how things are
[1921.56 → 1928.40] structured now a great way to do this i guess leadership thing would be to find out who's actually
[1928.40 → 1932.66] going to be the most affected by this who's going to have to go implement this and go talk to them and
[1932.66 → 1939.78] then transfer that decision-making apparatus to them and say ultimately your decision is the one that
[1939.78 → 1946.36] matters here because i don't have the right context to make this decision and that happens at you know
[1946.36 → 1953.18] all levels of being in an org from the hippy top all the way down and i think too with you know
[1953.18 → 1958.70] leadership one of the interesting things that is in a book called good to great there's this thing
[1958.70 → 1963.20] called level five leadership, and it's one of the things that can make a company absolutely fantastic
[1963.20 → 1967.64] it's a good book go read the book but one of the things they found is that these level five leaders
[1967.64 → 1973.40] are spread throughout the entire organization i think level five you can kind of more or less
[1973.40 → 1978.48] translate that into founder mode for the purpose of this podcast sort of kind of they're different
[1978.48 → 1983.78] concepts but they kind of effectuate the same thing but like they're all throughout an organization
[1983.78 → 1989.12] and they're not people that get like there's no one going around decreeing who a level five leader
[1989.12 → 1995.10] is it's just people that have a very specific type of mindset that enables them to do this work
[1995.10 → 2000.94] enables them to pull people together and make things happen and a major component of that which i think
[2000.94 → 2010.60] is kind of in this like hidden in this founder mode idea is that your ego and the needs of the
[2010.60 → 2018.58] organization become aligned, so your ego is no longer about you, it's about making sure that the best thing
[2018.58 → 2025.32] for the organization happens and that's like a really key property of a level five leader and i think
[2025.32 → 2030.90] that that is something that once again anybody at any part of the org can do where you don't have
[2030.90 → 2036.86] to be decreed by someone on high to go and be like I'm going to figure out like what's the best what's the
[2036.86 → 2042.50] the best thing we can do for the org not for me personally but for the org as a whole whatever the org is for you
[2042.50 → 2047.78] whether that's just your department or your team or the whole company and then start pushing forward
[2047.78 → 2054.22] initiatives for that in whatever way that you can at the end of the day so I think like that
[2054.22 → 2060.04] like I guess that's why like at the end of the day I think that separating out this decision-making
[2060.04 → 2065.84] apparatus from that leadership apparatus is like a key point in actually being able to be much more
[2065.84 → 2071.76] effective in leading things and making things happen which is kind of what this founder mode thing
[2071.76 → 2076.28] feels like is also like actually being able to get things done at the end of the day
[2076.28 → 2081.92] and make things happen because I think that's what founders do when they're running a company it's like
[2081.92 → 2088.46] yes I want to accomplish things not necessarily deal with a bureaucracy how how how should this affect
[2088.46 → 2097.68] my approach to code if is at all I mean it's the same sort of thing of you know i the way I like to
[2097.68 → 2103.62] think about it is who is going to have to like you know who's going to be the most affected by
[2103.62 → 2109.88] you know this change in the code that I'm making like am I the right person to be writing this code
[2109.88 → 2114.76] or do I need help from somebody else or if I need to write this and I don't understand it and there's
[2114.76 → 2119.60] no one else to write it who can I go out to get information for to make sure I write this in the right
[2119.60 → 2124.74] way instead of just you know trying to figure out myself because I was vested as the person that is
[2124.74 → 2128.74] supposed to be writing this code okay so let me pause you let me give you an actual scenario
[2128.74 → 2136.78] right and I want both your take and angelica's take on this so imagine you work at a fairly
[2136.78 → 2142.62] large organization right you are an engineer you know junior senior doesn't matter you are tasked
[2142.62 → 2147.76] with delivering a solution right that's the job deliver a solution nobody's asking you know telling
[2147.76 → 2153.66] you what lines of code to write where to go put your module or package you know what services
[2153.66 → 2160.56] the deployment nobody's telling you the tech like as you said the tactical steps toward achieving some
[2160.56 → 2167.22] some desired goal which fits into some strategy you know from leadership right you the tactical
[2167.22 → 2175.76] implementation is yours, and you know that in order for you to deliver said solution there needs to be
[2175.76 → 2181.08] involvement from at least two teams right teams that don't normally work with each other, but they are
[2181.08 → 2188.64] they are you know distinct teams right you've tried on multiple occasions to collaborate right to
[2188.64 → 2195.08] communicate right you own the solution your job is to deliver the solution so you own it right
[2195.08 → 2201.40] by definition of what we've been talking about, but you just can't seem to move the ball forward
[2201.40 → 2207.88] whatever you need to do you are able to and ready to do, but you can't seem to get all the ducks aligned
[2207.88 → 2214.40] right so in that setting right, and we'll start with you angelica and that setting what is the
[2214.40 → 2220.52] expectation right for this engineer who finds themselves right who they are willing and able
[2220.52 → 2229.10] but they just can't seem to deliver right through no fault of their own seemingly how do I own anything
[2229.10 → 2234.96] and how do I go founder mode in this setting I mean from my perspective I think you
[2234.96 → 2243.76] because you own the solution and not how do we make it happen logistically across teams like your
[2243.76 → 2252.34] your ownership is the implementation of the solution you think is best not the ownership of logistically
[2252.34 → 2260.80] how do we get this done cross team collaboration if I was that engineer knowing my box and knowing this
[2260.80 → 2266.46] is outside my box of ownership ideally that would have been set out clearly I would then go to the
[2266.46 → 2274.00] person who does own that which would be a project or a product manager and I would own the fact that i
[2274.00 → 2284.26] need help and I would stay be very, very clear and own clearly articulating what I need why I need it when i
[2284.26 → 2292.24] need it and who I need it from to that person and empower them to do their job and what they own
[2292.24 → 2299.16] and own keeping them accountable i if I flag it to my product manager and two days go past and nothing's
[2299.16 → 2304.28] been done I should own the follow-up of being like hey I brought this to you two days ago I really need
[2304.28 → 2311.36] this flagging again that like if you need me to do xyz if I'm going to own this solution what I need from you
[2311.36 → 2316.72] is xyz and I think that's like taking ownership of driving that forward even if you're not the one
[2316.72 → 2322.50] actively doing the things to make it happen right then is in my mind that kind of founder mode like
[2322.50 → 2328.12] you're not just throwing it over the fence you're taking accountability you're just asking for someone
[2328.12 → 2334.60] else to do something for you to help drive that forward yeah I think that's how I would think about
[2334.60 → 2340.70] it and then as soon as I get what I need, I haven't I'm still owning that solution I just have what I need
[2340.70 → 2347.10] to keep driving that forward yeah as opposed to throwing your hands up and saying I can't do it
[2347.10 → 2352.20] I can't do it right yeah well i think like if you is there are other teams that are not
[2352.20 → 2360.10] for whatever reason doing what they need to do to participate then the know you become the
[2360.10 → 2365.04] contextually uh correct person to be making decisions like if there's some decision that needs to get
[2365.04 → 2369.80] made, and it requires one of these teams, and they're not engaging a like you probably have
[2369.80 → 2374.12] some deadlines so you're now the one that makes the decision and that team that didn't participate
[2374.12 → 2377.94] I mean I would say definitely document it so if they come back later they'll say well we weren't
[2377.94 → 2381.74] involved it's like well I tried here are the emails here's all the communication you didn't want to
[2381.74 → 2387.78] participate so we had to make this decision but I would say that that is likely a sign of an
[2387.78 → 2394.90] organization that is a little toxic and needs some help um and I think that's something that could be
[2394.90 → 2399.50] that you as the person who's like responsible for this thing that kind of spreads across teams now
[2399.50 → 2405.40] should run that up whatever hierarchy you have to figure out why these problems are occurring like
[2405.40 → 2411.12] you can own at least attempting to resolve some of these problems by you know maybe it is going to
[2411.12 → 2415.74] your skip level manager or skip level and saying you know we have these teams we have this project
[2415.74 → 2421.12] it's super important but no one's communicating can we figure out what's happening and how we can start
[2421.12 → 2426.28] resolving it so that people are coming together again so that the right people can be making the
[2426.28 → 2431.90] decision so that you know that I don't make a wrong decision so short term you got to make the decision
[2431.90 → 2439.16] if you're running against a deadline but long term that's a symptom of organizational problems that
[2439.16 → 2444.58] need resolving right and yeah you don't own the company, but that's why we're kind of talking about
[2444.58 → 2450.44] this founder mode idea or the idea of like your ego becomes aligned with what is best for the
[2450.44 → 2455.02] organization as a whole what's best for the company and if you know teams aren't communicating
[2455.02 → 2462.96] that is not going to result in a know an effective organization in a company that is as
[2462.96 → 2467.66] successful as it should be so that's where you can run it up the ladder, and you might fail you might get
[2467.66 → 2472.46] pushed back and there is always politics, so someone might say like well we can't do this because
[2472.46 → 2478.38] that manager is just like you know overwhelmed or not too good at their job or whatever but I think
[2478.38 → 2485.32] the founder mode or the leadership idea is that you at least try and fix it and try and find a
[2485.32 → 2491.82] remedy or try and start a remedy uh from happening but in the immediate mode if you know you have to
[2491.82 → 2497.16] deliver something so make the decision and then move forward, and you know people complain later
[2497.16 → 2502.88] well they complain later, and you say well you had your chance, and you didn't say anything and if
[2502.88 → 2507.94] your leadership comes back and says oh well turn around do it a different way then it's probably time
[2507.94 → 2514.00] to find another job uh like if i kind of feel like the way that you're the way that you're explaining
[2514.00 → 2521.18] that though Chris I think that is a more toxic work environment to me in what way like doing pushing
[2521.18 → 2525.94] forward and like breaking eggs and having people be like why did you break these eggs like why didn't you
[2525.94 → 2532.36] include us why didn't you I mean that that seems to like so disparity between teams that had you just
[2532.36 → 2539.24] had the conversation like talked about it more openly flagged it in a way that didn't feel quite so
[2539.24 → 2546.14] like combative like that could have yeah like I think if you might spend more time in conversations
[2546.14 → 2552.62] not doing work but I do think that actually lends itself to a healthier work environment if you're able
[2552.62 → 2558.48] to stop and be like hey I have this problem the ideal solution involves these two other teams
[2558.48 → 2565.00] they benefit of the doubt aren't giving me the time of day maybe they don't mean to maybe they're just
[2565.00 → 2570.30] like on tight deadlines themselves let me like to own the fact that like this is the problem I'm gonna
[2570.30 → 2575.12] identify it I'm going to make sure those involved know what the problem is let's collaborate together
[2575.12 → 2583.50] to solve it as opposed to like oh this is a problem let me like drive the premise I had started with
[2583.50 → 2590.26] was that this that communication had already been attempted oh and that you were not getting any
[2590.26 → 2595.44] response back obviously the first step is to go talk to the teams like you don't just make a decision
[2595.44 → 2600.14] like the whole point of what I was saying is like okay you own this you need these other two teams or
[2600.14 → 2606.84] these other two teams have the context to make the decision okay go talk to them then if they is
[2606.84 → 2609.68] they're like you know they're not giving the time, but they're not responding to emails they're not
[2609.68 → 2615.30] communicating with you that's when you need to a project yourself by making sure that your project
[2615.30 → 2620.26] doesn't fail or what you need to do doesn't fail simply because someone else isn't doing their job
[2620.26 → 2624.68] or isn't holding up their end and then try to resolve whatever the problem was with why they weren't
[2624.68 → 2628.62] holding up their end but obviously the first step if you get a project that involves multiple
[2628.62 → 2634.46] people or multiple teams is to go talk to those teams that's that's absolutely required or
[2634.46 → 2641.18] start opening PRS and in their repos you now and then adding hashtag founder mode at the bottom
[2641.18 → 2648.32] you all can't get to this I'm gonna start doing it for you, I'm in founder mode damn it
[2648.32 → 2658.58] oh man yeah okay so I think overall there's an I think that there is consent you know
[2658.58 → 2664.84] the styling the style may be a little different but there is consensus right on what founder
[2664.84 → 2671.12] mode really should mean you know even if you're not a founder uh all right so the there is
[2671.12 → 2675.82] something to be gained even if you're not technically you know incentivized you know monetarily or
[2675.82 → 2682.00] otherwise right by not being a founder yourself right there there is value in in in taking
[2682.00 → 2688.10] ownership of things there is value and sort of really ultimately what it sounds like is learning how to be a
[2688.10 → 2693.40] better communicator uh to me ultimately I think which somehow seems to always come down to that
[2693.40 → 2699.14] right learn to be a better communicator whether it be through your code through cross team collaboration
[2699.14 → 2705.18] through you know whether it's managing up as they say it's all ultimately could all just be better
[2705.18 → 2710.28] communication and founder mode really to me is all about sort of that communication combined with
[2710.28 → 2714.06] um sort of initiative right taking initiative to do things
[2714.06 → 2732.64] what's up go time friends I'm not sure how you're using a VPN but I want to tell you about
[2732.64 → 2742.18] a new sponsor a new friend of ours nordvpn is for everyone it's easy to use over 6 300 servers
[2742.18 → 2748.22] worldwide change your virtual location to pretty much anywhere and one of the things I love most
[2748.22 → 2755.32] about NordVPN is their amazing speed they have one of the fastest VPNs out there and every major
[2755.32 → 2765.18] platform is supported windows android iOS macOS Linux and even android TV that's cool and the best way
[2765.18 → 2773.06] to get started is to go to nordvpn.com slash go time because hey they love go time it's risk-free
[2773.06 → 2780.22] with word's 30-day money-back guarantee get NordVPN's two-year plan plus four months extra
[2780.22 → 2785.52] again nordvpn.com slash go time
[2785.52 → 2795.28] so I think with that I think it's a good time to transition into unpopular opinions which I think
[2795.28 → 2800.22] I think there might be a couple after this this chat
[2800.22 → 2824.06] all right who wants to who wants to lean on me first I think a child should go first
[2824.06 → 2830.86] you're volunteering I mean I haven't got one that's poor leadership of you
[2830.86 → 2836.76] hey Chris you're not you know that's not why don't you go founder mode and own this one
[2836.76 → 2842.76] you've reached out to another team they're not responsive
[2842.76 → 2849.94] I respond you take ownership I mean I drive forward I got unpopular opinions for days
[2849.94 → 2857.12] so let's see what should I what should I start with I think like something I've been pondering a lot
[2857.12 → 2864.90] lately is that this industry needs more people with like liberal arch degrees like especially
[2864.90 → 2874.80] needs more English majors because I am very annoyed at uh this industry's inability to use English words
[2874.80 → 2880.50] properly like just we're bad we're bad at it and I'll give you an example of something I've been
[2880.50 → 2887.84] thinking about a lot lately which is that the words concurrent synchronous and parallel are all synonyms
[2887.84 → 2894.96] for each other they mean slightly different things but they are all equivalent roughly
[2894.96 → 2901.48] and yet we use them to mean completely different things right like something that's concurrent is not
[2901.48 → 2905.94] necessarily parallel and synchronous isn't even used when we're talking about concurrency or parallelism
[2905.94 → 2911.42] it's talking about something else entirely even though synchronous and parallel basically mean the same thing
[2911.42 → 2940.42] and to go on this rant a little bit more parallel implies non-convergence also so like concurrency and parallelism are like also like the way that we use them is just wrong right, but the other thing about this is that right concurrent and synchronous are synonyms and synchronous and asynchronous are antonyms they mean the opposite thing but like people use concurrent and asynchronous
[2940.42 → 2946.70] asynchronous to basically mean the same thing which doesn't make any sense right if you're like oh I'm
[2946.70 → 2968.42] going to go write this code in a concurrent way if someone has said asynchronous instead you'd be like yeah okay that's a word that would also fit there fine so now we have a situation where we have all these words and the ones that like we're saying mean something similar in the actual language mean opposite things which just doesn't make a lot of sense and that's just really annoying me
[2968.42 → 2980.54] and I think this is a case where like we need to try better to look up the definitions of words and actually use etymological references to understand what the meaning of words are
[2980.54 → 2990.70] because we're terrible at it, and it's making us look really dumb, and it's also making it very difficult for other people to learn how to be good software engineers or understand software engineering at all
[2990.70 → 2998.86] and I think we also end up confusing ourselves often okay my unpopular opinion is English is hard ignore Chris
[2998.86 → 3005.74] it's not that hard I mean you're wrong it's not that
[3005.74 → 3012.02] it's not that hard
[3012.02 → 3019.70] all right it's I mean a thesaurus that's all you need that's all you need a thesaurus look at the word
[3019.70 → 3025.22] and before you name something make sure like it doesn't mean the opposite of what you mean
[3025.22 → 3033.36] it takes too long it takes too long evidently if you don't have time okay here's a here's a spicier take
[3033.36 → 3040.64] if you don't have time to actually look up how what words mean then you should not be writing software
[3040.64 → 3048.46] oh okay well that's yes that's yeah we'll let the people decide we'll let the people decide I mean
[3048.46 → 3051.96] hey at the end of the day we're all writers so if you aren't going to respect the writing
[3051.96 → 3060.40] profession you can get out that's all oh, oh you woke up this morning and chose not health not healthy
[3060.40 → 3068.08] okay spice I mean i you know the spice must flow you know what it is like when I try to explain
[3068.08 → 3075.32] like these concepts are not like it isn't difficult to understand what is happening if you use words
[3075.32 → 3080.64] that make sense but I think the problem is that since we don't use words that make sense we wind up
[3080.64 → 3085.98] confusing ourselves about what is actually going on and we wind up making words be meaningless like Sam
[3085.98 → 3091.86] Newman has a talk about how asynchronous as a word is now completely meaningless because in order to
[3091.86 → 3096.46] understand what someone means when they say that word you have to shove so many other contextual words
[3096.46 → 3101.48] around it that you might as not you might as well not even say asynchronous, but it's also like
[3101.48 → 3106.72] synchrony is a good example right because if you think about let's say the event loop like in JavaScript
[3106.72 → 3112.94] where you say okay well that is asynchronous programming because you know you have a callback that gets
[3112.94 → 3117.82] returned to you, or you use async await which is just kind of a way of wrapping around callbacks you're
[3117.82 → 3123.34] like okay that's asynchronous and I would ask why do we think that that is
[3123.34 → 3128.56] synchrony like not in time like what is the measure of time that we're talking about
[3128.56 → 3135.42] right that it's its concurrency it's concurrency with other things that you aren't running but as far
[3135.42 → 3142.06] as the logical time of your application it's still synchronous right if you do async await if you call
[3142.06 → 3149.60] await your thread of execution logically stops and then goes again, and it's just still operating with
[3149.60 → 3157.68] time so if you say asynchronous means like without time or without a know logical step with
[3157.68 → 3162.96] time what time are you even talking about right i think that people that name these things
[3162.96 → 3168.52] didn't think about any of this at all which is why the names are rather silly but I think it does have
[3168.52 → 3173.32] rather large consequences on us as an industry because we wind up designing things that just
[3173.32 → 3179.86] don't really work that well for you know because someone came up with a word, and they named it that
[3179.86 → 3183.50] way we didn't really understand the concept that well but everybody's using it so it's popular right
[3183.50 → 3188.94] like I recently started trying to learn swift and I got to the part of the concurrency model of swift
[3188.94 → 3194.60] and I was like you know didn't the dude write uh robert angstrom I think his name is didn't he
[3194.60 → 3199.54] write what colour is your function article like so long I guess he did write it after swift was
[3199.54 → 3203.26] created, but it's like you wrote it so long ago it's like why are we still having languages that
[3203.26 → 3207.46] have this problem of these coloured functions, and you can't really call one from the other because
[3207.46 → 3212.84] of the weird models of synchrony and synchrony like we as an industry shouldn't be making these
[3212.84 → 3216.28] mistakes because it makes it really hard to program, and it makes it really hard to get our programs
[3216.28 → 3222.00] correct, and you know popular opinion go got it right with go routines where it's like everything
[3222.00 → 3227.98] is synchronous you can just call go, and it just works I'm just filled with spice today lots of spice yes
[3227.98 → 3236.76] indeed before you go on another rant Chris I'm going to stop you right there hey we can do some plus
[3236.76 → 3244.32] plus bonus content no, no no, no no, no people have we people have managing and delegation to go do
[3244.32 → 3250.36] and then ownership to go ahead I literally have a meeting after this that is about delegating some
[3250.36 → 3255.48] tasks to my team so we'll just delegate running the meeting to somebody else angelica that's how this
[3255.48 → 3261.66] works right I did I'm done it i dedicated it but I'm taking founder mode and I will be in the meeting
[3261.66 → 3266.58] listening to every word they say and making sure that everything just sends some random person hashtag
[3266.58 → 3270.66] founder mode, and it's kind of like tag, and now they're the one that has to do founder mode and you
[3270.66 → 3275.16] can just stay here and talk without I don't want to go to the board next week and be like sorry i just
[3275.16 → 3277.40] let the team do whatever hashtag founder mode
[3277.40 → 3285.06] but have you tried it all right let's not start another rant all right thank you listener
[3285.06 → 3291.44] for being on this episode with us and hope you had fun along with us with that we'll see you on the
[3291.44 → 3291.90] next one
[3291.90 → 3302.52] that is go time for this week thanks for listening you know what's cool free stickers during the month
[3302.52 → 3308.46] of September we are mailing out changelog sticker packs to everyone who leaves us a thoughtful
[3308.46 → 3315.56] five-star review or blog post about our pots simply email proof of your review to stickers
[3315.56 → 3322.56] at changelog.com alongside your address, and we'll mail out the goods anywhere in the world once again
[3322.56 → 3329.74] that's stickering at changelog.com picks, or it didn't happen only in the month of September let's do this
[3329.74 → 3336.16] thanks once again to our partners at fly.io to our beat freaking residents the one and only
[3336.16 → 3343.34] brake master cylinder and to our longtime sponsors at sentry use code changelog when signing up for a
[3343.34 → 3348.82] new century team plan and save 100 bucks too easy that's all for now, but we'll talk to you again next
[3348.82 → 3350.18] time on go time
[3359.74 → 3368.76] Enjoy complimentary
[3368.80 → 3371.54] regular
[3371.54 → 3372.10] cake
[3372.16 → 3373.50] Ö
