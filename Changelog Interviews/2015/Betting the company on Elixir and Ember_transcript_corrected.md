[0.00 → 15.52] welcome back everyone this is the change log and I'm your host Adam stikowiak this is episode 165
[15.52 → 22.60] and on today's show jarred is going solo all by himself talking to Brian saltarello from
[22.60 → 31.12] dockyard about betting the company on elixir and ember good show we have three awesome sponsors
[31.12 → 38.94] code ship code school and hip chat our first sponsor is code ship they launched a brand new
[38.94 → 44.64] feature called organizations now you can create teams that permissions for specific team members
[44.64 → 50.50] and improve collaboration in your continuous delivery workflow maintain centralized control
[50.50 → 56.60] over your organization's projects and teams with code ship's new organization plan you can save 20
[56.60 → 61.66] off any premium plan you choose for the next three months by using the code the changelog podcast
[61.66 → 68.42] again that code is the changelog podcast 20 off any premium plan you choose for three months
[68.42 → 73.32] head to code ship.com slash the changelog to get started and now on to the show
[73.32 → 85.52] welcome back everybody jarred here I am fresh off of our trip to Denver for gopher con 2015
[85.52 → 91.44] I just want to give a quick shout out to all of our new gopher friends and listeners and trust me
[91.44 → 98.12] we lined up a ton of go related shows in our pipeline more on that later, but we had tons of
[98.12 → 102.20] fun hanging out t-shirts and shooting video interviews with everybody in fact if you're
[102.20 → 108.30] wondering where is the mellifluous voice of Adam stack he's actually heading down in the editing room
[108.30 → 113.80] this week turning all of our raw footage from the conference into something awesome but don't worry
[113.80 → 118.92] Adam will be back next week, and we will welcome Toby Knapp who is a CTO of mesosphere to the show
[118.92 → 125.34] stay tuned for that but today I'm joined by Brian Cartagena who is the CEO of dockyard
[125.34 → 132.34] dockyard is a web and mobile user experience consultancy in Boston Massachusetts Brian thanks
[132.34 → 137.26] so much for joining me thanks for having me so did I do you justice in the intro anything else you
[137.26 → 144.00] want to say about yourself um as a way of introduction uh no that's it I'm sure we'll touch on a bunch of
[144.00 → 150.36] stuff yeah yeah absolutely Brian I think I was thinking back of when you first came across my radar
[150.36 → 157.90] and in the open source world and I think it was with your client side validations gem yeah which
[157.90 → 163.96] for those who don't know was a ruby gem and I think it was probably only in the context of rails
[163.96 → 172.64] um which purpose was to give us the ultimate kind of dry uh validations where you define them once in
[172.64 → 179.08] your models, and then we can actually like traverse them down into uh I think probably jQuery back than
[179.08 → 186.48] into validations in the client side right so it will allow you to write them once they'd export
[186.48 → 193.74] actually there was some before I even knew uh what transpiration was yeah it kind of did some ruby to
[193.74 → 199.38] JavaScript transpiration really, really bad right um, but it's interesting because client side of
[199.38 → 208.40] validations has kind of was my first like use case for how I've been writing code over the next few years
[208.40 → 214.74] so like client side validations was uh what motivated me to want to get more heavily interested in
[214.74 → 222.12] client side application development and specifically um something as uh complex as ember yeah I mean i
[222.12 → 227.90] remember with the gem because that gem came out and it spoke to me very uh very tight
[227.90 → 233.22] like inherently I was like yes this is something that we need something that I know I needed um and so i
[233.22 → 237.84] started using it and I think I can't remember if I contributed back I definitely did some bug reports for
[237.84 → 245.54] for you back in the day yeah, and it seemed like uh a great goal, but it just was a difficult thing for
[245.54 → 250.92] you to achieve I think it I think it was working well, but there were a lot of issues um did you
[250.92 → 257.68] struggle to actually like to execute on that idea uh well the way that i wrote it originally yes so
[257.68 → 265.38] what client side validations was doing under the hood was that it was trying to uh attach all these
[265.38 → 273.72] validation rules to input elements, and it was basing it off of string values and then there was all this
[273.72 → 279.14] you know crazy rules in the back end uh I'm sorry I mean within the library not on the back end right
[279.14 → 283.60] um and that's not even taking account of like remote client side validations the uniqueness
[283.60 → 290.70] validator was a whole mess yep but what I came to realize pretty early on and this is what I mentioned
[290.70 → 296.24] now I got became interested in ember was that uh client side validations really needed a model to
[296.24 → 301.50] work against needed like a like a user model or something where you're actually going against
[301.50 → 309.20] specific values rather than just trying to piecemeal all these values off of input elements and so when i
[309.20 → 315.02] was uh building on client side validations I actually went down the path I don't know if the branch
[315.02 → 320.72] still exists on the repo um but I still went down the path of building out a very, very small and
[320.72 → 326.08] probably very poorly thought out like client side framework just for re-implementing clients that
[326.08 → 332.48] validations and I got to the point like this is crazy I'll start looking the backbone um backbone
[332.48 → 338.40] didn't really interest me and that's where ember was starting to get on my radar and i I went off in
[338.40 → 346.76] that direction and then I realized that um this whole at least for me the nature of server side
[346.76 → 353.72] application development um was really I think going to fall by the wayside and client side application
[353.72 → 359.46] development was going to be the next big thing and so for someone that's running a business i really
[359.46 → 365.54] wanted to get ahead of that curve and start establishing expertise there so i kind of dropped
[365.54 → 371.94] client side validations off of my plate sorry for those that were using it um i I did do I did
[371.94 → 378.20] due diligence to try to find a replacement uh author um I put the radar i i I maintained it for
[378.20 → 383.60] like six months I asked people if they wanted to take it over didn't get any takers and so i finally
[383.60 → 388.48] sunset it however I think someone has taken it over now I gave somebody I don't know if they're still
[388.48 → 395.04] working on it but i uh I gave them somebody uh the ruby gems access, and they own the repo now
[395.04 → 401.24] so um hopefully it's found a good home but uh yeah that that was always an interesting project
[401.24 → 408.48] from an um a technical point of view of trying to get ruby over to JavaScript but also from an uh
[408.48 → 414.30] point of view of okay I realized that this is the completely wrong direction for implementing this
[414.30 → 421.90] and it's kind of taken me on this crazy journey to really becoming very well versed in clients
[421.90 → 426.76] application development yeah and I think as we know as this conversation progresses we'll
[426.76 → 431.52] probably take that journey a little bit I want to also mention something that you do annually which
[431.52 → 437.32] I've been a fan of over the years um you know we just met but I've been kind of following dockyard
[437.32 → 443.74] to a degree because I'm also a consultant uh you know I have a software company you know employee
[443.74 → 449.52] number one uh and I've always flirted with growing and not growing and the ideas behind it
[449.52 → 454.08] um so I follow other people that are doing that I follow thought bot to a degree and dockyard
[454.08 → 460.46] and just kind of watch you know like to watch what you're doing, and you make that really easy because
[460.46 → 467.46] you publish these lessons learned post annually um which is kind of a year in review it's kind of
[467.46 → 474.16] the entire life of your consultancy um and man you're like crazy transparent in that post
[474.16 → 480.14] like I feel like your just kind of bear it all there and I'm curious uh why you do that and
[480.14 → 487.38] and just have you talk about that so several reasons um first I think it's just in my nature
[487.38 → 494.92] I tend to I guess wear my emotions and myself on my sleeve to a certain degree I think anyone that
[494.92 → 500.30] follows me on Twitter kind of gets too much of that from time to time I do a lot of twitter
[500.30 → 504.04] complaining because I think that's the primary purpose of Twitter is just like
[504.04 → 511.64] complain about things yeah yeah um and uh but the other reason which is probably a more
[511.64 → 521.46] um like politically correct thing to say rather is that um when I was getting going with dockyard when
[521.46 → 529.18] i when I was because I was a freelancer i I worked in enterprise I worked in startups and i I finally had it
[529.18 → 534.52] with that world and I said I'm going to work myself and i I went and started freelancing i very quickly
[534.52 → 539.48] realized that I've really traded one boss for like you know 10 or 20 bosses exactly yeah whoever
[539.48 → 545.26] however many you happen to have during a given year um that's not really any more freeing uh but
[545.26 → 553.86] I started getting um more and more complex projects pushed my way stuff that required more than just me
[553.86 → 560.54] so I reached out to a few people and uh we just said we were working on a project we worked well
[560.54 → 567.22] together we decided okay let's give this a shot and start a company at the time my LLC was uh
[567.22 → 573.60] horribly named it was dirty water development uh for those that are from Boston yeah, yeah so for
[573.60 → 578.26] those that are from Boston and that are Red Sox fans that's the song that the Red Sox play the
[578.26 → 585.26] stand ells love that dirty water uh yeah it's an it's an um reference that went over everybody's head
[585.26 → 593.42] nobody got it especially in light of when i was doing business under that LLC was when the gulf
[593.42 → 600.56] oil spill happened oh no everybody thought that this was somehow a tongue-in-cheek reference the gulf oil
[600.56 → 607.10] spill which was not the case so i uh I think I realized very quickly that this was a bad name um
[607.10 → 614.46] and I'm an i I race sailboats I want to do something nautical so i I really do want shipyard
[614.46 → 619.10] because I'm like oh shipyard shipping software that makes sense right however there
[619.10 → 626.60] is a shipyard bear uh beer in Maine, and they own that domain name i uh and so dockyard was the uh the
[626.60 → 634.02] next obvious choice for me and to go back to your original question i I started when I was starting
[634.02 → 640.32] the company I was starting from zero right I never run a company before um I grew up in a family like
[640.32 → 646.04] my father ran his own company my grandfather ran his own company but uh very different businesses uh
[646.04 → 651.62] so i kind of got a sense of what it takes to um like the effort that goes into running company but
[651.62 → 657.04] as far as the specifics around running a software consultancy I really had no one to ask I emailed a
[657.04 → 663.14] few people that were doing it and what I realized very fast is that a lot of these shops are
[663.14 → 669.16] they're just using people they're lying they're they're saying everything's great everything's
[669.16 → 674.84] awesome because they feel that they have to put forth this image of excellence and anytime that
[674.84 → 679.62] there is anything that's negative about them out there they fear that they're going to lose out on a
[679.62 → 683.98] contract they're going to lose out an employee they're going to lose out on anything and so they just
[683.98 → 688.88] say everything's great everything's awesome all the time and I don't think that people learn
[688.88 → 695.62] from people's successes because I think success is fleeting success is very difficult to duplicate
[695.62 → 703.32] uh it's usually time-based it's luck-based you happen to be fortunate enough that you were in the
[703.32 → 709.02] right place at the right time and things worked out for you that's I think the significant key to
[709.02 → 714.24] success sometimes effort and persistence is definitely part of that, but persistence actually just means that
[714.24 → 720.72] you're able to stick it out long enough so that you get lucky uh failures are super easy to duplicate
[720.72 → 726.42] failures happen all the time and the way that you fail is probably very similar to the way that I fail
[726.42 → 733.20] and telling me how you failed will allow me to help cope with and avoid that particular failure or at least
[733.20 → 740.08] minimize the damage and nobody wanted to talk about their failures so i I decided early on that
[740.08 → 745.28] um if we can make it to one year I'd actually I think I did the first one after six months
[745.28 → 750.26] and I wanted to share those lessons with people because I didn't see those lessons anywhere else
[750.26 → 760.10] uh they were more of a cathartic thing for me and uh i I wasn't sure if anybody would like them
[760.10 → 766.74] but they tend to uh get a lot of attention um I think that annually they're definitely the most
[766.74 → 772.54] red blog posts at least at the time when I published them uh we have some uh ember posts that
[772.54 → 780.08] I think overall have gotten more traffic but um yeah i kind of i I talk about what went well
[780.08 → 784.88] what didn't go well what changes we can make in the upcoming year I talk about how much money we've made
[784.88 → 790.78] it's stupid not to talk about money right people don't like to share like the revenue they don't like
[790.78 → 796.92] the share their rates I don't know why maybe there's a like a perfect business
[796.92 → 801.46] school reason not to do it but I didn't go to business school it's never hurt us in any way
[801.46 → 807.06] um and I really wouldn't want to run a company that we wouldn't be able to talk about these type of
[807.06 → 813.06] things i if we end up losing if we end up doing worse one year yeah it will be embarrassing to say
[813.06 → 818.48] that we didn't make as much money this year as we did last year, but that's you know ultimately
[818.48 → 825.78] that lies upon me and I need to own that so do you where do you draw the line do you have a line
[825.78 → 830.98] do you have you thought about that or do you just uh bear it all whatever you feel like
[830.98 → 836.38] saying in this kind of posts or are they if it impacts one of my employees directly or a former
[836.38 → 841.96] employee it won't be brought up unless I've discussed it with them already gotcha so a good
[841.96 → 849.52] example of that um I've discussed firing people and um one of the employees specifically was actually
[849.52 → 855.10] one of the co-founders of the company and everyone hears this word firing, and they think oh that's
[855.10 → 860.68] that's bad, but it's what it is like we didn't lay them off we didn't dismiss them they were fired and
[860.68 → 868.50] there's no two ways around it um and I discussed it with him, I said I want to discuss this within this
[868.50 → 876.24] context in that you know perhaps in this case I was wrong uh i I did not you know adequately set
[876.24 → 882.82] so within that for that specific person i I spoke about how uh what ended up happening was when
[882.82 → 889.00] we co-founded the company we never set expectations upon people's roles and everything kind of fell upon
[889.00 → 895.36] me and I was getting frustrated and I think the lesson learned there was that when you're starting a
[895.36 → 901.24] company you should probably not even uh amongst your co-founders not even split up uh ownership
[901.24 → 905.24] percentage until maybe six months in when you get a sense on like okay here's what people are really
[905.24 → 911.94] doing because beforehand you can dream up like oh you're going to do this I'll do that and then reality
[911.94 → 918.52] sets in people will really own up to what the responsibilities are you probably wait until that
[918.52 → 923.06] point in time before you decide okay this person's doing way more work than me perhaps this
[923.06 → 930.50] perhaps my ownership percentage should be different from theirs and uh that ownership percentage wasn't
[930.50 → 935.60] necessarily part of the problem there it was more that i never really had expectations upon people
[935.60 → 941.74] beyond just development and I should have set those expectations, so the failing was my failure I think
[941.74 → 948.38] uh most of the firings that we've had at dockyard have been my failure except one or two
[948.38 → 954.88] um and that's me learning how to run a business and I've gotten much better at it, I've gotten much
[954.88 → 962.12] better at uh I guess being very clear with employees like here is your role here's your expectations here's
[962.12 → 966.50] how you get to the next level or maybe I'm not as clear as I think I am perhaps my employees would
[966.50 → 970.90] think differently but I think we're always working on it and trying to get better so a good example of
[970.90 → 978.12] that is uh we actually created a RFP process for dockyard it's an open and public process anyone can
[978.12 → 984.80] view I guess participate but we have one RFP that we've brought in so far we actually have one RFP
[984.80 → 991.02] we've ever opened if you go to dockyard slash RPS I think it's plural on GitHub you can see it
[991.02 → 997.76] and this was around the career life cycle of an employee at dockyard how they can move up what are the
[997.76 → 1003.74] expectations there what incentives they had have tied to bonuses because every year we actually we
[1003.74 → 1008.08] just put this in place so we would always have everyone gets a thousand dollars at the end of
[1008.08 → 1013.02] the year regardless of what they've done uh if you were here for half the year it's prorated to 50
[1013.02 → 1018.58] percent and what we realized is that hey this we might as well just increase everybody's salary by a
[1018.58 → 1026.38] thousand dollars this is not really an incentive and so we uh we determined a bunch of um
[1026.38 → 1031.78] activities or events or things that people can be doing that will benefit dockyard in some way so
[1031.78 → 1036.16] if you go speak at a conference if you speak at a meetup if you're writing blog posts if you're doing
[1036.16 → 1041.38] something that's helping the marketing of the company in some way uh this will be this will be
[1041.38 → 1046.96] calculated as part of a bonus at the end of the year, and it was never clear to people like what are
[1046.96 → 1054.18] those things so we created this RFP uh in order to do that so crazy amount of openness I think is a good
[1054.18 → 1061.04] thing um, and we're always looking for ways to be more open yeah well I mean just as an observer
[1061.04 → 1066.12] and somebody who you know casually observes your openness over the years I appreciate it because
[1066.12 → 1073.64] I draw insights from your trials and tribulations and your successes and um and have kind of been able
[1073.64 → 1079.60] to track you know the struggles of a software company or I guess now you've you guys have kind of
[1080.32 → 1083.60] focused in on you know web and mobile experience company, but you've
[1084.18 → 1089.42] traditionally been an engineering company that's bigger than I am and like thinking should I try
[1089.42 → 1094.34] that should I not you know and so it's fun from that perspective I've also been following along
[1094.34 → 1100.12] uh tech you know technically with a technology bent and just watching because I'm very interested in
[1100.12 → 1106.04] staying relevant and um you know keeping up with open source which is your know changelog's
[1106.04 → 1112.46] mission helping people do that um, and so I've watched you over the years make certain decisions
[1112.46 → 1119.32] uh I think that the ember decision was a while back um but then most recently the one that kind of
[1119.32 → 1126.00] surprised me or maybe even just was impressed upon me that I remembered it was in May of this year 2015
[1126.00 → 1134.10] uh you guys kind of relaunched uh the new dockyard.com website which is very well put together by the way
[1134.10 → 1141.20] but uh you had a kind of intro post and in that post on your guy's blog you wrote this you said this new
[1141.20 → 1148.04] website is also built how we believe modern web applications should be built with ember JS on the
[1148.04 → 1155.78] front end and phoenix on the back end um I want to focus on that decision kind of for the remainder
[1155.78 → 1160.80] of the show we were as I said we were kind of at gopher con last week not kind of we were at gopher
[1160.80 → 1165.74] con last week and there was a halfway there yeah just you know actually we kind of felt halfway there
[1165.74 → 1170.26] because we were in the always more than anything else, but there was a great talk given by Kelsey
[1170.26 → 1176.18] Hightower um who's with core OS where he said the kind of title was how they bet the company on go
[1176.18 → 1181.36] and how that bet paid off for them was kind of the content of the talk and I don't know if you
[1181.36 → 1187.78] necessarily you know betting the company uh on ember and elixir but it kind of feels like that uh to a
[1187.78 → 1192.30] certain degree it's definitely a bold move to come out and say this is how we believe
[1192.30 → 1199.40] um modern web applications should be built I'm going to stop for a sponsor break before you respond
[1199.40 → 1205.08] to all that setup um we'll hear from uh one of our awesome sponsors, and we come back I want to talk
[1205.08 → 1209.60] about that statement and whether it feels like you are betting the company
[1209.60 → 1215.90] all right put them away put them back put the books back on the shelf you don't need them
[1215.90 → 1226.78] and learn to code by doing with code school offers a variety of courses JavaScript HTML CSS ruby
[1226.78 → 1235.12] iOS git and many more to help you expand your skills and learn new technologies code school knows
[1235.12 → 1241.20] that learning to code can be a daunting task, and they've combined experienced instructors with proven
[1241.20 → 1246.20] learning techniques to make coding educational and memorable it gives you the confidence you need
[1246.20 → 1251.64] to continue past those rough tough hurdles that you will definitely face learning the code school
[1251.64 → 1257.00] also knows that languages are a moving target they're always updating their content to give you the latest
[1257.00 → 1263.12] and the greatest learning resources you can even try before you buy roughly one out of every five courses
[1263.12 → 1270.96] on code school is absolutely and totally free this includes instructor classes on git ruby jQuery
[1270.96 → 1277.46] and much more which allow free members to play full courses with coding challenges all included you can
[1277.46 → 1283.70] also pay as you go one monthly fee gives you access to every code school course and if you ever need a
[1283.70 → 1289.54] breather take a break you can suspend your account at any time don't worry your account history your
[1289.54 → 1294.30] points your badges they'll all be there when you're ready to pick things up again get started on
[1294.30 → 1299.50] sharpening your skills today at code school.com once again that is code school.com
[1299.50 → 1306.30] all right we're back Brian does it feel like you're betting the company on ember and does it feel
[1306.30 → 1311.86] like you're betting it on elixir I don't think you can ever do that in software right because it's
[1311.86 → 1316.36] always going to be something new, and you're just one blog post away from changing your mind from a new
[1316.36 → 1324.80] bet yeah, yeah like oh we decided we went with uh framework JavaScript 10.0 whatever right but i so the
[1324.80 → 1332.16] reasons why we started as a rails consultancy and i I've been working with rails since before 1.0
[1332.16 → 1340.36] um my I think my true talent still lies with rails and ruby I'm probably the most experienced
[1340.36 → 1345.54] of all the of all the technologies I have worked with I'm still the most experienced in ruby and rails
[1345.54 → 1352.48] the reason why we as a consultancy decided to move away from that was because rails has become
[1352.48 → 1358.28] a commodity at this point it has accomplished what it set out to do and I think I'm I either touched on
[1358.28 → 1364.60] this on in the blog post you refer to or perhaps in our uh annual blog post at the uh at the end of
[1364.60 → 1375.02] last year um we found that we were not able to get the rates that uh we want to be getting with rails work
[1375.54 → 1382.64] uh the market is becoming uh oversaturated with beginners that and because rails has done so
[1382.64 → 1387.52] well what it set out to do beginners can really get done maybe 80 percent of what a senior developer
[1387.52 → 1394.24] can do um that it's that 20 percent that you know makes it really need somebody yeah it makes all the
[1394.24 → 1400.44] difference but for getting it an application up and running um that's fine scaling the application
[1400.44 → 1410.32] different question right um so i I started and this is where we were poking around with ember out for
[1410.32 → 1416.18] for a period of time and I realized that you know this is perhaps a better business move to move over
[1416.18 → 1421.70] client-side application uh if this is the way that we feel that the technology is going to swing
[1421.70 → 1431.06] then uh if we can establish ourselves as an expert early on then maybe we can uh do something similar
[1431.06 → 1437.96] to what thought bot or hash rocket or pivotal did in the rail space, but we can do it with ember and for
[1437.96 → 1442.32] the to a certain degree I think we've accomplished that in the ember world we have a pretty good
[1442.32 → 1448.74] reputation there our brand is pretty well recognized uh we have a pretty good team um and I think for the
[1448.74 → 1455.56] most part we're pretty well respected in that space uh however I don't think that ember is ever going to
[1455.56 → 1463.08] rise to the yeah to the size that is the world big enough you know to be sustainable for just that kind
[1463.08 → 1467.76] of work I think the JavaScript world is definitely big enough yeah I think that the JavaScript framework
[1467.76 → 1474.28] world though is too fragmented and ember's piece of that pie is always going to be decent and perhaps
[1474.28 → 1480.14] it may sustain a consultancy a little bit larger than ours we're at 19 right now could probably
[1480.14 → 1488.46] sustain a consultancy around 30, but we're interested in really growing getting big uh so I don't think
[1488.46 → 1498.22] that ember alone can do that um we were continuing to build out back ends with rails and because now
[1498.22 → 1506.38] we have this superfast client side application that's running and uh routing between pages felt
[1506.38 → 1512.50] instantaneous the response time of the application especially when we got into production and started
[1512.50 → 1520.68] going a little bit under scale um any um any slowdown in response time any delay was really
[1520.68 → 1527.92] magnified under those conditions uh so uh i I'd always been following elixir i really
[1527.92 → 1533.90] respect José valid and always seemed very interesting because it gave like this ruby like
[1533.90 → 1540.18] syntax on top of a technology that I've always been peripherally very, very interested in which is Erlang
[1540.18 → 1550.72] uh a friend of mine who um worked at Basho uh Chris Mickelson uh he has been talking about Erlang for a
[1550.72 → 1559.80] very long time uh he's like everyone you have to try Erlang so i i I looked into it, I'm like um I'm I guess I'm a bit of a syntax
[1559.80 → 1565.70] snob I think ruby kind of ruined me in that way and I saw the syntax like oh I'm out I can't do this
[1565.70 → 1574.52] I just don't feel like if it's such an I just don't feel like it yeah yeah I just don't feel like it uh it's such a weird thing to say that the syntax
[1574.52 → 1581.38] turned me off and i think some people will point and laugh like ah that's stupid, but it was true i think a lot of ruby people tend to think that way
[1581.38 → 1587.44] or ruby is kind of like ruined our mind like we desire a good syntax and that's the starting of the conversation
[1587.44 → 1592.72] for us when it comes to technology like this is something I'm living in a lot like how is the syntax
[1592.72 → 1597.28] is this going to look ugly is this going to be a pain in the butt am I going to be able to read it am I going to be able to teach it
[1597.28 → 1604.78] um and Erlang syntax was uh i think it's based on prologue maybe it was just i don't know crazy weird
[1604.78 → 1613.80] so uh but when elixir i think was getting close to 1.0 i revisited it and Dave Thomas i think around
[1613.80 → 1621.52] the same time published his programming elixir book through prorogue, and he was one of uh he's one of the
[1621.52 → 1628.64] authors that got me interested in ruby in the first place so i bought the book i don't download books
[1628.64 → 1633.50] I'm not i guess i don't know maybe I'm getting too old but i like holding a book i have a hard time
[1633.50 → 1639.58] reading PDFs and i think that's actually kind of universal like i really yeah there's been recent
[1639.58 → 1645.82] studies even on like millennials or whatnot and teenagers today where you know we thought e-books
[1645.82 → 1650.88] were going to like to take over and just make paper books irrelevant, but it finds they're just kind
[1650.88 → 1656.52] of augmenting they're just another form of transport people actually do like holding things i agree
[1656.52 → 1661.34] with you of course yeah that that could be me also getting ancient but i think there are some studies
[1661.34 → 1667.10] behind the fact that that's actually i think people do have there's a there's something about the physical
[1667.10 → 1672.00] medium and the holding of it that's i don't know it's real but anyway all right I'm not alone
[1672.00 → 1679.32] then you're not alone definitely but i uh i read the book uh it's excellent and in it Dave even spoke
[1679.32 → 1685.98] about how he's excited he's as excited about elixir as he was when he first started doing ruby
[1685.98 → 1694.82] so that got me hooked into it, i respect Dave Thomas a lot uh and the more i read in the book the more I'm
[1694.82 → 1699.86] like wow this really makes a lot of sense to me because i was never i was never a ruby developer who
[1699.86 → 1709.30] really got into the design pattern craziness and i actually found that um design patterns to a
[1709.32 → 1718.62] were being overused over exploited were misused quite a bit and actually tended to do more damage
[1718.62 → 1723.76] in certain projects where you had like a lot of beginners were just taught patterns like do this
[1723.76 → 1728.34] pattern and that's what beginners get right they like to have like here's my rules, but they would
[1728.34 → 1733.00] just the pattern would become the hammer yeah like which pattern am I going to use here instead of like
[1733.00 → 1738.40] how do i solve this problem like which exactly should I use so we as a shop we inherited projects from
[1738.40 → 1743.62] consultancies or from freelancers or from existing teens, and we saw this all the time, and it became
[1743.62 → 1749.94] actually very difficult to follow and build on properly so what was nice that not that to say
[1749.94 → 1756.38] that elixir or line doesn't have patterns but its functional programming feels far more simplistic
[1756.38 → 1761.32] than object-oriented programming does object-oriented programming i think
[1761.32 → 1766.74] obfuscates a lot of what's going on whereas functional programming is like literally here's
[1766.74 → 1772.10] the data flowing through, and you can just follow it and for me that i really kind of clung on to that
[1772.10 → 1777.30] concept and oh by the way it's significantly faster it's orders of magnitude faster than ruby
[1777.30 → 1783.46] it doesn't consume nearly as much memory it's already set up for multicore consumption and
[1783.46 → 1788.42] distributed code so all those things were really nice to have as well I've never really done any
[1788.42 → 1794.68] distributed uh application development before i can't say that i have done real elixir distributed
[1794.68 → 1800.28] application development yet other than some of the examples in the prey prog book but to know that
[1800.28 → 1807.16] i have this tool under my belt that has 30 years of like of experience and building out huge
[1807.16 → 1814.36] distributed systems um is really nice to have and definitely something that i want to explore more
[1814.36 → 1821.48] in the next year let me ask you this i mean I've i had similar interest in elixir, and we've had um
[1821.48 → 1826.36] Chris McCord on uh recently who's the author of the phoenix framework and he kind of did a good job of
[1826.36 → 1833.60] selling uh the idea that it's something worth looking into and um for me, I'm still very interested in it but
[1833.60 → 1839.00] where i kind of like anytime there's something that's just built on top of another language you know
[1839.00 → 1844.26] it just feels like it's always going to be like a hobby, or it's its i don't know there's something like
[1844.36 → 1849.72] it feels like the longevity is not guaranteed whereas like Ealing itself you know was built
[1849.72 → 1853.10] way back in the 80s i think or i don't know when it started but way back in the day, and it's been
[1853.10 → 1860.72] around for years, and it's so you know mature and um you know i respect José valid quite a bit it's
[1860.72 → 1865.98] just like you do um and so this isn't a knock on him or his idea or anything but does it did it feel
[1865.98 → 1872.00] like it's just a bolt-on to a thing that already you know that's established or does it feel like
[1872.00 → 1880.32] it's its own thing it definitely feels like it's its own, and also it's from what I've heard at um
[1880.32 → 1884.22] i think it's called Erlang factory which is like the big Erlang
[1884.22 → 1889.96] a consultancy oh okay uh i think oh i think it's an i think there's actually consultancy but i think
[1889.96 → 1895.62] they have a conference annually i think you're right yeah and i could be wrong someone may say you're
[1895.62 → 1903.24] wrong Brian but i seem to Erlang factory pops up in my head but anyway uh i heard that there's a
[1903.24 → 1908.34] growing number of elixir attendees like a significant number of elixir attendees that are being attracted
[1908.34 → 1916.62] uh to the conference because elixir is like this gateway drug and Erlang has always had kind of a
[1916.62 → 1924.70] not a closed community it's definitely not closed, but it's um it's been more of an academic language
[1924.70 → 1934.10] and used for those purposes than ruby or JavaScript or python have been used for app web application
[1934.10 → 1941.86] development and now uh elixir has kind of thrown open the doors to the masses right it's this very
[1941.86 → 1948.98] approachable language built on great technology and i wouldn't be surprised if more people are doing
[1948.98 → 1954.62] elixir than are going to be doing um Erlang yeah you're going to be doing Erlang because it's not i don't
[1954.62 → 1963.88] think that the analogy of like elixir to Erlang is the same as uh Ruby to java JVM um
[1963.88 → 1971.94] i don't think that i never dreamed that j Ruby would ever overtake java world in any way yeah um
[1971.94 → 1976.54] it always kind of felt like this and i know knock against the Ruby team because those are
[1976.54 → 1981.14] like Charles nutter super smart guy and like the way that they built that out is amazing but
[1981.14 → 1986.60] it always kind of felt like this halfway world between ruby and java whereas elixir definitely
[1986.60 → 1993.86] feels like its own thing onto itself like that you not only get uh this nice uh language
[1993.86 → 2000.02] language and i say language with quotes around it because it's very more of an um it's like a
[2000.02 → 2007.50] parser and then most elixir standard library is written in elixir itself uh even certain things
[2007.50 → 2014.84] like if statements are written in elixir because it will just uh parse it, and then it gets access to
[2014.84 → 2023.28] the uh to the uh to the AST and that gets exported to beam and this is uh so you can augment the
[2023.28 → 2029.18] language any way that you want which you know can be good or bad in fact in Chris's book Chris McCord's
[2029.18 → 2035.78] book uh the meta programming for elixir book he sets out some rules of macro development and like
[2035.78 → 2040.34] i think the first one was not write macros and i the second one may also be don't write macros
[2040.34 → 2045.26] and so it's you know he shows you how to write macros after that yeah the rest of the book is writing
[2045.26 → 2053.88] macro but it's you know if it's one of those things that um it's a very powerful feature that
[2053.88 → 2060.16] is core to elixir, but you really want to go down the road of building out like all these language
[2060.16 → 2064.90] features they'll be non-standard people that are joining the project won't know what it is uh
[2064.90 → 2071.08] versus perhaps working with the language itself but if you need to do something if you need to
[2071.08 → 2076.58] the grasp that power it's there if you need it another aspect of elixir that you know just
[2076.58 → 2082.42] questions i have around it especially from the perspective of what you said with dockyard is you're
[2082.42 → 2090.94] trying to grow a large consultancy um is access to people who are good at it um you know perspective
[2090.94 → 2096.84] hires for you or developers that could you know build your back ends out um has that been an issue
[2096.84 → 2103.52] or do you see that being an issue down the road for hiring uh elixir developers or just ember
[2103.52 → 2113.74] elixir specifically yeah we have had um I wouldn't say that anybody in the shop right now is a dedicated
[2113.74 → 2120.04] elixir developer okay uh the majority of our contracts that over the past year have come our way have
[2120.04 → 2126.82] actually been specifically client-side application development with ember um the uh
[2126.82 → 2132.24] I'd say the most common case would be that it's actually interesting because now that we've we've
[2132.24 → 2136.52] done so well in the ember world I think a lot of clients that come to us actually don't know
[2136.52 → 2141.98] that we can do back-end development yeah, and so they've actually gone out in many cases hired a
[2141.98 → 2149.26] separate team to do the back-end a lot of the time it's rails or something else and I asked them
[2149.26 → 2153.34] why they why they did that one they just come to us like oh we thought you guys are just
[2153.34 → 2160.46] ember, and so we're hoping to establish ourselves in the same way that we did with ember from a
[2160.46 → 2167.10] from a marketing perspective right and that's going to require us to um start releasing open source for
[2167.10 → 2173.76] for phoenix and elixir uh start really blogging about our experience with it uh start getting some
[2173.76 → 2180.04] example client projects case studies on how perhaps we rewrote a particular back-end that was pre-existing
[2180.04 → 2185.22] in phoenix and what type of advantages and disadvantages were there that's going to take
[2185.22 → 2194.42] some time um but I think that anytime a consultancy engages heavily in a new technology
[2194.42 → 2199.84] and gets involved with the growth and community of that technology uh they put themselves in a really
[2199.84 → 2207.92] good position to benefit from it if is that technology ends up doing well right I think ember's done well
[2207.92 → 2213.62] and ember 2.0 especially ember 2.1 because 2.0 is more like the transition we remove all the
[2213.62 → 2221.32] deprecations from 113 2.1 is when we get a lot of nice new stuff um that's gonna I think see a lot
[2221.32 → 2226.48] higher rate of adoption because the barrier of entry to ember is being knocked down all the time
[2226.48 → 2230.76] with every new release they're they're just making it easier and easier to get into ember so now ember
[2230.76 → 2238.82] CLI is actually it's we hit the did lockstep versioning so we're at 113 we went from 0.2 to 113
[2238.82 → 2245.26] overnight um but the barrier of entry for ember is getting smaller, so ember is going to become more
[2245.26 → 2250.48] adoptable and because dockyard is in a good position we'll benefit from that yeah I think that phoenix
[2250.48 → 2257.56] and elixir are perfect technologies and uh as especially the closer phoenix gets to 1.0
[2257.56 → 2264.92] um we'll see an increase in uh in momentum and if we can position ourselves in such a way that oh
[2264.92 → 2270.70] dockyard is a good consultancy for building out phoenix applications then we'll benefit from that
[2270.70 → 2276.42] as well so we kind of have this two-pronged approach we're establishing a service we're I guess like you
[2276.42 → 2282.54] said early on betting on a client-side application uh framework and betting on a backend technology both
[2282.54 → 2288.98] of which are embers not exactly new at this point but um phoenix is definitely new yeah I mean back
[2288.98 → 2293.02] back I can't remember when it was when you decided or when you posted about ember you know your guy's
[2293.02 → 2300.16] new focus on ember I remember reading that post and thinking I had tried ember at the time and um
[2300.16 → 2306.26] I was dabbling with the different you know science at MBC things as well and just trying to see like
[2306.26 → 2312.22] where do I go where do I invest myself as a developer to um you know to produce good
[2312.22 → 2316.02] quality product and to make myself a viable person in the next five years or whatever
[2316.02 → 2322.24] and to me, I mean I was turned on to ember because of the people behind it like i there you know they
[2322.24 → 2326.68] come from the ruby land and uh yeah all that and I respect you, and we've had him on the show multiple
[2326.68 → 2335.02] times um ember data was so immature at the time that it felt like ember was mostly promises back then
[2335.02 → 2339.74] like good promises but like there wasn't much substance behind like I could tell man there's so much
[2339.74 → 2345.84] work to do before this is awesome um and then i kind of looked into angular and angular was more
[2345.84 → 2351.14] productive immediately, and so I had like a six-month love affair with angular yeah and i kind of you know
[2351.14 → 2358.74] kind of faded on that a little bit but um now with ember 2.0, and it seems like ember's finally here
[2358.74 → 2363.74] but is that safe to say like ember's now arrived, and it wasn't really like you guys probably
[2363.74 → 2371.04] had a lot of shoring up to do around it back then that ember's been slowly arriving for a while now
[2371.04 → 2376.84] right it's like this it's like this massive ship that's coming in the harbour yeah being pulled along
[2376.84 → 2383.32] by a tiny tugboat or something I don't know that might be a bad analogy but yeah it do i I've said
[2383.32 → 2388.14] uh several times that I actually think that ember 2.0 is really ember 1.0
[2388.14 → 2395.44] in many ways like 1.0 being like the hey we're you know this is the direction that we want to go in
[2395.44 → 2403.04] ember 1.0 I think that they reached some place of stability, and they wanted to get a 1.0 out
[2403.04 → 2409.42] there to start seeing adoption and use cases come in and so that the use cases have really driven the
[2409.42 → 2414.96] direction of ember I think it will continue to drive the direction of ember but uh it significantly
[2414.96 → 2421.16] drove the direction of ember between 1.0 and 2.0 while they're I'm going to say it was almost
[2421.16 → 2430.04] all like it was mostly semantically versioned uh yeah between 1.0 and 2.0 um I would debate on
[2430.04 → 2434.50] whether it was 100 but i I think for the most part amongst most open source projects it was
[2434.50 → 2441.04] probably the closest to being I guess perfect semantically version as you can get but um the
[2441.04 → 2447.00] direction changed quite a bit or they at least found the right use cases for pushing
[2447.00 → 2455.10] in one direction versus the other um I think that 2.0 is really going to be the version that people
[2455.10 → 2460.02] look at and say okay this is something that we can build something in uh this is something that
[2460.02 → 2466.86] um is competitive with the other frameworks that are out there we have the fast rendering engine
[2466.86 → 2472.76] with glimmer we have the client side application tool with ember CLI uh we're reducing oh I shouldn't
[2472.76 → 2479.44] say if we but uh core team is reducing uh the barrier of entry by just cutting out the fat uh the
[2479.44 → 2486.48] innumerable uh many of the innumerable tools that were in ember were just removed so why have all these
[2486.48 → 2492.98] array prototype stuff right uh if you can just depend upon lodash maybe a better citizen in the
[2492.98 → 2497.46] JavaScript community leverage the tools that are out there rather than rewriting them yeah uh
[2497.46 → 2504.50] controllers are still in 2.0, but they've really been kind of you know mum's the word on controllers
[2504.50 → 2510.46] but object controller array controller have been pulled out um it's just going to really simplify
[2510.46 → 2515.86] the amount of things peoples have to learn yeah within ember what I will say though is that it has
[2515.86 → 2523.28] also increased the barrier of entry from before you ever get to ember, so now people need to be an
[2523.28 → 2528.58] effective ember developer um or the quote-unquote ember way of doing things you're going to have to
[2528.58 → 2537.34] really understand es6 es7 is type stuff right um es6 modules you'll have to uh if you wanted to bug
[2537.34 → 2541.24] certain stuff you're going to have to start understanding how the build process works for ember CLI
[2541.24 → 2547.06] so I think the complexity of knowledge has been shifted off of the framework and more to the
[2547.06 → 2554.40] tooling and hopefully that will start to simplify and normalize especially as browsers begin to
[2554.40 → 2564.32] implement many of these es6 features and um ember CLI itself becomes uh, uh you know built out even more
[2564.32 → 2571.20] yeah, yeah well we're definitely seeing the maturation of ember and I think even uh
[2571.20 → 2577.12] the maturation of client-side MVC you know one thing I want to talk about we are going to take
[2577.12 → 2582.18] our second sponsor break when we come back um I want to talk about you know you guys said this new
[2582.18 → 2587.04] websites built how we believe modern web apps should be built with ember and phoenix I want to
[2587.04 → 2594.24] talk about the technical aspects of dockyard.com because uh traditionally in the last few years uh you
[2594.24 → 2600.20] know single page apps or client-side MVC frameworks where they've really shined is you know dashboards
[2600.20 → 2604.98] um heavily interactive visuals like anywhere where you're chilling on the same page for a long time
[2604.98 → 2610.00] and you're just loading new data in but where they haven't been on content sites it's kind of been
[2610.00 → 2615.34] the web app versus website debate um and the interesting thing about dockyard.com is I mean
[2615.34 → 2622.40] it's effectively a content site, and it's not a dashboard it's not a rich I mean it's a rich UI but
[2622.40 → 2627.38] you know what I'm saying um yeah yeah and so like it's not an application it's not an application it's a
[2627.38 → 2633.22] website right but yet you still think that ember and phoenix and that separation uh is
[2633.22 → 2636.60] the way that these should be made and built so I think there's been some advances you mentioned
[2636.60 → 2640.92] glimmer and some other things I think we'll talk about some of the technical details of the website
[2640.92 → 2649.40] uh when we get back hip chat is a game changer for team communication it helps you and your team get the
[2649.40 → 2655.18] information you need faster than email and reduces meaningless meetings teams that use hip chat
[2655.18 → 2662.30] are able to make faster decisions and get more work done with group chat video chat and file sharing
[2662.30 → 2666.92] hip chat is a great solution for distributed teams by letting you take the office with you
[2666.92 → 2675.06] no matter where you go iPhone android macOS it's all there hip chat is easy to use and gets everyone
[2675.06 → 2682.10] working in real time and right now hip chat is offering listeners of the change log 90 days of hip chat plus
[2682.10 → 2688.66] totally free get premium features like unlimited file storage unlimited message history and guaranteed
[2688.66 → 2697.44] support totally for free for 90 days visit hip chat.com slash change log again that's hip chat.com
[2697.44 → 2702.24] slash change log get your team started using hip chat plus today go and check them out
[2702.24 → 2707.96] all right Brian let's talk about the technical details of dockyard.com how it was built
[2707.96 → 2714.54] uh how ember and phoenix works together, and you know take me through it uh deployment all the goodies
[2714.54 → 2721.10] all the technical so the uh previous I'd say two or three iterations of our website were built in rails
[2721.10 → 2732.04] and we were no longer really doing rails um i I think that if we're in our blog posts in our open source
[2732.04 → 2737.50] in our presentations telling people that you should be using this technology we kind of have to dog food it
[2737.50 → 2742.92] we have to walk that walk we have to say okay we think you should be using this technology because we use it
[2742.92 → 2753.06] rather than just maybe using middleman or some sort of static site generator yep so we set out to rebuild
[2753.06 → 2763.78] and redesign uh docker.com around ember in phoenix it was a little bit of a bumpy road um mostly because we
[2763.78 → 2773.62] we're trying to use some really edge technology uh in the ember world uh specifically uh this new
[2773.62 → 2778.94] thing that was just released uh at the time called fast boot actually I don't even think it was like
[2778.94 → 2786.68] production ready release uh so fast boot was or is ember solution for server-side rendering
[2786.68 → 2794.76] of your ember application for the purposes of uh SEO right it was built by tom and Yehuda
[2794.76 → 2800.94] and they were sponsored by bustle uh which is a company I think in New York I want to say
[2800.94 → 2807.20] maybe wrong but anyway uh, and they've actually leveraged a lot of the work they did on fast boot
[2807.20 → 2814.32] uh to build out the glimmer rendering engine in ember so it had some you know very high impact
[2814.32 → 2823.46] uh benefits uh doing that particular feature so fast boot would actually uh take your
[2823.46 → 2830.10] ember application and boot it up in node and so when you hit it when you hit the request um it will
[2830.10 → 2835.70] render out your ember application server-side serve it up to you as a server-side rendered application
[2835.70 → 2843.02] and then it would be there and then ember would launch in your browser and I think the process they
[2843.02 → 2849.92] called it is hydrate the Dom and so it would just kind of realize that this is already um
[2849.92 → 2854.90] an ember generated application, and we're just going to kind of latch onto it and take over
[2854.90 → 2863.12] so we don't have to re redo everything uh that was a theory in reality what we saw was that but uh fast boot
[2863.12 → 2872.28] at the time had some hideous uh memory leaks in it, and so we like most memory leaks they did not
[2872.28 → 2880.56] come up until after a production right doccare.com uh always benchmark your applications I guess or
[2880.56 → 2885.88] stress test them all right, but we were too we were so excited to get it out um so uh
[2885.88 → 2894.64] we had to pull back and what we actually I think actually dockyard someone may say hey we have
[2894.64 → 2900.54] one up before but i I'm pretty sure that dockyard.com was the first production fast boot application out
[2900.54 → 2907.84] there um it may still only be the one of the few ones out there and what we've done to solve the
[2907.84 → 2916.66] memory leak issues was we're still using fast boot but uh when we deploy a new application it will
[2916.66 → 2925.14] actually send it to our back-end server as well we use our sitemap to walk through and generate all
[2925.14 → 2931.34] static templates uh based with fast boot and then those static templates sit behind nginx and nginx
[2931.34 → 2939.28] serves up you know them up through its cache, and so we get the benefits of the SEO um, but it's not as
[2939.28 → 2946.14] smooth as fast boot would be, but it's still a very fast website like even though we're um still using
[2946.14 → 2951.98] ember and that was a complaint people always had like oh ember's so fat uh ember's slow to load right
[2951.98 → 2958.38] if you go to docker.com I think on average it loads up in like 0.75 uh 0.75 seconds which is
[2958.38 → 2962.84] pretty quick for a client's application we were able to shrink down our asset size I believe in
[2962.84 → 2972.98] close to 200k somewhere around there which is pretty reasonable um, and we like our blog actually sits in
[2972.98 → 2979.26] a database and so when you hit the blog this is being served up by phoenix, and it's I believe
[2979.26 → 2985.76] the whole all the pages the whole page or just the data the whole page all the data so if you were to
[2985.76 → 2990.82] um if you look at your like a network tab you can see the data coming in so right this is all being
[2990.82 → 2995.72] served up by all of our data is being served up by phoenix uh I think most of the content pages
[2995.72 → 3002.60] actually sit in the database like all of our team members sit in the database so we have phoenix
[3002.60 → 3009.38] acting as this like dumb ap dumb API that's just being serving up data and then ember is our
[3009.38 → 3016.68] client side and um we don't we haven't heard any drawbacks from doing it this way we haven't
[3016.68 → 3023.60] heard how many people saying like oh um we get the occasional like oh you should support non-JavaScript
[3023.60 → 3029.84] browser type troll stuff but um we don't really pay attention to that way of thinking any more um
[3029.84 → 3035.98] but it it's its a very fast website like switching between pages is very fast and that that's what i
[3035.98 → 3040.14] want out of an application and so that's what I say that we feel that this is the way to build it
[3040.14 → 3049.46] because speed and response time is an I think becoming a very, very important concern for usability and the
[3049.46 → 3056.16] user experience of any application so we chose a framework and a back-end technology that gave us
[3056.16 → 3064.72] the best speed as well as being I think fits best into our uh our sensibilities as engineers yeah so
[3064.72 → 3070.00] when you navigate pages I mean there's no hash you know hashtag in the URL or anything you got your
[3070.00 → 3077.80] URLs are clean is that still ember is doing all that routing correct so is that uh just in
[3077.80 → 3085.06] feature of newer browsers uh does that work on everything yeah so I think um we might be using
[3085.06 → 3092.54] autolocation actually and in ember autolocation will detect whether you have the uh the
[3092.54 → 3097.88] history API okay in your whether that's available to your browser and if it does, it'll
[3097.88 → 3103.88] give us this nice clean you know URLs if it doesn't it'll fall back to the hashtag okay go to the hash
[3103.88 → 3112.92] hash version right I think like i.e. 10 below uh I think like i.e. 9 i.e. 8 stuff they may fall back
[3112.92 → 3118.52] but most evergreen browsers now I believe are all or all evergreen browsers are actually uh
[3118.52 → 3123.94] uh history API so what is autolocation is that a library is that part of ember proper
[3123.94 → 3129.80] it's part of ember so if you were to go to if you were to generate a new ember application
[3129.80 → 3136.68] the ember CLI I think it's in the uh config environment file there may be something about
[3136.68 → 3142.26] location, and then it's set to auto um I think it's I'm talking off the top of my head I think it may be
[3142.26 → 3149.54] there, but that's where uh ember's router will decide what type of URLs it's going to generate
[3149.54 → 3153.44] through its uh links yeah I just found the page we'll link that up in the show notes it says
[3153.44 → 3157.74] ember autolocation will select the best location option based off browser support with the priority
[3157.74 → 3165.08] order history and then hash and then none yep that's pretty cool um
[3165.08 → 3173.32] awesome so you're kind of using a modified fast boot, or you're using a're using regular fast
[3173.32 → 3181.06] boot, but we're not allowing public access to it got you so nginx is only serving up our cache generated
[3181.06 → 3186.60] templates right now you kind of crawl it yourselves on deploy type of thing correct okay so it's a
[3186.60 → 3190.80] little bit of an engineering you know what we would call maybe a hack to a certain degree until fast
[3190.80 → 3197.80] boot you know can and do it on its own, or it's just in service of even faster boot it was a hack
[3197.80 → 3204.88] to get us around the memory leak issue however as of this past Monday Stefan penned on the core team
[3204.88 → 3211.34] uh believes he may have closed out all the remaining memory leaks on fast food nice we're so he wants us
[3211.34 → 3218.06] to uh move dockyard.com over to regular fast boot I told him we're probably going to do that sometime
[3218.06 → 3226.00] in August yeah see what happens that would be definitely interesting um gosh what else about
[3226.00 → 3232.46] this so just perusing myself it's definitely loads fast I mean initial load is slower and then but
[3232.46 → 3238.06] it's still pretty fast and then obviously your page navigation is superfast um and I know that
[3238.06 → 3241.86] you're using it kind of as like we're we're investing in these technologies we're going to use these
[3241.86 → 3248.04] technologies does it is it possibly over-engineered for what you guys are trying to accomplish
[3248.06 → 3255.70] with your website it's uh over-engineered content site for sure okay i I don't if someone approached
[3255.70 → 3260.44] us and said we want to build a content site you wouldn't build it this way no not unless they had
[3260.44 → 3266.42] a very specific reason for doing so yeah yeah that's kind of like where I've where I've been is you know
[3266.42 → 3270.84] I'm trying to see like when does it become the way to build everything right I still feel like
[3270.84 → 3275.64] there's still use cases and there's still what are you trying to accomplish and let's build the
[3275.64 → 3279.88] website the way that makes the most sense for your goals and I think you guys have done that
[3279.88 → 3285.76] with this because you're you know because you are a company that does this, and you want to help you're
[3285.76 → 3289.08] kind of pushing the bleeding edge to a certain degree with helping out with fast boot helping out
[3289.08 → 3295.74] with these things and showing off what you guys are capable of in a good way um, but probably you know
[3295.74 → 3301.96] as far as about time and money and all that for the goals of a content site still unless it
[3301.96 → 3308.68] has some specific needs you know a static site generator or something simpler is probably still
[3308.68 → 3318.68] the way to go at least you know July 2015 agree with that um I think so for the most part i I do think
[3318.68 → 3327.34] that um there's also something to consider around uh those that don't have as great internet access
[3327.34 → 3332.70] as we do in the United States or if I'm not sure where you are but on the East Coast I think
[3332.70 → 3338.28] we have the best at least the shortest distance to everything and um if you're somewhere in Africa
[3338.28 → 3343.30] and you're reading a very content heavy site do you really want to have to read download the entire page
[3343.30 → 3349.58] on every single click or is it going to be more performant to just download perhaps right uh the data set
[3349.58 → 3357.10] so i think context matters right and uh the concept and architecture of a client's
[3357.10 → 3364.02] application uh really works well for many use cases that could be content driven sites but
[3364.02 → 3369.48] um as far as like a shop site like if we weren't an ember shop then we probably wouldn't have done that
[3369.48 → 3374.42] yeah I feel like we're you know we're breaking down barriers like the SEO barriers broken down and
[3374.42 → 3379.30] you know to a certain degree the URL cleanness barriers started to be broken down
[3379.30 → 3384.70] and yeah context always matters um so I could see where as long as you get I mean sometimes on a
[3384.70 → 3388.36] slow connection you don't get that official you know that initial download never happens and then
[3388.36 → 3398.54] you're like well um so it is it's give or take but uh awesome anything else about ember or elixir or
[3398.54 → 3404.90] yeah I'll say I'll say go ahead say one last thing about ember so um uh another really nice feature
[3404.90 → 3411.56] that's coming soon is that um a developer from LinkedIn is working on this we will have the
[3411.56 → 3418.58] ability to create uh even smaller uh versions of ember pretty soon so right now with es6 modules
[3418.58 → 3424.84] um we're doing like import statements at the top, and we import a specific module what's going to be
[3424.84 → 3432.18] coming pretty soon through ember CLI is the ability to walk that import tree and only uh transpire the
[3432.18 → 3436.44] specific modules that we're using so right now when we import ember we get the entire ember
[3436.44 → 3442.86] thing right and in the future we're going to say like import ember dash get import ember dash component
[3442.86 → 3450.38] if we don't use like the vented uh service for whatever reason then we won't have that in our final
[3450.38 → 3456.38] uh acid output and so our footprints can be significantly smaller so people's people's issue
[3456.38 → 3464.32] with the size of ember yeah uh should pretty much be going away uh soon enough that's great then
[3464.32 → 3468.58] the size of your asset bundle kind of scales up with the size of your application how much of the
[3468.58 → 3472.74] features are you actually using you know you get bigger and bigger but for those people that just
[3472.74 → 3477.64] want to take advantage of the routing and the um the other niceties you have a smaller bundle that'll
[3477.64 → 3484.02] be excellent any idea on timing around that this kind of progress uh I think that's a when it's done
[3484.02 → 3489.56] I'm sure but I know that they're actively working on it because it's a big concern for LinkedIn right
[3489.56 → 3497.18] awesome well lets uh let's take a moment to do our awesome closing questions um got two of them for
[3497.18 → 3502.82] you here and the first one is uh one that we ask quite often is that if you had to pick somebody
[3502.82 → 3507.74] out there you could have more than one if you need to but if you had to pick a programming hero somebody
[3507.74 → 3516.88] look up to uh who would that be and why um I'd probably pick a just left dockyard but uh Robert
[3516.88 → 3524.94] Jackson uh he is a core team member of ember and in the year and a half is time that he was at dockyard
[3524.94 → 3532.86] uh the guy just super impressed me with his ability to not just get things done but also remember things
[3532.86 → 3541.88] like he's got like an um he can recall i I like when I work on code I'm familiar with what I worked
[3541.88 → 3545.82] on and i kind of go if I don't touch it for a month i have to go back and kind of familiarize myself with
[3545.82 → 3550.98] it he just immediately remembers exactly what he was like what it was he can tell you everything and
[3550.98 → 3558.40] like that that level of uh recall just super impressive I think yeah he was uh excellent to work with
[3558.40 → 3566.58] very cool I'm definitely going to link him up in the show notes and uh I had never heard of Robert
[3566.58 → 3571.48] Jackson so I'll be uh checking him out uh I think he's the number one committer on ember right now
[3571.48 → 3575.52] what is so he moved on from dockyard where is he moving on to does he have plans or kind of
[3575.52 → 3583.34] I think the name of the company is actable I think uh they I'm not sure if I'm really I think they're
[3583.34 → 3587.78] I think they've brought their product up they're they're kind of doing ROK for health care
[3587.78 → 3592.72] so like a big problem with health care companies on Heroku is the compliancy yeah and I think that
[3592.72 → 3597.66] they're trying to solve that problem for platform as a service uh health care applications yeah that
[3597.66 → 3604.72] makes sense that's an uh that's a big market if you can get it cool uh next one is what's on your
[3604.72 → 3608.90] open source radar we've obviously talked a lot of different open source projects and feel free to
[3608.90 → 3613.50] you know mention ones that you're up to personally or the dockyard's doing but if you had a free weekend
[3613.50 → 3618.26] and you were going to just play with something new and exciting that has your eye what would it be
[3618.26 → 3629.92] um I actually have to do the opposite I have to stop playing with stuff because i got I get i
[3629.92 → 3635.44] got like developer add and I get onto too much stuff I mean that is probably part of the reason why i
[3635.44 → 3640.12] push my company in the direction I have rather than taking the safe bet and let's keep doing rails okay
[3640.12 → 3644.62] um I mean if there's something I want to do more stuff with distributed code
[3644.62 → 3648.06] yeah elixir cool I don't I don't have a specific library for that though
[3648.06 → 3655.00] cool speaking of uh dockyard and elixir and open source I noticed you guys have a library out
[3655.00 → 3661.48] there for testing phoenix Jason APIs called Voorhees any other cool open source you know GitHub
[3661.48 → 3668.70] projects that you are dockyards up to that you want to uh give a shout-out to I have like a 25 completed
[3668.70 → 3674.02] elixir uh they're called applications and elixir they're not libraries okay so I think that that's
[3674.02 → 3680.62] a that's an uh, uh Erlang term okay um which still feels a little weird to me but I have
[3680.62 → 3688.82] one that um it's kind of like a fixture library for um well for phoenix well phoenix applications
[3688.82 → 3696.60] elixir applications um it's going to have a very simple DSL for declaring fixtures
[3696.60 → 3703.70] hmm got a name for it, I just have it called fixtures right now it's called fixtures yeah it's
[3703.70 → 3712.26] not very creative all right cool well um I'm distracted searching for it on your GitHub is
[3712.26 → 3717.52] it still you're working on it also like 25 percent done you got to get to at least you know 60 percent
[3717.52 → 3722.22] done then you put it online you know yeah and then i I only bring it to about 70 percent of it yeah
[3722.22 → 3727.84] then i I move on to something else yeah then you find a maintainer uh well Brian thanks so much for
[3727.84 → 3732.64] joining us I really enjoyed uh picking your brain on all these things um how can people reach you out
[3732.64 → 3739.44] there on the internet uh probably don't want to follow me on Twitter, but you want to check out
[3739.44 → 3745.12] at dockyard on Twitter okay uh we put all our stuff on there we actually just finished so we host
[3745.12 → 3752.20] uh we hosted a conference wicked good ember comp in June we had uh about 200 people there we're on
[3752.20 → 3758.36] on island so we talk about that experience we've uh mentioned our blog posts through our twitter
[3758.36 → 3764.08] account uh that's probably the easiest way to kind of yes catch up with what put them up to cool
[3764.08 → 3769.46] very cool well as always links are in the show notes uh you can find those at changelog.com
[3769.46 → 3775.60] slash 165 we also want to thank all of our members and our awesome sponsors for making this show
[3775.60 → 3782.74] possible this week's sponsors are code ship code school and hip chat as I said before we have a
[3782.74 → 3789.26] bunch of awesome shows in the works uh some of those are mesosphere Prometheus news cone crystal
[3789.26 → 3794.08] bolt dB editor wars and a lot more so if you haven't hit that subscribe button yet
[3794.08 → 3801.32] why not remember we have an open inbox on GitHub.com slash the changelog slash ping give us a shout
[3801.32 → 3807.20] there with your show ideas entering projects that you have or that you've created or just say hi we
[3807.20 → 3811.84] love hearing from you, I want to announce that we're we're going to become a crystal uh development shop
[3811.84 → 3819.44] oh breaking news yes breaking news crystal is the new hotness very cool it does look it does look
[3819.44 → 3824.44] like a cool technology I'm excited about that show we're very interested in it that should be a good
[3824.44 → 3830.08] one but until next time let's go ahead and say goodbye see ya oh goodbye
[3849.44 → 3849.94] you
