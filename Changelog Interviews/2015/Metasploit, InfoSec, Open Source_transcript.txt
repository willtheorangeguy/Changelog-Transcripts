[0.00 --> 16.20]  welcome back everyone this is the changelog and i'm your host adam stachowiak this is episode 174
[16.20 --> 22.74]  talking metasploit today with trevor rosin and james egypt lee these are the guys behind
[22.74 --> 28.32]  metasploit which is the world's most used penetration testing software great show today
[28.32 --> 38.42]  we had four awesome sponsors code ship top tile harvest and trans loaded our first sponsor is
[38.42 --> 43.94]  code ship code ship launched a brand new feature called organizations a few months back everyone's
[43.94 --> 49.48]  been loving it now you can create teams you can set permissions for your specific team members and
[49.48 --> 55.00]  you can improve collaboration in your continuous delivery workflows you can maintain your centralized
[55.00 --> 60.52]  control over your entire organization's projects and teams with this new feature it's super awesome
[60.52 --> 67.50]  and you can save 20 off any premium plan you choose for three months by using our code the changelog
[67.50 --> 75.46]  podcast again that code is the changelog podcast 20 off any plan you choose for three months head to
[75.46 --> 80.90]  codeship.com slash the changelog to get started and one more thing i want to tell you about sean
[80.90 --> 87.00]  devine is doing an api workshop called api first training and guess what he's going to use code
[87.00 --> 92.68]  ship as a demo tool the url to learn more about that api training is in our show notes so check those out
[92.68 --> 94.32]  but now on to the show
[94.32 --> 109.88]  welcome back everyone jared here today i'm joined by two interesting guys this is trevor rosen
[109.88 --> 118.10]  and james egypt lee two of the people behind the metasploit project which is the world's most
[118.10 --> 123.76]  used penetration penetration testing software uh trevor egypt welcome to the show
[123.76 --> 129.76]  thanks thanks for having us so we're here to talk metasploit we're here to talk infosec we're here
[129.76 --> 136.28]  to talk open source lots of interesting topics uh out there but first let's let the audience get to
[136.28 --> 142.64]  know you guys a little bit and trevor i'll start with you because we met at gopher con which is a
[142.64 --> 148.72]  bit of a theme lately i feel like that conference was quite a boon to our to our podcast because we
[148.72 --> 153.64]  lined up a lot of new friends and a lot of guests for the show um yeah i can imagine
[153.64 --> 156.92]  it was it was a great con it was one of my one of my all-time favorite cons that i went to
[156.92 --> 164.12]  um so my name is trevor rosen i work um at rapid seven on metasploit as the leader of the architecture
[164.12 --> 170.52]  team which is um a small team kind of mostly software oriented people who work all different
[170.52 --> 175.80]  areas of the metasploit framework and the metasploit commercial applications um so metasploit
[175.80 --> 179.40]  framework is this uh sort of famous thing in the information security world
[179.40 --> 184.28]  um it's been around for a little over 10 years and it exists basically to help you
[184.92 --> 189.72]  um help penetration testers which is like kind of good guy hackers good person hackers i should say
[189.72 --> 196.20]  um white hats um help determine uh what an organization's level of exposure is to security
[196.20 --> 203.32]  threats and um so i get to work in all different areas of of our stacks on all sorts of fun open
[203.32 --> 209.96]  source stuff mostly ruby software and quite a bit of stuff in the rails ecosystem um and i'm not
[209.96 --> 215.00]  really a full-time security person in that i don't do security research really but i definitely have a
[215.00 --> 219.96]  lot of fun working on open source and i'm a big fan of what open source can be for the for the
[219.96 --> 225.08]  security world i feel like it's really vital so did you were you always in security side of things
[225.08 --> 229.72]  or did you start off as a programmer what's kind of your background yeah background is mostly software
[229.72 --> 233.80]  um i've done a bunch of different startups and things i always kind of had a soft spot for
[233.80 --> 238.28]  security though i was i was the guy on the team that was like you know in mapping everything on our
[238.28 --> 243.72]  production boxes and um finding open ports and you know hiring ops guys about that or or you know
[243.72 --> 249.80]  trying to hack my my dev environment yeah for sure yeah and then i mean back in the day as a kid um
[249.80 --> 256.44]  i may or may not have built some hardware that wasn't 100 legal um but uh yeah i these days mostly
[256.44 --> 261.48]  sort of i would say i fall onto the um the maker side of things and i mean by that not like make
[261.48 --> 267.96]  magazine but sort of like um security the security software world kind of has people who are interested
[267.96 --> 272.92]  in sort of breaking stuff and hacking it and figuring out the how to make it do something crazy or or
[272.92 --> 278.20]  weird um and then people who are much more interested in sort of just making good software so um that's
[278.20 --> 281.88]  really where i i guess i would put myself as kind of more on the maker end of the spectrum that's an
[281.88 --> 286.28]  interesting way to put it because i i came to a similar conclusion as i was telling you
[286.28 --> 290.76]  in the pre-call i do have a bit of a security background studied information assurance as a
[290.76 --> 297.80]  concentration um in college and was doing penetration testing and and mapping stuff like crazy which was
[297.80 --> 305.16]  like one of my favorite things to do um but i too kind of i found myself after that deciding i'd
[305.16 --> 310.76]  rather create things than tear them down i also wasn't that good at it i don't have that like mindset i'm
[310.76 --> 314.84]  sure you guys are well aware in egypt maybe you're one of these kind of people where like you can just
[314.84 --> 320.60]  find a way to break everything i was like okay at it but i didn't have like that that intuition that
[320.60 --> 326.20]  some folks have um and i do like creating so i can kind of relate with you a little bit there let's
[326.20 --> 334.28]  move on to james who i've been told not to call that i've been called his name's egypt uh but james egypt
[334.28 --> 342.20]  lee um want to go ahead and introduce yourself to the crowd yeah um i'm egypt pretty much everywhere
[342.20 --> 351.24]  um and i'm egypt on twitter etc um i'm the metasploit community manager here at rapid7
[351.88 --> 357.56]  um and that means that i'm writing a lot more emails than code these days oh man at least for
[357.56 --> 365.40]  the last couple of months um but i'm i'm sort of involved in in open source contributions and getting
[365.40 --> 372.52]  people interested in the project um as well as uh fixing the the old bugs in in code that that no one
[372.52 --> 380.44]  else has looked at in years um so i started with the project in uh roughly 2006 i started using it
[380.44 --> 387.00]  professionally um as well as the thing i was writing my exploits in working as a security researcher
[387.00 --> 391.80]  um and i found bugs and problems and things that just didn't work the way i wanted them to
[392.52 --> 400.44]  so i started submitting patches um and around 2008 um hdmore the founder of the project decided
[400.44 --> 404.44]  that it was easier to give me commit access than to keep taking all my patches all the time
[405.16 --> 410.04]  so in 2008 i got commit access to the then subversion repository
[410.04 --> 415.80]  um and broke master with my first commit oh you are a breaker then yes
[418.36 --> 424.44]  so what happened what happened there tell us about that uh well i with every everything i
[424.44 --> 430.28]  committed for the first couple of months um you know i would miss some edge case and it would make
[430.28 --> 437.08]  the the main interface not boot up or you know something stupid like that well the framework was not
[437.08 --> 441.64]  overburdened with you know regression tests back at that time either so right it's hard to give you
[441.64 --> 448.84]  too much blame the the account of the count of regression tests at that point was zero um and remained so
[448.84 --> 458.44]  for quite a bit longer um regression testing has been a uh an ongoing issue for us um but yeah i spent a lot
[458.44 --> 466.84]  of time um fixing bugs just to make it um possible to do some of the evil things that i was trying to do at
[466.84 --> 474.12]  the time uh and that got me in the door with the project uh and then in 2009 when the acquisition
[474.12 --> 483.48]  came about i was basically the first hire uh onto the new the newly minted metasploit team um so i wrote
[483.48 --> 490.60]  most of the um or a lot of at least the the back-end code for the original metasploit commercial product
[490.60 --> 497.48]  um i spent a lot of time there working on the commercial edition as well as the open source
[497.48 --> 503.80]  stuff um and in the time that i've been working at rapid seven something north of 80 percent of all
[503.80 --> 511.56]  my code has been open source so that's super uh super helpful um it really adds to the job satisfaction
[511.56 --> 519.32]  to see my code is going out open source um and it also allows me to interact with a very diverse
[519.32 --> 527.16]  group of of hackers putting together exploit modules and and you know kicking sandcastles
[527.16 --> 532.28]  and licking cupcakes as we do in the metasploit world say that again kicking sandcastles and licking
[532.28 --> 536.92]  cupcakes yeah because that's what you do when you break into a network right you're not in there
[536.92 --> 542.20]  saying you know everything is sunshine and rainbows you're you're you're ruining someone's day and you
[542.20 --> 547.56]  have to do it you have to do it nicely so it's all about imagine a tray of cupcakes and somebody runs
[547.56 --> 552.20]  over and licks all of them before anyone gets to eat them that that's what it is to lick cupcakes
[552.20 --> 559.96]  that's that is incredibly rude but nice for you because you get you taste the cupcakes i guess
[559.96 --> 565.32]  that's right uh it is kind of fun right when you find your way in well let's let's not uh bury the
[565.32 --> 574.52]  lead here let's talk about this name egypt ah yes it originated as a um a nickname in college
[574.52 --> 584.76]  based on my appearance so do you look egyptian i guess so no you don't uh pyramid pyramidal uh
[586.36 --> 589.48]  i guess yeah i'm not really sure i don't know i had a goatee at the time
[590.68 --> 593.16]  so you look a little bit like an egyptian pharaoh or something
[593.96 --> 598.84]  i suppose so friends started calling you egypt and it just stuck and it just stuck
[598.84 --> 605.72]  trevor where's your awesome a handle oh gosh yeah i don't know i don't really have one i don't
[605.72 --> 612.60]  have i don't have one either no i'm i'm burly scud on irc with two d's and always have been um points
[612.60 --> 616.76]  to anybody out there in the audience who knows what that's a reference to early scud yeah because i've had
[616.76 --> 621.32]  one person and all the times ever figured out but it's it's not super hard it's just kind of kind of
[621.32 --> 627.32]  obscure um but yeah i don't i don't have a super awesome handle um i spend i spend a lot of my time
[627.32 --> 633.08]  i've spent a lot of my time since i've been at rapid seven um kind of uh managing and wrangling cats
[633.08 --> 639.56]  and being involved in uh in the sort of the ongoing discussions about you know how we can
[639.56 --> 645.08]  do the next thing or whatever that kind of thing i'm sort of stumbled backwards into like um
[645.08 --> 650.20]  software as politics almost i guess you'd say so tell me a little about rapid seven as far as the
[650.20 --> 655.88]  company uh the culture kind of what it is that they do and then that maybe just intro the relationship
[655.88 --> 662.76]  to the metasploit uh framework sure um so rapid seven is a security company uh security software
[662.76 --> 670.20]  firm it's been around um since about 2000 2001 so um pretty long time um actually an unusually long
[670.20 --> 676.92]  time for for uh you know what was usually termed a startup to to go um from from its inception um
[676.92 --> 683.48]  through to the ipo that we had this past summer um but it's um a firm that had been um prior to
[683.48 --> 689.08]  metasploit working um in the vulnerability management space um you can think of a of a
[689.08 --> 694.36]  vulnerability scanner i guess and sort of security people in the audience might jump on me for this
[694.36 --> 699.16]  but kind of roughly analogous to like a a virus scanner for networks or something like in that
[699.16 --> 705.00]  like a virus scanner kind of scans your machine for a bunch of like known problems it has or sort of
[705.00 --> 710.52]  patterns of of activity that could be suspicious um a vulnerability scanner is going to scan like a lot of
[710.52 --> 715.80]  network endpoints a whole lot of machines on a network um and try to determine what kind of
[715.80 --> 721.24]  exposure exists there so that product is called nexpose and that's like a rapid seven sort of large
[721.24 --> 728.44]  long time product that we've had and um they're back whenever they decided and it predated my my time
[728.44 --> 734.28]  with the company to acquire the metasploit project um it was sort of along the lines of okay we understand
[734.28 --> 738.76]  a certain you know we have kind of half of the equation here in that we're um showing we're doing
[738.76 --> 743.40]  vulnerability management we're doing vulnerability scanning um and so that's that's defensive security
[743.40 --> 749.32]  right that's um figuring out what what your your problems are from a kind of like scanning the the
[749.32 --> 754.20]  the equipment you have perspective and then trying to patch it but then on the other side of that is
[754.20 --> 758.92]  like well what could you do what could a what could an attacker do what could a sufficiently empowered
[758.92 --> 766.76]  attacker do and um so metasploit has always existed to help empower um people who are attacking because
[766.76 --> 773.24]  they're they're being paid to um and it's you know paid by the company they're attacking hopefully um
[773.24 --> 778.04]  and so the idea was sort of we can make a commercial product um around that essential notion that
[778.04 --> 784.20]  offensive techno that offensive security um sort of stance and concept and it will be complementary to
[784.76 --> 791.00]  the the existing product that have um and metasploit is also a pretty big name um if you go to
[791.00 --> 796.60]  like insecure.org and you look at the the sec tools 100 you know top top 100 open source security tools
[797.16 --> 801.80]  metasploit um has for as long as i've known about metasploit which is uh since significant amount
[801.80 --> 806.92]  of time before i started rapid 7 so probably since about 06 or 07 metasploit was in like the top five
[806.92 --> 812.20]  or top ten um now i believe it's like number two or three on the list like right after like wireshark
[812.20 --> 817.32]  and in map or something right so it's regarded the framework the open source tool is a um a very
[817.32 --> 824.12]  essential piece of kit a very widely known widely used widely used thing so um rapid seven's kind of
[824.12 --> 831.56]  overall idea is that there's a lot of insight to be gained from um really approaching security as a
[831.56 --> 838.68]  matter of finding the right data finding the the right insights that you can um into into what the
[838.68 --> 843.88]  actual threats are because quite a bit of security tools just produce um incredible quantities of
[843.88 --> 848.68]  data but not a whole lot of actionable information about what you should do with that data yeah
[848.68 --> 856.76]  right so um you know our our um our leadership likes to say that that you know for a long time
[856.76 --> 861.00]  quite a bit of the security space is predicated on this idea of essentially kind of monetizing fear
[861.00 --> 866.28]  it's like hey here's a bunch of things to be terrified of okay what do i do about them uh yeah here's the
[866.28 --> 872.04]  big phone book sized pile figure it out right right but we want to we want to go beyond that that's that's
[872.04 --> 877.16]  really the the way that rapid seven wants to operate as we go beyond that to provide sort of
[877.16 --> 882.84]  much more in like much more in depth and immediately actionable kind of insight so um we have in
[882.84 --> 889.32]  addition to nexpos and to the metasploit commercial editions um we also have um this really interesting
[889.32 --> 894.52]  product called user insight and um user insight you can think of almost as sort of like an intrusion
[894.52 --> 900.60]  detection system for user behavior so instead of kind of saying like hey what what types of data are
[900.60 --> 905.64]  traversing my firewall on what ports etc etc you can kind of instead you can you can turn on his
[905.64 --> 910.92]  head and ask the question like what are users doing right now and is that okay and can you use
[910.92 --> 917.48]  heuristics to understand like hey today jared accessed 12 servers that he's never touched before
[918.04 --> 923.16]  you know um is that strange right and and a traditional intrusion detection system might not
[923.16 --> 927.48]  know about that because it might just be focusing on the perimeter like is you know art is some unauthorized
[927.48 --> 933.16]  person getting in or some particular high value data getting out um so user insight again it's that
[933.16 --> 937.88]  that idea of being able to sort of look at um security from a slightly different perspective and
[937.88 --> 942.76]  say you know can we can we change our perspective a little bit but dramatically increase the value of
[942.76 --> 948.20]  the insight that we're producing um so i guess that's kind of rapid seven in a nutshell i think you
[948.20 --> 953.16]  spawned a product you spawned a product idea um which i'll give you this one too for free so tell
[953.16 --> 958.84]  your friends are rapid seven like no big deal they can thank me later it's a scanner but it just scans
[958.84 --> 966.12]  your office or the scans every monitor to see if anybody has written their password down on a
[966.12 --> 972.20]  yellow sticky note and then stuck it to their monitor what do you think about that that's real
[972.20 --> 976.44]  that's real user user interactions scan do you mind if i go ahead and just like start the patent
[976.44 --> 981.24]  application right now as long as you guys give me a shout out or all right you know one percent of
[981.24 --> 988.28]  your first billion something like that no big deal so you know honestly honestly i would prefer
[988.28 --> 993.48]  people write their password down somewhere and put it in their wallet rather than then uh leave it
[993.48 --> 999.64]  in passwords.xls on their desktop yep good point or just use one password not one password the
[999.64 --> 1005.08]  application but like literally a single password for you know everything that they do so nothing bad
[1005.08 --> 1010.84]  ever came of that yeah exactly on the other side of that coin you have uh companies enforcing
[1010.84 --> 1016.04]  ridiculously onerous password policies uh which require their users to subvert them on a regular
[1016.04 --> 1022.36]  basis and come up with all sorts of things right and those ridiculous password policies lead to like
[1022.36 --> 1028.92]  the top four uh passwords in every single organization are summer followed by the year
[1029.64 --> 1035.88]  winter followed by the year spring followed by the right fall followed by the year they are in the top
[1035.88 --> 1041.88]  10 on every organization so is there is there a future for us to just be rid of passwords altogether
[1041.88 --> 1049.48]  is there is there a light at the end of that tunnel uh as a industry or not i don't see it like i really
[1049.48 --> 1056.36]  want to but i don't see it um we've moved towards two-factor authentication or multi-factor authentication
[1056.36 --> 1065.32]  um but it's so spotty and the support for it is so spread out that most of the time as a pen tester
[1065.32 --> 1070.92]  you know you get around you walk all over the network you kick those sand castles and lick those cupcakes
[1071.64 --> 1077.08]  and at the end of it you go and give the report and they say oh well what'd you do about our two-factor
[1077.08 --> 1086.20]  off i didn't know you had it i'm sorry right hmm so before we get into metasploit uh the details that
[1086.20 --> 1092.20]  the history and all that let's talk about penetration testing as a thing um we've mentioned it a few
[1092.20 --> 1098.52]  times here um but maybe egypt could you give us kind of a general definition and maybe even like
[1098.52 --> 1103.08]  what is a security audit looks like from a company if somebody hires a company like rapid seven there's
[1103.08 --> 1107.32]  a lot of these firms out there that will do it for you what's the process what's it about and kind
[1107.32 --> 1113.56]  of what are the results right so i don't have a lot of insight into the like sales side of it like
[1113.56 --> 1118.60]  who you call and talk to but i can tell you from the penetration tester side um you know
[1119.40 --> 1126.28]  a penetration tester is given uh someone to talk to as their point of contact and they usually have
[1126.28 --> 1131.80]  a list of ip addresses that are in scope and don't touch anything outside of those ip addresses
[1132.44 --> 1139.56]  um and sometimes though the scope will be really restrictive and say you know you're only allowed to look at
[1139.56 --> 1146.12]  this web app and you're only allowed to look for cross-site scripting uh you're not allowed to look
[1146.12 --> 1151.08]  for sql injection and that sort of thing and that gets really limiting and you end up with a report
[1151.08 --> 1156.84]  that's not very useful uh but sometimes you get a broader scope um you're allowed to look for more
[1156.84 --> 1163.00]  things you're allowed to take more actions uh and hopefully those are on um not necessarily
[1163.00 --> 1168.28]  production networks but something that like if it falls over you don't lose every customer's data
[1168.28 --> 1176.36]  etc etc um but a lot of times uh a penetration test is is just a week or two weeks long which
[1176.36 --> 1182.76]  means a very compressed time scale for an attacker a real attacker is going to have months right and
[1182.76 --> 1186.92]  a penetration tester is going to have a week or maybe two weeks and one of those days is going to
[1186.92 --> 1195.24]  be for reporting so they really only have four days um and you start out sometimes it's acceptable to
[1195.24 --> 1202.36]  scan beforehand and that saves a lot of time so as a penetration tester because of this compressed
[1202.36 --> 1207.00]  time scale you need to find stuff as quickly as possible and identify it as quickly as possible
[1207.00 --> 1212.44]  because you're looking at a lot of data so if you have a thousand ip addresses that you need to check out
[1213.40 --> 1219.08]  you want to scan those as quickly as possible and it's going to be super noisy and so for example if
[1219.08 --> 1223.64]  there's a firewall in the way or an ips in the way that says oh this is a port scan and then blocks
[1223.64 --> 1229.24]  your access now suddenly the scan is basically invalid so that happens pretty frequently
[1231.40 --> 1239.00]  and assuming that those roadblocks don't come up you do your scan you find out what's available
[1239.00 --> 1243.80]  usually there's a whole bunch of static html there's a whole bunch of web applications and
[1243.80 --> 1252.36]  not a whole lot else on the outside um occasionally you'll find the you know the golden ftp server with
[1252.36 --> 1258.28]  uh all of the company's financials on it open anonymously to the public but that doesn't happen
[1258.28 --> 1265.08]  terribly often um i did find a domain controller on the public internet once so that was fun
[1266.12 --> 1275.16]  um but fortunately that doesn't happen frequently anymore um so then you do your you do your external
[1275.16 --> 1281.72]  scans you find all the things um if if there are a bunch of web applications out there you spend some
[1281.72 --> 1288.36]  time fuzzing input you look at a thing called burp suite which allows you to muck around with with
[1288.36 --> 1294.52]  http headers and values uh it makes it really easy to fuzz some stuff and to examine responses um
[1295.64 --> 1300.68]  there are a number of other tools in that same vein but burp suite is kind of the de facto standard for
[1300.68 --> 1307.00]  screwing around with http when you say fuzz some stuff can you elaborate on that yeah uh basically just
[1307.00 --> 1313.80]  throwing uh values that might break an application um so in the case of if you're looking at a c
[1313.80 --> 1319.40]  application uh an application written in c you would be throwing large uh large strings because they
[1319.40 --> 1324.68]  might overflow a buffer in the case of a web application you might be throwing uh various
[1324.68 --> 1332.60]  kinds of quotes to to escape something out of a sql statement uh so those sorts of things just trying
[1332.60 --> 1338.52]  inputs that are probably bad given the application uh hoping for a crash or some aberrant behavior
[1339.88 --> 1348.52]  um and so once you once you get through that step um occasionally you'll end up with uh external
[1348.52 --> 1353.56]  access via something like uh a sql injection or a command injection on a web application
[1354.76 --> 1358.68]  and then you start the whole process over again and you scan the internal network
[1358.68 --> 1366.92]  uh a lot of of external uh engagements require that once you get inside all everything stops
[1366.92 --> 1371.24]  until you talk to your point of contact that's pretty common uh which sort of makes sense from
[1371.24 --> 1377.00]  the from the customer's perspective because you as as the person running the network you want to know
[1377.00 --> 1382.68]  when there's a big vulnerability that lets someone into the dmz or into the production environment
[1382.68 --> 1387.88]  you want to know that as soon as possible um and you also don't necessarily want a penetration tester
[1387.88 --> 1395.16]  uh running around rampant on your production uh internal network so a lot of times everything
[1395.16 --> 1401.48]  stops comes to a dead end right there um and you call up your point of contact and and tell them the bad
[1401.48 --> 1410.60]  news um there is also like social engineering campaigns um where you send out a bunch of emails and
[1410.60 --> 1417.80]  inevitably someone is going to run the executable um and that gets you usually corporate network access
[1417.80 --> 1423.32]  and again the thing starts all over again now as a penetration tester or as any attacker really
[1423.32 --> 1430.12]  you're looking to expand your influence so if i'm coming in from the outside i'm looking to gain access to
[1431.24 --> 1437.24]  either data through sql injection or possibly shell access through command injection or other sorts of
[1437.24 --> 1443.56]  things um and if i'm sending in a phishing email i'm looking to expand my influence instead of into the
[1443.56 --> 1448.28]  the dmz into the corporate network uh usually there's all sorts of information in there that's
[1448.28 --> 1454.28]  that's company sensitive that you really want to get a hold of um the crown jewels are always on
[1454.28 --> 1458.44]  somebody's desktop though or some file share that's available to everyone in the company
[1460.52 --> 1467.80]  most of the time you're not dealing with exploits yeah i'm when i i i'm sending when i'm talking to a
[1467.80 --> 1474.12]  web app on the external i'm creating my own exploits for the most part you know most of those things
[1474.12 --> 1479.08]  are custom apps as i was going to ask is if you are targeting specific you know endpoints on a
[1479.08 --> 1486.76]  network that are public facing they're usually web apps and are you just fuzzing those or are you
[1486.76 --> 1494.04]  actually you know inspecting the application and saying hmm i i think this might not this might not be
[1494.04 --> 1499.56]  checked or this could be injectable and like trying different things by hand or if you're only using
[1499.56 --> 1510.20]  these these tools sure both of both of those for sure um i mean in some cases like you can fuzz a few
[1510.20 --> 1514.76]  things and find a couple of interesting responses and say oh this is probably an injection and then
[1514.76 --> 1523.32]  you'll dive deeper manually i see um with other things like it at least when i first started doing
[1523.32 --> 1529.56]  penetration testing every login form was vulnerable to sql injection so the first thing you do is put
[1529.56 --> 1535.40]  tick or one equals one into the login form and you get admin so fortunately that's not nearly as common
[1535.40 --> 1539.40]  anymore and you know then what do you do just go you just go to lunch or something you're like well
[1539.40 --> 1545.56]  we're done for the day you know the point of contact and and you're done no from from that point
[1545.56 --> 1550.60]  you go in looking for credit cards and and social security numbers uh you want to lick all you want to
[1550.60 --> 1557.24]  lick all the cupcakes huh exactly so i mean one thought that comes to mind and maybe it's just
[1557.24 --> 1563.16]  because it's too expensive but if they're trying the point of this is to you know give us a reasonable
[1563.16 --> 1570.44]  idea of maybe not even how secure our our network is but how insecure it is i think you can you know you
[1570.44 --> 1574.92]  can guarantee an insecurity whereas you can't guarantee a security which is kind of the troublesome part of
[1574.92 --> 1582.60]  the business i think but um if they're trying to be as real world as possible you know a black box
[1582.60 --> 1588.52]  here's an outsider with a few ip addresses which is how you know people start why do they limit you to
[1588.52 --> 1593.48]  four days just because it costs too much to pay you to to keep hacking them for four months or or what
[1593.48 --> 1600.04]  yeah that's generally the thing cost is is is the deciding factor in a lot of those decisions
[1601.72 --> 1607.64]  i guess that makes sense well one tool that you use i'm sure is metasploit we're going to take a
[1607.64 --> 1612.12]  quick break here from one of our sponsors and then we're going to dig into all the details of
[1612.12 --> 1617.24]  metasploit what it is what it does and why it's useful and why it's so stinking popular we'll be right back
[1617.24 --> 1623.48]  you've heard me talk about top towel several times in this podcast but today is different i've got a
[1623.48 --> 1629.88]  special treat for you i went out and spoke with a listener who a year ago had never heard of top towel
[1630.28 --> 1635.32]  he listened to the show just like you're doing right here right now today and heard us talk about
[1635.32 --> 1640.76]  top towel and what they're all about and he decided to get in touch and now he's living the dream as a
[1640.76 --> 1645.88]  freelance software developer with top towel his name is daniel alzon and i sat down and i talked with
[1645.88 --> 1652.52]  him i said hey what is it that you love most about top towel take a listen well for me the the thing
[1652.52 --> 1658.52]  about top towel which i thought would be very hard for me personally as i transitioned to a more
[1658.52 --> 1665.32]  consulting role uh was the way i would have access to new clients and what quality of those would be
[1666.28 --> 1671.80]  so i found that i've had access to awesome clients through top towel and it hasn't been that hard to
[1671.80 --> 1677.64]  find because they have a lot of choice and even more than that uh there's enough choice and i i can
[1677.64 --> 1683.40]  actually be a little selective about what kinds of things i want to be working on so i use that as a
[1683.40 --> 1689.48]  way to sort of hone my skills and you know go towards the technology that i think are worth investing in
[1689.48 --> 1695.32]  for the future so whether it's you know including new front-end frameworks or doing a little devops work
[1695.32 --> 1701.08]  on the site i i usually am able to find clients who are have the needs of the things i want to get
[1701.08 --> 1707.56]  better at so that's been that's been truly useful all right that was daniel lazon a listener of the
[1707.56 --> 1714.44]  change log and also a freelance software developer with top towel if you want to follow in daniel's
[1714.44 --> 1723.96]  footsteps go to top towel dot com slash developers that's t-o-p-t-a-l dot com slash developers to
[1723.96 --> 1728.20]  learn more about what top towel is all about and tell them the change log sent you
[1730.60 --> 1736.84]  all right we are back and we are talking about a framework called metasploit i'd like to get into
[1736.84 --> 1744.28]  the history because it's been around a while it's massively popular and i even recall it from my
[1744.28 --> 1751.72]  youngster days at college um trevor you mentioned wireshark and nmap those were definitely tools
[1751.72 --> 1755.96]  exposed to us i think wireshark was called something different back then it was like
[1756.84 --> 1761.56]  ethereal thank you and i always thought that was a silly name wireshark's a pretty cool name though
[1762.20 --> 1770.76]  um anyhow metasploit was a thing that you know we used so uh that was back in 2005 2006 so
[1770.76 --> 1775.64]  um as much as you know kind of give us a little bit of a history of the project i know we've talked
[1775.64 --> 1783.16]  a little bit about it but let's recap and and when y'all got involved yeah so it started out as a game
[1783.72 --> 1791.96]  um hdmore our founder created it as the game you can play on any network and it was originally in
[1791.96 --> 1799.64]  and curses gooey really or yeah uh and it had one it started out with one exploit it was the
[1800.44 --> 1807.00]  uh apache chunked encoding overflow and i remember it well you had a yeah you had the um
[1807.64 --> 1815.56]  uh class c network block uh as individual pixels and whenever you compromise the machine one of the
[1815.56 --> 1821.32]  pixels would turn red that's awesome yeah it was super cool uh but not very useful at the time
[1822.52 --> 1830.76]  yeah um so we got it got it was originally in pearl it got rewritten uh in basically an entire rewrite
[1830.76 --> 1842.28]  when uh hd picked up a couple of contributors spoonim and scape um scape later went on to microsoft and
[1842.28 --> 1847.32]  created a whole bunch of mitigation technologies that made exploitation a heck of a lot harder
[1848.12 --> 1856.68]  in terms of memory corruption so the project went on without him and went on without spoon and around
[1857.56 --> 1867.48]  uh 2005 2006 um i started using it for um for writing my own exploits and it was about that time when scape and
[1867.48 --> 1879.32]  spoonim left and um that's that's when it started moving towards uh ruby where it had originally in
[1879.32 --> 1888.84]  pearl had a eula-like license to prevent uh some of the um blatant corporate misuse uh that had been going
[1888.84 --> 1898.92]  on with it um and when when it moved to ruby uh it maintained that license for a little while um shortly
[1898.92 --> 1910.36]  after i got commit access um we changed the license to bsd so now it's real full-fledged open source
[1910.36 --> 1917.24]  um and you can do anything you want with it but the uh the great thing about that is that we get
[1917.80 --> 1925.16]  um somewhere in the neighborhood of 200 unique authors on commits uh every year for the last two to three years
[1925.16 --> 1933.80]  nice um so that's that's really cool and a lot of them are only a single commit um which is great because it means that
[1933.80 --> 1941.72]  someone new is coming in and saying you know here is some thing that i see missing or or some
[1941.72 --> 1947.40]  functionality that i want to have and so they write it up and they submit it to us as a pull request
[1948.44 --> 1954.04]  and then they go about their business and they continue using the the tool and and and breaking
[1954.04 --> 1959.88]  into networks with it um but you know they've they've contributed something that 200 000 people use
[1959.88 --> 1966.44]  uh which really really makes me happy that that we can that we can get that kind of contribution from
[1966.44 --> 1971.16]  from so many unique people it is really cool to see i gotta say like and one thing that i'll add to
[1971.16 --> 1976.12]  that that is something i think drew has has drawn a lot of people who work on it full-time to the project
[1976.12 --> 1981.16]  is that um metasploit is now um because it's been around and and you know when it first started it was
[1981.16 --> 1985.00]  sort of controversial like oh we're going to actually publish these exploits right we're going to
[1985.00 --> 1991.32]  create this sort of library of malware um well now it's that that notion um where it was sort of
[1991.32 --> 1997.56]  very scary and and controversial when it first started um is is now pretty well understood and
[1997.56 --> 2003.64]  is pretty well accepted um even to the point where i think it was in an article in uh 2012 um the new
[2003.64 --> 2009.08]  york times referred to us as um a sort of early warning system for malware um and i've kind of always
[2009.08 --> 2014.12]  liked that that notion of what metasploit can be it's sort of like you know if you're vulnerable to
[2014.12 --> 2019.88]  something in metasploit um you're doing it wrong because we're we're not generally going to be
[2019.88 --> 2024.60]  publishing things that um have no mitigation available i mean there are going to be times
[2024.60 --> 2029.08]  when we do that but it's specifically to help put pressure on vendors and create a good outcome for
[2029.64 --> 2035.96]  all of the huge numbers of people who are going to be vulnerable to some given um software flaw and and
[2035.96 --> 2042.84]  when we do that um usually if we publish something that has no patch or has no uh vendor response yet
[2042.84 --> 2049.08]  it's because it's already being exploited in the wild exactly yeah one of my favorite examples is
[2049.08 --> 2058.52]  also um i believe from 2012 from late in 2012 um i'll get the dates and timing wrong but um there was a
[2058.52 --> 2066.36]  a large vulnerability in um pretty much every browser um there was the way that like the bridge of
[2066.36 --> 2072.60]  from javascript to java that was available so that like you know in 2005 you could go to like yahoo games and
[2072.60 --> 2078.28]  play bejeweled online or whatever um that that kind of like java applet sort of loading directly
[2078.28 --> 2084.92]  through javascript kind of bridge things called rhino um and there was this major major flaw that
[2084.92 --> 2090.68]  that was being exploited in the wild and that was giving um you know remote code execution like the
[2090.68 --> 2096.12]  holy grail um to whoever was was doing these attacks and these attacks were being weaponized in this real
[2096.76 --> 2100.76]  sort of compact kind of drive-by form right so you click the wrong web link and bam you're owned
[2100.76 --> 2108.52]  um so this is terrible and it it was estimated to affect over 750 million computers um and we were
[2108.52 --> 2115.00]  uh in we you know we maintained a disclosure program at rapid seven one of our colleagues does and so
[2115.00 --> 2119.56]  that involves a lot of sort of like you know closed door conversations with the security researchers who
[2119.56 --> 2123.16]  have found a vulnerability and want to to do responsible disclosure of that vulnerability
[2123.72 --> 2130.04]  um and these researchers had disclosed um to the maintainers of java oracle um already they had done it
[2130.04 --> 2135.72]  um that that spring right so um by the late summer so it had been like significant amount of time
[2136.52 --> 2141.56]  that they had since they had disclosed with oracle um and then they came to us because i guess we had a
[2141.56 --> 2149.56]  little bit more of a megaphone or whatever and um we disclosed again with them um and oracle came back
[2149.56 --> 2154.20]  and said you know we needed like a really long time to patch this i can't remember the exact amount
[2154.20 --> 2158.04]  of time but i believe it was something like a year or 18 months um to affect this patch
[2158.04 --> 2164.44]  yeah at the time oracle's patch cycle was 18 or was uh six months and they wouldn't guarantee
[2164.44 --> 2169.64]  a patch on anything uh fewer than two cycles out right so so you're looking at potentially like a year
[2169.64 --> 2174.92]  and a half before you're going to see anything on this right and you know and and metasploit was in
[2174.92 --> 2179.80]  a position to basically say as we don't care we don't believe that that's an acceptable thing like
[2179.80 --> 2186.76]  like you know um you bought you bought sun you've got java it's your thing now and um you know your
[2186.76 --> 2193.80]  your product is is vulnerable in in this enormous number of computers so um we were we we published
[2193.80 --> 2200.52]  the exploit and um i believe that that oracle had a patch out um if i recall correctly it's like three
[2200.52 --> 2204.76]  days but it was certainly less than a week later they had a patch version of java and now java as you
[2204.76 --> 2208.52]  as you know there's a kind of this spate you might remember around this time of a whole bunch of bugs
[2208.52 --> 2213.00]  and sort of this general area of things a whole bunch of vulnerabilities and now um i believe
[2213.00 --> 2218.04]  that on i know that on os 10 and on windows i believe pretty much anywhere you can think of
[2218.04 --> 2222.28]  if you're going to install a browser that browser is no longer going to have a hard dependency on java
[2222.92 --> 2228.12]  and if you want to do some java stuff you're going to need to go ahead and you know install it yourself
[2228.12 --> 2233.96]  in the case of like os 10 or i'm not 100 certain how it works on on windows right now but you know java
[2233.96 --> 2238.20]  used to just be like a dependency and just kind of just there and nobody really thought anything of it
[2238.20 --> 2242.68]  um but you know that's that's one of my favorite examples of metasplate putting
[2242.68 --> 2247.56]  um very significant pressure on a very large vendor and getting a really really positive outcome out of
[2247.56 --> 2252.28]  it man that's that's interesting there's so many different avenues i could go off of that because
[2252.28 --> 2258.44]  we have the licensing aspect you have kind of the the script kiddies idea you have the balancing act
[2258.44 --> 2265.72]  that you guys have to be participating in of what do we include in what is out so um whenever you
[2265.72 --> 2272.20]  wield a tool that's powerful like metasploit it can be used for good it can be used for bad
[2272.20 --> 2278.20]  this is where we kind of get the idea of white hat hackers black hat hackers um gray hats which that
[2278.20 --> 2284.52]  was a thing back in 2006 i'm not sure do people still use that term yeah okay just making sure um
[2285.08 --> 2288.04]  what's it mean i don't remember like you're kind of doing both you're just
[2289.72 --> 2293.24]  well the funny thing about white you put a little black in it and then no matter how much more white you
[2293.24 --> 2298.12]  put on top it's always going to also like you have a history is that what it means i see so it's
[2298.12 --> 2305.08]  like black hat turned white maybe uh that's where the intrigue comes in this work a white hat's the
[2305.08 --> 2311.00]  a white hat that's not necessarily entirely got you got you okay so you got those people um
[2312.68 --> 2319.00]  and man there's just a lot of actors there's a lot of interested parties and then we have this
[2319.00 --> 2323.08]  idea of a script kitty egypt you want to kind of explain what that is perhaps and then
[2323.08 --> 2331.08]  maybe address um metasploit's history with with these type of people yeah that's an interesting
[2331.08 --> 2336.20]  term script kitty is that still a term maybe i'm dating myself it is a term okay it definitely is
[2336.20 --> 2341.48]  it still exists and people do you hate that term um but i i did i just don't think it has the meaning
[2341.48 --> 2346.12]  that it used to it doesn't have the the weight that it used to because it used to mean that there was
[2346.12 --> 2351.56]  a script kitty was someone who used other people's scripts and didn't have the skill to write their own
[2351.56 --> 2357.64]  own couldn't write their own exploits um but the fact is today you don't have to write your own
[2357.64 --> 2364.52]  exploits because there are just so many things out there you know you don't need to know the intricate
[2364.52 --> 2371.08]  details of a particular heap allocator on this operating system because most exploits most things
[2371.08 --> 2376.92]  that get you data that let you steal credit cards are going to be sql injection now i've seen 12 year
[2376.92 --> 2386.04]  olds bust out sql injections and steal stuff like you you don't need to be super deep into all the
[2386.04 --> 2391.56]  details of how an operating system works to steal data so i'm saying it's just getting even easier
[2392.68 --> 2398.12]  right and and that's not because exploitation has gotten easier it's because the kind of bugs
[2398.12 --> 2404.68]  that are prevalent these days are different um you know there's still a lot of memory corruption
[2404.68 --> 2410.84]  vulnerabilities but they've gotten exponentially more difficult to exploit so i mentioned scape's
[2410.84 --> 2417.96]  work with microsoft with seh medications seh is the structured exception handler which was sort of a
[2417.96 --> 2427.56]  generic way to allow a buffer overflow on the stack to give you code execution and that basically killed an
[2427.56 --> 2434.52]  entire class of bugs because of that mitigation and it's no longer generically exploitable to
[2434.52 --> 2443.48]  overflow a buffer on a stack in a windows application so you know seh protections in in addition to stack
[2443.48 --> 2452.60]  cookies and other general exploit mitigations on on uh memory corruption issues in windows have made
[2452.60 --> 2459.96]  those sorts of bugs very difficult to exploit you know in in 1999 writing a buffer overflow required
[2459.96 --> 2464.20]  uh staring into the debugger and reading a lot of manuals and figuring out how it worked
[2465.08 --> 2473.16]  um and when you were done you had you know maybe 10 lines of exploit code and it took you a couple of
[2473.16 --> 2480.36]  days now if you want to exploit something uh in a modern browser so say for example in flash
[2481.32 --> 2488.12]  you have to understand how the action script bytecode compiler works in flash and then you have to
[2488.12 --> 2493.08]  understand the heap allocator how that works and then you have to understand all of the pieces of
[2494.28 --> 2500.52]  every other little thing that is necessary to control memory in that application it's a huge thing and
[2500.52 --> 2507.40]  there's a lot of stuff that gets in your way and there are some techniques that make it a little easier
[2507.40 --> 2516.12]  um but in general memory corruption is going the way of the dodo um with 64-bit operating systems
[2516.12 --> 2521.96]  becoming more and more um prevalent basically all your desktops are going to be 64-bit now
[2522.52 --> 2530.84]  um so many of those things are just going away but you have things like sql injection and you have command
[2530.84 --> 2538.36]  injection and you have just passwords lying around on passwords.xls on somebody's desktop so so saying
[2539.16 --> 2543.32]  someone's a script kitty for not writing their own exploits i just don't think has the weight that it used
[2543.32 --> 2550.84]  to um there's there are a lot of ways of getting into a system there's a lot of ways of stealing data
[2550.84 --> 2560.12]  that don't involve writing your own memory corruption exploit um and i i think it it's it's giving short
[2560.12 --> 2568.60]  shrift to the the attackers who are very clever but not necessarily um savvy in the ways of how an
[2568.60 --> 2573.80]  operating system works but can't we don't we just change the focus to web applications then and you
[2573.80 --> 2580.04]  can still you know let's take for instance now that the vector becomes uh ruby on rails just for
[2580.04 --> 2585.80]  instance keep it in the ruby camp of course django whatever a web framework now and some security
[2585.80 --> 2594.20]  researcher it would say a black hat finds a flaw and ruby on rails um it took perhaps a large amount
[2594.20 --> 2600.60]  of wisdom to do that maybe it was an easy one um isn't that the kind of exploit that would end up
[2600.60 --> 2606.12]  inside of metasploit and then me having no knowledge of that whatsoever can just point it at a machine and
[2606.12 --> 2611.72]  run it well it has but i mean you would also have to find you you would need the skill to find a machine
[2611.72 --> 2617.40]  that was that was vulnerable to that right you need to be able to dig that out of um you know the the
[2617.40 --> 2621.88]  sort of enormous that that needle out of the enormous like haystack of of kind of what the
[2621.88 --> 2627.72]  the modern you know modern large companies or even small companies um like attack surface looks like
[2628.28 --> 2632.44]  and then you would need to understand what to do once you've delivered that exploit right so
[2632.44 --> 2639.00]  i mean you know egypt's point is is really well taken here i mean we we talk a lot with obviously like
[2639.00 --> 2644.60]  a lot of big deal pin testers um guys who are on you know red teams for like fortune 50 companies
[2644.60 --> 2649.00]  and stuff like that who get paid to do nothing but try to break into these enormous enormous companies
[2649.00 --> 2653.64]  that do really big deal things and these guys will tell you that they've literally used exploits like
[2653.64 --> 2659.88]  once or twice in like a decade or a dozen years long career um just simply because it's just easier
[2659.88 --> 2665.08]  than that out there you know and you know to egypt's point from before i mean we take a look and we we
[2665.08 --> 2669.88]  watch um what's going on in terms of what's exploited in the wild and then we make an effort
[2669.88 --> 2675.32]  to make sure that that we are able to kind of follow along with that and have something in in
[2675.32 --> 2679.88]  metasploit that exploits something in that same way um but you know a lot of people are tempted to
[2679.88 --> 2685.48]  think of this and i think that this is really um you can blame you can blame media for this right
[2685.48 --> 2689.80]  a lot of people look at this stuff and they're like oh you're a hacker you have these magic powers
[2689.80 --> 2694.92]  metasploit is this collection of magic skeleton keys all i need to do is install it and then suddenly
[2694.92 --> 2700.36]  you know i can i can just wave a wand and like you know break into people i mean that's just false i
[2700.36 --> 2705.72]  mean most people probably don't think about it but it's it's probably easier to hack the average
[2705.72 --> 2711.48]  corporation almost certainly of any size than it is to hack an individual person just simply because
[2711.48 --> 2717.40]  there's so much out there that what they call the attack surface is so large right right and you've
[2717.40 --> 2722.76]  and you've got you know years and years of of it guys that have installed random stuff on there or
[2722.76 --> 2727.72]  have put local admin on a particular windows machine and da da da da and you know there's
[2727.72 --> 2732.28]  attrition people leave jobs people forget what they installed people you know just kind of leave
[2732.28 --> 2738.44]  things around as business moves forward um so you know even if somebody could say find um to just
[2738.44 --> 2743.72]  extend your example find a rails application that's vulnerable to like the yaml injection remote code
[2743.72 --> 2749.56]  execution bug from a couple years ago and they can get you to you know they can they can use that
[2749.56 --> 2756.20]  that that exploit well i mean metasploit has provided a a bit of code for that and has provided
[2756.20 --> 2762.68]  um you know a very very useful mechanism for interactivity with a nice little shell and for
[2762.68 --> 2767.64]  delivering a payload um to to be able to do something useful with that access but what then
[2768.20 --> 2773.16]  you know i mean the classic formulation of a script kitty is somebody who's just sort of like you know
[2773.80 --> 2778.52]  praying and spraying and just seeing what happens right um but then what then if that person
[2778.52 --> 2782.84]  actually knows how to you know move laterally through the network and steal a bunch of useful
[2782.84 --> 2787.88]  data can you really call that person a script kitty anymore i mean like a script teenager
[2789.16 --> 2795.16]  right exactly i mean these these people you know i think that the term itself while it still gets used
[2795.16 --> 2800.12]  um and even used at our expense indirectly on mr robot um go look for the um
[2800.12 --> 2808.68]  um no spoilers no spoilers i haven't right exactly sorry guys um but uh yeah i mean you know it's it just
[2809.80 --> 2817.96]  the the era i think of people being able to be like accidentally very damaging um is kind of um
[2818.60 --> 2824.28]  i don't know how and i don't know how legitimate that is anymore i mean um it's information security
[2824.28 --> 2829.56]  right so there's always like caveats and and long tales of problems out there and you know there's there's
[2829.56 --> 2833.72]  all kinds of things that are horribly insecure that are made directly available to the internet um
[2834.36 --> 2841.16]  atms being a fantastic example um but you know which are all running windows xp yeah which doesn't
[2841.16 --> 2847.48]  get security updates anymore so be afraid um yeah it's just not a i i don't know how how useful it is
[2847.48 --> 2852.12]  as like a genuine critique of the people who are actually trying to use a particular thing yeah and
[2852.12 --> 2856.52]  i'm not i'm not necessarily critiquing i'm trying to understand as a somebody who's involved you know
[2856.52 --> 2862.60]  at with the project is you have people using it for good and you have people using it for bad and
[2863.08 --> 2868.36]  some of those concerns you know have to maybe not weigh on you but things that you're actively
[2868.36 --> 2873.56]  thinking about when you decide if an exploit is going to go in when it's going to go in in the case of
[2873.56 --> 2881.00]  your oracle example you know that was something that you used it as leverage to get them to act um
[2881.00 --> 2885.40]  which ended up being a great win right that's a success story but what if they would have just been
[2885.40 --> 2890.20]  like well screw you guys we're going home now i mean effectively okay it's their fault not yours
[2890.20 --> 2896.68]  but now you've given that vulnerability that exploit out to well but that attitude assumes that like we
[2896.68 --> 2900.84]  had that and other people that's true and that we you know and that's it could get out there in a
[2900.84 --> 2905.08]  different way well it's already out there that's what you need to always remember it's already out
[2905.08 --> 2911.96]  there we we put this in because we're able to do some monitoring of various forums and whatnot and
[2911.96 --> 2916.52]  we're able to see like people have these types of things are getting exploited already out there
[2916.52 --> 2921.56]  right like keep in mind that the crime work kits that you would spend a bunch of money on right now
[2921.56 --> 2926.36]  like say you're um i don't know you're some bad actor somewhere in the world and you you decide to
[2926.36 --> 2932.36]  to get on there's basically like a silk road of like malware on on tour right you could get on there
[2932.36 --> 2937.96]  you could buy um a crime work kit um which comes about a thousand bucks about a thousand bucks it's
[2937.96 --> 2942.28]  beautiful interface it'll come with some stuff that's um you know it's not quite ode because
[2942.28 --> 2946.84]  it's in the crime work kits but you know it's it's not in metasploit either necessarily right i mean
[2946.84 --> 2953.16]  like we're we are not like there's this temptation to believe that oh the thing i know about is
[2953.16 --> 2959.32]  metasploit and metasploit's got this library of malware in it um therefore metasploit must be
[2959.32 --> 2964.92]  filled with awful stuff that can be used to like own computers all over the place which is really only true
[2964.92 --> 2970.60]  if you're not you know if you're not patched right so the idea that we aren't like completely
[2971.32 --> 2975.40]  um you know that we that we're like on the forefront and if we don't release something
[2975.40 --> 2980.76]  it just won't be out there that's tempting but it's totally not true the bad guys are going to
[2980.76 --> 2987.32]  have this stuff fair point fair point yeah and i'd like to point out that um especially in that rhino
[2987.32 --> 2992.52]  case um it was already being exploited in the wild and that's true of a whole bunch of our exploits
[2992.52 --> 3000.52]  already being exploited sometimes in targeted attacks against specific organizations and we
[3000.52 --> 3007.88]  make it available for everyone to know what the exploit is doing which significantly lowers the
[3007.88 --> 3015.64]  value for a malware author fair enough i just i'm stuck back where trevor said you got a bad actor
[3015.64 --> 3019.56]  out there trying to hack something and i just pictured ben affleck sitting there at a computer i don't know
[3019.56 --> 3025.88]  oh that's sneak had it had to sneak that one in there all right let's take another break here from
[3025.88 --> 3031.32]  another one of our sponsors we'll be back because we haven't talked about metasploit the technology
[3031.32 --> 3037.32]  very much how it works how you contribute how you use it those fun things we know it's built on ruby
[3037.32 --> 3041.40]  but that's about all that we know at this point so let's take a quick break and we'll be right back
[3041.40 --> 3047.96]  for those out there working solo or on a team tracking time you thought you were wrapping up
[3047.96 --> 3054.60]  a project until the client or your boss asks for a new feature at the last minute and here you are
[3054.60 --> 3058.52]  stuck you're not sure how much time you're spending on every feature how much time you're spending on
[3058.52 --> 3066.60]  bug fixes or tweaks well harvest is a time tracking tool built for understanding where your time is going
[3066.60 --> 3072.04]  and for developers it takes the pain out of time tracking just install the harvest crumb extension
[3072.04 --> 3077.00]  and you can start tracking time right from issues in jira or github and you won't have to go searching
[3077.00 --> 3082.20]  for your time sheet not only will you understand how much time you're spending on client work you'll
[3082.20 --> 3088.52]  also be able to turn your billable hours into an invoice from harvest in minutes harvest integrates
[3088.52 --> 3093.48]  with stripe and paypal to make sure you get paid fast and on time there's built-in reporting in
[3093.48 --> 3097.08]  harvest that lets you see how much time your projects took so you can use that information
[3097.08 --> 3102.60]  to make better estimates in the future for a better way to track time and invoice your clients
[3102.60 --> 3106.28]  and take the pain out of what you're doing when it comes to tracking time and invoicing
[3106.28 --> 3113.00]  head to getharvest.com create a 30-day free trial and after your trial is over here's a goodie for all of
[3113.00 --> 3121.08]  our listeners enter the code changelog to save 50 off your first month once again getharvest.com create a
[3121.08 --> 3127.80]  free 30-day trial and after that trial is over enter the code changelog for 50 off your first month enjoy
[3130.92 --> 3135.72]  all right we are back and i want to hear about metasploit from a technological perspective
[3136.28 --> 3142.76]  the software how it works um we know it's a ruby app we know it used to be pearl we know it used to be a
[3143.32 --> 3149.72]  a game a curses based game which still sounds pretty rad if you ask me but egypt um can you give us a
[3149.72 --> 3154.92]  little bit about the software stack um how you even use it how you install it and then maybe how you
[3154.92 --> 3165.96]  contribute exploits okay so there's the main thing which is ruby um with a client console interactive
[3167.00 --> 3173.08]  front end called msf console that's the metasploit framework console um there are also a number of
[3173.08 --> 3182.60]  other standalone tools um msf venom is our payload generator um we also have a an assembler shell that
[3182.60 --> 3195.56]  allows you to to assemble x86 and x64 um assembly into bytecode um all of our payloads are in the the
[3195.56 --> 3201.88]  payload uh technology that makes sense for that particular target so for windows it's written in c
[3201.88 --> 3210.44]  um and our our flagship payload is called meterpreter the meta interpreter it allows you to interact
[3210.44 --> 3217.32]  with a system like a normal command shell and in fact you can drop directly to a cmd shell or a power
[3217.32 --> 3228.04]  shell shell to talk to a windows box and all of that is written in c with a dll as the actual payload that
[3228.04 --> 3234.60]  gets delivered but we also have these things called stagers which as a result of the way exploits
[3234.60 --> 3241.48]  typically work in memory corruption vulnerabilities you have a small area where you can put your your
[3241.48 --> 3247.56]  payload which is often called shellcode and that's restricted in size and it's usually restricted in
[3247.56 --> 3255.00]  character set as well so for an example if your overflow is in like an ftp username well the at symbol
[3255.00 --> 3260.52]  separates the username from the host name so if your if your payload contains an at symbol then it's
[3260.52 --> 3266.12]  going to break the parsing and you won't get in the shell so we have we have encoders that get rid of
[3266.12 --> 3272.92]  those bad characters and randomize things with an xor key and you can create a small little piece of
[3272.92 --> 3280.92]  assembly that gets executed on the victim machine and all it's all it's for is to talk to the attacker
[3280.92 --> 3287.40]  machine uh and grab more code to execute and that more code to execute is typically a dll that allows
[3287.40 --> 3294.36]  us to do arbitrarily whatever you want um we should probably explain the payload like like the payload
[3294.36 --> 3299.88]  versus exploit sort of dichotomy here for people that don't understand it right yeah that's a good
[3299.88 --> 3307.16]  idea so um in general an exploit takes advantage of a vulnerability there there's some bug on a target
[3307.16 --> 3312.68]  system um that that i can take advantage of so i use an exploit to do that that's the terminology the
[3312.68 --> 3320.36]  exploit uh will deliver a payload as part of of the normal protocol that it speaks to the victim machine
[3321.24 --> 3328.20]  so in an in like an http example if this the server is listening on port 80 i connect up to it on port 80
[3329.08 --> 3335.08]  i send my malicious request which contains a payload that payload executes on the victim machine
[3335.08 --> 3342.04]  and then somehow it communicates back to me sometimes that's through tcp uh sometimes that's http
[3343.48 --> 3350.84]  but either way the payload is running on the victim machine and it talks to the attacker machine and
[3350.84 --> 3356.20]  that gives us the the ability to control that machine to get it to create new sockets so that we
[3356.20 --> 3362.76]  can talk to other machines that it can see inside its own network so if if i'm if i'm out on the internet
[3362.76 --> 3368.20]  and there's a machine on a dmz i compromise it now i can see all of the other machines on the inside
[3368.20 --> 3375.32]  of its network that i wouldn't be able to see from the internet um so an exploit executes a payload the
[3375.32 --> 3382.12]  payload talks to a handler that's the the thing on the on the ruby side that allows you to interact
[3382.12 --> 3389.40]  with it from a user perspective um and from there you can drop into uh an interactive shell as well
[3389.40 --> 3397.08]  and and run commands that will get executed on the target machine um so that's the like general
[3397.72 --> 3404.20]  workflow of an exploit you use an exploit you set all the options necessary to to take advantage of
[3404.20 --> 3409.40]  that vulnerability it runs a payload on the target machine that target machine connects back to you and
[3410.84 --> 3418.52]  gives you a shell through the handler and then from there you commence your post exploitation activities
[3418.52 --> 3424.36]  and we have a whole bunch of of modules that make post exploitation easier and that make it
[3426.12 --> 3433.56]  a little more robust in terms of the kind of data you can get a hold of one of my favorite things
[3433.56 --> 3440.68]  is a tool called meme cats that's been integrated into metasploit i'm liking the sound of this yeah
[3440.68 --> 3449.48]  uh what that does is it roots around in the memory on a windows machine um and finds all of the
[3449.48 --> 3455.72]  the authentication structures inside uh lss.exe which is the the thing that does authentication in windows
[3456.52 --> 3461.40]  it roots around in its memory using the windows debugging api and pulls out the structures that are
[3461.40 --> 3467.24]  necessary to do authentication uh and in many cases it can pull out plain text passwords for everyone who's logged in
[3467.24 --> 3474.84]  wow so that's really really super useful um if you don't get plain text passwords from that you can
[3474.84 --> 3481.96]  still often get ntlm hashes um and if you're if you're at all familiar with the way um windows
[3481.96 --> 3488.92]  authentication works uh an ntlm hash is essentially uh a password oh this is my favorite thing we got to
[3488.92 --> 3494.36]  talk about this like so yeah when i first got into information security like working at rapid 7 i started
[3494.36 --> 3499.32]  kept hearing about past the hash past the hash um which sounded you know illegal a drug thing or
[3499.32 --> 3504.36]  something right exactly and um it it's kind of astonishing if you've been working in like
[3504.36 --> 3510.12]  web application development or something for a long time because what it means is um in in windows
[3510.12 --> 3514.92]  authentication right and and probably quite a few of the people listening to this podcast whether they
[3514.92 --> 3520.36]  actually ever touch windows or not are they're very likely to be dealing with an active directory domain
[3520.36 --> 3525.16]  controller right like if you have outlook as your microsoft exchange is like your email solution right
[3525.16 --> 3530.68]  then a whole lot of things do like single sign on right right um they make this happen so um what
[3530.68 --> 3536.68]  happens in in past the hash is that the client is actually responsible for creating the hash as opposed
[3536.68 --> 3541.64]  to like in a web application where you take in a plain text password you run it through your hashing function
[3541.64 --> 3545.40]  you compare that to what you've stored in the database i mean hopefully you know that's what you're doing
[3545.40 --> 3551.40]  right um that's not what happens the client itself is actually sending doing the hashing and sending
[3551.40 --> 3557.80]  the hashed data that over to the the um the authentication mechanism so what you have there is
[3557.80 --> 3562.84]  exactly what egypt just said effectively if you can steal a hash you can pass it and use it as a password
[3564.04 --> 3568.92]  so this is the the basis for a lot of like lateral movement through networks right i mean you know quite
[3568.92 --> 3574.76]  a bit of the time you'll find that um for expediency back in the day some it guys set up five or six
[3574.76 --> 3580.52]  machines with local admin access and that local admin um you know is is using the same password
[3580.52 --> 3584.04]  that all the guys in the it department knew and now you can take that same thing and you can you
[3584.04 --> 3589.32]  grab that hash and you can pass it around um so the you know the one of the many things that you can do
[3589.32 --> 3593.56]  with with metasploit after you've compromised the machine after you have a session on there is
[3594.36 --> 3599.32]  scrape all different kinds of passwords out of all different kinds of files right we have um we've got
[3599.32 --> 3604.04]  obviously ones to do the classic windows stuff and grab all of those but then we've also got things like
[3604.04 --> 3609.88]  um stealing a keypass database if you can find one on the machine um scraping skype hashes from
[3609.88 --> 3615.16]  wherever they're located on whatever type of platform you've just victimized right and um
[3615.16 --> 3618.60]  bringing them all and handing over to offline cracking tools like john the ripper or something
[3618.60 --> 3623.64]  like that so you know um you can go through and just start running them through a cracker and then
[3623.64 --> 3628.20]  hopefully you know hours or days later or whatever you've got a whole bunch of nice passwords that
[3628.20 --> 3632.52]  you can start replaying in different places um yeah and in some cases you don't need to do any kind
[3632.52 --> 3638.36]  of cracking um so windows has this awesome thing called uh crypt secure data and crypt on secure
[3638.36 --> 3647.56]  data um which is the the api intended specifically for storing secret stuff in windows um but if i'm
[3647.56 --> 3653.32]  running as your user i can encrypt all of the stuff that you have encrypted as that user um so you can
[3653.32 --> 3658.20]  just ask ask the operating system it'll give you all of those secrets for free if you have the that
[3658.20 --> 3664.12]  user's privileges at the time right exactly so that's that's fine so if i'm if i'm running as
[3664.12 --> 3670.28]  you and you can do anything at all without using your password then i have your password well that
[3670.28 --> 3678.68]  doesn't sound very awesome for me so let's say that i'm a a budding network administrator or let's say
[3678.68 --> 3684.76]  that i'm a app developer with a network that i'm interested in running some of these things against
[3684.76 --> 3688.76]  or maybe i just want to play with it and see what it does how do you get started with meta
[3688.76 --> 3696.92]  display how do you use it as an end user uh well for an it admin i would suggest starting with the
[3696.92 --> 3703.56]  community edition which is a the rails gui um that's sort of the basis for our commercial editions
[3704.20 --> 3710.76]  because it gives you a lot of the the power of the console interface but it's point and click and it's
[3710.76 --> 3718.28]  got a less steep learning curve um if you really want to dive into it the the console does have
[3718.28 --> 3725.56]  a slightly higher learning curve but it does have faster access to some aspects of the framework um
[3726.20 --> 3730.92]  so i'd say when you're when you're first getting started community is absolutely the way to go
[3732.28 --> 3736.76]  yeah and i would say i would i would say that's that's definitely true um unless unless you're just
[3736.76 --> 3743.00]  like you love cli you want to dive in on the command line um you know it's very easy to um grab the code
[3743.56 --> 3751.16]  um there's also we distribute um we're with uh kali linux which is a big um open source um sort of
[3751.16 --> 3756.44]  penetration testing uh linux distribution so um the framework is available like right out of the box
[3756.44 --> 3759.88]  right there along with a bunch of other really fun tools pretty much everything that we mentioned um
[3759.88 --> 3766.92]  for the most part on this call um and i would say that also i i personally when i was getting up to
[3766.92 --> 3771.16]  speed on the application when i joined rapid 7 um i know that some of the content is a little bit out
[3771.16 --> 3777.56]  of date but the no starch press book um metasploit unleashed um which was written by a bunch of um
[3777.56 --> 3782.84]  of sort of long-time uh contributors and sort of friends of the family um basically a bunch of
[3782.84 --> 3788.52]  penetration testing people um is a really good book just sort of for understanding like how to how to get
[3788.52 --> 3793.16]  started how to use this how to kind of like um get your head around like what the framework does and
[3793.16 --> 3797.80]  why it's powerful might be a good time to mention that there is as you guys said there's a divide
[3797.80 --> 3805.00]  between the open source bsd license metasploit framework and i believe what's called the metasploit
[3805.00 --> 3812.12]  project which is well the commercial editions really is what we call them at rapid seven so um right so we
[3812.12 --> 3816.36]  have like like a lot of commercial open source things we have like a couple different like you know
[3816.36 --> 3820.84]  price points with different features turned on or off right um the framework is the engine of all
[3820.84 --> 3827.40]  of those things though so um so what's outside of the framework what's in the proprietary ones
[3828.04 --> 3836.76]  metasploit pro contains things um like a jasper reports based reporting engine um it has a a whole um
[3837.56 --> 3842.20]  really nice social engineering toolkit that you can use um it's it i like to tell people it's sort of
[3842.20 --> 3846.44]  like an evil online marketing system in a way because like you can use it to like create a
[3846.44 --> 3851.16]  little website and then like create an email and generate links that are like you know that have
[3851.16 --> 3855.08]  tags like to you know you can upload like an excel spreadsheet of like all the people in your org and
[3855.08 --> 3861.64]  then you can basically try to fish them and see like okay you know joe um you know opened the email but
[3861.64 --> 3868.20]  didn't click on it um mary didn't even open the email um but frank opened the email clicked on the link
[3868.20 --> 3873.08]  inside it and then filled out the form on the resulting web app and hit submit and we stole
[3873.08 --> 3878.36]  his creds so you know frank's got to go for security training or whatever right so a bunch of
[3878.36 --> 3882.60]  quite a few of our customers really enjoyed using that they can kind of like click click click they
[3882.60 --> 3887.24]  can clone an existing um website if they want to or whatever and they can kind of like deceive your own
[3887.24 --> 3893.32]  employees into right right it's weird it's it is it is a little weird but at the same time um
[3893.32 --> 3897.32]  most of the major breaches that anybody could name off the top of their head for the last couple
[3897.32 --> 3903.40]  years have been what we refer to at rapid seven as deception based attacks um so it's very germane
[3903.40 --> 3907.48]  like it it really really is and you'd be surprised how many people can fall for this now granted if
[3907.48 --> 3911.56]  you're creating one of these things and you've got internal knowledge of the company um you know
[3911.56 --> 3915.64]  you're kind of tempted to sort of go a little bit um out of the bounds of where you would normally go
[3915.64 --> 3921.00]  just kind of naturally but um that's available hold on there hold on there i think that that insider
[3921.00 --> 3926.44]  knowledge isn't always all that inside um so as an example the first phishing campaign that i ever
[3926.44 --> 3934.20]  did that i was ever involved with um there were there were public rumors about a merger with this
[3934.20 --> 3940.60]  company that we were that we were targeting and another company and so we sent a phishing email with
[3940.60 --> 3947.40]  a pdf containing an exploit in it and the the subject of the email was basically the merger the merger has
[3947.40 --> 3954.76]  gone through and uh this pdf contains a list of everyone who's getting fired yeah fair point like
[3954.76 --> 3960.76]  at that point i i don't know whether that's just preying on human yeah that's pretty uh compelling
[3960.76 --> 3965.80]  content right right like who's not going to open that i would see that as one of the most suspicious
[3965.80 --> 3970.52]  things ever to come into my inbox but maybe that's just me after spending four years on meta's plate
[3970.52 --> 3976.20]  yeah i think you're probably pretty unique in that regard i think um but i mean there's so there's a
[3976.20 --> 3983.40]  there are a couple other um like larger features that are available inside um inside pro and most of
[3983.40 --> 3990.76]  those are a bit effectively to help um people who are kind of in the the security admin space um run a
[3990.76 --> 3995.40]  collection of meta splite content and then do some things and report on what it was able to do
[3995.40 --> 4002.84]  um in a sort of um you know in a nice kind of automated orchestrated fashion right whereas the
[4002.84 --> 4008.36]  the framework is all kind of nitty-gritty hands-on you can script it but it you know that's a lot of
[4008.36 --> 4015.40]  work to really scale your way up right um versus pro is going to give you a nice um goo interface for
[4015.40 --> 4020.28]  dealing with for instance maybe you've um you know maybe you've compromised hundreds of machines at the
[4020.28 --> 4025.32]  same time and you want to run you know the same two or three modules on all of those machines and have
[4025.32 --> 4030.04]  those that all be part of like one big report or something like that that's that would be a pain
[4030.04 --> 4035.32]  in framework and it's uh it's very simple and pro so pro is all about scalability communication with
[4035.32 --> 4040.28]  other people communicating up to your bosses or your stakeholders that kind of thing very cool well guys
[4040.28 --> 4045.96]  we got to take one more break i still want to talk about infosec and open source and the relationship
[4045.96 --> 4051.00]  between the two it seems like there can be a bit of a divide obviously metasploit is a big
[4051.00 --> 4057.00]  uh success story where you have open source and infosec um and maybe some ideas around how we can
[4057.00 --> 4061.88]  bridge those gaps uh and of course on the other side of the break our awesome closing questions
[4062.68 --> 4065.48]  um so stay tuned for that and we will be right back
[4067.40 --> 4073.80]  this week we have a sponsored repo to mention from our friends at transload it transload it is a
[4073.80 --> 4078.44]  versatile file uploading and encoding service and they've asked us to give a shout out to their open
[4078.44 --> 4086.68]  source project tusk it's a new open protocol for resumable uploads built on top of http it's simple
[4086.68 --> 4092.52]  it's cheap and it's available for any language on any platform on any network supports tech sums
[4092.52 --> 4099.64]  parallel uploading of chunks no more lost cat videos it's mit and open source some smart minds have
[4099.64 --> 4106.60]  collaborated on it like the author of http 1.1 employees at google and yahoo female's director of
[4106.60 --> 4111.32]  engineering zero mqs creator and there are implementations being pushed out for all major
[4111.32 --> 4117.32]  languages and frameworks also vimeo has already announced to use this open protocol for their new
[4117.32 --> 4124.60]  video uploading services and the 1.0 of their protocol is nearing completion as we speak they are calling
[4124.60 --> 4129.80]  for a final round of feedback on their pull request which will link up in the show notes before releasing
[4129.80 --> 4138.36]  it so if you're at all interested go to tusk dot io that's t-u-s dot i-o or head to the link we
[4138.36 --> 4144.52]  mentioned in the show notes to check out that pull request for 1.0's feedback and now back to the show
[4146.84 --> 4150.60]  all right we're back and i think trevor i'll point this one at you because we kind of talked about this
[4150.60 --> 4158.52]  briefly at gopher con um you have these two communities you have the open source developer community you have
[4158.52 --> 4164.12]  the infosec community it seems like there's some overlap and maybe the actual distinction is kind
[4164.12 --> 4170.20]  of the maker community and the breaker community to a certain degree um and it seems like we don't
[4170.92 --> 4177.64]  mesh very often can you speak to that yeah and it's something that i've that i've found curious in my
[4177.64 --> 4182.20]  my involvement with metisploit um and it's certainly something that that i think egypt and i share a
[4182.20 --> 4187.40]  desire to to help change that right so um you know that's part of why we we gave our talk at
[4187.40 --> 4192.04]  lone star ruby con like a month ago um just sort of trying to get people understanding like here's
[4192.04 --> 4195.80]  the types of challenges that we tackle that don't necessarily have anything to do with security per
[4195.80 --> 4201.48]  se um you know building a good network client um you know dealing with all the the different types
[4201.48 --> 4204.76]  of abstractions that your business logic requires of you and things like that right these are just
[4204.76 --> 4210.84]  programming tasks um and i think that probably what we're really looking at is a historical situation
[4210.84 --> 4215.64]  more than anything else right so that gives me hope i don't think that there's anything inherent or
[4215.64 --> 4221.96]  intrinsic that makes it difficult for people to spend any time on this um other than just
[4221.96 --> 4226.36]  historically i think a lot of people who are developers maybe haven't spent a lot of time
[4226.36 --> 4231.56]  thinking about how executables are structured or thinking about how networks work or things like
[4231.56 --> 4237.24]  that i think on the other side of it um quite a few people who write a lot of code um in the
[4237.24 --> 4241.72]  security world they're writing code under the gun they're on that like five or six day timeline
[4241.72 --> 4244.84]  that egypt mentioned before you know where they actually have four days for real because of their
[4244.84 --> 4249.72]  you know their contractual obligations otherwise so people who are who are writing this stuff
[4249.72 --> 4254.84]  sometimes are putting something together that isn't really designed to live very long and maybe
[4254.84 --> 4259.24]  they finished something and it was great and they they got it to work really well on their engagement
[4259.24 --> 4262.20]  their pen test engagement and they say you know what i'm going to clean that up a little bit and i'm
[4262.20 --> 4268.04]  going to i'm going to send that over to metasplayed as a pull request right um but we we get a widely
[4268.04 --> 4273.32]  varying level of quality in the code that people want to submit to the framework um and i think in part that's
[4273.32 --> 4278.12]  just because a lot of people who have been spending a lot of time doing security have not necessarily
[4278.12 --> 4284.76]  been spending much time trying to make good software so um when when we when kind of egypt and
[4284.76 --> 4289.08]  i have these kinds of conversations about this kind of thing um we kind of ask ourselves you know what
[4289.08 --> 4293.48]  can we do to help bridge that gap and help get some of these people who are sort of security inclined
[4294.04 --> 4299.40]  thinking more in terms of good software practices so we've um we've got a pretty extensive set of things
[4299.40 --> 4304.04]  that someone's going to need to do in order to do a pull request um onto the framework it'll be
[4304.04 --> 4307.96]  different if it's purely just a meta splite module you know a piece of content um then if they're
[4307.96 --> 4312.92]  actually trying to hack on like the core of the of the framework itself there'll be different levels
[4312.92 --> 4318.36]  of sort of requirement we have a lot of um like sort of you need to provide external verification steps
[4318.36 --> 4323.64]  um potentially hopefully provide like a way to acquire a piece of software that that may be vulnerable to
[4323.64 --> 4328.60]  this or that you could use to to verify it um you know but especially in offensive security you have the
[4328.60 --> 4332.92]  challenge of like you know do i even have access to the thing that you're giving me a an exploit for
[4332.92 --> 4336.92]  right like is it is it some insanely expensive piece of like enterprise software that we're just
[4336.92 --> 4343.96]  not gonna be able to put into one of our labs um etc etc but i i do think that as as security um
[4343.96 --> 4349.88]  information security becomes much more of a of a thing outside of a cloister um and it's much more
[4349.88 --> 4353.64]  prevalent and these these big breaches that constantly happen you know and the president getting up there
[4353.64 --> 4358.52]  talking about it etc it kind of comes to the fore a little bit more you'll start to see
[4359.24 --> 4363.24]  um developers thinking a little bit more holistically and thinking a little bit more in terms of those
[4363.24 --> 4367.16]  those types of projects and then naturally i think the proclivity of developers the things they want
[4367.16 --> 4372.04]  to spend their time on outside of work you know that sort of classic direction that people move into
[4372.04 --> 4377.16]  to try to say what am i going to spend my open source contribution time doing um we really hope
[4377.16 --> 4381.24]  to kind of position ourselves to benefit from that that sort of trend over time you know i do think
[4381.24 --> 4384.68]  there's some convergence there but maybe i'm just a closet optimist yeah
[4384.68 --> 4393.24]  yeah speaking of that last point um you know something that's been long a tradition of uh info
[4393.24 --> 4399.80]  security folks is the you know capture the flags um i'm assuming that still goes on i used to do that
[4399.80 --> 4406.20]  back in college it was lots of fun and um it seems like recently there's been kind of like official ones
[4406.20 --> 4413.64]  put on like by stripe and um perhaps a few other where a company will host a ctf and whether those
[4413.64 --> 4421.48]  are you know legit vulnerabilities or you know hard or easy or whatever they do spur interest uh and
[4421.48 --> 4428.84]  they kind of bring ideas around uh secure practices to a larger group of people than the ones who are
[4428.84 --> 4435.00]  already doing it what are your thoughts on on those type of activities i think you're completely right
[4435.00 --> 4441.88]  about that i mean i don't really do ctf but um my understanding is that the average ctf is significantly
[4441.88 --> 4445.72]  harder than the average pin test engagement in terms of just sort of being an intellectual challenge
[4445.72 --> 4450.76]  um that makes sense actually yeah getting somebody actually thought about like designing a way in as
[4450.76 --> 4456.20]  opposed to just your typical open ftp server right right exactly and the thing that you're supposed
[4456.20 --> 4462.76]  to do is significantly more difficult right i mean right or like in the case of um you know of defcon
[4462.76 --> 4468.52]  like it's kind of the world series or super bowl or whatever your sports metaphor is of of ctf and
[4468.52 --> 4473.64]  you're really what actually what you end up doing is you know reversing binary software like you know live
[4474.28 --> 4480.04]  right so um it's it's not these i think that that you're absolutely right though that that that will
[4480.04 --> 4485.48]  probably just as sort of a fun intellectual challenge um could provide kind of a way in
[4485.48 --> 4490.20]  you know what i mean i think that the challenge to security practitioners to information security people
[4490.20 --> 4497.72]  now is to um kind of realize where their um where their jargon is and where their kind of collected
[4498.52 --> 4502.44]  um sort of hidden knowledge is and this is the knowledge that they assume amongst people they talk to
[4503.00 --> 4507.88]  and and realize that they might be talking to a software person who's an extraordinarily adept creator of
[4507.88 --> 4514.52]  software and really doesn't know the security landscape but given the right kind of particular
[4514.52 --> 4519.80]  pieces of knowledge um could really be somebody who's who's a benefit to to the information security
[4519.80 --> 4524.92]  world um i think that's kind of the attitude that egypt and i both approach it with is that
[4524.92 --> 4530.20]  there's just a lot of latent capability out there so um yeah i think we've you know we've kicked
[4530.20 --> 4534.84]  around ideas for years about how can kind of how could we get more people who are more software
[4534.84 --> 4539.96]  oriented um you know thinking in terms of security and really frankly people who are security people
[4539.96 --> 4543.56]  thinking a little bit more in terms of good software practices i think there's definitely
[4543.56 --> 4547.48]  an opportunity for people to kind of meet in the middle on that well hopefully here the change log we
[4547.48 --> 4552.04]  can help facilitate such things i think even just having a conversation around it brings up
[4552.92 --> 4559.24]  people thinking about such topics so hopefully we'll have more gosh can i say synergies and get away with it
[4559.24 --> 4563.96]  it sometimes you can sometimes i think i just did i think i just sometimes it's the word you need
[4564.68 --> 4570.20]  all right well i think it's time for our closing questions so uh y'all know the drill i'm gonna start
[4570.20 --> 4578.52]  with egypt and ask you who is your programming hero um i think my hero my programming hero is is a former
[4578.52 --> 4586.44]  co-worker named michael milvich who was just amazing in his in his breadth of knowledge he knew a little bit
[4586.44 --> 4595.88]  about everything um from from how compilers work at the base fundamental levels to uh you know the python
[4597.32 --> 4607.88]  vm to uh everything basically um and what what really made him special to me as a colleague um was
[4607.88 --> 4615.96]  that his depth was at least as impressive as his breadth so he knew a lot about everything and that was
[4615.96 --> 4622.92]  really inspiring to me and it got me um it got me looking into a lot more things and and and really
[4622.92 --> 4629.40]  challenging myself to to be a better programmer awesome trevor how about yourself yeah i've i've
[4629.40 --> 4633.64]  been spending so much time in go in the last year and i've been watching kind of all this sort of
[4633.64 --> 4639.00]  constant controversy of people being like oh it doesn't have my favorite thing in it or whatever um and
[4639.00 --> 4644.20]  i've been pretty severely impressed with uh rob pike you know who's um kind of a legend in the programming
[4644.20 --> 4649.80]  world but um you know this this whole idea that like there could be a much better language we could
[4649.80 --> 4655.00]  go back to some of our our basic principles and say look at these these old principles from from c and
[4655.00 --> 4659.64]  from some early unix programming and say you know these there's some really great ideas here there are
[4659.64 --> 4666.84]  some some some fundamentals and if we keep our language very small and if we really um sort of
[4667.40 --> 4672.36]  chart a particular course and and not waiver from that course and not kind of like bring in every idea that
[4672.36 --> 4677.00]  that everyone's ever had um we'll be making something kind of interesting i i'm always a big
[4677.00 --> 4682.52]  fan of the idea of creativity within constraints and it's it's been interesting to watch um this guy
[4682.52 --> 4686.36]  who's you know i doubt he ever really considered himself somebody who's going to become like this
[4686.92 --> 4692.20]  um you know person who is sort of kind of the the high priest of a programming language in the same
[4692.20 --> 4698.12]  way that he has but it's been it's been nice to watch um the way that the sort of the go authors have
[4698.12 --> 4704.68]  been um very i would say very generous with their time and very um interested in the reactions that
[4704.68 --> 4709.56]  people have to the things that they've built but they also kind of maintain um that you know they've
[4709.56 --> 4713.40]  got a vision for what this thing can be and they they kind of stick to that and it's been it's been
[4713.40 --> 4718.68]  cool to watch i'm also um like kind of in awe of yehuda cats and i know a lot of people probably
[4718.68 --> 4725.00]  mentioned him on this program but um the guy like just makes things that need to exist and as as a sort of
[4725.00 --> 4728.84]  a practically minded person um i really really appreciate that i remember rails dependency
[4728.84 --> 4733.56]  management before bundler um you know i i really appreciated a couple times i needed to write a cli
[4733.56 --> 4738.12]  tool in ruby really appreciated the existence of thor um you know yeah i love that somebody like you
[4738.12 --> 4742.28]  know sits down he's going to write something in rust and he's like well i need bundler for rust so i
[4742.28 --> 4746.36]  guess i'll just make it and that that kind of attitude you know somebody spends all the time
[4746.36 --> 4750.52]  dealing with open source stuff that kind of attitude is just it's like the ultimate yak shave right
[4750.52 --> 4756.44]  like i need a i'm going to write something in rust i need a dependency manager and you know months
[4756.44 --> 4762.52]  months yeah here comes the cargo here we are all exactly right very cool hats off okay last one we're
[4762.52 --> 4768.12]  running low on time here is what would you be doing if you weren't working on metasploit and egypt
[4768.12 --> 4776.20]  we'll start with you i would probably be penetration testing networks um breaking into stuff stealing
[4776.20 --> 4782.68]  things uh security has always been my passion and programming has been the means to that um and if
[4782.68 --> 4789.88]  not penetration testing of networks i would i would be uh reverse engineering binaries um staring at
[4789.88 --> 4794.36]  debuggers and disassemblers all day long and in fact that's what i was doing before i came to the
[4794.36 --> 4802.44]  ministry team so elite you did absolutely love it how about you trevor i've always liked early
[4802.44 --> 4808.52]  stage startups um i like sort of chaos um and the and the interesting opportunities that come out of
[4808.52 --> 4814.52]  it so i would probably be um off doing something on my own probably in like agricultural tech i'm
[4814.52 --> 4820.52]  really fascinated by the intersection of like um maker technologies and um the whole sort of like
[4820.52 --> 4824.04]  i don't even know if you can call it the food movement but i guess kind of the food movement so
[4824.60 --> 4828.76]  something in something in that area just speaking to that briefly uh i actually listened to a great
[4828.76 --> 4836.52]  podcast this morning um on econ talk have you ever heard of econ talk it's a economics podcast out of
[4836.52 --> 4843.80]  stanford i believe um i'm a bit of an economy nerd from time to time uh all about ag tech and kind of
[4843.80 --> 4850.52]  the return of nature that's been happening uh i'll link that up in the show notes it's pretty interesting
[4850.52 --> 4857.56]  to see the results of some of the advancements that we've made recently in ag tech very cool guys man
[4857.56 --> 4861.64]  this was such a fun time i could probably talk to y'all for hours about these things mostly because
[4861.64 --> 4865.48]  i'm so rusty that i'll just sit here and say is this still a thing is that still a thing
[4866.52 --> 4871.48]  as you as you can tell by now well come down to austin hang out it might have to happen it might have
[4871.48 --> 4879.32]  to happen um where can we find you so of metasploit.com um on the internets what's a good way to get a
[4879.32 --> 4891.24]  hold of you well i'm egypt egyp7 on twitter um we also maintain pound metasploit on freenode and i'm in there all the time
[4891.24 --> 4901.00]  and tur yeah same for me i'm uh trev rosen on uh twitter and github both um i uh i mock uh politicians
[4901.00 --> 4907.16]  frequently on my twitter account so it's not really my professional thing but um there it is i also talk about
[4907.16 --> 4912.92]  code so so if you're pretty politically aligned you may not want to follow trevor on twitter because
[4912.92 --> 4919.56]  he may make you angry it could be yeah or even if it's not politics it just might just might happen
[4920.36 --> 4925.48]  very cool well thank you guys again uh for joining me today i also want to thank our awesome sponsors
[4925.48 --> 4932.92]  for this episode that is code ship top towel harvest and transload it we appreciate your support
[4932.92 --> 4937.64]  and if you love the changelog we would love if you would help support those companies as well
[4938.44 --> 4944.28]  give a little bit of a tease to upcoming shows here um in case you have not hit the subscribe button
[4944.28 --> 4950.76]  quite yet we have the hybrid group coming on to talk about cylon js gobot and the internet of things
[4952.20 --> 4959.24]  we have we have rethink db uh follow up with the earlier interview we had with the cto there as well as
[4959.24 --> 4967.32]  saranya barak with code newbie upcoming all sorts of fun stuff make sure you subscribe and with that
[4967.32 --> 4980.68]  until next time let's say goodbye goodbye goodbye
[4989.24 --> 4996.74]  you
[5019.24 --> 5049.22]  Thank you.
[5049.24 --> 5079.22]  Thank you.
[5079.24 --> 5109.22]  Thank you.
[5109.24 --> 5139.22]  Thank you.
[5139.24 --> 5169.22]  Thank you.
[5169.24 --> 5199.22]  Thank you.
[5199.24 --> 5229.22]  Thank you.
[5229.24 --> 5259.22]  Thank you.
[5259.24 --> 5289.22]  Thank you.
[5289.24 --> 5319.22]  Thank you.
[5319.24 --> 5349.22]  Thank you.
[5349.24 --> 5379.22]  Thank you.
[5379.24 --> 5409.22]  Thank you.
[5409.24 --> 5439.22]  Thank you.
[5439.24 --> 5469.22]  Thank you.
[5469.24 --> 5499.22]  Thank you.
[5499.24 --> 5529.22]  Thank you.
[5529.24 --> 5559.22]  Thank you.
[5559.24 --> 5589.22]  Thank you.
[5589.24 --> 5619.22]  Thank you.
[5619.24 --> 5649.22]  Thank you.
[5649.24 --> 5679.22]  Thank you.
[5679.24 --> 5709.22]  Thank you.
