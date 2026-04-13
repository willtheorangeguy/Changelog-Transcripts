[0.00 --> 17.32]  let's do it it's go time welcome to go time your source for wide-ranging discussions from all
[17.32 --> 25.38]  around the go community find us on the web at gotime.fm on the fediverse at gotime at changelog.social
[25.38 --> 34.80]  and on x at gotime.fm big thanks to our partners at fly.io the home of changelog.com fly transforms
[34.80 --> 40.38]  containers into micro vms that run on their hardware in 30 plus regions on six continents
[40.38 --> 47.88]  so you can launch your app near your users learn more at fly.io okay here we go
[55.38 --> 66.24]  hello and welcome to another wonderful episode of go time i'm your host angelica hill and in this
[66.24 --> 71.84]  episode we're going to delve into the exciting world of go capture the flag my wonderful guests
[71.84 --> 77.12]  are going to share their experience organizing this wonderful game and overseeing it as they
[77.12 --> 83.72]  implement it for the first time at go for con 2023 last year for those of you who don't know capture
[83.72 --> 90.90]  the flag events involve teams vying for supremacy as they strive to gather digital flags presented as
[90.90 --> 96.84]  strings and successfully submit them to the competition organizers it's a dynamic competition
[96.84 --> 103.44]  where the team who amasses the highest amount of points is victorious so it's essentially a thrilling
[103.44 --> 110.84]  kind of scavenger hunt for nuts so join us today as we unravel the intricacies and the excitement
[110.84 --> 118.18]  surrounding this wonderful gaming experience and we are extremely lucky to have not one but both of
[118.18 --> 125.26]  the organizers of go capture the flag with us today um so our first wonderful guest is neil s primer
[125.26 --> 133.20]  who is a principal architect at reoc a boutique cloud and data consulting firm he lives in the san francisco
[133.20 --> 141.02]  bay area with his wife three children and a multitude of cats which i'm told the correct noun for that is
[141.02 --> 147.16]  a cloud of cats is that is that right neil that's what my research has found uh i can't back it up myself
[147.16 --> 152.54]  and i certainly don't refer to them that way well welcome to the show how are you today i'm doing
[152.54 --> 160.72]  fantastic awesome excited to dive in our next wonderful guest is benji vestiby who is the ceo of code
[160.72 --> 168.10]  pro which is a cyber security and software consulting based firm in north carolina where he lives with
[168.10 --> 175.58]  his wife his daughter two dogs and two cats and he says he's not cool enough to have a clowder of cats
[175.58 --> 180.24]  so he's gonna have to have the two dogs and two cats maybe you need to up the cat number to get that
[180.24 --> 185.98]  classification uh his background is in computer science which eventually led him to information
[185.98 --> 192.50]  security and everything from deep packet inspection to application security to industrial control
[192.50 --> 199.00]  system security how you doing today benji i'm doing pretty good awesome excited to dive in i'm not sure
[199.00 --> 205.90]  my wife will let me get a third cat really yeah oh well one can hope to aspire to the clowder level
[205.90 --> 214.12]  that neil has so we're going to start with the very basics what is go capture the flag so uh capture the
[214.12 --> 220.42]  flags are a type of competition where teams compete to get the most points by retrieving digital flags
[220.42 --> 225.84]  in the form of strengths and submitting them to the competition organizers yeah the easiest way i found
[225.84 --> 231.00]  to explain uh the capture the flag to people is that it's essentially a scavenger hunt for nerds
[231.00 --> 238.08]  the goal is to code or hack a given challenge in order to expose a flag which in the majority of cases
[238.08 --> 243.94]  for the one that we developed last year was a uuid v4 that was surrounded by curly brackets and
[243.94 --> 250.26]  prefixed with gc23 there were several flags that that didn't follow that pattern where uh we use some
[250.26 --> 256.46]  um you know hidden flags on the on the badges or on the hotel key cards things like that but uh for the
[256.46 --> 263.48]  majority of cases it was a uuid v4 and how did this kind of come together well i think we'll we'll go from the
[263.48 --> 269.16]  start and bring through till kind of where we're going after this so how did this come about how
[269.16 --> 275.94]  did the idea of creating a go capture the flag and bringing it to go for corn happen yeah so um
[275.94 --> 282.36]  the organizers of go for con wanted to um have more community events last year and having a background
[282.36 --> 287.88]  in security i proposed a capture the flag uh this is something that you normally see at security events
[287.88 --> 293.86]  and you know it does it's not exclusive to the security community and uh engineers enjoy puzzles
[293.86 --> 300.44]  so after you know figuring out you know rough amount of effort and uh and time involved we made
[300.44 --> 304.26]  the decision to move forward and started looking for a team of people uh neil joined me pretty early
[304.26 --> 312.02]  on and um we decided to co-host the event yeah as soon as benji asked me to join i was all in cts are
[312.02 --> 318.84]  something i've been interested in since sometime in the late 90s to early 2000s i remember watching
[318.84 --> 324.82]  coverage of some of the earlier def cons on zd tv and tech tv and just being really drawn into that
[324.82 --> 330.36]  idea of gamifying your own education you know there's more to it than just the ctfs but at least
[330.36 --> 335.04]  to you know neil in high school the idea of building improving your skills through doing something hands-on
[335.04 --> 341.06]  was really appealing as my actual career developed i had actually never expected to get the opportunity
[341.06 --> 346.34]  to participate in one my roles have been far enough away from security as a primary focus
[346.34 --> 351.16]  that didn't make sense for me to attend security conferences and the conferences i did attend
[351.16 --> 356.40]  didn't have an official ctf as part of the programming at least until this year so you've
[356.40 --> 362.16]  kind of talked about it being not specific to the security community but something a question that
[362.16 --> 366.86]  kind of just popped to mind was am i right in assuming that this is something that is more prevalent
[366.86 --> 373.64]  within the security community i'm kind of interested as to why that might be and is the nature of how
[373.64 --> 379.86]  you build and how you create these puzzles innately security based i'm kind of interested in that kind
[379.86 --> 387.44]  of interaction there between if there is even one yeah so security as a whole like you know if we take
[387.44 --> 392.94]  and look at the breadth of the security community and everything that it entails the scope is fairly large
[392.94 --> 398.20]  you have you know like if we just take a broad look you have infrastructure security you have
[398.20 --> 403.34]  application security you have network security you have i mean you start breaking down into smaller
[403.34 --> 408.54]  pieces then you start looking at okay well what are the subcategories of infrastructure and network
[408.54 --> 414.32]  and application and how are those things intertwined i mean you start going down the rabbit hole of
[414.32 --> 420.30]  okay we've got infrastructure that's hosting virtual machines which have containers running on them that are
[420.30 --> 425.80]  hosting kubernetes clusters or not well not containers running the kubernetes clusters but vms that are
[425.80 --> 431.16]  running kubernetes clusters which are then hosting pods that are running containers that are you know
[431.16 --> 435.94]  have that these mesh networks inside of them you know and each of these different layers has a different
[435.94 --> 442.04]  layer of security you know you've got networks and networks and networks you have all of these different
[442.04 --> 448.28]  levels of different security and so what's happened is you have this really really large
[448.28 --> 456.48]  scope of necessary essentially training and knowledge that has become necessary to know in the security community
[456.48 --> 462.80]  and one of the ways the security community has gone about trying to solve this problem of
[462.80 --> 470.78]  a lack of knowledge or training has been to develop these capture the flag events where people can
[470.78 --> 477.46]  challenge themselves to learn new skills in a more engaging way than just sitting down in a classroom which
[477.46 --> 484.00]  most people in the security community are not great at and allows them to engage more with the actual
[484.00 --> 490.36]  knowledge and do it in a more real world scenario where they get to actually attempt to you know
[490.36 --> 498.50]  attack a system or you know pivot into a network or you know use a multi-layered vector in order to
[498.50 --> 504.50]  actually like infiltrate a specific application or something like that it's not specific to security because
[504.50 --> 510.22]  the idea is just problem solving it's just using a different mentality to problem solve and in fact a
[510.22 --> 516.40]  security expert you know dealing with something like a capture the flag actually falls more into
[516.40 --> 523.42]  the mindset of somebody that you would normally meet in like QA you know somebody who is like their
[523.42 --> 529.42]  primary role is to actually break an application if you start comparing that to security and then if you
[529.42 --> 535.14]  start looking at like challenges or problem solving type events like this you know the ACM has actually
[535.14 --> 540.04]  had or the Association of Computing Machinery has had this for a long time you know through universities
[540.04 --> 545.64]  and things like that where they'll actually host these events and you have students competing against each
[545.64 --> 552.82]  other for you know in competitions and in academia solving computer science-based challenges for awards and so it's not
[552.82 --> 558.32]  that it's a new idea but you know the security community has kind of really popularized it
[558.32 --> 567.04]  and made it more of a generalized conference type you know event and I think it really pairs well with
[567.04 --> 573.40]  the software community. It's awesome. So before we dive into specifically what you all made happen at
[573.40 --> 580.08]  Go4Con this year I'd love to hear a little bit about your and it doesn't have to take long but I'm interested
[580.08 --> 587.06]  to hear kind of for you both how you first kind of came into either participating in or have you
[587.06 --> 593.44]  organized a CTF before Go4Con like have you used it as a learning tool in your own growth and development
[593.44 --> 599.36]  kind of interested to hear your personal I guess stories and experience prior to Go4Con
[599.36 --> 605.84]  with these kind of either competitive spaces or learning tools. Unfortunately I hadn't had the opportunity
[605.84 --> 612.02]  to participate in a real capture the flag prior to this year I did have some experience with similar
[612.02 --> 616.64]  challenge like series of challenges that you need to progress through I've had employers that use that
[616.64 --> 623.72]  as kind of a a test for advancement in certain times but an actual real full competition challenge I
[623.72 --> 628.30]  hadn't had the exposure to directly before. So exciting that's awesome that you got to do it for the
[628.30 --> 632.84]  first time there at Go4Con this year. How about you Benji? Yeah so I've been to a few different
[632.84 --> 637.64]  conferences where I've been able to take part in a capture the flag my first real introduction was
[637.64 --> 642.74]  actually at a company off-site when I was at Contrast Security and it was actually led by one
[642.74 --> 648.04]  of the organizers of KernelCon which is a security conference based in Omaha and he his name is Adam
[648.04 --> 652.98]  Shaw and he actually is the one that helped kind of guide us last year he was kind of our mentor actually
[652.98 --> 658.00]  in the process and he's actually who I had originally approached and said hey you know what does it
[658.00 --> 663.10]  normally look like to build one of these and because he's done quite a few of them so he he
[663.10 --> 667.58]  helped kind of guide the initial parts of the process and gave us direction and he had built
[667.58 --> 674.16]  this one at Contrast and it was something that they did as part of a company off-site the very first
[674.16 --> 679.10]  year I started with them. After that I went and had done some other ones at other security conferences
[679.10 --> 682.38]  and things like that and one of the things that I found most frustrating about it is that
[682.38 --> 689.34]  as a software engineer it required a lot of very niche security knowledge that you don't necessarily
[689.34 --> 695.80]  normally have. Now me specifically coming into it I have a security background right like before
[695.80 --> 700.82]  Contrast I was in an information security team working as a security engineer building out security
[700.82 --> 705.58]  tooling at Symantec and so I had a fair amount of that you know with the training and everything that
[705.58 --> 710.70]  I had from previous experience and even then it was difficult for me to participate in this
[710.70 --> 716.80]  capture the flag event at Contrast because it required very specific knowledge in certain areas
[716.80 --> 724.54]  of security. So what I what I wanted for the one that we built was to have it be more approachable
[724.54 --> 731.12]  for people who had never done one to be able to actually like come in the door and try it out and
[731.12 --> 736.50]  not have to feel intimidated and actually be able to make progress in the event without it being
[736.50 --> 740.56]  something where it's like you just want to throw your computer out the window and walk out of the
[740.56 --> 746.56]  conference you know as soon as you even just look at the first challenge. Great which kind of goes into
[746.56 --> 753.20]  I would love to kind of talk a little bit now off the back of what Benji was talking about as to how
[753.20 --> 759.68]  specifically did differentiate Go4Con CTF from the more traditional CTFs and maybe think through some
[759.68 --> 765.46]  of these pain points that Benji has flagged around needing that niche knowledge. Yeah like we've said a couple
[765.46 --> 771.04]  of times now traditionally capture the flags started in security conferences and have been played at
[771.04 --> 775.12]  security conferences you know there's there's actually a couple of different styles of play even
[775.12 --> 781.00]  within capture the flags. What we chose was called a jeopardy style where you have to kind of receive
[781.00 --> 786.28]  your challenges from the organizers and take each of those challenges on its own but there's other
[786.28 --> 791.00]  types such as an attack defense style where you have a red team and a blue team and one of them
[791.00 --> 798.00]  attacks infrastructure or or flags owned by the other team. That being said those competitions
[798.00 --> 803.90]  typically focus primarily on those cyber security skills and since Go4Con isn't a security conference
[803.90 --> 809.16]  we wanted to make sure that the challenges didn't require any security knowledge at all to solve
[809.16 --> 815.92]  but could be solved through the application of code. One of the examples is we had the raging radstorm
[815.92 --> 820.98]  challenge where contestants had to connect to a web socket endpoint and quickly solve math
[820.98 --> 827.24]  problems that grew in length as they progressed until they finally got the flag. In order to make
[827.24 --> 832.06]  sure that they were solving that programmatically the backend server was awarding points for each solve
[832.06 --> 837.50]  but then also taking points away for the time it took in between solves so if you were trying to do it
[837.50 --> 842.64]  all by hand you could get to a certain point but then the points just start decaying too fast for you
[842.64 --> 847.76]  to catch up. Finally we wanted to make some challenges that didn't require any specialized knowledge
[847.76 --> 854.14]  to all to complete mostly just there to be fun mini games. The terminal text twister challenge is one
[854.14 --> 860.50]  that is kind of in that category. We built a web app that duplicates the terminal hacking game from the
[860.50 --> 866.28]  Fallout series and for anyone who hasn't played Fallout that mini game is supposed to simulate evaluating
[866.28 --> 871.50]  a memory dump with a number of plain text strings in it where clicking the right string gives you access
[871.50 --> 877.10]  to the system like you're kind of picking the password from a memory dump. For our challenge we incorporated
[877.10 --> 882.22]  a series of these memory dumps the players had to progress through to get to the flag. There was also
[882.22 --> 886.38]  a hidden bonus flag available during this challenge for players who were paying enough attention to
[886.38 --> 891.92]  to their solves. So I don't know Benji whether I would love to hear a little bit more about some of the
[891.92 --> 899.06]  other challenges or kind of any other ways in which this differentiated or you intentionally made it
[899.06 --> 904.30]  different from those prior capture the flags that you kind of were chatting about previously having
[904.30 --> 909.16]  done them before. So it was important to have challenges that that would push participants to
[909.16 --> 913.50]  learn new skills. So there were some there were some fun ones there was one that Neil had implemented
[913.50 --> 918.08]  that was a one-time pad puzzle and I think we're planning on using that one as a as an example going into
[918.08 --> 922.70]  this next year that will publish the solution I think for that one as we're getting ready for
[922.70 --> 927.94]  GopherCon 24 essentially as a write-up to say hey you know if you're looking at trying out the
[927.94 --> 932.62]  capture the flag this next year this is something you should definitely read through for the mindset
[932.62 --> 937.06]  of how you should approach puzzles in this event. The challenges were set up in a way that you know
[937.06 --> 941.18]  some of them were security related and some of them were just challenging in general. We had some really
[941.18 --> 945.50]  interesting ones that actually leveraged some there was one specifically that was actually not
[945.50 --> 949.14]  implemented by Neil or I there were there were several others that contributed to the capture
[949.14 --> 954.60]  the flag. One of them was actually exploiting a vulnerability that was in one of the go open
[954.60 --> 959.52]  source libraries. Not the go standard library was actually a third-party package but that was a
[959.52 --> 963.98]  that was a quite an enjoyable one. There was one that I was really sad nobody got that was a it was a
[963.98 --> 970.94]  multi-phase challenge where you were able to get access to an ssh key and and use that shell into a
[970.94 --> 976.58]  server but nobody actually got to that one. But it seems like you know based on the final statistics
[976.58 --> 982.46]  I think we did a really good job of having a solid distribution of fairly simple challenges to fairly
[982.46 --> 987.38]  complex challenges. I think one of the one of the really interesting things that we saw when we first
[987.38 --> 993.06]  got started that I think that we're going to probably work around this year as we start developing
[993.06 --> 997.56]  out the event this year is that everybody started when they pulled up the site where they got the
[997.56 --> 1001.82]  challenges from everybody started from the top and went down so they all started on the same challenge
[1001.82 --> 1006.14]  and which I thought was kind of funny because they were they were broken into different categories
[1006.14 --> 1011.14]  with different levels and you know they were randomly put in there so they weren't in any
[1011.14 --> 1015.90]  particular order. So everybody seemed to start from top down even though there were other challenges
[1015.90 --> 1020.78]  and other categories that would have been easier to solve if it were me or you know if I had any
[1020.78 --> 1025.64]  recommendation anybody would be you know if you get stuck or you start feeling like you're frustrated
[1025.64 --> 1030.18]  with a with a puzzle move on to another one like you know just randomly pick start going through
[1030.18 --> 1035.82]  them find the puzzles and and or sorry find the flags and move on to the next puzzle and then go loop
[1035.82 --> 1040.24]  back to the ones you had difficulty with you know go solve all the easy ones first get as many flags as
[1040.24 --> 1045.02]  you can and then and then loop back to the hard ones mostly because like we you know we want it to be
[1045.02 --> 1049.64]  something where you feel like you've made progress we want it to be something where you've you feel like
[1049.64 --> 1054.40]  you learned at the end of the day and that you had fun that it's not just something where you know
[1054.40 --> 1059.26]  you're frustrated or or anything like that and then also you know look for a team of people who
[1059.26 --> 1064.92]  are are interested in solving challenges with you. So I'm kind of interested a little bit in the
[1064.92 --> 1070.68]  process of actually like picking what challenges are you going to create you talk a lot about making
[1070.68 --> 1075.42]  sure people are learning but also making it accessible to multiple levels. I would love it if you could just
[1075.42 --> 1080.58]  take a second either one of you both of you to chat a little bit about that process of deciding
[1080.58 --> 1084.66]  we're going to have this brainstorm perhaps like we have all these challenges that we could do which
[1084.66 --> 1091.06]  ones actually make it. Let's use go for con last year. How was that decision process to make sure it
[1091.06 --> 1095.44]  was kind of all the things you've said accessible people are learning you have things that are going
[1095.44 --> 1102.28]  to challenge your levels while keeping it interesting? Yeah so this one's this one was kind of
[1102.28 --> 1108.16]  interesting. So the the idea to do the capture the flag last year was kind of last minute. I think we had
[1108.16 --> 1114.10]  like I think a total time between deciding we were going to do this and actually the event actually
[1114.10 --> 1121.48]  taking place was less than two months of time. I think Neil and I first started putting code down
[1121.48 --> 1128.38]  with less than 60 days to the event and we were able to pull in a couple of others who helped contribute
[1128.38 --> 1133.76]  to some of the code and then there were some people that helped run it on site and so kind of what ended
[1133.76 --> 1138.30]  up happening was you know we ended up having a theme we had the fallout theme. I pulled a number
[1138.30 --> 1143.56]  of challenge ideas out of like previous capture the flags that I had been part of. One of the more
[1143.56 --> 1148.40]  difficult ones had come out of that one that I did at Contrast Security that everybody really hated
[1148.40 --> 1155.18]  and the one that Neil developed the one one time pad or what was that one called Neil?
[1155.18 --> 1160.88]  The Minutemen Missive. The Minutemen Missive that's the one. Yeah yeah yeah. The Minutemen
[1160.88 --> 1166.52]  Missive was the one that everybody hated. I think all of the teams got stuck on that one for almost
[1166.52 --> 1172.06]  an entire day for the teams that actually got to it. But yeah and I mean you know it was one of those
[1172.06 --> 1175.98]  things where it's like hey this could be interesting or fun. I kind of took you know initially I was
[1175.98 --> 1180.70]  like hey I took different categories of like security vulnerabilities. I was I had a whole list of them. I was
[1180.70 --> 1187.00]  like hey even we've got application security. We have supply chain security. We have you know web app
[1187.00 --> 1193.90]  network security things like that. The radio behind me was filled with raspberry pies. We had an on-site
[1193.90 --> 1199.26]  network that went live I think on the on the first day of the conference. I didn't have it live on
[1199.26 --> 1204.52]  community day but it was live on the on the first day of the conference. You had to actually you know in
[1204.52 --> 1209.38]  order to get into that network you had to actually go through a packet capture and find the password for
[1209.38 --> 1213.78]  it. And then you were able to attack some of the some of the raspberry pies inside of that network.
[1214.46 --> 1218.22]  So we you know we initially we had a set of categories that were they were broken out into
[1218.22 --> 1223.18]  and then Neil and I were just kind of hitting up each other on slack with new ideas as we would go.
[1223.54 --> 1228.42]  I mean originally the plan was we were going to because of the lack of time the original plan was
[1228.42 --> 1233.78]  we were just going to have like 10 challenges total. And it was going to be the team that completed all
[1233.78 --> 1240.52]  10 challenges first because what happened is the Adam who was a helping mentor you know said look
[1240.52 --> 1247.04]  you know you have limited amount of time so just do a 10 challenge plan and then the first team to
[1247.04 --> 1252.50]  complete all 10 challenges is the winning team. Normally you would do with a Jeopardy style capture
[1252.50 --> 1258.90]  the flag you would have 40 to 50 challenges and then not every team solves every challenge but most
[1258.90 --> 1265.50]  teams solve most challenges or most challenges are solved by at least one team. And what ended up
[1265.50 --> 1270.92]  happening was Neil and I started hacking away and we ended up with almost 50 challenges or I think
[1270.92 --> 1277.04]  we might have actually exceeded 50. I don't remember the exact numbers. I think we were over 50 flags but a lot
[1277.04 --> 1281.80]  of those were like bonus flags. I think we were somewhere around 40 total challenges.
[1282.30 --> 1287.38]  40 total challenges yeah. And actually the statistics ended up lining up pretty well with that
[1287.38 --> 1293.14]  balance too as far as like you know where the distribution of like number of solves per team
[1293.14 --> 1299.16]  you know how not every team solved every challenge and yeah no it ended up being one of those things
[1299.16 --> 1303.62]  where it ended up being a full capture the flag unexpectedly. The process was just I mean it was
[1303.62 --> 1307.88]  kind of more organic it was like hey this sounds like a fun problem you know can I do this thing.
[1308.48 --> 1313.04]  One of the more interesting ones I think was it wasn't a security challenge per se but like you
[1313.04 --> 1317.94]  could technically consider it as a security challenge is that you know we use the context
[1317.94 --> 1323.16]  and go to share values in like a REST API all the time. We pass around authentication data through
[1323.16 --> 1328.86]  it all the time and one of the challenges I put together I was like you know can I set it up so that
[1328.86 --> 1333.90]  you know with a known key somebody can pull an authentication value out if somebody incorrectly
[1333.90 --> 1339.50]  uses the plugin system can they create a plugin that then dumps the this known key out of context
[1339.50 --> 1344.72]  on a REST endpoint and of course you know they were able to do that and then I was like well what you
[1344.72 --> 1351.06]  know how difficult would it be to do the same thing but actually like use reflection and you know pull
[1351.06 --> 1356.24]  all the values out of the context and find all of the authentication data in that context that
[1356.24 --> 1362.14]  we don't know the key for so I was able to add an extra level of complexity to the problem that
[1362.14 --> 1367.60]  you know they had to actually go and find the hidden keys that were they didn't know the the actual
[1367.60 --> 1372.74]  you know flag value for so you know there were some of them that stretched their people's you know
[1372.74 --> 1377.50]  go knowledge like that one involved the plugin system which most people hadn't used I mean most
[1377.50 --> 1382.96]  people probably shouldn't and then you know there's like this year I mean not to ruin anything for
[1382.96 --> 1387.88]  anybody but I might throw in a tool exec thing we'll see for anybody who's familiar with that
[1387.88 --> 1393.20]  which is probably not a lot but that might be fun start studying up now yeah start studying up now if
[1393.20 --> 1398.32]  you if you know what I'm talking about if you don't know what I'm talking about have fun the work that
[1398.32 --> 1403.26]  I did at contrast so I saw a lot of really interesting like things in the go language that
[1403.26 --> 1409.38]  you should never do and so I got to see a lot of those like intricacies of like the language that I
[1409.38 --> 1414.26]  would not normally have seen and so I could play with some stuff that I I thought would be fun
[1414.26 --> 1420.78]  so I would love to kind of hear a little bit about how it went at go for con this year I mean Neil
[1420.78 --> 1424.78]  it was kind of one of your first as you said experiences organizing and then running
[1424.78 --> 1430.12]  I capture the flag I would love to hear from you like how did how did it go so I mean we we actually
[1430.12 --> 1435.52]  really had kind of high hopes even going into it just because we hadn't seen this at non-security
[1435.52 --> 1442.00]  conferences really but the participation actually exceeded our expectations we had almost 20 percent
[1442.00 --> 1449.38]  of the attendees register and 72 percent participation rate from those who registered we also had a pretty
[1449.38 --> 1455.46]  good response rate for the feedback form just over 15 percent most of our participants were there for
[1455.46 --> 1460.84]  their first go for con ever and about three quarters of them also had never participated in a capture the
[1460.84 --> 1465.88]  five before so this seems to confirm they were pretty close to the mark with what we were aiming
[1465.88 --> 1471.32]  for regarding the approachability of the challenges one thing we did get surprised by was the feelings
[1471.32 --> 1477.76]  around the theme we'd expected reactions somewhere between like meh to like being really excited but
[1477.76 --> 1482.68]  the feedback was a lot more polarized there were a number of people who disliked the theme they hadn't
[1482.68 --> 1487.32]  played the follow games at all and felt like they were at a disadvantage because they didn't pick up on
[1487.32 --> 1494.26]  context clues or we're worried about things just being like hidden in like game lore you know thus
[1494.26 --> 1498.96]  far the overall feedback we received on the theme can be summarized as you know we'd love to see the
[1498.96 --> 1504.44]  theme rotate each year so long as we're able to do it to the same depth I think that we did have a lot
[1504.44 --> 1510.38]  of depth to the fallout theme which was I think really able to help shape a lot of those challenges in a
[1510.38 --> 1515.32]  way that they would have felt more generic without one other thing that we were well aware of but that the
[1515.32 --> 1519.30]  feedback confirmed was that the hints for the challenges were kind of of inconsistent quality
[1519.30 --> 1524.40]  particularly in regards to the cryptography challenges you know bringing it back to that
[1524.40 --> 1529.08]  one-time pad we're hoping that for next year we're going to be able to incorporate some level of like
[1529.08 --> 1533.80]  contextual hints that will allow players to know which hints will actually help them instead of giving
[1533.80 --> 1538.36]  them information they've already figured out I'm kind of interested to talk a little bit more about
[1538.36 --> 1545.10]  that kind of theme slash story base slash like having some kind of through line between the
[1545.10 --> 1551.02]  challenges especially given as you as you noted Benji that you kind of should be able to take on
[1551.02 --> 1556.76]  the challenges in kind of any order that you see fit I'm kind of intrigued thinking about the experience
[1556.76 --> 1562.00]  in GoFaCon or just like generally as you think about doing this potentially again or past experience
[1562.00 --> 1569.06]  how important is it to have that kind of like through line overall theme that can tie everything
[1569.06 --> 1574.24]  together yeah so when I talked to Adam originally that was actually his first thing he's like you
[1574.24 --> 1579.32]  have to have a theme it's one of the most important things for having a successful event is to have a
[1579.32 --> 1585.48]  theme that is engaging for the participants otherwise it's not you know it's just a bunch of challenges
[1585.48 --> 1592.06]  with no direction so to what Neil said what's important is that I think that the participants
[1592.06 --> 1599.44]  misunderstood that just because there was a theme they assumed that they had to know about Fallout to
[1599.44 --> 1605.40]  do the challenges and that wasn't the case the challenges while they were themed for Fallout had no
[1605.40 --> 1611.02]  Fallout specific knowledge in them that was required in order to actually solve a challenge it was all very
[1611.02 --> 1615.46]  much like security or Go or programming in general in fact most of the challenges didn't even
[1615.46 --> 1620.28]  require a Go so one thing that is important to make clear though since not everybody who's hearing
[1620.28 --> 1625.94]  this is actually was there for the event when the challenges went live not every challenge was
[1625.94 --> 1632.06]  available in the in the system what it was is actually a list of challenges and each one of those
[1632.06 --> 1637.20]  there were there were some of them that were part of a series of challenges those ones as you would
[1637.20 --> 1643.12]  go through each step would unlock the next step so let's say for example we had one called the
[1643.12 --> 1649.22]  Nuka World challenge Nuka World is this is this area in the in the Fallout game series it's kind of like
[1649.22 --> 1655.46]  a messed up theme park that's based on Disney essentially right and that one was an application
[1655.46 --> 1660.88]  security set of challenges now there were five or six challenges in that set but they would unlock in
[1660.88 --> 1667.16]  sequence so the first challenge was the easier of the five or six but as you progress through that set of
[1667.16 --> 1673.10]  challenges it would unlock each one afterwards so you would have to do the in that specific series you would have to do
[1673.10 --> 1677.80]  the first one and it would unlock the next one but the first one in each of the series all the way down the
[1677.80 --> 1683.42]  the page were available so it's you know at the beginning you know there were maybe 25 available
[1683.42 --> 1688.06]  challenges by the end of it though you know you had 40 50 challenges available to the whole team
[1688.06 --> 1694.18]  assuming they unlocked the the other challenges so it was one of those things were like as you would
[1694.18 --> 1700.20]  progress you would expand the available challenges right the theme though like allows us to
[1700.20 --> 1706.02]  like one of my favorite thing was hiding easter eggs in different parts of the challenges right
[1706.02 --> 1711.28]  like one of the challenges so Fallout if you haven't played the game one of the things about Fallout that's
[1711.28 --> 1717.10]  really quite enjoyable for me is that just because I have a weird sense of humor is that it's based in this
[1717.10 --> 1722.50]  post-apocalyptic world that's kind of like stuck in the 1950s but it's kind of like this demented sense of humor
[1722.50 --> 1728.26]  and so there's this uh if you saw the the trailer that we put out on the GopherCon channel last year
[1728.26 --> 1733.52]  you can kind of see some of this in the uh the actual 1950s footage that is in that trailer from
[1733.52 --> 1740.54]  from here in the states that they showed children about nuclear fallout um that kind of humor is actually
[1740.54 --> 1747.74]  in the game and so I took some of the cartoon clips from the game and actually streamed them inside of
[1747.74 --> 1753.84]  the network that was inside the radio and one of the challenges actually made it to where if you
[1753.84 --> 1760.26]  successfully found that stream inside the radio and viewed it the flag was actually across the bottom
[1760.26 --> 1765.86]  of the broadcast and and you could actually play it it was it was an actual streamed video on an RTSP
[1765.86 --> 1770.42]  stream and it would have sound and everything I was just on on one of the actual systems was just
[1770.42 --> 1776.08]  over an RTSP stream so you know that was kind of a fun iseregi type like this is just fun for me you
[1776.08 --> 1780.98]  you know it was it was a simple network security challenge in the sense of like it required more
[1780.98 --> 1785.94]  security knowledge than software knowledge right you would normally at a security conference you
[1785.94 --> 1791.64]  would network scan you would see hey this port is open it's normally used for this specific protocol
[1791.64 --> 1798.24]  and then you would you know go go view it so it was a little less of the I'm a go you know programmer
[1798.24 --> 1803.28]  I'm a that kind of thing and more of a security challenge but it was fun for me and it was kind of
[1803.28 --> 1808.56]  like a little easter eggy type thing you know this year's theme we'll make an announcement as to that
[1808.56 --> 1814.30]  later on but it's going to be fun we'll have some uh some good easter eggs and and and uh good linking
[1814.30 --> 1820.08]  between challenges on that one I think yeah so it's nice because it creates this cohesion behind
[1820.08 --> 1825.68]  between like challenges that it's not just fun for participants but also it's fun for people building
[1825.68 --> 1831.48]  the challenges right like it keeps us engaged um as well I feel like one of my core questions was
[1831.48 --> 1836.34]  exactly that is are we gonna do this again we obviously we have go for con coming up this
[1836.34 --> 1842.08]  year so I'd love to hear one I think I already know the answer but I need confirmation are you
[1842.08 --> 1847.48]  going to be doing it again this year and if so what are the things you're going to take from from this
[1847.48 --> 1851.10]  last year and what are the things that you're thinking you'll do differently yeah we'll definitely
[1851.10 --> 1856.38]  be bringing the event back next year and we're already planning for next year's event that go for con
[1856.38 --> 1862.54]  2024 we do have some exciting additions and changes for next year that it's a little too early to spoil
[1862.54 --> 1867.76]  right now but definitely expect to hear more about it throughout the time leading up to go for con 2024
[1867.76 --> 1876.24]  and if we want to stay posted where where am I looking to see these these little spoilers keep an eye on
[1876.24 --> 1881.94]  the go for con social twitter uh youtube you know all of the different go for con social accounts
[1881.94 --> 1889.18]  uh slack we have a go for con uh slack channel or sorry an actual capture the flag go for con channel
[1889.18 --> 1894.84]  let's see what did we call that go for con dash ctf and it'll be in the episode notes wherever you're
[1894.84 --> 1900.78]  listening to this podcast yeah I do think we're uh we're planning on changing the name of it this year
[1900.78 --> 1905.84]  like one of the things that Neil and I discussed was that the first two days of the conference we spent
[1905.84 --> 1912.86]  the majority of our time explaining what a ctf or capture the flag was I think I explained it no less
[1912.86 --> 1918.38]  than 60 times on the first day of community day and just more the first day of the conference
[1918.38 --> 1924.48]  Neil you want to tell them what we're thinking yeah so we're actually thinking that you know to better
[1924.48 --> 1931.80]  emphasize what it is that we're trying to do uh as well as like the right mindset for people to come
[1931.80 --> 1938.40]  into it with is we're going to rebrand from capture the flag instead to challenge series the format's
[1938.40 --> 1942.90]  going to remark largely remain the same but we felt that there was definitely some missing clarity
[1942.90 --> 1947.62]  in the capture the flag moniker um some folks actually said they thought it was going to be like
[1947.62 --> 1954.88]  physically taking physical capture flags and capturing them like so you know that's definitely
[1954.88 --> 1960.64]  something we took into consideration when making that discussion for sure I will say when I first heard
[1960.64 --> 1964.78]  about it I was like bringing me back to middle school where is the flag that I have to try and
[1964.78 --> 1970.32]  dodge people to get to yeah and I and I realized that like when I was trying to explain it to um that
[1970.32 --> 1975.94]  first day like even when I tried to reference like a scavenger hunt as an example of what a capture the
[1975.94 --> 1982.70]  flag was even that is still like potentially something that's very cultural in nature right like that
[1982.70 --> 1989.10]  you know and I think that anyone who who didn't grow up here had difficulty like knowing what a capture
[1989.10 --> 1995.38]  the flag was or or you know what a scavenger hunt was and so with a challenge series it kind of like
[1995.38 --> 2001.00]  not only does it like separate it from that very specific like cultural reference it also allows us
[2001.00 --> 2008.20]  to move more away from not not move away from necessarily but gives us more access to a broader
[2008.20 --> 2014.58]  problem space so like it's not just about it was never about just security right like that's not what we
[2014.58 --> 2018.90]  wanted from it it just that's what generally capture the flags are at a security conference
[2018.90 --> 2025.02]  and not all of our challenges were security related the nice thing about calling it a challenge series
[2025.02 --> 2031.40]  is that it allows us to kind of like bridge the gap between I don't know more of the ACM style
[2031.40 --> 2037.92]  you know challenges where we you know like have somebody delete a node from a b plus tree and hash the
[2037.92 --> 2045.86]  data values and that's your flag versus you know go crack a password and it allows for people who have a more
[2045.86 --> 2051.66]  computer science background or more software engineering background to have a more comfortable time
[2051.66 --> 2057.80]  actually attempting a challenge it also allows us to to do things that are more specific to our industry
[2057.80 --> 2065.14]  and our field and encourage people to try new things that are go specific or software specific and
[2065.14 --> 2070.56]  challenge them in new and interesting ways that are not just security related because at the end of
[2070.56 --> 2077.06]  the day it's it's meant to help people try new things and learn new things it's not about like hey
[2077.06 --> 2084.56]  here's this new security thing or you know try this really interesting niche security attack it's really
[2084.56 --> 2089.30]  meant to like engage people in the community to try and you know try something you haven't tried before
[2089.30 --> 2094.50]  you know learn something about go you don't know about or you know maybe maybe you learn a new
[2094.50 --> 2099.42]  algorithm that you've never seen or something like that and I think a lot of the people that that
[2099.42 --> 2103.70]  participated last year I think I don't remember if we had this question on the on the survey Neil but
[2103.70 --> 2108.48]  I think if you asked them they would they would agree that they all learned something in the event
[2108.48 --> 2113.94]  yeah because I think the thing that I found most interesting I'd love to kind of dig in a little
[2113.94 --> 2120.80]  more with you both on is that learning aspect I see how this could be like a fun challenging kind of game
[2120.80 --> 2127.20]  experience a chance to flex different technical muscles or solve problems in different ways I'm
[2127.20 --> 2132.32]  kind of interested to dig a little bit deeper into that kind of learning aspect of it is it
[2132.32 --> 2138.56]  predominantly coming through exposing them to new technologies new approaches to problem solving and
[2138.56 --> 2143.70]  that's what they're learning is there a world in which there might be I don't know hints and clues
[2143.70 --> 2150.16]  for people who perhaps like come into a challenge and they look at it and have no idea what it is
[2150.16 --> 2157.62]  I'm kind of interested in how you strike that balance between challenge and like helping or
[2157.62 --> 2163.72]  facilitating that learning in a way that feels challenging enough to be exciting but not too
[2163.72 --> 2169.10]  challenging that it's like oh I can't do this yeah that was something we we had a little bit of a
[2169.10 --> 2173.58]  discussion about as we were building out these challenges and there's definitely somewhere we
[2173.58 --> 2179.02]  dialed back the difficulty a little bit as we like went through and did testing on them after we started
[2179.02 --> 2185.44]  developing them you know it's kind of hard to know how difficult a challenge is going to be for
[2185.44 --> 2192.24]  someone though because I actually expected that the the one-time pad challenge was going to be
[2192.24 --> 2198.26]  significantly easier for people to solve than it was because it's just one-time pads have been a thing
[2198.26 --> 2204.90]  I've known about for decades because like you know you read spy novels as a kid or something it gets
[2204.90 --> 2209.22]  brought up all the time and you're aware of how it works even if you've never actually implemented it
[2209.22 --> 2216.02]  but just missing that that one piece of knowing how it works makes that challenge infinitely more
[2216.02 --> 2220.26]  difficult and it just didn't cross my mind so then when we started actually digging into it
[2220.26 --> 2226.36]  you know seeing how high of a difficulty that was for people you know we're going to have a lot of
[2226.36 --> 2231.20]  feedback from the people who participated in this year's challenges to help us be a lot better at
[2231.20 --> 2236.38]  understanding that balance going into next year yeah and I think there's a lot that we didn't know
[2236.38 --> 2240.92]  that we didn't know right like to Neil's point like there was a challenge that had to do with a
[2240.92 --> 2245.72]  robots text file last year that I thought was going to be the easiest challenge of the whole thing
[2245.72 --> 2252.38]  like it was it was literally like I expected it to be this is the simplest challenge of the entire event
[2252.38 --> 2259.24]  and I sat there the first day and every team and because it was at the very top of the list it was
[2259.24 --> 2262.92]  the first one that everybody started with and every team struggled with it for the entire day
[2262.92 --> 2268.56]  and I really you know I quickly realized that just because of my background and I know what a
[2268.56 --> 2274.34]  robots text file is and I know to go look there as a security practitioner and and the hints you know
[2274.34 --> 2279.52]  they very much directed people at that people in the community or who have a different background
[2279.52 --> 2283.46]  who don't haven't necessarily worked in front of the development or haven't been in the industry as
[2283.46 --> 2288.90]  long who didn't have a geocity site when they were a teen maybe they didn't know have no to look at a
[2288.90 --> 2294.68]  robot robots.txt file I'm dating myself a little bit there that was a little less intuitive for them
[2294.68 --> 2299.10]  and so it gives you a different perspective from a because I mean essentially at the end of the day
[2299.10 --> 2303.64]  we're kind of like puzzle makers right like that's what we're doing we're we're building puzzles
[2303.64 --> 2308.56]  for others we have complete knowledge of the puzzle though and we don't know what they don't
[2308.56 --> 2313.80]  know and we don't know we don't know about who's going to be playing and so you know Neil had the
[2313.80 --> 2317.74]  idea of sending the the survey out at the end last year and we got a lot of information out of that
[2317.74 --> 2321.52]  and we also have some of the participants from last year who want to help with this year's challenges
[2321.52 --> 2327.58]  and I think that's going to be good to help direct us on a better path to make sure that more people
[2327.58 --> 2334.34]  get enjoyment out of it and I hope that I hope that this year the people who came by and might
[2334.34 --> 2339.72]  have been intimidated by it you know or or didn't know what it was and walked on by give it a try
[2339.72 --> 2344.14]  you know even if it's something where like you know because the cool thing is is like we'll do
[2344.14 --> 2347.68]  exactly what we did this last year we'll have challenges for anybody who solves at least one
[2347.68 --> 2352.94]  of the puzzles so like if you're at gopher con and you come by and even if you just sit down and you
[2352.94 --> 2357.22]  solve it even just one of the puzzles and you know you'll be on the random drawing from one of the
[2357.22 --> 2362.66]  prizes at the closing party but I really hope you know more people try it out this year because it
[2362.66 --> 2367.00]  really is it was really a lot of fun and I think this year's challenges are they're going to be
[2367.00 --> 2372.36]  not broader in scope but like they're gonna go beyond security and they'll be a little bit more
[2372.36 --> 2376.98]  in everybody's wheelhouse a little bit more approachable I think for most most people yeah I
[2376.98 --> 2382.50]  would highly encourage anyone who uh is coming to gopher con this year to check it out as someone who
[2382.50 --> 2387.06]  as a fellow organizer of the conference and was running around like a headless chicken one of
[2387.06 --> 2391.18]  the things that I've said this year is I'm not going to do that because I have to spend at least
[2391.18 --> 2396.90]  one day doing the catch of the flag kind of along those lines and just thinking through people who
[2396.90 --> 2401.52]  maybe will be coming for the first time as you said you had a very high percentage of first time gopher
[2401.52 --> 2408.62]  con attendees and as someone personally who is like a serial like over preparer what are some things
[2408.62 --> 2413.26]  is that like if I want to be super prepped I know it's supposed to challenge me but I would like to
[2413.26 --> 2419.04]  get that pre-knowledge in is there any websites technologies things that I can do to really set
[2419.04 --> 2426.10]  myself up to really enjoy it and and bluntly have the best chance of winning so one thing that we would
[2426.10 --> 2432.24]  really recommend is reading a book called the red team field manual that was actually one of the prizes
[2432.24 --> 2440.10]  we gave away I think three or four copies of last year to to various participants the other is just
[2440.10 --> 2446.80]  ctf101.org I actually use that as a resource when building some of the challenges this year so that's
[2446.80 --> 2451.22]  a definitely good place to start with just understanding a little bit more about how capture
[2451.22 --> 2457.60]  the flags work and how like what some of the mindset that goes into those challenges are yeah and then we
[2457.60 --> 2462.52]  haven't done it yet we'll try and get the blog out for the the one-time pad sometime between now and
[2462.52 --> 2468.00]  and when 2024 gopher con launches I'm not sure where that's going to be at the moment to be honest
[2468.00 --> 2472.44]  and then there's also you know there's a number of youtube tutorials things like that that you can look
[2472.44 --> 2476.22]  up I think there's hack my box is another example of a place you could probably find some training
[2476.22 --> 2482.74]  things like that look it up on on google or whatever don't don't get in trouble though but the red team
[2482.74 --> 2486.58]  field menu is a good a good place to start though like it talks a lot about a lot of tools play around
[2486.58 --> 2491.12]  with some kali linux drop a note in the the ctf channel ask last year's participants there's a lot
[2491.12 --> 2495.94]  of them in there I'm sure that they'd be willing to to share ideas or thoughts you know this year is
[2495.94 --> 2500.00]  going to be a lot more fun I mean not not that last year wasn't a lot of fun this year is going
[2500.00 --> 2504.94]  to be a lot more fun because we're going to bring a lot more challenges so you have more time this year
[2504.94 --> 2512.92]  as well you're not having to rush to get it well I say that now yeah my kind of final question
[2512.92 --> 2519.62]  before I'll kind of turn over to you all in case there's any final closing thoughts is we've kind
[2519.62 --> 2523.18]  of talked a little bit about the types of challenges we've talked about what people can do to prep
[2523.18 --> 2530.46]  but for those who might be either attending go for con for the first time with no software engineering
[2530.46 --> 2536.38]  experience whatsoever are there any actual like baseline requirements I know you all do all you can
[2536.38 --> 2542.30]  to make sure it's as inclusive as possible but for those like true newbies to the space so my first
[2542.30 --> 2547.00]  go conference I hadn't written a line of code in my life it was something where I went to the conference
[2547.00 --> 2551.64]  to just see what this community was about and then I was like oh my gosh I love this let's go now I'm
[2551.64 --> 2558.94]  gonna learn two questions you can choose which flavor to answer one is how can people who have never
[2558.94 --> 2565.00]  written a line of code in their life participate or get some kind of enjoyment or maybe come over and
[2565.00 --> 2570.26]  shadow and just watch it or for those who maybe are just getting into software engineering like goes
[2570.26 --> 2575.50]  their first language potentially are there any like you need to know how to use the terminal like
[2575.50 --> 2581.26]  are there any baseline requirements I just want to make sure like the true newbies have your guidance
[2581.26 --> 2585.46]  we definitely made an effort this year to make sure that at least one of the challenges was
[2585.46 --> 2591.26]  accessible to someone with like no code knowledge whatsoever like the the terminal text twister like I
[2591.26 --> 2596.88]  mentioned before fun little mini game you can just go through and you can brute force it by just
[2596.88 --> 2601.38]  clicking words until you figure out what the right word for each stage was and then move on to the next
[2601.38 --> 2607.52]  one there was also a crossword which was you could get the answers pretty easily without even needing to
[2607.52 --> 2613.38]  know anything about programming or about go or you know you could just use google and and figure out the
[2613.38 --> 2618.64]  answers yourself I think someone actually threw the answers into chat gpt and got their answers that way
[2618.64 --> 2622.76]  so we're going to make sure that we have at least a couple of those challenges for next year as well
[2622.76 --> 2628.14]  the idea is that everyone who has any interest should be able to participate and should be able to pass at
[2628.14 --> 2632.64]  least one challenge I think those are the people we want to reward the most are the people who are
[2632.64 --> 2638.64]  taking a bigger step and and coming in there and being able to say like I did it now what what's next
[2638.64 --> 2644.18]  and being able to be part of the the group and community surrounding just the competition
[2644.18 --> 2649.90]  is going to help them kind of take that next step beyond that yeah and and the thing is too is like
[2649.90 --> 2653.90]  you know some of the challenges too like we had several people that came by last year that didn't have
[2653.90 --> 2658.14]  their computers with them you know there were some challenges that you technically could do without
[2658.14 --> 2661.62]  a computer they were much more difficult if you're coming to go for con bring a laptop with you
[2661.62 --> 2667.16]  just in general it'll make things a lot easier on you but uh if you can't that's fine there probably
[2667.16 --> 2671.30]  will be some challenges you can do without it if you're new to coding if you're your intro to go
[2671.30 --> 2675.32]  things like that and you want to do the the challenge series right which we're gonna call
[2675.32 --> 2679.02]  the challenge series come hang out with the host at the table you know like one of the best things
[2679.02 --> 2683.88]  about go for con and and i'll tell anybody who ever asks me like this is like i've been to a lot of
[2683.88 --> 2688.70]  conferences over the years and go for con is my favorite and the reason being is because when i when
[2688.70 --> 2693.04]  i came to go for con the first time it was the i think it was the first time that i i can ever say
[2693.04 --> 2699.24]  that i was like i felt like truly accepted as a person and so like i sat down and i was able to sit
[2699.24 --> 2704.90]  with other people who like spoke the same language and enjoyed the same things and it was able to like
[2704.90 --> 2712.72]  learn from others in an environment where it didn't matter who i was and so i learned more in my first
[2712.72 --> 2720.34]  go for con about go than i had in like the year and a half that i had been coding go before i came so
[2720.34 --> 2725.70]  like if you're wanting to learn go or you're you're wanting to learn to program or you're wanting to get
[2725.70 --> 2732.26]  the software you know come to go for con come to the challenge series table like i will personally
[2732.26 --> 2736.54]  help you with the challenges like i mean i'll show you how to set up a terminal if you don't know
[2736.54 --> 2741.18]  you know any of that stuff the go community is incredible like it's welcoming and inclusive
[2741.18 --> 2747.90]  and it is is very much worth being part of there has never been a development community that i have
[2747.90 --> 2754.20]  been more proud to be a part of yeah and i'll i'll jump on top of that as well like i think the
[2754.20 --> 2760.76]  community i've seen around go is much more like a community than any other programming community
[2760.76 --> 2766.42]  i've been part of at least at that scale like i've been part of smaller location-based communities that
[2766.42 --> 2772.22]  feel more community-ish but for the tens of thousands of people surrounding the go language
[2772.22 --> 2778.70]  and ecosystem to feel so much like like you know people and you have friends and you you get to
[2778.70 --> 2783.92]  like really know the other people involved you know i keep saying that one of the biggest things
[2783.92 --> 2790.96]  and most important parts of go for con is community day and you know for me at least being part of the
[2790.96 --> 2796.08]  capture the flag felt like the entire conference was community day yeah that's for sure yeah it
[2796.08 --> 2799.46]  definitely felt like the whole conference was community day with the capture the flag that's
[2799.46 --> 2803.68]  amazing that's awesome great so what i'm hearing is whether you're complete newbie
[2803.68 --> 2813.60]  or your uh go genius there will be a challenge for you and challenge series is for you yes great i'm
[2813.60 --> 2820.02]  very excited and i will see you at the table in a few months and without further ado we're now going
[2820.02 --> 2824.64]  to move over to a completely unrelated although you can make it related if you like section of the
[2824.64 --> 2827.20]  episode which is unpopular opinions
[2827.20 --> 2854.48]  so i'm gonna come to you first neil i would love to hear your unpopular opinion
[2854.48 --> 2860.30]  okay benji and i coordinated on this a little bit i took the non-tech unpopular opinion okay i
[2860.30 --> 2866.88]  believe the most appropriate cheese for pizza is romano cheese that is my unpopular opinion say more
[2866.88 --> 2874.48]  why uh so the area i grew up in in like eastern ohio actually has this as like kind of a regional dish
[2874.48 --> 2880.16]  you take a pizza put like a kind of a sweeter sauce with green peppers bell peppers baked into it
[2880.16 --> 2886.22]  and then you don't do any of the regular like regular pizza cheeses you do just romano cheese
[2886.22 --> 2891.60]  like you know shaker cheese over it it doesn't melt quite the same way it's not nearly as heavy
[2891.60 --> 2898.02]  and it really meshes well with kind of a little bit sweeter sauce and it's just like the right type
[2898.02 --> 2905.16]  of pizza i cannot say that i have ever tried that in my entire life but i want it in my mouth right now
[2905.16 --> 2911.92]  i feel the same i'm like very intrigued i need to like go buy some now and make my own pizza at
[2911.92 --> 2918.70]  home for dinner it's a type of pizza called briar hill b-r-i-e-r hill pizza okay the only problem is
[2918.70 --> 2924.78]  that it would mean that i have to go to ohio oh no just just kidding just kidding to anybody who's
[2924.78 --> 2931.22]  listening in ohio you guys are great i've actually never been to ohio need to check it out i used to
[2931.22 --> 2935.84]  work for a company that was that's based in ohio and perrysburg actually yeah oh awesome that's
[2935.84 --> 2940.82]  actually i did i actually don't mind ohio it's very nice okay so we have a unpopular or potentially
[2940.82 --> 2946.54]  popular once people get a chance to try an opinion benji over to you are you sure you want me to go
[2946.54 --> 2950.82]  before uh before you go like you don't want to you don't want to go before everybody ragey quits
[2950.82 --> 2956.94]  no i'm i'm ready i'm ready we are not quitters on this show all right so so my unpopular opinion
[2956.94 --> 2964.94]  and you may or may not agree okay that's fine i don't care is that okay anyone at any time should
[2964.94 --> 2971.06]  be able to develop and release a net new project to the open source community regardless of the
[2971.06 --> 2977.32]  number of pre-existing projects of the same kind without being concerned for contributing to those
[2977.32 --> 2983.38]  existing projects that open source shouldn't be gatekept to new projects simply because a similar
[2983.38 --> 2988.96]  one exists and people should be able to contribute code however they want and be proud of their work
[2988.96 --> 2995.66]  there's an xkcd for this there's is there an xkcd for this yeah because there there has been so many
[2995.66 --> 3000.68]  times that i'll i'll build something and and i'll release because i i do most of my stuff in open
[3000.68 --> 3006.66]  source right well lately i haven't been but most of the time i'll build something and i'll open source
[3006.66 --> 3011.56]  it just because like hey i use this and it's easier for me to import a go package if it's open source so
[3011.56 --> 3016.44]  i'll throw it out open source right and you know because i'm proud of it i'll share it in the go
[3016.44 --> 3020.36]  slack or i'll share it on reddit or something like that and everybody gets up in arms oh this already
[3020.36 --> 3024.32]  exists why aren't you contributing to this other package and then i'll see it happen to others where
[3024.32 --> 3029.08]  somebody will you know share their their library things like that oh why aren't you contributing to
[3029.08 --> 3034.02]  this other thing instead and why did you build your own i don't think that should happen i think that
[3034.02 --> 3037.60]  i think that people should be able to contribute to the open source community and build what they want
[3037.60 --> 3043.44]  whether or not it exists already or not i mean maybe this isn't maybe you're preaching so quiet here
[3043.44 --> 3052.34]  i i would love to hear a little bit about why like devil's advocate it might be suboptimal to have
[3052.34 --> 3058.00]  loads of different open source projects that do the same or similar things because i can see that being a
[3058.00 --> 3064.38]  cool argument is if there's already something and if the ethos of one of the core goals of open source
[3064.38 --> 3068.70]  is to make something better and better and better like i put something out there and neil contributes
[3068.70 --> 3075.10]  makes it better benji you come in you make it so we build together a better surely that may be a
[3075.10 --> 3081.06]  better path to overall community service than me putting something out there neil put something out
[3081.06 --> 3085.36]  there benji put somewhere out there yeah i mean like i i think you could you could make the argument
[3085.36 --> 3092.20]  that if you feel inclined to contribute to another project like let's say for example you are like hey i
[3092.20 --> 3097.36]  really enjoy this open source project i like you know and i work in the same language or i work in
[3097.36 --> 3104.04]  the same you know or whatever let's say for example um i enjoy working with the gen router right let's
[3104.04 --> 3108.72]  say i prefer that one i don't want to go out and build my own router and i find a bug and i want to
[3108.72 --> 3113.08]  contribute to the project yeah sure i'll go and you know fix a bug in the project and i'll pr into it
[3113.08 --> 3117.22]  that's fine you know if you want to contribute to the project that's fine but like let's say for example
[3117.22 --> 3123.48]  i want to go down the rabbit hole of um i don't know uh creating my own logger i've done that i did
[3123.48 --> 3129.74]  it a while ago you know years ago then i found zap and i threw mine away you know but like now zap is
[3129.74 --> 3133.88]  thrown away because of slog so like you know it's one of those things where it's like as time progresses
[3133.88 --> 3139.42]  you know things change so like we see this in the go community good examples of this is uh go modules
[3139.42 --> 3143.60]  was a good example of this we saw a number of different like you know package repository options
[3143.60 --> 3147.66]  in the go community you know and then the go team was like hey you know let's look at
[3147.66 --> 3153.02]  depth and then um well i forget the other ones i only ever used up and then you know they're like
[3153.02 --> 3156.94]  let's consolidate them but let's look at them and see what the benefits of each of these different
[3156.94 --> 3162.64]  ones are and then build something that that we can kind of all coalesce on the same thing with
[3162.64 --> 3167.14]  the new slog library you know i don't need zap anymore i've got slog it's part of the standard
[3167.14 --> 3172.42]  library in go i can use that it's no longer in beta it's in standard library comes with go 121
[3172.42 --> 3176.94]  you know go generics has come out i don't have to worry about using some weird you know third party
[3176.94 --> 3183.10]  generics library that's using any the empty interface anymore i can use the standard go
[3183.10 --> 3188.66]  implementation of generics so in some respects i can understand where contributing to an existing
[3188.66 --> 3194.28]  project might be more beneficial right like it helps in some respects it helps push the community
[3194.28 --> 3200.48]  forward in other respects though it helps me develop as an engineer right like if i need to go out
[3200.48 --> 3204.74]  and learn how to develop a logging library i learned things that i didn't know before
[3204.74 --> 3210.52]  like with the logging library i learned how to better understand different levels of logging
[3210.52 --> 3215.80]  what's important to collect that you know in a log that's that's useful at different levels how do i
[3215.80 --> 3220.52]  handle formatting how do i handle lots of these different things you know how do i identify where
[3220.52 --> 3225.00]  a log is taken inside of a specific file how do i handle stack traces things like that
[3225.00 --> 3230.14]  and that's only one example you know like i think that one of the most important things is that as
[3230.14 --> 3235.60]  an engineer or as a person in general is that you learn from what you do and so whether or not it's
[3235.60 --> 3241.08]  you putting out something into the open source just because that's the easiest way for you to import a
[3241.08 --> 3244.94]  package or you want to share it with somebody and be proud of it or share with the community and be
[3244.94 --> 3250.88]  proud of it you should be able to do that without having others say well why aren't you contributing to
[3250.88 --> 3255.90]  this other project that somebody else created right that seems very you know rather immediately
[3255.90 --> 3261.30]  dismissive of somebody else at the same time you know like i think that that the community can you
[3261.30 --> 3266.66]  know coalesce on certain technologies and we have done that in the go community right we have continued
[3266.66 --> 3273.56]  to um evolve as a community and we've we've gotten better in in different places and so i i think that uh
[3273.56 --> 3278.42]  yeah i mean i can see the argument either way but at the end of the day i think it's important to
[3278.42 --> 3286.16]  encourage people to learn however they do that and i don't think that people learn best by being
[3286.16 --> 3292.72]  shut down for being excited about something they did i think that people learn best by being encouraged
[3292.72 --> 3299.10]  to try something that they want to do and and i think that that that's the difference so if i'm
[3299.10 --> 3304.76]  interpreting your unpopular opinion which actually i think is quite maybe quite popular it's less about
[3304.76 --> 3312.22]  whether you should either contribute to an existing or put your own work out to open source it's more
[3312.22 --> 3319.46]  about the response and the attitude towards being able to make that choice for yourself based on your
[3319.46 --> 3323.48]  goals what you want to do what's important to you whether it's learning adding to a larger project
[3323.48 --> 3330.04]  working with other maintainers etc it's less about the which you do and more about the attitude towards
[3330.04 --> 3335.96]  it and having the community be more supportive of that individual's choice regardless of what that
[3335.96 --> 3342.54]  motivation is they want to do it they all that's all they want to do i'm intrigued i'm i feel like this
[3342.54 --> 3349.52]  might um instigate a really great discussion i mean it's getting my cogs going awesome well
[3349.52 --> 3357.56]  we are pretty much at time so are there any closing thoughts final remarks of any nature
[3357.56 --> 3362.18]  before we close out i gotta fill my gas tank so i can go to ohio
[3362.18 --> 3371.96]  and on that note thank you both it was an absolute pleasure chatting to you both as we've noted if
[3371.96 --> 3379.70]  you're not on go for slack join and then you can look within go for slack and join the channel can you
[3379.70 --> 3385.10]  remind me again what the channel name is are you going to make a change to it given the challenge
[3385.10 --> 3389.92]  name change or it's going to remain as is you know we probably are going to change it this year
[3389.92 --> 3395.52]  and actually we might probably are going to be more active in the um the discord this year yeah
[3395.52 --> 3400.66]  um because i know that i know that uh go for con covers the subscription for discord and we can have a lot
[3400.66 --> 3406.80]  more um there's a lot more flexibility in there and so we'll probably uh be more active in discord this
[3406.80 --> 3412.44]  year for the challenge series so uh if you're not in in slack or you're not in the discord you know
[3412.44 --> 3417.62]  jump into both of those but uh yeah we'll probably probably work on something to synchronize the two
[3417.62 --> 3422.98]  of them some kind of bot i don't know we'll see great and then on general updates on go for con
[3422.98 --> 3429.88]  and the challenge series you can follow go for con on kind of twitter all the places to get updates
[3429.88 --> 3436.84]  um and cheeky reminder call for papers for go for con are open so if you they're about to open
[3436.84 --> 3444.52]  so if you're moodling on an idea please start formulating it into a concise proposal so that
[3444.52 --> 3450.48]  you can get it in asap yeah and if you if you're second guessing submitting don't second guess it
[3450.48 --> 3457.34]  submit it just do it just do it awesome well pleasure as always talking to you both and have a great rest of your day
[3457.34 --> 3466.42]  that is go time for this week thanks for hanging with us subscribe now if you haven't already head
[3466.42 --> 3473.22]  to gotime.fm for all the ways also check out changelog news while you're at it it's the software
[3473.22 --> 3479.50]  industry's best weekly podcast slash newsletter to keep you plugged in to developer news worth your
[3479.50 --> 3487.14]  attention subscribe now at changelog.com slash news thanks once again to our partners at fly
[3487.14 --> 3493.86]  dot io the home of changelog.com and thank you to breakmaster cylinder for producing so many fresh
[3493.86 --> 3499.78]  beats for us that we're now releasing full-length albums on spotify apple music and the rest listen
[3499.78 --> 3505.66]  along by searching for changelog beats in your music app of choice you'll find us that's all for now
[3505.66 --> 3508.74]  but we'll talk to you again next time on go time
[3517.14 --> 3540.56]  game
