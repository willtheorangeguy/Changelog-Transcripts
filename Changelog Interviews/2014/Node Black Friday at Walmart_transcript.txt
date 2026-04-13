[0.00 --> 14.40]  welcome back everyone this is the changelog and i'm your host adam stekowiak we're a member
[14.40 --> 21.94]  supportive blog podcast and weekly email covering what's fresh and what's new in open source check
[21.94 --> 28.58]  out the blog at the changelog.com our past shows at 5by5.tv slash changelog and subscribe to our
[28.58 --> 33.22]  weekly email it's called the changelog weekly we ship it on saturdays you don't want to miss it
[33.22 --> 39.80]  and you can subscribe at the changelog.com slash weekly this show is hosted by myself adam
[39.80 --> 46.22]  stekowiak and andrew thorpe now we recorded this show in particular before the new year didn't have
[46.22 --> 50.82]  time to publish it before the new year but at the tail end you'll hear andrew mention taking some
[50.82 --> 57.54]  time off that's already happened we missed you we're back we're excited it's 2014 and this is
[57.54 --> 65.42]  episode 116 and it's sponsored by digital ocean fresh books and top tile we'll tell you a bit
[65.42 --> 69.72]  more about fresh books and top tile later on the show but our our good friends over digital ocean
[69.72 --> 75.10]  have some cool stuff happening they're nearing their millionth droplet and to celebrate they're
[75.10 --> 81.30]  giving away ten thousand dollars in hosting credit ten thousand dollars in hosting credit you heard it
[81.30 --> 88.82]  right to a lucky user who hits this milestone and there are three ways you can qualify number one
[88.82 --> 94.38]  you got to be the user who spins up the millionth droplet so that's that's number one number two you've
[94.38 --> 100.88]  got to include your twitter handle in the droplets host name so when you create the droplet you got to
[100.88 --> 107.42]  put your twitter handle in that host name and number three you have to tweet the digital ocean with the
[107.42 --> 115.10]  hashtag millionth droplet for example i'm going to be the millionth droplet on digital ocean that would
[115.10 --> 121.58]  qualify you if you do all three things you're in it so try the ocean today for free using our promo
[121.58 --> 129.26]  code changelog sent me that's changelog sent me that'll get you a ten dollar hosting credit as well as
[129.26 --> 135.54]  as well as a chance i guess to potentially be the moon's droplet so good luck to you but head to
[135.54 --> 142.12]  digitalocean.com to get started and now on to the show we're joined today by aaron hammer to talk
[142.12 --> 149.90]  about happy a server framework for node.js and node black friday when walmart went node for black
[149.90 --> 154.12]  friday so aaron welcome to the show why don't you give us a introduction of who you are and what you do
[154.12 --> 162.50]  hey uh glad to be here i am uh the node uh lead architect at uh walmart uh i'm part of the mobile group
[162.50 --> 171.34]  and my team is uh basically focused on um moving the uh existing uh mobile services uh infrastructure
[171.34 --> 178.62]  from uh some legacy java stuff to node and uh we basically drive all the uh all the api for the
[178.62 --> 187.68]  mobile clients so what did you do before uh working at at walmart uh immediately before i was about
[187.68 --> 197.32]  uh three years at yahoo um focusing mostly on standards and focusing on interop and and um
[197.32 --> 204.92]  open web i was one of the uh the founder of the open web foundation and uh did a lot of ipr work
[204.92 --> 210.70]  um in terms of uh cla and agreement there and uh before that i spent about 10 years on wall street
[210.70 --> 217.42]  uh building uh high frequency trading systems and uh yeah that that's that kind of covers the last 15 years
[217.42 --> 225.00]  so you've definitely uh been deep into the business side of things um i've done a whole bunch of
[225.00 --> 230.88]  different uh different things and my my uh philosophy in life is that life is all about uh collecting uh
[230.88 --> 238.26]  experiences so i i tend to get bored with things uh and just switch to completely unrelated fields
[238.26 --> 244.26]  yeah so going from finance to you know just consumer web to retail well let's talk a little bit about
[244.26 --> 249.78]  the retail so uh what was behind the decision for walmart to to go to node and and what was that process
[249.78 --> 260.16]  like uh it wasn't it wasn't a very intense process uh to be honest basically two years ago uh ben and
[260.16 --> 270.24]  dion joined uh walmart mobile and they were looking for ways to kind of move it to the uh 21st century
[270.24 --> 279.14]  um from some some really uh old stacks on java it was using and what was clear is that we're not going
[279.14 --> 284.40]  to be rewriting all the all the back-end services but we are going to be building a new orchestration
[284.40 --> 291.40]  layer that's going to talk to a whole bunch of uh new and legacy systems uh some of them uh you know
[291.40 --> 298.12]  using you know like as400 and and you know offering you you know awesome soap apis and others
[298.12 --> 304.04]  use a little bit more modern with xml stuff and and so we don't want to implement any of that on the
[304.04 --> 309.16]  mobile clients and what you want to do you want to build an orchestration layer that kind of abstract
[309.16 --> 316.54]  all the crap in the back um or the good stuff in the back and then provides a uniform api to the mobile
[316.54 --> 323.46]  clients so we were looking at different technologies and we we just felt that node was the right choice
[323.46 --> 329.78]  that uh an orchestration layer that is mostly doing network uh it's basically a glorified proxy
[329.78 --> 336.46]  uh with some data manipulation or data transformation but it's not you know no calculation you're not
[336.46 --> 342.44]  pricing anything you're not uh you're not managing a complicated state um that that's all done by the
[342.44 --> 348.74]  upstream you know account management and and those so so node looked like a good choice and so we
[348.74 --> 354.42]  just went ahead and made a big bet that it's going to work out so you obviously walmart's one of the
[354.42 --> 359.94]  biggest you know companies in the world and um in my experience with larger companies it can be you
[359.94 --> 365.42]  know it's a lot harder to move a big ship right than a than a small boat and so what kind of like pain
[365.42 --> 371.14]  inside of walmart if any did you experience when you're presenting this you know this new newer
[371.14 --> 376.28]  emerging technology as an alternative to like a reliable uh stack that's that's been around for a while
[376.28 --> 384.22]  so it's still there's still resistance coming from other teams uh within mobile it it wasn't it was
[384.22 --> 391.26]  never an issue because uh mobile started out as a as a labs like environment where our mandate was to
[391.26 --> 397.34]  experiment and try new things and use whatever technology we want uh like you know we were already
[397.34 --> 405.48]  introducing new things if it's uh ios apps or android apps uh to to the existing uh it stack that was used
[405.48 --> 410.38]  there so that that wasn't a big deal but then going to the rest of the organization you know when we
[410.38 --> 416.56]  went to the uh the it folks and the data centers to try to get some some machines we can run it on
[416.56 --> 423.06]  uh one of the first bomb we hit is that the um the version of solaris that walmart was running at the time
[423.06 --> 429.44]  um could not support node we couldn't compile node on that operating system and so it took some time for us
[429.44 --> 435.52]  to convince uh enough people to get us some you know linux boxes or smart os boxes that we can actually
[435.52 --> 441.12]  uh run stuff so it was more once you start interacting with the rest of the it organization
[441.12 --> 446.92]  and it wasn't as much pushback as just uh we were asking them to do new things that they have never
[446.92 --> 452.78]  done before uh and those you know those things takes a lot of time um and if you think about uh walmart
[452.78 --> 460.26]  runs all i think it's like 17 countries now um so they're running all their operations um all from
[460.26 --> 466.68]  the same set of data centers so you talk about the retail stores and the online all coming from pretty
[466.68 --> 473.56]  much the same same spot so you can imagine the change control in those data centers is is quite
[473.56 --> 478.66]  insane right um and for a good reason uh you know you're talking about you know if you if you take
[478.66 --> 485.28]  down those data centers in the u.s you're disrupting uh food supply for about 40 of the country so it's
[485.92 --> 491.40]  the the scale and the size and the magnitude of any change you're making is is significant so that
[491.40 --> 498.58]  that's still the issue um but it's been very manageable yeah so for for walmart mobile i guess
[498.58 --> 503.46]  and i'm a little i'm not i wouldn't say i'm fuzzy i just to i think i've made some assumptions but
[503.46 --> 509.58]  you guys did you launch the node client for black friday or when did that launch actually happen
[509.58 --> 517.78]  we deployed our so so we we are working with a proxy strategy we're basically the idea is to stick
[517.78 --> 524.40]  node as a as a dumb proxy between the mobile clients and the existing services and then slowly
[524.40 --> 530.34]  as uh based on business priorities and other requirements start to hijack endpoints at the
[530.34 --> 537.12]  proxy and implement them in node so we've started doing that um but we're still um proxying a large
[537.12 --> 544.58]  amount of the traffic through node to the upstream services so we first rolled this out in april and
[544.58 --> 552.02]  uh we kind of ramped up to 100 of all mobile traffic around june and we've been running with all mobile
[552.02 --> 559.80]  traffic going through node uh since june the problem was that uh we had uh we suffered from a pretty
[559.80 --> 567.38]  awful memory leak um that caused us basically to have to you know restart the services all the time
[567.38 --> 576.34]  and um so we were never sure up until the day of black friday that that our system is actually ready for
[576.34 --> 583.22]  for that capacity um and we had mitigation we had other plans we had failovers so so it wasn't like oh
[583.22 --> 587.94]  if this doesn't work we're we don't have mobile uh mobile services for black friday that clearly is
[587.94 --> 594.68]  not going to be acceptable right um but we really didn't know up until the the day of uh how well
[594.68 --> 599.10]  this is going to perform so how well did it perform oh it was the most boring thing ever
[599.10 --> 604.50]  you had a tweet i can't remember exactly but you it's something along those lines that the servers
[604.50 --> 608.12]  are bored out of their mind yeah the servers are bored out of their minds what you said that's that
[608.12 --> 614.12]  was uh pretty intense and then you were also doing a lot of live tweeting at that time too like
[614.12 --> 620.02]  keeping a lot of nerds uh on their toes i'm sure just kind of like watching your progress and i know
[620.02 --> 625.66]  i was shopping and watching at the same time i just was watching the you know node bf was the was the
[625.66 --> 630.30]  hashtag on twitter we linked out to it and we'll put this in the show notes too so y'all can catch up
[630.30 --> 635.94]  those listening but node uh had the servers that were that they were bored so what was that like
[635.94 --> 644.22]  i mean the servers were doing nothing uh they're averaged about 0.75 percent cpu that's not 75
[644.22 --> 651.14]  that's 0.75 and by the way we had a we had a bug in our monitoring system for a while where
[651.14 --> 656.76]  uh we thought that the range was zero to one and we were really worried for a while because we were
[656.76 --> 662.52]  constantly hitting 50 to 60 cpu and then we started investigating like what is going on i mean that
[662.52 --> 668.04]  that we're not doing anything why is the cpu so high it should really be like 20 um and then we
[668.04 --> 675.76]  realized that it was a unit uh bug and we were actually at 0.5 percent cpu so that's good yeah it
[675.76 --> 683.66]  was very very uneventful um but uh no the node process was just sitting there doing nothing uh memory
[683.66 --> 691.32]  was completely stable uh people have uh nicknamed my uh rss charts is uh my um um um
[691.32 --> 698.96]  lasagna charts oh yeah where basically it just looks like a bunch of like you know swiggly but
[698.96 --> 706.04]  flat flat lines trending lines yeah um yeah no it it was really really boring and and as the night
[706.04 --> 711.82]  progressed and and you know my team was all up uh everybody was coming up with suggestions of how
[711.82 --> 718.30]  we can uh just just gently poke the servers to make something break just to kind of keep it a little
[718.30 --> 722.68]  a little more interesting everybody has their own suggestion of what we can do so i mean like you
[722.68 --> 729.06]  said black friday is like the biggest retail day you know of the year and you guys what were you
[729.06 --> 733.80]  planning for you said you had no idea what was going to happen but i mean really no idea or were you
[733.80 --> 741.86]  hoping for the best or like did what was in y'all's mind um so i mean the the industry uh as a whole
[741.86 --> 747.70]  the average is basically 40 to 60 percent of annual revenues online happen between thanksgiving and
[747.70 --> 752.62]  black and between thanksgiving and christmas which if you think about it for a business that's that's
[752.62 --> 761.50]  awful it's insane yeah and if you have a day downtime um with uh black friday and cyber monday being the
[761.50 --> 769.62]  the two busiest uh shopping days although now with all the retailers thanksgiving has become uh the
[769.62 --> 775.36]  number one shopping day it's a little crazy but um that that's that's where we've seen the most
[775.36 --> 780.24]  traffic especially since everybody's uh looking up the deals not necessarily buying but they're looking
[780.24 --> 787.10]  it up so we had the business every year the business gives us estimates of how much traffic uh what's
[787.10 --> 793.84]  the multiplier going to be from both last year and from um like from september of the same year yeah
[793.84 --> 800.58]  and so we were looking at uh at you know two three four times multipliers in terms of volume
[800.58 --> 806.74]  but more than anything we really didn't know how well the upstream services are going to perform
[806.74 --> 813.32]  so if you think about it node sits between the clients and the uh and the java services and
[813.32 --> 819.44]  because node is doing such a great job managing the income track the incoming traffic it's such a great
[819.44 --> 827.66]  uh little executable for managing sockets it's basically acting as a queue so load balancer is
[827.66 --> 832.72]  basically sending traffic to the node processes and then they are trying to proxy it over to java and
[832.72 --> 838.16]  if java is behind and starting to get slow it doesn't really add much load on the node process in terms
[838.16 --> 842.04]  of cpu because it's just because it's a non-blocking system so it doesn't do anything it's just sit there
[842.04 --> 847.76]  waiting for socket events and no socket events are coming back but what is happening is that we are
[847.76 --> 852.42]  growing in memory because all we were keeping we keep holding more and more and more sessions in
[852.42 --> 859.94]  memory until the java stuff is ready and in that environment basically node becomes a queue and if
[859.94 --> 865.16]  java gets very very slow then notice you know the queue gets very very big until at some point it blows
[865.16 --> 870.48]  up so we didn't really know what to expect in terms of how big is this queue going to be how how well is
[870.48 --> 876.82]  the memory going to perform so we we basically dumped a lot of extra capacity we ended up i think with
[876.82 --> 883.34]  about six times more capacity than we actually needed um which really contributed to like the
[883.34 --> 889.42]  completely boring yeah exactly performance so this was then a major success right for you and your team
[889.42 --> 899.06]  this this was huge i think um i think we kind of proved the entire stack but also like my the quote
[899.06 --> 904.50]  i've been using uh privately in conversation with the node core team and and you know a few other
[904.50 --> 912.32]  companies like joint and uh um voxer um i kept saying like i don't want to be the uh i don't
[912.32 --> 916.08]  want to be what twitter was for rails i don't want to be the the you know rails doesn't know
[916.08 --> 922.62]  yeah of node um because even though like you know it was largely bullshit at the time um
[922.62 --> 929.36]  it it did cause quite a significant damage to to rails adoption um you know once once twitter was
[929.36 --> 933.82]  having problems a lot of people uh there was like this this backlash and people were going back to
[933.82 --> 941.98]  php because you know facebook was on php and that was clearly much better yeah um so so i i was like
[941.98 --> 946.64]  i'm not going to be that guy like like i'm not going to be the number one you know headline on hacker
[946.64 --> 955.24]  news saying you know no doesn't scale uh just ask walmart so i was i was really freaking out about that
[955.24 --> 961.22]  and and that was kind of that was like the back of my mind um as we were approaching this yeah so we
[961.22 --> 967.10]  kind of threw more capacity at it we were like watching it um like everybody on the node core team
[967.10 --> 971.08]  was like following it throughout the night like all waiting for like anything if anything goes wrong
[971.08 --> 977.22]  to jump on irse with us and like help us fix it live um it was really like you know it it meant a lot
[977.22 --> 981.16]  to the community as a whole yeah it seemed like it i mean that's really the way i took it because
[981.16 --> 988.44]  we tweeted said we tweeted uh that night uh follow um node bf on twitter and lots of retweets came
[988.44 --> 993.76]  from that and i think your tweet alone got 82 favorites and 157 retweets and it just seemed like a lot of
[993.76 --> 998.24]  people were just like watching real time and a lot of people who were involved in node just kind of like
[998.24 --> 1004.58]  you know behind the scenes cheering to make sure that you know everything had gone successfully for you
[1004.58 --> 1009.66]  yeah my uh my follower count on twitter jumped by like a thousand for the night
[1009.66 --> 1016.14]  um it's crazy it was it was uh it was quite funny but it's a you know it's like you said it's big for
[1016.14 --> 1020.56]  the community right i mean people that like node they want to see node succeed and so it's not just
[1020.56 --> 1025.96]  big for you and your team because you're proving an emerging technology to a to a you know a very large
[1025.96 --> 1031.12]  company but it is it's it's it's big for the whole community because like you said if if something
[1031.12 --> 1035.94]  would have fallen flat on its face whether it was your fault or you know an inherent problem with node
[1035.94 --> 1041.28]  then you're right the the rumors would have been node can't scale and i mean you still hear that
[1041.28 --> 1045.24]  every once in a while when people are talking about rails you know just when they haven't you know
[1045.24 --> 1049.30]  been maybe not in the community for the last couple years but you'll still you know every once in a
[1049.30 --> 1053.46]  hear somebody say rails can't scale and you know that that kind of sticks with you so you're right it's
[1053.46 --> 1057.80]  a it's a good thing for the whole community not just the the walmart node branch you know
[1057.80 --> 1066.72]  yeah this this was a big deal and it also uh at node summit i gave a talk but basically my plan for
[1066.72 --> 1072.30]  node summit was to give a talk about black friday of course there was nothing to talk about so i
[1072.30 --> 1079.00]  basically gave a talk about how everything went wrong all the way until black friday and uh we only got
[1079.00 --> 1088.76]  the the fix for the for the infamous memory leak in um the week off like we actually that that was we
[1088.76 --> 1094.78]  and we couldn't even verify because we're doing daily uh daily releases so we we never actually got to
[1094.78 --> 1099.54]  observe the server over you know over like 48 hours to see that the memory leak was actually fixed
[1099.54 --> 1107.78]  so it was all very theoretical and we so that was part of the the thing is that if the memory leak was
[1107.78 --> 1114.58]  still going on uh it required us to restart our servers every seven days and we were expecting you
[1114.58 --> 1120.68]  know up to 10x yes traffic and well that means we can have to restart the servers more than once a day
[1120.68 --> 1126.94]  yeah and on black friday you don't really want to touch your servers right um so so it was all very
[1126.94 --> 1132.06]  suspenseful but it was kind of like uh edge of your seat suspenseful but boredom so did you have somebody
[1132.06 --> 1136.02]  like working on that memory leak all the time trying to find it or what happened with that
[1136.02 --> 1143.92]  um so we found a memory leak uh well we we saw the pattern of the memory leak back in uh april already
[1143.92 --> 1152.08]  and then by june it was i i was convinced the memory leak um and it was uh it was one of those things
[1152.08 --> 1156.98]  where like i i i argue with everybody including my own team that it is a memory leak and they're all
[1156.98 --> 1162.34]  like no it must be something else uh and i said no it's an it's a node memory leak and they're like no
[1162.34 --> 1165.50]  this it can't be no then really because if somebody else would report it right like other people are
[1165.50 --> 1171.84]  using node in production and they're not seeing any of that behavior and so we end up spending quite
[1171.84 --> 1176.94]  a lot of effort uh putting quite a lot of monitoring into the system where i was basically spending
[1176.94 --> 1181.92]  three months trying to find correlation between the memory leak when memory was was spiking to when
[1181.92 --> 1188.40]  something else was going on so we added monitors for uh client disconnects and response times and
[1188.40 --> 1196.26]  uh concurrent connections and just connections per uh per second and like really like we have we we build
[1196.26 --> 1202.38]  in so much monitoring into it so we can start comparing it and nothing correlated just absolutely
[1202.38 --> 1208.62]  nothing we knew the more traffic we get overall the more leak we get but it's not the leaking is not
[1208.62 --> 1214.32]  happening when the traffic is coming in it's just that there's a correlation between the overall daily
[1214.32 --> 1221.28]  pattern and at some point i found a few clues that i had some ideas and i said okay we're going to
[1221.28 --> 1225.78]  make a configuration change that is going to double the amount of http client calls that we're making
[1225.78 --> 1231.64]  and uh and i said and watch we'll do that and the memory leak will double itself and people were like
[1231.64 --> 1236.20]  kept saying like no no it's not gonna happen and of course memory leak doubled itself
[1236.20 --> 1245.16]  uh which helped us you know zoom zoom into the exact um spot where we're we're leaking and i was able
[1245.16 --> 1250.38]  to isolate that and then i wrote a little program that that showed it but it took about 12 hours of it
[1250.38 --> 1257.82]  to run to even show you a slight leak and it was all from what closing file descriptors no it ended up
[1257.82 --> 1264.80]  being a missing uh handle scope in the c++ side of node in what it was one it was one line missing
[1264.80 --> 1273.60]  a node uh in one function um it was basically two c++ words that was the bug and it caused a four in some
[1273.60 --> 1281.22]  cases it caused a four bytes leak per http request yeah so that takes a little while to add up but that
[1281.22 --> 1290.18]  definitely ends up uh yeah and so and at the time we were leaking about um eight eight megs a day
[1290.18 --> 1297.78]  so so we we got it really really low by mitigating it in other ways but um couldn't really solve it and
[1297.78 --> 1303.66]  then uh uh um tj fontaine from the node core team um was able to uh he spent like three weeks on it
[1303.66 --> 1311.26]  um we took some crazy stuff and there's a there's a great blog post on the um on the joint uh blog
[1311.26 --> 1320.10]  uh detailing exactly uh uh what tj uh uh used and and it's kind of like uh a little bit like uh
[1320.10 --> 1325.48]  black magic so that's interesting the blog post though let me ask you what was that experience
[1325.48 --> 1329.94]  like going back and forth with the the node core team and and you know trying to prove this and
[1329.94 --> 1335.86]  how receptive were they to you like you know pointing this stuff out so when we first reported it uh
[1335.86 --> 1342.88]  back in like june or july it was the uh people have been quite dismissive um where basically the
[1342.88 --> 1347.76]  the theory was like there is no way we have such a gigantic memory leak and you're the only one seeing
[1347.76 --> 1353.18]  it um but when at the end when i was able to actually come and say hey here's a little bit of
[1353.18 --> 1358.20]  node code and if you run it it will show you the leak uh and then of course they ran and they're like
[1358.20 --> 1361.68]  no we're not seeing any leak and i said like just just leave it alone for 12 hours and come back to
[1361.68 --> 1365.66]  it tomorrow and they did and they opened it up and it's like no it still doesn't look like a leak
[1365.66 --> 1371.46]  it's like oh go ahead and plot your trend line yeah on that on that chart and then they did that
[1371.46 --> 1375.18]  and i was like oh yeah you know what it looks like there's something going on there and then as they
[1375.18 --> 1381.06]  edit more instrumentation they can actually start seeing um what was actually happening is uh
[1381.06 --> 1389.68]  uh v8 was building a gigantic array of undefined which is where the four bytes came from basically it
[1389.68 --> 1395.52]  was pointing to the canonical undefined reference within the v8 uh it was just building a gigantic
[1395.52 --> 1401.32]  array of undefined that was never we're never getting cleaned right so because of the so you
[1401.32 --> 1408.82]  said it was fixed the week of is that right it was fixed about two two weeks before um uh but uh there
[1408.82 --> 1416.06]  was some uh some build issue with the uh smart os distribution of the new version of node and so
[1416.06 --> 1422.52]  uh we missed a stress test because it was like a few hours late and then after that we were busy with
[1422.52 --> 1428.38]  a few other things so we were we ended up putting it uh a week before and uh and crossing our fingers
[1428.38 --> 1432.52]  yeah can you really like how easy is it to to test that though to stress test that
[1432.52 --> 1440.06]  uh leave your system in production for a day yeah it's uh yeah like my favorite thing about walmart to
[1440.06 --> 1447.48]  say is that we're we're too big to stage um yeah and and the reality is that we could not really
[1447.48 --> 1452.10]  reproduce it for months um and we still can't reproduce it with the actual system the only way
[1452.10 --> 1457.70]  i was able to reproduce it was with with this little script i wrote that was uh creating a very
[1457.70 --> 1465.64]  specific scenario of bursts of traffic um to actually stress node in just the right way to to make it
[1465.64 --> 1472.30]  happen yeah well so long story short though the the whole thing was a big success big win for you big
[1472.30 --> 1478.74]  win for node um let's talk a little bit about you know the actual i mean the implementation of of uh
[1478.74 --> 1483.34]  you know what you guys did and then potentially you know get into happy a little bit so it's my
[1483.34 --> 1488.02]  understanding that you guys started out um using express as that was really the only option at the
[1488.02 --> 1493.72]  time is that right so i i started uh the origins of happy were really uh back at yahoo i was working
[1493.72 --> 1499.54]  on a project called slid for about a year so i started when node was uh just 0.2 just came out
[1499.54 --> 1508.72]  um so i guess it was november three years ago and and i was building a list making a collaborative
[1508.72 --> 1516.50]  list making tool at yahoo and and i used express at the time um it was really the only option um it was
[1516.50 --> 1521.06]  really just express and connect those were the only two things uh and express was built on top of it
[1521.06 --> 1527.06]  and we used that for a while but what was going on you know in that one year is that i found myself
[1527.06 --> 1532.52]  basically building a framework on top of express because express uh gave so little functionality
[1532.52 --> 1538.34]  it basically was just a router with a little bit of uh of helpers but it it wasn't really a full
[1538.34 --> 1545.62]  web framework that did all the things i want in terms of uh redirect the right way and uh and handle
[1545.62 --> 1552.24]  um like rendering views without having to constantly set up the view uh context and um
[1552.24 --> 1559.62]  and at the time also the the middleware ecosystem for express was very very uh very young um i mean
[1559.62 --> 1564.74]  basically i was finding uh express bugs on a daily basis and just and just iming uh uh tj and saying
[1564.74 --> 1573.12]  hey tj another one um and so that that has changed very dramatically but uh when i went to walmart
[1573.12 --> 1579.44]  but i did this i basically i took the uh the express um layer that we've built um in in the in the
[1579.44 --> 1585.26]  slide project which was open source by yahoo um so that was easy and then um we we kind of like said
[1585.26 --> 1590.86]  okay we're going to call this happy and it's going to be basically an express layer that uh that will
[1590.86 --> 1596.72]  add all of everything we needed and if you look at what paypal just did uh with their uh um um kraken
[1596.72 --> 1601.00]  framework they kind of did the same thing they took express and then they realized express by itself is
[1601.00 --> 1607.44]  not really a very useful framework um for a large team so they ended it went and added a bunch of uh
[1607.44 --> 1612.44]  of abstraction and layers on top of that right so we did that for a while and it was working well
[1612.44 --> 1619.60]  but then we uh we started hitting uh the the limits of of what express can do and the biggest one is
[1619.60 --> 1625.66]  the the way the the router is designed in express it's basically just a gigantic array of regular
[1625.66 --> 1630.94]  expressions and all it's doing is that whenever a request comes in it's just it just go through the
[1630.94 --> 1636.42]  array in the order that you added your routes into the array and it's doing a regex match against each
[1636.42 --> 1642.12]  one of them and when it finds a match it calls the function uh that will match it and when you uh and
[1642.12 --> 1647.14]  all the middleware stuff is basically just adding a wildcard match into the array there's nothing
[1647.14 --> 1653.62]  there's no magic there it's a very very um it's kind of beautiful in how simple the the entire
[1653.62 --> 1658.78]  architecture of expresses but when you're working in a in an enterprise environment when you have
[1658.78 --> 1663.98]  multiple team working on the same server you're going to uh want the server to take care of for
[1663.98 --> 1669.14]  example collisions in your routes you don't want to have to end up with you know two routes with the
[1669.14 --> 1675.42]  same path uh two middlewares conflicting on what they're changing um and very fast we got us into
[1675.42 --> 1683.64]  um middleware hell which uh i i'm very proud to say that that was a term that i i started um
[1683.64 --> 1688.84]  probably being like one of the first people to actually use express in in such a large scale that
[1688.84 --> 1696.84]  we experienced it and and it was it was really painful we we wanted the framework to to protect
[1696.84 --> 1702.82]  us from from doing stupid things and it wasn't so we switched to uh director from the nojitsu guys
[1702.82 --> 1708.08]  and we used no director for a little bit um because director just gives you a router and you can use it
[1708.08 --> 1713.38]  as any way you want uh but then we hit limitation there as well because of the way they store the
[1713.38 --> 1720.04]  route tree and at that point we felt pretty good about just doing our our own internals um we're
[1720.04 --> 1727.34]  talking about you know a year and a half into working on this this environment and um and the other thing
[1727.34 --> 1735.74]  is that that when you start to build a real production dependency on on on these things you you kind of
[1735.74 --> 1740.56]  require a different level of maturity from the from the modules you're using from the open source stuff
[1740.56 --> 1749.20]  you're using and we found ourselves um uh trying our best to use like public open source modules but
[1749.20 --> 1756.16]  very slowly but surely moving towards more and more code base that we were we were managing it just
[1756.16 --> 1763.72]  because uh the quality was was uh more uh within our our uh criteria and uh if there was a problem we
[1763.72 --> 1769.44]  can fix it right away we didn't have to fork um or start playing all those games or trying to find
[1769.44 --> 1776.72]  someone on you know twitter to help us uh accept a pull request we've made and so we're still using
[1776.72 --> 1783.12]  a significant amount of open source stuff but uh whenever we we hit a wall with a with a module um
[1783.12 --> 1788.66]  uh we we are much more trigger happy now to fork it and create our own than than we were a year ago
[1788.66 --> 1793.72]  right you guys are much more familiar with the whole environment now as a team and and your your needs in
[1793.72 --> 1800.50]  that environment so there's a lot more confidence in that area i would imagine yeah and and we we're
[1800.50 --> 1805.88]  also uh uh we we feel like we're you know we're we're giving uh we're giving enough back that uh
[1806.70 --> 1812.84]  um like we if you talk to most of the uh the the leader in the node community they're all about you
[1812.84 --> 1819.52]  know small tiny modules you know they all hate frameworks um you know and and it's kind of funny
[1819.52 --> 1823.82]  whenever they they talk about framework that like you always hear one of them will say yeah there's
[1823.82 --> 1827.70]  also you know happy from the from the mall mart guys um which if you're doing large scale stuff
[1827.70 --> 1832.16]  that's actually a good solution but you know really you don't need it um it's always this you know
[1832.16 --> 1838.94]  qualified love yeah uh coming from from from uh a lot of the the core node people which i respect
[1838.94 --> 1844.12]  but at the same time if you work in a large large team um you have a lot of people building stuff you
[1844.12 --> 1849.22]  really want to have a a plug-in architecture that people can build their own stuff and then
[1849.22 --> 1853.22]  just deploy it together without having to coordinate every change without having that
[1853.22 --> 1860.12]  one gigantic scary routing table file everybody has to constantly change uh to get their stuff into
[1860.12 --> 1866.72]  the server um so it's those were the the the things we focused on the last year in terms of
[1866.72 --> 1871.46]  of the framework so it's interesting then because you guys started so you did your own thing and
[1871.46 --> 1876.08]  and with happy you talked about you know how how node the node community loves a bunch of little
[1876.08 --> 1880.80]  tiny modules but uh you you briefly mentioned it but you went through a pretty modular approach to
[1880.80 --> 1887.28]  how you deal with happy right so um first of all you your uh organization name on github is spumco
[1887.28 --> 1892.90]  and uh why don't you real quick tell tell me the story you said about spumco and where that came from
[1892.90 --> 1900.04]  so the the first module was called happy which was uh short for http api
[1900.04 --> 1905.96]  uh so it was really an acronym but then as soon as uh i wrote it down i was like happy happy
[1905.96 --> 1912.90]  joy joy um all my childhood that ran in stimpy days uh just you know came flooding flooding back
[1912.90 --> 1919.50]  and so of course the second module we uh we created was called joy and we called it uh j-o-i just to
[1919.50 --> 1926.10]  stick with the same spelling um style of happy uh and after that basically every new module we created
[1926.10 --> 1934.62]  uh was uh based on some kind of random stimpy character or or episode uh and at some point
[1934.62 --> 1943.56]  we were like over 30 um public uh github projects which made uh life on the official warm at labs github
[1943.56 --> 1949.46]  account quite miserable because uh github doesn't give you like any way to organize your stuff other than
[1949.46 --> 1955.44]  everything is flat right in your in your organization and when you have a couple hundred other people
[1955.44 --> 1960.66]  all using the same github uh organization the dashboard becomes useless so we were like okay
[1960.66 --> 1965.44]  we need to move our stuff to a new org and what are we going to call it and i was like i don't want
[1965.44 --> 1969.92]  to call it another like you know walmart 2 or like let's find let's find something a little more
[1969.92 --> 1977.52]  creative so we we chose spunko which is uh uh spunko with a k with a c is the name of the animation
[1977.52 --> 1985.42]  studio that created ren and stimpy and so we call our our organization spunko with a k uh as a kind of a
[1985.44 --> 1993.86]  homage to uh um to that yeah it's all your all your uh plugins here so uh you guys actually were
[1993.86 --> 1999.88]  brave enough to name one poop and that is the plugin for uh or the module for uh kind of like
[1999.88 --> 2005.98]  exception error handling is that right well the the proper tagline is uh it's a plugin for taking dumps
[2005.98 --> 2012.56]  yeah processing a dump and cleaning up after an uncaught exception uh so that's a little that's funny
[2012.56 --> 2017.32]  but that's hilarious yeah it's a very modular approach now this interesting design is that is
[2017.32 --> 2021.90]  that kind of like to speak true you know to kind of capture the heart of the node community so that
[2021.90 --> 2026.46]  people can pick the modules as they want and kind of mix and match what they want for their different
[2026.46 --> 2033.10]  configuration so i i'm a big believer in uh expansion contraction pattern of development
[2033.10 --> 2039.74]  where you add features to your main uh main framework to the core of the framework and then
[2039.74 --> 2045.34]  as they mature as as you gain some experience of how they work you figure out if they should be
[2045.34 --> 2051.00]  abstracted out into their own uh sub module or if they should stay part of the core system you're
[2051.00 --> 2055.42]  still keeping the same integrated experience overall but uh in terms of code organization you're still
[2055.42 --> 2062.60]  breaking it up so right um but uh i would argue that uh so so happy itself uh the the just a happy
[2062.60 --> 2070.06]  module it's a pretty heavy framework so i won't try to portray it as a lightweight modular solution um
[2070.06 --> 2078.56]  it's taking a very opinionated hands-on approach to to um writing an http uh web server or api server
[2078.56 --> 2084.98]  and the reason for that is that we really want to integrate solution where when you define a route you
[2084.98 --> 2089.52]  can define the caching policy all in one place you can define your authentication you can define your
[2089.52 --> 2096.94]  your uh input validation and and everything just works out of the box you don't have to then start
[2096.94 --> 2102.60]  basically finding the right plugin to do this and the plugin to do that everything we we deemed as
[2102.60 --> 2110.34]  absolutely necessary for building any kind of modern uh web application is built in and and so so that's
[2110.34 --> 2116.50]  that's a core uh uh principle there what we've done though is um whatever we we consider to be
[2116.50 --> 2125.86]  uh more of a of an optional component for example um there's a very popular um um express uh middleware
[2125.86 --> 2131.58]  called um passport that basically everybody's using for all their third-party authentication so we
[2131.58 --> 2137.26]  created a wrapper for that uh and and that's called travel log and so that's not part of core it's part
[2137.26 --> 2142.64]  of uh it's a heavy plugin you can add in the other thing is is that uh we designed a plugin system
[2142.64 --> 2149.00]  to basically avoid all the middleware hell that that we've experienced before so you can actually
[2149.00 --> 2154.06]  describe relationship between plugins one one plugin can actually say i require another one to work
[2154.06 --> 2160.84]  uh a plugin can actually be very specific into the order of execution to say hey first go run this uh
[2160.84 --> 2166.92]  um csrf plugin and then only then run the cookie one or the other way around depending on what you need
[2166.92 --> 2172.06]  and so uh when you're loading them you don't have to worry about the order in which you're loading them
[2172.06 --> 2177.48]  um as long as they describe the the relationship they will the happy loader will make sure that it's
[2177.48 --> 2182.98]  uh done in the right order based on how it's been prescribed so so we've done a lot of that stuff um
[2182.98 --> 2189.62]  we're we're trying to avoid as much as possible uh so we're discouraging people from building
[2189.62 --> 2196.64]  new happy specific plugins as much as possible so like a lot of people are creating these plugins and
[2196.64 --> 2200.30]  they're all very disappointed when they're like they're showing it to me and i was like why is it
[2200.30 --> 2206.96]  the plugin like why is it not just a regular node module that you use um there is this excitement of
[2206.96 --> 2212.02]  you know like getting a putting a stake in the ground and saying i created the you know the happy plugin
[2212.02 --> 2220.10]  for this yeah um but in practice it's not necessary so uh we look at plugins as basically um something
[2220.10 --> 2224.16]  that is directly interacting with the framework that's directly adding functionality to the framework
[2224.16 --> 2230.48]  uh that is defining routes um if if you if all you want to do is uh you know parse a multi-form
[2230.48 --> 2237.28]  uh you know response or request uh i would say don't build a plugin for that just just write a module
[2237.28 --> 2244.22]  right yeah it's a different way of viewing it i guess people kind of it's a i don't know what the
[2244.22 --> 2250.50]  what the mindset is right but uh let's say you know like go right it's a pretty early adoption stage
[2250.50 --> 2257.54]  for for the program language of go and so people love to um write like the port of another solution
[2257.54 --> 2263.90]  for that thing right so people say oh if they're using um you know let's say you didn't have your
[2263.90 --> 2268.44]  your passport wrapper for for happy then they would say well people use passport for express i want to
[2268.44 --> 2274.42]  write the passport for for happy and i think it causes some fragmentation in the community right
[2274.42 --> 2279.38]  because it it i you know you can talk a long time about what the motivations behind that
[2279.38 --> 2284.34]  kind of looking for like some sort of fame or or whatever but at the same time like they want to
[2284.34 --> 2289.92]  help the community by providing a solution so i think node and npm specifically kind of kind of
[2289.92 --> 2294.34]  makes it pretty simple right to just use npm modules in general and so perhaps you're right that it makes
[2294.34 --> 2299.48]  more sense to to write a module that um you know is easier to manage in that way than than trying to do
[2299.48 --> 2304.94]  a specific plugin for happy yeah and and the other thing is that uh really all you need in order to
[2304.94 --> 2312.14]  create a happy plugin is to export export one function called register and so that's all that's
[2312.14 --> 2317.84]  all we're looking for when we're loading a plugin so um but you know if if you're writing a module and
[2317.84 --> 2324.58]  you really want it to be easily um absorbed into the happy ecosystem then you know write your plugin
[2324.58 --> 2329.62]  write your module the way you would write it for anybody to use and then just add one more exported
[2329.62 --> 2337.12]  function um so it so it can also work as a um as a plugin for happy and i would argue that you know
[2337.12 --> 2341.82]  if you're doing that might as well you know export one more function and then it can also work as a
[2341.82 --> 2346.88]  uh as a middleware for express uh if you know if you design it properly then then it should be pretty
[2346.88 --> 2352.60]  easy to uh to bridge the two um for most of the the the basic stuff that people are looking for
[2352.60 --> 2359.86]  let's pause for a minute and give a shout out to our sponsor fresh books now we've been using fresh
[2359.86 --> 2366.12]  books literally for years and years and years i gotta say probably as far back i can remember
[2366.12 --> 2375.32]  using fresh books is like 2007 2008 maybe but they're a staple in our business and what we do we
[2375.32 --> 2381.70]  would literally be lost if we didn't have fresh books to use for our invoice management we absolutely
[2381.70 --> 2390.08]  hands down red-faced love fresh books absolutely so just in case you didn't know we love fresh books
[2390.08 --> 2395.96]  but if you're the kind of person who's still sending your your invoices with word or excel and
[2395.96 --> 2400.64]  maybe you've kind of got your receipts kind of shoved into a shoebox kind of keeping track of your
[2400.64 --> 2406.28]  expenses there and just kind of hoping things will work out well with fresh books you can easily do all
[2406.28 --> 2411.20]  of that you can create invoices online you can capture and track uh capture and track expenses on the go
[2411.20 --> 2417.94]  you can get real-time business reports with a few simple clicks it's super super easy perfect for any
[2417.94 --> 2423.68]  large or small business we absolutely love it and we want you to try it today for free you can sign up
[2423.68 --> 2429.52]  today at get fresh books.com and here's the delicious part that fresh books is doing for our listeners
[2429.52 --> 2435.26]  every day they're giving away a birthday cake that's right a birthday cake to someone who signs up for a
[2435.26 --> 2439.82]  new account from this show so for your chance to win enter the changelog in the show in the uh
[2439.82 --> 2444.68]  and how did you hear about a section when you sign up for a new account and just know that with
[2444.68 --> 2452.88]  fresh books every day could be your birthday so go sign up at get fresh books.com so when was 1.0
[2452.88 --> 2457.60]  of happy released or i guess a better question i'm not sure what your versioning structure looks like
[2457.60 --> 2465.08]  when was happy production ready released uh well it was in production before 1.0 but um
[2465.08 --> 2473.14]  we uh so we're using the numbers to basically it's just a regular stammer contract of uh of you know
[2473.14 --> 2478.64]  a patch is just a bug fix that's backward and forward compatible and then uh minor is uh backward
[2478.64 --> 2487.08]  compatible and major is not backward compatible uh and so 1.0 came out i think in april uh we um
[2487.08 --> 2494.38]  we got it out right together with the node uh dot 10 release and that has been used in production for
[2494.38 --> 2505.70]  uh um since then and uh we're working on um 2.0 um right now uh hoping to ship it out next week and
[2505.70 --> 2513.92]  there are really no major uh changes in it it's just that um it's been long enough that we've uh
[2513.92 --> 2520.44]  accumulated uh a little too much uh backup compatibility crap around it um we've you know
[2520.44 --> 2525.08]  as as we've been using it as people have been using it we got a lot of feedback and a lot of
[2525.08 --> 2530.18]  the decisions we made you know in april were no longer valid uh in in september all of a sudden
[2530.18 --> 2535.02]  we're like oh we really don't want this configuration value to be in the same node as this configuration
[2535.02 --> 2541.22]  value because it doesn't it doesn't work right when you're trying to use defaults and so we made
[2541.22 --> 2546.72]  back compatible changes but it got to the point now where uh it's it's kind of time to clean it up
[2546.72 --> 2554.02]  and and do a breaking release so it's a very non-dramatic 2.0 yeah it was interesting um i was
[2554.02 --> 2559.34]  watching i don't know what video it was but uh like a tutorial happy video that you all put on and
[2559.34 --> 2565.52]  and i just noticed somebody was you know adding uh adding routes adding handlers with the route method
[2565.52 --> 2569.96]  on the server and then i saw in the documentation that there was the add route method and so i was like
[2569.96 --> 2575.10]  i wonder where you know something's wrong or you know in my head i was like i bet there's a major
[2575.10 --> 2579.42]  change coming out that that's like breaking you know that's either deprecating this or breaking it
[2579.42 --> 2584.62]  or something and it was interesting to me that that you all have a issue open for 2.0 breaking
[2584.62 --> 2589.90]  changes that's a neat way to do it and uh it was pretty um you know simple for me to figure out what
[2589.90 --> 2595.94]  was going on and why i saw the kind of discrepancy between the two so um how how much you know i guess
[2595.94 --> 2604.16]  my question is how how actively is your you know issues are your issues on the on the project watched
[2604.16 --> 2608.76]  like what do most people know that these breaking changes are coming that are using happy or or you
[2608.76 --> 2613.10]  know i guess that's the an awkward way to say basically but how much activity have you guys
[2613.10 --> 2620.18]  had around like the open source issues kind of pull requests kind of a thing um so there's a couple
[2620.18 --> 2626.28]  hundred people that are actually actively watching the the issues um at this point pretty much everybody
[2626.28 --> 2631.08]  who's using it in any kind of serious capacity if you have a production dependency on it you're
[2631.08 --> 2641.24]  watching what's going on and we we have uh we've basically um went all in on on github as our
[2641.24 --> 2645.94]  everything you know it's our project management solution our team communication solution it's basically
[2645.94 --> 2652.46]  we put everything there there there is no other like ticketing system for for happy like in privately
[2652.46 --> 2658.16]  in walmart or anywhere else um we basically made a decision that it's an open source project and we're
[2658.16 --> 2663.78]  going to run it completely as an open source project even though um you know we like i get bug reports
[2663.78 --> 2668.14]  from you know internal teams and i always say like go open an issue and they're like really like this
[2668.14 --> 2672.38]  issue you want me to like put it on the web i was like yeah go open an issue it's like i'm not
[2672.38 --> 2676.50]  embarrassed by it it's like it's a bug and we'll fix it you'll go open an issue i mean people will see
[2676.50 --> 2683.92]  the the the the commit so it's not like you know you can hide it sneak it by him yeah um but we've
[2683.92 --> 2689.32]  also made extensive use of milestones even before uh github kind of cleaned their act with versions
[2689.32 --> 2694.80]  um so we've been using milestone quite extensively so we don't do release notes because all we're doing
[2694.80 --> 2701.94]  we're like we're very religiously tagging everything to uh to an issue and then the issues are all part of
[2701.94 --> 2706.30]  of milestones so you can see exactly if you just look up you want to say okay what changed between
[2706.30 --> 2711.16]  this and this you can just bring up the milestones and you can see exactly what issues were associated
[2711.16 --> 2716.46]  and then once we did that we kind of added the uh the breaking change uh uh label and we said hey
[2716.46 --> 2721.42]  you know what if we're gonna make a change that's gonna be breaking um and we and before we were 1.0
[2721.42 --> 2726.68]  you know basically every minor release was a was a breaking change like every one of them was like
[2726.68 --> 2733.60]  oh yeah you can't upgrade unless you like rewrote your entire app um and and after that it became
[2733.60 --> 2739.70]  a lot more less sorry a lot less significant i think we made like two breaking changes throughout
[2739.70 --> 2746.64]  1.0 and both were for security reasons so like we changed the default of uh like multi-part uh parser
[2746.64 --> 2752.48]  not to create files by default um stuff like that that we felt like you know this is a a breaking change
[2752.48 --> 2757.40]  worth making um yeah the note the whole node community had to kind of to do that pretty much
[2757.40 --> 2766.20]  right if i remember correctly yeah so um we we we had a couple of breaking changes in 1.0 that were just
[2766.20 --> 2773.24]  that important um but overall uh it hasn't been a big deal and now we're working on 2.0 and um
[2773.24 --> 2780.54]  we're kind of like we have the one issue that we collect everything and it's more of like edited and
[2780.54 --> 2786.02]  it's it's a lot more friendly for you to understand but then every individual issue that is actually the
[2786.02 --> 2792.04]  one where the change is being made we also tag that so um because i'm not expecting everybody to be able
[2792.04 --> 2798.02]  to sit there and go through my you know 300 breaking changes issues in 2.0 and like read every one of
[2798.02 --> 2804.26]  those i mean that would be awful so instead like we're you know we're basically doing it that way and
[2804.26 --> 2809.18]  it's also great because then once we're done writing a migration guide it's just kind of like doing
[2809.18 --> 2814.04]  some editorial on that particular issue yeah uh and then and that and that's how we do it too like
[2814.04 --> 2818.18]  we're going to go in and edit that and that will be the migration guide like we're not going to
[2818.18 --> 2824.48]  actually like publish a like a wiki page of doing that so do you know anyone like that's using happy
[2824.48 --> 2832.14]  in production besides you guys at a at a at a large scale i don't know about large scale um i know that
[2832.14 --> 2839.86]  uh mozilla was using it for some of their identity stuff um for some of their the browser id uh they're
[2839.86 --> 2844.50]  using happy i don't know what's the status right now but they they uh were using it as of a few
[2844.50 --> 2853.02]  months ago um i know uh mastercard um is using it for some of their new project uh con and asked the the
[2853.02 --> 2860.16]  publisher uh they're using it as a as a building block for their new uh um uh cross-platform environment
[2860.16 --> 2867.04]  uh so and of course walmart is using it uh um uh quite heavily right now for mobile and we're
[2867.04 --> 2872.88]  looking this year to expand beyond mobile to a lot of other uh areas of the of the e-commerce business
[2872.88 --> 2882.30]  so yeah so it has some uh significant adoption um but then others you know um have have made a decision
[2882.30 --> 2889.98]  to uh uh either build their own or use express so uh i i think i the the default behavior
[2889.98 --> 2894.46]  for other people right now is um is to pick express because everybody else is using express
[2894.46 --> 2902.72]  and then um they they tend to once they got into express they they feel like it's too much right now
[2902.72 --> 2907.22]  to make changes so they just keep building more and more layers on top yeah to make it more manageable
[2907.22 --> 2914.60]  for them um so i'm hoping that you know as this time passes and more people are seeing what we're
[2914.60 --> 2921.98]  doing with it um you know they can uh they can make a a different decision and for example like if
[2921.98 --> 2926.56]  you you know if you if you have an existing api and you want to take the uh the proxy strategy
[2926.56 --> 2932.18]  to migrate to a new stack which is a it's a really great uh um approach in terms of you know sticking
[2932.18 --> 2937.48]  your your layer in between and slowly making changes you don't have to go in yeah otherwise you
[2937.48 --> 2942.10]  have to sit you know sit in in in dark room for a year and you know and rebuild everything and of
[2942.10 --> 2945.98]  course we know how well that works in production like when you ship the new version and nothing
[2945.98 --> 2950.58]  works right and then you know it's a year behind and probably get canceled and everybody quits right
[2950.58 --> 2958.46]  so yeah and and and basically you can you can uh deploy happy with probably about 30 lines of your
[2958.46 --> 2964.46]  own code and get all the proxy functionality immediately at walmart you know walmart scale
[2964.46 --> 2969.16]  yeah so that that's kind of neat yeah i was gonna ask i mean that that's kind of my next
[2969.16 --> 2973.78]  question was what you know what's the future of walmart look like for this kind of stuff so how
[2973.78 --> 2979.84]  much kind of so you're on the mobile team how much um you know i don't know what the best way to ask is
[2979.84 --> 2985.70]  but how much impact have you had on the other teams in walmart so it was kind of interesting because uh
[2985.70 --> 2992.34]  there was about a year ago there was some effort within the uh the people in the company who like to set
[2992.34 --> 2997.08]  standards and they came to me and they said we you know more people are asking us about notes so
[2997.08 --> 3001.80]  can we make it the formal that like happy is the official framework at walmart and i said no
[3001.80 --> 3006.28]  like i don't want that to be the case i don't want anybody to use happy because some policy is
[3006.28 --> 3011.46]  dictating it um because i wouldn't use it because you're telling me what to use so so i don't want
[3011.46 --> 3017.60]  to do it to other people um so we never like actually like promoted within the company and people
[3017.60 --> 3021.74]  just picked it up all on their own it's kind of neat all of a sudden like we're getting uh issues open
[3021.74 --> 3026.02]  and then like after like a few back and forth they're like oh wait a minute are you from the
[3026.02 --> 3032.04]  santa clara office um so it's kind of like this this funny where like we were meeting other people
[3032.04 --> 3038.30]  on like the irc channel like you know co-workers that we have never met before um so some of the other
[3038.30 --> 3044.42]  um other teams were building like smaller uh like like panels for the main website like
[3044.42 --> 3050.08]  recommendations and like the social stuff uh they're using happy to build their own stuff um and
[3050.08 --> 3054.54]  they have like their own deployment their own servers um and they're like they you know every
[3054.54 --> 3060.68]  month they'll come back um but the the real goal um for for my team this year is going to be to kind
[3060.68 --> 3067.78]  of like look and see where we can add value um beyond mobile um as we're uh as walmart you know
[3067.78 --> 3074.32]  uh walmart uh e-commerce uh as a whole is is moving to uh new apis and new technologies on the back end
[3074.32 --> 3082.94]  um we're all going to have to move to that stack uh and then also we're expanding our our mandate um
[3082.94 --> 3089.12]  to other countries so right now the mobile team is uh focused primarily on the u.s uh where we have
[3089.12 --> 3097.76]  walmart and sam's club and we also are um uh working on the mobile apps for asda which is the walmart brand
[3097.76 --> 3103.90]  in the uk um and walmart is active in a lot more other countries including you know mexico and canada
[3103.90 --> 3111.64]  and china and brazil and it's a very long list uh so we are um at some point going to expand um
[3111.64 --> 3117.70]  to those so it's really seeing how how much we can scale the node um uh engineering process
[3117.70 --> 3124.54]  uh beyond just you know scaling the the software but also scaling the the the engineering itself
[3124.54 --> 3130.76]  like the the writing of the software itself we're gonna pause the show for just a minute and give a
[3130.76 --> 3135.10]  shout out to our awesome sponsor top towel they've been sponsoring the show for a little bit and we've
[3135.10 --> 3138.34]  had a chance to tell you about some really awesome stuff they're doing i've been working with
[3138.34 --> 3143.70]  brendan their co-founder and cto and i mentioned that you know i wasn't quite sure what to expect
[3143.70 --> 3147.90]  from them and i was but i was excited about what they're doing they're helping developers
[3147.90 --> 3151.96]  who want to freelance with some really awesome companies find ways to do that
[3151.96 --> 3156.34]  and it's their mission these guys are the real deal they're engineers themselves from top to bottom
[3156.34 --> 3160.92]  they're not technical recruiters trying to pimp developers so if that's what you think then you've
[3160.92 --> 3166.12]  got you've got them completely pegged wrong they're a network of elite engineers all around the world who
[3166.12 --> 3171.04]  work with some really awesome clients and for those of you out there who are freelancing or or would
[3171.04 --> 3175.18]  like to freelance you've got to check out top top you can work on special projects with companies
[3175.18 --> 3181.32]  like airbnb artsy audio and many others you can work remotely you can go to andrew's favorite place
[3181.32 --> 3187.32]  which is on a beach or anywhere in the world it's there there no office is required and to get
[3187.32 --> 3192.42]  started head to top.com slash developer click join the best and because they want to work with only
[3192.42 --> 3197.28]  the best senior engineers out there they've got a well thought out four-stage screening process that
[3197.28 --> 3202.42]  begins with a personal phone call via skype to kind of get to know who you are and introduce you to
[3202.42 --> 3206.80]  who they are and what their mission is and see if you're a fit and from end to end the screening
[3206.80 --> 3212.34]  process includes an english speaking test a timed algorithm test technical interviews with core
[3212.34 --> 3217.62]  top top top engineers as well as a test project and once you've made it past the screening process
[3217.62 --> 3222.26]  the sky is the limit and if you think you have what it takes head to top.com slash developer right
[3222.26 --> 3228.78]  now to get started tell them the changelog sent you and enjoy now back to the show one of the things i
[3228.78 --> 3233.54]  wanted to kind of implore uh i don't know if that's even the right word at this point but to kind of
[3233.54 --> 3238.50]  congratulate or maybe thank you guys about was you know we've had a on the show a few times in the
[3238.50 --> 3243.86]  last couple weeks we've had discussions around you know how one deployment tool will come out and
[3243.86 --> 3249.44]  another deployment tool will come out and say you know we we are better than x or we don't suck as
[3249.44 --> 3254.14]  much as x and they'll kind of take a shot at the person that they're they're building on top of and uh
[3254.14 --> 3257.24]  you know i was looking through happy and you guys obviously are i wouldn't say you're a competitor
[3257.24 --> 3262.38]  with express but you've definitely kind of entered the same space as express and i don't see anything on
[3262.38 --> 3266.06]  you know your website saying like we're better than express or the reason we're doing this because
[3266.06 --> 3270.20]  express stinks and and i personally just wanted to like thank you guys for that because that's a i
[3270.20 --> 3275.52]  think that's a good a good thing to get away from in the open source community well i mean there's a
[3275.52 --> 3279.54]  couple reasons for that i think i had like in the last year i had one tweet where i said basically
[3279.54 --> 3285.20]  something like you know it's it's time if you're doing something serious with node it's time to start
[3285.20 --> 3292.36]  looking beyond express uh i think i was a little more snarky about it but um but really like there's
[3292.36 --> 3297.90]  there's there's two ways of looking at it one is um we're we are clearly the underdog in this space
[3297.90 --> 3306.68]  um uh both express and and restify uh which is the the joint um um api framework i have a lot more
[3306.68 --> 3313.12]  um deployed uh use cases than happy has right now um we have more revenues going through it so you know
[3313.12 --> 3321.04]  combine there's definitely more money being bet on on happy than everybody else combined um but that's
[3321.04 --> 3326.52]  not a very meaningful statistic yeah you're saying it um basically you're saying walmart's using it at
[3326.52 --> 3332.96]  that point yes so well i know if mastercard put some some real revenue on it too i mean i think
[3332.96 --> 3340.94]  between those two it's going to be like pretty significant um but if you're the underdog um and
[3340.94 --> 3348.92]  you're starting to basically uh um say nasty things about the the injury leader like you're really
[3348.92 --> 3353.30]  coming off as a dick yeah i mean you're not really coming off as like you know somebody who's like
[3353.30 --> 3361.26]  and the thing is the people who have uh uh create express um you know particularly the uh the formal the
[3361.26 --> 3369.56]  formal um uh learn boost uh guys they're now with uh um wordpress spot they're they're um cloud up
[3369.56 --> 3378.28]  startup but uh or spinoff but um those are all fantastic guys i mean they are uh just awesome
[3378.28 --> 3383.90]  people and brilliant engineers so for me to go out and like say anything better about their work i
[3383.90 --> 3389.56]  disagree with the choices they've made um and i think that architecturally what they've produced is
[3389.56 --> 3395.78]  not compatible with with the parts i want to have right but like to say that it's bad or it's it's just
[3395.78 --> 3401.98]  going to be stupid um and the thing is those are very two different philosophies express is very
[3401.98 --> 3409.30]  lightweight it's basically just giving you very very a little bit of sugar um on top of note and
[3409.30 --> 3415.74]  that that's what most people want so i don't think i need to be a yeah we don't need to actively go
[3415.74 --> 3419.86]  against it now like but at the same time like we're definitely trying to get more people to adopt happy
[3419.86 --> 3425.72]  um we're definitely trying to to highlight you know where we think we're better than than uh other
[3425.72 --> 3430.72]  frameworks in terms of the functionality we provide but i think you can do it without you know without
[3430.72 --> 3436.00]  being a dick yeah absolutely and i think that's that's what you all are doing so i uh i congratulate
[3436.00 --> 3443.10]  and thank you for that so for the listeners of the uh new listeners of the show um we do at the end of
[3443.10 --> 3448.96]  every episode we ask the same questions to our guests so aaron i'll go ahead and ask them to you now um
[3448.96 --> 3454.28]  it's the first one is for a call to arm so something around happy or any one of its modules
[3454.28 --> 3458.42]  or in node in general that you'd like to see the open source community kind of pitch in and contribute
[3458.42 --> 3466.28]  to uh mostly just use it um we really are looking for more people to give it a try um and the thing
[3466.28 --> 3471.14]  is if you try it and you don't like it please tell us why like go open an issue and say i tried it
[3471.14 --> 3476.12]  didn't like it here's why i didn't like it good luck with it um like we love issues we actually don't
[3476.12 --> 3481.60]  have a google group um like most other projects because we we just want everybody to open issues
[3481.60 --> 3486.78]  like and we have a label called discussion so we're basically using github issues just like a
[3486.78 --> 3496.84]  mailing list um and we found it it's basically it's creating a a psychological um barrier that people
[3496.84 --> 3503.50]  are less likely to be spammy and and um uh and troll uh where the mailing list is kind of like expected
[3503.50 --> 3508.98]  right so it's working really well but like really like like my request is for people to just go and
[3508.98 --> 3517.98]  give it a try and play with it um find bugs um ask for more stuff and uh and we're happy to uh to to
[3517.98 --> 3523.34]  engage awesome if you weren't working at walmart or working unhappy what would you be doing
[3523.34 --> 3532.12]  um i would be a full-time farmer that's awesome much right now i'm only a part-time farmer i would
[3532.12 --> 3537.94]  i would uh if i if i could afford to uh to do that full-time that that's definitely what i would be
[3537.94 --> 3543.04]  doing there's a there's a famous farming joke of a farmer goes to vegas and and win the jackpot so
[3543.04 --> 3547.14]  everybody's saying like what are you gonna do now and he kind of looks up and he thinks about it and
[3547.14 --> 3553.82]  says um i think i can continue being a farmer for another five years that's awesome what do you what
[3553.82 --> 3557.54]  would you farm what do you you live out in california so are you uh you into like avocado
[3557.54 --> 3564.44]  uh i actually like i'm not a big fan of the the orchard stuff so i have a small apple orchard but
[3564.44 --> 3572.58]  mostly uh a lot of vegetables um and i have uh quite a lot of uh um animals between uh uh chicken
[3572.58 --> 3582.10]  and ducks geese emus um alpacas pigs um a bunch of beehives so that's cool uh yeah beehives you're
[3582.10 --> 3586.84]  definitely the first guest that we've had that has said that but it's still it kind of is a recurring
[3586.84 --> 3592.38]  theme it's very rare for us to get you know a um somebody that we would say what would you rather
[3592.38 --> 3596.44]  be doing and they would say oh i'd go into another you know technology industry or something
[3596.44 --> 3601.48]  like that typically developers and people that that's in my experience that sit behind a computer
[3601.48 --> 3606.90]  all day tend to want to do something with their hands if they had more time you know so for you
[3606.90 --> 3611.34]  it'd be farming for me it'd be woodworking and and some people it's surfing and all that so yes
[3611.34 --> 3616.30]  it's a common theme among developers that i found to i agree with you kind of dream about doing things
[3616.30 --> 3623.78]  with your hands woodworking and bees yeah cool so i uh i actually uh um i gave a talk at uh real time
[3623.78 --> 3632.96]  um in october uh basically all i did was talk about food for an hour uh to engineers and uh
[3632.96 --> 3639.12]  it was like by far the the most insane talk production i've ever uh put together it was four
[3639.12 --> 3644.66]  months of uh of preparation i had to actually uh rent a u-haul and drive it all the way to portland
[3644.66 --> 3651.92]  from california because i had too much stuff i couldn't ship it that's crazy yeah you did it yeah so
[3651.92 --> 3657.88]  so developers i'm sure we're very uh glad to hear you talk about food it was fun it was uh it was it
[3657.88 --> 3662.24]  was like a psychotic you know like i think like the budget was like over five grand for the talk it
[3662.24 --> 3667.38]  was crazy wow but uh yeah and the video is online so uh you should check it out yeah we'll have to
[3667.38 --> 3672.38]  link to that uh our last question is for a programmer hero somebody in your in your life that has been
[3672.38 --> 3681.16]  influential um i don't think anybody has been influential but uh i would say uh roberta williams
[3681.16 --> 3687.98]  would be my my childhood engineering hero uh of course if you don't if you're if you're not as
[3687.98 --> 3695.96]  old as me um she created all the king quest games um so uh she she she together with her husband
[3695.96 --> 3703.90]  ken they created a sierra online yeah um and so yeah so i grew up on on those games and uh and you
[3703.90 --> 3707.20]  know all i want to do is kind of like reverse engineer them and figure out how they're done
[3707.20 --> 3714.44]  um played my first king quest you know when i was uh probably 10 or 11 year old so
[3714.44 --> 3721.64]  that's cool yeah i uh i have fond memories of games that i played when i was a kid the the one thing
[3721.64 --> 3728.80]  about this industry that has uh has kind of amused me or shocked me at kind of both levels is uh
[3728.80 --> 3733.62]  you know you expect a lot of your co-workers to have spent a lot of their childhood playing video
[3733.62 --> 3738.92]  games on the computer and you know for whatever reason a lot of developers just didn't didn't come
[3738.92 --> 3743.54]  that route so it's kind of interesting to me to bump into someone else that that you know enjoyed a
[3743.54 --> 3748.08]  lot of the the old school games that uh that perhaps a lot of the newer developers kind of never even
[3748.08 --> 3754.12]  heard of yeah my kids are playing king quest now so it's fun i they're playing right next to me and
[3754.12 --> 3759.50]  they keep asking me like how do you spell this how do you spell that that's awesome yeah well cool well
[3759.50 --> 3765.00]  hey i wanted to say thanks again for joining us on today's show we're here with aaron hammer from
[3765.00 --> 3770.70]  walmart labs and spumco as they're so noted on github uh talking about happy and black friday and
[3770.70 --> 3775.38]  and success it was and that you guys are definitely doing a uh a pretty awesome thing for the node
[3775.38 --> 3780.42]  community and and i mean shoot node should write white papers about walmart because i think it will
[3780.42 --> 3787.82]  help to pre preemptively squash any node can't scale arguments after hearing the uh the success of
[3787.82 --> 3793.32]  black friday but um i also wanted to give a shout out to our sponsors digital ocean and top towel for
[3793.32 --> 3798.42]  supporting the show you can go to digitalocean.com to set up your cloud server today and make sure you
[3798.42 --> 3804.08]  use our promo code changelog sent me that's changelog sent me in all caps to get a ten dollar hosting
[3804.08 --> 3810.24]  credit and if you want to freelance with companies like airbnb artsy or ideo you can head to toptow.com
[3810.24 --> 3815.28]  slash developer and click join the best to see if you have what it takes to join toptow's network of
[3815.28 --> 3821.20]  elite engineers again the url is toptow.com slash developer and that's it for this week thanks again
[3821.20 --> 3825.32]  to erin hammer for joining to erin i said that funny thanks again to erin hammer for joining us
[3825.32 --> 3829.44]  and also thanks to the listeners for tuning in and for your support if you haven't yet you can
[3829.44 --> 3834.44]  subscribe to the changelog weekly it's our weekly weekly email where we share everything that hits
[3834.44 --> 3840.50]  our open source radar you can subscribe at the changelog.com slash weekly uh i think we're off next
[3840.50 --> 3846.26]  week right we're gonna gonna encourage all of our developer friends and listeners to enjoy the
[3846.26 --> 3852.42]  holidays with your family and loved ones and we will be back uh sometime in the new year in the new
[3852.42 --> 3856.66]  year so until then guys let's say goodbye bye
[3856.66 --> 3872.52]  you
[3872.52 --> 3876.16]  yeah
[3876.52 --> 3876.70]  you
[3876.70 --> 3880.60]  yeah
[3880.60 --> 3880.72]  you
[3880.72 --> 3910.70]  Thank you.
