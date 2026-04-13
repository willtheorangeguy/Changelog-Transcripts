[0.00 → 14.78] welcome back everyone this is the changelog where a member supported blog podcast and weekly email
[14.78 → 21.48] comes fresh and what's new in open source check out the blog at the changelog.com our past shows
[21.48 → 28.24] at five by five dot TV slash changelog, and you're listening to episode 125 I talk with parker more
[28.24 → 34.18] about all things Jekyll and how he got started in open source today's show is sponsored by Rackspace
[34.18 → 39.72] snap CI and top towel we'll tell you a bit more about top towel and snap CI later in the show but
[39.72 → 44.80] our friends at Rackspace continue to dedicate themselves to support the open source and
[44.80 → 49.54] developer community with their developer discount, and now you can go make something awesome on them
[49.54 → 54.44] you're the makers each day you get up thinking about new awesome amazing stuff, and they just want
[54.44 → 59.64] to give back and help you put your imagination and skills to work and Rackspace wants to give you
[59.64 → 64.00] something special just to say thank you sign up today for their developer discount and get three
[64.00 → 69.56] hundred dollars three hundred dollars in free cloud services on your Rackspace cloud account
[69.56 → 74.78] this discount applies to new products like their performance cloud service as well as their cloud
[74.78 → 80.40] queues, and you're even eligible for early access to new features and products they roll out so
[80.40 → 87.36] make something awesome get started today developer.rackspace.com slash dev trial and now on to the show
[87.36 → 94.94] we're joined today by parker Moore he's uh parker you're a developer you're doing all sorts of cool
[94.94 → 99.78] stuff you're you're you're young you're still going to school you're interning at GitHub you have a
[99.78 → 105.22] pretty fantastic story so um you know I wanted to have you on the show because I've been a fan of what
[105.22 → 108.88] you've been doing with Jekyll so I wanted to kind of hear from the horse's mouth how to speak
[108.88 → 114.10] about whom this man is and what you all are what you're doing um in open source and what you're
[114.10 → 119.56] doing for uh for coding and stuff like that so lets uh let's kick off the show by I guess the
[119.56 → 124.82] the easiest way possible maybe to give the listeners a peek into who you are so when you introduce yourself
[124.82 → 129.90] to a crowd of people how do you do it um well I guess I've never had to introduce myself to a crowd
[129.90 → 137.04] of people of a technology or high technology background um but I'll give it a shot um as you said
[137.04 → 144.90] I'm parker um I'm a student at Cornell University um about to graduate um in August with a degree in
[144.90 → 149.60] information science um I've been programming for a really long time since maybe seventh grade
[149.60 → 159.30] and have loved it I found ruby um in maybe 2011 and have loved it ever since it's a fantastic language
[159.30 → 168.18] I have a lot of fun um and in 2012 I found myself um conversing with tom Preston Warner
[168.18 → 176.22] and um I asked to take over the project Jekyll and the rest is sort of history yeah that's that is a
[176.22 → 181.22] that's I want to tell that history as best we can so let's let's maybe rewind a little further back
[181.22 → 186.68] in the day then so you said you've been programming for a while um how early seventh grade is when I started
[186.68 → 191.28] um my math teacher in seventh grade uh with whom I spent a lot of time because that was the year
[191.28 → 196.02] that I wanted to get ahead in math, and so I was taking two math courses simultaneously um I forget
[196.02 → 201.52] what they were but like geometry probably you know uh probability that sort of thing um and then also
[201.52 → 207.86] moving up to sort of more of the pre-calculus stuff so um I was spending a lot of time with this
[207.86 → 215.76] this math teacher um, and he was a huge math geek, and he had a bunch of apples 2e's in his
[215.76 → 222.62] room as well as a couple old mackintoshes um and this was right before the mac g5 came out so this
[222.62 → 231.42] is you know when is this actually 2003 4 I'm guessing based on math around 2000 well I'm 21 now
[231.42 → 235.64] and I'm just graduating from college and I remember that September 11th attacks were in fourth grade
[235.64 → 242.52] so it was three years after that okay so I think it was um I think it was closer to 2004
[242.52 → 249.60] um, but anyway year is not that important um so I learned how to program in basic um with a group
[249.60 → 254.36] of friends we would take our lunch period, and we would go to this teacher's room Mr martin
[254.36 → 261.04] his room, and we would all leap onto an apple to eat, and we would program for the entire period if we
[261.04 → 266.60] weren't watching Monty Python or whatever um so we had a grand old time and I learned a lot of the
[266.60 → 273.36] basics of procedural programming um in basic if you don't know you have to give every line that
[273.36 → 278.62] you type of code has its own line number so you type one and that's your first line and then you
[278.62 → 284.86] you know print high or something and then 10 uh or two you could say two if you wanted to um
[284.86 → 292.12] you know get variable or something so um I learned a lot about how to think like a computer and sort of
[292.12 → 298.88] the basis of my computer science knowledge comes from that that time in lunch period
[298.88 → 305.76] um and I didn't actually start any formal computer science um lessons or any formal computer science
[305.76 → 314.66] until 10th grade when I took um cs1 and 2 at my high school um, and we learned java with carol the robot
[314.66 → 324.16] um whom we would program to go around a grid and collect like buttons or something um so if it was
[324.16 → 329.80] an amazing experience um and I ended up doing um advanced placement computer science my senior year
[329.80 → 336.02] in high school um and i sort of diverged a little bit in college I went to McGill university for my first
[336.02 → 343.32] year and studied linguistics and philosophy um with an a hint of political science um and then
[343.32 → 349.66] transferred to Cornell and decided you know computers are amazing let's study them let's study the
[349.66 → 355.26] sociological the psychological the economic impact of information and the information technologies
[355.26 → 359.88] that we have available to us and so that's sort of what I've been doing since I transferred to Cornell
[359.88 → 365.50] wow that's uh that's quite a history man I mean I'm not really even sure what to dive deeper into except
[365.50 → 373.18] for you know I guess uh javas is one maybe sort of somewhat fun thing to begin learning with
[373.18 → 380.08] but maybe also just as hard and not so encouraging um but then at the same time you're kind of where
[380.08 → 385.00] you're at now um you know you're contributing heavily to open source you look at your
[385.00 → 389.84] punch card on your GitHub profile, and it's just like it's straight up green so um I don't even know
[389.84 → 395.48] how you actually do it and do school and do a lot of the stuff you do you say in your free time you
[395.48 → 400.34] help maintain Jack I'm not sure if your free time is all the time or what, but maybe we can clear that up so
[400.34 → 408.32] well so I will say um I can give GitHub a little bit of credit um they will mark a box green
[408.32 → 414.34] even if you only have one commit, or you open one issue so you know my minimum on in terms of the
[414.34 → 420.98] GitHub uh punch card is one thing a day one contribution a day so that's not you know not too
[420.98 → 427.50] substantial um but if you know certainly that punch card keeps me active and keeps me busy and keeps me
[427.50 → 433.48] me motivated which is an interesting um element of that particular feature um but I got into open
[433.48 → 444.00] source in 2010 um do you remember the iPhone tracker um which tracker um I forgot exactly what it
[444.00 → 450.90] did specifically i it is would track you track where you were on an app that you could install on your
[450.90 → 458.02] phone it would track where you were um and send that information to a server and there was some
[458.02 → 464.28] element of subversion within this like there was some subversive element to this app such that you
[464.28 → 468.98] didn't necessarily know that you were being tracked maybe it was based on Wi-Fi address or something like
[468.98 → 475.42] that so the um it was in a news story and maybe in the New York times that I was reading often
[475.42 → 481.76] and so I found GitHub because the source code for this particular app was on GitHub and my very first
[481.76 → 487.82] pull request was a pull request to this Objective-C app I'd never touched Objective-C in my whole life
[487.82 → 494.82] um, but there was a problem with um with closing I forget exactly what it was but with closing
[494.82 → 500.12] down a piece of the app um when the app was when the user went back to the home screen
[500.12 → 504.80] or switched to a different app um so that was my very first pull request in Objective-C
[504.80 → 513.48] um and that was I guess the very first pull request being in the fall of 2010 right after i
[513.48 → 519.56] had started at McGill and I was just getting into a friend of mine um well an acquaintance rather um
[519.56 → 526.60] from Rochester where I'm from um it works at apple now and was a huge buff he used he was part of the
[526.60 → 532.50] the team that made cloud the cloud app okay um nick Paulson he's sort of been one of my like programming
[532.50 → 540.56] heroes um over the last several years in that he is just like a prodigy um exceptional at what he does
[540.56 → 546.92] um so i sort of got to know him a little bit through a mutual friend and got to know his work
[546.92 → 553.58] and was interested in mac and iPhone programming thought you know this will be great but then was
[553.58 → 558.28] a little bit worried because it was so tied to particular products it wasn't something that I could
[558.28 → 563.60] run anywhere it was if the iPhone doesn't exist then my job doesn't exist so i sort of moved away
[563.60 → 570.82] from that platform centric right all right um but yeah so i I found open source to this iPhone tracker
[570.82 → 576.92] project and in a way got hooked I would keep going back to GitHub more and more as time went by
[576.92 → 585.94] um and the summer before my junior year which was I guess the summer of 2012 I worked for um several
[585.94 → 591.76] companies but I worked for Cornell in the college of agriculture and life sciences communications
[591.76 → 596.16] department not the academic department but in the sort of college communications department
[596.16 → 602.42] and we were rebuilding our site and I'd used Jekyll a little bit heard about it and said why don't we
[602.42 → 607.16] use Jekyll for this site it'll be great it's all the uh the information that they needed or
[607.16 → 612.94] you know the requirements for the site um the cals.cornell.edu which is still running Jekyll at the moment
[612.94 → 619.72] um all the requirements were perfect they fit the bill perfectly for a static site
[619.72 → 625.28] generator so I was like let's use Jekyll, and we used Jekyll, and it was kind of painful um and I was
[625.28 → 630.58] writing a lot of plugins and hacking around um and going through the source code and sort of learn
[630.58 → 638.44] the ins and outs of how Jekyll worked through that experience and also the annoyance um of there were
[638.44 → 644.28] string encoding errors, and you know the file system watcher was uh directory watcher was still really
[644.28 → 651.74] old and so there was a lot to be done and I recognized this um and in December I said you know
[651.74 → 657.32] I really like this project and I really want to see it succeed, and so I emailed tom press and Warner
[657.32 → 663.84] um, and he eventually got back to me around Christmastime and was like let's skype, and so we chatted on
[663.84 → 670.06] skype and um he was like all right I'm going to give you a contributor access to the repo um you
[670.06 → 674.18] seem to know what you're doing um just don't merge any pull requests don't change anything in master
[674.18 → 679.92] yet great so like just go through the issues, and so I spent my entire winter break going through the
[679.92 → 688.10] issues on majumbo Jekyll um and went through like 300 or 400 in the first week um just sort of going
[688.10 → 695.64] through and closing the ones that were um that we know had to close because they were past done or
[695.64 → 704.32] um it was a quick fix or whatever and um and actually one day so I was in Rochester for that
[704.32 → 712.72] time and um nick Toronto um q rush crush yeah um on Twitter and GitHub um was also a contributor to
[712.72 → 718.24] to Jekyll he had access from you know from early on um, and he's in buffalo and buffalo is only about
[718.24 → 724.64] an hour away drive from Rochester so I went one night to a buffalo open hack night um and he and i
[724.64 → 729.96] hacked on Jekyll um which was awesome, and we closed a lot of issues as a result of that that one
[729.96 → 735.04] night so just sort of got more and more involved and became more and more obsessed with this product
[735.04 → 743.96] um and the potential of static sites um and sort of continued on and I went in January late January
[743.96 → 751.20] of 2013 I decided to take a semester off from school altogether and went to go work for um sex
[751.20 → 757.86] wunderkinder in Berlin they make Wunderlist right and um and I loved Wunderlist and I love the people
[757.86 → 762.76] that were that work there um so I was like hey you know is there a possibility that I could intern with
[762.76 → 767.50] you, and they interviewed me, and they were like you should come intern um and so of course yes
[767.50 → 776.66] what have you, and so i I went to go intern um and learned a lot there um which you know which was
[776.66 → 781.36] and it was an absolutely amazing experience so you're actually in Germany or just did you intern
[781.36 → 787.14] from here in the states i was actually living in Berlin I lived on Chelsea just off of
[787.14 → 796.50] no on Chelsea strafe um right there in matte wow so i I had a lot of free time because in
[796.50 → 802.04] college I didn't I don't have a lot of free time when I'm in classes um but I have a lot of free time
[802.04 → 809.02] when I'm working nine to five so which is surprising to me um so i was you know hacking on Jekyll more
[809.02 → 816.50] and more, and we released 1.0 by may and so this is what about I guess may 2013 right yep
[816.50 → 821.54] just about a year ago so you've kind of had this pattern of impressing people and getting the
[821.54 → 828.04] right connections i I guess pretty much early on and then using that as a way to bootstrap your
[828.04 → 834.08] skill set and bootstrap your abilities and kind of get in the right places so how much I guess maybe
[834.08 → 839.58] to rewind maybe a tiny bit how much do you know about the earlier days of Jekyll and kind of where
[839.58 → 845.38] it came from and its philosophy and then I guess now uh as of this past may which would be one year
[845.38 → 851.80] since 1.0 basically right so you got 2.0 that just came out yep yeah so I don't actually know
[851.80 → 856.76] very much about the early days I know it used to be called auto blog um so it was originally very
[856.76 → 863.90] focused on blogging um and originally very um more blog centric than blog aware as it now
[863.90 → 870.98] states right um I'm not sure what Tom's original wishes for it were I think he just wanted
[870.98 → 874.66] to write a static blog and didn't like any of the products that were available, and so he wrote it
[874.66 → 881.66] um along with nick so I'm not really sure about the early days, but the philosophy was
[881.66 → 888.22] was in the README um a blog aware and in the um GitHub description as well a blog aware static site
[888.22 → 894.44] generator so i sort of took that and based on the issues and how people were using it um moulded it into
[894.44 → 898.68] something that I thought people would like yeah let's talk about that a little bit then because
[898.68 → 907.94] um i it almost seems like you're you've said a couple of times a product uh you kind of act even i
[907.94 → 913.10] would you probably would agree with this but um like a product manager like you listen to the crowd
[913.10 → 917.98] or you kind of um you know you go through the like you'd mentioned you know earlier in the in your
[917.98 → 923.18] history with Jekyll that you kind of went through several hundred issues in a weekend to kind of
[923.18 → 928.74] get a heartbeat of where it's at what kind of um a telltale signs I guess did you use that are
[928.74 → 934.06] inherent in issues with Jekyll that helped you understand where it was coming from or where it
[934.06 → 939.02] needed to go to be successful for the people that were using it that's a really awesome question i
[939.02 → 945.86] think um when I was going through the issues the biggest of course uh indicator of a problem or a
[945.86 → 951.12] feature that should be implemented is the sheer number of comments on the um on the issue if there's
[951.12 → 957.00] an issue like for right now there's an issue that stands open um for incremental regeneration uh
[957.00 → 962.40] basically taking a site that's already been built um understanding the current state and then only
[962.40 → 968.06] only changing or rebuilding the pieces that need to be rebuilt which is a know a NP hard problem
[968.06 → 972.20] yeah it's probably a huge saving too for the disc you're on and just in general this is speed
[972.20 → 976.76] exactly, exactly it would be a huge win um and there are a lot of people who've said this would be
[976.76 → 980.70] amazing this would be amazing and of course I mean you know we've just both agreed it would be an
[980.70 → 986.32] amazing feature um the as I was going through the know several hundred issues I think there were
[986.32 → 993.80] like 623 or something uh open issues when I took when I came on to the project um as I was going through
[993.80 → 1000.20] them depending upon the number of comments and the sort of logic of each argument um i sort of weighed
[1000.20 → 1007.38] them in a certain way um if there was a and sort of got to know how people were using it based on
[1007.38 → 1013.42] their comments and the issues and the know occasional site that I would come across um on
[1013.42 → 1020.02] some repository on GitHub um and as that as i sort of got to know a little bit more about how people
[1020.02 → 1026.12] were using the product um I said you know this we should support this or this is not really how we
[1026.12 → 1030.28] envision this product to be used, but maybe we can make a compromise and just make it easily
[1030.28 → 1034.56] extensible so they can build it on their server without having to do all this crazy monkey patching
[1034.56 → 1041.40] etc um and so sort of weighing what are Jekyll's primary objectives based on what was in the README
[1041.40 → 1048.64] versus how are people using it versus how do people want to be using it what is the best sort of
[1048.64 → 1053.70] middle ground between those three elements um and I've I've that that took a lot of thought
[1053.70 → 1060.14] and when you first take over a project or first enter into a project like Jekyll that has been
[1060.14 → 1068.08] around for five years um and is relatively successful um it is took me probably six months
[1068.08 → 1075.68] to figure out exactly what the trajectory for this product should be I'd imagine even your
[1075.68 → 1081.70] your methodology had to be pretty methodical too to kind of go through comments and I mean maybe
[1081.70 → 1085.50] you're weighing them based on is there a code sample you know how passionate is this person is
[1085.50 → 1092.38] it you know is this person commenting on several other issues as well or kicking up issues um i have to
[1092.38 → 1097.28] imagine that was a pretty tough job to triage and like you said six months to even get a heartbeat
[1097.28 → 1102.88] that's that's a lot yeah um, and it's it part of it is because there's so many people using it and
[1102.88 → 1108.04] and as well it was still being used on GitHub pages so i sort of had to weigh in well how would
[1108.04 → 1114.04] this change GitHub pages is this still secure for GitHub pages um and one of the things that tom said
[1114.04 → 1120.82] to me during our initial chat was um basically like instill the fear in me of change which is very
[1120.82 → 1129.24] interesting um that said Jekyll is good as it is good at present it's good um it can be great
[1129.24 → 1135.82] but it shouldn't be but the the the way to get to greatness is not through completely rewriting
[1135.82 → 1140.58] everything that you have um basically to say add on to what you have change the things that
[1140.58 → 1147.20] absolutely must be changed um but don't go too crazy basically um so in terms of accepting
[1147.20 → 1151.76] pull requests that made me very skeptical um originally I was like oh you want this feature
[1151.76 → 1158.38] lets you know let's merge it in it'll be great but as long as the CI passed um but as after time
[1158.38 → 1164.54] after some amount of time even the general idea not even just the code I would scrutinize
[1164.54 → 1168.88] um significantly is this something that is useful to the majority of Jekyll users for example
[1168.88 → 1177.52] is this something that is safe to run on GitHub pages is this something etc, etc so um it is has
[1177.52 → 1184.30] taken a long time but yeah it's its been I think that's a really key part to taking over a
[1184.30 → 1192.58] project into to making something cool so what um I guess maybe playing off of if I'm tracking with
[1192.58 → 1199.58] you uh early on tom said you know hey you know kind of toe the line so to speak you know when you
[1199.58 → 1206.00] first took over how is that how is that contrast against how you are now with the project and what
[1206.00 → 1213.72] changed so when we when I initially took over tom was still very much present um
[1213.72 → 1220.46] you know quote unquote so I could, I had a tag on the issues that was at my jumbo and I would email
[1220.46 → 1225.20] him if that got too high maybe 35 issues or something like that, and it just needed a decision
[1225.20 → 1230.72] by him, it just needed you know hey what do you think about this um is this a good idea bad idea
[1230.72 → 1236.98] so i sort of at the beginning was really chatting with him a lot um as much as possible
[1236.98 → 1243.52] and getting his idea about what the product and where it should go and as a contrast to now
[1243.52 → 1252.38] I have complete control um I can't imagine so I have complete control in the literal sense in that
[1252.38 → 1258.96] I can change anything but uh there are still some philosophical constraints of course in that I want
[1258.96 → 1263.42] it to be something that people like to use etc um and something that that continues on with the
[1263.42 → 1268.70] tradition of what Jekyll has been um if you take a product, and you completely modify what it's like
[1268.70 → 1273.54] completely change everything then it's no longer the same thing so existing Jekyll sites for example
[1273.54 → 1279.80] I don't want someone to write a site and then for it to immediately break um we've with the 2.0 release
[1279.80 → 1286.46] we did our best to maximize the number of backwards compatible changes um I think there was like
[1286.46 → 1293.14] maybe one backward incompatible change, and it was we still had a way to work around it so
[1293.14 → 1302.00] not to mention too you also had GitHub as uh I guess an uh a customer so to speak um right because
[1302.00 → 1306.20] they're using it for pages, and they obviously have a trajectory where they're taking uh pages and what
[1306.20 → 1312.46] they're doing with it not it's obviously a large part of the open source ecosystem where people host
[1312.46 → 1318.54] their docs on there, or they host their you know single page kind of here's my repo kind of thing or
[1318.54 → 1324.80] even just simple sites it was a part of what GitHub was doing so how did uh I guess maybe to break the
[1324.80 → 1330.60] seal on this so right now you're an intern also at GitHub so that that kind of had to blossom into even
[1330.60 → 1337.82] new opportunities for you can you talk a little about that yeah so um my exact title is a
[1337.82 → 1346.88] as a GitHub pages contractor and so i as a contractor and um I'm working on GitHub pages and trying to make it
[1346.88 → 1351.78] an even better platform um some of the changes that we've released like the site.GitHub namespace
[1351.78 → 1357.28] um there's been there's been a complete rewrite behind the scenes in the back since I've I've
[1357.28 → 1364.46] joined the team um and basically what that's done is allowed me to gain new insights into how
[1364.46 → 1369.72] jackal's being used um in particular I'm working with Ben Walter who's an amazing guy um really
[1369.72 → 1376.80] brilliant um he recently he graduated from law school um was a WordPress core contributor um
[1376.80 → 1384.40] was a white house presidential um innovation fellow is just a crazy cool guy um, and he's sort
[1384.40 → 1388.94] of been my mentor on that project um the guy watching over me making sure I don't mess up too
[1388.94 → 1397.06] many things and uh and because he's focused on government I've gotten a huge I've I've gleaned a
[1397.06 → 1406.42] new or gained a huge appreciation in how um how jackal is being used on the massive scale or larger scale
[1406.42 → 1412.64] um so if you're is you're a government institution that wants to publish data how can how are they
[1412.64 → 1418.72] using jackal to publish data for example um they're using WordPress and jackal in many occasions
[1418.72 → 1429.18] to publish open data to um publish process um project open data is a jackal site um, and they're
[1429.18 → 1435.36] using that to write policy around open data if you're you know the city of Chicago how should your how
[1435.36 → 1439.74] should your data be released and what are what are the guidelines surrounding that that entire
[1439.74 → 1446.74] project that um every everything within that all the content is written um written as a jackal site
[1446.74 → 1453.18] that's funny that you mention uh Ben because you know he also just is a core contributor to
[1453.18 → 1459.06] WordPress uh you know for those who know about jack or maybe this is you're a listener this is the
[1459.06 → 1464.18] first time you're hearing about it, I don't know where you've been but um WordPress and Jekyll tend
[1464.18 → 1470.58] to fall into the same conversation because it tends to be a fork a choice of left or right Jekyll or
[1470.58 → 1475.60] WordPress, and you know a lot of the reasons why developers like is one because it's just
[1475.60 → 1479.68] developer centric I think far more than maybe WordPress is but not in a bad way
[1479.68 → 1484.40] WordPress is kind of designed and delivered as a product for different types of people and different
[1484.40 → 1489.32] types of developers, but you know the separation of the database and stuff like that so does
[1489.32 → 1493.44] Ben get involved with the product is he involved with Jekyll now or is he just kind of advisor to you
[1493.44 → 1499.44] he's he's definitely involved in the product um not as much as I am you know he's not he's not
[1499.44 → 1504.44] around day to day um but when I have sweeping questions or large questions I would have sweeping
[1504.44 → 1511.28] effects on the product I tend to run them by him um he actually was kind enough to
[1511.28 → 1516.52] invite me out to San Francisco um or out to the GitHub headquarters I was interning for visual
[1516.52 → 1521.72] supply company at the time-out to the GitHub headquarters one Saturday to sort of host a
[1521.72 → 1526.44] Jekyll NATO summit uh there's a GitHub issue with all the on jekyll with all the details
[1526.44 → 1534.88] of that summit um, and we sat in the situation room in the GitHub office um, and it was Ben and me and
[1534.88 → 1541.80] mis love um who's a great guy and Tom came for about an hour um and or an hour and a half and then
[1541.80 → 1550.06] um garden um as well GJ Parisian I think um I'm not sure about your name sorry garden uh your last name
[1550.06 → 1556.52] rather um, and so we sat around and matt uh rogers of course my co-maintainer um he was in he
[1556.52 → 1563.98] wasn't able to come physically but he was beamed in via blue jeans um and so we sort of
[1563.98 → 1569.14] chatted about the future of Jekyll what we wanted for 2.0 what we wanted for 3.0 sort of what
[1569.14 → 1578.32] the future would be um so Ben has been a significant advisor um and has sort of opened up or suggested
[1578.32 → 1583.90] things like a NATO summit where we would all meet and chat about it, you know in meet space um that
[1583.90 → 1590.10] I would never have thought to do um so he and you know he scheduled all of that he flew out from DC
[1590.10 → 1596.74] um to get to San Francisco just for this um, and it was an it was a really cool experience so he's been
[1596.74 → 1602.14] he's been an advisor a serious very serious advisor of this project um partly because I think he sees
[1602.14 → 1608.74] the potential of static site generators and the because Jekyll's already on GitHub pages the amazing
[1608.74 → 1616.66] potential for um open data for um open source websites in general um the bootstrap website the
[1616.66 → 1623.38] ratchet websites are both open source and on GitHub pages um and so and the know it's an
[1623.38 → 1629.54] alternative to WordPress in many ways because it is very content focused though it's less focused
[1629.54 → 1634.90] about how does my theme look um it's more focused on what are the words that I'm putting out there to
[1634.90 → 1643.56] for the world to see um if he's sort of been an evangelist in many ways of Jekyll um and a wonderful
[1643.56 → 1650.52] supporter of it let's pause the show for a minute give a shout-out to our sponsor snap, snap is a
[1650.52 → 1655.64] hosted CI and continuous delivery service that goes far beyond letting you do continuous deployment
[1655.64 → 1662.36] don't waste your time set up your own CI box under your desk use snap, snap has first class support for
[1662.36 → 1667.16] deployment pipelines with snap you can push any healthy build to multiple environments automatically
[1667.16 → 1671.72] or on demand this means with snap you could do things like deploy to your staging environment today
[1671.72 → 1677.88] verify it works and later deploy the exact same build to production snap integrates deep with
[1677.88 → 1683.24] GitHub has great support for lots of languages databases and testing frameworks snap deploys your
[1683.24 → 1690.84] application to cloud services like digital ocean Heroku open shift AWS and many more you can also use
[1690.84 → 1698.20] snap to push your ruby gem to ruby gems and snap is always free for open source projects try to snap for
[1698.20 → 1707.08] free for 30 days today sign up at snap ci.com slash the changelog i never really thought about the I mean i
[1707.08 → 1711.96] guess it's it seems kind of obvious and logical but i never really thought about the impact to
[1712.68 → 1719.40] increase the level of open source whether it's code content or whatnot that Jekyll's actually had the
[1719.40 → 1723.72] impact of i always kind of I guess i really just never thought about it like that because I mean
[1723.72 → 1729.40] we covered Chicago's open data about a year ago when they first started to publish a lot of their
[1729.40 → 1734.04] open data and whatnot they're leading the way in a lot of ways for local governments to do that kind
[1734.04 → 1740.68] of stuff and then what you mentioned too about just documentation and then twitter bootstrap and other
[1740.68 → 1746.68] sites that are kind of put out there, and they're open right like even your site your blog is
[1746.68 → 1751.80] open on GitHub it's you know it's its kind of like it just seems like a natural thing and it only
[1751.80 → 1757.96] helps uh bootstrap and bolster this open source ecosystem we all kind of desire to be in
[1758.76 → 1766.36] exactly and one of the main tenants of Jekyll um has always been to as much as possible and
[1766.36 → 1772.52] GitHub pages helps with this tremendously as much as possible open source your website um yeah let
[1772.52 → 1778.68] other people learn from it there's a great uh page on the wiki the Jekyll wiki called sites and it we
[1778.68 → 1784.60] have this one rule you post the link to your site, but you must post the source for your site as
[1784.60 → 1789.00] well so if your sort is your site isn't open source it can't be on the sites page and there's something
[1789.00 → 1795.00] like a thousand almost a thousand um sites with their sources linked directly next to the to where the
[1795.00 → 1800.36] page is so if you go to see a site that you really like then the source is right there for you to look
[1800.36 → 1806.44] at um so it's a great learning tool and anyone who has a site anyone who has a GitHub
[1806.44 → 1814.20] account can edit it so it's it the Jekyll community has been hugely a huge proponent I guess
[1814.20 → 1819.08] of open source and making sure that they can learn from each other the way that open source champions
[1820.20 → 1825.96] before we uh I guess before we turn away from I guess maybe newer topics more topics
[1825.96 → 1830.84] uh I want to ask you a bit more detail if you can share it about the conversation that Ben
[1831.32 → 1837.24] had with you when he kind of enlightened you about the overarching ecosystem of Jekyll like
[1837.24 → 1840.84] what was that conversation what were some of the things he kind of fed you to help you really get
[1840.84 → 1844.12] the aha moment and kind of be able to tackle what you've done
[1846.12 → 1851.96] the so it's been sort of an ongoing conversation it's its you know comments here and there in
[1851.96 → 1859.08] the GitHub pages repo and on Jekyll um as well as at that NATO summit but the overarching or
[1859.08 → 1867.08] sort of the aha moment that I had was um when Ben said two things that i really i
[1867.08 → 1871.88] really cared about one was um be the pull request that you want to see in the world which is really
[1871.88 → 1877.08] cliché but really awesome and goes along with the um let's make Jekyll the coolest thing that
[1877.08 → 1883.16] it can be not because we want it but because everyone wants it um and because everyone
[1883.16 → 1888.60] can contribute to it if they wish um and the second thing is make it as simple as possible
[1888.60 → 1896.04] absorb complexity as much as possible that is the way to a good product um and that I've sort
[1896.04 → 1902.36] of you know GitHub itself um the organization and all of its employees champion that that concept
[1902.36 → 1906.36] if you're not you don't make your user interface simple if you don't make the process
[1906.36 → 1910.20] simple then people aren't going to use it people aren't going to do what you're asking them to do
[1910.84 → 1915.88] so um he's really moulded this product into something that is as simple as possible
[1916.44 → 1924.12] um and that's you know sort of where it's been an ongoing conversation but um sort of where we get that
[1924.12 → 1931.96] that that heightened sense of simplicity from I guess since uh this might be a good time to talk about
[1932.36 → 1937.80] um you know I guess earlier um I'm almost forgotten which month it is sometimes but I guess it's
[1937.80 → 1942.20] earlier this month because it's its the last day of the month we're recording on May 30th by the
[1942.20 → 1947.32] way um because the show doesn't always come out the same day we actually record it but earlier this
[1947.32 → 1955.80] month um you released um Jekyll 2.0, but you know kind of flipping that on its head last year you were
[1955.80 → 1963.72] releasing 1.0 a lot's changed you got a lot of newfound vision because of this history and
[1963.72 → 1969.48] all that what is what are some of the core things that change from Jekyll 1.0 to Jekyll 2.0 and then
[1969.48 → 1974.84] also I guess to maybe make sure that the those who have been using Jekyll for the last five years
[1974.84 → 1982.36] don't have breaking sites right so to answer the first half the question of what has changed um we
[1982.36 → 1988.68] introduced a lot of things that a lot of new concepts and a lot of um support for technologies
[1988.68 → 1994.04] that people were using so the two main concepts that I really enjoyed working on and really enjoyed
[1994.04 → 2001.16] uh releasing I was really excited to release were um collections and uh YAML front matter defaults
[2001.72 → 2011.00] um, so collections allow you to define a series of documents um all collected into one entity as it
[2011.00 → 2016.76] were um so one of the reasons or the reason that we originally wrote this um this feature was
[2016.76 → 2024.52] actually because during the Jekyll NATO summit Milo said I'm writing for kept the API documentation
[2024.52 → 2031.72] I want to have one page per document or rather one page per method in the or function in the API
[2031.72 → 2039.08] and I don't want to have to mangle Jekyll you know monkey patch it up the Yazoo in order to actually
[2039.08 → 2047.40] write write write out individual pages for um for my um uh excuse me form for the API
[2048.44 → 2055.72] and I don't want to mix up the pages um or posts and I don't want to use posts for it etc
[2055.72 → 2061.40] so he wanted a lot more customization um he wanted to be able to take the the documents and
[2062.20 → 2068.60] import them into collection or into pages as well so include them um and write them out so he needed
[2068.60 → 2074.44] them to be to some insurance to make sure that they were processed beforehand etc he wanted them to be
[2074.44 → 2080.36] to be custom um he didn't want to necessarily have to have them write out as a file um so collections
[2080.36 → 2088.12] natively or in the base most basic sense um you have a series of documents um that contain data YAML
[2088.12 → 2095.80] front matter um and content and that's it um you can optionally set up um each individual document to
[2095.80 → 2100.76] have an output file um that just goes into forward slash collection name forward slash document name
[2100.76 → 2108.76] um and that will output an individual file if you want that um, but the idea is sort of data um
[2109.40 → 2114.68] plus content mixed together nicely that isn't this isn't just YAML can you give an example of it
[2114.68 → 2121.16] is that I'm thinking is it like if I were publishing a podcast so to speak would it be like a podcast is
[2121.16 → 2125.88] that what you mean where it acts like a page or acts like a post does by normal traits but you kind
[2125.88 → 2133.24] of give it its own name space, and it's its own kind of model so to speak right so you use collections
[2133.24 → 2137.32] for anything that isn't necessarily date sensitive, although you can use dates and collections if you
[2137.32 → 2146.28] want to um with when we were first setting up the Jekyll site for example we had each docs page set up in as
[2146.28 → 2153.72] a post it was just like 2010 01 01 here's my post uh or here's my docs page, and we set it up as a post
[2153.72 → 2158.84] because we wanted to make sure it was processed before the pages write them out into pages etc um
[2158.84 → 2166.84] and have an individual HTML file generated for each docs page as well so when we were
[2166.84 → 2173.24] doing that if it was creating a collection of items but in the only collection that we had which was
[2173.24 → 2179.32] posts um you can think of posts as a date centric collection okay um of documents and each document
[2179.32 → 2185.96] is called a post in that case um so what we wanted to do is take that idea and generalize it not make
[2185.96 → 2193.16] it so dates centric people were kept asking hey can we remove the dates from our posts of course in an in
[2193.16 → 2199.80] in a blog you every post should have a date um that's the point of a blog it's its a chronologically
[2199.80 → 2205.96] ordered um series of content so we said well if we're not going to take dates out of posts
[2205.96 → 2214.52] lets you know create some more generalized concept um that's based on posts but um allows you to um
[2215.16 → 2222.28] to collect various items um and write them out to individual files or just have that data um so
[2222.28 → 2229.56] an example is if we were to rewrite if Jekyll 2.0 were up on getup pages um I would take the all the
[2229.56 → 2236.76] docs pages that we have for Jekyll at the moment in site docs and I would move them into a collection
[2236.76 → 2241.80] called docs they would probably exist the same way that they do right now, but they would exist within
[2241.80 → 2249.32] this site. Docs collection this would allow me to iterate over them if is there were maybe two pages
[2249.32 → 2254.68] that I wanted to have on the same output page so two or two documents that I want to have this on the
[2254.68 → 2261.00] same page or if I wanted to list all the pages in like a site map um then I don't have to say okay
[2261.00 → 2269.88] site. Pages like four page and site. Pages in liquid um and I explicitly remove all the CSS pages
[2269.88 → 2276.76] or then you know index.html pages that aren't docs I have this one subset of the site in this underscore
[2276.76 → 2284.52] docs folder that i can iterate over that I can output that I can etc um as its own entity
[2284.52 → 2290.52] so I guess you can think of collections as a subset of the content of a site in a way
[2290.52 → 2295.88] and this is just one of the many changes and also I guess it's probably smart to drop a caveat in there
[2295.88 → 2302.38] that uh the collections is kind of unstable it's in it's its out there, but it's not finalized it may
[2302.38 → 2308.72] change right, right um and the other thing that we did, or the major feature was YAML
[2308.72 → 2313.54] front matter defaults so if you kept writing that you wanted the layout to be article or layout to be post
[2313.54 → 2319.92] um in all of your posts or all of your pages in a specific uh subdirectory now all that you have
[2319.92 → 2326.54] to do is add a few lines to your configuration file, and you have layout post set for all the
[2326.54 → 2331.46] posts or pages that you specify um right now YAML front matter defaults don't work with collections
[2331.46 → 2338.30] which is a bummer um, but we're we're working on getting it for the 2.1 release which should happen soon
[2338.30 → 2347.26] so I'm trying to think of where we can go where we can go next I know I got a couple of things on my
[2347.26 → 2350.10] my list that I want to mention but um
[2350.10 → 2358.76] I guess maybe I don't exactly struggle to really I mean I guess maybe to some degree I do
[2358.76 → 2363.44] but you know what's the sweet spot for Jekyll you mentioned earlier with Cornell working there and how
[2363.44 → 2368.16] you had this list of requirements and Jekyll was perfect, but that was way back you know several
[2368.16 → 2374.32] years ago at least it seems to be um you know what is the sweet spot for Jekyll I know we talked a
[2374.32 → 2378.40] little bit about documentation but for those who are listening out there that aren't using Jekyll
[2378.40 → 2385.42] what would make them want to use it why should they use Jekyll like it's not a cms it's not a blog
[2385.42 → 2392.92] it's evolved right, right I would say for two reasons I always stick with Jekyll the first
[2392.92 → 2399.94] reason is that I can use git I can use my lovely version control system um to version my content
[2399.94 → 2405.74] not just the theme or whatever that I have um but I can version my content which is amazing I can submit
[2405.74 → 2411.88] a pull request for my content um and that's that's hugely powerful um the second reason I'd say is
[2411.88 → 2417.70] because it's a static site generator and this is true of any static site generator um the sweet spot
[2417.70 → 2424.16] is really in page load time um there have been a couple of people who run um Jekyll sites on their own
[2424.16 → 2432.56] servers maybe like a t1 small or something um on AWS and they never their server never goes down
[2432.56 → 2438.20] whereas if you have WordPress you run into problems with memory, or you run into problems with the database
[2438.20 → 2442.90] load being too high and so your database just cancels connections um, or you can't connect to
[2442.90 → 2448.18] it when when someone loads your site so by stripping all of this out and just having a HTML
[2448.18 → 2453.68] file that nginx or Apache says oh here's your static file here like's the content that you need
[2453.68 → 2462.62] amazing um it is reduces any problems you would have with scalability to a ridiculous degree so I know
[2462.62 → 2469.44] I'm kind of uh hopping on one of those things you mentioned there because the changelog is actually
[2469.44 → 2475.66] a WordPress site, and we're on digital ocean we have a pretty beefy server at digital ocean so we like
[2475.66 → 2480.88] it I mean it's its great but for a bit there we had issues with our site toppling over and getting
[2480.88 → 2487.00] database connect connection issues because basically MySQL would uh you know bubble up to the point where
[2487.00 → 2490.72] it would take all the memory and then Apache couldn't run anymore so it couldn't connect to MySQL
[2490.72 → 2498.28] or something to that degree it was just a mess and essentially we kind of did uh essentially what
[2498.28 → 2503.42] I would probably consider a reversal right we kind of did what would eventually just become cached files
[2503.42 → 2509.76] right, but you know we used uh WP cache to cache all of our files which essentially is exactly what
[2509.76 → 2514.66] Jekyll helps you produce in the first place which is a static site essentially take this dynamic site
[2514.66 → 2521.88] and make it static based on cache times, and you know um time stamps and stuff like that so it's
[2521.88 → 2527.90] that's the one that I can actually really kick myself in the butt for but at the same time I love a lot of
[2527.90 → 2533.26] what WordPress gives, but you know i never really um moved over to Jekyll because of like multi-author
[2533.26 → 2537.66] support and stuff like that what do you say to people when they talk about multi-authoring and just
[2537.66 → 2546.60] I guess publishing tools that make the job a little easier so one thing that I've I followed intensely
[2546.60 → 2551.24] and actually that I think Ben originally told me about was prose and I'm sure you've heard of this
[2551.24 → 2557.94] but prose is sort of the silver bullet um or is intended to be at least the silver bullet
[2557.94 → 2564.56] um publisher for Jekyll sites online I've seen this yeah you connect to your GitHub account
[2564.56 → 2571.22] you go to an um repository that you have a site, and you make edits, and you commit them, and it's
[2571.22 → 2577.92] great um unfortunately sort of development on prose has slowed down significantly as it's not being used
[2577.92 → 2585.92] as much by the development seed team um these amazing guys down in um down in DC were the ones who
[2585.92 → 2589.92] originally created it I think they were the ones who originally created the landing page for health
[2589.92 → 2597.04] healthcare.gov using Jekyll um, and so they've created what they of replacement basically for this
[2597.04 → 2602.24] for the authoring tools that WordPress gives you so one of the things that I've always loved about
[2602.24 → 2607.98] WordPress is that it's super simple to go in and make a change, and then you know you click you hit save
[2607.98 → 2614.72] it puts it in the database, and you're done um what prose aims to do is emulate that process but for
[2614.72 → 2620.02] Jekyll sites using version control um so when you instead of hitting save you hit commit um instead
[2620.02 → 2627.04] of you know going to a specific instead of going to your site slash wp-admin you go to
[2627.04 → 2635.00] prose.io slash you know your site uh repo slash the path, and then you edit it commit it you're done
[2635.00 → 2641.56] you said it is it uh slowing down on development right now is that what you said at the moment it's
[2641.56 → 2645.74] it's not really it's under active development, but it's its a little bit slow at the moment
[2645.74 → 2650.48] um and that's just because it's there's no immediate pressure um if there's anyone who's
[2650.48 → 2657.42] really interested in um you know having it continue can you continue to uh to be developed
[2657.42 → 2663.06] um and to see it grow I'm sure that the development seed guys would be interested in hearing
[2663.06 → 2667.76] from you um it's all in JavaScript, and it all runs on GitHub pages except
[2667.76 → 2674.54] something called gatekeeper which is the um Heroku app that does all the OAuth with GitHub
[2674.54 → 2680.54] we'll have to either get them on the show or uh find a way to I guess put some light on that i
[2680.54 → 2684.94] mean that's I'm glad you mentioned that because it's its under development, but maybe they're just
[2684.94 → 2689.60] are they just not feeling like oh it's really needed because it's not being used by a lot of
[2689.60 → 2695.00] people is that the is that the concern now it's being used by a pretty good chunk of people but
[2695.00 → 2700.00] it's its because it doesn't they originally developed it so that they could write healthcare.gov
[2700.00 → 2706.16] right in a way you know the majority of healthcare.gov the content based uh piece of healthcare.gov
[2706.16 → 2709.46] the things that don't need to be dynamic basically the marketplace for example would have to be dynamic
[2709.46 → 2715.04] but um you know just you know FAQs and that sort of thing don't have to be dynamic so they originally
[2715.04 → 2722.56] wrote it so that anyone um could have this wonderful interface for changing files um and so
[2722.56 → 2727.28] people aren't using it as much and the development is slow because they aren't using it anymore
[2727.28 → 2733.98] yeah I feel like I almost feel like there's I know you're in school, and you've got a busy life
[2733.98 → 2738.92] and maybe this isn't you know the only thing you wanted to do in your development career but i kind of
[2738.92 → 2744.02] feel like maybe you might inherit uh not so much another project but at least kind of bring that into
[2744.02 → 2749.76] the fold so to speak because it's so closely aligned with um you know this publishing way for
[2749.76 → 2754.06] Jekyll that makes it a little easier because one of the concerns that I think we tend to have is
[2754.06 → 2759.22] it's okay for us as developers to like you know use git and push via the command line we're very
[2759.22 → 2763.28] comfortable with those kinds of things, but it's when we start to invite our business analysts and
[2763.28 → 2767.98] other people that are not always so fluent with it who may just want to go in make the change like
[2767.98 → 2773.88] you said and click save they want that experience they don't want to you know have a certain ruby
[2773.88 → 2778.64] installed, or you know do I use RVM should I use how do I version my you know how should I use my ruby
[2778.64 → 2782.74] and then you start to bring all these questions into somebody like forget it uh can we just use
[2782.74 → 2787.66] WordPress uh WordPress works, or you know that might be an example of the conversation you might have so
[2787.66 → 2792.64] I feel like there's an opportunity here maybe to bring that into the fold and make it part of your
[2792.64 → 2800.02] your uh your work with Jekyll and GitHub pages absolutely um and i you know we need a couple
[2800.02 → 2805.38] more things for example previews um for a pull request I've always wanted for GitHub pages to build
[2805.38 → 2812.90] pull requests if you can build a pull request then you can see the resulting site um on GitHub servers
[2812.90 → 2818.08] immediately you don't have to wait um, or you don't have to clone it down and deal with ruby installation
[2818.08 → 2823.82] um one of the pain points for Jekyll is definitely installing ruby um it's its not supported technically
[2823.82 → 2829.90] on Windows, but it is um you know it's not too hard to get it up and running um, but it's still a bit
[2829.90 → 2835.52] difficult so there are a couple more elements that I have to come and come into uh into the
[2835.52 → 2842.74] fold here but once those are in place um if they do come to fruition then um then it would
[2842.74 → 2848.46] be a pretty easy fix I think pros is trying to take the intimidating um somewhat intimidating
[2848.46 → 2853.84] interface that GitHub has with issues and discussions and all this business um and make it
[2853.84 → 2859.36] as simple as possible and as friendly as possible um so they and because it's Jekyll specific they
[2859.36 → 2864.70] make ready and will front matter for example um a piece of cake so they just have individual form
[2864.70 → 2870.26] items that you can specify, so your date should be a date and your title should always be um you know
[2870.26 → 2874.24] they give you a text box for your title and a drop-down for your layouts and all of that stuff so
[2874.24 → 2880.32] um so you know there are just a couple more pieces and then and then I think we can make a bit we can
[2880.32 → 2887.58] make the switch so a mutual I guess a mutual friend of ours had uh two questions I guess one of you
[2887.58 → 2890.90] you've kind of mostly answered but if there's anything that maybe you left out that you want
[2890.90 → 2895.20] to mention you're welcome to but so to the questions Brandon Mathis is the mutual friend I'm
[2895.20 → 2900.60] talking about, and we'll talk a bit more about your involvement with him and octopuses and that kind
[2900.60 → 2903.50] of stuff but one of the things he wanted me to ask but I think we've already answered this to some
[2903.50 → 2909.04] degree so feel free to uh riff as needed, but he said you know this is verbatim what he said parker
[2909.04 → 2913.66] came out of nowhere and impressed tom and i both enough to become significant parts of both of our
[2913.66 → 2918.70] projects Jekyll and octopuses as the projects uh get him to talk about how so I think you've kind
[2918.70 → 2923.76] of entered that but is there anything of how that he's talking about that maybe you didn't leak
[2923.76 → 2931.86] so the that's that's a great question the way that I got involved with Jekyll is that I emailed tom
[2931.86 → 2937.34] tom was this is this was at the time the CEO of GitHub um someone that I didn't think I was actually
[2937.34 → 2942.54] going to be in contact with ever he was not replying to issues um but I emailed him and I emailed him
[2942.54 → 2948.70] three times um over the course of like eight or nine months um and finally in December he replied
[2948.70 → 2956.52] so I think the key is to um sort of take that leap of faith as well as and i I got in contact with
[2956.52 → 2960.20] with Brandon because I was following him because I loved octopuses and I was using octopuses for my
[2960.20 → 2965.36] blog um so I was following him and I was like hey do you need any help with octopuses I tweeted at him
[2965.36 → 2969.74] and he was like yeah I would love some help with octopuses and then we just sort of kept going with
[2969.74 → 2976.62] that um and uh so it's you know reach out if you're interested is sort of the key um I think
[2976.62 → 2982.20] that the main bottleneck for finding uh added maintainers is the is to see their interest um
[2982.20 → 2988.30] are you interested in devoting the time to maintain something uh and to make it better um in
[2988.30 → 2993.44] in a more meaningful way than just submitting a pull request here and there um so I'd say persistence
[2993.44 → 2999.50] and just make that initial step okay so maybe dovetailing off of that then his second part
[2999.50 → 3004.68] of that question was uh and I had the same question so it's just kind of from both myself and Brandon
[3004.68 → 3010.04] um, and we'll talk you know for those listening and thinking what the heck is octopuses we'll talk
[3010.04 → 3014.60] about it here in just a second but uh the second part of that question uh a series of questions is
[3014.60 → 3017.76] do you have any and I think you kind of touched a little bit just now on this but
[3017.76 → 3023.88] do you have any advice for those out there who uh are you know similar to you, you know interested
[3023.88 → 3028.10] interested in technology but want to get started with open source software and don't really know
[3028.10 → 3035.56] where to start or really how to break through I suppose I think the main barrier to entry is to
[3035.56 → 3042.48] know how to contribute right so from my perspective go to the project that you're using
[3042.48 → 3048.06] the most maybe you're using rails um rails is a very intimidating project to first start off with
[3048.06 → 3054.54] um maybe go to Jekyll go to Jekyll find an issue that you care about um and find an issue that
[3054.54 → 3058.38] you care about or that you think might be a relatively quick fix um even if you don't know the
[3058.38 → 3064.42] code doesn't matter whether you've looked at the code or not see that then clone down the repo
[3064.42 → 3069.04] and look through the code a little bit try to familiarize yourself with how this particular product
[3069.04 → 3076.32] does what it does um once you've done that um then try to pinpoint exactly where the issue
[3076.32 → 3081.88] is happening um and or at least where the issue might be occurring um change that submit
[3081.88 → 3088.76] your pull request um as best as possible add tests you know do sort of do your dues as it were or
[3088.76 → 3096.40] um and in order to see that that would be merged um and submit an issue um or submit a pull request
[3096.40 → 3101.70] for that um if that's sometimes even that is too much um you know to pick an issue that you
[3101.70 → 3108.52] might be able to handle and um change it up or and you know fix it so maybe what you should do
[3108.52 → 3114.20] instead is found an issue that you're that you think might be um easy enough to do look through the code
[3114.20 → 3119.70] a little bit um and just write a comment and say like hey um I'm interested you know I'd love to help
[3119.70 → 3126.22] fix this um I'm not really sure where to start um maybe here or here um and sort of
[3126.22 → 3131.28] indicate that you're thinking about it and that you'd love to help um I'm I can, I write way more
[3131.28 → 3137.28] comments that i than i you know than commits that I write um so I'm happy to help someone through
[3137.28 → 3142.38] through that process um i love to see newcomers to Jekyll it's the best thing in the world
[3142.38 → 3148.48] um to see people who have never um submitted a pull request or who made their GitHub profile yesterday
[3148.48 → 3154.98] too only to read an issue or to submit a pull request so for people to you know find that
[3154.98 → 3158.56] repository that or that project that you're interested in find an issue that you think you
[3158.56 → 3163.02] might be able to handle write a comment or just fix it um and submit a pull request if the pull
[3163.02 → 3167.36] request isn't the way that they want them to want to handle it uh the maintainers will say this
[3167.36 → 3171.82] isn't really how we want to handle it but here's how we would prefer um, and then you can implement
[3171.82 → 3177.52] that um switch and switch things around so um it's its more a matter of like just throwing
[3177.52 → 3186.20] yourself into the process and at every turn offering your help and the time let's pause the
[3186.20 → 3189.98] show for just a minute give a shout-out to our sponsor top towel now we've been working with top
[3189.98 → 3194.80] towel for about a year now almost a year now, and we thought it would make sense to circle back
[3194.80 → 3201.34] and talk to some of our listeners who have applied to top towel and have been accepted because only about
[3201.34 → 3206.22] two to three percent of the engineers who apply make it past their strict elite engineering process
[3206.22 → 3210.46] and Daniel Luzon a long-time listener and fan of the changelog
[3210.46 → 3217.56] is now living the dream he's an elite engineer top towel and I say living the dream because he's now
[3217.56 → 3223.64] able to have 100 control of the types of projects and technologies he's working on as well as the
[3223.64 → 3229.78] rate he wants to charge Daniel earns 100 of his income as a top towel engineer, and he wanted me to
[3229.78 → 3235.32] pass on his seal of approval of the top experience for those of you out there who are freelancing
[3235.32 → 3239.40] or like to test out freelancing you've got to check out top towel if you think you have what
[3239.40 → 3246.14] it takes head to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to get
[3246.14 → 3252.50] started tell them the changelog sent you I know a lot of the times when folks come on the show when
[3252.50 → 3257.74] we ask them which we'll ask you here in a bit like the call to arms is usually just help us triage
[3257.74 → 3264.04] issues especially a lot of high traffic projects with issues that you know have just lots it's you know
[3264.04 → 3268.56] sometimes it's just can you comment back to somebody can you just help me you know keep
[3268.56 → 3272.74] the heartbeat alive so that they don't think we're a bunch of jerks because we're busy writing code or
[3272.74 → 3277.60] busy with day jobs and this is like you in your spare time or your free time so you say you know
[3277.60 → 3282.98] so it's like it's kind of like that and then even I like what you said too about um not just saying hey
[3282.98 → 3288.30] how can I help it's I've got an idea about this particular problem I've got a couple ideas on how I can
[3288.30 → 3293.86] solve it or what I think might work can you give me some guidance because they'll respond easier to
[3293.86 → 3300.66] to at least you know some legwork versus just hey I'm here to help what can I do right pick up a broom
[3300.66 → 3312.58] you know exactly, exactly so lets um let's talk um let's talk about uh your involvement not only with
[3312.58 → 3317.76] Jekyll but then octopuses this is like uh we've gotten through this pretty much you know this whole show
[3317.76 → 3322.24] without really mentioning the relationship between these two and I don't want to do it any ill justice
[3322.24 → 3326.70] because I haven't kind of riffed with brand much lately about the project and where it's going but I know
[3326.70 → 3332.38] you're involved in both now can you kind of give a know the listeners kind of mention of how
[3332.38 → 3340.24] these two projects align and where you see them fitting so octopuses at the moment um in its current form
[3340.24 → 3347.62] in Mathis slash octopuses is sort of a framework around Jekyll um a series of rake tasks usually uh
[3347.62 → 3355.14] generally um that makes it easier to work with Jekyll um it comes with a built-in um classic theme
[3355.14 → 3361.26] that allows you to you just go rake install, and it installs this theme which is beautiful um I'm sure
[3361.26 → 3368.90] you've seen it on a lot of sites um, and it's the idea of octopuses is really to make it as easy
[3368.90 → 3374.02] as possible to get started blogging with Jekyll um when you run gem install Jekyll you have nothing
[3374.02 → 3382.10] available to you um you have now um since 1.0 I think or maybe 1.2 um you have Jekyll new and Jekyll
[3382.10 → 3387.36] new, and then you give it a path will install some you know very basic very, very run-of-the-mill um
[3387.36 → 3393.84] or you know bare-bones skeleton sort of site um but if you're is you're looking for like if you're
[3393.84 → 3398.98] some Erlang programmer or something and you just you don't have the time to set up an UI you don't
[3398.98 → 3404.90] want to write any HTML you just want to write what like write a blog post about something um then
[3404.90 → 3412.04] all that you have to do is clone down the repo run rake install run rake new posts and then give it a
[3412.04 → 3418.54] title and then boom you're off um, and it's the coolest thing um it handles new posts new pages
[3418.54 → 3426.44] deployments um previewing generation all of that stuff um one of the key points as well is that it
[3426.44 → 3432.16] it has this one task called rake isolate and one of the points that you mentioned earlier
[3432.16 → 3439.00] about Jekyll um is or I guess that we talked about at uh briefly um was this idea of incremental
[3439.00 → 3445.00] regeneration right now Jekyll just says I'm gonna when you run Jekyll generate or Jekyll build rather
[3445.00 → 3449.96] it just takes your whole site and rebuilds it um and that's not that efficient um especially if
[3449.96 → 3458.28] it's the same in 98 of the files so um if you have a massive site maybe of like 1200 posts or something
[3458.28 → 3463.80] you've been writing for a long time um I know Matt gemmed uses octopuses, and he has you know I think
[3463.80 → 3468.08] close to a thousand posts, or he did you know a couple of months ago um I'm sure he has over a thousand
[3468.08 → 3474.00] posts now um he's a great writer, but it just took so long for those posts for that site to regenerate
[3474.00 → 3479.46] that he said you know I can't do this so um octopuses gives him the tool called rake isolate which gets
[3479.46 → 3486.18] rid of all the posts except for the one that he's working on and basically just regenerates that one
[3486.18 → 3492.22] um the entire site but just with that one post so it removes the 999 other posts that he doesn't
[3492.22 → 3497.36] need to be looking at because he's not working on it right now um and then you um you run rake
[3497.36 → 3502.00] integrate, and it puts all the posts back, and then you run rake gen deploy, and he deploys a whole new
[3502.00 → 3506.34] thing once it's once it's done so is that using git magic to do that or is that how's that working
[3506.34 → 3512.70] rake isolate um basically just takes it takes all the posts except for the one that you're working on
[3512.70 → 3519.54] moves it into a separate directory um that Jekyll won't look at and then runs Jekyll build or Jekyll
[3519.54 → 3523.68] served depending on what you're doing so it all that it does is it just moves the files
[3523.68 → 3528.38] um and then moves it back when you run rake integrate right it's its it's an amazing
[3528.38 → 3534.64] idea um, and it's such it's so you know dead simple that it's surprising that no one else
[3534.64 → 3540.26] has done it, but that's sort of a unique piece to octopuses so octopuses is sort of this framework
[3540.26 → 3544.92] that makes blogging with Jekyll or writing sites with Jekyll as easy as possible and gives you the
[3544.92 → 3553.44] the UI or the uh the site um uh theme and all this stuff to work with immediately did the projects
[3553.44 → 3560.66] so it's its almost um even still now even after hearing that it's still hard to really see
[3560.66 → 3567.32] where they know where they separate I understand that it's kind of built on top of
[3567.32 → 3571.88] Jekyll but is it a point that they'll ever merge they'll ever share the same functionality
[3571.88 → 3577.22] or essentially tackle the same kinds of problems or is that the reason why you're involved in both
[3577.22 → 3582.44] projects kind of help keep them in parallel and keep them kind of working together well
[3582.44 → 3588.38] I'm definitely I'm definitely involved with both um in order to make sure that they're going along
[3588.38 → 3593.82] parallel in parallel um I'm way more involved in Jekyll just because Jekyll has no I mean Matt's
[3593.82 → 3600.32] working on it as well but Matt's um Matt's really busy so um I'm the one that's sort of taking care of
[3600.32 → 3606.04] of the immediate day-to-day sort of stuff with Jekyll um and because no one else is doing that I'm sort
[3606.04 → 3611.32] of taking more of a back seat or more of an advisory role I guess um I look over pull requests that
[3611.32 → 3619.62] that Brandon puts up on octopuses repos um and helping with problems as needed um but in terms
[3619.62 → 3625.80] of the future there's definitely the chance that they would merge um the octopuses as we know
[3625.80 → 3631.98] it today would not be the octopuses of tomorrow in any sense um Brandon's doing amazing work um on
[3631.98 → 3637.98] the octopuses organization on GitHub, and you can take a look at um where he's taking octopuses and
[3637.98 → 3642.96] splitting it off into a gem and this gem is just about functionality it's just about sort of
[3642.96 → 3650.06] extending the basic Jekyll generation stuff into um generating new posts based on like era templates
[3650.06 → 3655.80] that sort of thing um, and he also created something which I'm really excited about called octopuses inc
[3655.80 → 3662.92] um and octopuses inc is an extension to Jekyll that allows you to write isolated themes
[3662.92 → 3668.44] so I have a gem for example called I don't know parker's site or parker's theme or something
[3668.44 → 3674.22] and I can publish that on ruby gems, and you can say gem install parker's site or parker's theme or
[3674.22 → 3679.68] whatever and use, and it uses octopuses inc such that when Jekyll says all right I'm going to go
[3679.68 → 3686.06] build this site um it uses the CSS the JavaScript that I've written um, and it's its all separate from
[3686.06 → 3692.64] my own content files so what octopuses inc has done is basically taken the concept of WordPress themes
[3692.64 → 3698.56] where the theme and the content are completely separate um and applied that to static site
[3698.56 → 3703.98] generation as Jekyll knows it so I'm sort of I'm sort of there to make sure that everything's
[3703.98 → 3708.62] going along at the same time and to help with like the Jekyll 2.0 major bump for example that's a
[3708.62 → 3712.24] fantastic teaser for an upcoming conversation I'm sure we'll have with Brandon I know that
[3712.24 → 3718.56] I mean anytime we ever mention and I try to get Brandon to share as much as he can but I know he's its
[3718.56 → 3723.26] he's been so close to 3.0 for a while now and I know that a lot of the listeners and a lot of the
[3723.26 → 3729.24] readers of our weekly email and the blog and anytime we publish any sort of teaser of the upcoming
[3729.24 → 3734.06] octopuses 3.0 they're always like all over it you know everybody's like waiting with bated breath kind
[3734.06 → 3738.84] of so to speak so I'm sure that that was a perfect teaser for to tee it up for Brandon when he comes on
[3738.84 → 3745.58] the on the show um I guess let's go ahead and tail off the call than I know there's probably
[3745.58 → 3750.34] I know you got things you got to do, and we could talk probably for days but because you do a lot of
[3750.34 → 3758.06] cool stuff but let's lets um let's talk about the future of Jekyll let's tail into that and I think
[3758.06 → 3762.98] you kind of know where I'm going with it but where is Jekyll going how does it align with GitHub pages how
[3762.98 → 3769.50] does it align with GitHub uh GitHub pages API what can you tell us about uh not just Jekyll 2.0 which
[3769.50 → 3775.48] came out early this month but the future and beyond that's a really awesome question um the
[3775.48 → 3783.04] future of Jekyll is the simplest but also simultaneously most powerful static site generator
[3783.04 → 3792.94] that you can find um for anyone um isolating it from um the expectation that
[3792.94 → 3800.56] you must know ruby is paramount to that objective um the Jekyll of tomorrow is a Jekyll that
[3800.56 → 3808.20] is easy to install um is really easy to use um doesn't hopefully have as few bugs as possible
[3808.20 → 3815.50] if none or if not none rather um and does the really amazing things like incremental regeneration
[3815.50 → 3825.08] and has themes um the way that octopuses inc act price inc um displays them um and in order to get
[3825.08 → 3831.72] there we just need a lot more manpower um we just need people who are interested in taking a stake
[3831.72 → 3837.32] in Jekyll and saying this is a really cool project um let's make it what I want it to be um and when
[3837.32 → 3842.54] they hit a pain point to say yeah I could write a plug-in for this that monkey patches Jekyll to the
[3842.54 → 3847.86] you know how I want it but why don't I take that change and contribute it upstream and see if
[3847.86 → 3854.78] they're interested um and to sort of have that constant conversation with how am I using Jekyll
[3854.78 → 3860.82] and how is Jekyll right now um is sort of what's gonna what's going to push Jekyll forward that might uh
[3860.82 → 3865.48] that might lead us right into the call to arms I guess for Jekyll because one of the things we
[3865.48 → 3871.54] ask on this show is some decent questions at the end that's our common questions I guess um but we
[3871.54 → 3875.40] always ask you know what's the call to arms how can the community step up and help out so maybe you
[3875.40 → 3881.20] kind of mentioned it, but maybe you can kind of go a little deeper yeah so the way that we would
[3881.20 → 3886.26] love for you to get involved is to be involved in the conversation the issues there's an IRC channel
[3886.26 → 3895.22] um pound Jekyll there is um there's so much available um there's also a Jekyll dash help repo um so if
[3895.22 → 3900.54] you're if you're is you find that you have an extra even 10 minutes a day to watch that repo and
[3900.54 → 3905.76] answer questions to help with the ecosystem or the users who are struggling with this or
[3905.76 → 3911.48] you know hey I installed Jekyll but I can't seem to get this to work can you help me yeah sure let me
[3911.48 → 3916.10] just take a quick look at your repo most Jekyll problems are diagnosable you know in five minutes
[3916.10 → 3923.68] um unless it's some crazy issue with you know your gem environment or something so um to be
[3923.68 → 3930.08] involved and to do what you can to um either contribute code um or contribute ideas just open
[3930.08 → 3934.14] an issue that's like hey this is a really cool idea that I had when I was just writing my site
[3934.14 → 3939.60] what do you think about it um, and then we can discuss it um to you know involve your friends
[3939.60 → 3945.24] maybe uh if you have an if you have a pal who's also using Jekyll or a colleague to have them you know
[3945.24 → 3949.68] get a GitHub profile they don't already and contribute their ideas um to be part of the
[3949.68 → 3954.48] conversation um there's obviously no way that you're you're going to be involved if you aren't
[3954.48 → 3959.30] a part if you aren't a part of it but um it's relatively easy to just watch the repo I promise
[3959.30 → 3967.84] like maybe 12 to 15 notifications a day I try to stay uh busy but not too overwhelming um
[3967.84 → 3975.54] so you know just sort of contribute where you want to where you can um of course triaging issues is
[3975.54 → 3980.70] super helpful but I handle every issue that comes through um so you're pretty active I was always
[3980.70 → 3986.48] when I was just kind of prepping for this conversation I was like wow you are on the
[3986.48 → 3992.38] ball you know and not just like hey thanks you know like uh maybe a text expander or something like
[3992.38 → 3996.90] that or some sort of you know snippet that you kind of put in it's like you know you really look and
[3996.90 → 4002.50] you re-quote and you ask for clarification you kind of give more feedback you're you know i really
[4002.50 → 4006.52] wonder when you say you know you do this in your free time like you must have a lot of free time so
[4006.52 → 4012.56] are you really going to school are you two people that kind of thing I've definitely slacked off on my
[4012.56 → 4017.52] on my classwork enough uh to make sure that the amount of time that I have on GitHub is
[4017.52 → 4024.30] substantial so I will uh apologize to my professors on behalf of my time on Jekyll um but that I mean it's
[4024.30 → 4030.06] taken a long time to get there but um I find that if you're kind and if you're is you're
[4030.06 → 4034.60] you give constructive feedback then people will be kind in return and that's there's so much
[4034.60 → 4040.06] animosity in the open source uh community that to yell at people is not useful
[4040.06 → 4044.72] yeah um, and it's its sort of counterproductive to the idea of let's build something awesome together
[4044.72 → 4049.32] we've we've talked about that a little bit on the show before just kind of like the not so nice
[4049.32 → 4055.30] responses from people and just the attitudes because it is mean we talked about burnout on the show before
[4055.30 → 4061.82] with lee hamlet and Cristiano and some other projects that have come on and people who uh lead
[4061.82 → 4067.06] those projects have expressed just burnout, and you can't always uh help your attitude sometimes you
[4067.06 → 4072.18] know let's maybe talk to you in two years and see if you feel the same way um but I mean it does
[4072.18 → 4077.82] happen um regarding the future of Jekyll there's one question i I do have as a dovetail off of what you
[4077.82 → 4083.86] said before you said um you know you need more people you need more manpower so to say um
[4083.86 → 4089.00] how does that how does that play into GitHub that's what I keep coming back to because
[4089.00 → 4094.90] it's obviously a part of pages they obviously have the money to employ people are they a part
[4094.90 → 4099.40] of these conversations to make sure that Jekyll thrives and Jekyll grows and Jekyll is awesome
[4099.40 → 4108.48] they aren't as much I will say um they're at the moment it's sort of an uh in maintenance mode pages is
[4108.48 → 4113.36] I'm I'm certainly building new features um and making it you know as great as I can
[4113.36 → 4120.82] um but there's they aren't building as many new features into pages certainly um and what
[4120.82 → 4126.92] they what they primarily want is to see pages be something that makes you know documentation
[4126.92 → 4133.58] really, really great software documentation so if i'm bootstrap how can we make sure that
[4133.58 → 4140.98] Jekyll and that pages are well suited to your um to your needs for that particular project
[4140.98 → 4147.28] so to make sure that Jekyll is as general as possible is sort of what um and not too complicated
[4147.28 → 4152.72] of course um is sort of what Ben's been doing as a part of sort of as an acting entity of GitHub
[4152.72 → 4158.34] and also in his own uh wishes he'd like to see something that's simple and easy to use
[4158.34 → 4165.26] rather than something that's super complicated um or super specific so they aren't they aren't that
[4165.26 → 4171.12] heavily uh involved in Jekyll, but they've certainly supported me in huge ways um whether
[4171.12 → 4178.88] it's just like random boxes of goodies um or you know hey um we want this feature added to Jekyll can
[4178.88 → 4187.76] you write it for us, we'll pay you well um I guess the last question is a fun one that I think you
[4187.76 → 4194.00] may have touched on at least one hero right uh but who do your you know you can name one you can name a
[4194.00 → 4198.40] few it's we don't really have any sort of roles here but uh if you had to name some programming
[4198.40 → 4206.56] heroes who would they be um I definitely have a bunch um, and they've i I'm I tend to take to heroes
[4206.56 → 4212.62] pretty quickly um because they're someone that I can look up to and it sort of gives me a goal
[4212.62 → 4219.18] um to set so I'm starting off in middle school when I was learning basic um the guy's name was Dan
[4219.18 → 4227.50] Lavoie um later it was nick Rao um who now works at mod cloth as a software engineer um really brilliant
[4227.50 → 4232.10] guy who he was the one who originally taught me how to use rails um and got me interested in ruby
[4232.10 → 4238.00] so he's the reason that i I know ruby at all um leaf Walsh was an um an acquaintance in high school
[4238.00 → 4242.90] who is just ridiculously brilliant um he got a joint degree at stony brook SUNY stony brook
[4242.90 → 4248.60] um in like theoretical mathematics and computer science um and then of course they're the
[4248.60 → 4256.10] know they're the I guess more general or more normal uh answers of um people like tom um and
[4256.10 → 4261.02] Chris wans troth who wrote um and PJ who wrote GitHub initially and just sort of wrote it in their
[4261.02 → 4267.50] spare time um people like Ben who are amazing product people but also or sort of um product
[4267.50 → 4274.40] managers and can can develop vision um in addition to writing amazing code um and so and people
[4274.40 → 4281.92] from my time at sex wunderkinder as well um, um Hans Heidelberg um uh Ryan device um uh
[4281.92 → 4288.56] thus or Joseph bach um he's a great guy and chad fowler as well um they're all like just amazing
[4288.56 → 4296.70] people that I've I have looked up to um and have tried to try to be more like yeah several uh in
[4296.70 → 4303.62] there I definitely share similar remarks but uh this has um this has been well I guess probably
[4303.62 → 4307.40] one of our longer shows in the last several shows I think we just kind of got on some riffs there and
[4307.40 → 4313.24] I want to pull you off and I'm glad that you were uh such a good trooper for the show parker so um
[4313.24 → 4317.16] thanks so much for having me I know we wanted to get you on the show for a while and I'm just you
[4317.16 → 4323.72] know very excited about what you're doing so keep up the great work um however we can be of a support
[4323.72 → 4330.30] to you and to help uh to help you and Matt kind of keep this project you know at the forefront and
[4330.30 → 4335.90] just knowing that it is the next generation and the way to be when it comes to uh static
[4335.90 → 4340.14] site generation and the future of it, and you know octopuses we hope to have brain on the show
[4340.14 → 4345.12] in the near future about that so I want to just you know you got our support however we can
[4345.12 → 4351.68] give it so um great thank you so much uh same to you as we uh to close out the show I want to give
[4351.68 → 4358.80] another shout out to our awesome sponsors Rackspace uh snap and top towel uh for supporting the show
[4358.80 → 4364.54] they do an awesome job to help make sure we stay around as part of just helping uh parker do his
[4364.54 → 4370.38] awesome work and help him stay around so uh I also want to plug our new partner to DIV shot uh who's
[4370.38 → 4376.66] helping pave the way for really awesome static web hosting for developers uh, and they're hosting Jekyll too
[4376.66 → 4380.36] so we'll give you more information about that for the members and if you're not a member yet you
[4380.36 → 4384.82] should check it out but uh that's it for this week we'll be back next week and until then
[4384.82 → 4388.48] uh parker and I will say goodbye so bye-bye
[4388.48 → 4390.48] you
[4410.36 → 4420.48] you
[4420.48 → 4421.48] you
[4421.48 → 4423.48] you
[4423.48 → 4427.48] you
[4427.48 → 4429.48] you
