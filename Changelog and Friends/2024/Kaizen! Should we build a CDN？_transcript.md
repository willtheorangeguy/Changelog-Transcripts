[0.00 --> 21.84]  welcome to changelog and friends a weekly talk show about cdn shopping thank you to our partners
[21.84 --> 31.66]  at fly.io the home of changelog.com launch your app close to your users learn how at fly.io okay let's
[31.66 --> 47.38]  talk gerhard is here once again we are kaizen in 2024 yeah great to be back 2024 here we go we made it
[47.38 --> 53.26]  we're here yeah the first kaizen for this year and it happened so soon we all made it back from
[53.26 --> 58.32]  chicago no crazy stories on the way home we already shared all of our crazy stories on the way there
[58.32 --> 64.98]  so here we are did we actually share those stories though i think it was like in a i've learned how
[64.98 --> 72.60]  to say cheers adam and jared style it involves a single glass oh yes that was so funny
[72.60 --> 82.32]  that was one of my highlights say more say more so apparently the way you say cheers is both of you
[82.32 --> 87.74]  hold the same glass you hold it up so it was like you're almost like holding your hands and you say
[87.74 --> 96.12]  cheers i haven't seen that one before that was so fun that's funny that is funny it was so inconsequential
[96.12 --> 100.32]  to me i don't even remember it no offense i think it was a picture moment i think we have a picture
[100.32 --> 104.56]  of that somewhere we're holding the same glass pretty much yeah we're pretty close we get pretty
[104.56 --> 108.56]  close around here we're not holding the exact same glass we're holding our own version to the glass
[108.56 --> 113.10]  and we're clinking them right is that what you're talking about no no no gosh maybe i am there is a
[113.10 --> 117.32]  picture of this didn't happen yeah i don't remember that picture didn't happen no no it didn't happen
[117.32 --> 122.90]  that's okay what happened in chicago can stay in chicago unless you have a picture and then it can come
[122.90 --> 128.34]  out i don't have no problem with it i can look it up it's there somewhere okay i'll take your word for it
[128.34 --> 132.62]  so the receipts are in the show notes if gerhard can come up with receipts they will be in the show
[132.62 --> 137.72]  notes if not then we just know he's just fabricating evidence yeah yeah since this is the new year can
[137.72 --> 143.82]  i just say that i remember when gerhard used to version our infrastructure by the year yes and now
[143.82 --> 148.86]  it's sort of versioned i guess every two months or kind of continuously in a way really that was
[148.86 --> 154.40]  crazy right like that we're a whole new era of continuous improvement yeah i mean i do it's almost
[154.40 --> 160.68]  like a generation so for example our fly app the one that is currently running production is 2022
[160.68 --> 167.90]  0 3 13 right and guess how i remember it i just remember it just sticks with you and the next one
[167.90 --> 176.16]  the one that we're currently experimenting with is 2023 12 17 so 17th of december okay this is the new
[176.16 --> 183.32]  generation of the changelog app that's already old and busted it's 23 we're on 24 now yeah well guess
[183.32 --> 187.80]  what we can delete that one and set the new one up and that's okay it's too easy right yeah it's too
[187.80 --> 194.50]  easy i like your propensity to date stamp things because it's very nice for like remembering like
[194.50 --> 199.46]  hey when did i do that thing what i don't like about it is it makes things feel old for instance
[199.46 --> 205.80]  one subdirectory in our code base that i do not appreciate and i'm here to air my grievances is
[205.80 --> 215.22]  2022.fly a that's just an ugly folder name b that's forever ago c i have to like go in there to
[215.22 --> 220.64]  do stuff with fly when i could just have all that in the root and just be chilling so i'd just like you
[220.64 --> 225.76]  to defend the decision making process there garth and explain it to me what how did that come to be
[225.76 --> 232.76]  so it really was the generation of the app it was 2022 we've set it up for 2022 and i just created
[232.76 --> 237.62]  the fly folder because before if you remember we had the various kubernetes clusters and we had
[237.62 --> 242.22]  them versioned by year and we're kind of straddling for a while weren't we yeah and exactly that's what
[242.22 --> 248.00]  this was like our migration to fly which happened in 2022 that's that's how long ago it's been wow
[248.00 --> 253.50]  and since then we really haven't changed the app we've done a bunch of other things but that app
[253.50 --> 261.04]  in its implementation state as is there's a new flooded io directory where we're starting to capture apps
[261.04 --> 265.94]  oh yeah that's been there for a while is it year stamped um it's just fly because the apps are
[265.94 --> 271.38]  are time stamped in the directory and the one that we have there you'll see it's the dagger engines
[271.38 --> 278.46]  gotcha because our ci also runs on fly the the workers themselves and that's what that is so the new
[278.46 --> 284.90]  app which is basically part of a pr uh 492 and we'll get to that in a minute in flight in progress
[284.90 --> 291.12]  exactly it's in flight it's also in that directory so the app is time stamped and we have multiple apps
[291.12 --> 296.72]  because the idea is we have more than one and like changelog social for example it's another app
[296.72 --> 301.06]  that we run on fly but that's in a different repo maybe we consolidate maybe we don't i don't know
[301.06 --> 306.90]  the point is it's a nice way to store all your apps because we have more than one and then you know
[306.90 --> 312.86]  which one you're targeting it makes it very simple uh to not make mistakes when you want to work
[312.86 --> 317.32]  against a specific app right right you can't basically be in the root and the root has changed
[317.32 --> 322.48]  and then maybe you're targeting a different app instance this way it's very clear which app instance
[322.48 --> 327.58]  you're working against makes sense well said good defense are those tied to the machine then like you
[327.58 --> 331.76]  said or does that make sense to tie to the machine or did i miss that part i was trying to grok everything
[331.76 --> 338.26]  you're saying no it's just the app instance so each app is backed by multiple machines okay so that is
[338.26 --> 343.50]  like a subdivision of the app and this flat directory fly.io directory is part of the
[343.50 --> 348.52]  492 pull request or this is predating that it predates it okay because i didn't see it in master
[348.52 --> 354.70]  it's there i got it in my code base is it there in master yeah it's just hidden oh i see it because
[354.70 --> 360.38]  it only has one directory it's it's not year there's no year so yeah that's why okay cool but more are
[360.38 --> 364.74]  coming more apps like this one for example the second one because we've been doing this for a while
[364.74 --> 369.64]  right we have two apps like two change logs running at the same time and we don't want that to be part
[369.64 --> 375.74]  of a pull request for too long this 492 is a special case again we'll come back to that but uh that's
[375.74 --> 380.16]  the idea you can have multiple apps running at the same time and you do like a long blue green
[380.16 --> 385.60]  awesome dig it one thing which i would like to do now because it is the beginning of a new year
[385.60 --> 393.64]  is take a step back and take a bigger take on this okay so what i'm thinking and we have time
[393.64 --> 399.90]  okay this is edited so it's okay okay it's a big idea when i answer this real quickly everybody
[399.90 --> 405.24]  will know that there's like six minutes of silence that got out i was thinking about my answer what
[405.24 --> 411.60]  is the one thing that you want to achieve this year with regarding to change on.com you can make
[411.60 --> 416.86]  it as big or as small as you want okay we have some big ideas they're more like features though not
[416.86 --> 423.10]  infra we can do we can go there like this is basically so we don't we don't constrict the creativity
[423.10 --> 428.08]  and the space right he wants this is open-ended on purpose he's setting us up here open-ended on
[428.08 --> 434.34]  purpose yes and mine is big i can tell like mine is really really big okay oh wow why don't you go
[434.34 --> 443.58]  first okay it's as if i'm prepared yeah i am so i'll go no edit necessary here yeah go ahead
[443.58 --> 448.84]  my birthday doesn't happen every year that's right you're a leap year baby and this one is special
[448.84 --> 456.10]  because it also kicks off a new decade for me oh so just to put it into perspective the next time
[456.10 --> 462.86]  that my birthday coincides with a new decade i'll be 60 years old so this is like a once a score
[462.86 --> 470.22]  you're scoring yeah pretty much so after two decades of hands-on experience which is well over 10 000
[470.22 --> 475.64]  hours i have this urge to produce something that i haven't done before something in the content space
[475.64 --> 482.76]  something that combines audio and video and ai and ai is a very important element and 2024 is a
[482.76 --> 488.48]  combination of so many things for me that makes me really excited for it because it doesn't come
[488.48 --> 495.58]  often no this is a lot of pressure i think this is it the next one will be 60 so it's big i told
[495.58 --> 501.36]  he's big do you have more than that or is that all you're saying that's all i'm saying because um so
[501.36 --> 505.58]  big that you're not going to put any sort of box around it yet remember last time when i've done
[505.58 --> 510.76]  this let's see if this time it works better big something up but then disappointing you so i'm
[510.76 --> 518.68]  not going to say anymore yeah don't build up too big so content and ai and video and audio yep okay
[518.68 --> 524.36]  is there any more details that's it just content space and it's going to ship on your birthday uh
[524.36 --> 528.58]  before but yes there i'm going to do something special for my birthday for sure it's a one-time
[528.58 --> 533.68]  thing or is it an episodic thing i think it's going to be an episodic thing but i have like all
[533.68 --> 539.06]  these interests in hardware and software and combining things and it is the long term that
[539.06 --> 544.58]  i'm thinking about like not months not even years decades something that can be tracked over decades
[544.58 --> 549.72]  something that when i'm 60 i can look back and i can say wow the last 20 years have been amazing
[549.72 --> 554.36]  so that's the time scale that i'm thinking at okay so you're going to start something but you're not
[554.36 --> 559.06]  going to finish it it's going to be a new thing you're starting yeah something like that okay how
[559.06 --> 563.76]  do you start and not finish i'll finish when i'm 60 or when i can take yet or when i'm done exactly
[563.76 --> 569.82]  okay but i'm you know this is enough i had fun how frequent are these episodes are they are they
[569.82 --> 576.26]  yearly are they monthly are they weekly let's see what happens let's okay wow he's not gonna say he's
[576.26 --> 581.48]  not gonna build it up that's a good goal i mean i feel like i shouldn't have any goals shared after
[581.48 --> 586.70]  that one i mean it's i'm gonna sound like a mere piker no matter what i say we can make a smaller
[586.70 --> 591.16]  one i mean this is big right there's like different time scales um in the context of this is like a
[591.16 --> 595.74]  project of the lifetime yeah something like that it feels that way almost like a next evolution of
[595.74 --> 600.04]  something that i've been working on for a long long time and ship it was part of it by the way
[600.04 --> 604.86]  that was just a small part it was a stepping stone on your way to this other thing pretty much and
[604.86 --> 610.44]  before that it was the rabbitmq videos tgir those were fun that was like a whole year of videos
[610.44 --> 616.52]  well i hope you achieve that goal it's still live tgi.rabbitmq.com people can go and check it out
[616.52 --> 623.24]  i was terrible but i run so much so go and have some fun there you go see how not to do videos
[623.24 --> 630.74]  i was learning yeah that's how you learn all right i like that one um adam what's your
[630.74 --> 638.06]  goal for the year oh big or small doesn't have to be as big as gear hearts probably won't be
[638.06 --> 645.94]  i have two oh he always does this he'll end up with seven yeah well i think we know what one goal
[645.94 --> 652.78]  is which is to finally get plus plus in-house meaning not on supercast and i think that there's
[652.78 --> 658.60]  some things that will all gain from that both you know how we promote it how you know listeners
[658.60 --> 664.32]  understand it how it can grow how it can be embedded in the application process and just how
[664.32 --> 668.96]  all the workflows work i think there's a lot of gain there and i know we've been taking incremental
[668.96 --> 674.42]  steps towards that and i think one that you and i were kind of passionate about jared so i think if
[674.42 --> 679.06]  you don't mind me talking about the one we just talked about the tail end of the last year which
[679.06 --> 684.82]  has the word j-o-b in it and i guess an s is that cool can i mention that well we're we're
[684.82 --> 688.92]  goaling so yeah go ahead doesn't mean it's going to happen but it's a goal yeah i think so i think
[688.92 --> 694.18]  it's worth talking about and it feels kind of even weird to put this as a goal because it seems very
[694.18 --> 700.42]  simple but i think to execute at the level we like to execute at it is not very simple and so we
[700.42 --> 705.26]  we're talking with our friends at go time about just different ways to sustain that podcast
[705.26 --> 710.70]  and you know during the conversation that the idea of a job or came back up is a way to
[710.70 --> 717.68]  alternatively sustain a podcast so that show has not had the best track record of being
[717.68 --> 724.54]  well sponsored but it also is a really awesome podcast and that's not its fault that it has
[724.54 --> 728.68]  trouble gaining and maintaining sponsors i think it's just a challenging thing for the podcast industry
[728.68 --> 733.70]  and i was like well what if we found a different way to like give value back to that community
[733.70 --> 740.38]  and so the conversation sort of stemmed towards you know it may be a go focus job board and then
[740.38 --> 744.46]  i think afterwards jared and i had a brief conversation or it was in slack or something
[744.46 --> 751.20]  like that like what if it was just changelaw.jobs so there is a .jobs tld and so like if we had
[751.20 --> 757.58]  changelaw.jobs and we made it a sas product where you can subscribe to it to have jobs there frequently
[757.58 --> 763.94]  being the job promoter not the job seeker and we leveraged our podcast network and found a way to
[763.94 --> 770.14]  automatically or systematically pull those job promotions in and out of the podcast to make them
[770.14 --> 778.78]  dynamic basically then we have a real interesting way to have a job board that has an interesting
[778.78 --> 786.56]  economic footprint behind it where it's sas based or one-off based and we really do a pretty good job
[786.56 --> 791.56]  of this job or not just like put it up and go post a job kind of thing but far more embedded into the
[791.56 --> 799.14]  network i think if we can execute on that well then we have a decent i would just say money maker on our
[799.14 --> 805.60]  hands that helps us sustain whenever sponsorship slim or you know as we prop up plus plus and that
[805.60 --> 810.76]  becomes more and more of a leg which honestly for those who support us on the plus plus side
[810.76 --> 818.30]  we want it to be more of a leg to our chair i suppose in terms of stability but we never really
[818.30 --> 824.40]  anticipated being that like traditionally sponsorships have always trumped the amount of revenue we can
[824.40 --> 830.06]  gain from plus plus but i think there's like an untapped market on subscribers supporting you
[830.06 --> 836.32]  and i think that's where bringing plus plus inside gives us that chance but then also this opportunity
[836.32 --> 844.32]  for changelog.jobs being a great indie dev centered place to get and look for cool jobs and i think one
[844.32 --> 848.82]  part of that is maybe the vetting process so lots of interesting things on how to execute not just throwing
[848.82 --> 854.34]  it up and you know there you go post a job but something that's a bit more well executed and
[854.34 --> 858.32]  really for the indie market because most of the indie markets in the job space that have been like
[858.32 --> 865.98]  boards have been bought up by the big guys you know the big folks or neglected yeah or neglected i mean
[865.98 --> 871.28]  github jobs is pretty cool but i mean obviously github is not jobs um and i think it went by the wayside
[871.28 --> 877.24]  last time i checked early early on that was one of our first sponsorships here on this podcast and it's
[877.24 --> 885.56]  kind of cathartic jared to say that uh my dream thing for this i suppose goal is to promote jobs
[885.56 --> 892.20]  i said it before we will never promote jobs on this podcast i'm never saying never again man why are you
[892.20 --> 896.42]  bringing why are you telling people again why are you bringing it back up it always bites me i mean i
[896.42 --> 902.02]  don't mind uh that's cool but i think if uh i really don't mind i like being wrong honestly i love being
[902.02 --> 908.50]  wrong when it when it's right to be right i suppose because i think if we do this right it could be a
[908.50 --> 913.44]  cool fun thing for the community and it could be a good revenue driver for us and it'd be kind of
[913.44 --> 917.12]  cool to put that info behind that like the front end the back and all the things that we've been
[917.12 --> 922.60]  building it would just be kind of you know easy to extend what we're already doing well yeah so that's
[922.60 --> 927.68]  my one thing which i would like to add to this because it does connect i was exchanging some dms
[927.68 --> 935.44]  with someone from our community her name is mary hightower and i'll just read the one sentence which
[935.44 --> 942.72]  is very relevant to this this was end of november uh so a few a few months back one thing and i'm
[942.72 --> 949.18]  quoting mary one thing i've seen in the changelog crowd is the perspective of how to build software
[949.18 --> 955.44]  and teams well i think that's something important because it is in changelog's dna to care about those
[955.44 --> 960.32]  things and it's not me saying this it's like someone that has been our community and i'm sure
[960.32 --> 967.26]  that others must feel similar to this because there is a perspective on what does it mean to be a good
[967.26 --> 974.74]  team what does it mean to have a successful community a successful relationship and coming back
[974.74 --> 980.58]  changelog and friends look at us what we're doing now how open we are how we're trying to you know
[980.58 --> 985.86]  support those that you know maybe are less fortunate than us when it comes to their work
[985.86 --> 992.52]  environment yeah well said i think that's uh i think that's on point and entirely relevant
[992.52 --> 998.50]  and a reason why something like this which to me has always seemed like potentially a bolt-on
[998.50 --> 1006.80]  you know could actually be very integral and valuable you know yeah if we execute it right
[1006.80 --> 1013.58]  which is always for us you know uh strengths and weaknesses our strength is our weakness we know
[1013.58 --> 1018.52]  that perfection is the enemy of progress and progress over perfection and that's why we kaizen
[1018.52 --> 1025.90]  and that's why we do mvps and all these kind of things because adam and i both desire the the
[1025.90 --> 1030.46]  perfection and sometimes we just don't build the thing because we're like well we can't figure out how
[1030.46 --> 1035.42]  to do it perfect or even well and so we're not going to do it right now yeah hopefully we can
[1035.42 --> 1042.56]  eschew that and get a jobs thing going in order to provide that value and to sustain shows like go
[1042.56 --> 1050.16]  time and it really our entire network when advertising wanes so to me it's feeling less and less like
[1050.16 --> 1057.46]  a bolt-on money maker and more and more like true value for all of us so i'm into it whereas in the
[1057.46 --> 1062.70]  past i've kind of pooh-poohed it um yeah so i've had a change of tone same me too that's why i was like
[1062.70 --> 1067.20]  so cathartic that we would actually go back to it that uh or just that would become an idea again
[1067.20 --> 1073.42]  i suppose like how in the world does that even make sense and somehow it does make sense now that
[1073.42 --> 1080.02]  that's even something we're promoting or suggesting and it it has always seemed like a bolt-on that
[1080.02 --> 1084.30]  didn't really provide the value it always seemed like well this would only be so that we can find
[1084.30 --> 1089.24]  one more way to sustain right whereas now i feel like if we can embed them into the shows
[1089.24 --> 1095.88]  in the ways we think we can and swap them out when necessary dynamically then i think that's a big
[1095.88 --> 1101.70]  win for us and a big win for the folks trying to find the right folks you know and i think if we could
[1101.70 --> 1107.92]  do a good job on vetting who comes into that pool and just some way to provide like you were saying
[1107.92 --> 1113.06]  with with you know quoting mary hightower hi mary by the way you know i think that's great like
[1113.06 --> 1117.70]  building great software building great teams i think has always been the fun part of the
[1117.70 --> 1122.52]  conversations we just had that conversation uh with dan moore on uh letters to developers
[1122.52 --> 1127.74]  such a cool conversation the first shot of the gate this year and yeah i think it's gonna be
[1127.74 --> 1137.04]  a big hit for the year and it's show number one for 2024 yeah so adam shared two therefore i will
[1137.04 --> 1144.48]  share zero three three no yeah one two three no i'm thinking he stole mine so changelog plus plus
[1144.48 --> 1150.04]  2.0 was exactly what i was gonna say sorry jared no it's all right you're doubling down it's definitely
[1150.04 --> 1155.00]  going to happen we're on the same page that's a good thing we have i mean uh we should have similar
[1155.00 --> 1162.48]  goals shouldn't we yeah bringing changelog plus plus on site in our control and making it way better
[1162.48 --> 1167.36]  we have lots of ideas and we've kind of been inching towards that we haven't gone all in on it because
[1167.36 --> 1171.98]  there's always been one more thing that pops up is more important for instance even our big
[1171.98 --> 1176.90]  conversation today about postgres is the thing that is currently just more important than that although
[1176.90 --> 1180.94]  you're doing the bulk of the lifting on that there's other things that are popping up i'm sure we'll be
[1180.94 --> 1185.44]  talking about soon which are more time sensitive than that and so it kind of always gets pushed off
[1185.44 --> 1191.72]  yeah and i just want to stop pushing it off and actually get it done because a we've had more
[1191.72 --> 1197.76]  subscribers recently so thank you to all of you who joined yes big time uh it's been very uplifting
[1197.76 --> 1203.38]  to see so many people joining on even in its current state which we know is not as good as it could be
[1203.38 --> 1209.90]  and 90 of the people are there just to support us and we love that but we also want to you know
[1209.90 --> 1215.26]  quid pro quo that and provide value back and make it awesome so it's been a thing that i think
[1215.26 --> 1220.30]  i even wanted to do last year and just didn't do it so it's like enough is enough let's do this
[1220.30 --> 1227.88]  and let's do it well and not perfect because then it'll never ship but ship something and do the
[1227.88 --> 1232.26]  bulk of the work and then refine from there so that's my goal that's a good one that's a good one
[1232.26 --> 1244.64]  what's up friends i'm here with one of our good friends for ross of buka dj
[1244.64 --> 1252.06]  for ross is the founder and ceo of socket you can find them at socket.dev secure your supply chain
[1252.06 --> 1257.50]  ship with confidence but for ross i have a question for you what's the problem what security concerns
[1257.50 --> 1261.98]  do developers face when consuming open source dependencies what does socket do to solve these
[1261.98 --> 1267.32]  problems so the problem that socket solves is when a developer is choosing a package there's so much
[1267.32 --> 1271.84]  potential information they could look at right i mean at the end of the day they're trying to get a
[1271.84 --> 1275.74]  job done right there's a feature they want to implement they want to solve a problem so they go
[1275.74 --> 1279.88]  and find a package that looks like it might be a promising solution maybe they check to see that it
[1279.88 --> 1284.22]  has an open source license that it has good docs maybe they check the number of downloads or github
[1284.22 --> 1290.56]  stars but most developers don't really go beyond that and if you think about what it means to use a good
[1290.56 --> 1295.62]  package to find it to use a good open source dependency we care about a lot of other things too right we care
[1295.62 --> 1300.62]  about who is the maintainer is this thing well maintained from a security perspective we care about
[1300.62 --> 1305.16]  does this thing have known vulnerabilities does it do weird things maybe it takes your environment
[1305.16 --> 1309.98]  variables and it sends them off to the network uh you know meaning it's going to take your your api
[1309.98 --> 1314.58]  keys your tokens like that would be bad uh the unfortunate thing is that today most developers
[1314.58 --> 1318.66]  who are choosing packages and and going about their day they're not looking for that type of stuff
[1318.66 --> 1323.64]  it's not really reasonable to expect a developer to go and open up every single one of their
[1323.64 --> 1328.94]  dependencies and read every line of code not to mention that the average npm package has 79
[1328.94 --> 1333.46]  additional dependencies that it brings in so you're talking about just you know thousands and
[1333.46 --> 1339.06]  thousands of lines of code and so we do that work for the developer so we go out we we fully analyze
[1339.06 --> 1343.48]  every piece of their dependencies you know every one of those lines of code and we look for strange
[1343.48 --> 1347.64]  things we look for those risks that they're not going to have time to look for so we'll find you
[1347.64 --> 1353.32]  know we detect all kinds of attacks and and kinds of malware and uh vulnerabilities in those dependencies
[1353.32 --> 1357.36]  and we bring them to the developer and help them when they're at that moment of choosing a package
[1357.36 --> 1362.04]  okay that's good so what's the install process what's the getting started socket super easy to
[1362.04 --> 1366.50]  get started with so uh we're you know our whole team is made up of developers and uh so it's super
[1366.50 --> 1371.68]  developer friendly we got tired of using security tools that send a ton of alerts and were hard to
[1371.68 --> 1376.82]  configure and and and just kind of noisy and so we built socket to fix all those problems so we have
[1376.82 --> 1382.44]  all the typical integrations you'd expect a cli a github app an api all that good stuff but most of our
[1382.44 --> 1388.18]  users use socket through the github app and it's a really fast install a couple clicks you get it going
[1388.18 --> 1393.66]  and it monitors all your pull requests and you can get an accurate and kind of in-depth analysis of all
[1393.66 --> 1398.36]  your dependencies really high signal to noise you know it doesn't just cover vulnerabilities it's
[1398.36 --> 1404.32]  actually about the full picture of dependency risk and quality right so we we help you make better
[1404.32 --> 1408.98]  decisions about dependencies that you're using directly in the pull request workflow directly directly
[1408.98 --> 1412.56]  where you're spending your time as a developer you know whether you're managing a small project or a
[1412.56 --> 1417.26]  large application with thousands of dependencies socket has you covered and it's pretty simple to
[1417.26 --> 1424.04]  use it's it's really not a complicated tool very cool the next step is to go to socket.dev install the
[1424.04 --> 1432.48]  github app or book a demo either works for us again socket.dev that's s-o-c-k-e-t.dev
[1432.48 --> 1460.42]  okay well my next goal is to encourage you to open up github discussion 485 it's in our the changelog
[1460.42 --> 1465.54]  changelog.com repository because the bulk of this conversation is going to happen around that and
[1465.54 --> 1471.44]  if you're listening you can go there by then it should have been done but you can see all the
[1471.44 --> 1477.10]  topics all the links everything's there links in the show notes too by the way i think the biggest
[1477.10 --> 1482.30]  thing for us and we mentioned this a couple of times it is pull request 492 where we are migrating
[1482.30 --> 1489.48]  postgres to neon.tech so that's the big thing and it's the biggest change i think that we had since
[1489.48 --> 1497.32]  kaizen 12 is to set up neon.tech as a managed postgres alternative to our current postgres which
[1497.32 --> 1504.32]  is running on fly.io let's open up this pull request and yeah let's take a look at it just like to
[1504.32 --> 1512.04]  load some of the context let's do it so when i started this the first thing which i did and this is
[1512.04 --> 1517.36]  almost like the boy scout rule update dependencies and i know that we should have bots that do this
[1517.36 --> 1521.64]  automatically but sometimes especially when it comes to the major versions you would want to do
[1521.64 --> 1529.94]  that yourself like for example erlang that was an okay one 25 to 26 with that upgrade postgres this
[1529.94 --> 1534.90]  was like a bigger one from 15 to 16 nothing changed so it was still good but those types of upgrades you
[1534.90 --> 1540.16]  would want to you know supervise you wouldn't just want like a bot to do it for you and then you figure
[1540.16 --> 1544.34]  out oh there's like all these things which i missed and to be honest end of the years are really
[1544.34 --> 1549.92]  good for these like big upgrades so that's like 490 which is a precursor to this pull request we can
[1549.92 --> 1552.76]  come back to the elixir upgrade because by the way that's the one thing which didn't work very
[1552.76 --> 1558.42]  smoothly but we can come back to that later and just focus on this one so we have a new app instance
[1558.42 --> 1566.14]  as we discussed uh the 2023 1217 which is running on fly and that is configured to use postgres
[1566.14 --> 1571.84]  so adam is the one that set up postgres for us how is that adam how is like the whole initial setup
[1571.84 --> 1580.64]  of postgres you mean neon uh yeah on neon uh it was actually pretty easy uh barely any convenience
[1580.64 --> 1587.18]  for my uh screen fan lovers out there it was uh pretty easy i mean i think i just went in there
[1587.18 --> 1591.94]  the only confusing thing was there wasn't the idea of orgs you know you create a project and inside
[1591.94 --> 1598.04]  that project you invite people so that was kind of i guess the only oddity i mean i did nothing besides
[1598.04 --> 1603.50]  you're giving way too much credit honestly i just talked to the folks folks behind neon are amazing
[1603.50 --> 1608.30]  you started it without that we wouldn't we could that this would not have been possible so
[1608.30 --> 1612.60]  well if you want me to give you the real getting started story i began in all things open really
[1612.60 --> 1619.02]  and so uh their cto was there and their team was there ralph and others were there and i was like
[1619.02 --> 1622.84]  jerry we should just go over there and talk to them because we want to have a managed postgres
[1622.84 --> 1627.88]  like gara's been pushing for this and my first you know you might want things gara but then i go and
[1627.88 --> 1634.32]  ask jared do you also want this do you do you bless this because jared really is our you know our cto
[1634.32 --> 1639.82]  really and so if i would never make a tech choice without conferring with both of you guys that that's
[1639.82 --> 1646.06]  what we should do yeah and so i asked jared he's like yeah that works let's do that and so i went over
[1646.06 --> 1650.76]  and we ended up getting them in the pod and we talked further and then we talked further afterwards
[1650.76 --> 1656.76]  and i just laid it out like hey we love fly big love to fly but we want something that's
[1656.76 --> 1663.96]  future focused and i think in my discussions with kurt around kurt mackie who is the co-founder and ceo of
[1663.96 --> 1669.36]  fly.io he was always like you know we we have different ambitions and databases are part of it but
[1669.36 --> 1674.20]  we know we're not providing the state of our thing it's good it's good for everybody but this
[1674.20 --> 1678.84]  isn't something that we're sort of like laying further into now that may have changed in that year and a
[1678.84 --> 1683.90]  half a good conversation but i i was always like i know after our conversation jared and i was
[1683.90 --> 1689.26]  conversation with nikita sham got out the ceo of neon i think about a year back right jared about a year
[1689.26 --> 1695.36]  and some back now that he really laid out a lot of good promise and he had experience in databases
[1695.36 --> 1700.66]  before like he had been previously successful around databases with like memcache i believe i forget
[1700.66 --> 1705.70]  what sequel cache or i forget what his previous startup was that was acquired but he had had some
[1705.70 --> 1711.52]  success and impressed us in that podcast about where they're taking postgres in particular
[1711.52 --> 1716.42]  serverless managed postgres and then the idea of maybe getting to geo which they're not quite there
[1716.42 --> 1721.26]  yet and then i think what really impressed me recently talking to them was around the way that
[1721.26 --> 1727.88]  they plan to bolt in bringing this dev mode to neon and postgres really where you're and y'all can
[1727.88 --> 1732.48]  probably speak to this more than i can but the way you interact with the database is one in production
[1732.48 --> 1741.44]  but also in dev and so to innovate and to experiment with the database at the dev level always requires
[1741.44 --> 1746.72]  some sort of like cloning of the production database and this weird flow and they've made it a way because
[1746.72 --> 1752.76]  it's serverless and because it's sort of ephemeral to allow you to just branch off the database and this
[1752.76 --> 1759.04]  isn't a new concept necessarily for databases i think who's it out there gosh their other name it's the
[1759.04 --> 1764.44]  sql one my the my sequel one planet scale planet scale yes thank you i think planet scale really
[1764.44 --> 1770.30]  began a lot of this branching idea with vitess and whatnot so it's not a new concept but it's a new
[1770.30 --> 1774.36]  concept of postgres they have upstream commits they have a lot of promise and so we're like
[1774.36 --> 1779.34]  really enjoying the process of where neon can go so that's sort of the the precursor backstory
[1779.34 --> 1784.08]  well then all things open talk to them talk to them about partnerships and stuff like that and
[1784.08 --> 1789.26]  like let's do it and so they gave me the keys i went in i opened up the project and i invited gary
[1789.26 --> 1795.90]  that's what i did to kick off neon for the long story short but it really began uh a year or so ago
[1795.90 --> 1801.28]  really the the idea of neon being something that we can use and just knowing we like to play with cool
[1801.28 --> 1808.56]  things manage serverless postgres is something we should be playing with and now we are yeah so i'm very
[1808.56 --> 1815.86]  curious to see what jared thinks about connecting to a branch for his local development would you do
[1815.86 --> 1820.36]  that do you see yourself doing that absolutely is that weird for you you expect me to say no
[1820.36 --> 1826.54]  no i mean like would you generally i'm a naysayer you are also it's not local so it's going to be
[1826.54 --> 1832.64]  slower and you need like an internet connection and all of that i agree it will be um not slower like
[1832.64 --> 1837.46]  docker for mac slower which for me was a long time naysayer like no i'm not going to run on my
[1837.46 --> 1841.28]  development environment through docker i already have it set up we've i mean that's years long
[1841.28 --> 1846.10]  thing with like how should people contribute let's set up docker containers jared won't use it so it's
[1846.10 --> 1852.20]  not going to be good you know that whole deal that's right i'm way less concerned about some slower
[1852.20 --> 1861.34]  query times in development because i have a recurring pain with development where i do like to have fresh
[1861.34 --> 1867.44]  data as i'm coding uh it's just more realistic it's more enjoyable it's just i prefer that
[1867.44 --> 1878.34]  and so i am often doing a fly proxy a pg dump to my local and a pg restore or whatever the actual
[1878.34 --> 1884.44]  command is in order to get fresh data and i'll do that once a week uh every time i'm starting up a
[1884.44 --> 1888.22]  new coding session sometimes i'll be like oh this is fine it's last week's data no big deal other
[1888.22 --> 1892.60]  times especially like there's a bug well the bug often has to do with data that's in production that's
[1892.60 --> 1897.02]  not in development of course and so i want freshens and so i'm just constantly doing that
[1897.02 --> 1901.70]  and it's just part of my workflow you know i go get a cup of coffee it's not a very large database
[1901.70 --> 1907.98]  it's large enough that you're going to wait for it and that's a pain that i live with but i do want
[1907.98 --> 1913.66]  that snapshot to be relatively recent being able to connect to a dev mode which is just a branch of
[1913.66 --> 1919.80]  production that i'm assuming i can either re-sync or just do a new snapshot whenever i'd like to
[1919.80 --> 1924.16]  and it just is somewhere else and i just change my connection string i don't have to
[1924.16 --> 1930.12]  version postgres locally it's one less dependency on my local box i'm here for it i haven't tried that
[1930.12 --> 1936.00]  yet i haven't used it obviously we are in flight with even you know doing this so maybe i'll end up
[1936.00 --> 1940.74]  hating it and be like nah i'll just run my local postgres and do a snapshot and and everything will
[1940.74 --> 1946.78]  be fine but i'm definitely not naysaying it yet like i'm excited to try it and i think it's
[1946.78 --> 1950.88]  going to be better than what i currently do i think that's a really cool idea because it helps
[1950.88 --> 1958.34]  me figure out what else is important part of this pull request the 492 and my most important take on
[1958.34 --> 1963.72]  this was like okay so if we do this what will this unlock what will this enable us to do differently or
[1963.72 --> 1969.56]  better than we're doing today and what you're saying to me sounds like that's like a great goal
[1969.56 --> 1975.60]  to work towards because it will simplify things a lot you don't need postgres locally one other thing
[1975.60 --> 1981.74]  it's almost like a complication to this what about contributors what about people that don't have
[1981.74 --> 1987.28]  access to our production data and we will not be able to give them access to production data even if
[1987.28 --> 1991.62]  it's a branch they're currently in the exact same box like they're already there they live there right
[1991.62 --> 1996.04]  now yeah and that's one of my pains is people are like i'd love to contribute cool go click on the
[1996.04 --> 2000.38]  repo check the contributing guide and they're like awesome can i have some data that's like real because
[2000.38 --> 2005.16]  they don't even have like podcasts when they're you know and we had seed data in the past and it's
[2005.16 --> 2010.74]  just like we are not an open source project like most open source projects where it's like there are
[2010.74 --> 2017.44]  dozens if not hundreds of strangers working together it's like we have a fly by contributor once in a while
[2017.44 --> 2024.98]  and we want to enable them but oftentimes that person who comes maybe once every few months is not worth
[2024.98 --> 2030.30]  maintaining seed information or i i had a long like my to-do list right at the bottom of it's like
[2030.30 --> 2037.20]  find a way of just taking production and sanitizing it and reducing it down to what they could use and
[2037.20 --> 2041.66]  provide that for people and i don't have it done like there's no i don't have answers for them i'm
[2041.66 --> 2047.40]  like yeah you can you can just do it without data it's no big deal hopefully and like one guy was
[2047.40 --> 2052.74]  working on the player which like he couldn't play an mp3 so he couldn't actually do i can't remember what
[2052.74 --> 2057.24]  he was trying to do and i'm like well it's going to take me hours to get you going so that's where
[2057.24 --> 2061.36]  we already are so we aren't losing anything we're not solving that problem though sounds like yeah
[2061.36 --> 2068.70]  maybe we are maybe there's a way you can provide them a branch with a sanitized branch you know yeah
[2068.70 --> 2074.12]  i think this is where neon would be great conversation with neon to see okay so when we do create a branch
[2074.12 --> 2080.26]  can we add some extra stuff that runs part of that branch so it puts it in a state which is okay to
[2080.26 --> 2085.64]  share and then we can automate that in some way so that whenever someone wants to contribute they
[2085.64 --> 2089.04]  basically connect to the latest one and they don't have to do anything because the connection string
[2089.04 --> 2093.56]  doesn't change right and what we make available you know so that's that would be an interesting one
[2093.56 --> 2097.96]  and i kind of got that far i have to go back and find it but i do have at least the start of like
[2097.96 --> 2104.24]  what is the series of sql commands i would run to take production and sanitize it and reduce it
[2104.24 --> 2109.70]  to useful but not real and i started like writing some deletes and stuff like i probably have that
[2109.70 --> 2114.06]  somewhere but i never actually got to a place where i could then it was all ad hoc like okay i'm gonna
[2114.06 --> 2119.08]  go get a snapshot i'm gonna delete stuff i'm gonna give you the sql file via dropbox or something lame
[2119.08 --> 2126.40]  right so this could be cool in that way maybe yeah so that sounds almost like a step four we're still
[2126.40 --> 2132.92]  at step zero we're still migrating towards it in that the pull request is open and one of the first
[2132.92 --> 2139.26]  observations was that the latency increased and if you think about it it makes sense because with fly
[2139.26 --> 2145.38]  postgres was local so we get like sub millisecond latency in neon's case the postgres is remote
[2145.38 --> 2152.34]  it's running in aws still the same region but it adds a couple of milliseconds and when you have lots
[2152.34 --> 2158.22]  of queries which we do on some pages they add up so for example when we started this the home page
[2158.22 --> 2165.48]  latency just shot up by 3x and jared you like came here and did like some elixir foo and reduced the
[2165.48 --> 2173.00]  number of select statements we had 70 plus now we have 15 so while it was 3x before now it's like maybe
[2173.00 --> 2181.86]  10 which is 0.1 so that's a huge huge improvement so how do we feel about knowing that the latency
[2181.86 --> 2188.48]  of all our database queries will increase are we okay with that yes because we are leveraging
[2188.48 --> 2195.90]  cached information most of the time okay and also that i can now be more diligent as well so a lot of
[2195.90 --> 2204.22]  the reason is like i never had a good enough reason to go optimize that particular page and then i did and
[2204.22 --> 2211.20]  i spent an hour or two and now it went from 70 to 15 queries and i could do that on other things as
[2211.20 --> 2218.42]  well i know you you posted slash feed is also super slow 477 selects i think which is too many for
[2218.42 --> 2225.12]  anything but that page is never live it's always pre-computed and so i mean when you hit it on fly
[2225.12 --> 2230.78]  directly of course it's going to hit but when you hit it through changel.com it's going to a pre-computed
[2230.78 --> 2238.24]  xml file that's on r2 so like we've already kind of solved for that in other ways and we can use
[2238.24 --> 2244.14]  honeycomb and know when stuff gets slow and then we go optimize it just like developers do so i'm not
[2244.14 --> 2248.62]  really concerned with that i think it's kind of it sucks having network latency when you don't need it
[2248.62 --> 2256.20]  like we could avoid it with this other thing but i think the the wins outweigh the the drawbacks
[2256.20 --> 2261.78]  what do you think guard is there a way to reduce it natively like you said they're in the same region
[2261.78 --> 2267.38]  is there a way that uh you know from an interest standpoint we can put them closer even though
[2267.38 --> 2272.56]  they're different networks like how can we get them in quotes closer to not have that much latency
[2272.56 --> 2279.88]  so there's nothing that we can do like this team can do to improve that because we are already in the
[2279.88 --> 2285.88]  flyer region which is closest to the neon region so we can't basically pick another region
[2285.88 --> 2293.42]  either on fly or neon maybe there are some improvements that neon or fly can do but it's
[2293.42 --> 2297.58]  the speed of light that's what we're working against here so let's say we make it like a
[2297.58 --> 2302.36]  millisecond quicker it will not have the same impact as for example if we optimize some of the queries so
[2302.36 --> 2308.54]  we don't have to run 400 plus if we could reduce those that would help i think those are the biggest
[2308.54 --> 2314.50]  wins or the bigger wins that we should be looking at rather than physically getting these two things
[2314.50 --> 2320.14]  closer yeah but are you saying that our fly machines so we had a fly instance multiple fly
[2320.14 --> 2324.52]  instances that are running app servers and we had one fly instance that was running postgres
[2324.52 --> 2330.62]  and are you saying that those did not have network latency between them are you saying now there's
[2330.62 --> 2335.36]  more network latency they have a much lower network latency so we have they're still traversing
[2335.36 --> 2340.50]  the network stack though right like they're not co-located on the same machine correct but it
[2340.50 --> 2345.28]  doesn't leave the fly network so it's all happening within the fly network and we have two postgres
[2345.28 --> 2352.36]  instances so a primary and the replica this is on fly and we have the same setup on neon we have the
[2352.36 --> 2358.06]  primary it's called the read write instance and we have a read only which is a replica and the next point
[2358.06 --> 2362.64]  is like maybe we should look into that maybe we should configure to use read replicas but before we talk
[2362.64 --> 2369.26]  about that again same setup in neon as we have in fly the difference is that the physical distance is
[2369.26 --> 2373.94]  greater and there's more network hops and when i say network hops some of them are invisible
[2373.94 --> 2378.92]  because you don't see all network hops that happen but anyways we're just basically adding
[2378.92 --> 2384.86]  one maybe one and a half millisecond latency and again these aren't always the same they're variable
[2384.86 --> 2390.72]  but basically we're adding more latency to every single uh sql statement per query exactly and they
[2390.72 --> 2396.12]  just add up the more you have you're basically paying the network latency penalty for each of those
[2396.12 --> 2400.92]  queries rather than having one query that you know does more and then it comes back with all the
[2400.92 --> 2406.68]  results it goes back and forth back and forth right and that's is there any sort of like uh
[2406.68 --> 2412.68]  connection pooling or other things we could do in order to reduce that per query cost we have all
[2412.68 --> 2417.76]  that set up we do have that it's literally you run one you have to wait for the response you run
[2417.76 --> 2422.26]  another one and some of them do run in parallel but eventually you've run all these things and all the
[2422.26 --> 2427.76]  responses have to come back for you to be able to rebuild the page while if you use fewer request
[2427.76 --> 2434.80]  responses it will be quicker it's just just a law of math and physics doing less costs less than doing
[2434.80 --> 2439.08]  more yeah pretty much but again it's like it's a light of speed that that that's what we're dealing
[2439.08 --> 2444.82]  with here no physical distances and we're doing many round trips back and forth well let's work on
[2444.82 --> 2450.22]  that gerhard what can we do about that let's kaizen speed of light what can we can we slowly
[2450.22 --> 2457.94]  make that faster you know iteratively uh i don't think in my lifetime but i don't want to say never
[2457.94 --> 2465.70]  but i don't what about my 60 you know this could be your next 20 year project yeah maybe maybe uh
[2465.70 --> 2473.14]  a shorter project would be to um i think to look at the read replicas i think they would help
[2473.14 --> 2478.78]  so having some read replicas and having some i'm not sure they're in the same region but distribute
[2478.78 --> 2484.98]  them a little bit because fly i mean we have this option of distributing our app we haven't used it
[2484.98 --> 2489.02]  we're still like in a single region and we haven't used it because we haven't configured read replicas
[2489.02 --> 2494.28]  yet if we had a read replica in every single location this would be a lot more interesting
[2494.28 --> 2500.50]  so what do you think about read replicas in the context of our phoenix app gerard
[2500.50 --> 2507.08]  i think it's interesting i wouldn't put it like high priority just because of the obvious reason
[2507.08 --> 2514.32]  like most requests are never hitting our app you know you say that you say that but remember the
[2514.32 --> 2520.18]  issue with fly sorry not fly fastly oh my goodness me i was looking leaving that like towards later
[2520.18 --> 2525.12]  because that's not a fun one but we'll dig into it that's bad again well it's been bad since october
[2525.12 --> 2531.56]  and we can't seem to get anywhere with the fastly support that one so our hit ratio it's really
[2531.56 --> 2537.56]  tanked it's way down exactly and we've been trying to figure this out with fastly what is going on
[2537.56 --> 2543.52]  and we can't get the clear answer no changes on our end that we can identify no changes on our end no
[2543.52 --> 2550.86]  can you zoom out a bit and give a one minute version of that problem and exactly what's happening so
[2550.86 --> 2557.46]  there's context okay so let's talk about that um no he's excited you can tell to talk about this
[2557.46 --> 2563.66]  yeah i'm prepared for this i really like man this took this burned a lot of my budget that i have for
[2563.66 --> 2569.70]  changelog that's why this hurt this burned almost like a whole month of work budgets this like whole
[2569.70 --> 2577.92]  fastly cdn thing it was really that bad and there's an issue it's issue 486 it's a long one if you open
[2577.92 --> 2583.74]  it up to see just how much we talked and james a rosen was there so thank you james for helping out
[2583.74 --> 2589.12]  it's honestly like it'll take you at least 30 minutes to read it so can you imagine how long it
[2589.12 --> 2593.44]  took and this is only the public stuff there's also something even longer which is a whole fastly
[2593.44 --> 2599.52]  support thread that i wouldn't even want to open but anyways october 8th this is when it started
[2599.52 --> 2610.78]  our cdn cash misses increased by 7x so we had about 750 000 cash misses in a two-week period
[2610.78 --> 2620.70]  and after october 8th we had 5 million cash misses that's a crazy amount of number now this has improved
[2620.70 --> 2627.32]  since so we didn't do anything december 28th we are now at 900 000 now obviously requests go up and
[2627.32 --> 2634.12]  down but we still have more than we should do most of these requests are to the home page 80% of them
[2634.12 --> 2646.94]  are http 1 90% of them 19 19 are http 2 and only 1% are http 3 75% of all text html requests are cache misses
[2646.94 --> 2653.50]  so this is like highly cacheable content that there shouldn't be any misses and we get no explanation
[2653.50 --> 2659.44]  for why this just started happening i got so frustrated that i want to build my cdn
[2659.44 --> 2666.36]  that's not the 20 years project so yeah so three years ago kurt posted about this he wrote the five
[2666.36 --> 2671.64]  hour cdn on the flyo blog i already caught talking about this i think on a kaizen briefly yeah and
[2671.64 --> 2677.32]  actually it won't be that difficult honestly that would be easier to do than deal with all the fastly
[2677.32 --> 2683.10]  issues that's where i'm at now and this has been years this is not the first time by the way this is a
[2683.10 --> 2688.90]  long long long story i'm using a similar approach like i have like something like this configured in
[2688.90 --> 2694.56]  my kubernetes clusters i have quite a few nginx caches everything i have origins configured and it works
[2694.56 --> 2700.12]  and you can serve stale content it's not rocket science but at least would have full control over
[2700.12 --> 2705.20]  so what i'm thinking is let's deploy some nginx instances all over the world using fly
[2705.20 --> 2711.42]  let's serve all requests from those they'll have some local disks we cache all requests there
[2711.42 --> 2720.58]  problem solved we're done that's it worth a try and i'm thinking cdn.gerhardt.io
[2720.58 --> 2727.24]  i even have a name for it not a logo yet but i can ask chat gpt to create me one
[2727.24 --> 2731.74]  what do you think about that well i don't know what it takes to build a cdn
[2731.74 --> 2739.50]  uh i think it in the conversation one of it is streaming logs that is how we have built around
[2739.50 --> 2744.86]  and the question was whether or not if cloudflare had that similar support because the obvious
[2744.86 --> 2751.24]  answer here would be okay for having challenges with fastly and they're aware of this stuff like
[2751.24 --> 2756.74]  we've brought it their attention that we have had challenges multiple times and it's strange to me
[2756.74 --> 2762.64]  because we obviously have such it's not like we're here trying to bad mouth anybody but we do have a
[2762.64 --> 2768.78]  mouthpiece to the developer community and we're we're using the technology to showcase the technology
[2768.78 --> 2776.44]  so it would make sense in my opinion if you had that kind of relationship with such a content
[2776.44 --> 2782.16]  i guess media company is probably the better way to say it that you would want to put some effort
[2782.16 --> 2787.64]  into ensuring that they get the right help to ensure that these problems aren't there and maybe
[2787.64 --> 2791.66]  it's just a fastly thing maybe it's an us thing i don't think it is us because we've seemed to have
[2791.66 --> 2797.26]  exhausted every single possible thing we could do around it and so the obvious next choice would be
[2797.26 --> 2802.84]  okay maybe maybe we're just we're not holding it wrong it's just we can't hold it right and we
[2802.84 --> 2807.60]  can't figure it out because there's no support to hold it right and so we go and talk to cloudflare we
[2807.60 --> 2813.52]  decide to build our own thing and i think it really comes around what does it really take to build a cdn
[2813.52 --> 2818.94]  for the kind of company we have and the kind of content we have that we need to cash globally does
[2818.94 --> 2822.92]  it make sense to build something in the house does it make sense to move to the next key player in the
[2822.92 --> 2827.32]  industry which is cloudflare they've shown desire to work with us we're talking with them it's not
[2827.32 --> 2832.28]  come to full fruition but there's a lot of desire but i don't like to bet on desire necessarily so i
[2832.28 --> 2837.36]  don't want to say there's something happening there but it's definitely on the table to talk about and
[2837.36 --> 2842.58]  they're talking with us we just haven't landed the point of the deal and i think for us we look at
[2842.58 --> 2847.16]  infrastructure partners like this like honeycomb uh like fastly has been like linode has been in
[2847.16 --> 2854.88]  the past like fly is like type senses is we want integrated embedded partners not because that's what
[2854.88 --> 2858.90]  we necessarily want but because we see that's what they get the best benefit of we get the best benefit
[2858.90 --> 2863.66]  because we get to have that deep relationship and that conversation back and forth to improve
[2863.66 --> 2869.16]  and i'm sure if neon succeeds with us and we you know fully migrate our postgres there and we're
[2869.16 --> 2873.44]  super happy with all the things we've been sort of talking about that there's going to be a deep
[2873.44 --> 2877.80]  embedded relationship i've kind of come up with this idea over the over the holidays this embedded
[2877.80 --> 2883.34]  sponsorship is is different than just sort of flying by and throwing some money content and hoping that
[2883.34 --> 2888.62]  you can talk to their audience it's far more of a partnership and embedded and so that's why i go
[2888.62 --> 2894.08]  that route and i think cloudflare has an opportunity to work with us if that works out uh we've given
[2894.08 --> 2900.42]  fastly years to work that out and they haven't done it and that's just a shame i really would love to
[2900.42 --> 2906.48]  have them figure that out i've begged them in email in conversations and i don't mind saying that because
[2906.48 --> 2912.88]  i've i've worked it personally to the to the nth degree that i'm kind of sad and upset that that's
[2912.88 --> 2919.06]  where we're at they are amazing maybe not amazing for us but we've just not gotten the kind of support
[2919.06 --> 2925.92]  we need to get past these challenges over and over and over so i guess my question to you is does it
[2925.92 --> 2931.56]  make sense for us to build our own cdn what does it really take should a small operation like ours
[2931.56 --> 2937.78]  try to do that or does it make sense to go to the goliaths and the behemoths like cloudflare and
[2937.78 --> 2942.78]  fastly like we have done does it should we try something different which we do one thing
[2942.78 --> 2948.12]  which i want to mention here and this is really important is that if we didn't have fly and if
[2948.12 --> 2953.36]  we didn't have the partnership that we have with fly i wouldn't be suggesting this so that's the first
[2953.36 --> 2960.20]  thing the second thing is as crazy as this idea was three years ago when kurt laid it out um you know
[2960.20 --> 2968.04]  having sat on it for years and understanding what we need we're not that complicated as like a
[2968.04 --> 2972.72]  from a technological perspective like our app isn't that complicated and it's
[2972.72 --> 2978.06]  not changing that that much we're not a big team and what that means that our needs are fairly
[2978.06 --> 2983.78]  simple and straightforward which means that some of the big companies they can't really meet them
[2983.78 --> 2989.48]  because they're too big there's too much there there's like a lot of complications that we 99% of
[2989.48 --> 2993.30]  the stuff we don't even care about we don't care whether it's varnish we don't care whether it's
[2993.30 --> 2998.80]  nginx we just care about the experience and the experience is too complicated so i'm sure there's a way
[2998.80 --> 3003.32]  that you know we can make this work but is it worth our time and the answer is no that's what i keep
[3003.32 --> 3008.48]  coming back to what we need is something really simple and we don't have that really simple thing
[3008.48 --> 3014.98]  so even like our config what we need in terms like streaming logs it's such a simple feature that we
[3014.98 --> 3019.94]  that we require and yes sure we can go and start the conversation with someone else but just back to
[3019.94 --> 3024.40]  jared's point it would take him a few hours to explain to someone or to do something for someone
[3024.40 --> 3029.12]  what he could do himself in like five or ten minutes there's like an equivalent there to
[3029.12 --> 3035.46]  what we would need and it's really not that complicated and we're leveraging something someone
[3035.46 --> 3042.84]  like fly which have have come light years in the last three years like they're like light years apart
[3042.84 --> 3048.80]  where they were as an organization as like the services they offer can you gush a bit about that
[3048.80 --> 3053.14]  that light year change just real quick i mean they are a partner they're not sponsoring this message
[3053.14 --> 3058.38]  i'm asking you to say but can you gush a little tiny bit about their improvements because that is
[3058.38 --> 3063.78]  the home of the change of change law.com almost said the change law.com jared accidentally you know fly
[3063.78 --> 3070.30]  is the home of change law.com let me change this question since we went from kubernetes to fly.io
[3070.30 --> 3078.58]  how many issues did we had because of fly.io was postgres a problem for us on fly not really no i mean
[3078.58 --> 3086.30]  we had some issues like minor issues but nothing big nothing of the scale of fastly whenever we like
[3086.30 --> 3090.66]  how many times did we reach out to support and they couldn't help us i can't even count on a hand
[3090.66 --> 3098.64]  i can't exactly fly there you go from a technological perspective the machines the way they work
[3098.64 --> 3104.68]  deploys i mean they just work for us they just kind of like meet our needs exactly where they are
[3104.68 --> 3112.12]  and things are fairly fast it's very easy to spin up new apps i know that not everyone has this amazing
[3112.12 --> 3118.18]  experience with fly but we've served billions of requests in the last two years we're still good
[3118.18 --> 3125.52]  we didn't have anything big or anything bad to say about them i mean i can talk for example why our
[3125.52 --> 3129.66]  dagger on fly has been failing and there's something there's some problems with the wire guard
[3129.66 --> 3136.36]  i mean it's not all great and we can talk about that but that's a very specific use of fly in a very
[3136.36 --> 3141.32]  specific context and it's not their core competency necessarily like their core competency is what they
[3141.32 --> 3146.88]  provide to us it's the edges where they're sort of moving and innovating that still need work which is
[3146.88 --> 3153.30]  part of the course yeah so i mean this basically has to do with uh the fly there's intermittent
[3153.30 --> 3160.56]  flooded io wire guard gateway issues uh when you're connecting for example from ci from github in this
[3160.56 --> 3164.58]  case sometimes that whole setup and it's very difficult to say whether it's fly or whether
[3164.58 --> 3169.50]  it's github or microsoft azure where this runs so it's difficult to say what exactly is happening
[3169.50 --> 3174.14]  which is no that specific combination isn't working well but because we have two of everything
[3174.14 --> 3179.42]  it's okay because we've been falling back to the github runners builds have been a bit slower
[3179.42 --> 3185.62]  uh but they worked so you know deploys were taking 10 minutes rather than and i get the github
[3185.62 --> 3191.68]  action run failed emails when my deploy goes out successfully and i'm like so i just want to like
[3191.68 --> 3197.98]  balance this out and that we have had some issues with fly but not in the path that we really care about
[3197.98 --> 3202.60]  like production hasn't been down because of them and again knock on wood it doesn't happen but
[3202.60 --> 3208.62]  you know it's been good now should we put all our eggs in one basket you know two of everything if
[3208.62 --> 3214.50]  we run everything on fly and the fly goes down we are we're down yeah let me ask a different question
[3214.50 --> 3222.06]  then so if we did decide to build our own cdn like this is one more thing for a small team of
[3222.06 --> 3228.10]  ours to maintain uptime too like what will we be taking on in terms of burden too it's one thing that
[3228.10 --> 3234.20]  we don't have the need for you know let's just say 99 like you said of a cloud flare or fastly feature
[3234.20 --> 3239.18]  set we really only need the the good one percent because our needs are just limited and we don't
[3239.18 --> 3245.32]  have exhaustive needs and we did decide okay let's build our own cdn again eggs in one basket we're
[3245.32 --> 3250.06]  going to build it on fly if we decide to do that but what would it be in terms of like build time
[3250.06 --> 3258.08]  burden to maintain you know if it's down like how do we i mean that seems like a we'd have to like
[3258.08 --> 3263.00]  probably have more of your time i mean i don't know it just seems like we're taking on way more
[3263.00 --> 3268.80]  responsibility because fastly is in front of everything and while there's some challenges
[3268.80 --> 3274.42]  there and there's some misses of frequent of recent we're relying on them to do their job and
[3274.42 --> 3278.50]  they kind of do their job for the most part you know we've had some issues obviously but we would
[3278.50 --> 3285.36]  be taking all that on ourselves does that make sense so let's break it down in terms of like um
[3285.36 --> 3292.24]  the big pieces that we need to get into place we have one new application which is our cdn application
[3292.24 --> 3299.24]  all that is nginx exactly as it's described in kurt's blog we have an nginx config that has all
[3299.24 --> 3307.36]  the rules that currently we are defining in fastly we distribute this app across all the fly regions
[3307.36 --> 3316.60]  maybe not all all of them but most of them so a couple like us west us central us east south americas
[3316.60 --> 3321.92]  a few in europe and all this is like literally run a few commands in fly and you have all these
[3321.92 --> 3330.10]  app instances spun up they're the same config same everywhere we get one dedicated ip it's an anycast ip
[3330.10 --> 3336.04]  again fly feature so regardless where you are you use the same ip that would be cdn.changelog.com
[3336.04 --> 3341.34]  it will hit one of those fly instances if the instance is down i think the way it works
[3341.34 --> 3346.78]  the fly proxy which you're basically hitting the proxy on any of the edge again where you are it
[3346.78 --> 3351.86]  will redirect to running instance and then you have some very small rules which basically tell you what
[3351.86 --> 3356.64]  do you do so let's say that you're serving an mp3 if you don't have the mp3 it will stream it
[3356.64 --> 3361.78]  from wherever it is and will cache it locally so you have some disks attached to every single
[3361.78 --> 3367.10]  nginx instance so that you have like a local ephemeral cache of all the content that's requested
[3367.10 --> 3374.32]  in that region it's just simple config you just add the volume boom you're done that's it i mean
[3374.32 --> 3378.94]  there's not much more i suppose it's like the config for the nginx right so that jared gets the logs
[3378.94 --> 3383.32]  that can't be it what about logs and stuff like that what about the things we need for stats in the
[3383.32 --> 3389.00]  application and logs exactly yeah so nginx logs we'll get them in the format we need to
[3389.00 --> 3394.94]  we'll write them to a disk i mean fly has nats that's how they distribute all the logs i know
[3394.94 --> 3398.54]  that's not always reliable there's like small issues and i know because i've been using this
[3398.54 --> 3403.20]  for another project for like the past year this is for dagger by the way so i know exactly how nats
[3403.20 --> 3409.82]  works how log distribution works in fly and the challenge would be to get those logs reliably
[3409.82 --> 3416.72]  from the nginx instances to s3 i think that's the one thing which is like an unknown in the sense
[3416.72 --> 3422.02]  that i know the limitations of nats which is internal to fly but maybe there's something more
[3422.02 --> 3427.86]  that we can do there we cannot do this without a little bit of fly's help and what i mean by that
[3427.86 --> 3432.44]  we wouldn't want our logs to get lost right fastly has been very reliable as far as i know when it
[3432.44 --> 3436.88]  comes to delivering those logs i know that we can get them in the right format because nginx is super
[3436.88 --> 3444.58]  configurable what i don't know is how reliable will it be to get those logs from fly into s3
[3444.58 --> 3452.32]  one tool that i've used and i love is called vector.dev it's an open source tool very lightweight
[3452.32 --> 3460.08]  written in rust that consumes they're called inputs so it can be anything from like a log file
[3460.08 --> 3465.70]  to standard in standard out whatever it has a couple of sources and then it does transformations
[3465.70 --> 3470.96]  and it has syncs so we could co-locate some of those vector instances right next to nginx they're
[3470.96 --> 3477.22]  super lightweight think megabytes of memory usage hardly any cpu usage and they could distribute those
[3477.22 --> 3483.36]  logs reliably they have backup mechanisms they have all sorts of things so even that i would have an
[3483.36 --> 3493.40]  idea of how to do time-wise we're talking days of my time preach i like it so i think like by the
[3493.40 --> 3499.70]  next kaizen if i set myself to do this this would be done by the next kaizen what about costs i mean
[3499.70 --> 3507.48]  we would have to compare apples to apples of fastly pricing versus fly pricing it looks like it's about
[3507.48 --> 3515.50]  0.02 cents per gigabyte mostly i'm worried about outbound data transfer 100 gigabytes per month free
[3515.50 --> 3524.22]  that's north america and europe and two cents per gigabyte outbound data transfer so i think we would
[3524.22 --> 3533.92]  do some sort of analysis of what we are doing currently on fastly and what that would cost with our own cdn
[3533.92 --> 3542.04]  fly and that would be interesting to compare yeah so if we did let's go five cents per gigabyte
[3542.04 --> 3550.16]  we would still be within our sponsorship account because fly sponsors our infra we would not exceed
[3550.16 --> 3558.14]  our sponsorship limit oh sorry no hang on i may be wrong hang on hang on hang on let me time this
[3558.14 --> 3566.18]  i have an extra times uh maybe would be slightly over slightly over but then we i mean we have a
[3566.18 --> 3571.08]  bunch of redundant info that we can uh shut off maybe we can increase the sponsorship a little bit
[3571.08 --> 3575.58]  or fly can increase the sponsorship a little bit right we can always go back to them with you know a new
[3575.58 --> 3586.10]  cause an idea to say i had an idea i suppose and this may not fly um but i was thinking like the idea
[3586.10 --> 3591.84]  of really simple syndication what if it was a really simple cdn like rscdn like a repo we started
[3591.84 --> 3597.56]  up where you could do the same thing we're going to do if we decided to do this and it became a template
[3597.56 --> 3604.46]  you know via open source as it works yeah called rscdn and it's meant to run on fly and you can spin up
[3604.46 --> 3609.66]  your own really simple cdn essentially and kind of follow our blueprint and i think that that's promotion
[3609.66 --> 3616.20]  for fly that's obviously promotion for open source dog fooding in a way because that's what we're
[3616.20 --> 3623.10]  asking for is like just a really simple cdn don't give us all the extras i mean if we think of it as
[3623.10 --> 3628.78]  an experiment to try out and see how far we can get maybe we can invest a little bit of time and see
[3628.78 --> 3635.60]  will this work i mean we have the blueprint we have a couple of like things which are out there
[3635.60 --> 3642.18]  i think we're relying a lot on on nginx and nginx caching i know as a feature that's one of the
[3642.18 --> 3647.96]  nginx plus features especially managing the cache and visibility into the cache so maybe there's other
[3647.96 --> 3655.12]  tools that are more cdn focused and open source i don't know traffic i know is popular in the cloud
[3655.12 --> 3659.80]  native world as an alternative to nginx i don't know the reasons you probably do but just as an
[3659.80 --> 3665.50]  example like maybe nginx isn't necessarily the solution yeah i'm thinking something battleharden
[3665.50 --> 3670.66]  that has been used for this purpose for many many years even decades at this point and there's only
[3670.66 --> 3677.92]  really three options there's varnish there's nginx or apache apache i would discount because again
[3677.92 --> 3683.78]  i don't want to go into that so it's either varnish or nginx varnish is a beast why don't we just export
[3683.78 --> 3688.30]  our varnish config and just import it into our news thing we've already written the code i mean
[3688.30 --> 3696.44]  i've learned varn i know vcl now i know vcl that might just work really i get lost in those thousands
[3696.44 --> 3702.02]  of lines of stuff that's what makes me think like is this a really simple cdn because when i look at
[3702.02 --> 3706.38]  our varnish config on fastly i think it's actually doing more lifting than we think it's doing but
[3706.38 --> 3711.18]  maybe some of that's a lot of it's generated based on we turn on a few features and they boilerplate
[3711.18 --> 3716.32]  out some stuff but when i start thinking about replacing fastly with anything i go back to that
[3716.32 --> 3721.98]  varnish config and i realize okay i do have and i have more rules that i would like to deploy as we
[3721.98 --> 3728.14]  take plus plus on site and stuff it's going to get more i'm happy to write an nginx config i'm already
[3728.14 --> 3734.54]  writing vcl so i'm not against it i just think like you've used both which one do you prefer this point
[3734.54 --> 3739.96]  well it's tough because i've only ever used varnish through the fastly admin and so it's like
[3739.96 --> 3744.60]  this weird you know thing that you're doing and you're kind of you write it directly but then you
[3744.60 --> 3749.98]  like it exports it to the right place and you gotta like set priorities in order to get the code where
[3749.98 --> 3756.18]  you want it to be and so that's never what i want right and i've written nginx configs like the way i
[3756.18 --> 3761.34]  want to write them in vim or in sublime text so i like nginx better just because i've never actually had
[3761.34 --> 3766.00]  i've never just gone and like downloaded varnish and ran it so it's tough for me to compare but
[3766.00 --> 3772.42]  they're both fine i mean i used to know nginx very well i haven't run it personally for years
[3772.42 --> 3779.22]  but for me nginx configs are pretty straightforward stuff you know yeah you can still screw it up good
[3779.22 --> 3784.98]  and i will say that chat gpt led me astray a couple times on varnish stuff it's gotten it right but also
[3784.98 --> 3789.46]  got it wrong a couple times where i was like nope that's not how you do it i had to learn the hard way
[3789.46 --> 3797.36]  one plus is that chat gpt and all the gpts knows nginx configs very very well so when you're lost
[3797.36 --> 3803.08]  you can be found i know this point all i'm trying to say is that there's a lot of frustration that
[3803.08 --> 3808.44]  has built up over the years it doesn't seem to be getting any better and it's almost like i want to
[3808.44 --> 3813.90]  do something about it and maybe this is not it i mean it's close to me like the heart of a hacker
[3813.90 --> 3820.18]  the hacker has to hack the easy button to me i mean i'd love to do that some sort of hacking i think
[3820.18 --> 3826.06]  i would love to investigate further really what it would take for us because i mean i i love to tinker
[3826.06 --> 3832.02]  just like you do but do we want to hold a cdn forever as our own responsibility that's not really
[3832.02 --> 3836.54]  the business we're trying to be in i think that we are in the business of partnering with great tech
[3836.54 --> 3844.16]  stacks and great infrastructure partners and helping them evolve to fit our needs more so than
[3844.16 --> 3849.90]  us trying to like tinker i mean i would totally tinker with this rscdn kind of idea but i think
[3849.90 --> 3854.90]  in the end of the day i want a great partner as a business you know i want to promote a great partner
[3854.90 --> 3860.58]  to a great developer audience that makes sense for them to try out and and use on their own to me
[3860.58 --> 3868.14]  cloudflare seems like the winner of what we should try next unless you investigate and further
[3868.14 --> 3872.74]  in quote sell us on the idea that this makes sense for us to build and hold ourselves
[3872.74 --> 3877.44]  because if there's legs there then that's kind of cool and maybe that's kind of fun it would put us
[3877.44 --> 3881.72]  more in the fly basket which i'm not against because we can certainly circle back with kurt and the team
[3881.72 --> 3886.40]  there and showcase our ideas and they love that they love the hacker spirit so i can't imagine we would
[3886.40 --> 3892.46]  get turned away with this idea i think my primary concern would be going against the grain in terms
[3892.46 --> 3898.52]  of infrastructure partners and then going against the grain of building out a service that we may not
[3898.52 --> 3904.56]  actually want to manage ourselves but i like the idea of the tinkerer they kind of be it almost be fun
[3904.56 --> 3910.00]  to do just for the fun of it really there's a limp into this as well that we could deploy which is that
[3910.00 --> 3917.72]  we could leave cdn.changelog.com completely alone we have two domains on fastly and then we have
[3917.72 --> 3923.26]  changelog.com which is fronting our app servers and those are two different things inside of fastly
[3923.26 --> 3927.82]  and obviously one has the bulk of the traffic and the other one has way less traffic the feeds is
[3927.82 --> 3933.78]  going to be big but it's it's not even the logs we don't care about as much right like the mp3 download
[3933.78 --> 3938.52]  logs are the ones that we want that's the bulk of the traffic we could leave that alone for now
[3938.52 --> 3943.42]  and tinker with changelog.com which is really just fronting our app servers anyways and has a bunch
[3943.42 --> 3949.22]  of logic like where the feed rewrites are and go to r2 and like there's lots that you could get done
[3949.22 --> 3954.54]  there but it's probably like 20 of the work that it would be if you took them both on at the same time
[3954.54 --> 3959.82]  and said like completely so you could build kind of a a poor man's version of this as a tinker
[3959.82 --> 3965.84]  which maybe takes one day for gear hard versus three or something and we could roll it out and leave cdn
[3965.84 --> 3970.44]  alone and then if it doesn't work to turn it off and go back to what we're doing so i think that's
[3970.44 --> 3976.20]  like a way we could do it with way less risk and probably more fun what about cloudflare jared have
[3976.20 --> 3982.24]  you looked at the logs uh just enough to know that i think that we need the enterprise plan before i can
[3982.24 --> 3987.32]  even play with the features which is kind of weird to me and they don't tease them where i would expect
[3987.32 --> 3993.10]  you know like in the cloudflare ui you expect it to be like here's a feature you can't use hit a button
[3993.10 --> 3997.78]  here but like this feature just doesn't exist over until you get to the docs and they're like oh log
[3997.78 --> 4003.74]  push which seems to be exactly what we need is it just like writes your logs out in real time to r2
[4003.74 --> 4009.38]  right that's the feature we need for for our analytics and then i haven't looked at it for
[4009.38 --> 4014.24]  rewrite rules and all the other stuff we're doing fancy you know how could i recreate the varnish
[4014.24 --> 4019.46]  functionality over in cloudflare i haven't got that far yet because i figured why do it if we're not
[4019.46 --> 4024.88]  sure yet so i'm pretty sure we can get everything done there that we got done and fastly i just don't
[4024.88 --> 4028.52]  know exactly how and but the log push is an enterprise feature which we're just on a standard
[4028.52 --> 4033.20]  plan right now and so i can't even i'm sure we can get that blessed like hey just turn that on for us
[4033.20 --> 4036.46]  yeah i just can't even look at it i haven't even looked at it yet because you just can't
[4036.46 --> 4041.64]  and that's been the main hang-up really because i mean to zoom way way back we wanted to actually
[4041.64 --> 4048.06]  run cloudflare and fastly side by side and i think jared i can't recall remind me why we did or
[4048.06 --> 4053.84]  didn't do that but we had the idea of doing it and it came around that it was we were always unsure
[4053.84 --> 4059.84]  of how to do essentially what log push does which is move those logs streaming to another service so
[4059.84 --> 4064.52]  we can consume them and use them for the stats and whatnot or any blessed way that we could get the
[4064.52 --> 4069.40]  data that we need from cloudflare the first time we looked at it which was probably five years ago now
[4069.40 --> 4072.80]  they just didn't even have it like they had your dashboard and they'll show you what you've done
[4072.80 --> 4076.94]  and that was it like you can't say it yeah but how many requests to this endpoint
[4076.94 --> 4081.58]  did we serve like they just didn't have that kind of stuff back then they seem to have that kind of
[4081.58 --> 4087.32]  stuff now there's other stuff called website analytics which is in beta which has even more
[4087.32 --> 4092.58]  granular data so i think they're like been adding that over time and then the log push service seems
[4092.58 --> 4097.52]  to be exactly what we would be after maybe there's an even easier way that they have that's like this is
[4097.52 --> 4102.04]  the cloudflare way and i haven't i can just ask them that i haven't asked them but the question is
[4102.04 --> 4106.74]  like hey if i wanted to count downloads to an mp3 endpoint like how would i get that done i'm pretty
[4106.74 --> 4111.90]  sure most cloudflare engineers are like oh here's how you do it you know i just haven't asked and maybe
[4111.90 --> 4117.44]  and maybe the answer is you do it with log push okay well we don't have that so that's where that is
[4117.44 --> 4124.78]  but i'll be down tinkering with this uh personalized fly cdn even if it's just for changelog.com
[4124.78 --> 4129.10]  which just fronts our app servers we don't really care about the data we don't need to stream the
[4129.10 --> 4134.02]  logs we just need the rewrites to work so it gets the feeds from the right place on r2 and like
[4134.02 --> 4140.48]  the basics there and if that works great and nothing works out with cloudflare or fastly
[4140.48 --> 4146.48]  and the costs make sense then you just do the other part which is going to be harder but
[4146.48 --> 4150.86]  once you've done the easy part the hard part becomes less hard i think it's worth trying a couple
[4150.86 --> 4155.96]  things i think if cloudflare will work from a certain perspective we should definitely try out
[4155.96 --> 4161.62]  and see how far we can get i think this fly thing has some merit to it at least trying it out and see
[4161.62 --> 4166.06]  again how far we can get maybe we'll come across things that will be blockers like real blockers
[4166.06 --> 4171.02]  or kurt after he hears this he says hey you guys are crazy don't do it
[4171.02 --> 4177.66]  that was a joke yeah actually i wrote that three years ago and i do not believe it anymore
[4177.66 --> 4182.94]  please don't do that yeah that's true you guys are crazy or maybe he's like you guys are crazy i love
[4182.94 --> 4185.04]  it maybe yeah let's do it
[4185.04 --> 4206.64]  what's up friends this episode is brought to you by our friends at neon serverless postgres is exciting
[4206.64 --> 4230.46]  and we're excited and i'm here with nikita shemganoff co-founder and ceo of neon so nikita one thing i'm a firm believer in is when you make a product give them what they want and one thing i know is developers want postgres they want it managed and they want it serverless so you're on the front lines tell me what you're hearing from developers what are you hearing from developers about postgres managed and being serverless
[4230.46 --> 4260.44]  so what we hear from developers is the first part resonates absolutely they want postgres they want it managed the serverless bit is 100 resonating with what people want they sometimes are skeptical like is my workload going to run well on your serverless offering are you going to charge me 10 times as much for serverless that i'm getting for provision those are like the skepticism that we're seeing and then people are trying and they're seeing that the bill arriving at the end of the month and like whoa this
[4260.44 --> 4290.14]  is strictly better the other thing is the other thing is the other thing is the other thing is the other thing that is resonating incredibly well is participating in the software development lifecycle what that means is you use databases in two modes one mode is you're running your app and the other mode is you're building your app and then you go and switch between the two all the time because you are you know you're deploying all the time and there is a specific you know part when you just like building out your application
[4290.44 --> 4318.44]  from zero to one from zero to one and then you push the application into production and then you push the application into production and then you keep iterating on the application what databases on amazon such as rds and aurora and other hyperscalers are pretty good at is running the app they've been at it for a while they've learned how to be reliable over time and they run massive fleets right now like aurora and rds run massive fleets of databases so they're pretty good at it now they're not serverless
[4318.44 --> 4348.44]  now they're not serverless at least they're not serverless by default aurora has a serverless offering it doesn't scale to zero neon does but that's really the difference but they have no say in the software development lifecycle so when you think about what a modern deploy to production looks like it's typically some sort of tie-in into github right you're creating a branch and then you're developing your feature and then you're setting your pr
[4348.44 --> 4378.12]  and then you're on github actions or you're running github for ci cd and eventually this whole thing drops into a deploy into production so databases are terrible at this today and neon is charging full speed into participating in the software development lifecycle world what that looks like is neon supports branches so that's the enabling feature git supports branches neon supports branches internally because we built neon we built our
[4378.12 --> 4407.76]  you know your own proprietary you know your own proprietary you know your own proprietary you know your own proprietary proprietary you know your own proprietary proprietary is built in house you know the technology is actually open source but it's built in house to support copy and write branching for the postgres database and we run and manage that storage subsystem ourselves in the cloud anybody can read it you know it's all in github under neon database repo and it's quite popular there are like over 10 000 stars on it and stuff like that this is the enabling technology it supports branches the moment it supports branches
[4407.76 --> 4437.74]  it's trivial to take your production environment and clone it and now you have a developer environment and because it's serverless you're not cloning something that costs you a lot of money and imagining for a second that every developer cloned something that costs you a lot of money in a large team that is unthinkable right because you will have 100 copies of a very expensive production database but because it is copy and write and compute is scalable so now 100 copies that you're not using you're only using them for development they actually don't cost
[4437.74 --> 4467.72]  you that much and so now you can't cost you that much and so now you can arrive into the world where your database participates in the software development life cycle and every developer can have a copy of your production environment for their testing for their feature development we're getting a lot of feature requests by the way there people want to merge this data or at least schema back in into production people want to mask PII data people want to reset branches to a particular point in time of the parent branch or the production branch or the current
[4467.74 --> 4496.74]  the current in time like against the head of the current in time like against the head of that branch and we're super excited about this we're super excited we're super optimistic all our top customers use branches every day I think it's what makes neon modern it turns a database into a URL and it turns that URL to a similar URL to that of GitHub you know you can send this URL to a friend you can branch it you can create a preview environment you can have dev test staging and you live in this iterative mode of building applications
[4496.74 --> 4497.74]  okay go to neon.com
[4497.74 --> 4503.74]  okay go to neon.tech to learn more and get started get on-demand scalability bottomless storage and data branching one more time that's neon.tech
[4503.74 --> 4510.74]  I mean I think to be honest I think fly should have a CDN because I think that's one of the first things that are fairly easy to run as a distributed systems worldwide because the state is decoupled.com
[4510.74 --> 4517.74]  it's the simplest use case right yeah so if fly invests in something next I think a CDN should be it
[4517.74 --> 4538.74]  I mean I think to be honest I think fly should have a CDN because I think that's one of the first things that are fairly easy to run as a distributed systems worldwide because the state is decoupled it's the simplest use case right yeah so if fly invests in something next I think a CDN should be it
[4538.74 --> 4544.74]  the thing which we haven't talked about maybe we should is super base on the fly
[4544.74 --> 4556.74]  oh yeah because that popped up just recently after we were already starting with neon I mean we wanted managed postgres for a while and they weren't doing anything about it and so we're like well let's go talk to neon and then tell them the rest Gerhard
[4556.74 --> 4562.74]  there is a super base postgres on fly.io it's in the fly docs I think this was in December 13th or something like that yeah it was fairly recent super base partnered with fly.io to offer a fully managed postgres database on the fly.io infrastructure and low latency I mean it's just like right there in the intro I think that makes a lot of sense so yeah I think it was like bad timing I suppose in a certain or good timing depending on how you look at it but it's just like
[4562.74 --> 4566.74]  I think the neon I think I really want to see that through but it's interesting to see something like postgres in the future
[4566.74 --> 4568.74]  I think that was in December 13th or something like that yeah it was fairly recent
[4568.74 --> 4572.74]  super base partnered with fly.io to offer a fully managed postgres database on the fly.io infrastructure
[4572.74 --> 4578.74]  and low latency I mean just just like right there in the intro I think that makes a lot of sense so
[4578.74 --> 4590.74]  yeah I think it was like bad timing I suppose in a certain or good timing depending on how you look at it I think the neon I think I really want to see that through but it's interesting to see something like postgres
[4590.74 --> 4592.84]  But it's interesting to see something like Postgres
[4592.84 --> 4595.28]  appearing on fly as a managed service through partnership.
[4595.62 --> 4598.54]  So I'm wondering, maybe a CDN is next.
[4598.72 --> 4599.80]  And this is my wishful thinking.
[4600.20 --> 4600.48]  Yeah, maybe.
[4601.06 --> 4602.52]  It's definitely an obvious move.
[4602.60 --> 4605.30]  I mean, it's not obvious that they would partner with Superbase.
[4605.44 --> 4608.06]  I think that for me was kind of a pleasant surprise.
[4608.16 --> 4608.66]  It makes sense.
[4608.76 --> 4611.12]  It's like, oh yeah, this is like a great partnership.
[4611.26 --> 4614.84]  I think both companies are very impressive and aligned in that way.
[4614.84 --> 4615.84]  And it benefits both.
[4616.12 --> 4617.96]  So I thought it was a good idea.
[4618.56 --> 4620.28]  Obviously, I felt like it was late to the game
[4620.28 --> 4623.46]  because we had been wanting managed Postgres for a long time on fly.
[4623.72 --> 4625.52]  So much so that we made a different move.
[4626.06 --> 4626.60]  That's right.
[4626.82 --> 4630.66]  And still interested in maybe trying and comparing the two.
[4630.74 --> 4634.08]  Obviously, depending on how tightly Superbase is integrated
[4634.08 --> 4635.22]  into fly's infrastructure,
[4635.84 --> 4638.20]  I expect them to have that advantage in terms of performance.
[4639.46 --> 4644.14]  Yeah, maybe they go out and find a CDN-focused upstart
[4644.14 --> 4646.50]  that could integrate into fly.
[4646.70 --> 4647.14]  I don't know, maybe.
[4647.66 --> 4649.32]  I mean, if I was to pick a CDN,
[4649.32 --> 4650.46]  and I haven't tried them,
[4650.58 --> 4652.24]  but I did a bit of research,
[4652.88 --> 4654.58]  Key CDN looked interesting.
[4655.36 --> 4656.74]  And not because it's based in Switzerland.
[4656.88 --> 4657.88]  That has nothing to do with it.
[4659.04 --> 4660.58]  But there's that as well.
[4661.50 --> 4662.64]  So Key CDN.
[4662.70 --> 4663.68]  It was real fast for you.
[4663.90 --> 4664.50]  Real close.
[4664.72 --> 4664.94]  Yeah.
[4665.16 --> 4666.02]  One of your favorite places.
[4666.44 --> 4666.62]  Yeah.
[4666.62 --> 4668.96]  I haven't shopped CDNs for a long time.
[4669.30 --> 4673.46]  I just have been happy for the most part until October the 8th.
[4673.78 --> 4674.14]  Yeah.
[4674.86 --> 4676.32]  It's almost like a yearly thing.
[4676.46 --> 4678.28]  Like every year something like that happens,
[4678.34 --> 4679.92]  and then we spend a few days with support,
[4679.96 --> 4680.72]  and we get nowhere.
[4681.06 --> 4682.70]  I end up going in circles and saying,
[4682.76 --> 4683.06]  you know what?
[4683.18 --> 4684.54]  Like, flip the table.
[4684.66 --> 4685.40]  I build my own.
[4685.76 --> 4687.16]  And then I calm down.
[4687.42 --> 4687.92]  And then you're like,
[4688.00 --> 4689.68]  I don't really want to build my own.
[4689.98 --> 4690.28]  Yeah.
[4690.28 --> 4690.68]  Yes.
[4690.90 --> 4691.60]  Yes, we should.
[4691.92 --> 4692.66]  Here we are like,
[4692.74 --> 4693.64]  yes, you should, Gerard.
[4693.72 --> 4694.26]  You should build.
[4694.48 --> 4696.28]  This is like the third time this thing has happened
[4696.28 --> 4698.08]  over like the last couple of years.
[4698.18 --> 4699.96]  So I think there's something there.
[4700.08 --> 4701.36]  And it will happen again, I'm sure.
[4701.82 --> 4702.64]  Just a matter of time.
[4702.92 --> 4704.28]  I guess just a later one more on.
[4704.40 --> 4705.92]  Like, thank you, James A. Rosen,
[4706.04 --> 4706.90]  for helping us out.
[4706.94 --> 4710.16]  But to have to reach out to an ex-Fastly person,
[4710.24 --> 4711.86]  or for them to actually reach out to us,
[4712.30 --> 4713.30]  probably with like,
[4713.38 --> 4715.06]  oh my gosh, you guys are feeling so much pain.
[4715.06 --> 4717.06]  I just need to step in and help you all.
[4717.58 --> 4719.90]  That is just not cool.
[4720.28 --> 4720.52]  Really?
[4720.98 --> 4721.42]  That's not great.
[4721.56 --> 4725.02]  But did you know that Vercel Postgres is powered by Neon?
[4725.52 --> 4725.94]  No.
[4726.12 --> 4726.82]  Is this an advertisement?
[4727.40 --> 4727.84]  No.
[4728.62 --> 4729.82]  It just sounded like that.
[4729.90 --> 4731.46]  Did you know that Vercel Postgres,
[4731.70 --> 4733.18]  is this a product placement?
[4733.50 --> 4734.04]  Or is it jingle?
[4734.50 --> 4734.68]  Yeah.
[4735.48 --> 4737.32]  Well, the reason why I say that
[4737.32 --> 4738.16]  is because, you know,
[4738.22 --> 4740.08]  SuitBase is available on Fly.
[4740.90 --> 4742.96]  And like, it just makes sense to say,
[4742.96 --> 4744.18]  well, maybe Neon at some point
[4744.18 --> 4746.40]  will be also available on Fly.
[4746.60 --> 4749.40]  Yeah, that might be to Fly's advantage to do that, right?
[4749.60 --> 4749.84]  Right.
[4749.84 --> 4750.76]  It makes sense.
[4751.00 --> 4752.56]  And, you know, but at the same time,
[4753.12 --> 4755.30]  I've had this back of the head thought
[4755.30 --> 4758.92]  that maybe Neon will be acquired by Vercel.
[4759.18 --> 4759.44]  Yeah.
[4759.78 --> 4761.90]  Are they the only database provider on Vercel now?
[4762.26 --> 4764.76]  Well, Vercel Postgres is Neon.
[4765.44 --> 4768.10]  So Postgres on Vercel is Neon.
[4768.64 --> 4769.52]  You don't need an account.
[4769.76 --> 4770.74]  I'm just reading from their docs.
[4770.80 --> 4772.10]  I'm not at all advertising.
[4772.78 --> 4775.54]  It is not SOC 2, Type 2 compliant.
[4775.88 --> 4776.46]  Coming soon.
[4776.82 --> 4777.82]  I'm just reading from their docs.
[4779.62 --> 4780.90]  But it just makes me think, like,
[4781.12 --> 4783.38]  maybe Neon will be acquired at some point.
[4783.44 --> 4784.44]  I don't think so.
[4784.50 --> 4785.92]  But it just gave me this feeling,
[4785.98 --> 4787.60]  because when I talked to Nikita
[4787.60 --> 4789.06]  for these ad spots we did with them,
[4789.12 --> 4790.10]  which was sponsored,
[4790.76 --> 4791.46]  it was really,
[4791.70 --> 4793.86]  his perspective was around the JavaScript developer,
[4793.86 --> 4795.78]  and you never bet against JavaScript,
[4795.90 --> 4796.98]  this idea that he had said.
[4797.64 --> 4798.98]  And, you know, they're quite embedded.
[4799.10 --> 4800.42]  I just wonder if there's, like,
[4801.04 --> 4801.86]  fruits there happening
[4801.86 --> 4804.22]  where eventually they might get acquired by them.
[4804.64 --> 4805.06]  I don't know,
[4805.12 --> 4808.26]  because Vercel is such an acquisition behemoth these days.
[4808.38 --> 4809.84]  Like, they're acquiring a lot of different stuff.
[4810.28 --> 4812.54]  And just a thought there.
[4812.62 --> 4814.26]  But maybe at the same time,
[4814.28 --> 4818.96]  we can expect to have a Neon Postgres inside of Fly,
[4818.96 --> 4821.92]  where we just basically have the same great features we love
[4821.92 --> 4823.44]  that we're thinking we'll love,
[4823.44 --> 4825.38]  with dev mode and whatnot,
[4825.50 --> 4827.28]  and branching and copy on writing
[4827.28 --> 4828.46]  and all the fun stuff they provide.
[4828.60 --> 4829.16]  Maybe it's just like,
[4829.28 --> 4831.36]  well, now it's just network latency's gone.
[4831.58 --> 4832.52]  It's just not there anymore,
[4832.56 --> 4834.66]  because it's within the fly infra.
[4834.98 --> 4836.56]  And that's going to be a good thing for us.
[4837.04 --> 4837.98]  The good thing is, really,
[4838.08 --> 4839.18]  is that we have choice, right?
[4839.18 --> 4840.44]  We have so much choice as developers,
[4841.00 --> 4842.42]  and that really is the fun part of it, right?
[4842.56 --> 4843.92]  There is a lot of choices here.
[4844.00 --> 4845.44]  It's almost the paradox of choice.
[4845.44 --> 4847.74]  Yeah, paradox of choice in the green scheme.
[4847.96 --> 4849.38]  We'll end up doing nothing again.
[4849.60 --> 4850.78]  Like, eh, we didn't do anything.
[4850.98 --> 4851.50]  Build your own.
[4851.96 --> 4852.98]  There's 14 choices.
[4853.44 --> 4855.46]  It's not the right one.
[4855.78 --> 4858.26]  There'll be 15 choices now, 15 standards.
[4858.66 --> 4860.80]  We'll release our open source CDN,
[4860.92 --> 4862.32]  and there'll be 15 of them, right?
[4862.56 --> 4862.76]  Yeah.
[4863.20 --> 4865.48]  So I kept one more thing as last.
[4865.74 --> 4866.52]  All right, one more thing.
[4866.52 --> 4867.30]  This is almost like an Easter egg.
[4867.58 --> 4868.50]  It's not Easter yet,
[4868.94 --> 4870.46]  and it won't be Easter next time we record,
[4870.52 --> 4871.46]  I don't think, but still.
[4874.04 --> 4875.94]  Part of the pull request 492,
[4876.06 --> 4878.70]  I snuck something in that I wanted to have for ages.
[4879.06 --> 4879.80]  Oh my goodness.
[4879.94 --> 4880.74]  Did I notice it?
[4880.84 --> 4881.20]  I don't know.
[4881.38 --> 4881.96]  Let's have a look.
[4882.04 --> 4882.92]  This is a test.
[4882.92 --> 4888.60]  See if you can notice a feature which I snuck in pull request 492.
[4888.94 --> 4889.22]  Okay.
[4889.54 --> 4891.62]  I'm now switched to the file changes tab.
[4891.70 --> 4893.04]  I'm going to just scroll through the file.
[4893.24 --> 4895.04]  Is that where I'll find it probably snuck in?
[4895.10 --> 4896.88]  It's just some sort of file change here.
[4896.88 --> 4897.92]  I think it's actually,
[4898.04 --> 4900.00]  if you look at the pull request of the conversation,
[4900.16 --> 4901.48]  it's actually the second comment.
[4901.56 --> 4902.26]  Actually, it's the comment,
[4902.32 --> 4905.12]  the first comment which I've made after the description.
[4905.12 --> 4907.72]  Don't give me all these hints, man.
[4907.80 --> 4908.74]  Yeah, too easy.
[4909.08 --> 4910.00]  That was for Adam.
[4910.94 --> 4912.30]  You keep looking at the code, Jared.
[4912.40 --> 4912.78]  It's okay.
[4912.84 --> 4913.90]  Let's see who gets there first.
[4913.90 --> 4916.32]  Is it this video?
[4916.32 --> 4919.28]  No, that's actually a surprise.
[4919.28 --> 4920.28]  It's okay.
[4920.28 --> 4920.62]  It's okay.
[4920.62 --> 4923.06]  The auto scaling slider works in Neon,
[4923.16 --> 4924.66]  which is very counterintuitive.
[4924.82 --> 4926.68]  So I left that gotcha there.
[4926.76 --> 4928.96]  And I've gave support to their product team about,
[4929.16 --> 4930.80]  you know, how that could be improved.
[4931.14 --> 4931.96]  Is it 1Password?
[4932.14 --> 4932.42]  Yes.
[4932.88 --> 4934.36]  Oh, I'm glad you mentioned that because,
[4934.46 --> 4936.88]  you know, I love 1Password.
[4937.02 --> 4938.28]  And you're doing more with this.
[4938.40 --> 4939.30]  What's happening here?
[4939.56 --> 4940.12]  What's this about?
[4940.12 --> 4941.56]  So in a nutshell,
[4942.16 --> 4945.04]  our application needs a single secret now.
[4945.34 --> 4946.38]  Shh, don't tell them.
[4946.74 --> 4949.96]  OP underscore service underscore accounts
[4949.96 --> 4951.04]  underscore token.
[4951.42 --> 4952.12]  Single secret.
[4952.68 --> 4954.10]  And during boot,
[4954.60 --> 4956.38]  the application uses the OP,
[4956.98 --> 4958.26]  the 1Password CLI,
[4958.64 --> 4961.76]  to inject all the secrets that it needs at boot time.
[4962.12 --> 4965.52]  So it pulls them down from the 1Password vault
[4965.52 --> 4966.72]  when it boots.
[4966.72 --> 4969.78]  And is that hosted by like 1Password cloud?
[4969.78 --> 4970.76]  Or where's it vault?
[4970.94 --> 4971.34]  Correct.
[4971.80 --> 4973.34]  That's all 1Password cloud, yes.
[4973.64 --> 4973.90]  Okay.
[4974.52 --> 4977.24]  And so we don't have any additional infrastructure for that.
[4977.38 --> 4978.38]  Nothing additional, no.
[4979.14 --> 4980.94]  Spell it out for us really detailed.
[4981.04 --> 4981.76]  Why is this cool?
[4982.28 --> 4983.62]  I mean, I think I understand why it's cool,
[4983.66 --> 4984.16]  but spell it out.
[4984.26 --> 4985.24]  We have a single secret
[4985.24 --> 4986.76]  that gives the app access
[4986.76 --> 4988.18]  to all the secrets that it needs.
[4988.30 --> 4991.04]  And there's a dedicated vault for that app.
[4991.54 --> 4992.76]  What that means is that that secret
[4992.76 --> 4995.38]  only allows the app to access
[4995.78 --> 4997.42]  just-in-time secrets when it boots.
[4997.52 --> 4998.50]  We don't write them anywhere.
[4998.70 --> 4999.74]  We could, but we don't.
[4999.98 --> 5000.82]  It's all in memory.
[5001.00 --> 5001.92]  When the app boots,
[5002.00 --> 5003.74]  it has access, boom, it pulls them down.
[5004.34 --> 5006.10]  The secrets never leave 1Password
[5006.10 --> 5007.88]  apart from loading into the app's memory.
[5008.22 --> 5009.30]  We don't configure them in Fly,
[5009.42 --> 5011.12]  which is what was happening before, right?
[5011.16 --> 5012.80]  Every single secret the app needs,
[5012.84 --> 5013.70]  we configure it in Fly.
[5013.78 --> 5015.26]  Remember how we rotated secrets, Jared?
[5015.66 --> 5016.28]  That's a pain.
[5016.84 --> 5017.82]  So that process,
[5017.92 --> 5019.30]  we no longer have to do anymore
[5019.30 --> 5021.14]  because if you want to update a secret,
[5021.58 --> 5022.88]  you update it 1Password,
[5022.88 --> 5024.24]  you restart the app,
[5024.58 --> 5024.92]  and boom,
[5025.36 --> 5026.00]  at boot time,
[5026.00 --> 5027.42]  the app picks up the new secret.
[5027.92 --> 5028.38]  That's it.
[5028.72 --> 5030.46]  Does 1Password Vault
[5030.46 --> 5031.98]  have some sort of a web hook
[5031.98 --> 5032.70]  or something
[5032.70 --> 5034.58]  that they could trigger?
[5034.98 --> 5035.48]  Because then you just
[5035.48 --> 5036.88]  take step two out,
[5037.14 --> 5037.40]  you know?
[5037.44 --> 5038.06]  That's what I want.
[5038.26 --> 5038.50]  Yeah.
[5038.78 --> 5040.08]  Just let the app restart itself.
[5040.34 --> 5041.28]  Like reboot my app
[5041.28 --> 5042.64]  when I add a secret kind of thing?
[5042.74 --> 5043.72]  We don't step one,
[5044.16 --> 5045.90]  so please continue being excited
[5045.90 --> 5046.66]  for step one
[5046.66 --> 5049.08]  before we talk about step two.
[5049.60 --> 5050.44]  Don't you love how
[5050.44 --> 5051.76]  I'm never satisfied by you?
[5051.82 --> 5052.30]  I'm like, no,
[5052.48 --> 5053.04]  not cool.
[5053.16 --> 5053.80]  This would be cooler.
[5054.02 --> 5055.20]  You and every other developer.
[5055.64 --> 5057.10]  That's why we keep kaizening this.
[5057.18 --> 5058.18]  It never gets old.
[5058.58 --> 5058.92]  It just gets getting better.
[5058.92 --> 5059.68]  You know what would be cool
[5059.68 --> 5060.50]  if we prove this?
[5060.50 --> 5060.74]  Right.
[5061.26 --> 5062.18]  And before you know it.
[5062.60 --> 5063.04]  Gerhard's like,
[5063.08 --> 5064.16]  can you just appreciate this
[5064.16 --> 5064.72]  for a second
[5064.72 --> 5065.84]  before you ask for more?
[5066.56 --> 5067.38]  That's cool, Gerhard.
[5067.50 --> 5068.14]  I'm loving this.
[5068.34 --> 5068.98]  I'm loving this.
[5069.14 --> 5070.46]  And it hasn't even emerged yet,
[5070.56 --> 5071.38]  so again,
[5071.56 --> 5072.86]  let's merge it first.
[5072.86 --> 5073.86]  Let's start using it.
[5074.20 --> 5074.96]  Let's get it merged.
[5075.30 --> 5075.64]  Okay.
[5075.84 --> 5076.78]  That's a nice Easter egg.
[5077.18 --> 5077.84]  Well, he did ask
[5077.84 --> 5079.10]  if this covered all the secrets
[5079.10 --> 5080.00]  and you said it looks correct,
[5080.08 --> 5080.76]  so I think that's all
[5080.76 --> 5082.24]  we needed to worry about in there.
[5082.44 --> 5083.08]  That is kind of cool.
[5083.18 --> 5084.22]  So the cooler thing,
[5084.26 --> 5084.66]  I think,
[5084.66 --> 5085.80]  is that it's limited.
[5086.22 --> 5087.64]  Even if it could somehow leak,
[5087.64 --> 5088.74]  it's only the secrets
[5088.74 --> 5090.10]  that we store in one password
[5090.10 --> 5090.84]  for that vault
[5090.84 --> 5091.94]  for the infra, right?
[5092.04 --> 5093.60]  So there's a barrier.
[5093.70 --> 5094.20]  There's a perimeter
[5094.20 --> 5095.86]  to its touch point of secrets.
[5096.52 --> 5096.72]  That's it.
[5097.12 --> 5097.84]  And if this was leaked,
[5098.18 --> 5098.34]  yeah,
[5098.74 --> 5100.48]  rotate the service token.
[5100.76 --> 5101.44]  Basically rotate
[5101.44 --> 5102.48]  all the secrets in the vault
[5102.48 --> 5103.40]  and we're good.
[5104.34 --> 5104.62]  Again,
[5104.66 --> 5105.06]  that would be like
[5105.06 --> 5106.00]  a step number three
[5106.00 --> 5107.10]  where could we automatically
[5107.10 --> 5108.30]  rotate all the secrets
[5108.30 --> 5108.92]  that were leaked
[5108.92 --> 5109.80]  from one password?
[5110.18 --> 5110.92]  And that's almost like
[5110.92 --> 5111.96]  a one password request.
[5112.30 --> 5112.36]  Yeah.
[5112.82 --> 5114.14]  This is where I also say
[5114.14 --> 5115.28]  that we're working with
[5115.28 --> 5116.58]  one password behind the scenes
[5116.58 --> 5119.24]  to make this embedded partnership
[5119.24 --> 5120.32]  more apparent as well.
[5120.40 --> 5121.88]  We were using this tech.
[5121.94 --> 5122.80]  We're paying for this tech.
[5123.12 --> 5124.30]  We're not promoting it
[5124.30 --> 5125.36]  because they're paying us.
[5125.36 --> 5127.48]  And we're actually pursuing them
[5127.48 --> 5128.84]  to pay us.
[5129.14 --> 5130.38]  Not so they can keep promoting it,
[5130.42 --> 5131.28]  but we love it so much.
[5131.38 --> 5132.44]  And we love to work with them
[5132.44 --> 5133.80]  to share more of this story
[5133.80 --> 5134.46]  on the inside
[5134.46 --> 5136.00]  and maybe even have,
[5136.10 --> 5136.36]  you know,
[5136.38 --> 5137.10]  that relationship
[5137.10 --> 5137.64]  where we're,
[5138.04 --> 5138.08]  hey,
[5138.10 --> 5139.14]  this is how we're using it.
[5139.32 --> 5140.58]  And Jerry's response was,
[5140.66 --> 5141.44]  could there be a web hook?
[5141.48 --> 5142.16]  And maybe they're like,
[5142.44 --> 5142.68]  yes,
[5142.70 --> 5143.68]  there could be a web hook.
[5144.24 --> 5144.94]  Reminds me of this book
[5144.94 --> 5145.58]  I read my kids.
[5145.66 --> 5146.02]  But anyways,
[5146.50 --> 5147.22]  that's cool.
[5147.38 --> 5148.36]  So hopefully we can get
[5148.36 --> 5149.16]  a one password sponsorship
[5149.16 --> 5149.64]  here soon
[5149.64 --> 5151.10]  because of just how we keep
[5151.10 --> 5151.70]  using it
[5151.70 --> 5153.00]  and improving it
[5153.00 --> 5154.30]  in terms of our infrastructure.
[5154.46 --> 5154.88]  That's awesome.
[5155.00 --> 5155.48]  I love that.
[5155.96 --> 5156.76]  Been using one password
[5156.76 --> 5157.76]  since the dawn of time,
[5157.82 --> 5158.18]  basically.
[5158.92 --> 5159.56]  I just adore it.
[5159.66 --> 5160.04]  It's awesome.
[5160.70 --> 5161.62]  So does fly secrets
[5161.62 --> 5162.96]  then go by the wayside?
[5163.20 --> 5163.96]  Pretty much, yeah.
[5164.16 --> 5164.68]  The only secret
[5164.68 --> 5165.40]  which we set
[5165.40 --> 5167.14]  is this one password token,
[5167.56 --> 5168.14]  service token,
[5168.28 --> 5170.12]  and then the one password CLI
[5170.12 --> 5170.84]  loads all the secrets
[5170.84 --> 5171.98]  directly from one password.
[5172.44 --> 5173.20]  So when I want to add
[5173.20 --> 5173.76]  a new secret,
[5173.88 --> 5174.66]  let's say I integrate
[5174.66 --> 5175.40]  a new service,
[5175.80 --> 5176.48]  I go add it
[5176.48 --> 5177.62]  to the one password vault
[5177.62 --> 5179.56]  and then I go restart the app.
[5179.90 --> 5180.88]  I push the code
[5180.88 --> 5182.18]  that references it
[5182.18 --> 5182.82]  and by the time
[5182.82 --> 5183.54]  the thing boots up,
[5183.56 --> 5184.46]  it's going to have access to it.
[5184.50 --> 5185.22]  That's pretty cool, man.
[5185.24 --> 5185.62]  I love it.
[5185.84 --> 5185.98]  Yeah.
[5186.30 --> 5187.36]  There's still a file there.
[5187.50 --> 5190.76]  There is the env.op file
[5190.76 --> 5191.86]  where we put
[5191.86 --> 5192.84]  what secrets you want.
[5193.30 --> 5194.52]  That's part of the pull request.
[5194.86 --> 5195.66]  I'll add it to there.
[5195.86 --> 5196.22]  Exactly.
[5196.66 --> 5197.58]  Because that's what gets it
[5197.58 --> 5198.20]  in the environment,
[5198.30 --> 5199.12]  in the app's environment,
[5199.60 --> 5200.30]  just in time
[5200.30 --> 5201.02]  when the app boots.
[5201.24 --> 5201.56]  Okay.
[5201.68 --> 5202.44]  What about dev?
[5202.50 --> 5203.10]  Are we still using
[5203.10 --> 5204.24]  der env for dev?
[5204.54 --> 5205.22]  So yes.
[5205.28 --> 5205.88]  So for example,
[5205.88 --> 5206.66]  part of this,
[5206.84 --> 5208.88]  I have an envarc.op
[5208.88 --> 5211.14]  and basically that one
[5211.14 --> 5212.30]  I template just in time,
[5212.38 --> 5213.00]  which does exactly
[5213.00 --> 5213.76]  the same thing.
[5214.10 --> 5215.20]  But in this case,
[5215.26 --> 5216.92]  I write it locally
[5216.92 --> 5218.08]  to my file.
[5218.12 --> 5218.84]  I wouldn't need to.
[5219.06 --> 5219.92]  I could, for example,
[5220.04 --> 5221.52]  run op every single time,
[5221.74 --> 5222.40]  the one password,
[5222.68 --> 5223.72]  to load them in the env,
[5223.94 --> 5224.80]  but I don't do that.
[5225.10 --> 5225.84]  But it's an option.
[5226.26 --> 5226.76]  Say that again
[5226.76 --> 5227.44]  in different words.
[5227.90 --> 5228.48]  Right now,
[5228.90 --> 5229.90]  if you wanted to
[5229.90 --> 5231.62]  use this in dev,
[5232.08 --> 5232.98]  you would need
[5232.98 --> 5234.80]  to run the command locally
[5234.80 --> 5236.04]  to read the...
[5236.04 --> 5237.00]  The op command.
[5237.26 --> 5237.70]  Exactly.
[5238.12 --> 5238.68]  So like to read
[5238.68 --> 5240.12]  the env.op file
[5240.12 --> 5241.68]  and maybe template it,
[5241.78 --> 5242.88]  like maybe write it
[5242.88 --> 5243.38]  to a disk
[5243.38 --> 5244.44]  or load it
[5244.44 --> 5245.14]  in your environment
[5245.14 --> 5245.66]  so you'd need
[5245.66 --> 5246.44]  to run things
[5246.44 --> 5248.36]  through the op CLI.
[5248.64 --> 5249.30]  Can I continue
[5249.30 --> 5250.20]  to ignore that
[5250.20 --> 5251.06]  and just use
[5251.06 --> 5252.26]  my der env
[5252.26 --> 5253.54]  as I have been?
[5254.06 --> 5255.00]  Because my secrets
[5255.00 --> 5255.82]  obviously in dev
[5255.82 --> 5256.58]  are going to be different
[5256.58 --> 5257.20]  than the secrets
[5257.20 --> 5258.16]  in prod anyways.
[5258.38 --> 5259.00]  You could, yes.
[5259.38 --> 5260.08]  What I really want to know
[5260.08 --> 5261.14]  is when this gets merged,
[5261.26 --> 5262.38]  is my setup going to be
[5262.38 --> 5263.48]  hosed or not?
[5264.04 --> 5265.12]  Oh, you have no secrets.
[5265.12 --> 5266.10]  No, we shouldn't
[5266.10 --> 5267.18]  because this just
[5267.18 --> 5268.26]  configures it for prods.
[5268.28 --> 5268.94]  So whatever you're doing
[5268.94 --> 5269.84]  in development...
[5269.84 --> 5270.60]  This is additional.
[5270.96 --> 5271.74]  Additional, yes.
[5271.88 --> 5272.10]  Gotcha.
[5272.22 --> 5272.72]  I could use it
[5272.72 --> 5273.78]  if I wanted to in dev,
[5273.84 --> 5274.52]  but I don't have to.
[5274.74 --> 5275.04]  Correct.
[5275.96 --> 5276.32]  Sweet.
[5276.88 --> 5277.28]  Cool.
[5277.80 --> 5278.16]  Awesome.
[5278.36 --> 5278.82]  That's awesome.
[5279.18 --> 5279.76]  Anything else?
[5279.82 --> 5280.50]  I feel like that was
[5280.50 --> 5281.66]  the coup de grace.
[5282.40 --> 5283.36]  The Easter egg.
[5283.58 --> 5284.44]  That's why I left it last.
[5285.18 --> 5285.84]  That was it.
[5286.54 --> 5286.90]  Awesome.
[5288.22 --> 5289.32]  So my question is
[5289.32 --> 5290.62]  do we build a CDN or not?
[5290.96 --> 5291.82]  That's what I want to know.
[5292.28 --> 5292.50]  It's always,
[5292.60 --> 5293.30]  that's like a title.
[5293.44 --> 5294.58]  Let's build a CDN.
[5294.58 --> 5295.84]  That might be a show title
[5295.84 --> 5296.40]  right there.
[5296.52 --> 5297.74]  Yeah, that's the show title.
[5298.80 --> 5299.12]  Kaizen.
[5299.82 --> 5300.92]  Kaizen, build a CDN?
[5301.26 --> 5303.74]  Yeah, I like that.
[5304.66 --> 5306.12]  To be determined, I think.
[5306.46 --> 5307.32]  Well, let's tinker.
[5307.66 --> 5308.64]  I think that's the answer.
[5308.80 --> 5309.24]  Let's tinker.
[5309.56 --> 5310.04]  I like it.
[5310.18 --> 5310.98]  And we'll talk about it
[5310.98 --> 5311.68]  again on the next Kaizen.
[5312.22 --> 5313.26]  Yeah, and we're merging
[5313.26 --> 5314.84]  the Neon techs.
[5314.90 --> 5315.84]  We're going to take that
[5315.84 --> 5316.50]  into production.
[5317.54 --> 5318.88]  Okay, so we are all good
[5318.88 --> 5319.44]  with the latency,
[5319.72 --> 5320.74]  so all good.
[5320.98 --> 5321.74]  There are some issues
[5321.74 --> 5323.08]  with the Elixir configuration.
[5323.42 --> 5324.66]  I've left a couple of things
[5324.66 --> 5326.02]  for the Neon support.
[5326.28 --> 5327.56]  I have a support case open,
[5327.68 --> 5328.86]  so we'll select back and forth
[5328.86 --> 5329.40]  on that.
[5329.76 --> 5330.58]  I have a workaround
[5330.58 --> 5331.24]  which works,
[5331.70 --> 5332.98]  but the official documentation
[5332.98 --> 5334.06]  doesn't work for us.
[5334.42 --> 5335.18]  It's the official
[5335.18 --> 5336.74]  Neon tech documentation
[5336.74 --> 5338.18]  for Elixir configuration.
[5338.96 --> 5340.50]  Some issues with the SSL,
[5340.58 --> 5341.28]  with the SNI,
[5341.60 --> 5342.70]  it doesn't work as advertised.
[5342.70 --> 5342.86]  Nice.
[5343.58 --> 5346.68]  So we'll be on Neon.tech
[5346.68 --> 5347.80]  as of the shipping
[5347.80 --> 5348.46]  of this podcast.
[5349.22 --> 5350.88]  So when people listen to this,
[5351.46 --> 5352.58]  we'll be on Neon?
[5353.02 --> 5353.62]  I think so.
[5354.02 --> 5354.96]  Depends when we ship it.
[5355.16 --> 5355.90]  It's a week from today.
[5356.28 --> 5357.12]  Yeah, a week from today
[5357.12 --> 5357.62]  is fine, yeah.
[5358.12 --> 5359.62]  So if you listen to this,
[5360.42 --> 5361.38]  go to changelog.com
[5361.38 --> 5362.90]  and see if things are snappy
[5362.90 --> 5364.36]  or if the latency upsets you.
[5364.54 --> 5365.66]  See if it loads.
[5366.28 --> 5367.26]  Still Fastly in front,
[5367.36 --> 5368.00]  so by the way,
[5368.18 --> 5369.32]  Fastly will be serving
[5369.32 --> 5370.58]  your request most likely.
[5370.58 --> 5372.44]  Sign in to the website
[5372.44 --> 5374.72]  and we'll give you a cookie.
[5375.14 --> 5376.00]  And if you have that cookie,
[5376.22 --> 5377.44]  Fastly just passes through
[5377.44 --> 5378.36]  to the apps.
[5378.96 --> 5379.08]  Yeah.
[5379.12 --> 5380.66]  And you'll enjoy slower
[5380.66 --> 5381.90]  response times
[5381.90 --> 5382.70]  because you're going to be
[5382.70 --> 5383.24]  hitting Neon.
[5384.04 --> 5385.96]  But we hope you enjoy that cookie.
[5386.70 --> 5387.48]  An easy way to do that
[5387.48 --> 5388.18]  is for free, right?
[5388.22 --> 5388.70]  Just go to
[5388.70 --> 5389.50]  changeelog.com
[5389.50 --> 5390.20]  slash community.
[5390.56 --> 5390.96]  That's right.
[5391.14 --> 5391.52]  And hey,
[5391.56 --> 5392.38]  while you're doing that,
[5392.48 --> 5393.46]  come and say hi in Slack
[5393.46 --> 5394.74]  because I want to say hello to you.
[5395.36 --> 5396.18]  Lots of cool people in there,
[5396.24 --> 5397.08]  lots of good conversation.
[5398.08 --> 5399.06]  Home Lab's been active.
[5399.52 --> 5400.14]  TV and movies
[5400.14 --> 5400.98]  has been active.
[5401.70 --> 5402.26]  A lot of,
[5402.36 --> 5403.02]  I think you got your
[5403.02 --> 5403.84]  Wordle channel still yet,
[5403.88 --> 5404.02]  Jared.
[5404.10 --> 5405.04]  I'm tracking that.
[5405.46 --> 5405.62]  Oh,
[5405.64 --> 5406.74]  we picked up some Wordlers
[5406.74 --> 5408.90]  thanks to State of the Log.
[5409.02 --> 5410.08]  We got a few new Wordlers.
[5411.10 --> 5412.12]  Still going strong.
[5412.70 --> 5413.92]  I'm still keeping my streak alive.
[5414.18 --> 5414.38]  So,
[5414.64 --> 5415.14]  a lot of fun.
[5415.90 --> 5416.28]  All right, y'all.
[5416.72 --> 5417.36]  Bye, friends.
[5417.56 --> 5418.04]  Bye, friends.
[5418.04 --> 5418.46]  Kaizen.
[5418.62 --> 5418.98]  Kaizen.
[5419.12 --> 5419.32]  Kaizen.
[5424.48 --> 5425.16]  That's it.
[5425.24 --> 5427.10]  Our 13th Kaizen episode.
[5427.10 --> 5429.08]  If you have a long road trip
[5429.08 --> 5430.36]  or a marathon to run,
[5430.68 --> 5431.48]  you could go back
[5431.48 --> 5432.64]  to the very first one
[5432.64 --> 5434.60]  and binge our entire journey
[5434.60 --> 5435.20]  along the way.
[5435.56 --> 5436.18]  Find them all
[5436.18 --> 5437.66]  at changelog.com
[5437.66 --> 5438.62]  slash topic
[5438.62 --> 5439.48]  slash Kaizen.
[5439.82 --> 5439.98]  Oh,
[5440.06 --> 5441.26]  and you've probably heard
[5441.26 --> 5442.40]  that we're bringing Ship It back
[5442.40 --> 5443.04]  real soon,
[5443.16 --> 5445.06]  but not with Gerhardt on the mic.
[5445.52 --> 5446.16]  Maybe you're wondering
[5446.16 --> 5447.16]  how he feels about that.
[5447.72 --> 5448.62]  So was Adam.
[5449.22 --> 5450.34]  So for the Plus Plus folks,
[5450.92 --> 5452.38]  how do you feel about us
[5452.38 --> 5453.84]  relaunching Ship It?
[5453.84 --> 5454.52]  Hmm.
[5454.96 --> 5456.28]  Changelog Plus Plus members,
[5456.54 --> 5457.80]  stick around for that bonus.
[5458.28 --> 5459.48]  And if you haven't signed up yet,
[5459.72 --> 5461.06]  now is a great time
[5461.06 --> 5462.70]  to directly support our work
[5462.70 --> 5464.38]  with a Plus Plus membership.
[5465.06 --> 5465.90]  Ditch the ads,
[5466.28 --> 5466.98]  get free stickers
[5466.98 --> 5468.18]  and discounts on merch,
[5468.36 --> 5470.02]  and hear about Gerhardt's feelings
[5470.02 --> 5471.80]  at changelog.com
[5471.80 --> 5472.94]  slash Plus Plus.
[5473.30 --> 5474.58]  Changelog Plus Plus.
[5474.78 --> 5475.54]  It's better.
[5475.76 --> 5476.38]  Thanks once again
[5476.38 --> 5477.04]  to our partners
[5477.04 --> 5478.24]  at Fly.io,
[5478.90 --> 5480.06]  to Breakmaster Cylinder,
[5480.46 --> 5481.36]  and to you for listening.
[5481.96 --> 5482.92]  We appreciate you
[5482.92 --> 5483.78]  spending time with us.
[5484.20 --> 5485.94]  Next week on the Changelog,
[5486.44 --> 5487.36]  news on Monday,
[5487.76 --> 5490.06]  Alan Jude talking FreeBSD
[5490.06 --> 5490.88]  on Wednesday,
[5491.30 --> 5492.88]  and Techno Tim joins Adam
[5492.88 --> 5494.46]  for the state of the home lab
[5494.46 --> 5495.36]  on Friday.
[5495.96 --> 5496.80]  Have a great weekend,
[5497.32 --> 5498.40]  share the Changelog
[5498.40 --> 5498.98]  with your friends
[5498.98 --> 5499.84]  who might dig it,
[5500.08 --> 5501.10]  and we'll talk to you again
[5501.10 --> 5501.76]  next week.
[5501.76 --> 5501.82]  We'll see you next week.
[5501.92 --> 5502.50]  Changelog.
[5502.50 --> 5507.60]  scape of the state of the home lab
[5507.74 --> 5508.70]  and I'll see you next week.
[5509.26 --> 5512.64]  Check this out for now.
[5513.64 --> 5513.80]  Video role�무� live S Camens
[5513.80 --> 5516.22]  while in the exclusive
[5516.22 --> 5518.12]  Changelogmen
[5518.12 --> 5519.00]  is a Part Shavirus Challenge
[5519.00 --> 5519.88]  inoney Trag
[5519.88 --> 5520.74]  for the store from the homewhat
[5520.74 --> 5521.30]  and your friends
[5521.30 --> 5522.14]  are a part of the game
[5522.14 --> 5522.88]  where you can hear
[5522.88 --> 5523.38]  the show sometimes
[5523.38 --> 5523.98]  in business,
[5523.98 --> 5524.70]  and your friends
[5524.70 --> 5525.38]  and your friends
[5525.38 --> 5526.22]  and your friends
[5526.22 --> 5526.58]  and friends
[5526.58 --> 5527.12]  and everyone
[5527.12 --> 5528.12]  as well as possible see you
