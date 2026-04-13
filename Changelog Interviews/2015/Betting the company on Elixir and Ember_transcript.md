[0.00 --> 15.52]  welcome back everyone this is the change log and i'm your host adam stikowiak this is episode 165
[15.52 --> 22.60]  and on today's show jared is going solo all by himself talking to brian cartarello from
[22.60 --> 31.12]  dockyard about betting the company on elixir and ember good show we have three awesome sponsors
[31.12 --> 38.94]  code ship code school and hip chat our first sponsor is code ship they launched a brand new
[38.94 --> 44.64]  feature called organizations now you can create teams that permissions for specific team members
[44.64 --> 50.50]  and improve collaboration in your continuous delivery workflow maintain centralized control
[50.50 --> 56.60]  over your organization's projects and teams with code ship's new organization plan you can save 20
[56.60 --> 61.66]  off any premium plan you choose for the next three months by using the code the changelog podcast
[61.66 --> 68.42]  again that code is the changelog podcast 20 off any premium plan you choose for three months
[68.42 --> 73.32]  head to code ship.com slash the changelog to get started and now on to the show
[73.32 --> 85.52]  welcome back everybody jared here i am fresh off of our trip to denver for gopher con 2015
[85.52 --> 91.44]  i just want to give a quick shout out to all of our new gopher friends and listeners and trust me
[91.44 --> 98.12]  we lined up a ton of go related shows in our pipeline more on that later but we had tons of
[98.12 --> 102.20]  fun hanging out t-shirts and shooting video interviews with everybody in fact if you're
[102.20 --> 108.30]  wondering where is the mellifluous voice of adam stack he's actually heads down in the editing room
[108.30 --> 113.80]  this week turning all of our raw footage from the conference into something awesome but don't worry
[113.80 --> 118.92]  adam will be back next week and we will welcome toby knopp who is a cto of mesosphere to the show
[118.92 --> 125.34]  stay tuned for that but today i'm joined by brian cartarella who is the ceo of dockyard
[125.34 --> 132.34]  dockyard is a web and mobile user experience consultancy in boston massachusetts brian thanks
[132.34 --> 137.26]  so much for joining me thanks for having me so did i do you justice in the intro anything else you
[137.26 --> 144.00]  want to say about yourself um as a way of introduction uh no that's it i'm sure we'll touch on a bunch of
[144.00 --> 150.36]  stuff yeah yeah absolutely brian i think i was thinking back of when you first came across my radar
[150.36 --> 157.90]  and in the open source world and i think it was with your client side validations gem yeah which
[157.90 --> 163.96]  for those who don't know was a ruby gem and i think it was probably only in the context of rails
[163.96 --> 172.64]  um which purpose was to give us the ultimate kind of dry uh validations where you define them once in
[172.64 --> 179.08]  your models and then we can actually like traverse them down into uh i think probably jquery back then
[179.08 --> 186.48]  into validations in the client side right so it will allow you to write them once they'd export
[186.48 --> 193.74]  actually there was some before i even knew uh what transpilation was yeah it kind of did some ruby to
[193.74 --> 199.38]  javascript transpilation really really bad right um but it's interesting because client side of
[199.38 --> 208.40]  validations has kind of was my first like use case for how i've been writing code over the next few years
[208.40 --> 214.74]  so like client side validations was uh what motivated me to want to get more heavily interested in
[214.74 --> 222.12]  client side application development and specifically um something as uh complex as ember yeah i mean i
[222.12 --> 227.90]  remember with the gem because because that gem came out and and it spoke to me very uh very tight
[227.90 --> 233.22]  like inherently i was like yes this is something that we need something that i know i needed um and so i
[233.22 --> 237.84]  started using it and i think i can't remember if i contributed back i definitely did some bug reports for
[237.84 --> 245.54]  for you back in the day yeah and it seemed like uh a great goal but it just was a difficult thing for
[245.54 --> 250.92]  you to achieve i think it i think it was working well but there were a lot of issues um did you
[250.92 --> 257.68]  struggle to actually like execute on that idea uh well the way that i that i wrote it originally yes so
[257.68 --> 265.38]  what client side validations was doing under the hood was that it was trying to uh attach all these
[265.38 --> 273.72]  validation rules to input elements and it was basing it off of string values and then there was all this
[273.72 --> 279.14]  you know crazy rules in the back end uh i'm sorry i mean within the library not on the back end right
[279.14 --> 283.60]  um and that's not even taking account of like remote client side validations the the uniqueness
[283.60 --> 290.70]  validator was a whole mess yep but what i came to realize pretty early on and this is what i mentioned
[290.70 --> 296.24]  now i got became interested in ember was that uh client side validations really needed a model to
[296.24 --> 301.50]  work against needed like a like a like a user model or something where you're actually going against
[301.50 --> 309.20]  specific values rather than just trying to piecemeal all these values off of input elements and so when i
[309.20 --> 315.02]  was uh building on client side validations i actually went down the path i don't know if the if the branch
[315.02 --> 320.72]  still exists on the repo um but i still went down the path of building out a very very small and
[320.72 --> 326.08]  probably very poorly thought out like client side framework just for re-implementing clients that
[326.08 --> 332.48]  validations and i got to the point like this is crazy i'll start looking the backbone um backbone
[332.48 --> 338.40]  didn't really interest me and that's where ember was starting to get on my radar and i i went off in
[338.40 --> 346.76]  that direction and then i realized that um this whole at least for me the nature of server side
[346.76 --> 353.72]  application development um was really i think going to fall by the wayside and client side application
[353.72 --> 359.46]  development was going to be the next big thing and so for someone that's running a business i really
[359.46 --> 365.54]  wanted to get ahead of that curve and start establishing expertise there so i kind of dropped
[365.54 --> 371.94]  client side validations off of my plate sorry for those that were using it um i i did do do i did
[371.94 --> 378.20]  due diligence to try to find a replacement uh author um i put the radar i i i maintained it for
[378.20 --> 383.60]  like six months i asked people if they wanted to take it over didn't get any takers and so i finally
[383.60 --> 388.48]  sunset it however i think someone has taken it over now i gave somebody i don't know if they're still
[388.48 --> 395.04]  working on it but i uh i gave them somebody uh the ruby gems access and they own the repo now
[395.04 --> 401.24]  so um hopefully it's found a good home but uh yeah that that was always an interesting project
[401.24 --> 408.48]  from a um a technical point of view of trying to get ruby over to javascript but also from a uh
[408.48 --> 414.30]  point of view of okay i realized that this is the completely wrong direction for implementing this
[414.30 --> 421.90]  and it's kind of taken me on this crazy journey to to really becoming very well versed in clients
[421.90 --> 426.76]  application development yeah and i think as we you know as this conversation progresses we'll
[426.76 --> 431.52]  probably take that journey a little bit i want to also mention something that you do annually which
[431.52 --> 437.32]  i've been a fan of over the years um you know we just met but i've been kind of following dockyard
[437.32 --> 443.74]  to a degree because i'm also a a consultant uh you know i have a software company you know employee
[443.74 --> 449.52]  number one uh and i've always flirted with growing and not growing and the ideas behind it
[449.52 --> 454.08]  um so i follow other people that are doing that i follow thoughtbot to a degree and dockyard
[454.08 --> 460.46]  and just kind of watch you know like to watch what you're doing and you make that really easy because
[460.46 --> 467.46]  you publish this lessons learned post annually um which is kind of a year in review it's kind of
[467.46 --> 474.16]  the entire life of your your consultancy um and man you're like crazy transparent in that post
[474.16 --> 480.14]  like i feel like you just kind of bear it all there and i'm curious uh why you do that and
[480.14 --> 487.38]  and just have you talk about that so several reasons um first i think it's just in my nature
[487.38 --> 494.92]  i tend to i guess wear my emotions and myself on my sleeve to a certain degree i think anyone that
[494.92 --> 500.30]  follows me on twitter kind of gets too much of that from time to time i do a lot of twitter
[500.30 --> 504.04]  complaining because i think that's the the primary purpose of twitter is just like
[504.04 --> 511.64]  complain about things yeah yeah um and uh but the other reason which is probably a more
[511.64 --> 521.46]  um like politically correct thing to to say rather is that um when i was getting going with dockyard when
[521.46 --> 529.18]  i when i was because i was a freelancer i i worked in enterprise i worked in startups and i i finally had it
[529.18 --> 534.52]  with that world and i said i'm gonna work myself and i i went and started freelancing i very quickly
[534.52 --> 539.48]  realized that i've really traded one boss for like you know 10 or 20 bosses exactly yeah whoever
[539.48 --> 545.26]  however many you happen to have during a given year um that's not really any more freeing uh but
[545.26 --> 553.86]  i started getting um more and more complex projects pushed my way stuff that required more than just me
[553.86 --> 560.54]  so i reached out to a few people and uh we just said we were working on a project we worked well
[560.54 --> 567.22]  together we decided okay let's give this a shot and start a company at the time my llc was uh
[567.22 --> 573.60]  horribly named it was dirty water development uh for those that are from boston yeah yeah so for
[573.60 --> 578.26]  those that are from boston and that are red sox fans that's the song that the red sox play the
[578.26 --> 585.26]  standells love that dirty water uh yeah it's a it's a um reference that went over everybody's head
[585.26 --> 593.42]  nobody got it especially in in light of when i when i was doing business under that llc was when the gulf
[593.42 --> 600.56]  oil spill happened oh no everybody thought that this was somehow a tongue-in-cheek reference the gulf oil
[600.56 --> 607.10]  spill which was not the case so i uh i think i realized very quickly that this was a bad name um
[607.10 --> 614.46]  and i'm a i i race sailboats i want to do something nautical so i i really do want shipyard
[614.46 --> 619.10]  because i'm like oh shipyard shipping shipping software that makes sense right however there
[619.10 --> 626.60]  is a shipyard bear uh beer in maine and they own that domain name i uh and so dockyard was the uh the
[626.60 --> 634.02]  next next obvious choice for me and to go back to your original question i i started when i was starting
[634.02 --> 640.32]  the company i was starting from zero right i never run a company before um i grew up in a family like
[640.32 --> 646.04]  my father ran his own company my grandfather ran his own company but uh very different businesses uh
[646.04 --> 651.62]  so i kind of got a sense of what it takes to um like the effort that goes into running company but
[651.62 --> 657.04]  as far as the specifics around running a software consultancy i really had no one to ask i emailed a
[657.04 --> 663.14]  few people that were doing it and what i realized very fast is that a lot of these shops are
[663.14 --> 669.16]  they're just dsing people they're lying they're they're saying everything's great everything's
[669.16 --> 674.84]  awesome because they feel that they have to put forth this image of excellence and anytime that
[674.84 --> 679.62]  there is anything that's negative about them out there they fear that they're gonna lose out on a
[679.62 --> 683.98]  contract they're gonna lose out an employee they're gonna lose out on anything and so they they just
[683.98 --> 688.88]  say everything's great everything's awesome all the time and i don't think that people learn
[688.88 --> 695.62]  from people's successes because i think success is fleeting success is very difficult to duplicate
[695.62 --> 703.32]  uh it's usually time-based it's luck-based you happen to be fortunate enough that you were in the
[703.32 --> 709.02]  right place at the right time and things worked out for you that's i think the significant key to
[709.02 --> 714.24]  success sometimes effort and persistence is definitely part of that but persistence actually just means that
[714.24 --> 720.72]  you're able to stick it out long enough so that you get lucky uh failures are super easy to duplicate
[720.72 --> 726.42]  failures happen all the time and the way that you fail is probably very similar to the way that i fail
[726.42 --> 733.20]  and telling me how you failed will allow me to help cope with and avoid that particular failure or at least
[733.20 --> 740.08]  minimize the damage and nobody wanted to talk about their failures so i i decided early on that
[740.08 --> 745.28]  um if we can make it to one year i'd actually i think i did the first one after six months
[745.28 --> 750.26]  and i wanted to share those lessons with people because i didn't see those lessons anywhere else
[750.26 --> 760.10]  uh they were more of a cathartic thing for me and uh i i wasn't sure if anybody would like them
[760.10 --> 766.74]  but they tend they tend to uh get a lot of attention um i think that annually they're definitely the most
[766.74 --> 772.54]  red blog posts at least at the time when i published them uh we have some uh ember posts that
[772.54 --> 780.08]  i think overall have gotten more more traffic but um yeah i kind of i i talk about what went well
[780.08 --> 784.88]  what didn't go well what changes we can make in the upcoming year i talk about how much money we've made
[784.88 --> 790.78]  it's stupid not to talk about money right people don't like to share like the revenue they don't like
[790.78 --> 796.92]  the share their their rates i don't know why maybe maybe there's a like a really good business
[796.92 --> 801.46]  school reason not to do it but i didn't go to business school it's never hurt us in any way
[801.46 --> 807.06]  um and i really wouldn't want to run a company that we wouldn't be able to talk about these type of
[807.06 --> 813.06]  things i if we end up losing if we end up doing worse one year yeah it will be embarrassing to say
[813.06 --> 818.48]  that we didn't make as much money this year as we did last year but that's you know ultimately
[818.48 --> 825.78]  that lies upon me and i need to own that so do you where do you draw the line do you have a line
[825.78 --> 830.98]  do you have you thought about that or do you just uh bear it all whatever whatever you feel like
[830.98 --> 836.38]  saying in those kind of posts or are they if it if it impacts one of my employees directly or a former
[836.38 --> 841.96]  employee it won't be brought up unless i've discussed it with them already gotcha so a good
[841.96 --> 849.52]  example of that um i've discussed firing people and um one of the employees specifically was actually
[849.52 --> 855.10]  one of the co-founders of the company and everyone hears this word firing and they think oh that's
[855.10 --> 860.68]  that's bad but it's what it is like we didn't lay them off we didn't dismiss them they were fired and
[860.68 --> 868.50]  there's no two ways around it um and i discussed it with him i said i want to discuss this within this
[868.50 --> 876.24]  context in that you know perhaps in this case i was wrong uh i i did not you know adequately set
[876.24 --> 882.82]  so so within that for that specific person i i spoke about how uh what ended up happening was when
[882.82 --> 889.00]  we co-founded the company we never set expectations upon people's roles and everything kind of fell upon
[889.00 --> 895.36]  me and i was getting frustrated and i think the lesson learned there was that when you're starting a
[895.36 --> 901.24]  company you should probably not even uh amongst your co-founders not even split up uh ownership
[901.24 --> 905.24]  percentage until maybe six months in when you get a sense on like okay here's what people are really
[905.24 --> 911.94]  doing because beforehand you can dream up like oh you're gonna do this i'll do that and then reality
[911.94 --> 918.52]  sets in people will really own up to what the responsibilities are you probably wait until that
[918.52 --> 923.06]  point in time before you decide okay this person's doing way more work than me perhaps this
[923.06 --> 930.50]  perhaps my ownership percentage should be different than theirs and uh that ownership percentage wasn't
[930.50 --> 935.60]  necessarily part of the problem there it was more that i never really had expectations upon people
[935.60 --> 941.74]  beyond just development and i should have set those expectations so the failing was my my failure i think
[941.74 --> 948.38]  uh most of the firings that we've had at dockyard have been my failure with the exception of one or two
[948.38 --> 954.88]  um and that's me learning how to run a business and i've gotten much better at it i've gotten much
[954.88 --> 962.12]  better at uh i guess being very clear with employees like here is your role here's your expectations here's
[962.12 --> 966.50]  how you get to the next level or maybe i'm not as clear as i think i am perhaps my employees would
[966.50 --> 970.90]  think differently but i think we're always working on it and trying to get better so a good example of
[970.90 --> 978.12]  that is uh we actually created an rfp process for dockyard it's an open and public process anyone can
[978.12 --> 984.80]  view i guess participate but we we have one rfp that we've brought in so far we actually have one rfp
[984.80 --> 991.02]  we've ever opened if you go to dockyard slash rps i think it's plural on github you can see it
[991.02 --> 997.76]  and this was around the career life cycle of an employee at dockyard how they can move up what are the
[997.76 --> 1003.74]  expectations there what incentives they had have tied to bonuses because every year we actually we
[1003.74 --> 1008.08]  just put this in place so we would always have everyone gets a thousand dollars at the end of
[1008.08 --> 1013.02]  the year regardless of what they've done uh if you were here for half the year it's prorated to 50
[1013.02 --> 1018.58]  percent and what we realized is that hey this we might as well just increase everybody's salary by a
[1018.58 --> 1026.38]  thousand dollars this is not really an incentive and so we we uh we determined a bunch of um
[1026.38 --> 1031.78]  activities or events or things that people can be doing that will benefit dockyard in some way so
[1031.78 --> 1036.16]  if you go speak at a conference if you speak at a meetup if you're writing blog posts if you're doing
[1036.16 --> 1041.38]  something that's helping the marketing of the company in some way uh this will be this will be
[1041.38 --> 1046.96]  calculated as part of a bonus at the end of the year and it was never clear to people like what are
[1046.96 --> 1054.18]  those things so we created this rfp uh in order to do that so crazy amount of openness i think is a good
[1054.18 --> 1061.04]  thing um and we're always looking for ways to be more open yeah well i mean just as an observer
[1061.04 --> 1066.12]  and somebody who you know casually observes your openness over the years i appreciate it because
[1066.12 --> 1073.64]  i draw insights from your trials and tribulations and your successes and um and have kind of been able
[1073.64 --> 1079.60]  to track you know the struggles of of a software company or i guess now you've you guys have kind of
[1080.32 --> 1083.60]  focused in on you know web and mobile experience company but you've
[1084.18 --> 1089.42]  traditionally been an engineering company that's bigger than i am and like thinking should i try
[1089.42 --> 1094.34]  that should i not you know and so it's fun from that perspective i've also been following along
[1094.34 --> 1100.12]  uh tech you know technically with a technology bent and just watching because i'm very interested in
[1100.12 --> 1106.04]  staying relevant and um you know keeping up with open source which is you know changelog's
[1106.04 --> 1112.46]  mission helping people do that um and so i've watched you over the years make certain decisions
[1112.46 --> 1119.32]  uh i think that the ember decision was a while back um but then most recently the one that kind of
[1119.32 --> 1126.00]  surprised me or maybe even just was impressed upon me that i remembered it was in may of this year 2015
[1126.00 --> 1134.10]  uh you guys kind of relaunched uh the new dockyard.com website which is very well put together by the way
[1134.10 --> 1141.20]  but uh you had a kind of intro post and in that post on your guys's blog you wrote this you said this new
[1141.20 --> 1148.04]  website is also built how we believe modern web applications should be built with ember js on the
[1148.04 --> 1155.78]  front end and phoenix on the back end um i want to focus on that decision kind of for the remainder
[1155.78 --> 1160.80]  of the show we were as i said we were kind of at gopher con last week not kind of we were at gopher
[1160.80 --> 1165.74]  con last week and there was a halfway there yeah just you know actually we kind of felt halfway there
[1165.74 --> 1170.26]  because we were in the always more than anything else but there was a great talk given by kelsey
[1170.26 --> 1176.18]  hightower um who's with core os where he said the kind of title was how they bet the company on go
[1176.18 --> 1181.36]  and how that bet paid off for them was kind of the content of the talk and i don't know if you
[1181.36 --> 1187.78]  necessarily you know betting the company uh on ember and elixir but it kind of feels like that uh to a
[1187.78 --> 1192.30]  certain degree it's definitely a bold move to come out and say this is how we believe
[1192.30 --> 1199.40]  um modern web applications should be built i'm gonna stop for a sponsor break before you respond
[1199.40 --> 1205.08]  to all that setup um we'll hear from uh one of our awesome sponsors and we come back i want to talk
[1205.08 --> 1209.60]  about that statement and whether or not it feels like you are betting the company
[1209.60 --> 1215.90]  all right put them away put them back put the books back on the shelf you don't need them
[1215.90 --> 1226.78]  and learn to code by doing with code school code school offers a variety of courses javascript html css ruby
[1226.78 --> 1235.12]  ios git and many many more to help you expand your skills and learn new technologies code school knows
[1235.12 --> 1241.20]  that learning to code can be a daunting task and they've combined experienced instructors with proven
[1241.20 --> 1246.20]  learning techniques to make coding educational and memorable it gives you the confidence you need
[1246.20 --> 1251.64]  to continue past those rough tough hurdles that you will definitely face learning the code code school
[1251.64 --> 1257.00]  also knows that languages are a moving target they're always updating their content to give you the latest
[1257.00 --> 1263.12]  and the greatest learning resources you can even try before you buy roughly one out of every five courses
[1263.12 --> 1270.96]  on code school is absolutely and totally free this includes instructor classes on git ruby jquery
[1270.96 --> 1277.46]  and much more which allow free members to play full courses with coding challenges all included you can
[1277.46 --> 1283.70]  also pay as you go one monthly fee gives you access to every code school course and if you ever need a
[1283.70 --> 1289.54]  breather take a break you can suspend your account at any time don't worry your account history your
[1289.54 --> 1294.30]  points your badges they'll all be there when you're ready to pick things up again get started on
[1294.30 --> 1299.50]  sharpening your skills today at code school.com once again that is code school.com
[1299.50 --> 1306.30]  all right we're back brian does it feel like you're betting the company on ember and does it feel
[1306.30 --> 1311.86]  like you're betting it on elixir i don't think you can ever do that in software right because it's
[1311.86 --> 1316.36]  always going to be something new and you're just one blog post away from changing your mind from a new
[1316.36 --> 1324.80]  bet yeah yeah like oh we decided we went with uh framework javascript 10.0 whatever right but i i so the
[1324.80 --> 1332.16]  reasons why we started as a rails consultancy and i i've been working with rails since before 1.0
[1332.16 --> 1340.36]  um my my i think my true talent still lies with rails and ruby i'm probably the most experienced
[1340.36 --> 1345.54]  of all the of all the technologies i have worked with i'm still the most experienced in ruby and rails
[1345.54 --> 1352.48]  the reason why we as a consultancy decided to move away from that was because rails has become
[1352.48 --> 1358.28]  a commodity at this point it has accomplished what it set out to do and i think i'm i either touched on
[1358.28 --> 1364.60]  this on in the blog post you refer to or perhaps in our uh annual blog post at the uh at the end of
[1364.60 --> 1375.02]  last year um we found that we were not able to get the rates that uh we want to be getting with rails work
[1375.54 --> 1382.64]  uh the market is becoming uh oversaturated with beginners that and because rails has done so
[1382.64 --> 1387.52]  well what it set out to do beginners can really get done maybe 80 percent of what a senior developer
[1387.52 --> 1394.24]  can do um that it's that 20 percent that you know makes it really need somebody yeah it makes all the
[1394.24 --> 1400.44]  difference but for getting it an application up and running um that's fine scaling the application
[1400.44 --> 1410.32]  different question right um so i i started and this is where we were poking around with ember out for
[1410.32 --> 1416.18]  for a period of time and i realized that you know this is perhaps a better business move to move over
[1416.18 --> 1421.70]  client-side application uh if this is the way that we feel that the technology is going to swing
[1421.70 --> 1431.06]  then uh if we can establish ourselves as an expert early on then maybe we can uh do something similar
[1431.06 --> 1437.96]  to what thoughtbot or hashrocket or pivotal did in the rail space but we can do it with ember and for
[1437.96 --> 1442.32]  the to a certain degree i think we've accomplished that in the ember world we have a pretty good
[1442.32 --> 1448.74]  reputation there our brand is pretty well recognized uh we have a pretty good team um and i think for the
[1448.74 --> 1455.56]  most part we're pretty well respected in that space uh however i don't think that ember is ever going to
[1455.56 --> 1463.08]  rise to the yeah to the size that is the world big enough you know to be sustainable for just that kind
[1463.08 --> 1467.76]  of work i think the javascript world is definitely big enough yeah i think that the javascript framework
[1467.76 --> 1474.28]  world though is too fragmented and ember's piece of that pie is always going to be decent and perhaps
[1474.28 --> 1480.14]  it may sustain a consultancy a little bit larger than ours we're at 19 right now could probably
[1480.14 --> 1488.46]  sustain a consultancy around 30 but we're interested in really growing getting big uh so i don't think
[1488.46 --> 1498.22]  that ember alone can do that um we were continuing to build out back ends with rails and because now
[1498.22 --> 1506.38]  we have this super fast client side application that's running and uh routing between pages felt
[1506.38 --> 1512.50]  instantaneous the response time of the application especially when we got into production and started
[1512.50 --> 1520.68]  going a little bit under scale um any any um any slowdown in response time any delay was really
[1520.68 --> 1527.92]  magnified under those conditions uh so uh i i'd always been following elixir i really
[1527.92 --> 1533.90]  respect jose valim and always seemed very interesting because it gave like this ruby like
[1533.90 --> 1540.18]  syntax on top of a technology that i've always been peripherally very very interested in which is erlang
[1540.18 --> 1550.72]  uh a friend of mine who um worked at basho uh chris micklejohn uh he has been talking about erlang for a
[1550.72 --> 1559.80]  very long time uh he's like everyone you gotta try erlang so i i i looked into it i'm like um i'm i guess i'm a bit of a syntax
[1559.80 --> 1565.70]  snob i think ruby kind of ruined me in that way and i saw the syntax like oh i'm out i can't do this
[1565.70 --> 1574.52]  i just don't feel like it it's such a i just don't feel like it yeah yeah i just don't feel like it uh it's such a weird thing to say that the syntax
[1574.52 --> 1581.38]  turned me off and i think some people will point and laugh like ah that's stupid but it was true i i think a lot of ruby people tend to think that way
[1581.38 --> 1587.44]  or ruby is kind of like ruined our mind like we we desire a good syntax and that's the starting of the conversation
[1587.44 --> 1592.72]  for us when it comes to technology like this is something i'm living in a lot like how is the syntax
[1592.72 --> 1597.28]  is this going to look ugly is this going to be a pain in the butt am i going to be able to read it am i going to be able to teach it
[1597.28 --> 1604.78]  um and erlang syntax was uh i think it's based on prologue maybe it was just i don't know crazy weird
[1604.78 --> 1613.80]  so uh but when elixir i think was getting close to 1.0 i revisited it and dave thomas i think around
[1613.80 --> 1621.52]  the same time published his programming elixir book through pragprog and he was one of uh he's one of the
[1621.52 --> 1628.64]  authors that got me interested in ruby in the first place so i i bought the book i don't download books
[1628.64 --> 1633.50]  i'm not i guess i don't know maybe i'm getting too old but i like holding a book i have a hard time
[1633.50 --> 1639.58]  reading pdfs and i think that's actually kind of universal like i really yeah there's been recent
[1639.58 --> 1645.82]  studies even on like millennials or whatnot and teenagers today where you know we thought ebooks
[1645.82 --> 1650.88]  were going to like take over and just make make paper books irrelevant but it finds they're just kind
[1650.88 --> 1656.52]  of augmenting they're just another form of transport people actually do like holding things i i agree
[1656.52 --> 1661.34]  with you of course yeah that that could be me also getting ancient but i think there's some studies
[1661.34 --> 1667.10]  behind the fact that that's actually i think people do have there's a there's something about the physical
[1667.10 --> 1672.00]  medium and and the holding of it that's i don't know it's real but anyways all right i'm not alone
[1672.00 --> 1679.32]  then you're not alone definitely but i uh i read the book uh it's excellent and in it dave even spoke
[1679.32 --> 1685.98]  about how he's excited he's as excited about elixir as he was when he first started doing ruby
[1685.98 --> 1694.82]  so that got me hooked into it i respect dave thomas a lot uh and the more i read in the book the more i'm
[1694.82 --> 1699.86]  like wow this really makes a lot of sense to me because i was never i was never a ruby developer who
[1699.86 --> 1709.30]  really got into the design pattern craziness and i actually found that um design patterns to a
[1709.32 --> 1718.62]  were being overused over exploited were misused quite a bit and actually tended to do more damage
[1718.62 --> 1723.76]  in certain projects where you had like a lot of beginners were just taught patterns like do this
[1723.76 --> 1728.34]  pattern and that's what beginners get right they like to have like here's my rules but they would
[1728.34 --> 1733.00]  just the pattern would become the hammer yeah like which pattern am i going to use here instead of like
[1733.00 --> 1738.40]  how do i solve this problem like which exactly should i use so we as a shop we inherited projects from
[1738.40 --> 1743.62]  consultancies or from freelancers or from existing teens and we saw this all the time and it became
[1743.62 --> 1749.94]  actually very difficult to follow and and build off of properly so what was nice that not that to say
[1749.94 --> 1756.38]  that elixir or line doesn't have patterns but it functional programming feels far more simplistic
[1756.38 --> 1761.32]  than object-oriented programming does object-oriented programming i think
[1761.32 --> 1766.74]  obfuscates a lot of what's going on whereas functional programming is like literally here's
[1766.74 --> 1772.10]  the data flowing through and you can just follow it and for me that i really kind of clung on to that
[1772.10 --> 1777.30]  concept and oh by the way it's significantly faster it's orders of magnitude faster than ruby
[1777.30 --> 1783.46]  it doesn't consume nearly as much memory it's already set up for multi-core consumption and
[1783.46 --> 1788.42]  distributed code so all those things were really nice to have as well i've never really done any
[1788.42 --> 1794.68]  distributed uh application development before i can't say that i have done real elixir distributed
[1794.68 --> 1800.28]  application development yet other than some of the examples in the preg prog book but to know that
[1800.28 --> 1807.16]  i have this tool under my belt that has 30 years of of like of experience and building out huge
[1807.16 --> 1814.36]  distributed systems um is really nice to have and definitely something that i want to explore more
[1814.36 --> 1821.48]  in the next year let me ask you this i mean i've i had similar interest in elixir and we've had um
[1821.48 --> 1826.36]  chris mccord on uh recently who's the author of the phoenix framework and he kind of did a good job of
[1826.36 --> 1833.60]  selling uh the idea that it's something worth looking into and um for me i'm still very interested in it but
[1833.60 --> 1839.00]  where i kind of like anytime there's something that's just built on top of another language you know
[1839.00 --> 1844.26]  it just feels like it's always going to be like a hobby or it's it's i don't know there's something like
[1844.36 --> 1849.72]  it feels like the longevity is not guaranteed whereas like erling itself you know was built
[1849.72 --> 1853.10]  way back in the 80s i think or i don't know when it started but way back in the day and it's been
[1853.10 --> 1860.72]  around for years and it's so you know mature and um you know i i respect jose avalim quite a bit it's
[1860.72 --> 1865.98]  just like you do um and so this isn't a knock on him or his idea or anything but does it did it feel
[1865.98 --> 1872.00]  like it's just a bolt-on to a thing that already you know that's established or does it feel like
[1872.00 --> 1880.32]  it's its own thing it definitely feels like it's its own and also it's from what i've heard at um
[1880.32 --> 1884.22]  i think it's called erlang factory which is like the big erlang
[1884.22 --> 1889.96]  a consultancy oh okay uh i think oh i i think it's a i think there's actually consultancy but i think
[1889.96 --> 1895.62]  they have a conference annually i think you're right yeah and i could be wrong someone may say you're
[1895.62 --> 1903.24]  wrong brian but i i seem to erlang factory pops up in my head but anyway uh i heard that there's a
[1903.24 --> 1908.34]  growing number of elixir attendees like a significant number of elixir attendees that are being attracted
[1908.34 --> 1916.62]  uh to the conference because elixir is like this gateway drug and erlang has always had kind of a
[1916.62 --> 1924.70]  not a closed community it's definitely not closed but it's um it's been more of an academic language
[1924.70 --> 1934.10]  and used for those purposes than ruby or javascript or python have been used for app web application
[1934.10 --> 1941.86]  development and now uh elixir has kind of thrown open the doors to the masses right it's this very
[1941.86 --> 1948.98]  approachable language built on great technology and i wouldn't be surprised if more people are doing
[1948.98 --> 1954.62]  elixir than are going to be doing um erlang yeah you're gonna be doing erlang because it's not i don't
[1954.62 --> 1963.88]  think that the analogy of like elixir to erlang is the same as uh jruby to java jvm um
[1963.88 --> 1971.94]  i don't think that i never dreamed that j jruby would ever overtake java world in any way yeah um
[1971.94 --> 1976.54]  it always kind of felt like this and i know knock against the jruby team because those are
[1976.54 --> 1981.14]  like charles nutter super smart guy and like the way that they built that out is amazing but
[1981.14 --> 1986.60]  it always kind of felt like this halfway world between ruby and java whereas elixir definitely
[1986.60 --> 1993.86]  feels like its own thing onto itself like that you not only get uh this nice uh language
[1993.86 --> 2000.02]  language and i say language with quotes around it because it's very more of a um it's like a
[2000.02 --> 2007.50]  parser and then most of elixir standard library is written in elixir itself uh even certain things
[2007.50 --> 2014.84]  like if statements are written in elixir because it will just uh parse it and then it gets access to
[2014.84 --> 2023.28]  the uh to the uh to the ast and that gets exported to beam and this is uh so you can augment the
[2023.28 --> 2029.18]  language any way that you want which you know can be good or bad in fact in chris's book chris mccord's
[2029.18 --> 2035.78]  book uh the meta programming for for elixir book he sets out some rules of macro development and like
[2035.78 --> 2040.34]  i think the first one was don't write macros and i the second one may also be don't write macros
[2040.34 --> 2045.26]  and so it's you know he shows you how to write macros after that yeah the rest of the book is writing
[2045.26 --> 2053.88]  macro but but it's you know it it's one of those things that um it's a very powerful feature that
[2053.88 --> 2060.16]  is core to elixir but you really want to go down the road of building out like all these language
[2060.16 --> 2064.90]  features they'll be non-standard people that are joining the project won't know what it is uh
[2064.90 --> 2071.08]  versus perhaps working with the language itself but if you need to do something if you need to
[2071.08 --> 2076.58]  the grasp that power it's there if you need it another aspect of elixir that you know just
[2076.58 --> 2082.42]  questions i have around it especially from the perspective of what you said with dockyard is you're
[2082.42 --> 2090.94]  trying to grow a large consultancy um is access to people who are good at it um you know perspective
[2090.94 --> 2096.84]  hires for you or developers that could you know build your back ends out um has that been an issue
[2096.84 --> 2103.52]  or do you see that being an issue down the road for hiring uh elixir developers or just ember
[2103.52 --> 2113.74]  elixir specifically yeah we have had um i wouldn't say that anybody in the shop right now is a dedicated
[2113.74 --> 2120.04]  elixir developer okay uh majority of our contracts that over the past year have come our way have
[2120.04 --> 2126.82]  actually been specifically client-side application development with ember um the uh
[2126.82 --> 2132.24]  i'd say the most common case would be that it's actually interesting because now that we've we've
[2132.24 --> 2136.52]  done so well in the ember world i think a lot of clients that come to us actually don't know
[2136.52 --> 2141.98]  that we can do back-end development yeah and so they've actually gone out in many cases hired a
[2141.98 --> 2149.26]  separate team to do the back-end a lot of the time it's rails or something else and i asked them
[2149.26 --> 2153.34]  why they why they why they did that one they just come to us like oh we thought you guys are just
[2153.34 --> 2160.46]  ember and so we're hoping to establish ourselves in the same way that we did with ember from a
[2160.46 --> 2167.10]  from a marketing perspective right and that's going to require us to um start releasing open source for
[2167.10 --> 2173.76]  for phoenix and elixir uh start really blogging about our experience with it uh start getting some
[2173.76 --> 2180.04]  example client projects case studies on how perhaps we rewrote a particular back-end that was pre-existing
[2180.04 --> 2185.22]  in phoenix and what type of advantages and disadvantages were there that's going to take
[2185.22 --> 2194.42]  some time um but i think that anytime a a consultancy engages heavily in a new technology
[2194.42 --> 2199.84]  and gets involved with the growth and community of that technology uh they put themselves in a really
[2199.84 --> 2207.92]  good position to benefit from it if if that technology ends up doing well right i think ember's done well
[2207.92 --> 2213.62]  and ember 2.0 especially ember 2.1 because 2.0 is more like the transition we remove all the
[2213.62 --> 2221.32]  deprecations from 113 2.1 is when we get a lot of nice new stuff um that's gonna i think see a lot
[2221.32 --> 2226.48]  higher rate of adoption because the the barrier of entry to ember is being knocked down all the time
[2226.48 --> 2230.76]  with every new release they're they're just making it easier and easier to get into ember so now ember
[2230.76 --> 2238.82]  cli is actually it's we hit the they did lockstep versioning so we're at 113 we went from 0.2 to 113
[2238.82 --> 2245.26]  overnight um but the barrier of entry for ember is getting smaller so ember is going to become more
[2245.26 --> 2250.48]  adoptable and because dockyard is in a good position we'll benefit from that yeah i think that phoenix
[2250.48 --> 2257.56]  and elixir are really good technologies and uh as especially the closer phoenix gets to 1.0
[2257.56 --> 2264.92]  um we'll see an increase in uh in momentum and if we can position ourselves in such a way that oh
[2264.92 --> 2270.70]  dockyard is a good consultancy for building out phoenix applications then we'll benefit from that
[2270.70 --> 2276.42]  as well so we kind of have this two-pronged approach we're establishing a service we're i guess like you
[2276.42 --> 2282.54]  said early on betting on a client-side application uh framework and betting on a backend technology both
[2282.54 --> 2288.98]  of which are embers not exactly new at this point but um phoenix is definitely new yeah i mean back
[2288.98 --> 2293.02]  back i can't remember when it was when you decided or when you posted about ember you know your guys's
[2293.02 --> 2300.16]  new focus on ember i remember reading that post and thinking i had tried ember at the time and um
[2300.16 --> 2306.26]  i was dabbling with the different you know science at mbc things as well and just trying to see like
[2306.26 --> 2312.22]  where do i go where do i invest myself as a as a developer to um you know to produce good
[2312.22 --> 2316.02]  quality product and to make myself a viable person in the next five years or whatever
[2316.02 --> 2322.24]  and to me i mean i was turned on to ember because of the people behind it like i there you know they
[2322.24 --> 2326.68]  come from the ruby land and uh yeah all that and i respect you and we've had him on the show multiple
[2326.68 --> 2335.02]  times um ember data was so immature at the time that it felt like ember was mostly promises back then
[2335.02 --> 2339.74]  like good promises but like there wasn't much substance behind like i could tell man there's so much
[2339.74 --> 2345.84]  work to do before this is awesome um and then i kind of looked into angular and angular was more
[2345.84 --> 2351.14]  productive immediately and so i had like a six month love affair with angular yeah and i kind of you know
[2351.14 --> 2358.74]  kind of faded on that a little bit but um now with ember 2.0 and it seems like ember's finally here
[2358.74 --> 2363.74]  but is that is that safe to say like ember's now arrived and it wasn't really like you guys probably
[2363.74 --> 2371.04]  had a lot of shoring up to do around it back then that ember's been slowly arriving for a while now
[2371.04 --> 2376.84]  right it's like this it's like this massive ship that's coming in the harbor yeah being pulled along
[2376.84 --> 2383.32]  by a tiny tugboat or something i don't know that might be a bad analogy but yeah it does i i've said
[2383.32 --> 2388.14]  uh several times that i actually think that ember 2.0 is really ember 1.0
[2388.14 --> 2395.44]  in many ways like 1.0 being like the hey we're you know this is the direction that we want to go in
[2395.44 --> 2403.04]  ember 1.0 i think that they they reached some place of stability and they wanted to get a 1.0 out
[2403.04 --> 2409.42]  there to start seeing adoption and use cases come in and so that the use cases have really driven the
[2409.42 --> 2414.96]  direction of ember i think it will continue to drive the direction of ember but uh it significantly
[2414.96 --> 2421.16]  drove the direction of ember between 1.0 and 2.0 while they're i'm going to say it was almost
[2421.16 --> 2430.04]  all like it was mostly semantically versioned uh yeah between 1.0 and 2.0 um i would debate on
[2430.04 --> 2434.50]  whether or not it was 100 but i i think for the most part amongst most open source projects it was
[2434.50 --> 2441.04]  probably the closest to being i guess perfect semantically version as you can get but um the
[2441.04 --> 2447.00]  direction changed quite a bit or they they at least found the right use cases for pushing
[2447.00 --> 2455.10]  in one direction versus the other um i think that 2.0 is really going to be the version that people
[2455.10 --> 2460.02]  look at and say okay this is something that we can build something in uh this is something that
[2460.02 --> 2466.86]  um is competitive with the other frameworks that are out there we we have the fast rendering engine
[2466.86 --> 2472.76]  with glimmer we have the client side application tool with ember cli uh we're reducing oh i shouldn't
[2472.76 --> 2479.44]  say if we but uh core team is reducing uh the barrier of entry by just cutting out the fat uh the
[2479.44 --> 2486.48]  innumerable uh many of the innumerable tools that were in ember were just removed so why have all these
[2486.48 --> 2492.98]  array prototype stuff right uh if you can just depend upon lodash maybe a better citizen in the
[2492.98 --> 2497.46]  javascript community leverage the tools that are out there rather than rewriting them yeah uh
[2497.46 --> 2504.50]  controllers are still in 2.0 but they've really been kind of you know mum's the word on controllers
[2504.50 --> 2510.46]  but object controller array controller have been pulled out um it's just going to really simplify
[2510.46 --> 2515.86]  the amount of things people have to learn yeah within ember what i will say though is that it has
[2515.86 --> 2523.28]  also increased the barrier of entry from before you ever get to ember so now people need to be an
[2523.28 --> 2528.58]  effective ember developer um or the quote-unquote ember way of doing things you're going to have to
[2528.58 --> 2537.34]  really understand es6 es7 ish type stuff right um es6 modules you'll have to uh if you wanted to bug
[2537.34 --> 2541.24]  certain stuff you're going to have to start understanding how the build process works for ember cli
[2541.24 --> 2547.06]  so i think the complexity of knowledge has been shifted off of the framework and more to the
[2547.06 --> 2554.40]  tooling and hopefully that will start to simplify and normalize especially as browsers begin to
[2554.40 --> 2564.32]  implement many of these es6 features and um ember cli itself becomes uh uh you know built out even more
[2564.32 --> 2571.20]  yeah yeah well we're definitely seeing the maturation of of ember and i think even uh
[2571.20 --> 2577.12]  the maturation of client-side mvc you know one thing i want to talk about we are going to take
[2577.12 --> 2582.18]  our second sponsor break when we come back um i want to talk about you know you guys said this new
[2582.18 --> 2587.04]  website's built how we believe modern web apps should be built with ember and phoenix i want to
[2587.04 --> 2594.24]  talk about the technical aspects of dockyard.com because uh traditionally in the last few years uh you
[2594.24 --> 2600.20]  know single page apps or client-side mvc frameworks where they've really shined is you know dashboards
[2600.20 --> 2604.98]  um heavily interactive visuals like anywhere where you're chilling on the same page for a long time
[2604.98 --> 2610.00]  and you're just loading new data in but where they haven't is on content sites it's kind of been
[2610.00 --> 2615.34]  the web app versus website debate um and the interesting thing about dockyard.com is i mean
[2615.34 --> 2622.40]  it's effectively a content site and it's not a dashboard it's not a rich i mean it's a rich ui but
[2622.40 --> 2627.38]  you know what i'm saying um yeah yeah and so like it's not an application it's not an application it's a
[2627.38 --> 2633.22]  website right but and yet you still think that ember and and phoenix and that separation uh is
[2633.22 --> 2636.60]  the way that these should be made and built so i think there's been some advances you mentioned
[2636.60 --> 2640.92]  glimmer and some other things i think we'll talk about some of the technical details of the website
[2640.92 --> 2649.40]  uh when we get back hip chat is a game changer for team communication it helps you and your team get the
[2649.40 --> 2655.18]  information you need faster than email and reduces meaningless meetings teams that use hip chat
[2655.18 --> 2662.30]  are able to make faster decisions and get more work done with group chat video chat and file sharing
[2662.30 --> 2666.92]  hip chat is a great solution for distributed teams by letting you take the office with you
[2666.92 --> 2675.06]  no matter where you go iphone android mac os it's all there hip chat is easy to use and gets everyone
[2675.06 --> 2682.10]  working in real time and right now hip chat is offering listeners of the change log 90 days of hip chat plus
[2682.10 --> 2688.66]  totally free get premium features like unlimited file storage unlimited message history and guaranteed
[2688.66 --> 2697.44]  support totally for free for 90 days visit hip chat.com slash change log again that's hip chat.com
[2697.44 --> 2702.24]  slash change log get your team started using hip chat plus today go and check them out
[2702.24 --> 2707.96]  all right brian let's talk about the technical details of dockyard.com how it was built
[2707.96 --> 2714.54]  uh how ember and phoenix works together and you know take me through it uh deployment all the goodies
[2714.54 --> 2721.10]  all the technical so the uh previous i'd say two or three iterations of our website were built in rails
[2721.10 --> 2732.04]  and we were no longer really doing rails um i i think that if we're in our blog posts in our open source
[2732.04 --> 2737.50]  in our presentations telling people that you should be using this technology we kind of have to dog food it
[2737.50 --> 2742.92]  we have to walk that walk we have to say okay we think you should be using this technology because we use it
[2742.92 --> 2753.06]  rather than just maybe using middleman or some sort of static site generator yep so we set out to rebuild
[2753.06 --> 2763.78]  and redesign uh docker.com around ember in phoenix it was a little bit of a bumpy road um mostly because we
[2763.78 --> 2773.62]  we're trying to use some really edge technology uh in the ember world uh specifically uh this new
[2773.62 --> 2778.94]  thing that was just released uh at the time called fastboot actually i don't even think it was like
[2778.94 --> 2786.68]  production ready release uh so fastboot was or is ember solution for server-side rendering
[2786.68 --> 2794.76]  of your ember application for the purposes of uh seo right it was built by tom and yehuda
[2794.76 --> 2800.94]  and they were sponsored by bustle uh which is a company i think in new york i want to say
[2800.94 --> 2807.20]  maybe wrong but anyway uh and they've actually leveraged a lot of the work they did on fastboot
[2807.20 --> 2814.32]  uh to build out the glimmer rendering engine in ember so it had some you know very high impact
[2814.32 --> 2823.46]  uh benefits uh doing that doing that particular feature so so fastboot would actually uh take your
[2823.46 --> 2830.10]  ember application and boot it up in node and so when you hit it when you hit the request um it will
[2830.10 --> 2835.70]  render out your ember application server-side serve it up to you as a server-side rendered application
[2835.70 --> 2843.02]  and then it would be there and then ember would launch in your browser and i think the process they
[2843.02 --> 2849.92]  called it is hydrate the dom and so it would just kind of realize that this is already um
[2849.92 --> 2854.90]  a ember generated application and we're just going to kind of latch onto it and take over
[2854.90 --> 2863.12]  so we don't have to re redo everything uh that was a theory in reality what we saw was that but uh fastboot
[2863.12 --> 2872.28]  at the time had some really ugly uh memory leaks in it and so we like most memory leaks they did not
[2872.28 --> 2880.56]  come up until after a production right doccare.com uh always benchmark your applications i guess or
[2880.56 --> 2885.88]  stress test them all right but we were too we were so excited to get it out um so uh
[2885.88 --> 2894.64]  we we had to pull back and what we actually i think actually dockyard someone may say hey we have
[2894.64 --> 2900.54]  one up before but i i'm pretty sure that dockyard.com was the first production fastboot application out
[2900.54 --> 2907.84]  there um it may still only be the one of the only ones out there and what we've done to solve the
[2907.84 --> 2916.66]  memory leak issues was we're still using fastboot but uh when we deploy a new application it will
[2916.66 --> 2925.14]  actually send it to our back-end server as well we use our sitemap to walk through and generate all
[2925.14 --> 2931.34]  static templates uh based with fastboot and then those static templates sit behind nginx and nginx
[2931.34 --> 2939.28]  serves up you know them up through its cache and so we get the benefits of the seo um but it's not as
[2939.28 --> 2946.14]  smooth as fastboot would be but it's still a very fast website like even though we're um still using
[2946.14 --> 2951.98]  ember and that was a complaint people always had like oh ember's so fat uh ember's slow to load right
[2951.98 --> 2958.38]  if you go to docker.com i think on average it loads up in like 0.75 uh 0.75 seconds which is
[2958.38 --> 2962.84]  pretty quick for a client's application we were able to shrink down our asset size i believe to
[2962.84 --> 2972.98]  close to 200k somewhere around there which is pretty reasonable um and we like our blog actually sits in
[2972.98 --> 2979.26]  a database and so when you hit the blog this is being served up by phoenix and it's i believe
[2979.26 --> 2985.76]  the whole all the pages the whole page or just the data the whole page all the data so if you were to
[2985.76 --> 2990.82]  um if you look at your like a network tab you can see the data coming in so right this is all being
[2990.82 --> 2995.72]  served up by all of our data is being served up by phoenix uh i think most of the content pages
[2995.72 --> 3002.60]  actually sit in the database like all of our team members sit in the database so so we have phoenix
[3002.60 --> 3009.38]  acting as this like dumb ap dumb api that's just being serving up data and then ember is our is our
[3009.38 --> 3016.68]  client side and um we don't we haven't heard any drawbacks from from doing it this way we haven't
[3016.68 --> 3023.60]  heard how many people saying like oh um we get the occasional like oh you should support non-javascript
[3023.60 --> 3029.84]  browser type troll stuff but um we don't really pay attention to that way of thinking anymore um
[3029.84 --> 3035.98]  but it it's it's a very fast website like switching between pages is very fast and that that's what i
[3035.98 --> 3040.14]  want out of an application and so that's what i say that we feel that this is the way to build it
[3040.14 --> 3049.46]  because speed and response time is a i think becoming a very very important concern for usability and the
[3049.46 --> 3056.16]  user experience of any application so we chose a framework and a back-end technology that gave us
[3056.16 --> 3064.72]  the best speed as well as being i think fits best into our uh our sensibilities as engineers yeah so
[3064.72 --> 3070.00]  when you navigate pages i mean there's no hash you know hashtag in the url or anything you got your
[3070.00 --> 3077.80]  urls are clean is that still ember is doing all that routing correct correct so is that uh just in
[3077.80 --> 3085.06]  feature of newer browsers uh does that work on everything yeah so i think um we might be using
[3085.06 --> 3092.54]  autolocation actually and in ember autolocation will detect whether or not you have the uh the
[3092.54 --> 3097.88]  history api okay in your whether or not that's available to your browser and if it does it'll
[3097.88 --> 3103.88]  give us this nice clean you know urls if it doesn't it'll fall back to the hashtag okay go to the hash
[3103.88 --> 3112.92]  hash version right i think like ie 10 below uh i think like ie 9 ie 8 stuff they may fall back
[3112.92 --> 3118.52]  but most evergreen browsers now i believe are all or all evergreen browsers are actually uh
[3118.52 --> 3123.94]  uh history api so what is autolocation is that a library is that part of ember proper
[3123.94 --> 3129.80]  it's part of ember so if you were to go to if you were to generate a new ember application
[3129.80 --> 3136.68]  the ember cli i think it's in the uh config environment file there may be something about
[3136.68 --> 3142.26]  location and then it's set to auto um i think it's i'm talking off the top of my head i think it may be
[3142.26 --> 3149.54]  there but that's where uh ember's router will decide what type of urls it's going to generate
[3149.54 --> 3153.44]  through its uh links yeah i just found the the page we'll link that up in the show notes it says
[3153.44 --> 3157.74]  ember autolocation will select the best location option based off browser support with the priority
[3157.74 --> 3165.08]  order history and then hash and then none yep that's pretty cool um
[3165.08 --> 3173.32]  awesome so you're kind of using a modified fast boot or you're using a we're using regular fast
[3173.32 --> 3181.06]  boot but we're not allowing public access to it gotcha so nginx is only serving up our cache generated
[3181.06 --> 3186.60]  templates right now you kind of crawl it yourselves on deploy type of a thing correct okay so it's a
[3186.60 --> 3190.80]  little bit of an engineering you know what we would call maybe a hack to a certain degree until fast
[3190.80 --> 3197.80]  boot you know can and do it on its own or it's just in service of even faster boot it was a hack
[3197.80 --> 3204.88]  to get us around the memory leak issue however as of this past monday stefan penner on the core team
[3204.88 --> 3211.34]  uh believes he may have closed out all the remaining memory leaks on fast food nice we're so he wants us
[3211.34 --> 3218.06]  to uh move dockyard.com over to regular fast boot i told him we're probably going to do that sometime
[3218.06 --> 3226.00]  in august yeah see what happens that would be definitely interesting um gosh what else about
[3226.00 --> 3232.46]  this so just perusing myself it's definitely loads fast i mean initial load is slower and then but
[3232.46 --> 3238.06]  it's still pretty fast and then obviously your your page navigation is super fast um and i know that
[3238.06 --> 3241.86]  you're using it kind of as like we're we're investing in these technologies we're going to use these
[3241.86 --> 3248.04]  technologies does it is it possibly over-engineered for what you guys are trying to accomplish
[3248.06 --> 3255.70]  with your website it's uh over-engineered content site for sure okay i i don't if someone approached
[3255.70 --> 3260.44]  us and said we want to build a content site you wouldn't build it this way no not unless they had
[3260.44 --> 3266.42]  a very specific reason for doing so yeah yeah that's kind of like where i've where i've been is you know
[3266.42 --> 3270.84]  i'm trying to see like when does it become the way to build everything right i still feel like
[3270.84 --> 3275.64]  there's still use cases and there's still what are you trying to accomplish and let's build the
[3275.64 --> 3279.88]  website the way that makes the most sense for your for your goals and i think you guys have done that
[3279.88 --> 3285.76]  with this because you're you know because you are a company that does this and you want to help you're
[3285.76 --> 3289.08]  kind of pushing the bleeding edge to a certain degree with helping out with fastboot helping out
[3289.08 --> 3295.74]  with these things and showing off what you guys are capable of in a good way um but probably you know
[3295.74 --> 3301.96]  as far as about time and money and all that for the for the goals of a content site still unless it
[3301.96 --> 3308.68]  has some specific needs you know a static site generator or something simpler is probably still
[3308.68 --> 3318.68]  the way to go at least you know july 2015 agree with that um i think so for the most part i i do think
[3318.68 --> 3327.34]  that um there's also something to consider around uh those that don't have as great internet access
[3327.34 --> 3332.70]  as as we do in the united states or if i'm not sure where you are but on the east coast i think
[3332.70 --> 3338.28]  we have the best at least the shortest distance to everything and um if you're somewhere in africa
[3338.28 --> 3343.30]  and you're reading a very content heavy site do you really want to have to read download the entire page
[3343.30 --> 3349.58]  on every single click or is it going to be more performant to just download perhaps right uh the data set
[3349.58 --> 3357.10]  so i think i think context matters right and uh the the concept and architecture of a client's
[3357.10 --> 3364.02]  application uh really works well for many use cases that could be content driven sites but
[3364.02 --> 3369.48]  um as far as like a shop site like if we weren't an ember shop then we probably wouldn't have done that
[3369.48 --> 3374.42]  yeah i feel like we're you know we're breaking down barriers like the seo barriers broken down and
[3374.42 --> 3379.30]  you know to a certain degree the url cleanness barriers started to be broken down
[3379.30 --> 3384.70]  and yeah context always matters um so i could see where as long as you get i mean sometimes on a
[3384.70 --> 3388.36]  slow connection you don't get that official you know that initial download never happens and then
[3388.36 --> 3398.54]  you're like well um so it it it's give or take but uh awesome anything else about ember or elixir or
[3398.54 --> 3404.90]  yeah i'll say i'll say go ahead say one last thing about ember so um uh another really nice feature
[3404.90 --> 3411.56]  that's coming soon is that um a developer from linkedin is working on this we will have the
[3411.56 --> 3418.58]  ability to create uh even smaller uh versions of ember pretty soon so right now with es6 modules
[3418.58 --> 3424.84]  um we're doing like import statements at the top and we import a specific module what's going to be
[3424.84 --> 3432.18]  coming pretty soon through ember cli is the ability to walk that import tree and only uh transpile the
[3432.18 --> 3436.44]  specific modules that we're using so right now when we when we import ember we get the entire ember
[3436.44 --> 3442.86]  thing right and in the future we're going to say like import ember dash get import ember dash component
[3442.86 --> 3450.38]  if we don't use like the evented uh service for whatever reason then we won't have that in our final
[3450.38 --> 3456.38]  uh acid output and so our our footprints can be significantly smaller so people's people's issue
[3456.38 --> 3464.32]  with the size of ember yeah uh should pretty much be going away uh soon enough that's great then then
[3464.32 --> 3468.58]  the size of your asset bundle kind of scales up with the size of your application how much of the
[3468.58 --> 3472.74]  features are you actually using you know you get bigger and bigger but for those people that just
[3472.74 --> 3477.64]  want to take advantage of the routing and the um the other niceties you have a smaller bundles that'll
[3477.64 --> 3484.02]  be excellent any idea on timing around that those kind of progress uh i think that's a when it's done
[3484.02 --> 3489.56]  i'm sure but i know that they're actively working on it because it's a big concern for linkedin right
[3489.56 --> 3497.18]  awesome well let's uh let's take a moment to do our awesome closing questions um got two of them for
[3497.18 --> 3502.82]  you here and the first one is uh one that we ask quite often is that if you had to pick somebody
[3502.82 --> 3507.74]  out there you could have more than one if you need to but if you had to pick a programming hero somebody
[3507.74 --> 3516.88]  look up to uh who would that be and why um i'd probably pick a he just left dockyard but uh robert
[3516.88 --> 3524.94]  jackson uh he is a core team member of ember and in the year and a half ish time that he was at dockyard
[3524.94 --> 3532.86]  uh the guy just super impressed me with his ability to not just get things done but also remember things
[3532.86 --> 3541.88]  like he's got like a um he can recall i i like when i work on code i'm familiar with what i worked
[3541.88 --> 3545.82]  on and i kind of go if i don't touch it for a month i gotta go back and kind of familiarize myself with
[3545.82 --> 3550.98]  it he just immediately remembers exactly what he was like what it was he can tell you everything and
[3550.98 --> 3558.40]  like that that level of uh recall just super impressive i think yeah he he was uh excellent to work with
[3558.40 --> 3566.58]  very cool i'm definitely gonna link him up in the show notes and uh i had never heard of robert
[3566.58 --> 3571.48]  jackson so i'll be uh checking him out uh i think he's the number one committer on ember right now
[3571.48 --> 3575.52]  what is so he moved on from dockyard where is he moving on to does he have plans or kind of
[3575.52 --> 3583.34]  i think the name of the company is aptable i think uh they i'm not sure if i'm really i think they're
[3583.34 --> 3587.78]  i think they've brought their product up they're they're kind of doing roku for health care
[3587.78 --> 3592.72]  so like a big problem with health care companies on heroku is the compliancy yeah and i think that
[3592.72 --> 3597.66]  they're trying to solve that problem for platform as a service uh health care applications yeah that
[3597.66 --> 3604.72]  makes sense that's a uh that's a big market if you can get it cool uh next one is what's on your
[3604.72 --> 3608.90]  open source radar we've obviously talked a lot of different open source projects and feel free to
[3608.90 --> 3613.50]  you know mention ones that you're up to personally or the dockyard's doing but if you had a free weekend
[3613.50 --> 3618.26]  and you were going to just play with something new and exciting that has your eye what would it be
[3618.26 --> 3629.92]  um i actually have to do the opposite i have to stop playing with stuff because i got i got i get i
[3629.92 --> 3635.44]  got like developer add and i get onto too much stuff i mean that is probably part of the reason why i
[3635.44 --> 3640.12]  push my company in the direction i have rather than taking the safe bet and let's keep doing rails okay
[3640.12 --> 3644.62]  um i mean if there's something i want to do more more stuff with distributed code
[3644.62 --> 3648.06]  yeah elixir cool i don't i don't have a specific library for that though
[3648.06 --> 3655.00]  cool cool speaking of uh dockyard and elixir and open source i noticed you guys have a library out
[3655.00 --> 3661.48]  there for testing phoenix json apis called vorhees any other cool open source you know github
[3661.48 --> 3668.70]  projects that you are dockyards up to that you want to uh give a shout out to i have like a 25 completed
[3668.70 --> 3674.02]  elixir uh they're called applications and elixir they're not libraries okay so i think that that's
[3674.02 --> 3680.62]  a that's a uh uh erlang term okay um which still feels a little weird to me but i have
[3680.62 --> 3688.82]  one that um it's kind of like a fixture library for um well for for phoenix well phoenix applications
[3688.82 --> 3696.60]  elixir applications um it's going to have a very simple dsl for declaring fixtures
[3696.60 --> 3703.70]  hmm got a name for it i just have it called fixtures right now it's called fixtures yeah it's
[3703.70 --> 3712.26]  not very creative all right cool well um i'm distracted searching for it on your github is
[3712.26 --> 3717.52]  it still you're working on it also like 25 percent done you got to get to at least you know 60 percent
[3717.52 --> 3722.22]  done then you put it online you know yeah and then i i only bring it to about 70 percent of it yeah
[3722.22 --> 3727.84]  then i i move on to something else yeah then you find a maintainer uh well brian thanks so much for
[3727.84 --> 3732.64]  joining us i really enjoyed uh picking your brain on all these things um how can people reach you out
[3732.64 --> 3739.44]  there on the internet uh probably don't want to follow me on twitter but you want to check out
[3739.44 --> 3745.12]  at dockyard on twitter okay uh we put all our stuff on there we actually just finished so we host
[3745.12 --> 3752.20]  uh we hosted a conference wicked good ember comp in june we had uh about 200 people there we're on
[3752.20 --> 3758.36]  on island so we we talk about that experience we've uh mentioned our blog posts through our twitter
[3758.36 --> 3764.08]  account uh that's probably the easiest way to kind of yes catch up with what put them up to cool
[3764.08 --> 3769.46]  very cool well as always links are in the show notes uh you can find those at changelog.com
[3769.46 --> 3775.60]  slash 165 we also want to thank all of our members and our awesome sponsors for making this show
[3775.60 --> 3782.74]  possible this week's sponsors are code ship code school and hip chat as i said before we have a
[3782.74 --> 3789.26]  bunch of awesome shows in the works uh some of those are mesosphere prometheus nejs conf crystal
[3789.26 --> 3794.08]  bolt db editor wars and a whole lot more so if you haven't hit that subscribe button yet
[3794.08 --> 3801.32]  why not remember we have an open inbox on github.com slash the changelog slash ping give us a shout
[3801.32 --> 3807.20]  there with your show ideas entering projects that you have or that you've created or just say hi we
[3807.20 --> 3811.84]  love hearing from you i want to announce that we're we're going to become a crystal uh development shop
[3811.84 --> 3819.44]  oh breaking news yes breaking news crystal is the new hotness very cool it does look it does look
[3819.44 --> 3824.44]  like a cool technology i'm excited for that show we're very interested in it that should be a good
[3824.44 --> 3830.08]  one but until next time let's go ahead and say goodbye see ya oh goodbye
[3849.44 --> 3849.94]  you
