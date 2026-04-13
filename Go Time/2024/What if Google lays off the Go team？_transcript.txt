[0.00 --> 16.60]  let's do it it's go time welcome to go time your source for wide-ranging discussions from all
[16.60 --> 24.30]  around the go community find us on the web at gotime.fm on the fediverse at gotime at changelog.social
[24.30 --> 31.54]  and on x at gotime.fm thanks to our partners at fly.io the home of changelog.com launch your app as
[31.54 --> 37.68]  close to your users as possible find out how at fly.io okay here we go
[37.68 --> 49.30]  our friends at fire hydrant offer modern engineering teams less stress from ring to retro
[49.30 --> 57.60]  full end-to-end incident management alerting on call and of course streamlining every aspect of
[57.60 --> 65.24]  your incident process from webhook to alert trigger to notifications to incidents open to retro tasks to
[65.24 --> 72.60]  meantime to x analytics everything is inside fire hydrant for modern engineering teams and what
[72.60 --> 77.36]  you're about to hear are real reactions from pager duty users when seeing signals from fire hydrant
[77.36 --> 83.20]  for the first time pager duty i don't want to say they're evil but they're an evil that we've had
[83.20 --> 89.06]  to maintain i know all of our engineering teams as well as myself are interested in getting this moving
[89.06 --> 95.68]  the correct direction as right now just managing and maintaining our user seats has become problematic
[95.68 --> 100.88]  that's all that's that's really good actually this is this is a consistent problem for us and teams is
[100.88 --> 106.46]  that covering these sorts of ad hoc time frames is is very difficult um you know putting in like
[106.46 --> 113.24]  overrides and specific days and different new ships is is quite onerous oh and you did the most
[113.24 --> 118.10]  important piece which is didn't tie them together because that's half the problem with pager duty
[118.10 --> 124.44]  right is i get all these alerts and then i get an incident per alert and generally speaking when
[124.44 --> 131.10]  you go sideways you get lots of alerts because lots of things are broken but you only have one incident
[131.10 --> 137.12]  yeah i'm super impressed with that because being able to assign to different teams is an issue for us
[137.12 --> 142.12]  because um like the one the one alert fires for one team and then it seems like to have to bounce
[142.12 --> 147.88]  around and it never does uh which then means that we have tons of communication issues because like
[147.88 --> 153.26]  people aren't updated no i mean to to be open and honest uh when can we switch
[153.26 --> 160.88]  okay the next step is to go to firehydrant.com slash signals assemble the team and work the problem
[160.88 --> 166.52]  without a single swivel of the chair fire hydrant delivers end-to-end incident management and on-call
[166.52 --> 173.64]  learning for the modern software teams get started for free once again firehydrant.com slash signals
[173.64 --> 198.82]  hello hello hello and welcome to go time this week we're talking about the news or at least some
[198.82 --> 204.30]  of it for this episode i have two wonderful co-host i'm joined by ian lobshire how are you doing today
[204.30 --> 209.58]  ian i'm doing wonderful excellent and i'm also joined by johnny borsico how are you doing johnny
[209.58 --> 216.28]  i'm doing all right all right so yeah we we got a couple news articles that were i guess not they're
[216.28 --> 221.30]  all not news articles some of them are like social media posts but also we got a whole bunch of articles
[221.30 --> 225.22]  that we're going to talk about a whole bunch of news we're going to talk about and uh first up is this
[225.22 --> 231.82]  discussion from reddit about uh what might happen if google decided to part with the core go team
[231.82 --> 238.00]  and what that might mean for go's future adoption let's start by like uh explaining why this come came
[238.00 --> 246.24]  up um the the layoffs at google they appear to have fired a large number of the flutter team the dart team
[246.24 --> 254.20]  and a lot of their python teams um just a little bit crazy there is this like google's uncanny ability
[254.20 --> 261.08]  to get rid of useful products that people still use and love they're like well let's extend this
[261.08 --> 269.62]  philosophy to language teams and it's not just products in the chopping block it's programming languages
[269.62 --> 274.74]  frameworks like we need a verb we need a verb for google getting rid of useful things like
[274.74 --> 282.06]  inboxing or something um inboxing or uh what was that was the really popular one google uh
[282.06 --> 291.66]  waving it we could call it oh man man if you're old enough to remember google wave well i i am so i'm
[291.66 --> 299.02]  not gonna say anything bad about it but dang oh man google's been been waving off products for a long
[299.02 --> 303.70]  time huh oh that's a that's a good verb for that too yeah it's like oh wave wave goodbye to those
[303.70 --> 308.20]  products but yeah so yeah that's the that's the background of it as ian said we're you know they
[308.20 --> 314.08]  they've decided to lay off some more people this is like a an interesting time in the tech industry
[314.08 --> 320.54]  as far as big companies doing lots of rounds of layoffs of various different teams but given that
[320.54 --> 325.50]  background and context there's like quite a bit of quite a bit of discussion some thoughts i think
[325.50 --> 331.40]  that the top comment or the top uh because this is in reddit so the top reply is basically kind of
[331.40 --> 335.78]  saying there's probably not going to be that big of a problem if they did but they probably won't do
[335.78 --> 342.88]  it what do you think what do you guys think well it goes go up is open source right so i don't know
[342.88 --> 349.96]  it's there's a lot of there's a lot of open source projects that i mean it is open source that's great
[349.96 --> 356.70]  but we can't underestimate basically having a corporate benefactor right behind certain corporate
[356.70 --> 363.64]  projects um if they weren't funding the development of these things in some way whether directly or
[363.64 --> 369.80]  sponsoring the the teams that work the contributors that were out in the community that sort of um keep
[369.80 --> 376.54]  something alive i don't think we can underestimate the power of you know a mega funder like like google
[376.54 --> 384.90]  so but i'd say that there's there are enough large companies using go that rely on go um whether it's at the
[384.90 --> 391.72]  infrastructure level or part of their product or whatever it is um that i think if i mean that's
[391.72 --> 399.30]  my hope at least that if google were to sort of take a back seat on sort of the leadership for go
[399.30 --> 405.70]  other companies would definitely be vying for that spot they would definitely want to step in now what
[405.70 --> 411.32]  the governance model would be right now it's the go team that decides what goes in obviously with input
[411.32 --> 415.94]  and contribution from the community but it's a centralized sort of corporate decision body
[415.94 --> 422.00]  basically you know and so far you know i can't i can't really complain with some of the decisions
[422.00 --> 427.36]  they've made um not everything has been smooth um you can't really expect it to be but they've done a
[427.36 --> 433.84]  pretty good job so if all of that were to change we don't know what we would get for leadership of the
[433.84 --> 440.80]  language now right so it would certainly give a sort of a a branding blow to go not a critical
[440.80 --> 448.86]  technical blow right but it will also create a leadership sort of uncertainty right for a while
[448.86 --> 454.88]  until the dust sort of settled i feel like if if google did just like okay we're we don't want to do
[454.88 --> 458.96]  go anymore we're going to get rid of it we're going to lay off the whole team i feel like one of the other
[458.96 --> 465.92]  big tech companies like amazon or microsoft would just pick up that whole team and be like okay then
[465.92 --> 470.28]  we'll just we'll just start doing this i mean like microsoft what they basically almost did that with
[470.28 --> 474.80]  open ai and that was a whole lot more people than the go team and as we'll talk about later like
[474.80 --> 479.94]  microsoft seems to have a pretty significant investment in go so it seems like some some kind
[479.94 --> 485.08]  of corporate benefactor some someone would want to actually pick this up and run with it if it was
[485.08 --> 490.76]  kind of the whole team just being let go at once or like a foundation because i think as mentioned in
[490.76 --> 497.04]  the in the reddit post there's like the cncf has so many different projects that are written in go
[497.04 --> 503.58]  you know you're not going to rewrite kubernetes at this point in another language so it'd be some
[503.58 --> 509.70]  will try i mean people will try but like is the cncf really gonna like if they had to weigh it are they
[509.70 --> 515.06]  gonna let go just disappear and then try and rewrite all of their projects in other language or would
[515.06 --> 520.86]  they just be like okay we're gonna help pick up the slack so by comparison does c have a major
[520.86 --> 526.62]  corporate body behind it i mean still still still around it's still being used and you know it's
[526.62 --> 533.04]  certainly underpins a lot of technologies that we build on top of so i mean c is a standard so they
[533.04 --> 537.00]  have the standards body that's behind it just like c plus plus is also a standard so it has like a
[537.00 --> 542.72]  standards body behind it we've also seen these languages be spun off corporate benefactors before
[542.72 --> 549.66]  right like russ survived mozilla's kind of mozilla mozilla's dive so yeah i don't think it's gonna
[549.66 --> 554.74]  happen but if it did i'm not sure there's a ton to worry about yeah i feel like the the more worrying
[554.74 --> 559.44]  thing would be like the slow starvation of resources from the go team like if google like
[559.44 --> 563.86]  slowly started under investing in go and then you'd have to be like okay well
[563.86 --> 568.98]  that that almost seems worse than just a just a smooth like okay we're just getting out of the
[568.98 --> 573.12]  the whole game like goodbye we're shutting down this whole division figure it out rest of the
[573.12 --> 577.52]  world laying off half the team would be way worse than all of them right right so yeah if all of a
[577.52 --> 583.62]  sudden you know russ cox has been reassigned to something else and ian lance taylor all of a sudden
[583.62 --> 593.12]  you know other projects or you know if all the well-known you know people who lead the team at least
[593.12 --> 598.62]  technically sort of change roles and get reassigned or something i don't know i'd be scratching my head
[598.62 --> 604.68]  i'd be like wondering uh what's about to happen here uh are we getting waved off or like you know
[604.68 --> 612.02]  what's happening i do wonder what would happen to like the module repo and the go.dev site
[612.02 --> 617.40]  the doc site because that's all google hosted right now right yeah there's like a whole bunch of
[617.40 --> 622.84]  infrastructure that is currently hosted by google and there have to be some plan to actually
[622.84 --> 628.00]  migrate it but even you know in that case i think i don't think google would would be like oh we're
[628.00 --> 632.70]  just going to shut everything down i think they'd probably do something like google domains and be
[632.70 --> 639.36]  like okay we're going to find somebody else who wants to have this now squarespace squarespace now host
[639.36 --> 647.52]  go.dev i'm sure it'd be picked up by like amazon or microsoft but it's now go.squarespace.com
[647.52 --> 655.76]  that is so freaking funny oh man
[655.76 --> 663.36]  there's some ads that come along when you go check out some vulnerabilities oh yes you edit the
[663.36 --> 672.08]  go website in their in their nice whizzy way uh some ads and some some shops that just
[672.08 --> 677.62]  it's auto suggested to you in your go.mod file oh lord
[677.62 --> 682.78]  check out these check out these shoes
[682.78 --> 692.82]  you imported this module and people that import this module like lasagna so here's some good frozen
[692.82 --> 701.38]  lasagna yeah oh man oh it's so funny my uh i have tears
[701.38 --> 711.64]  oh please google don't do this i i i don't think google is gonna sell go to squarespace i think i think
[711.64 --> 720.24]  we're okay oh man could google even sell go is that a thing they could do i mean i pretty sure they own
[720.24 --> 728.32]  like the copyrights so yes i mean it'd be it'd be kind of weird but i think they own the brand yeah
[728.32 --> 733.28]  that's right the people that built go worked at google at the time and google has those all
[733.28 --> 739.16]  encompassing contracts that are like we own all of it so so go is open source what what does
[739.16 --> 746.42]  intellectual property law look like for open source like open source means you just can use it
[746.42 --> 750.62]  yeah really reuse it and do all kinds of things right does that mean it mean that you couldn't
[750.62 --> 754.72]  like if you forked it you couldn't call it go like it's the same thing that happened with like
[754.72 --> 759.14]  terraform right where they they forked terraform but they can't call it terraform because terraform
[759.14 --> 765.70]  is intellectual property of hashicorp so go is intellectual property like the brand of it wait who forked
[765.70 --> 772.42]  terraform uh the get off topic a little bit cncf did with open tofu ian's been living in the
[772.42 --> 778.02]  iraq for the last couple of weeks maybe we should do more of it wait was this after they sold to ibm
[778.02 --> 782.94]  is that no that was it was way before this was like six months ago how did i miss this i don't know
[782.94 --> 789.02]  you yeah you bet me because you don't use terraform that often hashicorp did the reddest thing or i guess
[789.02 --> 792.70]  reddest did the hashicorp thing which did like the so many other companies thing where they relicensed
[792.70 --> 798.60]  it as this dual license and everybody was like no and so the group of people got together and they
[798.60 --> 804.86]  forked terraform and they made open tofu all right another thing to add to my reading list um yeah
[804.86 --> 811.84]  thankfully there's only one fork unlike redis where there's like so many um wait isn't there a there's
[811.84 --> 815.74]  an apache fork of redis now right there's a lot okay we're getting off topic oh i'm sure there's
[815.74 --> 821.70]  lots of forks of redis i mean my mom probably has a fork of redis at this point it's it's
[821.70 --> 831.38]  you know so it's it's it's fine like it'll be interesting if ibm sort of reverts the whole
[831.38 --> 836.76]  terraform licensing although i like the backhole they did i think it was reading something where i
[836.76 --> 842.94]  think ibm does have a fork of terraform like an open source fork of terraform and everybody's like
[842.94 --> 851.24]  huh it's all this it's it's a interesting situation but so i guess the answer to the question is like yes
[851.24 --> 857.14]  you you could sell go or at least the ip to it like i mean you could if you sold it to someone
[857.14 --> 862.48]  like oracle i'm sure they'd try and find a way to un-open source it as well but i think everybody
[862.48 --> 868.40]  else would just kind of take it and run with it and be like okay yeah maybe well let's us all uh
[868.40 --> 874.82]  hold our breath and hope that doesn't happen um yeah like which part specifically the all of it
[874.82 --> 880.84]  but uh all of it oh okay okay good yeah yeah we're in agreement there oh good lord yeah i mean
[880.84 --> 886.92]  i think we're all pretty pretty safe from google abandoning go but also from like a contribution
[886.92 --> 891.52]  standpoint i think like the majority of core contributions come from outside of google
[891.52 --> 897.52]  so it's not like the the language would necessarily slow down in development you just have to
[898.36 --> 901.58]  there's really you need to find a new home for things and as i think you said johnny like a new
[901.58 --> 907.68]  governance model to uh figure out like how do proposals happen what gets into the the core
[907.68 --> 912.40]  language as far as like big things not like the small things where people are just kind of like
[912.40 --> 917.34]  maintaining a library or something like that so yeah i mean it'll it'll be interesting to see but for
[917.34 --> 926.22]  now we are we are safe um there is no risk of uh of go being sold to squarespace as far as we know i
[926.22 --> 934.38]  mean we're we're three you know peeps on a podcast just making wild guesses you know as to what a
[934.38 --> 940.82]  mega corporation might or might not do i mean they're laying off entire language teams and entire
[940.82 --> 945.38]  frameworks like can you imagine if you're like what is it like flutter they laid off or something
[945.38 --> 951.92]  or dart or whatever it is can you imagine if you've invested like years into into these frameworks and
[951.92 --> 959.18]  languages and all of a sudden on some corporate execs whim like well now we we need to now divert these
[959.18 --> 966.66]  funds into ai now no more of these no more of these side things these are not core to our mission
[966.66 --> 974.24]  these do not align with our objectives and all of a sudden just with that sentence your your livelihood
[974.24 --> 981.84]  is now at risk can you fathom it i mean yes but not put all your eggs in one basket folks
[981.84 --> 989.34]  do not put your eggs all of them in one basket never never ever yeah i mean it'll be interesting
[989.34 --> 994.74]  especially with all this ai development and whatnot to see where everything goes well speaking of
[994.74 --> 999.86]  corporate benefactors that might come to go's rescue there's a story about microsoft on there on here
[999.86 --> 1006.54]  isn't there yes very good segue johnny so we have a nice little blog post from microsoft about the fact
[1006.54 --> 1013.10]  that they have started a go blog although they've kind of snuck in here as well that they basically
[1013.10 --> 1018.88]  have their own fork of go they use internally and that they're contributing things upstream which is
[1018.88 --> 1024.30]  super interesting i think it's not it's not common but it's not uh necessarily uncommon for companies to
[1024.30 --> 1029.90]  have their own internal forks of things that they use to do little tweaks and whatnot um but i think the
[1029.90 --> 1036.08]  whole like we're gonna upstream as much of the changes as we can is a very interesting philosophy for them to
[1036.08 --> 1042.52]  have yeah what are your guys thoughts well i mean first it's not just a internal fork now i mean it's
[1042.52 --> 1047.68]  public it's you can use it if you want does it do go routines differently does it like shell out to
[1047.68 --> 1053.88]  c sharp or something no if you if you actually go through and read what it is i mean it's basically
[1053.88 --> 1059.50]  just crypto changes to comply with like government standards right uh so like phips the phips standard
[1059.50 --> 1064.96]  and stuff i have no idea what phips is but phips 140-2 why you're not you're not familiar with
[1064.96 --> 1074.56]  phips 140-2 i'm not no nobody is man unless unless unless unless this is your like your your bread
[1074.56 --> 1078.80]  and butter your daily work i don't think anybody like even pays attention to these things unless
[1078.80 --> 1084.22]  they have to i think it's like government contracts yeah it's the federal information processing standards
[1084.22 --> 1088.34]  yeah yeah i guess if you're if you're an engineer working with the government these things are going
[1088.34 --> 1093.92]  to be very familiar to you yeah it's for uh the non-military government agencies and contractors
[1093.92 --> 1100.62]  so i assume government agencies and military contractors do something different uh well
[1100.62 --> 1105.98]  yeah military yeah the military agencies and military contractors undisclosed something probably a bit more
[1105.98 --> 1110.76]  advanced more secure i don't know yeah more more kept close to the vest you know you don't want to
[1110.76 --> 1116.54]  reveal that information to to the enemy yeah yeah yeah yeah so let's get back to the news
[1116.54 --> 1123.32]  but yeah so i think i think this is interesting of of microsoft taking an even stronger stance of
[1123.32 --> 1127.66]  investing in in go i feel like that's part of their whole like trajectory of trying to
[1127.66 --> 1132.60]  become a big open source company again like when they bought github and all this other stuff
[1132.60 --> 1137.16]  so yeah and i think wasn't didn't github have a lot of investment in go too so i think they probably
[1137.16 --> 1142.36]  got a ton of go investment from that yeah i mean i think this is interesting like more more versions
[1142.36 --> 1148.40]  of go also sounds nice right you know we got the two big ones i guess and is that an unpopular opinion
[1148.40 --> 1154.66]  did we already jump to that bit more versions of go sorry not versions more implementations of go
[1154.66 --> 1159.08]  why do you want more implementations of go oh no the like you don't like the one you have
[1159.08 --> 1166.98]  i i like the one that we have but we we already have what three two at least well
[1166.98 --> 1171.46]  i guess three depending on how you count right we have the gc compiler which is the main go compiler
[1171.46 --> 1178.94]  you have gcc go you have tiny go you know and there's like a few others like i isn't uh is there
[1178.94 --> 1185.10]  one that works with the gnu compiler system gcc go and there's ll go that's the other one i was
[1185.10 --> 1189.66]  thinking of yeah there's just there's a lot of different versions not versions a lot of different
[1189.66 --> 1194.60]  implementations of go which is how they the designers meant it to be so adding another one in there
[1194.60 --> 1201.00]  seems like a fine thing to do okay all right i mean i'll give it a pass disagree johnny if you
[1201.00 --> 1208.90]  want to disagree no no no no i'll allow it i'd like to know who is using these other implementations
[1208.90 --> 1214.86]  i know like it depending on what architecture you're targeting some people use like either gcc go
[1214.86 --> 1221.06]  or like the llvm go like ll go if it's like if there's a back end for those compilers that the
[1221.06 --> 1227.22]  standard go compiler doesn't have like for a while i think there wasn't support for like the z
[1227.22 --> 1233.06]  architecture ibm's like mainframe architecture like it wasn't officially supported within the
[1233.06 --> 1238.88]  go compiler but it was supported within uh llvm's back end so people were using ll go for that
[1238.88 --> 1245.14]  or if you want like just compatibility with other languages in a nicer way you can use the you know
[1245.14 --> 1249.96]  those alternative compilers and then obviously for things like tiny go it's like well if you want
[1249.96 --> 1255.84]  to run go on a microprocessor you want something that is uh not going to give you like a 80 megabyte
[1255.84 --> 1263.84]  binary yeah so what do we think this means for go um and they're like announcement post they say
[1263.84 --> 1267.98]  they're going to be posting about running go workloads on azure i think we're going to see more
[1267.98 --> 1273.66]  compatibility there i don't use azure so i don't even know how it works with go but i know aws has
[1273.66 --> 1279.56]  some nice build-in like you run go on lambda right right yeah i assume that some of their like more
[1279.56 --> 1284.74]  their products are going to support go natively i imagine they already have quite a bit of go in
[1284.74 --> 1288.26]  i mean like because we like anything that has like kubernetes integration like if you're doing all of
[1288.26 --> 1291.48]  that work you're probably doing a lot of that work in goes you probably already have like
[1291.48 --> 1299.32]  substantial go expertise within your cloud infrastructure teams i just like so many cncf
[1299.32 --> 1303.80]  things are written i mean so many cloud things are written in go that i don't think you can have a
[1303.80 --> 1310.12]  cloud company that doesn't at least have a pretty strong familiarity with go if you do anything in
[1310.12 --> 1315.06]  the cloud you you're whether or not you interact with it directly you probably have go somewhere
[1315.06 --> 1321.48]  in your stack so um that's um i think that's fairly certain at this point yeah i mean all the all three
[1321.48 --> 1325.74]  because all three of the big cloud providers all have kubernetes systems like you know product
[1325.74 --> 1331.72]  offerings so that right there is right so yeah i mean it's it's exciting to see other companies doing
[1331.72 --> 1334.80]  investment also i think that helps you know kind of with what we were talking about before where
[1334.80 --> 1340.22]  there's just less of a risk of like one company being able to do something that might deal a critical
[1340.22 --> 1346.00]  blow to go because now there's like oh okay well you know if microsoft does you know and if over the
[1346.00 --> 1350.36]  course of the next few years really establish themselves as a big contributor to go then if there
[1350.36 --> 1354.88]  ever is a risk of google saying we don't want to do this anymore there's an obvious successors an
[1354.88 --> 1359.08]  obvious like obvious company to pick the language up and keep going with it so
[1359.08 --> 1365.02]  yeah yeah i i think this is a good thing overall you know i think i was joking earlier that all of a
[1365.02 --> 1370.06]  sudden having a job at microsoft and the go engineering group all of a sudden doesn't seem
[1370.06 --> 1372.34]  like a bad a bad thought
[1372.34 --> 1377.44]  they need somebody to evangelize this stuff internally right
[1377.44 --> 1385.50]  i mean it's uh it's not it's not the it's not the microsoft of the old times of you know when
[1385.50 --> 1391.76]  johnny first started programming in the ancient time you know and it's it's a different it's a
[1391.76 --> 1397.18]  different world my friend i mean you know it's a different world it's not when i used to install
[1397.18 --> 1403.66]  you know windows with diskettes um on machines those windows floppy days it's not those times
[1403.66 --> 1410.06]  those to those floppies you were no longer right how long ago was that don't ask don't ask
[1410.06 --> 1418.48]  please i can't imagine windows on a floppy is it like 30 of them it was it was a decent number
[1418.48 --> 1424.68]  yeah yeah just about just about it was annoying to install here is windows four megabytes at a time
[1424.68 --> 1434.00]  yeah now install disk 17 you just hit the little button pop up the 16th one is that what a floppy was
[1434.00 --> 1439.32]  4.3 megabytes is that right oh they're varied in sizes over time it depends on whether it depends on
[1439.32 --> 1443.82]  when you entered into the into this game you know i mean you could have entered at the five and a
[1443.82 --> 1447.32]  five and a half was that five and a half or five and a quarter yeah three and a half and then uh and
[1447.32 --> 1453.24]  then and then we we sized it down to you know the three and a half inch or something but in between
[1453.24 --> 1457.58]  there you know like we we went through all kinds of you know various kinds of mediums and you know
[1457.58 --> 1463.58]  zip drives and this is in that i mean we it's been i mean the kids these days they have no idea how
[1463.58 --> 1471.72]  good to have it a zip drive was legit a tape right uh no it was a zip was still a like magnetic platter
[1471.72 --> 1479.06]  oh was it yeah it was just yeah yeah fancy one because i i grew up in the era of you know zip
[1479.06 --> 1484.70]  drives and floppy like when i was in high school we had to save all of our word documents onto floppy
[1484.70 --> 1491.98]  disks for you know classes or whatever it was oh god i don't remember i don't remember that era of life
[1491.98 --> 1496.72]  and then thumb drives came along and that just changed everything that did change everything i
[1496.72 --> 1503.12]  remember when when what a five meg thumb drive was like it was like yeah it was something ridiculous
[1503.12 --> 1509.28]  ridiculous but at the time it was like wow five megabytes you know how much you can store in that
[1509.28 --> 1517.28]  that's like 12 you know wolfensteins or something you know it was it was crazy now it's like uh wow five
[1517.28 --> 1524.40]  megabytes that's like a a tenth of a of an image coming out of a camera that's but yes back to
[1524.40 --> 1531.26]  microsoft being a redeemed entity those tangents you know those fun entertaining tangents
[1531.26 --> 1539.54]  this is not news from the from the early night late 90s of microsoft but yeah no it's it's nice seeing
[1539.54 --> 1545.02]  that they're they because you know a few years ago when microsoft was like yes we're going to try and
[1545.02 --> 1550.26]  become a better open source contributor we're gonna we're gonna you know basically atone for
[1550.26 --> 1556.72]  our sins from the past i think everybody was kind of like oh we're not we're not really sure and uh
[1556.72 --> 1562.74]  then there was you know the problems and issues of like when they when they bought github and
[1562.74 --> 1568.08]  everybody was like oh is github gonna look a little look a little weird are we gonna have clippy on github
[1568.08 --> 1572.74]  and i think they did a pretty good job with that so seeing them kind of continue all of that is uh
[1572.74 --> 1576.88]  it's a really nice thing yeah it does feel like just a continued path for them i mean they
[1576.88 --> 1585.86]  did dot net core they did the github acquisition they had linux subsystem for windows so excited to
[1585.86 --> 1590.78]  see them get on the go train now yeah that part that part's nice is like oh yeah you're seeing this
[1590.78 --> 1596.50]  gradual progression of what they're doing and how they're doing it it's like okay nice nice you're
[1596.50 --> 1601.58]  not you're not you weren't like pulling the rug out from under us yeah i think github got better
[1601.58 --> 1608.60]  after microsoft too like unlimited free repos free private repos i i enjoyed that yeah cheaper for
[1608.60 --> 1612.58]  sure i remember it was like four dollars a month for all of this stuff that's great
[1612.58 --> 1630.68]  what's up go time adam here in the breaks talking to stegar bachu co-founder and ceo
[1630.68 --> 1637.70]  of speakeasy speakeasy is the complete platform for great api developer experience generate sdks
[1637.70 --> 1646.06]  in typescript python go java c sharp and php you know what cigar imagine i have some listeners who
[1646.06 --> 1651.20]  write go because you know they're listening to go time and they say i maintain our sdk and i don't
[1651.20 --> 1658.14]  mind doing it but i realize there are ways to generate our sdks using the open api specification
[1658.14 --> 1666.36]  now give me an exact workflow end to end from curious to leveraging speakeasy to generate and
[1666.36 --> 1672.00]  maintain sdks for an api written in go let's take the case of you're building an api from scratch
[1672.00 --> 1676.28]  today if you're building an api in go you're probably going to start with one of the common
[1676.28 --> 1682.32]  frameworks to build a go api i would highly encourage looking at frameworks like goa and
[1682.32 --> 1687.98]  humor which actually give you a lot of scaffolding out of the box to not just write your api but also
[1687.98 --> 1693.54]  to make sure that you get an open api spec generated off of each build of your api that is like a really
[1693.54 --> 1698.22]  great foundational building block to invest in as a company because that means all future development
[1698.22 --> 1703.82]  of the api is guaranteed to be described and documented out of the box once you do that it's
[1703.82 --> 1708.50]  i think a good idea to have some basic concepts of ownership built in so if you have multiple services
[1708.50 --> 1714.08]  or microservices make sure your sense is annotated by teams that own it and then also give your
[1714.08 --> 1719.96]  resources simple names that get reflected in open api spec once you do that the spec is going to get
[1719.96 --> 1725.42]  created every time you build your api so through cicd your spec will get generated every time you build
[1725.42 --> 1730.30]  and host the api make sure that spec gets pushed to a change management solution i think that's where
[1730.30 --> 1734.42]  speakeasy can come in they actually push the spec to us in every build and we'll create a version
[1734.42 --> 1739.34]  snapshot of it so you have it for we give you prominence of it so you have it for future builds
[1739.34 --> 1744.54]  and future work that you want to do on it once that happens you can attempt to generate an sdk
[1744.54 --> 1750.52]  and we'll hook diacline to your cicd and grab the latest version of the spec every time that happens
[1750.52 --> 1755.34]  we'll compare the spec to a previous version tell you if there's any breaking changes and send you a
[1755.34 --> 1760.92]  pull request on any repo to generate that new code once you get to that first version of the sdk
[1760.92 --> 1765.08]  that's where you really want to do some human in the loop investment and take a look at does the
[1765.08 --> 1770.20]  sdk suit your needs is it ergonomic and the way you think it should be and then also make is it
[1770.20 --> 1775.70]  documented is it described well if there are gaps in that documentation you know you can go back and
[1775.70 --> 1781.62]  add that in your code base but if if this is not a new api and this is a legacy api you can use tools
[1781.62 --> 1787.82]  like overlays to actually add in that documentation without altering the original spec itself or altering
[1787.82 --> 1792.66]  the source code so you do some investment there to make sure that the sdk output is ergonomic well
[1792.66 --> 1798.26]  to the scrap and documented and once that happens you kind of set us on all autopilot so every time
[1798.26 --> 1803.54]  your spec changes speak as you will send you your pull requests and once you merge a pull request gets
[1803.54 --> 1808.32]  published and released on github thank god go doesn't have a you know separate package manager it's
[1808.32 --> 1813.74]  all github so the moment the git repo is updated you get a brand new sdk version released to your
[1813.74 --> 1819.12]  customers that's the complete workflow all the way from your api server to your cicd to actually
[1819.12 --> 1824.46]  having generated and hosted sdk so take me in as close as you can give me an ant's eyes view
[1824.46 --> 1830.48]  why is this beneficial for a team i think it's really beneficial when you start thinking about
[1830.48 --> 1835.98]  growth and scaling the company the moment you have more than one developer touching an api let's say
[1835.98 --> 1841.10]  you have two and three developers touching and iterating on an api you want all those changes to be
[1841.10 --> 1846.94]  captured and documented somewhere so that someone else not necessarily the same developer can decide
[1846.94 --> 1853.42]  whether that api is distributed uh to outside the company doing that upfront investment means every
[1853.42 --> 1859.34]  api change is described documented and every n plus one developer that comes on the team is also going
[1859.34 --> 1863.50]  to onboard that much faster right because every everything like you don't you're not going to need
[1863.50 --> 1868.22]  to know about how every service is constructed you're just going to be able to look at the open api spec
[1868.22 --> 1874.44]  and say we have three apis today two of them are generally available ones in beta and then you
[1874.44 --> 1880.58]  know ones of b1 and ones of b2 right that's like you at the at the most granular level like that
[1880.58 --> 1885.62]  upfront documentation means you're going to be able to move a lot faster on other development going
[1885.62 --> 1891.30]  forward so i would say like that's the that's if i had to say one huge benefit of that is doing
[1891.30 --> 1896.44]  that for investment means every developer building an api going forward is not going to have to like
[1896.44 --> 1901.44]  learn all the context of every api it's just going to be there described in a simple single document
[1901.44 --> 1911.76]  okay go to speakeasyapi.dev you get your first sdk generator for free once again speakeasyapi.dev
[1911.76 --> 1913.44]  and tell him go time sent you
[1913.44 --> 1937.74]  what's next what's next we are going to i think we want to talk about oh yes this nice post from
[1937.74 --> 1946.18]  the go blog about uh evolving the standard library with a v the first v2 package in the form of math
[1946.18 --> 1951.56]  rand getting a new version this this one feels like it's a long time coming i've always had my own
[1951.56 --> 1957.82]  dislikes of how math rand has worked and especially i i get why they made it different from crypto rand
[1957.82 --> 1962.38]  so you couldn't like accidentally use math rand or you'd want to use crypto rand but it was still
[1962.38 --> 1969.32]  very annoying to have to use like a completely different you know api if you wanted to have a
[1969.32 --> 1974.14]  pseudo random number generator instead of a you know cryptographically random one but yeah i think
[1974.14 --> 1978.74]  this is like a good an interesting next step when it comes to all of the changes that we've been making
[1978.74 --> 1986.18]  that have been made over the years when it comes to like really realizing that go to vision even though
[1986.18 --> 1992.74]  go to isn't a thing it is just a set of features being added to go to allow it to advance it's really
[1992.74 --> 1998.42]  it's nice to see that we're kind of coming to the the the full view of that and seeing like the standard
[1998.42 --> 2004.48]  library being to incorporate newer things in these types of changes without breaking backward compatibility
[2004.48 --> 2012.66]  it's the first uh v2 in the standard library it's yeah we went we went from after all these years
[2012.66 --> 2019.68]  we went from theoretical to practical in the standard library itself with regards to go module package
[2019.68 --> 2024.96]  versioning so what are your what are your thoughts ian got any thoughts i don't know i think the article
[2024.96 --> 2030.12]  uh makes some really interesting points kind of about the drift between the version one and version two
[2030.12 --> 2036.24]  which we don't want to happen right uh so it goes on to say like any v2 package will be completely
[2036.24 --> 2041.20]  be able to completely do what a v1 package does at the time of release so it's not going to be
[2041.20 --> 2046.72]  like a v2 package that we get part of another package which i think is good and it also goes on to say
[2046.72 --> 2054.22]  that the plan is to kind of make the v1 packages just a thin wrapper over v2 packages uh so v1 packages
[2054.22 --> 2061.36]  can i don't know get bug updates and fixes from changes in the v2 packages which i think is great
[2061.36 --> 2066.76]  i hope that works out oh change the v1 package to be wrapped around the okay yeah yeah so i mean i think
[2066.76 --> 2072.02]  that's that's smart and i hope it works it doesn't seem like it's going to work for everything but it
[2072.02 --> 2078.62]  worked for well what did it work for i'm trying to think of a a package where that actually no i'm
[2078.62 --> 2084.06]  thinking of something else i'm thinking of uh when uh context was formally introduced basically went
[2084.06 --> 2089.92]  from experimental to being part of standard library in initially back in the day used to make uh used
[2089.92 --> 2097.40]  to use http package to do new requests right http that new request when the context package was formalized
[2097.40 --> 2104.70]  new with requests was introduced but the existing new request was simply changed to under the hood
[2104.70 --> 2110.28]  create a context for you that way every request would have a context by default right so things
[2110.28 --> 2114.16]  like that where changes are introduced to the language and under the hood you have to go change
[2114.16 --> 2119.62]  your code i think there's a great ways to do that but like you said ian there there are some there are
[2119.62 --> 2126.46]  some apis that that are going to be so different that you can't really maybe you know some values you
[2126.46 --> 2132.58]  know get added you need to now invoke you know with with more arguments some things have changed maybe
[2132.58 --> 2136.40]  some value a particular data type is no longer required or is not required i mean there's going
[2136.40 --> 2141.34]  to be some situations where it just can't work and i think you are going to see basically what
[2141.34 --> 2146.68]  happened with you know the math ran package here you're going to see a v2 sort of uh being introduced
[2146.68 --> 2152.28]  um for that new capability and thankfully i mean i do like this approach fundamentally right i mean this
[2152.28 --> 2157.92]  is doing exactly what the go compatibility promise sort of you know promised basically not breaking any
[2157.92 --> 2163.08]  existing code out there when the api changes or when there's something fundamentally different about
[2163.08 --> 2168.92]  how some particular behavior works we rely on a v2 and i think it's not going to be just the job of
[2168.92 --> 2172.98]  the standard library to do that right things like linters are gonna you know gonna have an impact on
[2172.98 --> 2178.38]  this right right now even right now like basically i try to get a random number generator initialized
[2178.38 --> 2183.00]  um you know earlier this week and then i'm not sure which one of my linters i have like a dozen at
[2183.00 --> 2187.58]  this point i'm not sure which one you know caught it but it told me that hey you no longer need to do
[2187.58 --> 2192.48]  the whole dance with the you know seeding of the time that you don't know you need to do that just
[2192.48 --> 2196.94]  use the math ran you know package you know as you normally would right so it was it was nice i was
[2196.94 --> 2201.84]  like oh yeah that's right this was introduced back in march i'm so used to doing this particular
[2201.84 --> 2205.38]  way i didn't even realize i was doing it the old way right i didn't even realize i could do it
[2205.38 --> 2209.78]  you know the new and better way right so my linter my editor my development environment sort of
[2209.78 --> 2214.76]  helped me move along right and catch up with the future kind of thing uh with current state right
[2214.76 --> 2219.62]  so i think it's going to be the job of the entire ecosystem to move everybody towards a new thing
[2219.62 --> 2223.60]  when there's a new thing yeah i think that that brings up one of the great strengths of like the
[2223.60 --> 2230.38]  semantic import versioning that v1 and v2 can just exist in the same code base and you can gradually move
[2230.38 --> 2238.06]  so like you said you can use that v2 now right um without changing everything yeah i also think with the
[2238.06 --> 2243.94]  the fact they added the functionality that in the in the go.mod file there's like the version of go
[2243.94 --> 2249.36]  you're compiling with which i think allows them to fix a lot of things that might have been attempted
[2249.36 --> 2255.08]  to be fixed with like a v2 package in the past or like a v2 of the language in the past like i think
[2255.08 --> 2259.76]  the shadowing stuff that they just got rid of i think is one of those things where it's like oh well
[2259.76 --> 2266.10]  it would have been very difficult to fix this before but now that you can be like oh okay you're you're
[2266.10 --> 2270.20]  compiling for this older version of the language so we're going to keep those semantics the same or
[2270.20 --> 2275.84]  oh you're in this newer version of language now the semantics are different or like the ability to say
[2275.84 --> 2283.84]  just uh was use a number in a range which i've wanted forever like just being able to do that
[2283.84 --> 2287.86]  kind of stuff and be able to like detect based on like oh yeah like you're you're on this version
[2287.86 --> 2292.74]  of the compiler so we know that we can we have these features we have this functionality i think helps
[2292.74 --> 2297.78]  make sure that we don't rush to to v2 packages when we we don't need them and that we actually
[2297.78 --> 2303.98]  go to the v2 when we actually have a pressing need to to do something at a higher level that's
[2303.98 --> 2307.12]  different like something semantically different instead of just some like i don't like this
[2307.12 --> 2311.96]  syntax or i don't like this particular thing you all excited for any v2 packages i don't think
[2311.96 --> 2317.28]  anybody's excited about any v2 packages it's just you know the that's the system we've got yeah i mean
[2317.28 --> 2323.60]  i don't like semantic import version love the one you're with semantic import versioning is still
[2323.60 --> 2330.20]  kind of garbage but i mean like if it's what we got it's what we got i like it now like i mean i i
[2330.20 --> 2337.06]  haven't used many because i think so many people just pinned at like version zero or version one to
[2337.06 --> 2342.60]  avoid the problem but like when there were modules that had like you know we're on version five and
[2342.60 --> 2347.78]  they had a whole bunch of packages like trying to get the right package to get imported using go
[2347.78 --> 2352.02]  imports was a pain for a long time i don't know if that's been fixed but that was definitely like my
[2352.02 --> 2356.46]  biggest headache was just like writing code became much more annoying with semantic import versioning
[2356.46 --> 2362.56]  because it applied to individual packages and not to like the module as a whole which i think is a
[2362.56 --> 2366.18]  fine way to do it but i just think it's there's there's still all those problems but i think it it
[2366.18 --> 2370.58]  probably works pretty fine for the standard library library because there's not going to be
[2370.58 --> 2378.90]  as many like i it's going to be a long time before we have like a v5 of a package um and i think
[2378.90 --> 2384.00]  there's going to be a lot of very careful things that are done to make sure that like when you import
[2384.00 --> 2389.46]  something you get like the correct version of it i'd be surprised if we ever got to a v3
[2389.46 --> 2395.46]  because they're not v2ing packages unless you live you live long enough ian you live long enough
[2395.46 --> 2403.74]  and funny things happen like we no longer have zip drives right like so don't dismiss it it's it's
[2403.74 --> 2409.10]  fine just give it time stick around all right let's uh put a bet on it and i'll talk to you in 10 years
[2409.10 --> 2415.02]  and we'll see who was right we'll have we'll have an inaugural we'll have no no no what do you call
[2415.02 --> 2420.64]  them uh the one one thousandth episode or something and then we'll be invited back as old timers
[2420.64 --> 2428.66]  back and back in my day uh we had v2 that was the most you could expect yeah i mean i think it's
[2428.66 --> 2433.72]  interesting because the only the other reason you really need a v2 is if you want to reuse
[2433.72 --> 2439.36]  a name because otherwise you just make a new package with a new name right if it's like oh this is the
[2439.36 --> 2443.18]  more advanced it's like okay here's a new name kind of what they did with like the fs package where
[2443.18 --> 2446.98]  they were just like okay well we're just gonna make a new package and a new name for this new thing
[2446.98 --> 2453.20]  it's not like the os v2 package or something like that or you can do it like some projects did
[2453.20 --> 2459.70]  they pretty much said listen just assume that when you download when you do a go get the next time
[2459.70 --> 2463.18]  even though the package path is going to be the same you're getting a v2
[2463.18 --> 2474.20]  if you want the v1 of anything you better pin to a commit hash bro oh god the bad old days
[2474.20 --> 2480.90]  i did just add a package to something i was working on and i think it was like version 44
[2480.90 --> 2489.40]  and i was so confused i wish i could remember what it was i mean i guess like some people just like
[2489.40 --> 2492.34]  we're like oh semantic import versioning we're just gonna go hog wild like we're just gonna
[2492.34 --> 2498.66]  ever release new version i think it's like it it is a it's a interesting challenge of our industry
[2498.66 --> 2503.22]  that i think like you know i have my gripes with how like semantic import versioning and how a bunch of
[2503.22 --> 2509.52]  this stuff works this does feel like one of the better ways this has been done in the industry
[2509.52 --> 2516.66]  right like we've basically successfully managed to move go into like go to right like this is go
[2516.66 --> 2523.34]  version two without actually having any breaking changes which i think is is kind of incredible
[2523.34 --> 2527.92]  because we didn't have to run into like the thing that happened with python or happened with like so many
[2527.92 --> 2533.94]  other languages where it's just like oh god we have these few years of awfulness because we had
[2533.94 --> 2538.96]  to like make we had to make all of these changes at once and now everybody's mad at us and everybody's
[2538.96 --> 2543.16]  stuck on the old thing for an extra decade and we don't know what to do but with go it's just kind
[2543.16 --> 2548.14]  of like nah it's like you're stuck on the old thing for not that long because you can you can just
[2548.14 --> 2553.06]  move forward and i think that's also you know partly because of ghost history you know with like the go
[2553.06 --> 2556.82]  fix tool and a whole bunch of other stuff that's like okay well we'll just like rewrite your code
[2556.82 --> 2562.70]  for you to help you upgrade some of this if we can i think thank goodness we didn't take a page
[2562.70 --> 2567.88]  from the javascript community and just start creating polyfills everywhere and transpilers and
[2567.88 --> 2575.32]  this and that and yeah the javascript community is a uh be nice be nice be nice it's an interesting
[2575.32 --> 2580.10]  approach they've taken which is it feels like they don't have a lot in their standard library so they
[2580.10 --> 2586.06]  have like a crap load of packages and then their packages all depend on other packages but it seems
[2586.06 --> 2591.74]  to work right it's not like they're all like javascript hasn't had enough hasn't had like the
[2591.74 --> 2597.20]  same kind of breaking change problem that python had for example and they've advanced that language
[2597.20 --> 2603.04]  considerably over time so i think that's it's another approach to solve the same sort of problem
[2603.04 --> 2608.30]  but like i think the approach that go took only works if you have some centralized control of the
[2608.30 --> 2613.08]  language right if you have like the go team that is making all of these decisions i think if you have
[2613.08 --> 2619.30]  a much more representative democracy style way of doing things that's going to be a lot harder to do
[2619.30 --> 2623.50]  to actually like make sure that you know you're you're charting the right path at the end of the day
[2623.50 --> 2629.32]  so i think what javascript did is probably what would have been possible with the type of with the type
[2629.32 --> 2636.36]  of community that they are um and it works so and to be fair you know it's it's you have people who
[2636.36 --> 2641.14]  mean well right that want to advance you know the language and the community forward but you have a
[2641.14 --> 2646.40]  lot of incumbents who you know basically they have their money is made with the status quo and you
[2646.40 --> 2650.24]  know it's the same problem across any and everything right whenever you need to make a change to
[2650.24 --> 2654.04]  something change is disruptive all right whenever you make it if somebody has built entire business
[2654.04 --> 2660.30]  right you know brought be it browser makers or or plugin vendors and this and that if if people don't
[2660.30 --> 2665.64]  want change right because whenever you change these things and underlying technology that means
[2665.64 --> 2670.94]  now they have to you know put in more costs to also adapt and change their wares and you know that
[2670.94 --> 2676.20]  means they they're making less money so you know the the tyranny of shareholders you know what i mean
[2676.20 --> 2680.72]  you can't you can't keep you know increasing your costs and not be given you know money to shareholders
[2680.72 --> 2687.68]  so there's gonna be like this reminds me of an interesting lesson i had to learn in sort of the early
[2687.68 --> 2694.80]  days of my career where i figured out right that technical decisions were rarely purely technical
[2694.80 --> 2701.62]  decisions right you know i'd present i'd present really well well argued well structured you know
[2701.62 --> 2709.98]  reasoning logical um sort of uh proposals for you know changing from this framework to that framework
[2709.98 --> 2714.62]  this language to that language or this architectural style to that one and blah blah right you know with
[2714.62 --> 2719.78]  a clear path of migration you know not blow things up but she's incremental changes you know like a
[2719.78 --> 2724.80]  release schedule roadmap i'd do all this work right and then uh you know they'd be like oh yeah we'll
[2724.80 --> 2730.22]  take it from here and then the decision is made in some room somewhere where i'm not at the table and
[2730.22 --> 2735.78]  you know and i'm like i'm realizing like what you're going with this approach but this makes no sense
[2735.78 --> 2742.52]  like technically it is a poor bad decision you don't know what the heck you're doing like you know i was
[2742.52 --> 2746.10]  literally i would be getting mad about this stuff and then i realized one day like oh crap
[2746.10 --> 2752.44]  it's not about the technical decision all the time right there are other factors that i'm not
[2752.44 --> 2758.10]  privy to that go into these decisions right so yeah you know it's the same thing with you know and even
[2758.10 --> 2762.44]  in the open source community there's going to be incumbents who don't want things to change that much
[2762.44 --> 2768.48]  because they have a lot at stake right yeah and i think that's why like forking is a is a good thing
[2768.48 --> 2775.26]  like i remember back when my my last couple of i think maybe like last year or so of actively doing
[2775.26 --> 2779.14]  drupal development there was this you know big push for the new version of drupal it's gonna be drupal 8
[2779.14 --> 2783.04]  and it was gonna change everything and there were a whole bunch of people that are like
[2783.04 --> 2790.26]  we kind of like how drupal 7 worked and the historical way drupal works so uh we're just gonna go fork it
[2790.26 --> 2795.00]  and make this other thing and it seems like both things are thriving and so it's like okay well
[2795.00 --> 2800.62]  if you want the old thing then go over here use this backdrop thing if you want the new thing
[2800.62 --> 2805.36]  then you know go go use the new drupal stuff wait hang on a second i gotta go fork redis
[2805.36 --> 2814.14]  speaking of which don't we have a don't we have another redis clone or something
[2814.14 --> 2821.76]  on our list of news yes yes we do uh although of course we do any any last comments about you
[2821.76 --> 2828.90]  the math ran v2 package or you know the evolution of go this is this is just a thought i would love
[2828.90 --> 2837.60]  to see go written like that first year compared to now like has it changed that much go look go look
[2837.60 --> 2843.46]  at the commit history you mean like like someone writing go in like an http server written a how long
[2843.46 --> 2850.94]  how old does it go i don't know i mean zero oh from like 2009 2009 to now like it's definitely
[2850.94 --> 2857.24]  changed but not that much if you ask matt ryer he'll can probably tell you because he's been he's been
[2857.24 --> 2864.58]  writing you know how how i still write go after 20 years or something um you know 13 years he said yeah
[2864.58 --> 2868.36]  30 yeah 30 is that after 20 years johnny language isn't 20 years old
[2868.36 --> 2875.98]  i'm i'm i'm using recruiter math sorry after 32 years of writing go
[2875.98 --> 2884.86]  oh this is uh i still you know handle my routes or something right i matt will i feel like there'd
[2884.86 --> 2892.38]  probably be a bigger delta difference between the initial like open source version of go and the v1 of
[2892.38 --> 2898.52]  go like go 1.0 then it would be between go 1.0 and now like i feel like that change would probably
[2898.52 --> 2903.42]  be very subtle like okay we have context now we have like a few of these other things but like
[2903.42 --> 2909.92]  the change in those first few years is probably much more about like oh this doesn't this well i mean a
[2909.92 --> 2914.60]  probably doesn't even compile with a modern compiler whereas like something written with go 1.0
[2914.60 --> 2922.12]  should technically still compile so yeah but that would be interesting to do maybe that someone
[2922.12 --> 2930.36]  should go out there write a blog post about that on to more forks redis so uh we we have a little
[2930.36 --> 2937.92]  uh redis re-implemented and go with sqlite backing it you call it sqlite wait hang on hang on hang on
[2937.92 --> 2944.08]  i think we're about to have another debate here do you call it gif or gif well i go between sqlite
[2944.08 --> 2953.26]  and sqlite but if we're if we're going to be pick a side bro very pedantic it would be sqlite
[2953.26 --> 2960.24]  because the language is called sql and you call it sql like whenever you refer to sql i yes i call it
[2960.24 --> 2964.22]  sql the vast majority of times sometimes i'll call it sql most of the time i call it sql only thing worse
[2964.22 --> 2971.80]  than sql is when people call it squeal or i've heard people do that and it's squealite
[2971.80 --> 2978.18]  but no there's like history there of like it's called sql because there was another
[2978.18 --> 2982.66]  basically competing language that was trademarked called sql so they couldn't call it sql
[2982.66 --> 2990.32]  so they had to call it sql but everybody but those if you know you know right you just call it sql and
[2990.32 --> 2994.32]  call it that's like you know calling everything like calling tissues kleenex it's like okay yes
[2994.32 --> 3000.06]  it's it's technically a tissue like everybody knows that's good kleenex it's okay yeah yeah you
[3000.06 --> 3005.46]  know we had we've been having these debates for for time immemorial like you know just the same way
[3005.46 --> 3010.48]  we're like nah bro serverless doesn't mean no servers right like we we have these conversations
[3010.48 --> 3014.94]  all the time right but eventually you you just like you know what let me just stop fighting the
[3014.94 --> 3020.00]  marketing people and just go with it i mean the hard part is english isn't in a
[3020.00 --> 3023.58]  phonetic language like you can't look at a word and know how it's supposed to be pronounced so
[3023.58 --> 3028.36]  that that's that's half the battle well some hill some hills i'm not wanting to die on i don't
[3028.36 --> 3033.76]  have how do you pronounce it how do you pronounce the image format it's a gif or is it okay do you do
[3033.76 --> 3039.78]  you refer to the individual known as god do you refer to him as jod
[3039.78 --> 3046.74]  that's not how that's not how pronunciation word is johnny
[3046.74 --> 3051.82]  g can make a joke or a good sound
[3051.82 --> 3060.66]  yes yes you don't you don't call i have a friend named george i don't call him gorge although that's
[3060.66 --> 3064.20]  kind of funny i kind of like that one
[3064.20 --> 3071.42]  yeah it's i guess it's a difference between like do you see it as like gif as the word so you have a
[3071.42 --> 3077.46]  gi as like the which would be a gut or do you see it as a a gr word which would be like a gu
[3077.46 --> 3085.06]  like a j or gu i don't know it doesn't matter it truly does not matter it's like one of the dumbest
[3085.06 --> 3089.50]  debates of like you know what you know what is it not a dumb debate though tabs or spaces
[3089.50 --> 3094.24]  choose carefully tabs because we're writing go like what do you mean all right yeah yeah we're
[3094.24 --> 3095.00]  still we're still friends
[3095.00 --> 3100.72]  like you can't you literally can't use spaces like i don't know
[3100.72 --> 3105.40]  although you could configure your editor every time you hit the tab key it just has four spaces
[3105.40 --> 3108.04]  and then gofunk will just turn it back into tabs
[3108.04 --> 3116.32]  those people must hate gofunk oh man they're probably not doing go anyway i mean if you're a
[3116.32 --> 3121.06]  diehard spaces person then anyway we're supposed to be talking about redis um yeah we are
[3121.06 --> 3127.36]  that's so off track uh so i don't know what what are what are our thoughts about all of these these new
[3127.36 --> 3134.18]  forks and things of redis or this this one in particular of redka redka the good parts oh the
[3134.18 --> 3139.80]  good part it's already opinionated the good parts of redis with secret light as opposed to the bad parts
[3139.80 --> 3142.70]  you know you know all that comes from i remember that book javascript the good parts
[3142.70 --> 3150.12]  and ever since then people started coming up with the good parts it's like johnny the good parts
[3150.12 --> 3155.98]  like what what do you mean the hard way the hard way right right but i feel like the good parts also
[3155.98 --> 3161.00]  with javascript was contrasted with the javascript the definitive guide the definitive guide is like a
[3161.00 --> 3167.08]  thousand pages long and the good parts is like 150 you know like that right yeah exactly it's such a
[3167.08 --> 3171.34]  nice contrast you kind of have to be in the publishing business to kind of get the inside joke there
[3171.34 --> 3178.60]  yeah i would imagine in any case redka redka how do you feel about it i i'm interested in all these
[3178.60 --> 3185.38]  new things popping up using sqlite i know sqlite has always been well used right like it's popular
[3185.38 --> 3192.22]  but i feel like in the last year i hear about sqlite more and more and more it took off you know you know
[3192.22 --> 3199.58]  i will agree and you know for me personally you know what sort of started making it more even more
[3199.58 --> 3207.46]  relevant in my life uh is um oh ben johnson ben johnson exactly you know he created a um bolt
[3207.46 --> 3212.82]  which bolt db which i you know for a long time i use you know constantly yeah he's he's very
[3212.82 --> 3216.94]  knowledgeable in and databases and and writing you know database servers and everything else
[3216.94 --> 3223.68]  and he had this project i think i think it's called light stream where basically if your use case
[3223.68 --> 3229.24]  is right you can literally right put sqlite into production and actually have a reliable system
[3229.24 --> 3234.44]  that has you know continuous you know streaming backups and you don't lose your stuff right he
[3234.44 --> 3241.00]  kind of opened my eyes to the possibilities right of actually treating sqlite not just as a toy
[3241.00 --> 3246.04]  database or something i use locally when i'm developing or or you know something i use in in sort of a
[3246.04 --> 3251.42]  low power devices or you know or whatever it is but actually using it you know instead of you know
[3251.42 --> 3255.90]  relying on the sort of the go-tos the postgres the you know the my sequel and so on and so forth so
[3255.90 --> 3263.72]  i think i agree like sqlite is very capable for for certain use cases right the primary thing for me
[3263.72 --> 3268.56]  has always been sort of the lock issue with rights right that we can only have one writer at a time
[3268.56 --> 3273.42]  so that creates a problem in some cases you kind of have to be clever with how you get around that
[3273.42 --> 3278.64]  you know maybe you just have one writer within a ton of readers that you have to kind of approach
[3278.64 --> 3284.16]  your design architecture a little differently than than some extra thinking you have to do around
[3284.16 --> 3289.06]  you designing your software right when you're not using like a full-blown database like postgres or
[3289.06 --> 3294.02]  my sequel or something like that i suppose although like when you're using you know sqlite it's like
[3294.02 --> 3300.16]  you're you're or you're operating at like many orders of magnitude faster than like a postgres or
[3300.16 --> 3305.78]  my sequel because it's just like you don't have a network you're just kind of there talking straight
[3305.78 --> 3311.28]  today so it's a lot faster in general i think but i also think like the you do have to structure
[3311.28 --> 3314.70]  things differently but i think there's also like the macro structuring of your application differently
[3314.70 --> 3320.54]  if you want to put sqlite at the center of what you're doing i've seen articles where it's people
[3320.54 --> 3326.44]  literally using one sqlite database per user yeah things like that like you can you can totally like
[3326.44 --> 3330.28]  the moment you start thinking about the problem a little differently right it's like it's just a file
[3330.28 --> 3334.76]  on disk why not just give each user a file all right then when they log in they have their own
[3334.76 --> 3339.94]  database like it it's a little trippy like if you're used to just like the the good old style
[3339.94 --> 3345.58]  of well-trodden path of you know framework servers connecting to databases you know rds databases
[3345.58 --> 3350.02]  relational databases that that you need to have connection pools and this and that i mean it's
[3350.02 --> 3354.82]  completely it's very trippy but the more you think about it like why not why can't i give every user
[3354.82 --> 3360.18]  its own database yeah i mean and sqlite is also interesting because it's one of those like
[3360.18 --> 3366.98]  actually like very stable very solid file types basically like the library of congress has listed
[3366.98 --> 3371.86]  it as one of like their like acceptable file types for data that needs to last like centuries
[3371.86 --> 3377.28]  i think it's the only binary one so i think the other ones are like text and like or like csv and json
[3377.28 --> 3383.38]  but like sqlite is right there next to it and like that's like a full-fledged system you got right there
[3383.38 --> 3389.50]  and actually advocate a lot of sqlite used as like an application storage format which is i think why it's
[3389.50 --> 3393.88]  probably one of the most is the most popular and most used database in the world i think a lot of
[3393.88 --> 3399.62]  like the apple app ship with a built-in sqlite database right yeah and like every browser does
[3399.62 --> 3404.64]  as well like yeah i think everything everything ships with sqlite and if you if you look at something
[3404.64 --> 3408.86]  you're like oh i'm using this application where is it storing its data probably in an sqlite database
[3408.86 --> 3415.02]  it's probably there probably sqlite yeah i do think it's a good fit for redis as well because it's
[3415.02 --> 3421.64]  redis is already think single threaded right it's it's a queue right like of of requests um
[3421.64 --> 3428.34]  so that whole write lock doesn't seem as much of an issue yeah i mean it it does fit that kind of
[3428.34 --> 3432.92]  use case really well even if you want to do like a distributed redis sort of thing like i think there's
[3432.92 --> 3437.84]  a someone that has done it a couple times where they just like wrote they put like raft on top of
[3437.84 --> 3441.50]  redis i think it's called rqlite or something like that and kind of distribute you can do the same
[3441.50 --> 3447.62]  type of thing with with redis where you put like you know redis and then raft behind it on top of
[3447.62 --> 3452.50]  sqlite and you can basically do the same thing it is also nice that it comes shipped with its own uh
[3452.50 --> 3459.26]  go client so i don't think you even have to use the wire protocol if you're running on the same that
[3459.26 --> 3465.60]  is cool not not this thing has me interested in re-evaluating sqlite and some of my life choices
[3465.60 --> 3469.84]  drop this a star while we're talking about it yeah yeah yeah for sure it's like a month old so
[3469.84 --> 3477.60]  i mean don't don't go deploy anything critical in production with it last commit was like a month
[3477.60 --> 3485.46]  ago no the first commit was a month ago so careful out there people i i think that like i feel like
[3485.46 --> 3491.00]  like sqlite also is having kind of a resurgence in go specifically because there's like there was uh
[3491.00 --> 3494.64]  i don't remember his name but there's a guy that's been basically working on trying to make it so you
[3494.64 --> 3499.78]  have sqlite in pure go so you don't have to use cgo and i think that actually just went one point
[3499.78 --> 3504.42]  recently or got to like some very stable point so you can start using it more and it literally is
[3504.42 --> 3511.44]  a drop-in replacement for sqlite which means that if you want to use sqlite but in go you don't have
[3511.44 --> 3516.78]  to use cgo which i think is a huge advantage and really opens the opportunities i mean sqlite was
[3516.78 --> 3522.18]  pretty easy to embed into go in the first place because it's packaged and shipped as a single c file
[3522.18 --> 3528.32]  with no dependencies so it's as far as things that you integrate into go from c land it's pretty
[3528.32 --> 3534.12]  easy to do but just having it so you can like still do cross compiling and all of that easily is like a
[3534.12 --> 3540.82]  huge advantage we should do a we should do an episode on licensing because i'm still when i see
[3540.82 --> 3547.72]  like licenses like the only thing i know is mit good everything else suspect right if i say like
[3547.72 --> 3554.64]  bsd3 clause blah blah blah like like like now i need to go do research right to see if i can i can
[3554.64 --> 3560.28]  if i can go get this i mean bsd and mit are the two like yeah and do what you want bro those are
[3560.28 --> 3565.54]  basically the attitude of those licenses yeah i think we should do an episode on licenses we could
[3565.54 --> 3572.12]  probably get uh louis villa back because he's a lawyer we talked to him about other ip-based stuff
[3572.12 --> 3576.32]  being interesting to talk about licenses with him if he's on an episode you'll want to listen
[3576.32 --> 3582.02]  those are the best episodes we've ever made in my opinion and yeah i mean i think you said that in
[3582.02 --> 3587.68]  episode 300 so in the this is sparta episode that johnny likes so much even though it's a 20 year old
[3587.68 --> 3597.06]  this is sparta so so what else are we all newsed up or or i mean i think there's a couple other news
[3597.06 --> 3601.54]  things we can talk about if we'd like to talk about them or we could do a nice quick round of
[3601.54 --> 3611.92]  unpopular opinions let's do unpop i got places to be so with that on to unpopular opinions
[3611.92 --> 3635.98]  all right johnny do you have an unpopular opinion for gretis
[3635.98 --> 3643.50]  if you haven't already that seems to be like peak popular opinion sir um
[3643.50 --> 3652.14]  oh man i'm having too much fun of myself
[3652.14 --> 3661.50]  okay okay uh yeah yeah that was it that was okay a fork redis unpopular opinion okay
[3661.50 --> 3667.44]  ian if you haven't already yeah i don't think fork redis is an opinion you should fork redis
[3667.44 --> 3675.76]  that's an opinion oh i mean ian you fit in right well with us being that pedantic about things okay
[3675.76 --> 3683.38]  oh i actually do have an unpopular opinion oh okay go for it so i always thought the fancy office
[3683.38 --> 3689.54]  chairs were were silly you know like the herman millers and the expensive office chairs and i've been
[3689.54 --> 3695.34]  using a chair designed to be at a dining room table for like two and a half years that sounds
[3695.34 --> 3700.68]  awful for your back but continue and baby what is you doing you know my back kind of hurts maybe i
[3700.68 --> 3701.82]  should look at a new chair
[3701.82 --> 3713.16]  so i finally bought an office chair uh the herman miller embody um and it is life-changing everyone
[3713.16 --> 3720.34]  should do this right now uh my back doesn't hurt should have done this two and a half years ago
[3720.34 --> 3726.18]  so my opinion is that expensive chairs are not overrated
[3726.18 --> 3734.88]  oh that's like that's like when you go from notepad and you start coding in an actual editor
[3734.88 --> 3742.66]  for the longest time like what are those fools like with their fancy syntax highlighting
[3742.66 --> 3751.92]  and like and like air air notification like what is this fancy stuff like notepad just it works just
[3751.92 --> 3758.04]  fine it's like a thousand dollar desk chair i'd rather have to pay for back surgery instead like
[3758.04 --> 3769.08]  oh man i got it cheap though so no worries there oh ian yeah my man my man wow wow okay i thought i was
[3769.08 --> 3777.88]  just getting old turns out it was for 10 hours a day you've just been using a notepad of chairs for 10
[3777.88 --> 3787.44]  years the notepad of chairs i mean when you first jump into like an ie or like a good editor yeah it's
[3787.44 --> 3792.74]  like oh okay i mean at least upgrade to notepad plus plus like how you gonna be a notepad well no
[3792.74 --> 3798.10]  it's only available in windows right notepad plus plus i know that because i used it for for a couple
[3798.10 --> 3807.34]  of uh dare i say years it was it was the ish back then yeah because it supported yeah it was it was it
[3807.34 --> 3812.86]  was the ish because you know i could have different language syntax um files in there and things it was
[3812.86 --> 3819.22]  great i was like sublime text guy for a long time eventually we all i mean weren't we all this was
[3819.22 --> 3827.36]  like the the granddaddy right of of new new age editors right um i never used sublime but that's
[3827.36 --> 3831.92]  because i went from like awful eclipse-based idees into vim and then i was just like okay i'm gonna
[3831.92 --> 3837.88]  live here forever oh you went extremes you went you went from eclipse heavyweight to just yeah it was
[3837.88 --> 3843.44]  like one of the eclipse like spin-offs for php and then i was like this thing takes forever to start
[3843.44 --> 3848.06]  up so i'm using like not like bb edit but one of oh text wrangler i was like using text wrangler for
[3848.06 --> 3852.06]  some things and then i was like i just need to learn one of these better editors i'm in servers all the
[3852.06 --> 3857.16]  time so it was like do i pick vim do i pick emacs and looked at that firestorm and it was like okay
[3857.16 --> 3863.92]  they're probably the same and then i was like oh well vim is by default on all of the like every system so
[3863.92 --> 3870.38]  i'm just gonna learn them but can you close it listen but can you exit out of it
[3870.38 --> 3875.86]  the chris probably still has the same session he opened 20 years ago
[3875.86 --> 3882.14]  still can't figure out how to exit like how do i get out of here
[3882.14 --> 3887.78]  colon what colon q but i have a modified buffer what do i do
[3887.78 --> 3896.36]  oh man i do remember trying to do an interactive rebase for the very first time and literally just
[3896.36 --> 3902.40]  deleting that branch i mean that recoding recoding like when i get out of it oh gosh
[3902.40 --> 3908.64]  i mean i know it's a meme it's not that hard to get out of them like it's
[3908.64 --> 3910.78]  it is if you don't know you're in vim
[3910.78 --> 3912.40]  i mean true
[3912.40 --> 3918.40]  oh man
[3918.40 --> 3922.36]  oh yeah i can't win jokes today
[3922.36 --> 3928.38]  i mean i do i do got the i got the vim posters you know it's gotta
[3928.38 --> 3933.68]  gotta represent that's how you know that's how you know does it have the shortcut for exiting on
[3933.68 --> 3940.18]  there uh no on your poster for anybody that's listening it's colon q if you want to save an
[3940.18 --> 3946.80]  exit don't be a fool and use an extra keystroke by doing colon wq just do colon x it's more efficient
[3946.80 --> 3952.06]  i didn't know that i still use colon wq yeah colon x is the same thing wq does
[3952.06 --> 3957.48]  mm-hmm oh chris do you have an unpopular opinion
[3957.48 --> 3962.08]  vim is the best text editor in the world what did i say yeah no uh
[3962.08 --> 3969.50]  no uh let's see unpopular opinions do i have one i mean do i have one i want to say out loud
[3969.50 --> 3973.82]  is is the real question i i probably said this one before but speaking of editors
[3973.82 --> 3979.92]  i'm just like go learn vim or emacs like go learn a nice text like a terminal based editor
[3979.92 --> 3984.14]  and at least at least try it out for a while because i think like your productivity kind of
[3984.14 --> 3989.48]  it it's it soars in a way that i don't know it does if you use you know idees not that against
[3989.48 --> 3995.62]  i mean everybody lets a little point clicky but those terminal terminal listen those those are
[3995.62 --> 4001.58]  those i have to disagree with your list there emacs is is not just an editor it is a lifestyle
[4001.58 --> 4007.94]  i mean so you don't one does not just one does not just anything with emacs right like it's a
[4007.94 --> 4014.46]  it's a way of life okay so if you want to just try some editors you don't just try emacs okay it's it's a
[4014.46 --> 4020.62]  it's an investment you know like it's you have to you have to you know ease yourself in and learn
[4020.62 --> 4027.16]  learn the way preferably from a guru a master become a padawan find find a jedi master to help
[4027.16 --> 4033.38]  you out if you used to play the piano emacs is for you change your keyboard layout to dvorak and
[4033.38 --> 4039.96]  i mean is that how you say that dvorak i have no idea i have no idea uh but like you know emacs if
[4039.96 --> 4045.76]  you like lisp as well emacs is very good for lisp no one likes viml um thankfully neovim we have lua
[4045.76 --> 4051.70]  now and go you can write plugins for neovim and go which is really cool i've been experimenting with
[4051.70 --> 4056.46]  that lately but yeah no i i would say my unpopular opinion is like yeah learn a learn a terminal based
[4056.46 --> 4062.70]  editor it's not for everybody right like there's a lot of it's not like with you know intellij or like
[4062.70 --> 4067.06]  the kind of jetbrains idees where it's just like it open the thing and you're good to go right you
[4067.06 --> 4071.70]  have to have to do some configuration you have to build the thing that you you want to have
[4071.70 --> 4078.14]  but if you figure out how to do that it's a really nice experience i enjoy not having to take my hands
[4078.14 --> 4084.60]  off the keyboard to do most of the the writing that i want to do so just just try that's all i'm saying
[4084.60 --> 4089.50]  everybody should try it out it's not for you it's not for you we all like a little bit of a
[4089.50 --> 4095.88]  exploration of ourselves on a little journey or as johnny said a lifetime saga of figuring out how emacs
[4095.88 --> 4100.74]  works and i mean you're not wrong right like org mode for emacs like some of my friends are keep
[4100.74 --> 4104.38]  telling me like you should you should use org mode it's a good way to organize your life like it's
[4104.38 --> 4111.00]  i get it i get it people people really love people love emacs people live in emacs they'll
[4111.00 --> 4115.28]  they'll run their entire lives off emacs i mean almost literally
[4115.28 --> 4121.44]  they'll put all their tasks their calendar their to-do list i'm sure there's a way to like check your
[4121.44 --> 4126.00]  email and they do everything in there so it's a way of life like i said it's a way of life yeah
[4126.00 --> 4133.10]  yeah and you know maybe that way of life is for you try it out nah i prefer calendars i'm good i mean
[4133.10 --> 4136.76]  i hate that's a whole lot of rant i don't want to yeah let's not start that
[4136.76 --> 4142.66]  let's have a bonus episode of how much does chris hate calendars it's like
[4142.66 --> 4149.30]  anyway that sounds like a good place for us to end chris just chose up randomly for appointments
[4149.30 --> 4156.40]  on different days and times that's how much he hates calendars i i yeah you calendars begrudgingly
[4156.40 --> 4159.46]  it's just such a bad you're gonna get me started like you can't
[4160.92 --> 4166.94]  abort abort unless we want to make a plus plus segment of this where we talk about calendars
[4166.94 --> 4169.16]  abort or we can't just be done
[4169.16 --> 4176.92]  mayday mayday see johnny coming in two weeks don't troll me too much because you don't know
[4176.92 --> 4179.90]  what's gonna happen i might have a half hour rant and calendars
[4179.90 --> 4188.12]  all right well this was a fun episode talking about some news and all that fun stuff but yes
[4188.12 --> 4193.56]  with yeah we should do it more often yeah maybe listeners if you enjoy us talking about news
[4193.56 --> 4197.48]  although this was also kind of like meta news plus news but of course you know johnny may
[4197.48 --> 4201.52]  end the episode so of course it's gonna get meta so but if you like this episode on news you want
[4201.52 --> 4206.30]  to you know have us do some more news coverage uh let us know you know reach out to us on the
[4206.30 --> 4210.78]  various platforms and go for slack and change log slack if you're not in change log slack you should get
[4210.78 --> 4216.42]  in there um and yeah let us know if you if you enjoy this and we'll we'll set some more up but with
[4216.42 --> 4222.68]  that thank you for joining me johnny it was wonderful having you and ian yeah no you forgot about i was
[4222.68 --> 4228.58]  i was going to say i was gonna wait for you to say chris i thought we were friends thank you for
[4228.58 --> 4234.42]  being here and then i was gonna say thank you for being here ian i was doing the outro in the reverse
[4234.42 --> 4248.66]  order i did the intro what the heck i was not oh my lord oh man next i'm gonna put you last that's
[4248.66 --> 4253.10]  what i get for it's being like i'm gonna go and say thank you for joining me johnny and you're like
[4253.10 --> 4257.34]  oh thanks for having me i'm like oh thank you as well ian and you say thank you for having me it's
[4257.34 --> 4261.86]  like okay good we're done but we can't do that because you had to be all snooty snooty
[4261.86 --> 4267.78]  i think i'm gonna i'm not gonna i'm not gonna do that to my friend it's my friend
[4267.78 --> 4270.96]  yeah yeah rude
[4270.96 --> 4280.26]  oh on that note it was a pleasure on that note a pleasure having you both here ian johnny
[4280.26 --> 4288.74]  it was a pleasure being here chris yes ian was here oh lord and thank you listener for sticking
[4288.74 --> 4301.02]  through this whole episode uh and we'll catch you next time on go time i'm trading changelog sticker
[4301.02 --> 4308.34]  packs for thoughtful five-star reviews on apple podcasts and spotify or blog posts recommending
[4308.34 --> 4316.42]  go time simply send evidence of your review or blog post to go time at changelog.com alongside a
[4316.42 --> 4322.44]  mailing address and i'll send you free stickers right to your mailbox once again that's go time
[4322.44 --> 4328.46]  at changelog.com go ahead get your sticker on thanks once again to our partners at fly.io
[4328.46 --> 4334.58]  to our bee freaking residents breakmaster cylinder and to our friends at sentry use code changelog when
[4334.58 --> 4340.82]  you sign up and save 100 bucks on their team plan why not right that's all for now but we'll talk to
[4340.82 --> 4343.20]  you again next time on go time
[4346.42 --> 4359.76]  Aj Dig Log
[4360.92 --> 4365.10]  ...
[4368.04 --> 4368.90]  ...
[4369.52 --> 4370.98]  ...
[4370.98 --> 4373.98]  ...
