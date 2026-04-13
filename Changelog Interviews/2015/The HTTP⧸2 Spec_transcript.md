[0.00 --> 14.70]  welcome back everyone this is the change log and i'm your host adam stekowiak this is episode
[14.70 --> 21.68]  161 and on today's show we got ilio gregor joining us today he's an internet plumber as
[21.68 --> 29.00]  he said before working at google working on the http2 spec uh the precursor to this was known as
[29.00 --> 34.88]  speedy so if you've played with speedy whatsoever you know what what h2 is all about or what it's
[34.88 --> 39.18]  what it's proposed to you about the spec is finalized we talked deeply about it this whole
[39.18 --> 45.04]  conversation is the definitive conversation around h2 and what it's all about binary
[45.04 --> 52.24]  binary framing layer uh pipelining multiplexing header compression also known as hpack server push
[52.24 --> 60.54]  tls time to glass upgrading support adoption you name it we covered it this is the definitive
[60.54 --> 69.76]  conversation around the h2 spec we have three awesome sponsors code ship code school and also
[69.76 --> 78.28]  dream host our first sponsor is code ship very hosted continuous delivery service focusing on speed
[78.28 --> 85.12]  security and customizability you can set up code ship in your app in a matter of seconds and
[85.12 --> 89.58]  automatically to pull your code when your tests have passed code ship supports your github and your
[89.58 --> 95.26]  bitbucket project so no worries there and you can get started today with our free plan or you can go
[95.26 --> 101.54]  with a premium plan and stay at 20 off using our code it'll save you 20 off any plan you choose
[101.54 --> 108.56]  three months use the code the changelaw podcast head to code ship.com slash the changelaw to get
[108.56 --> 110.50]  started and now on to the show
[110.50 --> 122.56]  all right jared we're back we got ilia the internet plumber himself on here third time on this show
[122.56 --> 127.52]  what do you think what do you think jared i think three times puts him into an elite group of people
[127.52 --> 137.08]  that's right smoking jacket and all yes previously on episode 55 episode 144 back in february we
[137.08 --> 142.96]  talked about github archive ilia we talked about nightly which was his turn into changelaw nightly
[142.96 --> 148.42]  um pretty pretty fun stuff everybody's enjoying that nightly email that we've been shipping out but
[148.42 --> 153.18]  uh welcome back to the show ilia thanks thanks for inviting me back it's always fun chatting with you
[153.18 --> 160.48]  guys and uh today's show is all about http 2 which will be a tongue twister for me i don't know about
[160.48 --> 168.36]  you ilia but do you get tired of saying http 2 1 whatever oh i tongue tied i think every other
[168.36 --> 173.94]  sentence i say contains http so i don't notice it anymore have you found a way to say it faster or
[173.94 --> 181.44]  more i don't know that people can actually understand it other than geeks well if you're talking to
[181.44 --> 187.66]  geeks you can actually say just h2 which is a valid name uh for the alpn upgrade token which we'll
[187.66 --> 194.26]  talk about at some point h2 i like that that is a lot easier to say h2 is a lot easier better than
[194.26 --> 202.22]  http 2 and even when i'm trying to say it just well i still stumble over it but anyways so you know
[202.22 --> 205.48]  welcome back do you want to give another introduction for those who may not know who you are i know you
[205.48 --> 210.60]  were on 55 and 144 we talked heavily about who you are and you described yourself as an internet plumber at
[210.60 --> 216.16]  google so anything else you want to add to that no i think that's that's pretty much it so i work on
[216.16 --> 221.80]  the developer relations team at google in particular focus on web performance or work very closely with
[221.80 --> 229.02]  the chrome team and as of late i've been doing lots of work in the web performance working group so
[229.02 --> 235.68]  trying to define and improve existing apis in the browser to allow developers to build better
[235.68 --> 241.80]  applications and h2 is not related to the web perf group it's part of the itf effort but it's definitely
[241.80 --> 248.24]  something that was a big effort within chrome we'll talk about speedy of course and something that i've
[248.24 --> 255.42]  been very passionate about and i said i guess since this show is all about h2 since you've cracked that
[255.42 --> 260.52]  nut we can say that which saves me some stumbling but if we're going to talk about h2 then we've got to
[260.52 --> 266.10]  go back and talk about h1 and uh talk about the history of this spec that we've been living in and
[266.10 --> 271.16]  since you've you've been hanging out in that area what's the best way to talk about the basics of what
[271.16 --> 278.16]  the original spec was and how it turned into speedy and how it turned eventually into h2 sure so i'll i'll
[278.16 --> 284.32]  try to keep it uh brief but as you said it's good to kind of rewind the the time clock and understand
[284.32 --> 291.08]  how we got to where we are today right um and of course everything starts with uh htp 0.9 which is
[291.08 --> 296.22]  tim berners-lee basically creates this very simple protocol it's literally one line that says get you
[296.22 --> 301.72]  you give it the name of the resource you hit enter and you get back a resource right so this is about
[301.72 --> 308.84]  uh 93 94 and the idea was i just want to retrieve a text document because that's what it's supposed to
[308.84 --> 315.74]  be http right hypertext transfer protocol right um then after that uh this web thing became kind of
[315.74 --> 321.92]  popular and people figured that hey um we would like to actually fetch other things uh as well so
[321.92 --> 327.18]  you know somebody had this crazy idea of putting images into a document and other people started
[327.18 --> 331.88]  inventing other mechanisms to style things like style sheets and then of course later we got javascript
[331.88 --> 337.02]  and we started kind of building up these use cases and we also realized that
[337.02 --> 342.48]  uh it's nice to be able to say like cache a resource instead of having to fetch it all the time
[342.48 --> 349.22]  so all of these use cases were emerging from the community there wasn't an official effort around it
[349.22 --> 355.16]  like a working group or on itf effort now this was basically just people picking up http and just
[355.16 --> 360.94]  building servers and just saying like hey i dreamt up with this cool feature caching um so here it is
[360.94 --> 366.78]  and then other browser and server implementers would just kind of pick and choose
[366.78 --> 373.40]  and say like okay i like this feature and whatnot and the way we arrived at http 1.0 which was uh in
[373.40 --> 378.70]  1997 uh it wasn't actually an official standard in the sense that somebody sat down and wrote
[378.70 --> 382.90]  everything from beginning to an end rather it was a document that tried to capture the existing best
[382.90 --> 388.56]  practices so in the period of like four years starting from when http first came out when tim
[388.56 --> 392.68]  berners-Lee first introduced it to like four years later there was just a lot of emergent behavior
[392.68 --> 397.96]  and in http 1.0 we tried to just like document it and that's that's all it was there wasn't even
[397.96 --> 402.02]  like a large attempt to rationalize at all it was just like here are the best practices that you'll
[402.02 --> 406.26]  find on a common web server today so that's and then that's point nine is that going into 1.0 and
[406.26 --> 411.42]  everything right so that that's what became 1.0 effectively right 1.0 was an attempt to capture
[411.42 --> 417.30]  like this best practices and the common usage patterns on the web and then once we did that
[417.30 --> 423.82]  uh in with 1.0 there was a second effort which was 1.1 which took another about two years or so
[423.82 --> 431.94]  uh to actually go back and start like cleaning up the spec so to introduce common language common terms
[431.94 --> 436.72]  um into the spec such that it becomes kind of rational and more easier to implement for
[436.72 --> 446.72]  uh new servers and user agents and effectively uh when hp 1.1 came out which is in 1999 uh
[447.30 --> 452.26]  that's you know that's the web though that's the hp protocol rather that we've built the web on
[452.26 --> 457.92]  so there was that initial burst of creativity we captured it we kind of cleaned it up and then we
[457.92 --> 462.64]  just kind of left it there and as you were well aware if you think about if you've been online in
[462.64 --> 469.68]  1999 and then you've visited the web recently the web is very different right so we have uh not just
[469.68 --> 474.86]  pages they're full out applications we have video we have all kinds of interesting things happening on
[474.86 --> 480.50]  the web and uh during this time the web was evolving but the ht protocol basically stayed where it was
[480.50 --> 491.24]  and uh in around uh 2007 or 2008 um the chrome team when we're working on chrome uh realized that as
[491.24 --> 496.98]  we were building uh the browser uh that the protocol had a number of deficiencies which didn't allow us
[496.98 --> 503.24]  to build and present the pages as quickly as we wanted to the user uh so there was this new effort
[503.24 --> 508.10]  kind of a bunch of studies that we started under the name of speedy uh which was around
[508.10 --> 514.46]  experimenting with the protocol ht protocol uh and trying to figure out what kind of changes we would
[514.46 --> 519.98]  have to make to the protocol to address some of the limitations and specifically one of the challenges
[519.98 --> 527.38]  with hp has been the fact that uh it's a it's a serialized request response protocol in the sense
[527.38 --> 532.24]  that if i send if i have a connection and i send a request and say hey i would like to get
[532.24 --> 538.80]  the index.html file you have to wait uh until you get the full response back before you can reuse that
[538.80 --> 543.68]  connection to ask for a second thing which may not seem like a big problem and it wasn't really a
[543.68 --> 548.76]  problem back in the 90s when all you were fetching is a document and maybe a couple of resources
[548.76 --> 554.96]  but now an average page is fetching over 100 resources which are things like images javascript css and
[554.96 --> 559.98]  all the other stuff and now that you have 100 resources and you have to do this in serial it becomes a
[559.98 --> 565.28]  bottleneck so you know there's workarounds for that of course you just open more connections but
[565.28 --> 569.46]  turns out that's also not great because if you open too many connections it can actually hurt user
[569.46 --> 575.30]  experience because now you run into troubles with congestion control and opening unbounded number of
[575.30 --> 580.80]  connections may hurt the server that you're trying to talk to so realistically we have to cap that
[580.80 --> 589.20]  and uh kind of through experimental uh deployments we uh we and other browsers determined that kind of
[589.20 --> 595.98]  arbitrarily six connections per origin is the optimal number so what that means is with http one you can
[595.98 --> 604.70]  fetch up to six resources in parallel uh which kind of worked you know in between 2000 and 2007 but in
[604.70 --> 610.60]  2007 we realized that that's not sufficient like this does not scale clearly uh developers are putting
[610.60 --> 615.72]  more and more resources they're building more ambitious applications and to do and to fix this issue we
[615.72 --> 624.66]  need to kind of rethink the the protocol and that was effectively the uh inception of speedy and speedy
[624.66 --> 631.98]  tried to change some of the basics of how messages are exchanged within hsp uh to address this thing
[631.98 --> 637.50]  when you talk about the connect yeah totally so when you talk about the connections and limiting that
[637.50 --> 643.02]  that's why we get things like um you know sprites for example with images that's why you have
[643.02 --> 648.22]  you know all of your uh websites images in one single file so you can just sort of sprite around and
[648.22 --> 653.52]  you css to move that as a background image that's where you get practices like concatenating a job all
[653.52 --> 659.12]  you know seven or eight different javascript files that support your your site to operate down into one
[659.12 --> 666.12]  and that's where you get all these sort of i guess workarounds to get into this six you know this
[666.12 --> 670.12]  glorified sixth number where you guys have figured out that that's the best number to focus on
[670.12 --> 675.14]  yeah yeah exactly and that's a really good point so we call these things like concatenation and
[675.14 --> 682.46]  as optimizations today right like bundle all your javascript files into app.js or you know use an
[682.46 --> 689.46]  asset pipeline to create this thing on the fly for you and really it's exactly as you pointed out it's a
[689.46 --> 695.98]  workaround it's a workaround for the fact that http provides limited parallelism or lack of
[695.98 --> 701.38]  parallelism if you want to call it that so we've been forced down this path of doing things like
[701.38 --> 707.84]  spriting images and concatenating files which actually has a lot of negative side effects so
[707.84 --> 713.70]  for example say you take say you have you know you've developed a beautiful application which is
[713.70 --> 720.44]  modular and has everything all the logic is split into different files and you like you it's just a
[720.44 --> 725.82]  well-engineered software project right and now you want to ship it to the client so they can
[725.82 --> 732.22]  execute it well today in order to do that the best practice in air quotes there is that you put all
[732.22 --> 738.54]  those files into one giant application.js and you ship it to the user now moments later you realize
[738.54 --> 743.18]  that hey i made a mistake or maybe i need to update something so you change a single character or single
[743.18 --> 749.50]  byte in that one file and now the user has to re-download the entire file right so you changed one
[749.50 --> 753.98]  byte and you have to download the whole thing all over again which of course is expensive data-wise
[753.98 --> 758.16]  it also slows down your application because now you have to download this giant thing when you only
[758.16 --> 767.32]  changed one little part of it and this is just not a good user experience so these best practices or
[767.32 --> 773.12]  these optimizations like concatenation actually prevent us from deploying effective caching strategies
[773.12 --> 778.30]  and the reason we were willing to put up with that in the past is precisely because the
[778.30 --> 788.10]  the latency trade-off of like this this constraint of lack of parallelism was so bad that we just kind
[788.10 --> 794.86]  of brushed it the brush the caching concerns under the rug and said that's okay we'll just re-download
[794.86 --> 802.30]  it all over again and so all this led into what was kicked off by google trademark by google even
[802.30 --> 808.70]  uh speedy s-p-d-y it's not an acronym but it looks like it might be and were you a part of the team
[808.70 --> 812.36]  when this kicked off originally like you were the founder of this project or what part did you originally
[812.36 --> 817.50]  play when speedy no i actually came in after the project got started so okay i think it's actually
[817.50 --> 823.66]  interesting to talk about um why it started in the first place and uh it all came down to
[823.66 --> 830.80]  this one experiment which was done by a couple of engineers um on the chrome team and what they tried
[830.80 --> 839.10]  to do was they took i think the top 100 websites uh they and they tried to simulate what would happen
[839.10 --> 844.64]  in terms of the loading performance of those websites if we varied bandwidth and latency
[844.64 --> 851.28]  independently so say you have a one megabit connection and then you load all the pages and
[851.28 --> 855.60]  you just measure the how long it took to load each page and then you double that to two megabits
[855.60 --> 860.12]  and you measure that again and see if there was a difference right like intuitively you would expect
[860.12 --> 864.48]  or you would hope rather that going from one to two would make things significantly faster because
[864.48 --> 869.66]  you can just download a lot more stuff more quickly so they kept increasing that bandwidth and
[869.66 --> 874.04]  then separately they ran the same experiment for latency so if we just keep increasing or decreasing
[874.04 --> 878.34]  latency from let's say 100 milliseconds to 100 milliseconds what's the impact and the thing that
[878.34 --> 884.28]  they realized was that after about five megabits per second which is uh more than
[884.28 --> 893.30]  uh the average uh broadband connection speed in the united states so basically if you're on broadband
[893.30 --> 898.78]  in the united states or in most of the countries you already exceed that five megabits upgrading from
[898.78 --> 903.76]  five to say 10 megabits will only give you like a single percentage point improvement in the page
[903.76 --> 908.34]  loading speed wow and that's a lot of people are spending too much on the internet on their internet
[908.34 --> 913.42]  too potentially to not get a faster web not because they're watching netflix that's right well that's
[913.42 --> 917.14]  that's a good point right so there there is there is some type of traffic on the web that is
[917.14 --> 922.20]  bandwidth constrained so these large streams like video are definitely bandwidth constrained so if you
[922.20 --> 927.10]  want to watch hd video yeah please go ahead and get yourself uh you know 100 megabit connection
[927.10 --> 933.96]  but upgrading from let's say a five megabit to 100 megabit connection does not or will not
[933.96 --> 938.96]  significantly improve your browsing experience which is kind of sad right if you think about it
[938.96 --> 945.28]  that makes sense yeah because you don't see you know isps uh marketing their you know their round
[945.28 --> 950.60]  trip times or their latency all right even use bandwidth so you can't just go buy better latency right
[950.60 --> 956.28]  well yeah and and therein therein is the the actual rub here right so repeating the same experiment
[956.28 --> 963.56]  with uh changing latency they saw a linear performance improvement as in the lower the latency
[963.56 --> 969.56]  there's there's a very direct correlation between lower latency and improving the uh performance so
[969.56 --> 974.94]  if you actually rather performance of loading websites or browsing the web so if you really want
[974.94 --> 979.92]  to have a faster experience of browsing the web you should find a connection that has the lowest
[979.92 --> 985.26]  latency but as you said i'm not aware of single isp out there that is actually advertising the sort
[985.26 --> 991.58]  of thing in their marketing right which is a whole other discussion that we should have at some point
[991.58 --> 998.14]  yeah i mean some of that of course out of their control right the there's a lot of factors that
[998.14 --> 1005.94]  play into latency um and they're just one player uh in a game of you know in a what is effectively like
[1005.94 --> 1010.34]  a mesh network is that fair to say yeah that's true there are many hops between you and the server
[1010.34 --> 1017.26]  and the isp is perhaps the first couple of hops in practice it turns out that isps or the last mile
[1017.26 --> 1025.26]  as we call it um can contribute a significant amount of latency so um that's typically because
[1025.26 --> 1031.84]  the area is under provisioned so everybody starts watching netflix and all of a sudden there's not
[1031.84 --> 1036.98]  enough capacity and latency suffers and all these things happen so there's definitely a lot that
[1036.98 --> 1041.28]  carriers can do to improve this sort of thing but you know that's that's probably a whole separate
[1041.28 --> 1045.32]  discussion so the outcome of this whole experiment was basically the realization that
[1045.32 --> 1053.04]  uh the web is not going to get faster unless we either decrease latency which you know we can't
[1053.04 --> 1058.86]  as as an outsider or we re-examine our protocols and figure out what is it that prevents us from
[1058.86 --> 1065.08]  utilizing the bandwidth but in a better way and uh one way to improve latency is to like pipeline
[1065.08 --> 1070.22]  requests right so instead of serializing every request one after the other what if we were able to
[1070.22 --> 1075.10]  just say well i need these 50 resources so let me just send you all 50 requests at the same time
[1075.10 --> 1081.36]  hsp does not allow us to do this but what if it could and that was effectively the premise for
[1081.36 --> 1086.06]  speedy like what do we need to do to change the protocol to allow that sort of thing and further
[1086.06 --> 1093.02]  if we're going down this path we also know that as the web has evolved and we've put more and more
[1093.02 --> 1098.68]  different kinds of resources these resources have different priorities so for example if i send you 50
[1098.68 --> 1104.22]  resources the html file is very very important to me and the image file is important but not as
[1104.22 --> 1107.92]  important as html so it'd be kind of nice if i could communicate that to the server and say
[1107.92 --> 1113.32]  here's 50 resources but i would i could really use your help on getting the html file first because
[1113.32 --> 1120.06]  that allows me to display something to the user so uh htp also or the htp1 rather does not allow you
[1120.06 --> 1126.22]  to do that htp2 does and then there's other use cases like dependencies let's say you are trying to
[1126.22 --> 1134.94]  stream a video file it'd be kind of silly for the server to send you a frame a subsequent frame before
[1134.94 --> 1139.32]  it was able to send you the first frame ahead of it right it's like i don't want the second frame
[1139.32 --> 1144.96]  before i can get the first one so there's some notion in there of saying like here's two requests
[1144.96 --> 1149.78]  but please deliver the other request or the response after you've sent me the first one
[1149.78 --> 1157.74]  and kind of between all of this uh that was the foundation of speedy and that started in around
[1157.74 --> 1164.06]  2008 we ran some experiments we saw some significant improvements in terms of uh the actual performance
[1164.06 --> 1169.84]  so at first we were actually able to deploy it or implement the first version in chrome and we also
[1169.84 --> 1176.78]  implemented uh the server portion on some google servers and we ran an experiment where we opted in
[1176.78 --> 1182.94]  some users into using speedy and uh there were significant uh performance improvements for those
[1182.94 --> 1188.22]  users for the users that we saw that were using speedy and this was mainly on like document-based
[1188.22 --> 1194.34]  sites not so much like video-based sites or these non-web-based sites like non-document sites
[1194.34 --> 1201.56]  um no no no it wasn't it wasn't that specific we saw improvements across the board just because we were
[1201.56 --> 1208.64]  able to remove these bottlenecks but it is true that the biggest benefits were typically for
[1208.64 --> 1214.44]  sites that had a lot of requests because now we were able to pipeline and eliminate
[1214.44 --> 1220.06]  these unnecessary um latencies like queuing latencies and head of line blocking
[1220.06 --> 1228.84]  we're definitely getting into http2 landscape here um is there anything else on speedy we should cover in
[1228.84 --> 1235.92]  terms of like you know as the precursor it's it was the originating experiment to get to what is now
[1235.92 --> 1240.98]  the h2 spec so is there anything else we need to cover on speedy to sort of migrate into talking
[1240.98 --> 1248.38]  deeply about h2 um i think we covered the main points i guess i'll just say that uh speedy was meant as
[1248.38 --> 1255.62]  an experiment and uh with time because we did see um good improvements in performance it was actually
[1255.62 --> 1263.36]  becoming well adopted outside of google so we had firefox that enabled speedy as well in their
[1263.36 --> 1270.02]  browser safari announced that they will support it i think it was from safari 9 um ie also added
[1270.02 --> 1275.60]  support for speedy so in effect it was becoming a de facto protocol and similarly server support was
[1275.60 --> 1281.70]  emerging so there was apache nginx and other servers that were all supporting it and uh kind of on the
[1281.70 --> 1287.46]  on the basis of that the http working group uh said well look clearly there's something here so
[1287.46 --> 1296.30]  uh let's uh start an effort to modernize http and they did a call for proposals um google and others
[1296.30 --> 1301.54]  submitted their proposals google submitted uh the speedy protocol and after a couple of rounds of
[1301.54 --> 1307.18]  kind of discussions and feedback the speedy spec was adopted as a basis or a starting point for the
[1307.18 --> 1314.22]  http protocol uh and then from that point forward as http 2 development proceeded now speedy was also
[1314.22 --> 1319.96]  being developed but it was effectively kind of like an experimental branch where we were able to
[1319.96 --> 1325.98]  prototype new ideas kind of test them see if they pan out and then that feedback would get merged into
[1325.98 --> 1334.10]  http 2 so that's kind of the history and uh so http 2 development started in around um i think it was 2011
[1334.10 --> 1341.54]  before we get into that i do have kind of a big picture question around the the idea of replacing
[1341.54 --> 1348.72]  you know the current application layer protocol http with something better um the goal being to make
[1348.72 --> 1354.72]  the web faster reduce latency you know networked computers you know have lots of different technologies
[1354.72 --> 1360.78]  at play um the network stack for for those who aren't quite familiar with the networking side
[1360.78 --> 1367.30]  has many layers uh depending on how you look at it there's seven or five and yeah regardless of
[1367.30 --> 1373.38]  the way you look at it http is that you know that top layer that's the application layer where
[1373.38 --> 1379.68]  uh developers kind of play and integrates with with your apps and whatnot um below that you know
[1379.68 --> 1384.30]  there's the session layer where you have your encrypted connections there's transport layer this is where
[1384.30 --> 1390.28]  you know tcp and udp are often used and then you have your ip layer which we're most familiar with
[1390.28 --> 1398.60]  ip addresses and whatnot was there efforts to swap out lower down to say well maybe tcp is not the
[1398.60 --> 1405.34]  best way to deliver the web and um was there research that went into that were there efforts
[1405.34 --> 1411.72]  that are trying to do that or have tried to do that um so funny that you ask yes uh even at the
[1411.72 --> 1419.36]  very beginning back in kind of 2007 uh we knew that we would probably need to solve problems at
[1419.36 --> 1424.60]  multiple layers but at the same time it didn't make sense to try to tackle everything at once
[1424.60 --> 1430.34]  right i think that would have been just too much to bite off yeah so initially the focus was on http
[1430.34 --> 1437.78]  so what can we do to solve that and then once we unblock those issues we will immediately run into
[1437.78 --> 1442.14]  the performance issues at the layer below and that in particular here this would be the question
[1442.14 --> 1446.14]  about tcp like we've solved issues at the application layer of http we removed head of line
[1446.14 --> 1452.96]  blocking but turns out that tcp also has its own failure modes with head of line blocking and uh now
[1452.96 --> 1457.24]  there's actually a different effort within within chrome called quick which is effectively
[1457.24 --> 1464.16]  think of it as http2 over udp there's some other things but it's an experiment that we're working
[1464.16 --> 1469.58]  on now which is using udp to mitigate some of these issues that we're uh that we're running
[1469.58 --> 1476.78]  into within tcp but that's probably a whole other episode on this one so long story short there are
[1476.78 --> 1481.60]  some you know ancillary efforts that aren't just sitting at the application layer they're going
[1481.60 --> 1485.84]  further down like the the tcp layer the transport layer as jared mentioned that's kind of hanging out
[1485.84 --> 1492.60]  there or the udp layer that's right yeah yeah and uh tcp continues to improve right so there's there's
[1492.60 --> 1500.06]  lots of work happening uh in all parts of the stock i also think that it seems like the further
[1500.06 --> 1506.00]  down you go the the more tightly integrated into the operating systems that you are and so perhaps
[1506.00 --> 1512.66]  more difficult even as a uh a wide you know as far as adoption goes as a rollout you know we see how
[1512.66 --> 1521.30]  ipv6 you know uh still not out there in droves um over years and years of it being you know pretty
[1521.30 --> 1528.44]  much done i guess or available so perhaps starting at the top and working your way down is even the
[1528.44 --> 1535.18]  most effective way to to do it so that makes some sense um we're getting into the transition between
[1535.18 --> 1544.04]  speedy and h2 um you covered a little bit of how speedy was being adopted can you maybe reiterate
[1544.04 --> 1550.64]  reiterate or at least tell us why why the need to you know move away from speedy as a thing and
[1550.64 --> 1559.92]  and uh and do the h2 thing instead sure so the intent to the intent here was to standardize on on a
[1559.92 --> 1565.64]  protocol right so to bring in we came up with some ideas within speedy for how to address the
[1565.64 --> 1570.48]  particular issues that we thought were important to move the web forward in terms of performance
[1570.48 --> 1575.24]  um then you take that to your itf and there's just a lot more people around the table with
[1575.24 --> 1580.76]  different kinds of experiences different perspectives on what is important and that was the intent uh
[1580.76 --> 1588.68]  behind taking it to to itf and that's the intent of itf and that's where hsp2 was developed so over
[1588.68 --> 1594.46]  the period of about two years there was uh 14 drafts 14 kind of big milestones along the way
[1594.46 --> 1600.10]  that we went through and now actually back in may so about a month ago now
[1600.10 --> 1604.78]  uh these specs have been officially published so there's actually two specs one is the htp2
[1604.78 --> 1612.42]  specification and another one is the hpack or the the header compression uh specification which we can
[1612.42 --> 1619.18]  we actually haven't talked about this yet but we can uh in a little bit and i guess one thing i'll
[1619.18 --> 1627.02]  mention here is uh you kind of hinted at this um a little bit earlier modifying something as big as http
[1627.02 --> 1633.82]  uh is a big task right and i think this is why to some degree it took us so long to get to this point
[1633.82 --> 1638.20]  because there's so much built on http that any thought of trying to modify it
[1638.20 --> 1649.10]  um would be like a just a huge undertaking so one interesting uh point to keep in mind with hp2 is that
[1649.10 --> 1658.72]  hp2 does not actually modify any of the semantics of the http protocol so the headers and the header names
[1658.72 --> 1665.92]  the methods kind of your all your restful stuff all of that is exactly the same and that is intentional
[1665.92 --> 1672.64]  so in fact some people criticize hp2 for not tackling some of the higher level issues that they
[1672.64 --> 1677.84]  think should be addressed in hp2 but that was explicitly out of scope when the when we chartered the
[1677.84 --> 1683.04]  whole http2 effort because we knew that there's so much that we could do but we wanted to focus on
[1683.04 --> 1688.80]  kind of this low level performance and framing so any application that you have today that runs over
[1688.80 --> 1695.04]  http you can put that over http2 and everything will work as is because nothing has changed semantically
[1695.04 --> 1702.00]  and i think this is very very important whether we should modify some other things kind of like
[1702.00 --> 1707.04]  semantics http is now beyond that right and that that's like now that we finished hp2 we can now start
[1707.04 --> 1712.18]  that discussion so it's backwards compatible in in in many ways what you're trying to say
[1712.18 --> 1718.20]  that's right right so you can deploy like you'll have to swap out the server because it'll need to
[1718.20 --> 1722.18]  understand http2 but you don't have to modify your application like there's there's nothing about
[1722.18 --> 1727.90]  your application that will like be http2 incompatible now that said there are things that you can do within
[1727.90 --> 1733.50]  your application to make it perform better over http2 but that's a very different discussion right like this is
[1733.50 --> 1738.84]  the uh coming back to your earlier point like you were concatenating files well perhaps you shouldn't
[1738.84 --> 1743.68]  do that now because it actually hurts performance yeah we were just talking about that actually in the
[1743.68 --> 1749.14]  last show we were talking about that and it was sort of the discussion of things that have become in
[1749.14 --> 1755.64]  quotes what we said earlier which was have become best practices around you know the http1 spec that you're
[1755.64 --> 1759.70]  doing now to concatenate and you know all that stuff and now that might not be a good thing since
[1759.70 --> 1763.96]  it's you have different things for like pipelining or multiplex and they can support that better now
[1763.96 --> 1770.08]  right exactly the problem with that i guess and where it gets complicated of course i'm an
[1770.08 --> 1773.36]  application developer so i'm always thinking about like how does it complicate my workflows and stuff
[1773.36 --> 1779.86]  and and like that sounds great as far as http2 actually simplifies my workflow because i don't need to do
[1779.86 --> 1786.12]  all that stuff anymore but it's not like h1's going anywhere anytime soon right so we're still gonna have to
[1786.12 --> 1793.80]  support both for you know for years to come um let's do this let's get a high level overview because
[1793.80 --> 1797.58]  we haven't actually talked about what it brings to the table we know what it's trying to do which
[1797.58 --> 1802.56]  is improve performance reduce latency you know kind of be a more modern protocol for more modern web
[1802.56 --> 1809.58]  uh ilia why don't you give us kind of the big tentpole tentpole features of h2 and then we'll take a
[1809.58 --> 1816.02]  break and come back and we'll we'll dig deep into each one all right sure um so let's see where
[1816.02 --> 1823.58]  to start um so we talked about uh the fact that everything in htp1 is kind of has a serial request
[1823.58 --> 1829.60]  response model and that was one of the main things that we wanted to address with htp2 uh we know that
[1829.60 --> 1835.12]  in htp1 world we also had these six connections and we want we don't want that either so the first
[1835.12 --> 1840.94]  premise that htp2 started with in speedy as well is that we want to optimize and transfer everything
[1840.94 --> 1844.72]  over a single tcp connection like there should be there shouldn't be a reason why we need multiple
[1844.72 --> 1849.02]  connections right opening multiple connections to the same server doesn't actually give you anything
[1849.02 --> 1853.12]  in terms of like throughput right if you can you can transfer everything over the same connection or
[1853.12 --> 1858.54]  six uh except that you will actually get better performance of the transport layer if you're
[1858.54 --> 1864.50]  reuse the same connection because there's just a lot of mechanisms within like say tcp and other
[1864.50 --> 1872.32]  protocols that are optimized for making the best use of available bandwidth so one tcp connection
[1872.32 --> 1878.38]  is is the start and then if you have one cp connection what do we need to do to actually
[1878.38 --> 1884.60]  be able to send and receive multiple requests and responses at once so to do that we added this
[1884.60 --> 1892.32]  notion of framing where a message so in htp world a message is a collection of headers which are just
[1892.32 --> 1897.46]  key value pairs like get this and you know this header that content length with the number
[1897.46 --> 1903.90]  uh in the actual payload so a message can be split into many different frames so for example
[1903.90 --> 1909.22]  headers can be transferred independently of the body and body itself can be split into many different
[1909.22 --> 1915.80]  chunks which we kind of had before right with chunks encoding but you couldn't interleave multiple
[1915.80 --> 1921.52]  messages like you couldn't say here's a little bit of the body of the request or the response for this
[1921.52 --> 1927.54]  request that you sent and here is the other bit for another request like you couldn't interleave those
[1927.54 --> 1935.32]  and that's what binary framing provides it introduces this notion of a stream id so in htp2 world requests
[1935.32 --> 1942.00]  are we refer to them as streams so you open multiple streams to the server and each one of the streams
[1942.00 --> 1947.94]  carries say htp headers and get headers for all of your requests the server receives all of those streams
[1947.94 --> 1954.18]  each stream has an id and it just starts generating responses and in order to send data back it just
[1954.18 --> 1960.76]  packages each chunk of data and appends that stream id plus some other metadata and sends it back to the server
[1960.76 --> 1965.96]  and now all of a sudden because we can split these messages into smaller chunks we can actually interleave them
[1965.96 --> 1971.54]  so say you get two requests and one is for i don't know a css file another one for an image
[1971.54 --> 1977.26]  you start sending the css file because it's the most it has a higher priority which is something the client
[1977.26 --> 1982.12]  communicated to you but then the server blocked maybe your application is kind of slow so then the
[1982.12 --> 1987.38]  server can say okay well i'll pause that and i'll start sending you the the image data and then once
[1987.38 --> 1993.50]  the css data once is available once again it resumes that so now that this data can flow over the single
[1993.50 --> 1998.30]  connection it can be prioritized we no longer need multiple connections right everything is just
[1998.30 --> 2003.86]  transferred within uh the same stream so that's multiplexing and prioritizations and prioritization
[2003.86 --> 2011.06]  another thing that was added uh now that we have this notion of streams is a flow control so if
[2011.06 --> 2016.54]  you're familiar with things like tcp flow control this is a similar thing but it allows you to
[2017.36 --> 2026.56]  express things like um i want to receive so here's a request here's a stream and i'm willing to receive
[2026.56 --> 2033.84]  up to x many bytes of the stream and then i will tell you when to resume it and this is kind of
[2033.84 --> 2038.16]  cool because that actually opens up new opportunities for the client and server to interact
[2038.16 --> 2046.74]  in ways which you couldn't before for example uh say images right um many or not many some image
[2046.74 --> 2051.46]  formats allow progressive rendering where you can fetch a little bit of the file and you can render a
[2051.46 --> 2059.90]  preview of the image well before we had to fetch basically the entire image and then display it now with
[2059.90 --> 2064.58]  something like flow control we can say well i have a lot of very important things i need to fetch
[2064.58 --> 2070.10]  but i also want to render a preview of the image because that would help me get the page displayed to
[2070.10 --> 2075.26]  the user more quickly so i'm willing to accept like 10 kilobytes of the image because that's sufficient
[2075.26 --> 2080.80]  for me to render a preview but then after that i want all the other more important stuff and then
[2080.80 --> 2086.14]  once i receive that i can resume that stream and receive the rest of the image so this is fundamental
[2086.14 --> 2091.92]  so this is something that is fundamentally new and previously not possible and http2 provides that
[2091.92 --> 2102.06]  and then the other interesting feature that was added is server push so the idea here is
[2102.06 --> 2109.04]  today in http1 you send the request and you get a response and there's a one-to-one correlation
[2109.04 --> 2115.06]  but what if the server could actually send you back multiple responses and concretely the use
[2115.06 --> 2123.80]  cases the use case here is you send the request for let's say a page about.html and then we send
[2123.80 --> 2128.32]  you back the html and you immediately come back to us and say well yes i also want the style sheet
[2128.32 --> 2135.54]  that you declared in in that file but the server already knew that like the server could know already
[2135.54 --> 2140.30]  know about that so why can't they just say here's the index.html file and by the way i know that you
[2140.30 --> 2144.94]  will also need the style file or the style sheet file so here it is as well so like don't waste the
[2144.94 --> 2149.44]  round trip there's absolutely no reason to block on a round trip i know you will need this so please have
[2149.44 --> 2155.72]  it and this sounds kind of crazy but we've actually been already using this this is what inlining does
[2155.72 --> 2160.96]  right because when you inline right the contents of a file you're effectively saying don't don't come
[2160.96 --> 2167.42]  back and ask me for this like i know you will need this so here just have it uh so it effectively
[2167.42 --> 2172.70]  formalizes and enables this sort of interaction at the protocol layer which is nice because one of the
[2172.70 --> 2178.24]  side effects of inlining is that caching yeah you can't cache it independently right and so now you're
[2178.24 --> 2182.84]  inflating the size of the other file it has problems with prioritization or you can't prioritize it
[2182.84 --> 2188.40]  you have to invalidate it more frequently so push enables that which is uh really cool and once again
[2188.40 --> 2193.42]  that's kind of a new capability that we just didn't have access to before so some of these
[2193.42 --> 2200.98]  features are kind of direct they're directly addressed the limitations of the previous uh limitations of
[2200.98 --> 2206.00]  the of the protocol and some of these features just enable fundamentally new patterns of interaction
[2206.00 --> 2212.54]  between the client and server that i think uh we're yet to explore uh really effectively and we'll talk
[2212.54 --> 2218.10]  about i guess the adoption and the the current state of servers a little bit later
[2218.10 --> 2223.12]  but i think there's just a lot of room for innovation for how we deliver web applications with http2
[2223.12 --> 2231.00]  good deal that's definitely a a good overview of http2 uh we'll break here actually you know what
[2231.00 --> 2236.16]  there's one more isn't there yes there's one more there's one more thing there's one more thing
[2236.16 --> 2243.22]  i almost forgot header compression so we i mentioned that this is a separate specification and
[2243.22 --> 2250.32]  uh the problem that this was trying to address is that http1 allows you to transfer data in compressed
[2250.32 --> 2257.62]  form for example you can gzip your content uh your text content right which is very nice because it just
[2257.62 --> 2261.76]  so happens that gzip is very effective at compressing text content typically reducing it
[2261.76 --> 2270.82]  it's file size by like 30 to 80 percent which is huge savings but the problem is that the actual
[2270.82 --> 2276.40]  metadata about the request things like your headers your cookies and all the rest was always transferred
[2276.40 --> 2284.62]  uncompressed and uh over time because we rely so much on headers and cookies and other things this
[2284.62 --> 2291.84]  stuff has kind of accrued and we're now sending sometimes megabytes of header metadata i was recently
[2291.84 --> 2299.32]  looking at one website which had a lot of analytics and other beacons that during a single page load
[2299.32 --> 2309.18]  it was generating one megabyte of traffic of just uncompressed http headers what which blew my mind i mean
[2309.18 --> 2315.50]  the cookies are maxed out at a certain size right uh yeah different browsers actually have different
[2315.50 --> 2320.98]  ways to enforce it but you know if you send enough requests it all adds up pretty quickly it turns out
[2320.98 --> 2326.86]  that on average the request response even without cookies adds about 800 bytes of metadata which doesn't
[2326.86 --> 2332.98]  seem like much but then you have to multiply it by you know a couple hundred requests per page and then
[2332.98 --> 2337.62]  if you if you do add cookies you're very quickly approaching you know some pretty significant territory
[2337.62 --> 2344.82]  like hundreds of kilobytes so uh header compression was our way to address that to say like we should
[2344.82 --> 2350.26]  be able to compress this and that's what hpack is now hpack actually provides uh two different mechanisms
[2350.26 --> 2357.24]  one is uh it uses huffman coding to with a static dictionary just to compress value so you just give
[2357.24 --> 2362.48]  it a string and there's a predefined dictionary which is used to compress these transferred data and then
[2362.48 --> 2368.96]  uh the other mechanism it has is that it the client and server keep state about what data has been exchanged
[2368.96 --> 2377.08]  so think of something like uh say the user agent header right uh which is kind of long string which describes
[2377.08 --> 2382.52]  the vaguely describes i should say the user agent uh and some properties about the device
[2382.52 --> 2386.08]  that data does not change between requests
[2386.08 --> 2392.72]  right but in hsp1 we keep sending it on every single request which adds hundreds of bytes of data
[2392.72 --> 2400.84]  so with hsp2 the way it works is you just send it once that goes into what we call a dynamic table
[2400.84 --> 2406.90]  which basically just remembers that okay this this thing has been sent and it's let's say its id is 55
[2406.90 --> 2415.20]  so next next time on the next request i can just say 55 and you immediately know that oh okay you want to
[2415.20 --> 2420.76]  communicate that you you're also sending this header so that significantly reduces the amount of
[2420.76 --> 2427.04]  metadata that's being transferred we're talking by a couple of orders of magnitude where the
[2427.04 --> 2436.88]  the lowest overhead of a hsp2 stream now is about nine bytes as compared to say
[2436.88 --> 2444.70]  900 yeah 900 bytes with hsp1 which makes it very appealing for many other use cases
[2444.70 --> 2452.84]  hsp2 or hsp in general is very popular outside of browsers as well api traffic and all the rest
[2452.84 --> 2459.46]  and but what one of the issues has been kind of this high overhead of hsp headers and with hsp2
[2459.46 --> 2466.28]  that's no longer a concern so you can actually use it for much and many other use cases
[2466.28 --> 2473.74]  good deal so uh you got one tcp connection you got request and stream with multiplex and prioritized
[2473.74 --> 2479.60]  streams binary framing layer header compression also known as hpack that sort of comprises
[2479.60 --> 2485.92]  http2 uh in sort of one whack there let's take a break real quick we'll come back
[2485.92 --> 2492.02]  um and talk more deeply about each of these sections here but we'll hear from a sponsor and we'll be right back
[2492.02 --> 2501.08]  dream host now has managed vps hosting built for speed and scalability including solid state drives
[2501.08 --> 2507.18]  and that's awesome these vps's are built for open source developers and now include one click installs
[2507.18 --> 2515.22]  of node.js custom ruby and rvm support speed speed and more speed is what it's all about their vps servers
[2515.22 --> 2521.56]  use ssd hard drives and are 20 faster than traditional sata drives all virtual private
[2521.56 --> 2529.84]  servers from dream host include ssd storage ubuntu 1204 lts web-based control panel scalable ram which is
[2529.84 --> 2534.48]  super awesome you can go from one gig of ram and easily scale up to eight gigs if you need it
[2534.48 --> 2540.60]  node.js one click install ruby version manager unlimited bandwidth unlimited hosted domains
[2540.60 --> 2547.54]  unlimited 24 7 support go check them out and learn more at dreamhost.com slash the changelog
[2547.54 --> 2557.88]  all right we're back and uh so deep dive here on all the details of http2 i think the next question
[2557.88 --> 2562.96]  really is where from here we got server support browser support security concerns where's the best
[2562.96 --> 2568.36]  place to start with the how http2 actually becomes a thing to to developers out there
[2568.36 --> 2574.72]  let's start with how you uh how it's implemented and how a conversation between a client and server
[2574.72 --> 2582.48]  goes from h1 to h2 and if they're just how does that all work oh yeah right so the upgrade cycle
[2582.48 --> 2589.60]  um i think this will take a short detour into the security discussion as well or not security tls in
[2589.60 --> 2597.64]  particular uh so in order to upgrade to http2 we have to somehow figure out if the client and server
[2597.64 --> 2604.20]  support it right previously we've just assumed that http1 uh now we need to somehow figure that
[2604.20 --> 2609.08]  out and ideally we'd like to do that with without any additional latency because that would kind of
[2609.08 --> 2618.12]  defeat the whole purpose of doing the performance optimization uh so uh turns out http actually provides
[2618.12 --> 2625.40]  some mechanisms to do upgrade and negotiation so that there's this upgrade flow uh but uh for some
[2625.40 --> 2632.76]  interesting reasons that is actually not practically useful for http2 in particular uh one of the things
[2632.76 --> 2638.88]  we we learned when we first started experimenting with speedy uh was that there's a lot of existing
[2638.88 --> 2645.24]  middleware on the web uh things like proxies even antivirus software running on users computers and
[2645.24 --> 2652.92]  other things that are looking at the flows uh over port 80 as they're as they happen and uh oftentimes they
[2652.92 --> 2657.40]  when they detect something that doesn't smell like http1 or something that they don't understand they
[2657.40 --> 2663.64]  assume that it's either bad malformed or malicious and just shut it down and this is actually not new
[2663.64 --> 2670.12]  uh we actually had the same experience with web sockets because they also flow over port 80 and it turns
[2670.12 --> 2676.60]  out that if you try to deploy web sockets over just unencrypted connections uh oftentimes things just
[2676.60 --> 2680.92]  fail and you have no idea why they fail it just for some reason the connection is aborted or it hangs or
[2680.92 --> 2687.64]  something else but then you switch that same connection into 443 or you run it over tls and
[2687.64 --> 2691.72]  everything's fine so in practice you'll find that today the best practice for deploying web sockets
[2691.72 --> 2697.88]  is over tls and we ran into the same issue with speedy where we you know we would try to make connections
[2697.88 --> 2704.92]  over the unencrypted channel and sometimes these things would just fail and like 20 to 30 of the time
[2704.92 --> 2709.08]  connections would just fail which is obviously unacceptable right if you try to browse the web like
[2709.08 --> 2713.88]  imagine trying to open google and 20 to 30 of the time a third of the time uh it just fails like
[2713.88 --> 2718.92]  that that's just not going to happen bad ux right for sure that that's more than bad ux that's just
[2718.92 --> 2725.96]  like we failed the user right yeah just what i mean it's just a horrible all around that's no ux
[2726.84 --> 2735.24]  right exactly no experience so like for that reason alone uh we had to deploy speedy over https
[2735.24 --> 2741.40]  because it provides an end-to-end encrypted tunnel which means that these intermediaries and other
[2741.40 --> 2745.80]  things uh just see encrypted data flow and encrypted data flow they all look the same
[2746.44 --> 2753.56]  so they can't really choke on it or do bad things to it and it turns out that uh that same reasoning
[2753.56 --> 2763.08]  applies to https so there's the spec itself does not mandate that you use https it actually provides
[2763.08 --> 2769.24]  mechanisms for you to uh use http over unencrypted connections and you can certainly do that
[2769.88 --> 2777.16]  but the browsers that have implemented http 2 which are chrome and firefox have already shipped support
[2777.16 --> 2785.64]  for http 2 uh have said that they will only do http over https on the public web why the discrepancy
[2785.64 --> 2791.08]  between the spec and the implementations uh well so so the spec just says like there's no reason
[2791.08 --> 2796.68]  say you're in a controlled environment say you have two servers that you control and you control
[2796.68 --> 2801.64]  the path between them there's no reason for the spec to mandate https from that perspective
[2802.36 --> 2808.12]  and we know that http is being used in a variety of different environments now you know as a with my
[2808.12 --> 2813.48]  security hat on i will tell you that even though you think you have a clear path you should still use
[2813.48 --> 2818.60]  https between your server to server communication or some sort of encrypted tunnel because we know that
[2818.60 --> 2823.08]  you know malicious people do malicious things and they sniff on traffic and they will they can do
[2823.08 --> 2829.08]  things bad things with that traffic never heard of it yeah yeah so you heard here first brox
[2830.36 --> 2836.20]  using cryptic connections uh it's a good thing uh but at the same time like there's no reason there's
[2836.20 --> 2841.96]  no fundamental reason why we need to require that right so the spec says yes you can use it but in
[2841.96 --> 2847.08]  practice on the web if you want to deploy it uh you need https and further the browsers will only
[2847.08 --> 2852.68]  uh negotiate hsp2 over tls and now the question is okay so now that we have tls tunnel how do we
[2852.68 --> 2858.60]  actually know that the client and server support hsp2 in particular and uh there there's actually a
[2858.60 --> 2865.24]  mechanism called al alpn negotiation which is the uh which is used to negotiate which protocols are
[2865.24 --> 2872.84]  supported during the tls handshake so you said alpn that's right alpn okay um so what happens there is
[2872.84 --> 2878.52]  when the client sends starts the establishment of the secure channel uh the client and server
[2878.52 --> 2882.84]  negotiate the parameters for the secure connection things like what kind of crypto you're going to use
[2882.84 --> 2888.76]  and other stuff and as part of that handshake there's now an extension that negotiates or
[2888.76 --> 2894.84]  rather the client advertises which protocols it supports and then and one of those protocols is hsp2
[2894.84 --> 2900.76]  if you support it and then the server sees that and it can uh confirm that and say okay well i also
[2900.76 --> 2906.60]  support hsp2 so i will be talking to you in hsp2 so this negotiation happens as part of the tls handshake
[2906.60 --> 2914.36]  and this is important because it does not add extra latency so if you're using htps already that would
[2914.36 --> 2920.68]  happen over tls in the negotiation bit and then your server would just automatically know to encode frames
[2920.68 --> 2926.28]  with htp form htp2 format as opposed to htp and this is great because it actually makes the whole thing
[2926.28 --> 2931.40]  transparent uh like the server can take care of all of all of those details for you and there's no extra
[2931.40 --> 2940.84]  latency so just as a quick aside certain people would complain about the practical uh requirement of
[2941.56 --> 2948.44]  https to you know because it raises the barrier to entry on the web it costs money at least until
[2949.00 --> 2955.24]  the ff gets their thing rolling it complicates things i'm you know it's a hobby project it's my blog i don't
[2955.24 --> 2962.12]  need security what do you say to that uh well that's that's a very long discussion so in practice
[2962.68 --> 2970.92]  make it quick yeah there's no there's no such thing as insensitive traffic on the web uh you can
[2972.60 --> 2981.24]  a malicious observer can infer a lot about your behaviors based on uh navigation patterns of things
[2981.24 --> 2986.20]  that you may not consider to be sensitive but which in fact leak information about you those around you
[2986.20 --> 2993.40]  and all the rest so the the argument of oh but i'm just navigating like i'm just serving a personal blog
[2994.04 --> 2999.72]  does not stand uh in my books and you know many different people have made very good arguments in
[2999.72 --> 3004.52]  both directions i happen to be on the side that like i believe that we should encrypt all these things because
[3004.52 --> 3014.76]  the uh the incidentary uh kind of damage of revealing all of these bits adds up and you can
[3014.76 --> 3021.24]  infer a lot about the user and their intent just by observing these uh traffic patterns yeah so then
[3021.24 --> 3026.20]  there is the questions the practical concerns over how does this affect my performance uh obviously
[3026.92 --> 3032.20]  doing crypto requires more work than not doing crypto so how expensive is that it turns out that
[3032.20 --> 3039.32]  a decade ago that was actually very expensive modern cpus are optimized to execute crypto very very
[3039.32 --> 3046.28]  quickly you don't need dedicated hardware for that sort of thing you did before for example google
[3046.28 --> 3052.60]  facebook twitter all the big companies run tls purely in software like we're not buying additional
[3052.60 --> 3059.16]  hardware and further actually as an interesting side effect of deploying things like speed in hp2
[3059.16 --> 3065.16]  because we require far fewer connections it actually can decrease your operational costs
[3065.16 --> 3069.80]  because you have to maintain fewer sockets you have to do fewer handshakes and handshakes are actually the
[3069.80 --> 3078.60]  most expensive part of tls so we've seen studies uh where if you run a load test against an http1 server
[3078.60 --> 3084.44]  and then enable hp2 the resource usage is actually lower because of all the things we just mentioned
[3084.44 --> 3090.68]  uh so uh yes there are costs to it uh the the whole certificate question it you know it depends on
[3090.68 --> 3097.48]  what kind of certificate you need whether you need um to support older browsers or not um in in all the
[3097.48 --> 3102.28]  rest so yes that's it adds a bit more complexity but practically speaking it is a requirement because
[3102.92 --> 3109.56]  we're just not willing to accept 30 failure rate right on so while we're talking complexity and knee-jerk
[3109.56 --> 3116.12]  reactions um i admit that i had a knee-jerk reaction around the binary framing layer when i first heard
[3116.12 --> 3124.04]  about it um being a fan of http and the plain text aspect of it of course a binary communication
[3125.00 --> 3133.32]  protocol doesn't doesn't let you just see what's going on down the wire i'm sure you've had that uh
[3133.96 --> 3138.92]  come at you what do you say about people that complain about that particular aspect of h2
[3139.56 --> 3143.48]  sure sure so i think there's a couple of different perspectives that we should untangle there one
[3143.48 --> 3149.72]  is implementation second one is kind of observability right as a user so it turns out that
[3149.72 --> 3155.72]  implementation wise binary protocols are actually simpler and easier to implement correctly
[3156.84 --> 3163.08]  i happen to have some experience with implementing both i've implemented both http2 and http1 in ruby
[3163.08 --> 3170.44]  and from my own experience i can tell you that parsing text protocols which have kind of very ambiguous
[3170.44 --> 3176.44]  semantics about things where they terminate how they terminate and all the rest is much harder than a
[3176.44 --> 3182.84]  length prefixed binary protocol which is very particular right it just says how many bytes i'm going to send you
[3184.20 --> 3190.28]  and then the type of frame and you ask specific rules for how to parse the data so in practice it's actually
[3190.28 --> 3199.72]  easier to implement binary protocols uh it is more provably correct in the sense that there's far
[3199.72 --> 3205.16]  fewer edge cases that you have to consider and performance wise because you're twiddling bits is
[3205.16 --> 3209.48]  actually better as well for the server because now you don't you're not parsing strings you're parsing just
[3210.04 --> 3214.84]  bits bits and bytes right uh so that's that's the implementation bits
[3214.84 --> 3222.68]  there are other uh implementation concerns uh with things like hpack and all the rest and there's
[3222.68 --> 3226.36]  more complexity on the server in terms of dealing with priorities but that's kind of a separate
[3226.36 --> 3236.44]  discussion then from the observability part um i i'm sympathetic to the use case of well i just want
[3236.44 --> 3242.36]  to open telnet and type in get and make the request or like observe it uh but realistically i don't think
[3242.36 --> 3248.92]  that's a that's a very compelling use case or very common at that and uh if you need observability
[3248.92 --> 3254.04]  then it's just a question of tooling like maybe we just need better tools we we already have great
[3254.04 --> 3261.08]  plugins for wireshark uh that will parse all the binary data and show you all of the all the things that
[3261.08 --> 3265.64]  you're used to similarly if you open say chrome dev tools or any dev tools in any browser
[3266.28 --> 3270.28]  it doesn't matter where you whether you're running over http1 or http2 like all of it is already
[3270.28 --> 3276.12]  parsed and you can see all the data there right uh and further like if you use tls then that's
[3276.12 --> 3282.12]  already binary framing right like so there's nothing new here uh it's just a question of tooling and
[3282.12 --> 3288.20]  it like i do see some kind of short-term pain where we go from something that was easily inspectable
[3288.20 --> 3296.52]  because you can just run uh like a grep on a stream right uh to something that needs to take the stream
[3296.52 --> 3302.52]  parse it and then grep it uh but that's i think that's very easily solved so it's essentially it
[3302.52 --> 3311.00]  sounds like the binary framing layer has allowed you to provide a more testable provable method to do it
[3311.00 --> 3317.80]  rather than with text-based where before it had more edge cases that to work around and more potential to
[3317.80 --> 3328.44]  fail yep exactly yeah uh we talked about security we talked about uh several things there does it
[3328.44 --> 3332.60]  make sense to dive into the hpc whatsoever i know there was kind of two components to that we talked
[3332.60 --> 3338.44]  a bit about that but not quite that deeply on how that changes the headers to the fact that it's got
[3339.24 --> 3344.12]  the frame layer and the data the header frame and then the data frame i think that particular aspect is
[3344.12 --> 3352.92]  most interesting to implementers um as a user i'm more thinking about how do i use this you know who's
[3352.92 --> 3359.24]  using this what's the upgrade process how does it implement how does it impact browser clients and server
[3359.24 --> 3367.40]  clients um maybe we can go there ilya and talk about adoption and who's adopting it how it's rolling out
[3367.40 --> 3373.24]  and then how how do we adopt it sure yeah so i guess let's start the beginning with the spec itself so the
[3373.24 --> 3380.68]  spec has been finalized it's been published as rfc so i believe it's is it rfc 7540 and 7541
[3381.40 --> 3389.64]  i think that's correct so that's that's out in the wild um as of a month ago back in february
[3391.08 --> 3397.48]  firefox was the first browser to enable http2 in their stable browser so if you're using firefox
[3398.28 --> 3402.52]  and you're talking to a server that is capable of talking http2 then you're already talking http2 which is
[3402.52 --> 3409.08]  great uh chrome has already also enabled support that was shortly after firefox so both browsers
[3409.08 --> 3416.12]  support http2 in stable today um ie has indicated that they will ship http2 support and actually
[3416.68 --> 3424.20]  actually let me make that stronger so ie their new browser um edge is shipping with windows 10 which is
[3424.20 --> 3432.92]  coming out i believe at the end of july i want to say 29th of july and edge supports http2 so as of
[3433.48 --> 3438.36]  early august you can get your hands on our users real users will start getting their hands on on
[3438.36 --> 3446.28]  stable version of windows windows 10 which will have edge which will talk http2 safari also supports speedy
[3446.28 --> 3453.40]  uh safari or apple in general does not generally comment on their plans uh but there is no absolutely
[3453.40 --> 3460.28]  no reason to believe that they will not support http2 uh sooner rather than later and in fact uh because
[3460.28 --> 3468.68]  we do not want uh maintain to maintain both protocols speedy and http2 and we want to move people towards
[3468.68 --> 3475.08]  hp2 chrome has actually announced that we will deprecate speedy in chrome in early 2016
[3476.76 --> 3482.52]  which is kind of a nudge to the community to say that like hey you've deployed speedy and but there's a
[3482.52 --> 3487.64]  better thing and an official thing called hp2 so let's move over there so there's kind of this year
[3487.64 --> 3492.20]  grace period where we've more or less formalized hp2 to deprecating speedy
[3492.20 --> 3499.16]  uh so that's client support uh there's also a growing and a good list of implementations
[3499.72 --> 3506.68]  for hp2 at for various languages so kind of libraries and all the rest uh if you go to the
[3506.68 --> 3514.04]  h if you just search for hp2 wiki uh you will come to a github site that has a list of implementations
[3514.04 --> 3521.40]  and maybe we can share that in the notes afterwards so you'll find i think most every popular language
[3521.40 --> 3527.00]  you'll find support for it is that http2.github.io is that the one you're talking about yep that's the
[3527.00 --> 3533.32]  one and then at the top there you'll see a link to implementations yes and that contains a table it's
[3533.32 --> 3541.32]  just a wiki page on github that contains the list so you know if you're working on on an implementation
[3541.32 --> 3546.36]  please do add it there so that's uh so let's see that's that's client uh in terms of servers uh
[3546.36 --> 3553.40]  there are some really good implementations out there already so uh there is there are a number of
[3553.40 --> 3560.60]  big sites that have enabled it on their servers so uh twitter google facebook a bunch of others
[3561.16 --> 3566.60]  there are also open source implementations so coming out of this whole h2 h2 effort there's
[3566.60 --> 3572.36]  actually a couple of new servers that have merged for example in ng http and h2o
[3572.36 --> 3580.12]  uh both built by the hp2 community in uh in japan uh they're very good what was the second one
[3580.12 --> 3587.88]  earlier uh h2o h2o yeah some high quality h2o nice yep yep and they're they're actually they're very
[3587.88 --> 3593.32]  good you can you can try and deploy them today uh you can play with them rather uh and there is
[3593.32 --> 3601.40]  support coming to kind of more popular uh servers as well so engine x and has announced that uh they will
[3601.40 --> 3607.72]  support uh hp2 or they will add support for hp2 sometime in i think q3 or q4 of this year
[3609.00 --> 3612.68]  so they support speedy today but that will be replaced with hp2
[3614.52 --> 3622.20]  yep uh varnish uh said that they're working and that's likely coming kind of in early 2016 that's my
[3622.20 --> 3630.12]  understanding uh then there is apache traffic server already supports hp2 uh there is a couple of
[3630.12 --> 3638.36]  modules for apache that implement hp2 so um well what else node there's there's guessing
[3638.36 --> 3645.08]  limitations for hp2 i mentioned that i built a ruby version uh it's a library not a server but you can
[3645.08 --> 3651.56]  build it or a client or server with it so all that to say like the support is coming it's growing the
[3651.56 --> 3658.84]  client support is there the servers are coming online uh there's lots of usage of it on the web
[3658.84 --> 3665.56]  today already which i think is really important to note uh hp2 is not some kind of like newfangled
[3665.56 --> 3671.56]  thing that has not been tested uh recall the fact that speedy has been been in development in parallel
[3671.56 --> 3678.28]  with hp2 and effectively uh we've been testing all of these ideas for a very long time for like five years
[3678.28 --> 3684.92]  plus so a significant portion of the traffic on the web today is already using hp2 and this is a very
[3684.92 --> 3693.24]  well tested uh protocol so it's safe to deploy and production ready awesome well i think we will take
[3693.24 --> 3698.84]  a break here and we come back we'll talk about straddling the line between h1 and h2 and also
[3698.84 --> 3703.72]  if you're interested in the nitty-gritty details how you can learn more let's take a break and we'll be right
[3703.72 --> 3710.36]  back all right put them away put them back put the books back on the shelf you don't need them
[3710.36 --> 3720.44]  and learn to code by doing with code school code school offers a variety of courses javascript html css
[3720.44 --> 3729.08]  ruby ios git and many many more to help you expand your skills and learn new technologies code school
[3729.08 --> 3734.76]  knows that learning to code can be a daunting task and they've combined experienced instructors
[3734.76 --> 3740.04]  with proven learning techniques to make coding educational and memorable gives you the confidence
[3740.04 --> 3745.64]  you need to continue past those rough tough hurdles that you will definitely face learning the code code
[3745.64 --> 3750.52]  code school also knows that languages are a moving target they're always updating their content to
[3750.52 --> 3755.56]  give you the latest and the greatest learning resources you can even try before you buy roughly
[3755.56 --> 3761.72]  one out of every five courses on code school is absolutely and totally free this includes
[3761.72 --> 3769.24]  instructor classes on git ruby jquery and much more which allow free members to play full courses with
[3769.24 --> 3775.64]  coding challenges all included you can also pay as you go one monthly fee gives you access to every
[3775.64 --> 3781.40]  code school course and if you ever need a breather take a break you can suspend your account at any time
[3781.40 --> 3786.52]  don't worry your account history your points your badges they'll all be there when you're ready to
[3786.52 --> 3792.04]  pick things up again get started on sharpening your skills today at code school.com once again that is
[3792.04 --> 3801.40]  code school.com all right we are back we are talking with ilia gregorik about http2 aka h2
[3801.40 --> 3811.96]  the new hotness in web performance um it's here it's arrived the spec is finalized support is coming
[3813.16 --> 3818.44]  h1's gonna be around for a long time isn't it it's not going to air nope nope we're not gonna
[3818.44 --> 3825.96]  full-on replace it it's with us for a while but the nice news is is that as um people that deploy websites
[3825.96 --> 3833.08]  doesn't matter too much because we can just wait for the client to say they support uh the new hotness
[3833.08 --> 3837.88]  and then just kind of upgrade them and not worry about anything else is there anything at an application
[3837.88 --> 3843.32]  level i mean server push i thought maybe would play in but really that's just like pushing assets it's
[3843.32 --> 3849.00]  not like uh server push as opposed to long polling um is there anything at the application level somebody
[3849.00 --> 3854.44]  who's building a web app that they'd have that they could like leverage in h2 feature wise
[3854.44 --> 3859.48]  uh yeah definitely there's it comes back to the question of
[3861.96 --> 3867.16]  whether and what you can do to optimize for htp2 right so we said earlier that any application will
[3867.16 --> 3873.00]  continue to work over htp2 so if you just deploy a new server that happens to talk htp2 everything
[3873.00 --> 3878.20]  will just work right then the question becomes can i make it better and the answer is there's probably
[3878.20 --> 3882.76]  most definitely yes and this is where we have to get into a whole separate discussion about like
[3882.76 --> 3889.56]  let's re-examine some of our existing yeah in air quotes best practices to uh revisit them and see
[3889.56 --> 3894.68]  if we can undo some of the damage so uh i don't think we have enough time to get into all of these
[3894.68 --> 3902.04]  but things like domain charting is and clearly an anti-pattern on uh on htp2 so you want to avoid that
[3902.04 --> 3908.44]  and there's actually some uh good and nifty tricks that will allow you to do that without changing anything
[3908.44 --> 3915.80]  in your application um so i'll just i have a i have a resource that talks about that in particular
[3915.80 --> 3920.36]  that we'll mention later uh then there is concatenation so you can actually start undoing
[3920.36 --> 3925.08]  some of that and then the question becomes like well if i want to optimize for both protocols because
[3925.08 --> 3931.64]  i have clients in both camps how do i do that and i think the practical answer there is you can make
[3931.64 --> 3936.60]  it arbitrarily complex in the sense that you can actually say well i know which protocol the client
[3936.60 --> 3940.76]  negotiate it's all sort of one version of a website here and another version of website there
[3940.76 --> 3944.60]  perhaps it's a little too involved i think a more interesting question now becomes like
[3945.16 --> 3951.16]  maybe there's a happy middle uh as more and more users migrate towards htp2 i think you will see a
[3951.16 --> 3957.16]  very quick rise in adoption of htp2 in terms of capabilities i think the server basically by the
[3957.16 --> 3963.72]  end of this year will have very good server support i expect very good client support as well and at
[3963.72 --> 3970.20]  that point the majority of the user user on htp2 i think you i think that should be sufficient to
[3970.20 --> 3975.96]  nudge most websites to say well now we're willing to sacrifice some of the performance in htp1 without
[3975.96 --> 3981.88]  adding too much complexity in our in our actual development process in order to optimize for htp2
[3981.88 --> 3987.16]  so perhaps we'll undo some of the concatenation maybe we won't ship a hundred files but we can now
[3987.16 --> 3993.32]  consider sending 10 files right which may have some slightly negative repercussions for htp1 but it makes
[3993.32 --> 3997.80]  things much better because we can do caching and all these other things similar things with server
[3997.80 --> 4005.56]  push there is lots of cool opportunities there for total automation so one cool example is
[4006.92 --> 4014.92]  jetty jetty java http web server has had support for htp2 for a long time and they actually have this
[4014.92 --> 4021.32]  really cool mode where the server observes the requests that come in so say the client requests the
[4021.32 --> 4026.44]  index file and then and then the client also comes back and asks asks the css file and javascript
[4026.44 --> 4034.44]  file there's a refer header that it can use to infer um kind of that map of well you asked this and
[4034.44 --> 4039.56]  then you came back for these other things it observes that traffic pattern and then automatically starts
[4039.56 --> 4044.76]  server push for future clients so you as a developer don't have to do anything the server just takes care
[4044.76 --> 4048.68]  of all of all of these things so i think we're going to see a lot of innovation in that space
[4048.68 --> 4057.00]  uh there's new uh capabilities in terms of like well can you push uh cache invalidations so if i told
[4057.00 --> 4062.04]  you to cache something for a year uh can i push a record that says well please delete that out of your
[4062.04 --> 4067.32]  cache uh so i think that those are the new and interesting things that we're still yet to explore
[4067.80 --> 4074.20]  uh but we're in pretty good shape awesome so i think by now our listeners are probably in two camps
[4074.20 --> 4080.36]  camp one is thinking http two sounds awesome i can't wait till nginx supports it so i just get
[4080.36 --> 4085.72]  better performance kind of out of the box for my web app and then camp two is probably like i want to
[4085.72 --> 4091.72]  dig in i want to understand hpack i want to understand server push and the binary framing and stuff
[4092.36 --> 4097.80]  um i think for the second group we have good news with regards to your book high performance browser
[4097.80 --> 4104.92]  networking you want to tell us about that yeah uh so that's a book i've been working on or worked on
[4104.92 --> 4113.08]  with a reilly uh it's available today um and the book actually came out let's see a year and a half
[4113.08 --> 4119.88]  ago and in the original version i talked about the earlier drafts of http 2 and speedy and i recently
[4119.88 --> 4126.36]  updated that so the print version does not have the latest content but the good news is that you can go
[4126.36 --> 4136.84]  online and read the up-to-date content for free in your web browser and you can find it at hpbn.co
[4137.88 --> 4142.76]  if you just add slash hp2 you can just go to the chapter directly or you can just scan through the
[4142.76 --> 4149.96]  entire book and it covers all the things we talked about here but probably much more coherently and in
[4149.96 --> 4154.76]  more detail so you can learn about kind of all the nitty-gritty of the protocol and there's also a
[4154.76 --> 4160.52]  follow-up section on well now that we have this how can we what should we revisit and how can we
[4160.52 --> 4165.64]  optimize our applications awesome so we'll link that up in the show notes and you did hear him
[4165.64 --> 4169.64]  right the print version is not up to date so whatever you do don't buy the book
[4175.08 --> 4180.84]  yeah so i should say uh we've been updating so the beauty about writing technical books is they go out of
[4180.84 --> 4186.52]  date the moment you hit publish so i've been updating the content kind of in small and incremental bits
[4186.52 --> 4191.64]  ever since it was published and we've actually released updates print updates since then uh and
[4191.64 --> 4197.80]  the hp2 one is just much newer so it hasn't yet made it into the print version so if you were to buy a copy
[4198.60 --> 4204.60]  today when we're recording this it wouldn't have the the latest hp2 but the plan is to definitely have it
[4204.60 --> 4210.68]  there you mentioned potentially even like a smaller volume just for these this new protocol coming in
[4210.68 --> 4215.64]  place and sort of diving deep into that that's right actually if you go to the o'reilly website
[4215.64 --> 4222.36]  and you search for hp2 now they've published the the new chapter the new hp2 chapter as a separate ebook
[4222.92 --> 4229.00]  so if you just want to read that you can get that as a kindle pdf or one of whatever version you prefer
[4229.00 --> 4236.28]  gotcha we'll uh we'll definitely link up the chapter 12 is the chapter it is so if you're
[4236.84 --> 4241.96]  on the high performance browser networking site and you're already there then just navigate the
[4241.96 --> 4249.32]  chapter 12 and you'll see the new chapter there for hp2 can you restate the the url that you said was
[4249.32 --> 4253.56]  the blessed one for you because i got the long version which i think was a redirect are you tracking
[4253.56 --> 4258.20]  that or something like that uh yeah it's it's just it's just more convenient it's a shortened version so
[4258.20 --> 4262.44]  it's hpbn which is the high performance browser networking it's just the first letters of the book
[4263.16 --> 4270.28]  uh dot co slash hp2 yep and that should take you to i guess chapter 12 gotcha perfect
[4271.80 --> 4277.24]  well jared what else we got to cover i know we talked about pretty much everything um i think the
[4277.24 --> 4283.64]  only thing we didn't talk about really was was uh something that was sort of off topic but sort of
[4283.64 --> 4290.92]  in this camp to a degree which was ilia your focus on time to glass and jared and i before the call
[4290.92 --> 4295.00]  we talked about time to glass and i was like well what is what is time to last year do you know what
[4295.00 --> 4300.36]  this is this is a term you've heard before and jared what did you say uh google glass time to google
[4300.36 --> 4306.04]  glass how to get our websites onto google glass faster than you thought it was so how long it takes
[4306.04 --> 4310.68]  someone to buy google glass that's your time to glass yeah i think today that's pretty long
[4310.68 --> 4317.40]  i think it's quite quite the wait list yeah so i mean we talked heavily about h2 and what that's
[4317.40 --> 4323.96]  bringing we talked quite a bit about stride online and and uh what your suspected best practice is to
[4323.96 --> 4330.76]  support h2 and h1 at the same time which is to you know sort of monitor your your usage and as the
[4330.76 --> 4337.80]  number teeters more towards h2 support more performance uh enhancements for that are prescribed by
[4337.80 --> 4345.00]  h2 versus h1 but what is this thousand milliseconds time to glass challenge that that was in one of your
[4345.00 --> 4353.40]  slides as you talked about h2 sure so the the general premise is that we want to make pages visible or
[4353.40 --> 4360.60]  respond to user input within less than a second and that means like from the moment that you type in a
[4360.60 --> 4365.64]  url to to you hitting enter regardless of what type of network you're on whether you're on a mobile phone
[4365.64 --> 4372.04]  uh with a crappy connection or on a fast gigabit connection you should have something visible to
[4372.04 --> 4377.56]  you within a second and if you accept that as a challenge then it becomes a question of well okay
[4377.56 --> 4383.00]  so what are the mechanics behind that like if you factor in all the latencies for setting up a connection
[4383.00 --> 4388.20]  and making the request and getting a response you very quickly arrive at the conclusion that you
[4388.20 --> 4393.48]  actually don't have a lot of time like a second seems like a long a lot of time but it's actually not
[4393.48 --> 4398.04]  very much like it puts very hard constraints on how quickly your server has to respond
[4398.04 --> 4403.88]  how you structure your pages and a lot of other details and actually if you're curious about this
[4403.88 --> 4411.64]  particular topic i'll uh i'll do another plug i actually have a udacity course which it's probably
[4411.64 --> 4416.28]  take you a couple of hours to go through but we kind of talk through in great detail about how the
[4416.28 --> 4421.56]  browser actually constructs the page like from receiving the first html bytes to parsing css and
[4421.56 --> 4426.28]  executing javascript like what does that pipeline look and what do you need to think about to allow
[4426.28 --> 4432.52]  the browser to paint something very quickly because you can take the same page with the same assets and
[4432.52 --> 4438.84]  you can make it block and not render anything for like arbitrarily long say five or ten seconds right
[4438.84 --> 4444.28]  and you can make the same page render something very quickly but then continue progressively adding
[4444.28 --> 4450.60]  content later and that and the latter is the behavior that we want to enable so this is both on the
[4450.60 --> 4454.04]  browser like there's lots of things that the browser has to do to make this happen but also
[4454.04 --> 4458.12]  on the developer because there are certain things that you do that the browser just can't work around
[4459.16 --> 4464.12]  and the reason why it's accompanied in your http2 talks is because a lot of this is really depending
[4464.12 --> 4470.52]  upon this entire conversation we just had which was h2 being more supported and that's gonna like
[4470.52 --> 4476.52]  getting to one second on h1 is probably a lot harder or near impossible but h2 makes it more possible
[4476.52 --> 4481.48]  yeah exactly that's that's a question about uh like i need to fetch this many assets and only have
[4481.48 --> 4491.00]  this much time uh but http2 or http1 places strict uh restrictions on how many things i can fetch in
[4491.00 --> 4498.60]  parallel so that prohibits me from say hitting that goal whereas with http2 we can actually work around a
[4498.60 --> 4504.44]  lot of those things or rather not work around http2 fixes all those things and one of the reasons why i wanted to
[4504.44 --> 4508.68]  to bring that into i know it's sort of slightly off topic and in addition to the conversation we just
[4508.68 --> 4514.04]  had but if you've been following along in change law weekly which we ship out every saturday the last
[4514.04 --> 4520.92]  two weeks we've uh we've talked about this time to glass uh term and one of them linked to something
[4520.92 --> 4526.12]  you had done illia i can't recall the link but um to recommend right now but i'll put it in the show
[4526.12 --> 4531.48]  notes for those listening and even to the issues of weekly but um i wanted to bring that up since you
[4531.48 --> 4535.16]  were here on the show we talked about time to glass recently in change law weekly so for those
[4535.16 --> 4541.80]  listeners that read that email once every week uh sort of closes some of the gap on on the term itself
[4541.80 --> 4548.04]  and what that means for h2 and getting closer to one second what our 1000 milliseconds or one second
[4548.04 --> 4553.32]  time to glass yeah it's a it's a really interesting topic if you're uh interested in kind of web web
[4553.32 --> 4561.08]  development in general but also just uh performance because it turns out that a lot of um a lot of
[4561.08 --> 4565.96]  use cases right now are driven by mobile which places a lot of restrictions on latency and also
[4565.96 --> 4571.80]  emerging markets so there's explosive growth in terms of number of users coming online in places like
[4571.80 --> 4577.80]  india brazil and russia and everywhere else and networks are kind of slow there and they're also
[4577.80 --> 4584.28]  expensive and we need to think really really carefully about how we build pages and all the rest so
[4584.28 --> 4591.40]  that's that's probably enough uh of material there to like talk about on another three episodes
[4593.00 --> 4599.72]  yes uh actually uh it i went back and looked episode 54 or sorry issue 54 of
[4600.44 --> 4604.92]  change law weekly we actually linked to this chapter 12 that we just been talking about here so that was
[4604.92 --> 4611.08]  the one link the other one was talking about rails and turbo links and how turbo links aren't as bad as
[4611.08 --> 4615.80]  everyone says they are the reals community has been seeing this all along and and bonus we actually
[4615.80 --> 4621.64]  linked out to your talk on breaking the 1000 millisecond time to glass mobile barrier which is what
[4621.64 --> 4628.20]  we've been talking about here so yep there you go circle completed well it's definitely fun having
[4628.20 --> 4632.84]  you back for for three times we'll get your jacket out to you soon enough uh so you can wear that with
[4632.84 --> 4638.44]  pride it's got the changelog emblem on there and it's got i've been on the changelog three times on the
[4638.44 --> 4643.80]  back you can wear it to the office or local meetups whatever you know sweet whatever whatever
[4643.80 --> 4649.40]  just tickles your fancy on that part there uh jerry any thoughts on the closing here no just
[4649.40 --> 4655.56]  really appreciate you coming on the show we really enjoyed it i've been interested in the innards of
[4655.56 --> 4661.56]  what's coming on down the pipeline with h2 for a while so i'm glad we got the chat good deal all
[4661.56 --> 4668.04]  right well that's uh that is the show and for now let's say goodbye everybody see ya see ya thanks
[4668.52 --> 4673.88]  so
[4674.36 --> 4677.72]  okay
[4696.20 --> 4696.68]  you
[4698.44 --> 4728.42]  Thank you.
