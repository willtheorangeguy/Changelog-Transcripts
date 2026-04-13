[0.00 --> 15.88]  welcome back everyone this is the change log and i'm your host adams tokoviak this is episode 146
[15.88 --> 21.94]  today jared and i are talking to sarah may about mining the gap and why we're missing our best
[21.94 --> 26.74]  chances for gender parity and you much needed conversation on this show great having sarah
[26.74 --> 31.50]  on the show today she's the founder of rails bridge director of ruby central and she's a chief
[31.50 --> 38.34]  consultant at dev mind we got some awesome sponsors for the show code ship top tile and code school
[38.34 --> 41.92]  we'll tell you a bit more about top tile and code school later in the show but our friends at code
[41.92 --> 48.26]  ship they want you to deploy to production 10 times faster than you're doing today they do it by this
[48.26 --> 53.48]  awesome new feature called parallel ci and if you want faster tests you have to run your builds in
[53.48 --> 58.86]  parallel and with parallel ci you can now split up your test commands in up to 10 test pipelines
[58.86 --> 64.20]  this lets you run your test suite faster than before in parallel and drastically reduce the time
[64.20 --> 68.98]  it takes to run your builds and get that code of production they integrate with github and bitbucket
[68.98 --> 74.80]  you can deploy to cloud services like heroku aws and many more and you can get started today for
[74.80 --> 80.98]  free by trying out their free plan which includes 100 builds a month and five private projects or you
[80.98 --> 86.88]  can use our offer code the changelog podcast again that code is the changelog podcast to get a 20
[86.88 --> 92.56]  discount on any plane you choose for three months head to codeship.com slash the changelog to get
[92.56 --> 100.58]  started and now on to the show everyone back uh back here with sarah may sarah how are you
[100.58 --> 105.28]  doing good thanks for having me yeah we got jared on the line too you can't forget jared right
[105.28 --> 110.24]  jared how are you i'm hanging in there how are you hanging in there well you know that's the best
[110.24 --> 116.26]  way to be to be hanging in there this is the first show in a long time this show's being live
[116.26 --> 121.08]  broadcast so if you're a member you may be listening to this live we didn't do a lot of promotion around
[121.08 --> 125.76]  it because sarah wanted to be the experimental guest to be on the live broadcast we're live
[125.76 --> 130.00]  broadcasting just to members so if you want to listen to the show live you've got to be a member
[130.00 --> 134.58]  that's the that's the barrier to entry for that so you can do that by going to the changelog.com
[134.58 --> 139.64]  slash membership you learn all the details there you get access to slack the live channel and a ton of
[139.64 --> 145.40]  other stuff to sort of surround our community of open source enthusiasts and uh sarah it's so great
[145.40 --> 150.82]  to have you on the show today we got suggested to have you on the show um by matt brixton actually
[150.82 --> 156.72]  um a member he's just having a conversation around your article which is i guess somewhat popular what
[156.72 --> 161.88]  do you think mind the gap was it popular it was pretty popular it's definitely as popular as your
[161.88 --> 167.56]  other article you mentioned pre-call but yeah still popular yeah yeah it's been it's been interesting
[167.56 --> 172.02]  it hasn't made the front page of you know the programming subreddit but uh but it's definitely
[172.02 --> 176.86]  sparked some really interesting conversation especially on twitter yeah so let's give an
[176.86 --> 181.90]  introduction to you sarah i mean um i knew of you you know jared in the pre-call we talked about us
[181.90 --> 186.72]  being rubius at heart so we've known of you for a while but for those who may not know who sarah may
[186.72 --> 193.40]  is who are you who am i that's a loaded question isn't it uh well i am right now i'm in the chief
[193.40 --> 198.20]  consultant at dev mind software which means that i'm working with clients mostly in san francisco
[198.20 --> 204.78]  dev mind's based in chicago but i am i am the san francisco office uh and i'm also a director of ruby
[204.78 --> 208.84]  central which is a non-profit that runs both ruby comp and rails comp which are the two largest
[208.84 --> 215.30]  ruby related conferences in the world and uh i am also the co-founder of rails bridge which is an
[215.30 --> 219.10]  organization working to get more diversity into the ruby and rails communities
[219.10 --> 226.04]  and uh let's see what else do i do that's about it i do a lot of conference speaking i do a reasonable
[226.04 --> 232.54]  lot of writing and i'm working on a book and you also do the refactoring of the codes i do a lot of
[232.54 --> 239.64]  that yeah most of what i do in my client work is going into um i wouldn't say elderly code bases
[239.64 --> 247.06]  exactly but going into mature code bases and helping the team figure out where and when to refactor things
[247.06 --> 252.92]  elderly i like that it has a certain connotation to it doesn't it i feel like a rails app can
[252.92 --> 259.64]  actually be elderly after like three months so no doubt just depends totally okay you know it's it's
[259.64 --> 265.66]  funny too because we just had david hennemar hands on this on this call before last week um and you're
[265.66 --> 270.88]  the director of ruby central so you've got uh rails comp coming up here in may uh some exciting stuff
[270.88 --> 275.24]  happened around that call proposals i think it's closed now right yeah we've announced the program i'm
[275.24 --> 279.68]  really excited uh we have a very strong program this year and i'm super excited of course that
[279.68 --> 284.58]  david's going to come back and do his keynote as he always does yes of course you can't can't have a
[284.58 --> 289.92]  rails comp without dhh giving the keynote right i know right what would we do it's like apple with
[289.92 --> 297.28]  no steve jobs yeah and that hasn't worn out for them has it no no i guess not it has not so on uh
[297.28 --> 304.66]  on rails bridge um and dev mind of course as well uh the work you do there what's what's cool about
[304.66 --> 309.96]  rails bridge you had some recent news too about bridge foundry so a slight shift in the way
[309.96 --> 314.38]  the organization is sort of organized i think from a non-profit standpoint can you talk a little bit
[314.38 --> 320.52]  about rails bridge and what you do there yeah absolutely so rails bridge we swum we i started
[320.52 --> 327.48]  it with a woman named sarah allen in 2009 and originally it was uh it was like it was our goal was
[327.48 --> 332.50]  to bring more women into the ruby community in san francisco so that i could go to a ruby meetup and not be
[332.50 --> 337.98]  the only one there that was essentially my goal uh it turned into something much larger than that
[337.98 --> 344.82]  and we've done hundreds of workshops now across dozens of different countries and we've had i think
[344.82 --> 350.44]  last count about 10 000 people go through one of our workshops which is awesome we've expanded our
[350.44 --> 355.86]  mission a bit and we're now focusing on bringing in members of other underrepresented groups as well
[355.86 --> 363.06]  we've done uh we did a we did a workshop with the black founders we have a couple of uh we have the
[363.06 --> 367.66]  curriculum translated into spanish we've done a couple of spanish language workshops uh and recently
[367.66 --> 373.18]  we decided that the model that we've been using is actually super useful for other technical communities
[373.18 --> 377.78]  as well so we formed a parent organization called bridge foundry and under that we now have closure
[377.78 --> 382.30]  bridge which is pretty cool yeah they've been holding uh events we have mobile bridge which does both
[382.30 --> 386.76]  ios and android uh workshops and then of course we've still got rails bridge under there as well
[386.76 --> 393.04]  so we're we're excited to bring that model to other communities we have a little bit of rails bridge here
[393.04 --> 397.90]  in the heart of the change law because uh beverly nelson i think it's your south she's your south
[397.90 --> 404.24]  eastern chapter manager is that what you call yes absolutely does yeah so beverly's been on the team
[404.24 --> 411.58]  for a while worked with her at pure charity she uh loves learning as you know so one of the things
[411.58 --> 416.78]  that she's tasked with here on the change log not so much on the podcast but uh on our editorial side
[416.78 --> 423.70]  is really um like she just put out a post this last week called a huge list of coens because everybody
[423.70 --> 429.72]  loves ruby coens to learn coen to learn ruby the enlightened way of course and so there's you know
[429.72 --> 437.52]  this splurge of other um of other languages using the coens um coens way of of doing things so
[437.52 --> 443.00]  she's on the team and we're happy to have her so that's that's cool there's some some crossover
[443.00 --> 448.02]  there yeah that's cool i didn't know that you didn't know that huh see every day we got surprises
[448.02 --> 453.78]  for you every day in fact she's working up a post right now about bridge troll oh oh nice i believe
[453.78 --> 459.50]  is your guys's as a software is it a real app it's an open source rails app that we've built to manage
[459.50 --> 465.50]  the workshop process that we have so it takes our svps and originally we did most of it through meetup.com
[465.50 --> 470.88]  but as we got bigger we discovered of course that meetup has some limitations being a service and
[470.88 --> 476.66]  being not within everyone's price range certainly so we decided to build this and we also think it's
[476.66 --> 481.16]  a great way to for our students if they're interested in getting involved in open source for them to
[481.16 --> 487.14]  sort of nice easy entry into into the field because it's software they've already used and it's people
[487.14 --> 493.48]  they already know and it's uh so we it sort of serves dual purpose in that sense i like the name
[493.48 --> 499.36]  bridge troll definitely cool name yeah i like it too any other fun internal names y'all use that
[499.36 --> 507.02]  you could share here today fun internal names hmm i'm not sure bridge troll came out about actually
[507.02 --> 512.64]  because uh mostly because we had uh we had a workshop i think once where we have we usually
[512.64 --> 517.70]  have child care at our workshops and at that workshop the child care was in a conference room and the kids
[517.70 --> 524.22]  drew all over the um all over the whiteboards which of course is fine but one of them drew a troll and
[524.22 --> 532.80]  someone came in and said hey that looks like so that's cool that's that's cool that's a nice story
[532.80 --> 538.70]  too that uh it's it's funny those happy accents sometimes right yeah yeah things happen like that
[538.70 --> 545.98]  so let's um let's dive deep into the heart of the conversation so our show is roughly you know 45
[545.98 --> 552.12]  minutes 45 minutes ish um and today like i mentioned matt brixton one of our members
[552.12 --> 557.20]  has suggested um i've read the blog post before that i didn't think about having you on the show to
[557.20 --> 562.00]  sort of talk about this but uh we serve our member community so they want to hear it we're going to
[562.00 --> 567.08]  have you on the show to talk about minding the gap and i certainly enjoyed the you know the perspective
[567.08 --> 571.08]  that you brought to the table here in this in this conversation it's really kind of going around
[571.08 --> 576.60]  why we're missing our best chance for gender parity can you talk a bit about like the overall summary of
[576.60 --> 582.92]  of what this article is about and we'll sort of dive into some specific points along the way sure yeah
[582.92 --> 589.76]  absolutely so i wrote this mainly because i see a really interesting trend happening in the ruby community
[589.76 --> 594.98]  and also in other communities right now which is that we have a bunch of people who are coming in
[594.98 --> 601.00]  because of uh various code schools and boot camps and things like that we have never had an influx of
[601.00 --> 605.66]  this type before and in fact i think the ruby community is about the first we're the vanguard in
[605.66 --> 610.22]  that we are the first community to be seeing this because a lot of the early code schools taught ruby and
[610.22 --> 619.48]  taught rails and so now we have this enormous pool of people that are junior developers and are in general
[619.48 --> 625.50]  much more diverse than the community we have right now and so we've got this amazing opportunity
[625.50 --> 633.30]  to really bring a lot of diversity into our uh into our community but in order to do that we need to
[633.30 --> 638.36]  know what our own limitations are and we need to understand how it is that we got where we are
[638.36 --> 646.28]  and how we can not make the same mistakes when we're trying to hire people now uh and and the other
[646.28 --> 651.94]  thing that prompted this was that i found uh i love reading scientific research of various types that
[651.94 --> 658.92]  relate to things like uh programming teams and practices and how we write software and i came
[658.92 --> 666.36]  across one uh that was a very basic it was actually an economic study about the way that women and men are
[666.36 --> 671.84]  perceived when they're being interviewed or they're being or when you're looking at a resume or when you're
[671.84 --> 678.06]  evaluating the conference proposal things like that and what they found was that people who are
[678.06 --> 686.20]  from western cultures have a very strong built-in uh bias that they will look at a resume that has
[686.20 --> 690.78]  that is exactly the same except one of them has a female name at the top and one of them has a male
[690.78 --> 695.76]  name at the top and they will evaluate the one with the male name at the top more strongly than they
[695.76 --> 701.20]  will the one with the female name at the top and uh it's unintentional right this is something we all do
[701.20 --> 708.16]  because it's part of the culture that we live in and uh and so the question is like what can we do
[708.16 --> 716.54]  to to move away from that what can we do to to combat that bias because if we just allow it to
[716.54 --> 719.92]  continue the way it's been going what's going to happen is you're going to look at you're going to
[719.92 --> 725.98]  try and bring these people in but you're not going to be able it's much harder to get them into your
[725.98 --> 731.74]  pipeline get them in to your company if you're not aware of this bias that everyone has
[731.74 --> 739.40]  this bias you say has kind of exposed itself in what you might call an epic way in our specific
[739.40 --> 746.58]  community the open source and startup community which is kind of a microcosm of the larger tech
[746.58 --> 751.82]  industry which already has the problem uh some of the stats that you gave out there is that in the
[751.82 --> 756.38]  industry overall women make up 26 percent of developers which is already pretty bad right
[756.38 --> 763.72]  but you say in your world which is our world here so we're not even at 74 over 26 we're at 98
[763.72 --> 772.04]  over 2 for every woman there are 49 men which is ridiculously extreme and then you go on to kind
[772.04 --> 776.84]  of try to figure out why is it so extreme in this particular subculture of the tech industry
[776.84 --> 784.58]  um what are your thoughts on that well it's it's interesting because uh when when you talk about
[784.58 --> 791.48]  these differences between the open source startup world and programming in general you're looking at
[791.48 --> 797.32]  as you said a huge gap meaning if women are 26 percent of developers in general and they're two
[797.32 --> 803.74]  percent of developers in open source and startup uh you know there's one question which is why are we
[803.74 --> 809.06]  only at 26 percent overall there's a lot of people that are thinking about that uh problem but the one
[809.06 --> 815.02]  that i'm more interested in is why are we only at two percent why don't we track the overall industry
[815.02 --> 820.88]  because you would think right you would think that if if the overall industry was 26 percent that we
[820.88 --> 826.68]  would be you know sort of within margin of error of 26 percent but we're not and so one of the things
[826.68 --> 834.14]  that i thought about that was that there are we have a very interesting culture in the startup and open
[834.14 --> 841.12]  source world that is not present in the big company world and that is that we we love people who are
[841.12 --> 848.64]  self-taught all of our heroes are people that are were college dropouts the mark zuckerbergs the dhhs for
[848.64 --> 854.86]  example right these are people that don't have computer science degrees but have made incredible impacts
[854.86 --> 863.32]  on the world of programming and uh you can see that also in the way that we have shifted our hiring
[863.32 --> 868.68]  practices to be more to take more into account things like your github profile like how much
[868.68 --> 874.42]  open source do you do what kind of things do you contribute to can i look at your code right so
[874.42 --> 882.02]  um we depend much more on these informal qualifications than do than does the rest of the industry so if you walk
[882.02 --> 888.54]  into a google interview or microsoft interview or or something like that uh they're going to expect
[888.54 --> 891.76]  you to have a computer science degree and they're going to expect you to have all the knowledge that
[891.76 --> 897.26]  a computer science degree brings and that is not necessarily true where we are and so in uh sort of
[897.26 --> 903.76]  in compensation for that because we we like to think about ourselves as being sort of a self-taught
[903.76 --> 911.90]  bootstrap type people uh we fill in the gap with other things like github profile and conference talks and
[911.90 --> 918.54]  blog posts and that kind of thing and those are the things that are more subject to the bias that i
[918.54 --> 925.24]  spoke about earlier and so what that means is that as a community we are more reliant on evaluation
[925.24 --> 932.68]  methods that are subject to that bias and uh people with formal educational degree people who have
[932.68 --> 937.22]  computer science degrees who for you know for example have worked at google or worked at microsoft
[937.22 --> 945.94]  those folks have uh formal qualifications that can sometimes compensate for uh for the gap but if
[945.94 --> 949.90]  they're self-taught which is what we see all these people coming into the community from the code schools
[949.90 --> 954.98]  uh most of them are self-taught and don't have computer science degrees those people are going to find
[954.98 --> 961.04]  it much harder because they're going to find that the evaluation criteria that people use is much more subject
[961.04 --> 969.76]  to this gender and racial bias that we all have yeah i think you know it is definitely a gender and racial bias i think it also
[969.76 --> 978.08]  kind of leads itself into uh you know you could call it age discrimination or even lifestyle bias because the ones who
[978.08 --> 986.22]  may not have the strong open source uh contributions or the you know the excellent list of conferences that they've spoke at
[986.22 --> 993.02]  are keynoted it's because they're doing other things with their free time right i mean yeah absolutely and
[993.02 --> 997.60]  with women you know traditionally it's at home with kids or you know the housework the things that you
[997.60 --> 1003.98]  bring up in the article um you know the same can apply uh probably less so in the west to men with kids
[1003.98 --> 1011.64]  um so what do you think about this whole github as resume as a thing is that is that just a bad idea
[1011.64 --> 1018.74]  that we all kind of stumbled into or or are we just kind of doing it wrong i think that it's a it's
[1018.74 --> 1023.88]  an interesting it's definitely an interesting idea um one of one of the things that i think though
[1023.88 --> 1027.72]  is interesting about that i actually did a talk about this last year at nickel city ruby
[1027.72 --> 1033.68]  is that if you look at my github profile i basically don't contribute to open source so you look at my
[1033.68 --> 1038.30]  contribution graph it's basically completely blank there's a few little green squares here and there
[1038.30 --> 1042.56]  where i did some bridge stuff usually yeah i was right you look at that and you're like huh
[1042.56 --> 1048.30]  well sarah geez what's going on here well and the interesting thing was when i was at nickel city
[1048.30 --> 1052.54]  ruby i looked at all of the other speakers contribution graphs and they were all extremely
[1052.54 --> 1057.54]  impressive lots of green squares it was great so you look at that and you're like well i mean if
[1057.54 --> 1063.26]  you're looking at github as your resume and you look at my github uh you're probably not going to
[1063.26 --> 1069.02]  get a really good sense of what i can do right and you know i think i'm an extreme example because
[1069.02 --> 1075.44]  i have surfaced in other ways within the community but for people who haven't done that the question
[1075.44 --> 1083.00]  is like how how much are we losing by depending on uh public publishing of code like how many people
[1083.00 --> 1087.26]  are we missing out on because that's one of you know that's the thing that we depend on the most
[1087.26 --> 1091.00]  i think it's definitely something that can be taken into consideration just like everything else
[1091.00 --> 1096.26]  uh however i don't think that it's it's great as a filtering mechanism
[1096.26 --> 1104.10]  i think some of it plays into the whole passion conversation which is something that the startup
[1104.10 --> 1111.12]  and open source community have in common have in common is that we value the desire the passion
[1111.12 --> 1118.44]  as something that's that is a characteristic that we like and so we look at lack of contribution or lack
[1118.44 --> 1126.30]  of public code or what have you as you don't have a passion for this craft which could which is
[1126.30 --> 1131.38]  sometimes the case and sometimes it's a complete red herring right right exactly i don't think those
[1131.38 --> 1135.64]  are necessarily comparable statements i agree with you that's what we're looking for is the passion
[1135.64 --> 1142.24]  um but i think that the mechanism that we've chosen for that is insufficient i agree we uh we started
[1142.24 --> 1147.32]  out talking about the industry overall could could maybe you better define what the industry overall is
[1147.32 --> 1153.46]  when you say that versus because it feels kind of like a a slightly us versus them or at least when
[1153.46 --> 1161.92]  it comes to stats of 26 percent of developers and only not you know two out of 98 are women who is the
[1161.92 --> 1164.72]  what makes up the industry overall when you say that
[1164.72 --> 1171.08]  the industry overall includes uh in addition to sort of the startup and open source worlds that we
[1171.08 --> 1176.08]  that we're in it includes both sort of a larger what i would consider to be the larger open source
[1176.08 --> 1183.46]  companies things like google um and also larger more traditional organizations your ibms your hps
[1183.46 --> 1192.12]  and also even more than that it is the non-technology focused organizations that employ programmers so for
[1192.12 --> 1200.02]  example banks insurance companies support uh provide millions and millions of programmer jobs
[1200.02 --> 1207.78]  uh most of which uh are not that i most of which we don't see living in our github world
[1207.78 --> 1215.18]  well we got to take a quick break here uh to listen to a word from one of our sponsors we'll come back in just a second
[1215.18 --> 1222.30]  top tile is the best place to work as a freelance software developer if you're freelancing right now
[1222.30 --> 1226.88]  as a software developer and you're looking for a way to work with top clients on projects that are
[1226.88 --> 1232.56]  interesting challenging and using the technologies you want to use top tile might just be the place
[1232.56 --> 1237.44]  for you working as a freelance software developer with top tile means your days of searching for
[1237.44 --> 1242.90]  long-term high quality work and getting paid what you're worth will be over let's face it you're an
[1242.90 --> 1247.34]  awesome developer and you deserve to be composite like one joining top tile means you'll have the
[1247.34 --> 1252.06]  opportunity to travel the world as an elite engineer on top of that top tile can help provide
[1252.06 --> 1257.14]  the software hardware and support you need to work effectively no matter where you are in the
[1257.14 --> 1264.66]  world head to top tile.com slash developers that's t-o-p-t-a-l.com slash developers to learn more
[1264.66 --> 1273.10]  and tell them the changelog sent you all right sarah we're back um i think some of the things we've been
[1273.10 --> 1278.62]  talking about around this perceived competence is is what you describe as the credibility gap can you
[1278.62 --> 1286.92]  talk about that a little bit yeah the the credibility gap is is a phenomenon where if you have two people
[1286.92 --> 1292.64]  that have more or less equivalent skills and the difference between them is gender then people will
[1292.64 --> 1298.06]  make assumptions about comp the competence of the person if you're trying to judge the competence of the
[1298.06 --> 1304.26]  person in front of you and you know what the gender of the people are you will usually assign a higher
[1304.26 --> 1309.44]  competence to a male programmers in front of you than to a female programmer in front of you and you
[1309.44 --> 1314.16]  can see this come out in a lot of different ways so for example if you go to a meetup and you see a
[1314.16 --> 1320.24]  woman in a meetup it used to be that you could pretty much assume that she was a recruiter and not
[1320.24 --> 1326.48]  necessarily a programmer but that making that assumption can be dangerous because if she is a
[1326.48 --> 1331.92]  programmer then she is starting from this deficit of competence that you have sort of projected onto her
[1331.92 --> 1337.74]  and even if even if you get corrected even if you talk to her and discover she's not a recruiter she
[1337.74 --> 1342.28]  is a programmer in fact she's a better programmer than you are like that's great but it doesn't
[1342.84 --> 1352.26]  make up for the initial gap that you perceive and that you assign essentially to her and that's you know
[1352.26 --> 1357.26]  it's a psychological phenomenon I think of it as a it's a bug in our wetware meaning like it's it's
[1357.26 --> 1362.94]  something that our brain does that we don't want it to do necessarily and so at this point what we
[1362.94 --> 1370.16]  need to do is understand that it does it and work with it in golf they call that uh that credibility
[1370.16 --> 1378.40]  gap a handicap no word yeah because uh right so if you're a golfer right if I don't play golf off
[1378.40 --> 1383.48]  enough but I know enough of the terms but they call the you know the idea of the game shooting so if you
[1383.48 --> 1388.48]  shoot I don't even know what the number is Jared that was the last time you played golf ah never
[1388.48 --> 1395.82]  it's nine par 72 man I mean right there you go par 72 okay so just to give me some baseline to run
[1395.82 --> 1401.90]  some numbers off here there's like you know par don't worry about the golf terms I messed that up
[1401.90 --> 1407.52]  but nonetheless nonetheless they do call it a handicap the point is is that if I come into the game and
[1407.52 --> 1412.82]  I'm not as good as a pro or somebody who's better than me I come in with some shots ahead and they
[1412.82 --> 1417.88]  call that a handicap which is somewhat similar to what you're talking about which is actually a
[1417.88 --> 1425.20]  perceived gap which is me or someone else placing a deficit of of ability on someone based on their
[1425.20 --> 1430.58]  gender race or creed exactly yeah and a handicap is trying to actually level the playing field
[1430.58 --> 1435.58]  yeah um in the case of the credibility gap is that we start off with a unlevel playing field
[1435.58 --> 1440.32]  subconsciously in our mind I believe is what she's saying and so maybe we're getting ahead of
[1440.32 --> 1445.76]  ourselves because some of some of the solutions to the to the problem that Sarah suggests is to
[1445.76 --> 1451.64]  kind of give that benefit of the doubt almost to give a woman that you don't know a handicap until you
[1451.64 --> 1458.44]  have more information to act on because she's she's operating at such a deficit already that it's unfair
[1458.44 --> 1465.24]  yeah but you also said too Sarah that you first noticed yourself make the same kind of mistake a few
[1465.24 --> 1469.50]  years ago at a conference can you talk a little bit about that situation and how you felt when you did that
[1469.50 --> 1477.10]  yeah I was uh I was at a I think I was at a meetup in San Francisco and uh I was in line at the bar
[1477.10 --> 1484.56]  and there was a woman in front of me and so I started talking to her uh and I was before I did that I
[1484.56 --> 1489.34]  had this this you know I do what everyone does which is that I looked at her and I was like well she's
[1489.34 --> 1495.38]  dressed pretty nice probably she's not wearing t-shirt and jeans like hmm she's probably a recruiter
[1495.38 --> 1500.64]  or you know maybe she's a product manager or something and it wasn't necessarily a conscious
[1500.64 --> 1505.28]  judgment but I looked at her and I made a decision about what I thought she wanted to talk about for
[1505.28 --> 1511.42]  example and so uh I started to talk to her and I realized about three or four sentences in that
[1511.42 --> 1515.90]  she was a developer in fact she was a developer with way more experience than I had
[1515.90 --> 1524.02]  and I had just mistaken her for essentially uh a non-programmer um based purely on the what she
[1524.02 --> 1531.40]  looked like so did you put your foot in your mouth or yeah I totally did did you apologize or did you
[1532.02 --> 1537.20]  no it's one of those things where it's like it's more like it's more of an internal thing I think I'm
[1537.20 --> 1541.24]  sure she noticed because I notice when people do it to me but most of the time I don't mention it
[1541.24 --> 1546.64]  and she didn't mention it which I was very grateful for but you know what that shows is that
[1546.64 --> 1551.80]  that even people who are in that group make that mistake right I make that mistake all women make
[1551.80 --> 1557.78]  that mistake um you know and when you see this come through also in race you'll notice you'll you'll see
[1557.78 --> 1563.36]  that uh white people make this mistake in assuming that other white people are more competent but
[1563.36 --> 1570.40]  black people also do it they also will rate people who are white higher and so it's just part of the
[1570.40 --> 1574.82]  the cultural milieu that we're living in and it's unescapable for all of us that are that are here
[1574.82 --> 1580.92]  yeah I know that uh you know just in the fact that we all discriminate that way I think it's
[1580.92 --> 1585.64]  as you said in your in your post here it's sort of like cultural it's sort of subconscious that
[1585.64 --> 1590.92]  you sort of get pulled into this and you may not even do it intentionally even if you can bleed
[1590.92 --> 1595.80]  to the nth degree that you're not racist or biased or whatever the terms you might apply to
[1595.80 --> 1601.42]  a negative connotation on that is that we tend to just do that I think it's part of societal
[1601.42 --> 1607.50]  upbringings to a degree and we see it in media we see it in marketing we see it almost everywhere we
[1607.50 --> 1613.60]  go people being objectified not just women but also men also different religions of the race and creed and
[1613.60 --> 1619.50]  it's sort of this systemic issue that we have and but you're zooming specifically into
[1619.50 --> 1624.10]  the you know as you mentioned in the pre-call this subreddit the subculture
[1624.10 --> 1628.28]  of where we kind of hang out which is like in the in the open source community the developer
[1628.28 --> 1634.50]  community where I guess the the rubber meets the road so to speak that that none of this we do is
[1634.50 --> 1641.46]  really intentional but we do do it day to day we do and sometimes these assumptions are correct
[1641.46 --> 1647.66]  right and so that's that's when it's even hardest to see it like when I see a woman at a meetup and I
[1647.66 --> 1652.68]  assume she's a recruiter and I'm right then I don't notice it right I don't notice that I made that
[1652.68 --> 1660.08]  judgment and so one of the things that I've been thinking a lot about is how can I how can I practice
[1660.08 --> 1666.70]  not making that mistake and so what I've been trying to do is when I meet a woman at a conference or at
[1666.70 --> 1672.58]  a meetup I assume she's incredibly technical and I will start talking to her as though she is and then
[1672.58 --> 1678.96]  sometimes I'm wrong but I what that does at least what I'm hope that it does is that it
[1678.96 --> 1687.86]  it levels the playing field a little bit so that if she is technical that we can talk about you
[1687.86 --> 1693.46]  know we can she doesn't start with the same perception gap that she would otherwise and
[1693.46 --> 1698.10]  hopefully over time what that'll do is it'll recalibrate hopefully you know at least a little
[1698.10 --> 1703.20]  bit recalibrate the way that I evaluate people at a subconscious level but I think that's a
[1703.20 --> 1710.74]  that's a long-term goal how does some of this play into the passions that come back to Sarah the
[1710.74 --> 1715.36]  Sarah that goes to Railsbridge and Sarah that co-founded Railsbridge that you know does all this
[1715.36 --> 1721.62]  stuff how does that you know this play into you know this topic play back into how you treat your
[1721.62 --> 1729.90]  work there and how you form community and bonds there inside of Railsbridge um it's interesting
[1729.90 --> 1737.06]  because Railsbridge has exposed me to many more female developers than I ever knew before and so
[1737.06 --> 1742.24]  I have seen an incredible variety of people come through Railsbridge we actually have quite a few
[1742.24 --> 1746.18]  people come through Railsbridge who are developers from other communities that just want to learn Rails
[1746.18 --> 1753.66]  in addition to people that are new to programming and so I've met all kinds of female developers of
[1753.66 --> 1761.02]  various types system administrators um dbas php does dot net people java people and so on
[1761.02 --> 1769.18]  and it's expanded my idea of and that has helped me expand my idea of what a female developer looks
[1769.18 --> 1773.70]  like because I've seen so many more examples I think part of the problem that we have is that we don't
[1773.70 --> 1779.34]  have that many examples because we're at two percent and because we don't tend to go to conferences
[1779.34 --> 1786.68]  where people from insurance companies hang out we don't see those people and part of the goal of
[1786.68 --> 1792.94]  Railsbridge was always to to integrate not to have our own little island of women doing their own thing
[1792.94 --> 1798.18]  but to integrate back into the larger community as I said my original goal was to not be the only
[1798.18 --> 1806.94]  woman at any given SF Ruby meetup and so to that end we've always brought in men from the community to
[1806.94 --> 1816.42]  to teach to TA to volunteer and we have our workshop structure is set up fairly deliberately so that
[1816.42 --> 1823.80]  there are social opportunities to and not just sort of from on the teacher student level to get to know
[1823.80 --> 1831.02]  people in the community and so an interesting side effect of that is that around San Francisco at least
[1831.02 --> 1834.28]  I've heard this from other communities that have strong Railsbridge contingents
[1834.28 --> 1839.08]  the men in the community have gotten better at teaching which is an interesting side effect
[1839.08 --> 1847.42]  and they've also been able to see more varieties of female developers than they can see just at their
[1847.42 --> 1854.02]  job or at the you know at the meetups where it used to be you know two to three percent so I think that
[1854.02 --> 1861.12]  part of where this comes from for me is that I feel like we need to as a community we need to see the
[1861.12 --> 1868.92]  variety of of developers along many different axes of diversity in order to start normalizing their
[1868.92 --> 1875.92]  presence in our community at all well in your blog post you did have some prescriptions for us so
[1875.92 --> 1879.92]  maybe it's a good point here to sort of talk about some of those prescriptions in terms of
[1879.92 --> 1885.78]  what we can do to to sort of do this and the first thing you mentioned was I guess is the summary of your
[1885.78 --> 1889.66]  your blog post which we didn't really talk about the intro which I loved a lot too which was your trip in
[1889.66 --> 1895.60]  London talking about this idea of the gap when you're walking off the tram but you know the first
[1895.60 --> 1901.60]  in your list of things to do that you can do to fight back is is to notice the gap recognize and
[1901.60 --> 1906.14]  acknowledge that these assumptions are in place when you make them you know sort of like you did at that
[1906.14 --> 1910.22]  conference or sort of like I might do when I'm at a meetup and I might make an assumption about
[1910.22 --> 1916.58]  someone that they are not a developer or just in general is to just notice this gap period
[1916.58 --> 1922.88]  yeah I think that's the first step and and for me uh it took a while before I knew what to do about
[1922.88 --> 1928.72]  it so I I sort of I I just for a long time I just sort of kept an eye on it like I would notice when
[1928.72 --> 1935.36]  it happened I started to try and pay attention to it uh so to you know so that when I met women
[1935.36 --> 1939.78]  other women uh at meetups and at conferences and so on I would just sort of keep track of like oh
[1939.78 --> 1943.88]  I made an assumption about that one I didn't make an assumption about that one that's interesting
[1943.88 --> 1950.48]  and I think just noticing it is is the first step because none of us you know I don't think
[1950.48 --> 1958.64]  that I am sexist I don't think that I'm racist uh however my actions when I'm looking at resumes and
[1958.64 --> 1965.02]  when I'm meeting people at meetups is different depending on those factors and I think that it's
[1965.02 --> 1971.96]  important for us to understand the cognitive skew that we are subject to because that's the only just
[1971.96 --> 1976.54]  just being able to see it is the first step to being able to do something about it
[1976.54 --> 1983.14]  I agree with you absolutely I think some of the best things that we can do to help one another
[1983.14 --> 1990.40]  with regards to these subconscious uh prejudices that we have is first of all just to raise awareness
[1990.40 --> 1995.86]  that this is a possibility that this is something that you do um and then secondly is to put a name on
[1995.86 --> 2001.24]  it um which at least for me you've done for me credibility gap is not something that
[2001.24 --> 2006.72]  previously had a name in my mind um but as I was reading your post I can definitely like go back
[2006.72 --> 2012.56]  in recent history and be like yep that's I did that there I did that there you know as I I could uh
[2012.56 --> 2019.00]  commiserate with with your experience that you recorded there and I think it's incredibly valuable
[2019.00 --> 2024.88]  first of all that we just have these conversations and secondly that we can actually put a name to
[2024.88 --> 2030.70]  something that to a bias that we have um just like in software when you can put a name on something
[2030.70 --> 2037.54]  it becomes more concrete it's a lot easier to check yourself if you have like some sort of hook by which
[2037.54 --> 2044.28]  to do it and I think just having that term credibility gap kind of empowers us to judge our own thoughts
[2044.28 --> 2052.10]  you know before we project those onto other people yeah absolutely well let's pause here for an ad and we'll be right back
[2052.10 --> 2058.52]  it is time to put the program books away put them away put them down and learn by doing with code
[2058.52 --> 2064.30]  school code school offers a variety of courses to help you expand your skills and learn new technologies
[2064.30 --> 2073.06]  such as javascript ruby ios git html css and many more code school knows that learning the code can be a
[2073.06 --> 2079.10]  daunting task they combine experienced instructors with proven learning techniques to make learning the code
[2079.10 --> 2084.22]  educational as well as memorable giving you the confidence you need to continue past the hurdles
[2084.22 --> 2090.42]  they're always launching new courses on new technologies and offering deep dives on tried and
[2090.42 --> 2095.48]  true languages so if you don't see them you need suggest a course and they'll build it if there's enough
[2095.48 --> 2101.62]  demand code school also knows that languages are a moving target they're always updating content to give
[2101.62 --> 2107.72]  you the latest and greatest learning resources you can even try before you buy roughly one out of
[2107.72 --> 2115.04]  every five courses on code school is free this includes introductory classes for git ruby and jquery
[2115.04 --> 2121.98]  which allow free members to play full courses with coding challenges included you can also pay as you go
[2121.98 --> 2128.52]  one monthly fee gives you full access to every code school course and if you ever need a breather
[2128.52 --> 2135.44]  take a break you can suspend your account at any time don't worry your account history points and badges
[2135.44 --> 2140.36]  will all be there when you're ready to pick things up again get started on sharpening your skills today
[2140.36 --> 2149.64]  at code school.com once again that's code school.com all right well we're back um it's a little weird
[2149.64 --> 2153.64]  because we're not doing those pauses so just if you're listening and they and they sound a little
[2153.64 --> 2159.70]  abnormal this is the first time we're doing them so we around we like to experiment and we uh we do things
[2159.70 --> 2165.90]  abnormally sometimes so the second thing that uh you talked about sarah in terms of what we can do
[2165.90 --> 2171.20]  is to step across the gap what do you what do you mean by that you say and make it conscious ever to
[2171.20 --> 2176.64]  to combat those assumptions but i think we kind of touched a little bit there uh pre to the the
[2176.64 --> 2182.62]  sponsorship there but what is some ways that um that we can step across that gap and begin to break
[2182.62 --> 2189.54]  down those barriers yeah one of one of the ones was what i mentioned earlier which is that uh when you
[2189.54 --> 2196.62]  when when i meet a woman or a non-white person at a conference i make a conscious decision in my head
[2196.62 --> 2203.60]  to assume that they are technical until i am absolutely proven otherwise and my hope with that
[2203.60 --> 2210.74]  is that uh i am making up for a little bit of that gap the the credibility gap that has embedded itself
[2210.74 --> 2217.14]  in my brain another thing that i do that i found that's been really effective is that when i'm hiring
[2217.14 --> 2223.84]  uh before i look at anyone's resume i have somebody take out all of the indications of gender and that's
[2223.84 --> 2229.20]  not just the name it can be things like you know if they went to a women's college or traditionally
[2229.20 --> 2233.74]  about a black university like they need to take that kind of stuff out so on and so forth so there's a
[2233.74 --> 2238.64]  lot of things beyond the name that need to need to be adjusted and you'll find out what those are over
[2238.64 --> 2244.34]  time when you start doing it uh but the nice thing about that is that it allows me to look at a resume
[2244.34 --> 2251.28]  without without making assumptions about the gender then if i for the people that sort of make it
[2251.28 --> 2258.74]  through the first screening then i actually ask my hr person to print out some of their code from github
[2258.74 --> 2265.56]  and show it to me without basically i want to see it without their name attached because this bias
[2265.56 --> 2270.78]  will also affect us when we're looking at code when we're judging someone when we're doing code review
[2270.78 --> 2278.16]  when we're evaluating conference proposals and so on and so uh any way that i can remove
[2278.16 --> 2285.18]  that bias from the preamble i mean certainly once you're like talking to somebody it's pretty
[2285.18 --> 2291.26]  difficult to ignore but the steps leading up to that actually seem to be where a lot of the women
[2291.26 --> 2298.44]  drop out of our process and what i found was that once i started doing that we got a lot we got a much
[2298.44 --> 2305.08]  more diverse set of folks in the door for interviews and uh this is part of the you know the the problem
[2305.08 --> 2308.88]  that we have where a lot of companies will tell me well you know i don't know what to do because no
[2308.88 --> 2315.68]  women applied for my job no women submitted a talk to my conference there's a problem there uh in terms
[2315.68 --> 2320.00]  of getting people to you know in terms of reaching out to people and asking them to apply and asking them
[2320.00 --> 2328.02]  to submit but even once you do if you are then evaluating what they send in knowing their name or their
[2328.02 --> 2336.28]  other demographic information what you find is that fewer women get through that phase so i think that
[2336.28 --> 2342.26]  uh it's absolutely critical that we remove that information from whoever it is that's making that
[2342.26 --> 2348.74]  decision about who moves on to the next section of the interview you find that causes a lot of
[2348.74 --> 2354.48]  management overhead i know you mentioned a little bit but is it a real pain to get those uh names scrubbed
[2354.48 --> 2360.48]  before you view and do the code review uh it can be i think that um you know sometimes it will
[2360.48 --> 2368.00]  sometimes it's difficult to evaluate you know there's sometimes when it's it requires so much
[2368.00 --> 2372.76]  information to be taken out that it's then difficult to evaluate right yeah i try to do that case by case
[2372.76 --> 2380.48]  right and uh you know part of how people could help me with that is if they could i'm not quite sure how
[2380.48 --> 2385.60]  to make the suggestion but if they could write um some software that'll do it no well i mean when
[2385.60 --> 2390.82]  they send in a resume try to make sure that there's nothing in the body of the resume that would give
[2390.82 --> 2395.80]  away gender or race for example right so for example sometimes occasionally people will refer to
[2395.80 --> 2400.82]  themselves as a third person right so you know as you're talking about something like he did blah blah
[2400.82 --> 2407.36]  blah at this company right uh that kind of stuff you know which you know resume style guides tell you
[2407.36 --> 2414.52]  not to do anyway but we we see a reasonable amount of that um you know things like that but uh yeah i
[2414.52 --> 2421.46]  think that it's it's definitely been overall positive because it does mean that we get a lot more women
[2421.46 --> 2427.36]  in for like the in-person interviews um and you know there's another set of problems once you're in
[2427.36 --> 2433.36]  the in-person interviews but but at least you talked about that a bit didn't you was that another uh
[2433.36 --> 2439.56]  you might have another post i read that just just the um the the boardroom kind of look you know you
[2439.56 --> 2444.26]  come into a you know you mentioned google earlier in the call but the in-person interview can be just
[2444.26 --> 2449.52]  as hard as just getting in the door or you know getting your proposal looked at then getting a face-to-face
[2449.52 --> 2455.18]  with someone could be just as hard as actually getting there in general yeah and that's true but i think
[2455.18 --> 2461.28]  that there are we have to combat this bias in different ways at each stage of these processes
[2461.28 --> 2470.24]  and uh so you know step zero really is getting uh resumes in the door and then step one is making
[2470.24 --> 2475.96]  sure that you can evaluate those resumes in a way that is less subject to bias than it would be if you
[2475.96 --> 2481.10]  just looked at them the way they came in i think it's a smart idea too to to sort of protect yourself
[2481.10 --> 2485.88]  you know this is this is more like um i guess that's maybe a bad way to put it but
[2485.88 --> 2491.78]  it's protect yourself from yourself for the betterment of the community because you know
[2491.78 --> 2496.08]  there you go with when you say make a conscious effort to step across the gap you know that you have
[2496.08 --> 2501.98]  some sort of uh subconscious prejudice whether you like it or not that happens whether you like it or
[2501.98 --> 2507.34]  not it's just some sort of innate subcultural thing that we sort of judge people based on some
[2507.34 --> 2513.74]  attributes to remove those abilities to judge and then you kind of get a an even playing field and
[2513.74 --> 2519.52]  even and even look at a person's proposal for a conference or a job application or what have you
[2519.52 --> 2524.24]  sort of protect yourself from that that uh evaluating them in a bad way you know you give
[2524.24 --> 2529.42]  them a chance before they're where they may not have been a chance move us closer to what we all
[2529.42 --> 2534.50]  as programmers want is like a meritocracy right yeah where it's just purely based on merit
[2534.50 --> 2541.64]  and we can't do that without some barriers to biases because they're so ingrained in us so
[2541.64 --> 2546.24]  i think on the on the coding side it seemed like a pretty decent chance of writing some open source
[2546.24 --> 2551.32]  software where you could you know point to a specific thing on the web and maybe you'd go and
[2551.32 --> 2557.88]  scrub it of any names and uh you know for certain adverbs and or not adverbs pronouns and whatnot
[2557.88 --> 2565.96]  um on the resume side yeah definitely harder as they come in all so many forms but um we definitely
[2565.96 --> 2570.04]  seen some some conferences doing that as well i think maybe you mentioned that you also do that
[2570.04 --> 2575.38]  for your conference talks seems like a great uh way of of leveling the playing field for picking
[2575.38 --> 2581.34]  conference uh speakers as well yeah we've actually had pretty amazing success with that
[2581.34 --> 2586.56]  um at ruby confident rails conf we use a piece of software that we developed ourselves actually
[2586.56 --> 2594.26]  um but which is open source which anyone can use and it has a it follows a process where there are
[2594.26 --> 2599.68]  reviewers and reviewers will go in and assign a rating to a talk but they don't see any of the
[2599.68 --> 2607.00]  demographic information so they don't see the name they don't see the bio and we ask people in the
[2607.00 --> 2613.96]  call for proposal text to please not put any identifying information in their proposal itself
[2613.96 --> 2619.86]  um and some people you know some people still do but uh usually how that works is we just kind of ask
[2619.86 --> 2628.64]  them to take it out before we start evaluating it and then once we have a first round of scores uh at
[2628.64 --> 2634.92]  that point a smaller group of people goes in and looks at looks at the talks uh including the
[2634.92 --> 2642.02]  biographical information including the name and then uh evaluates them based on you know there's a
[2642.02 --> 2645.82]  lot of stuff that goes into making a balanced program certainly for a big conference like rails
[2645.82 --> 2652.78]  conf uh i should say big for the ruby world although it's fairly small overall but for something like
[2652.78 --> 2657.78]  that there's definitely a set of topics that we want to make sure we cover um and so at that point
[2657.78 --> 2662.90]  we're taking a lot of different things into consideration including the experience of the speaker and things
[2662.90 --> 2672.06]  like that so but it allows us to get a first round at least that is uh less subject to the biases that
[2672.06 --> 2677.38]  we all carry that's a good starting point what's the name of that software if you recall i think it's
[2677.38 --> 2685.10]  called cfp app right nice uh creative name uh there's a link to it in my blog post i found it ruby
[2685.10 --> 2692.04]  central slash cfp dash app we'll link that up in the show notes yeah i also liked what you said too that uh
[2692.04 --> 2697.10]  sarah when when going through this process that some known good speakers may not actually get
[2697.10 --> 2702.92]  through because of a crappy i think you actually said but crappy proposal um you know so you know
[2702.92 --> 2708.04]  it's it sort of strikes a balance there where you know get your proposal in order even if you're a
[2708.04 --> 2713.72]  known credible speaker get your proposal on par and and you might make it through and you actually
[2713.72 --> 2717.84]  take it based on not so much who they are and what they've done but what the actual proposal is
[2717.84 --> 2723.46]  proposing for the conference right yeah that's exactly it i feel like this process has actually
[2723.46 --> 2730.00]  improved overall the quality of the proposals that we get not just the number of them or the
[2730.00 --> 2734.80]  diversity of them but actually i think everyone's proposals have improved because i think they have
[2734.80 --> 2741.16]  to right if you're if you want to make it through the first round and you know we do consider who the
[2741.16 --> 2746.36]  speaker is at some point during the process so that's not something that we don't consider at all
[2746.36 --> 2754.44]  but i think that it's some conferences in the ruby space i feel like have become a collection of
[2754.44 --> 2758.96]  people that i have seen before right and it's sort of the same set of people that you see at every
[2758.96 --> 2764.02]  conference and i am one of those people at this point because i've done so many conference talks
[2764.02 --> 2769.78]  that's one of the reasons why i'm doing fewer of them is because i feel like it's someone else's turn
[2769.78 --> 2776.76]  essentially but i think that uh one of the things that this process can help with is in is help us
[2776.76 --> 2784.04]  to discover people who are going to be amazing speakers and find them even if they haven't done a talk
[2784.04 --> 2787.86]  before or even if they've only done a talk at their local meetup or something along those lines
[2787.86 --> 2794.20]  and uh get them you know get them onto the circuit get them into into our collective consciousness
[2794.20 --> 2801.24]  well i know that we could probably go uh quite a bit further when talking through this i know that
[2801.24 --> 2808.12]  uh this is certainly on our hearts we when we think about you know prejudice and biases uh to our peers
[2808.12 --> 2812.88]  and it's something that i certainly want to be mindful of but at the same time your last point which is not
[2812.88 --> 2818.90]  to stare too deeply for too long into this gap because you might go a little crazy i you didn't say that
[2818.90 --> 2825.02]  well i think that it's it's something that you need to think about but it doesn't mean that it
[2825.02 --> 2830.40]  needs to consume everything that you think about it and you need to give yourself permission to still
[2830.40 --> 2835.08]  screw it up uh because it's going to happen you're going to make this human you know i mean we're gonna
[2835.08 --> 2840.90]  exactly we're just we're just broken people it's gonna it's gonna happen sometime yeah and my the way
[2840.90 --> 2846.22]  that i try and deal with that is just to when i notice myself doing it just be like wow i just did that
[2846.22 --> 2852.06]  thing and i'm sorry about that let's move on so i do apologize these days when i notice myself doing
[2852.06 --> 2856.76]  it because i think that it's important for me to acknowledge to other people that i am you know that
[2856.76 --> 2863.10]  i made that mistake and i'm sorry but then i move on and i think my hope is that over time it'll make
[2863.10 --> 2868.50]  at least a little bit of a difference in how i perceive people i think it goes back to your second
[2868.50 --> 2872.52]  prescriptive which is making conscious effort to step across i think part of stepping across
[2872.52 --> 2877.90]  is admitting that there's something to step across of and like you said apologize when it might happen
[2877.90 --> 2884.72]  that way you know whomever you may have offended whether it's face-to-face or digitally somehow via
[2884.72 --> 2889.54]  email or something passive it gives you a chance to you know apologize right then and there
[2889.54 --> 2896.02]  and you know kind of bring it back to even uh to a degree and and hopefully have made a friend versus
[2896.02 --> 2903.06]  an enemy yeah and i worry less about uh offending people i worry more about alienating them yeah i
[2903.06 --> 2909.30]  think that uh we've got these people coming into the community now and we are you know it would be
[2909.30 --> 2914.62]  very easy for them to have a couple of bad experiences and say you know screw this i'm going to go back to
[2914.62 --> 2921.34]  being a an economics professor or whatever it is and uh i think that that's that's the thing that i worry
[2921.34 --> 2927.76]  about i worry about alienating these people that we really really want here absolutely i think uh
[2927.76 --> 2932.86]  related to that when we talk about the business case because sometimes we have to appeal to the to
[2932.86 --> 2938.94]  our to our basest desires which is you know to make more money and i think at the end of the day
[2938.94 --> 2946.94]  you know there's of course the social and the uh moral reasons of fighting towards these equalities but
[2946.94 --> 2952.40]  there's also a strong business case for diversity inside your company uh which you link to in your
[2952.40 --> 2956.36]  article do you want to touch on that real quick yeah it's interesting there's been a bunch of
[2956.36 --> 2961.14]  interesting scientific research around the fact that if what you are doing uh could be considered
[2961.14 --> 2966.30]  creative which means that there's more than one way to solve a problem which you know sounds a lot
[2966.30 --> 2973.52]  like programming to me then uh often your creative problem solving process will benefit from a team that is
[2973.52 --> 2979.76]  diverse and they may not even look on paper as qualified as a team that is less diverse but they
[2979.76 --> 2984.12]  will routinely do better and i think that that's fascinating there's also been some interesting
[2984.12 --> 2990.28]  research around uh things like startups that have women on the board are routinely more successful
[2990.28 --> 2996.24]  and things along those lines so there's a growing body of research that says that anytime you're doing
[2996.24 --> 3002.76]  something creative which includes in my opinion programming and creating products a more diverse team is
[3002.76 --> 3010.50]  actually going to get you a better outcome absolutely you also mentioned sarah um i can't remember it was
[3010.50 --> 3015.04]  it uh in the pre-call was it in the early call you mentioned your article pairing with junior developers i
[3015.04 --> 3019.40]  also wanted to talk quickly about this because it sort of bleeds into uh what you do at devmind and what
[3019.40 --> 3025.12]  you do at uh rails bridge how does all this play out i guess in what it means to pair with junior
[3025.12 --> 3032.74]  developers and that was a huge article for you and even devmind 29,234 views so congrats on that
[3032.74 --> 3039.58]  yeah in two months which is more than i was expecting for sure it's interesting because uh the ruby
[3039.58 --> 3043.84]  community is an interesting place right now because we do have um we are the vanguard for all of these
[3043.84 --> 3050.76]  new folks coming in from these code schools and so we are figuring out a bunch of stuff such as uh how do
[3050.76 --> 3054.62]  you work with someone this junior what cultural changes do you need to make within your team
[3054.62 --> 3061.74]  in order to be able to welcome a junior person into the team and what code-based changes do you need to
[3061.74 --> 3066.46]  make in order to be able to welcome a junior person into your team and so that that post was basically
[3066.46 --> 3070.68]  my first set of steps of like here's what here's what you need to do here's how you need to think
[3070.68 --> 3075.30]  about it when you're working with someone who's junior and we've had a bunch of different apprentices
[3075.30 --> 3081.20]  uh at devmind in fact we're hiring more apprentices right now and the interesting thing about it is that
[3081.20 --> 3088.84]  it really has changed both how we uh organize our teams and how we actually write software
[3088.84 --> 3092.30]  um and maybe that's the subject for another post
[3092.30 --> 3098.76]  what uh you mentioned some job opportunities at devmind where can someone go is it slash jobs
[3098.76 --> 3106.92]  devmind.com slash jobs that might be it yes d-e-v-m-y-n-d.com slash jobs since i'm asking you a rhetorical
[3106.92 --> 3111.04]  question since i knew the answer yeah that sounds great but we're on a podcast so it was not record
[3111.04 --> 3120.86]  rhetorical um yeah devmind d-e-v-m-y-n-d.com slash jobs um you got a couple there and you also mentioned
[3120.86 --> 3126.48]  your apprenticeship as well in the same area so if you're interested take a peek at that
[3126.48 --> 3132.22]  um maybe now jared's a good time to to tail into some of our super awesome ending common questions
[3132.22 --> 3139.18]  yeah let's start with uh the old saw sarah please tell us who is your programming hero
[3139.18 --> 3146.74]  who is my programming hero you can't pick just one we know there's so many we'll let you pick a couple
[3146.74 --> 3156.74]  so i've always been inspired by grace hopper who i'm sure you're familiar with who mainly because she
[3156.74 --> 3164.06]  became a programmer at the age of 39 wow she did all of her best work in her 40s
[3164.06 --> 3170.54]  and uh as someone who is heading into that direction at this point in my life we have a
[3170.54 --> 3176.24]  mythos in our culture that all of the best work is done by young people that everyone's best work is
[3176.24 --> 3181.54]  done by the time of 25 so one of the things that i love about her story is that that shows it's really
[3181.54 --> 3186.58]  not true all of the amazing work she did with the compilers and so on was all done in her 40s
[3186.58 --> 3193.28]  and that gives me hope i guess as someone who's who's getting there um that uh that maybe my best
[3193.28 --> 3200.82]  work isn't behind me yeah i i don't subscribe to that that uh rule of thought either i'm uh you know
[3200.82 --> 3208.14]  i'm post 25 i'm actually next month this month geez in a few days matter of fact next week is my
[3208.14 --> 3216.10]  birthday happy birthday bro on the same day i turned 36 36 uh yeah over the hill dude that's
[3216.10 --> 3224.90]  the thing oh man your best work is behind you oh man my best work my best work i was i was a terrible
[3224.90 --> 3229.82]  terrible programmer when i was 25 so i was too and that's the amazing thing i mean
[3229.82 --> 3236.22]  yeah yeah i don't know i have high hopes thank god for amazing grace hopper to uh show us the way
[3236.22 --> 3243.42]  awesome well another uh closing question that we ask uh you have to adjust it a little bit usually
[3243.42 --> 3248.24]  we ask what's a call to arms or something you would say to the open source community with regard to
[3248.24 --> 3253.86]  some project that you're working on but in the case of mining the gap i guess uh here's an opportunity
[3253.86 --> 3260.26]  for you sarah to have a call to arms to those listening out there uh how they can uh help you
[3260.26 --> 3266.28]  and us in this effort what would you say i would say the first thing that you can do is to volunteer
[3266.28 --> 3272.02]  at a rails bridge workshop or a rails girls workshop or or any of these other things or even at one of
[3272.02 --> 3279.98]  the code schools that's uh working with diverse students start uh start to meet people that are
[3279.98 --> 3286.28]  programmers that are not who are you're used to looking at just meeting them and even just for a
[3286.28 --> 3292.08]  day even just going in and doing doing rails bridge for a day is actually an incredibly eye-opening
[3292.08 --> 3297.18]  experience it was for me anyway and i've people continue to tell me that that is one of their
[3297.18 --> 3301.94]  favorite things about it is that they they meet people that are so different from the folks that they
[3301.94 --> 3309.90]  encounter at uh every day in their work you know that brings to mind how can someone take part in
[3309.90 --> 3315.42]  a rails bridge so what you mentioned you got mobile bridge now you got closure bridge um what's
[3315.42 --> 3320.38]  the easiest way to find out what's happening in that in those in that community at large and then
[3320.38 --> 3324.72]  those micro communities as it relates to a certain language or a certain camp that's an interesting
[3324.72 --> 3330.10]  question we've actually been thinking about that quite a bit ourselves right now the best way is to
[3330.10 --> 3337.98]  look at bridge troll um which i think it's bridge troll.org although don't quote me on that but that's
[3337.98 --> 3344.94]  where we have all of the um workshops that are coming up in all of the different bridges and uh
[3344.94 --> 3352.12]  we've been thinking about how we can evangelize both the individual communities but also you know
[3352.12 --> 3357.36]  get other communities interested in doing this type of thing um and we've got some ideas in that in
[3357.36 --> 3361.68]  that direction but we haven't quite put anything into action yet but so for now bridge troll is the
[3361.68 --> 3367.24]  best way to find out what's happening and just to confirm for everyone it is bridge troll.org so just like
[3367.24 --> 3372.72]  you could spell bridge and just like it's spelled troll bridge troll.org uh i like that i like the
[3372.72 --> 3381.72]  the the the troll too he's he's very shrek like yeah he's a friendly troll he is you know it doesn't bite
[3381.72 --> 3389.74]  exactly um let's see the next one um we should ask i'm looking through it i guess this one fits no
[3389.74 --> 3393.28]  matter what no matter who you are what's what's on your open source radar like if you had a weekend
[3393.28 --> 3397.52]  to hack on something what would it be would it be a new language would it be a new framework
[3397.52 --> 3403.08]  would it be curriculum you know what would it be for you so one of the things i've been realizing
[3403.08 --> 3409.06]  recently is that i i look at a lot of rails apps being a consultant and being someone that goes in
[3409.06 --> 3414.96]  and tends to you know sort of go into projects that are already already going already a going
[3414.96 --> 3420.10]  concern i see a lot of different code bases but they tend to all be rails apps and one of the most
[3420.10 --> 3428.70]  interesting things happened to me last week i was uh on vacation and uh i paired on fixing an rspec
[3428.70 --> 3434.48]  bug with sam pippin who's a member of the rspec core team and looking at the rspec the interior of
[3434.48 --> 3440.54]  the rspec code base was amazing because all of my assumptions that i carry with me from rails apps about
[3440.54 --> 3447.34]  what makes good code are all wrong it was really amazing and so i think at this point what i would do is
[3447.34 --> 3453.20]  i i would want to look at more look at rspec more look at other gems and the interior of them and
[3453.20 --> 3458.16]  just try and figure out like what are the different assumptions that they have that lead to such
[3458.16 --> 3466.26]  structurally different code well if you do that you should write about it so i can read about your
[3466.26 --> 3471.94]  findings that'd be spectacular i've done a conference talk about that before actually but maybe you have
[3471.94 --> 3478.86]  write it down did that get on that get on video is it online somewhere let's i think that was that's
[3478.86 --> 3484.52]  the one that i did at nickel city actually uh so i think it is on conference cool you know something
[3484.52 --> 3489.26]  that you just mentioned there too jared reminded me of a whole different post but something in the
[3489.26 --> 3495.40]  same vein and maybe we can spend a minute on this or if you've got an opinion was that um even
[3495.40 --> 3502.26]  conference talks from those who are often judged or biased against or towards i'm not really sure
[3502.26 --> 3509.46]  the best way to to sort of say that but are apprehensive about uh giving a talk because it
[3509.46 --> 3515.22]  often ends up on video there's some sort of like you know always this artifact where you just want to
[3515.22 --> 3521.68]  sort of meet in person um and i even saw um jan leon leonard uh the other day talked about i can't
[3521.68 --> 3525.94]  recall which conference but it was super neat was how they had colored bands you might know this um
[3525.94 --> 3531.44]  for yes you could take pictures of me uh maybe if you can if you ask me you can take a picture of me
[3531.44 --> 3538.20]  or no not at all um and they had different colored lanyards based on you know how you felt about showing
[3538.20 --> 3544.54]  who you are or just i guess showing your face or you know in public but having this artifact that sort
[3544.54 --> 3551.38]  of lives beyond uh beyond conferences what do you feel about the the thought of someone possibly not
[3551.38 --> 3558.08]  uh giving a proposal because they don't want to be on camera that is a really interesting thing i
[3558.08 --> 3562.78]  you know for for some people there's there's definitely some safety issues involved right
[3562.78 --> 3568.82]  you know for example someone has you know an abusive ex-spouse or something you know things like that
[3568.82 --> 3575.12]  uh where they just don't want to end up even in you know even in uh sort of incidental photos of the
[3575.12 --> 3580.82]  conference um and beyond that i think that it's good for us to support different ways of being at a
[3580.82 --> 3587.82]  conference i think that you know it's it's always the case that we can uh if we want to talk we can
[3587.82 --> 3595.36]  always you know the whether or not it's on video is can always be a point of negotiation so obviously as
[3595.36 --> 3601.18]  a conference organizer we'd love to have all of the all of the talks on video so that we can use them
[3601.18 --> 3609.52]  to promote you know next year's conference however uh it's not required um i think that we would be
[3609.52 --> 3615.00]  missing out on a bunch of talks if we made it mandatory to have them be filmed so you know as
[3615.00 --> 3619.52]  much as i would love to have films of every single talk um i don't know if you've looked at the con
[3619.52 --> 3626.96]  freak site recently but there's like thousands of them already there so uh i think it's you know if
[3626.96 --> 3630.10]  you want to do a conference talk but you don't want it to be recorded it's certainly something that
[3630.10 --> 3635.88]  you can ask the organizer about yeah i think that's the the point there too is just being able to
[3635.88 --> 3640.84]  you know sometimes when you're newer to a community you feel like you have less authority
[3640.84 --> 3646.46]  or less ability and i think part of the part of that is an invitation a sort of an open invitation
[3646.46 --> 3651.56]  to the world hey if you're coming to one of my conferences or conference i'm involved in you know
[3651.56 --> 3656.10]  if you can't go to the organizer come to me directly and if you have some concerns and we'll figure it out
[3656.10 --> 3662.20]  yeah absolutely you know i think that's the the point there well sarah it was definitely great
[3662.20 --> 3666.56]  having you on the show i know we had a little bit of rescheduling there but we uh with your travel
[3666.56 --> 3670.44]  back from denver and london and everywhere you've been where have you been out recently
[3670.44 --> 3676.74]  uh last three weeks let's see i was in denver last week and then the week before that i had a week at
[3676.74 --> 3681.00]  home and then i was in chicago and then i had a week at home there i was in melbourne australia for
[3681.00 --> 3685.94]  ruby conf au and you have a daughter too right i do i have two kids actually i have a daughter and a son
[3685.94 --> 3691.60]  daughter does either of them travel with you i'm actually about to go on my first conference
[3691.60 --> 3698.60]  trip with my daughter who's nine we're gonna go to new york so very excited good old new york yes
[3698.60 --> 3703.40]  well it's been uh it's definitely been fun having you thanks to matt to one of our members who suggested
[3703.40 --> 3708.34]  the conversation to have with you uh minding the gap but definitely enjoy the article in this
[3708.34 --> 3713.68]  conversation with you um is there anything you could do like towards rails bridge or anything around
[3713.68 --> 3717.12]  the things you're doing anything you want to mention as we're closing and in uh you know how
[3717.12 --> 3721.28]  to connect with you anyways they can step into to rails bridge or anything like that whatsoever
[3721.28 --> 3726.78]  yeah rails bridge is a is an open source organization in that we publish all of our stuff on github
[3726.78 --> 3732.00]  and that anyone can pick it up and do a workshop where they are and so we are trying to expand
[3732.00 --> 3736.56]  geographically so if you are living in a place where you think a rails bridge workshop would be useful
[3736.56 --> 3742.56]  uh do get in touch with me you can find uh email and so on on uh i believe if you look at my twitter
[3742.56 --> 3748.90]  account you'll eventually find my email and uh definitely get in touch because we are looking at
[3748.90 --> 3755.36]  um doing some geographical expansion in 2015 so when you say all of your stuff is on the github
[3755.36 --> 3762.48]  you mean curriculum right the curriculum all of our uh notes for running a conference uh sorry a workshop
[3762.48 --> 3769.04]  we actually organize all of the workshops through github issues so you can actually see workshops
[3769.04 --> 3775.12]  being organized uh we do most of our things like board meeting notes and so on also through github
[3775.12 --> 3781.12]  issues so uh we actually make fairly heavy use non-traditional use you might say of github in order to
[3781.12 --> 3789.44]  have a very open process awesome well sarah it has been a pleasure uh we'll link up your twitter
[3789.44 --> 3793.84]  and your github on the show notes so if you're a listener go to the show notes for the show it's
[3793.84 --> 3799.52]  episode 146 get links out to sarah and all the stuff we've talked about today so if you've got any
[3799.52 --> 3803.28]  questions whatsoever don't worry about trying to jot down the link while you're trying to drive and
[3803.28 --> 3808.00]  listen to this podcast just add to the show notes they're going to be there uh and with that everybody
[3808.00 --> 3812.16]  let's uh let's go ahead and call this a show and say goodbye all right well thank you so much for
[3812.16 --> 3826.00]  having me thanks for coming on sarah appreciate it
[3826.00 --> 3828.00]  you
[3842.16 --> 3844.16]  you
