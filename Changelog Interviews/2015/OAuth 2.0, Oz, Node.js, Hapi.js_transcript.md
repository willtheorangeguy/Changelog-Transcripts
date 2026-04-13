[0.00 --> 17.20]  welcome back everyone this is the changelog and i'm your host adam stekowiak this is episode 178
[17.20 --> 24.02]  and on today's show jared and i are joined by aaron hammer for an awesome show on happy node
[24.02 --> 30.24]  oauth and a deep discussion around security specifically talking about oz aaron's
[30.24 --> 39.00]  replacement for oauth 2.0 we had four awesome sponsors for the show code ship top tile casper
[39.00 --> 45.94]  and imagix our first sponsor of the show is code ship there you hosted continuous delivery service
[45.94 --> 52.78]  focusing on speed security and customizability you can easily set up continuous integration for your
[52.78 --> 57.36]  application today in just a few steps and automatically deploy your code when your test
[57.36 --> 64.76]  pass code ship has great support for lots of languages test frameworks notification services
[64.76 --> 70.60]  and they even integrate with github and bitbucket and you can deploy to cloud services or even your
[70.60 --> 77.54]  own servers get started today with their free plan when you upgrade to a premium plan use our code
[77.54 --> 85.04]  the changelog podcast and with that code you'll save 20 off any plan that you choose for three months
[85.04 --> 92.28]  again that code is the changelog podcast head to code ship.com slash the changelog to get started
[92.28 --> 94.32]  and now on to the show
[94.32 --> 109.98]  all right we were back we got myself here jared here we have aaron hammer back on the show now aaron
[109.98 --> 113.88]  it's been wow i don't even know how long it's been at least a year and a half since you've been on the
[113.88 --> 119.32]  show the last time you're on here we were talking about uh node at walmart and black friday what a
[119.32 --> 125.70]  triumph that was so welcome back to the show hey glad to be back and uh aaron i guess i don't want
[125.70 --> 129.42]  to do your intro for you but whenever you come on a show like this how do you introduce yourself
[129.42 --> 141.42]  oh it's uh it got much easier now um yeah i'm uh i'm the uh uh the founder of uh of a very early
[141.42 --> 148.56]  state startup called sideway um trying to make sharing conversations uh more interesting and fun
[148.56 --> 160.22]  um really early stage um and before that i spent three and a half years at uh walmart uh leading the
[160.22 --> 170.24]  uh mobile web services team uh building among uh other things um quite a big portfolio of uh open source
[170.24 --> 179.94]  projects for node um for building server side applications so that's uh that's kind of where i am
[179.94 --> 190.76]  before that i spent a bunch of time doing web standards and um and working on security related protocols
[190.76 --> 201.66]  like oh uh and you mentioned um you mentioned sideway the your very early stage startup is anything you
[201.66 --> 206.26]  can mention about that whatsoever anything you can share that's uh kind of secret maybe no one knows
[206.26 --> 217.42]  about um well i talk about a lot i just don't write about it a lot um basically um it's trying to kind of
[217.42 --> 226.14]  fill the gap between the high noise low barrier um social media sites like twitter and instagram and
[226.14 --> 231.70]  pinterest um where people can express themselves but it's very hard to find audience and there's it's
[231.70 --> 237.82]  very hard to consume it because it's very very noisy and very low quality low value um but it's so you
[237.82 --> 243.00]  know there's gems here and there and on the other side you have um the full blogging platforms you know
[243.00 --> 250.38]  if it's wordpress and medium and and all those where it's it's pretty tedious and expensive to to
[250.38 --> 259.94]  produce content i mean everybody i know has a blog post idea every day and they rarely write it
[259.94 --> 266.78]  and so because it's it's a lot of work um you have to write and you have to do spell checking on it and
[266.78 --> 271.90]  grammar and then you have to make sure it's linked and has high value and all that so
[271.90 --> 279.80]  what i'm trying to do is kind of like people um convert conversations into content you know we have
[279.80 --> 286.32]  all of these uh kind of like podcasting but written um and so you'll have a conversation and when you're
[286.32 --> 291.96]  done with the conversation the transcript becomes um the actual content that you're producing and people
[291.96 --> 298.86]  can follow the conversation live as it's happening um but then when it's over they can read the
[298.86 --> 309.00]  transcript um and so there's a lot of work involved in building a new kind of uh basically chat experience
[309.00 --> 315.90]  that is not optimized for your real-time communication needs but is optimized for producing
[315.90 --> 323.88]  a great conversation because if you if you look at your chat transcript that you're having whether it's
[323.88 --> 332.34]  you know hangouts or slack or whatever whatever it is um they're pretty terrible um so you know they're
[332.34 --> 337.94]  they get the job done for uh communicating something in the moment but if you're trying to read the
[337.94 --> 345.40]  conversation on those on those tools um after the fact um it's it's just completely um
[345.40 --> 353.10]  useless and so the challenge here is to come up with the right user experience that can basically
[353.10 --> 365.34]  convert these kind of conversations into really great um written uh transcripts so you know whether
[365.34 --> 373.36]  it's an interview or um more of a town hall style or just a casual conversation so is this something
[373.36 --> 378.14]  that you're starting yourself or is this something that you're starting with other people um i something
[378.14 --> 387.28]  i started myself um recently closed a small seat round and um hired um the of my first employee
[387.28 --> 395.74]  um so we're a team of two now and um yeah so that's what i'm doing uh spending most of my time on
[395.74 --> 403.12]  these days um i'm also doing a significant amount of open source work you know keep keeping happy going
[403.12 --> 412.30]  and uh and also doing um a good chunk of uh uh consulting work um with a great company called near form
[412.30 --> 421.10]  um so yeah keeping myself busy interesting so seed rounds a little bit of side work a little bit of
[421.10 --> 425.90]  open source work obviously because you can't put that down uh especially whenever you did such a good
[425.90 --> 430.38]  job transitioning happy whenever you left walmart what what can you share about uh your departure
[430.38 --> 434.86]  from walmart and just sort of the the i guess whatever you want to share about your personal
[434.86 --> 439.58]  breakup i think you blogged about it quite quite well but specifically around the community around
[439.58 --> 442.78]  happy and how well that transition is there any insight you can share with the open source
[442.78 --> 453.74]  community about that it was pretty clear internally um about uh two years ago that the organization
[454.62 --> 462.22]  is is getting was getting to a point where they got what they wanted out of the project and that the
[462.78 --> 468.78]  the the resource spent wasn't really sustainable at those levels moving forward for this particular
[468.78 --> 476.94]  project so basically the the the feature said that that happy was providing walmart uh seems to match
[476.94 --> 484.86]  their requirement quite well um and beside bug fixes and small enhancements it it was clearly moving
[484.86 --> 492.06]  into a direction where uh we couldn't justify having four people full-time working on on that piece and so
[492.06 --> 500.22]  we worked really hard in order to uh increase outside involvement and you know it was it was done in
[500.22 --> 510.06]  in two like the long tail and the and the super high quality um involvement so we we built relationship
[510.06 --> 516.54]  with companies that you know had interest in happy and made sure that um they're also contributing resources
[516.54 --> 521.66]  to the project and at the same time we uh made sure to put a governance model in place that
[521.66 --> 534.62]  will really um reduce uh walmart's presence um in terms of control and um somewhat you know association
[534.62 --> 540.06]  um with the project so that people outside feel more comfortable contributing and getting the credit that
[540.06 --> 546.06]  they deserve um without feeling like now either they're affiliated with a company that they don't
[546.06 --> 551.58]  necessarily want to be affiliated with or just giving you know giving free work to walmart to been
[551.66 --> 560.46]  then go and boast about so um this was a long process and it was a not just a community process it was
[560.46 --> 566.22]  an engineering process because um in order to get more contributions and diversify your community
[566.94 --> 572.62]  you need to have more active developers it's i'm a big believer in the benevolent dictator model of
[572.62 --> 578.54]  open source i don't like other models very much um i think there should be someone in charge and someone
[578.54 --> 583.26]  who can make the the final decision and if you don't like it you can fork and do your own thing
[583.90 --> 589.74]  that's something that uh actually in our last show uh jared you can help me out with this but ron he was
[589.74 --> 595.74]  like uh he was just lamenting on just just uh with open source how you can go and say like trying to
[595.74 --> 600.06]  find who's in charge and like he's saying you can go back and listen to him he's like no one's in charge
[600.06 --> 606.14]  like ah how it drives him crazy because yeah you get uh it's good for open source that it is open but
[606.14 --> 611.10]  it's bad that there isn't really someone in charge that can say like here's where we're going and and
[611.10 --> 618.14]  drive it like you said with the edfl model right so um what what a few things happen you know one
[618.14 --> 624.06]  happy got too big for me to be the uh i couldn't really be benevolent
[624.06 --> 632.54]  um it became it became a huge amount of work um it and i got to the point where i was slowing things
[632.54 --> 638.54]  down because we had 30 to 50 modules and i was basically responsible for all of them and i just
[638.54 --> 646.94]  it just was too much so um and core happy core got so big that um you know like we had everything
[646.94 --> 653.34]  inside the the the router was inside cookie parsing was inside a bunch of security stuff was inside
[654.06 --> 663.42]  um file processing you know v rendering like all these features and what we did is we broke it up
[663.42 --> 669.90]  and everything that that could be moved out was moved out so it was it wasn't a question of what what
[669.90 --> 675.90]  belongs or did not belong in court was can we from an engineering perspective move this piece of software
[675.90 --> 682.86]  somewhere else and everything that we could we moved out um so we kind of smashed the core framework
[682.86 --> 692.54]  into a lot of tiny little pieces and then basically said hey who wants what and and in order to to take
[692.54 --> 697.82]  over one of the those pieces all you had to do is just kind of show up and start working on it you know
[698.38 --> 704.86]  they all had no documentation so the first thing you do is you go add documentation and and kind of clean
[704.86 --> 712.22]  up the code and add more tests and um show that you're willing to put in the time on the you know
[712.22 --> 717.10]  kind of annoying pieces right if someone is willing to do documentation that's a good sign that they
[717.10 --> 725.82]  would be willing to do the the much more uh exciting work of writing code and so um we did all that at the
[725.82 --> 733.50]  same time we also want to make sure that we're um welcoming to everybody so we put in a um
[733.50 --> 741.98]  um code of conduct we put in um we put a bunch of effort into getting um a more diverse core team
[741.98 --> 750.54]  so we recruited uh prominent community members um that are not just um white men um in order to kind
[750.54 --> 757.90]  of change the face of the project so the project is um more welcoming to everybody and and the goal
[757.90 --> 762.78]  wasn't necessarily to like you know have better statistics about how many people are you know from different
[763.50 --> 768.46]  um backgrounds are participating it is more that if someone comes in they look at the the project
[768.46 --> 776.86]  pages who are the team they can say okay well you know i i can i can see people like me there i mean i'm
[776.86 --> 784.70]  not going to be like you know the the first of my um unrepresented group in in our environment and
[785.26 --> 793.02]  um i'm not sure how actual success we had ultimately in in changing the the percentages but at the same time
[793.50 --> 799.58]  um i think that that we create a very welcoming environment so that that you know and some of
[799.58 --> 803.26]  the stuff succeeded some of it didn't work we tried to do a mentoring program but that
[804.14 --> 808.78]  is something that we're still trying to get working but it's so much effort to maintain it that um
[809.42 --> 817.18]  you know that that's always tricky but um yeah so we we kind of broke into pieces put a governance model
[817.18 --> 823.34]  that is kind of codifying how the relationship is between the different modules and the different
[823.34 --> 829.98]  you know lead maintainers who are uh their own you know little benevolent dictatorship for their their piece
[831.82 --> 840.06]  so we did put all in place um we got i think at this point um walmart employees account for probably
[840.06 --> 851.90]  um one to four percent of the active maintainers on the on the ecosystem as a whole um and that was that
[851.90 --> 861.02]  was great so it it was a long process but it was a very planned um process in order to take something
[861.02 --> 866.70]  that was very much a corporate sponsorship setup and move it into a completely community-based
[866.70 --> 874.06]  um environment and and we actually uh recently introduced a sponsorship policy so that um
[874.06 --> 880.14]  companies can get their logos and their name uh associated with the happy module so that they you know
[880.14 --> 884.62]  people who are getting paid by their company to do this work can give some benefit back to their
[884.62 --> 890.06]  for their company and notice in the readme that the sideway logo is there actually so that there is
[890.06 --> 898.38]  some sort of sponsorship option for happy yeah um that one is funny basically the i kind of calculated
[898.38 --> 908.30]  and the cost um kind of like my lost wages on happy work every month uh is between uh it's between
[908.30 --> 915.10]  three to six thousand dollars a month um in terms of if if i take the hours i'm spending on the project
[915.10 --> 926.78]  and i was just bill for them at my um extremely overpriced rate um and so i kind of decided like
[926.78 --> 932.46]  i'm not quite ready to go and get other people to to do the sponsorship i'm i'm almost there i'm
[932.46 --> 937.98]  probably like a month or two away from that um i'm probably gonna wait for another major release
[937.98 --> 944.78]  and then um i'll just say hey if if the company wants to put their name on the on the readme uh
[944.78 --> 951.66]  get a few tweets um from the happy account about the sponsorship and um you know basically cover
[952.86 --> 959.82]  my my cost uh of doing this work then i'm probably gonna do that um just kind of a
[960.54 --> 965.74]  two three months arrangement um but for now you know basically when i do happy work that is not
[965.74 --> 971.90]  directly benefiting my own startup then it's basically my startup is paying for it right in a
[971.90 --> 982.22]  way um and so yeah so i put that up there um we'll see where it goes uh it's it's it's kind of you know
[982.22 --> 991.34]  a new new territory uh i haven't really seen projects um doing that kind of of uh temporary sponsorship of
[991.34 --> 997.10]  open source that's interesting i think it's a interesting model if if someone that was listening
[997.10 --> 1000.46]  and they were like hey i want to sponsor happy one month or something like that how would they
[1001.26 --> 1005.74]  submit an issue get in touch with you privately what's the best way oh whatever they want they
[1005.74 --> 1010.46]  can my email is all over the place they can do what they actually know yeah any whatever they're
[1010.46 --> 1016.86]  comfortable usually companies don't want to be public about asking to sponsor um and so you know my
[1016.86 --> 1023.42]  email is everywhere it's aaron at hammer.io i mean if you can't find my email then you probably can't
[1023.42 --> 1029.98]  read there you go it's always interesting to think about the the copyright and the licensing
[1029.98 --> 1035.90]  permission and goes into these sponsored community projects especially one that seemed to like spawn out
[1035.90 --> 1040.62]  of walmart and then become a community project looking at your license it looks like there's multiple
[1040.62 --> 1048.54]  copyright holders can you speak to that yeah so copyright is really simple um it's basically
[1048.54 --> 1055.58]  whoever creates something has the copyright and then um you can't technically ever waive your
[1055.58 --> 1061.50]  copyright you can assign it and you can kind of like give it to someone else but um copyright law is
[1061.50 --> 1067.26]  really really tricky and also doesn't really matter much because for for the most part you can't really
[1067.26 --> 1073.90]  sue people for the vast majority of copyright on code um but the bottom line was um we kind of asked
[1073.90 --> 1080.78]  everybody and um we kind of looked at how the bsd license is set up and if you and if you see the
[1080.78 --> 1087.66]  license it just says that you can you need to retain the copyright statement from any previous code you've
[1087.66 --> 1095.50]  used and you need to retain the terms um you don't have to retain them as an atomic unit so originally
[1095.50 --> 1104.62]  um happy started with yahoo and um a lot of the initial code just was just lifted from the postmile
[1104.62 --> 1110.78]  project that i worked on at yahoo and then yahoo open source uh before i left and that was copyrighted
[1110.78 --> 1117.18]  uh to yahoo and if you look at the happy corp uh license it's basically saying it's copyright to yahoo
[1117.18 --> 1124.94]  it's copyright to walmart it's copyright to other people um anybody who contributes um basically has a
[1124.94 --> 1131.98]  piece of the copyright uh and then by contributing you're basically buying into the bsd uh license
[1131.98 --> 1139.90]  that's sitting there so it's at some point it became just hard to maintain that list of copyrights
[1139.90 --> 1144.62]  because every pull request you technically need to go and add that name to the license so we just
[1144.62 --> 1148.62]  added the link we asked the lawyers and the lawyer said yeah it's perfectly reasonable that you know you
[1148.62 --> 1153.42]  have a link to say you know here are the main copyright holders you know the vast majority of the code but
[1153.42 --> 1161.74]  then there's all these other people and so uh copyright is held by whoever contributed piece of code
[1161.74 --> 1168.86]  if they work for an employer then their employer has whatever rights they agreed to and um all we do
[1168.86 --> 1178.30]  is we just say hey all of you are bound by this license agreement and so when when it's time to decide on
[1178.30 --> 1183.66]  a new project um like who gets their name on the license who gets the other contributors right that's
[1183.66 --> 1191.26]  kind of the main question people have and to me it's uh usually whoever starts something get their name
[1191.26 --> 1198.38]  so whether everything i started walmart walmart got their name there everything i started um after i've left
[1198.38 --> 1203.82]  got my name on it um if something was started by someone else then they can choose who they want
[1203.82 --> 1214.46]  uh to be the primary uh copyright holder on um ultimately it doesn't really matter um as long
[1214.46 --> 1220.94]  as it's not out of control so i i would say that if um i'm contributing significantly to to something now
[1221.50 --> 1225.98]  that was started somewhere else i might go and add my name as another copyright holder because i'm doing
[1225.98 --> 1232.78]  significant work but it's it's kind of more of like a credit for big contributors um than anything
[1232.78 --> 1238.54]  legal the other contributors clause kind of covers it and in practice because it's only a copyright
[1238.54 --> 1245.58]  license um and it's a very liberal one it doesn't really matter at the end you can't really do anything
[1245.58 --> 1253.26]  about anyway um yeah was it bsd from day one yep yeah it was it was three clause bsd from day one
[1253.26 --> 1259.26]  uh that's the one that the yahoo lawyers asked to use and since that was the one you know once you
[1259.26 --> 1267.02]  switch to something else um and let's face it all the copyright all the like mit and bsd and all those
[1267.02 --> 1272.14]  are exactly the same um you know one will give you a little bit of liability the other one will give
[1272.14 --> 1277.58]  you a little bit of you know brand protection but it's all all nonsense it's basically do whatever you
[1277.58 --> 1283.02]  want and you know if we sue you the person who has the more more money will win anyway
[1284.94 --> 1289.82]  so were there conversations uh at walmart about licensing or was it just you know you were trusted
[1289.82 --> 1298.06]  to do what you thought was appropriate um we had i had come see with the lawyers uh the walmart lawyers um
[1299.42 --> 1305.90]  were focused more on trademark issues than copyright issues um it's you know it's a bigger concern for them
[1305.90 --> 1314.94]  um trademark is uh especially for for a company that's you know basically selling brands um and is
[1314.94 --> 1322.70]  in business with pretty much every every manufactured good electronic or otherwise in the world um the
[1322.70 --> 1328.62]  the trademark relationships are really um are really strict and so they want to make sure that they're not
[1328.62 --> 1335.34]  opening themselves for liability and they're not um and that you know people can go out after the fact and
[1335.34 --> 1341.90]  kind of take credit for for the work so um what we've done is um i've kind of worked with them um and
[1341.90 --> 1349.74]  that's really um great team uh the legal team there um and we basically did two things one we made sure that
[1349.74 --> 1355.66]  none of the marks were using our trademark with anybody else uh worldwide so we're not infringing on anybody
[1355.66 --> 1363.34]  else's work and at the same time we kept everything public domain so as a matter of policy we did not trademark a single
[1363.34 --> 1371.66]  happy related um mark now no logos or names and so they're basically in the public domain so in
[1371.66 --> 1377.90]  practice everything is just covered by the bsd license um there are no trademarks in happy it's all
[1377.90 --> 1384.94]  just copyrighted stuff um and you can do whatever you want with it um that covers the logo it covers
[1384.94 --> 1390.14]  everything else um we even removed like the copyright statement from the website you know it's basically the
[1390.14 --> 1399.18]  same as every all the other licenses so it's um it's a little different i think now um i think that
[1400.14 --> 1408.38]  happy was the very first um meaningful open source project done at walmart and so um the organization
[1408.38 --> 1414.62]  was catching up with us um we were basically doing things and after the fact they came and said oh i guess
[1414.62 --> 1421.10]  we're doing open source now so maybe we should have a policy about it and so we um as a general the
[1421.10 --> 1426.14]  the team i was part of um i can say it freely now because pretty much everybody that is relevant has
[1426.14 --> 1434.94]  left um as well um over the last year but basically uh we were kind of like you know uh do and ask
[1434.94 --> 1441.90]  forgiveness kind of attitude versus first you know go through the entire corporate ladder and make sure it's uh
[1441.90 --> 1451.42]  it's all approved um but in practice um i mike i had extensive um engineering ip experience um you know
[1451.42 --> 1459.26]  i play a lawyer on the internet and having having done um three full years at yahoo working with a legal
[1459.26 --> 1466.38]  team there on exactly this kind of stuff um all about you know copyright and patents and and trademarks um
[1466.38 --> 1471.74]  i have a pretty solid understanding of it so whenever we did something without asking permission
[1471.74 --> 1477.74]  the lawyers came you know um semi freaking out about it and i was saying oh yeah we know here's where we
[1477.74 --> 1483.18]  did this and here's we did this and here's what the policy they were like oh uh i guess you know
[1483.18 --> 1489.34]  everything about this already um and so that was really helpful it really helped create uh the kind of
[1489.34 --> 1495.50]  trust that um that they needed in order to feel comfortable that we're not doing something you know
[1495.50 --> 1502.22]  particularly stupid yeah um and then the other thing is which made things really easy um and
[1502.22 --> 1509.58]  that's kind of like an advice for everybody who wants to game the system is um if you fork something with
[1509.58 --> 1517.02]  a license you're basically make you you're making yourself life you're making yourself sorry you're
[1517.02 --> 1523.98]  making your life really easy um because you can just inherit what's going on there and the lawyers can't
[1523.98 --> 1530.46]  really argue anymore because it's kind of required for you to keep sustaining that license so find
[1530.46 --> 1537.66]  yourself a product with very little code fork it and change to something else but it's like a loophole in
[1537.66 --> 1546.30]  all these big corporations um and so i know i can't do the extreme but basically uh if you join a company
[1546.94 --> 1551.82]  if you the day before you join you go and open source a tiny little piece of code and then you continue working on it
[1551.82 --> 1556.46]  then it's much easier to get the legal team to just agree with the terms that you set up there
[1556.46 --> 1561.58]  than if you're starting from scratch and now you have a so all we need is a bunch of shell projects
[1561.58 --> 1566.70]  with each license available for forking and then people can do much uh it needs to have
[1566.70 --> 1571.50]  work away the empty empty folders you need to have some meaningful some something in there so that when
[1571.50 --> 1575.74]  you go to the legal team because they're you know the the big big shot lawyers are not stupid so
[1575.74 --> 1580.94]  they'll say hold on there's no code here so why can you just start from scratch right so there there
[1580.94 --> 1586.78]  or basically is if you are forking a project like jared said that's sort of a shell project to the
[1586.78 --> 1593.02]  license only yeah so uh it's helpful if you're starting from something that it has some meaning
[1593.66 --> 1598.94]  and some value to what you're doing but it's really a great system because because once you once you fork
[1598.94 --> 1610.70]  an existing piece of work um the default requirement is to just keep that um because switching licenses is
[1611.26 --> 1615.90]  tricky because now you have dual licenses and some code is under this something under that and nobody
[1615.90 --> 1622.22]  likes that um it's also generally easier for most companies to allow you to contribute to an open
[1622.22 --> 1630.30]  source project than to open source their own stuff um and so really if you if instead of creating original
[1630.30 --> 1637.50]  work you are doing a fork or uh contributing something else um the legal stuff within big companies becomes much
[1637.50 --> 1644.22]  much simpler to manage so there's there's a lot of way of gaming the system but ultimately uh if if you
[1644.22 --> 1653.66]  want to make your life easier in in a big uh corporation um being being um verse in the the area is really
[1653.66 --> 1660.06]  important because the lawyers if they feel comfortable then they let you do a lot more um i mean the same thing with
[1660.06 --> 1669.26]  security i mean i did i got yelled at multiple times for posting you know uh code snippets on on just um
[1669.26 --> 1674.70]  from like walmart code like during black friday and the infosec team you know immediately found it and
[1674.70 --> 1681.26]  freaked out that you know there's walmart code now being shared and it has port numbers and other security
[1681.26 --> 1686.62]  stuff and so they freaked out and and um i was immediately called to the principal office and um
[1686.62 --> 1693.66]  and um and i was immediately able to tell well i said you know first of all um you know maybe you
[1693.66 --> 1699.58]  look up who i am and then they looked up and oh okay we're using all his protocols for security so
[1699.58 --> 1704.86]  maybe he knows something and then um i said uh what your concerns are and they said like you know you
[1704.86 --> 1709.34]  can't publish this and this and this and this and i said well all the ports have already been changed
[1709.34 --> 1715.58]  all the sensitive uh paths have all been you know changed so basically what we posted is exactly what
[1715.58 --> 1721.02]  we're running only not and everything and everything that's meaningful for anybody to understand that
[1721.02 --> 1726.54]  internal topology has been already changed um in a in a random way so that it's not even
[1727.74 --> 1732.94]  and so they they saw that and they were like oh i guess it's okay then and then the next time it
[1732.94 --> 1736.46]  happened they basically said like we just want to confirm that you did that already on all this stuff
[1736.46 --> 1742.38]  right it wasn't like freaking out it's just like we just want to cover our ass that you know yes we um
[1742.38 --> 1747.50]  um we have we have told you that you can't post this confirmation and you agree that you didn't
[1748.06 --> 1756.30]  um so it's if you give the you know a lot of these uh these policies are important but at the same time
[1756.30 --> 1762.30]  the people who enforce them are sometimes they care more about protecting their jobs than protecting the
[1762.30 --> 1768.38]  actual ip or security of the environment and if you just make them comfortable then that goes a long way
[1768.38 --> 1773.90]  i'm glad you mentioned black friday because that kind of leads us into the next quick topic i wanted
[1773.90 --> 1779.02]  to mention but i do want to take a quick break before we do that so let's break and hear from a sponsor
[1779.58 --> 1785.82]  and when we come back we're going to talk a bit about node uh specifically the the foundation the
[1786.78 --> 1791.18]  formation of io and then a lot of stuff that's changed since then so we'll be right back
[1791.18 --> 1804.06]  say hello to top towel designers our friends at top towel have done something really really awesome
[1804.06 --> 1811.34]  they've expanded into a new market they're talking designers top dot has been known as a thriving
[1811.34 --> 1817.18]  network of some of the best software developers and engineers out there many of the developers in
[1817.18 --> 1822.94]  their network know extremely talented designers and they've always had this sort of informal
[1823.58 --> 1828.54]  relationship with designer involvement in top town they've done a little bit you know but it hasn't
[1828.54 --> 1835.74]  been an exact um you know product so to speak or internal model and so they've expanded they've
[1835.74 --> 1843.10]  evolved today uh they're extremely excited to announce the official launch of top towel designers what
[1843.10 --> 1848.14]  this means now is the same experience that you've had on both sides of the fence whether you're
[1848.14 --> 1853.66]  someone that's looking for really awesome designers or you're a really awesome designer looking for
[1853.66 --> 1858.86]  really awesome opportunities this is the place for you not only if you're engineers but also if
[1858.86 --> 1864.94]  you're designers out there as well so designers listen up it is time to go check out top towel.com
[1865.50 --> 1872.22]  designers that's t-o-p-t-a-l dot com slash designers and tell them the change law sent you
[1873.10 --> 1879.66]  all right we're back with uh aaron hammer and aaron it's it's been a while since you've been on the
[1879.66 --> 1885.10]  show and the last time you're on the show you were talking about node's performance with uh at
[1885.10 --> 1890.78]  walmart on black friday that was a pretty interesting conversation and that as a matter of fact um me and
[1890.78 --> 1895.66]  and andrew thorpe uh was was hosting the show then and jared you weren't on that show so that's a bummer
[1895.66 --> 1904.94]  um but since then uh node was was fort io js was created the node js foundation was formed and
[1905.42 --> 1909.98]  ultimately io and node decided to reconcile i haven't been keeping up day to day for the past few
[1909.98 --> 1914.62]  months on exactly what's going on there so if you know anything feel free to scold me but you did write
[1914.62 --> 1921.34]  a post uh that had some pretty clear thoughts from you and just uh quoting one thing you said was for
[1921.34 --> 1926.06]  the sake of full disclosure i'm generally opposed to any foundation and this was uh why do not
[1926.06 --> 1930.14]  support a node foundation and this is probably back in that drama days but what's what's happened
[1930.14 --> 1934.06]  since the last time we talked to you around node that is interesting to you that you like to talk about
[1934.06 --> 1941.26]  uh here on the show so i think a bunch of interesting things have been going on one is that contribution
[1941.26 --> 1951.10]  and participation has really um skyrocketed um i think that the drama part um was
[1952.14 --> 1959.90]  somewhat necessary given that um you know there are corporations involved and and legal uh agreements
[1959.90 --> 1963.82]  and and copyright and names and all that stuff and trademarks and um
[1965.98 --> 1972.30]  it took about a year of this this path um a little little tortured path but it was it took about a year
[1972.30 --> 1980.46]  to get to a point where the community could fully own the project um and and kind of set course and
[1980.46 --> 1987.50]  decide on the things that that mattered um i i don't like foundations in general i think it's a it's a um
[1989.98 --> 1991.74]  i think it's a it's just like you know
[1994.22 --> 2000.62]  a way for for people to make a living off um corporate money without really adding value um i'm
[2000.62 --> 2006.54]  not accusing the node foundation of any of that and right now um you know most of the work is done by
[2006.54 --> 2014.38]  michael michael rogers who is awesome um and um in general michael gets a blank check from me um in
[2014.38 --> 2020.46]  terms of trusting him to do the right thing uh for the project in the community so i'm okay with with
[2020.46 --> 2027.58]  with the current staffing um i don't really care much about the foundation part i kind of think it's
[2027.58 --> 2034.22]  unnecessary and i personally don't find any use for it um i was doing just fine working with the the
[2034.22 --> 2039.58]  joint people i i had great collaboration with them and if now i have to collaborate with with someone
[2039.58 --> 2045.50]  else that's fine um the more interesting part for me is the is the fact that the project now has
[2045.50 --> 2052.70]  significant amount of contribution and is able to move faster um io was a good phase as well because
[2052.70 --> 2059.34]  it kind of like gave all these new uh contributors and new core core members it gave them a little
[2059.34 --> 2069.34]  sandbox to kind of play and mature and and and grow up and understand how to uh run a project with you
[2069.34 --> 2078.22]  know tremendous amount of uh um influence and importance um in a responsible way when io was
[2078.22 --> 2083.90]  going on i didn't really want to touch it because it was like it was just crazy uh the amount of changes
[2083.90 --> 2094.86]  and the amount of of um just uh modification and and um add-ons and just just noise that was going on
[2094.86 --> 2101.74]  was just unmanageable um i can't imagine anybody with a day job that is not full-time working on node
[2101.74 --> 2106.70]  uh core was able to keep track of anything that was going on there and i think that's kind of a lot
[2106.70 --> 2112.22]  of people felt and the people who were using io were primarily the people who either just like the
[2112.22 --> 2116.70]  latest of anything and they don't really care much about it or they just really needed the new v8
[2116.70 --> 2126.22]  features you know the new es6 and and so on and and that was not available to them uh in the the 010 um
[2127.26 --> 2136.54]  releases so now things are kind of different and i think that uh version 4 represents a significant
[2137.10 --> 2145.42]  milestone for the project um i've been using it for a couple months now um i'm really satisfied with it
[2145.42 --> 2149.42]  i'm using it for you know for sideways that was going to be all starting from node 4 i'm using
[2149.42 --> 2156.22]  node 4 for another another project i'm doing um as part of my my consulting work um as far as i'm
[2156.22 --> 2162.62]  concerned that's what everybody should be it will take a few more months before some some big players
[2162.62 --> 2168.54]  will um move their environment to node 4 and kind of come back and say yes you know we're running it at
[2168.54 --> 2173.98]  scale and it's working really well for us you know the the the kind of you know walmart black friday memory
[2173.98 --> 2181.74]  leak story um we know it's you know there's there's more of those in there um and so we just need
[2181.74 --> 2188.30]  somebody to find those first uh or at least give us the the confidence to know that uh the the code
[2188.30 --> 2193.26]  base is sufficiently solid that even if there are problems they're not going to be devastating for you
[2193.26 --> 2198.94]  once you reach scale um i don't think we're far from that point i think we're almost there um but
[2198.94 --> 2205.18]  that's kind of where it is and as far as you know i'm concerned you know like i moved happy to node 4
[2205.98 --> 2215.90]  version 10 is um no longer supporting uh happy uh node uh 0.10 um it still works with it but uh we
[2215.90 --> 2222.06]  don't run any tests with it so we are no longer guaranteeing that it will work and also we have said
[2222.06 --> 2230.54]  that uh even you know within um version 10 we're going to start using uh node um version 4 features
[2231.26 --> 2236.62]  in there so we're going to start using constant let and uh error functions and a bunch of those features
[2237.42 --> 2243.02]  um that will completely break on on 0.10 so what are some features in node 4 that have you excited
[2243.98 --> 2251.02]  i primarily i'm mostly excited about just the project using a newer v8 honestly um i'm not one of the
[2251.02 --> 2256.86]  the those people who are super excited about all the new language features um i'm excited about let
[2256.86 --> 2266.22]  and const um just because they finally make sense in terms of uh um proper scoping of variables um but
[2266.22 --> 2272.14]  uh the the other features i don't really care about that much i'll i'll see how i like them as i use
[2272.14 --> 2279.02]  them more um i'm probably just i probably just just want to get access to the latest v8 the performance
[2279.02 --> 2287.34]  improvement improvement are significant the um amount of uh bug fixes um that are included the fact
[2287.34 --> 2294.30]  that it's um running the same version as chrome uh which makes it a lot easier for quick testing of
[2294.30 --> 2302.54]  things and um kind of having the same performance profile across the um client and server so and i think
[2302.54 --> 2310.06]  those are those significant uh improvement but i also um i'm glad that the the project is has more
[2310.06 --> 2317.98]  people working on it and so it's uh the team is more responsive now to issues um and it's kind of more
[2317.98 --> 2324.30]  um more democratic now it's you don't need to have did you ever have any particular issue with with
[2324.30 --> 2333.34]  joyant and it's it's uh the way it kind of helped node move along um not not really um i i'm a big fan
[2333.34 --> 2341.42]  of joyant and i i felt that up until the point where the foundation discussion started i felt that they
[2341.42 --> 2350.54]  did a pretty good job um leading the project and and um promoting the the values that were of main
[2350.54 --> 2359.34]  concern to me which was mostly stability um and um and security and performance and and those things
[2359.34 --> 2367.58]  were working well um i think that there was a lot going on both internally at joyant uh with a new ceo
[2367.58 --> 2373.82]  and some internal changes as well as around the community with a bunch of new startups uh focused
[2373.82 --> 2383.42]  on node and trying to um make a living off node as well as more um more of the the big the big players
[2383.42 --> 2391.02]  you know if it's uh um ibm and and oracle and others like that who start showing interest and it got to a
[2391.02 --> 2400.62]  point where um the status quo was clearly not sustainable and i i think that um at that point um joint
[2400.62 --> 2411.82]  in hindsight could have um managed that transition uh better but um that said um i don't think that
[2411.82 --> 2418.70]  you know they were um completely unreasonable in the way that they acted and ultimately um you know with
[2418.70 --> 2427.02]  their new ceo um they they came to the right conclusion and they did a a pretty smooth transition
[2427.02 --> 2432.94]  um to the environment um to the environment and to the foundation and at the same time the definition
[2432.94 --> 2442.62]  was set up um purposely to make really easy to merge it with with the io uh community so that um you know
[2442.62 --> 2451.10]  that that was all done um very well so there's you know there you have the typical um corporate uh um
[2451.82 --> 2456.06]  flexing and and kind of trying to um
[2457.90 --> 2462.38]  trying to get the most out of the most out of the situation for your shareholders and your own
[2462.38 --> 2468.86]  your own corporate needs but ultimately i i think that this this it took time because it was a it was
[2468.86 --> 2474.94]  a dramatic change and people had to get comfortable with it especially within their their uh corporate
[2474.94 --> 2482.46]  boards um but i i don't really think you know that i was an insider and i was i was privy to pretty much
[2482.46 --> 2487.18]  everything that was going on from the very very beginning uh i mean i knew about the things going
[2487.18 --> 2493.58]  on even before all the other players knew about them just because uh i kind of was in the middle and
[2493.58 --> 2499.74]  and everybody was was treating me as a as a confidant so i kind of was able to get a big picture um
[2499.74 --> 2506.06]  um a long time ago um and everybody had a great intention everybody was you know approaching it from
[2506.06 --> 2514.62]  from really um the right motives and and um and primarily with the the project well-being in mind
[2514.62 --> 2520.62]  um you know reasonable people can disagree so i think that you know the drama played out some of it played
[2520.62 --> 2526.06]  some of it played out because you know people like drama and so they it's fun um but ultimately i
[2526.06 --> 2530.86]  don't i don't really i've never seen that as an issue and even throughout the process i've kind of
[2530.86 --> 2534.54]  blogged about it and tweeted about it kind of like you know everybody you know if you want drama you can
[2534.54 --> 2539.58]  enjoy it but otherwise you can ignore this it's just noise and everything is good and keep using node
[2539.58 --> 2545.90]  it's it's still the best platform to use so um no i don't i don't have concern i think
[2545.90 --> 2553.66]  for the most part i've never seen you know like companies behave like companies when it come to
[2553.66 --> 2562.86]  open source i've seen people working for companies um sometimes making bad calls on on open source policy
[2563.58 --> 2567.90]  um you know sometimes your legal team is a little too eager and they're just you know they don't want
[2567.90 --> 2575.74]  to take risk um but ultimately it's about uh making sure that the company understand the value
[2575.74 --> 2583.26]  what they're giving up what they're gaining um and for the most part um participating in open source
[2583.26 --> 2589.34]  is a huge asset um for for pretty much every company out there i guess when it comes to companies
[2589.34 --> 2596.78]  like as big as dwind or walmart if if for some reason we had the ear of someone inside of a company like
[2596.78 --> 2603.58]  that that was like maybe had a if they want to do more in open source but they're not really sure how to
[2603.58 --> 2609.10]  approach it what is what are some i guess now that you've gone through a couple different scenarios
[2609.10 --> 2613.50]  what kind of advice would you give to corporations out there and how they should approach open source
[2613.50 --> 2619.58]  and what they should look at towards value back to them and value back to the community uh open source
[2619.58 --> 2624.54]  is is like any other skill you need to bring experienced people to the table to help you out with it
[2625.10 --> 2631.02]  um companies that have done a bad job have typically tried to do it on their own without learning from
[2631.02 --> 2637.74]  anybody's experience and we are using other people's help so if if a corporation has the
[2637.74 --> 2642.86]  resources and is looking to invest seriously in open source they should go and bring in someone who is
[2642.86 --> 2648.70]  an open source expert whether they are a policy maker uh which is the approach yahoo took they brought
[2648.70 --> 2655.50]  in uh someone uh when i was working there to lead open source policy um and he did a great job setting
[2655.50 --> 2660.94]  up a good balance between what the company was kind of afraid of and what the engineers wanted to do and
[2660.94 --> 2668.54]  kind of where the the um balance um what the balance approach would be um you can do something that's more
[2668.54 --> 2676.22]  like you know what walmart ended up doing uh maybe not consciously but um it was just hiring a few people um that
[2676.22 --> 2684.22]  brought in a significant amount of open source experience uh whether it's you know ben and deon or myself or other people uh to the organization that um
[2684.22 --> 2694.22]  can help them can kind of hold their hand and say hey look you know we're going to open source this this is why we're doing it this is how we know how to do it correctly to gain value um
[2694.22 --> 2702.22]  um so these are these it's it's it's the same way that you know if you if you have a company that has never done um
[2702.22 --> 2712.22]  um you know node before or javascript before uh you're not going to go and hire you know java engineers and buy them a javascript book
[2712.22 --> 2720.22]  and say you know learn this and and let's build everything in javascript now that would probably be a terrible idea um
[2720.22 --> 2728.22]  what you do is you go and you find people who are experienced in the area and you hire them and then use them to leverage other people and grow
[2728.22 --> 2736.22]  grow so open source is the same way i you know it's it's it's a really complex ecosystem you know between the tooling
[2736.22 --> 2745.50]  and the community and the and the legal part and also just managing um the logistics of an open source project
[2745.50 --> 2752.22]  uh you have to understand the cost involved it's not cheap and you have to understand the pitfalls uh open
[2752.22 --> 2758.30]  open sourcing a project that gets no traction is really bad uh it can actually cost you more than if
[2758.30 --> 2764.22]  you did nothing um so there you kind of have to understand those things and at this point there's
[2764.22 --> 2770.22]  plenty of experts um and if you don't have the money to or they just don't want to hire someone just to
[2770.22 --> 2776.94]  manage open source policy hiring like you know go find a really successful open source project and hire that
[2776.94 --> 2783.74]  maintainer and and ask them to be your guide to to do open source so there's there's all these different
[2783.74 --> 2789.74]  approaches um on how you can navigate it but it's not just a matter of taking your source code and
[2789.74 --> 2794.86]  dumping it on github that is not open source that is just yeah that is just you know show and tell
[2796.06 --> 2802.94]  well said well said well let's take a another break um when we get back i want to dive deep into the
[2802.94 --> 2810.30]  the the the the topic at hand really uh you know your thoughts on oauth and your uh your replacement
[2810.30 --> 2815.50]  your oauth replacement oz so let's take a break when we come back we'll kick off that topic
[2817.18 --> 2823.10]  guess what everyone we've partnered with casper the online retailer of premium mattresses to give you
[2823.10 --> 2828.94]  fifty dollars towards your new mattress the mattress industry has inherently forced consumers
[2828.94 --> 2835.82]  myself included into paying notoriously high markups and casper has revolutionized the mattress
[2835.82 --> 2841.42]  industry by cutting the cost of dealing with resellers and showrooms and they pass those savings
[2841.42 --> 2849.02]  directly onto you their mattress is a one-of-a-kind it's a new hybrid mattress that combines premium latex
[2849.02 --> 2855.82]  foam with memory foam and the casper experience was designed with you in mind and optimized for sleep
[2855.82 --> 2862.78]  and this is my favorite part it's backed by a 100 night no hassle return policy with full refund
[2862.78 --> 2868.94]  and a 10-year warranty and what's even cooler is how they ship this mattress to you it comes in a
[2868.94 --> 2874.22]  box that couldn't possibly fit a mattress and when you open it the mattress unravels for you to lay down
[2874.22 --> 2881.66]  and catch some z's head to casper.com change log and use the code change log when you check out to get
[2881.66 --> 2892.06]  fifty dollars towards your new mattress enjoy all right we're back with aaron hammer and aaron uh this call
[2892.06 --> 2900.94]  started as a tweet i guess in a way right as they all do as as they all do and and i'm i thought i had my notes
[2900.94 --> 2907.90]  here perfectly but i didn't and i i went away from my tweet that i had saved from you but long story
[2907.90 --> 2912.46]  short you were like you were announcing oz and you were saying hey i don't want to give any talks
[2912.46 --> 2915.98]  about oz right now but i wouldn't mind coming on a podcast and so i chimed in and said hey
[2916.86 --> 2922.86]  well technically the change log did and me as the change login and here here we are so so this is this
[2922.86 --> 2929.18]  is pretty interesting so what what is happening i guess with oauth one two and then this road to hell
[2929.18 --> 2938.14]  as you said and and what what the heck is oz so it's actually interesting because a lot of almost
[2938.14 --> 2945.26]  all my cool stuff um from the last couple years all came from this this yahoo postmark project um
[2945.26 --> 2956.70]  and oz is is also a byproduct of that work um i was working on oaf and oaf2 um i think the the story
[2956.70 --> 2964.30]  about uh me and the um messy divorce with with oaf2 is uh well known if you don't um there's some
[2964.30 --> 2973.82]  highly entertaining blog posts and videos online enjoy um and the way i looked at it is that um when
[2973.82 --> 2981.50]  i when i stopped working on oaf2 um i felt that once i had enough i just spent you know four or five
[2981.50 --> 2987.50]  years on on doing that that kind of work and i just couldn't take it anymore um but also
[2989.50 --> 2998.30]  i felt that the the atmosphere wasn't very wasn't conducive for meaningful alternative um at the time
[2998.30 --> 3009.98]  i felt that um we we tilted too much to decide of um convincing people that uh the security provided
[3009.98 --> 3016.22]  by oaf2 was just good enough and and it was so much easier to use and so you know so much less
[3016.22 --> 3022.38]  developer friction that you know if it's good enough for google and and and facebook and uh and yahoo
[3022.38 --> 3029.42]  and microsoft then it must be just good enough um the problem was that um like i said back then um
[3029.42 --> 3037.02]  oaf2 is a is an outline it's not really a useful implementation you know if you if you took oaf1 and
[3037.02 --> 3044.78]  you did a a compliant implementation to the spec you got pretty good security out of the box it's it was
[3044.78 --> 3052.14]  it's very hard to implement oaf1 um insecurely in terms of the protocol itself yeah you can always
[3052.14 --> 3059.50]  you know leak stuff and and just do stupid things but um but the message flow the the um the workflow
[3059.50 --> 3066.62]  the the structure of the tokens all that stuff is pretty solid um with oaf2 uh because of all the
[3066.62 --> 3073.10]  compromise that were made it just became an outline which meant that if you are google or microsoft
[3073.10 --> 3079.42]  you can hire um the best security experts and they can write a great implementation that will be very
[3079.42 --> 3088.70]  secure but if you're not then what you have is a you know whatever whatever random stuff you end up
[3088.70 --> 3095.58]  understanding from it and you just have a simple bear token uh protocol where if that token leaks out
[3095.58 --> 3101.02]  then it's game over um and if you look at the implementation for example the vast majority
[3101.02 --> 3108.30]  of oaf2 implementation today um don't expire their tokens so you get a token from i don't want to put
[3108.30 --> 3114.62]  anybody on the spot but there's i'm sure if you've if you've used oaf2 um you got an off to token and you
[3115.18 --> 3120.46]  cut and paste it somewhere and you're happy and it's been a year now two years now and it's still working
[3120.46 --> 3128.30]  um that's that's pretty bad if you think about you have this really long lasting credential that has
[3128.30 --> 3134.38]  no security attached to it and if anybody gets hold of it um you know an employee quits a company they
[3134.38 --> 3139.58]  take that token with them and now they have access to all that data and you can't even know you can't
[3139.58 --> 3147.50]  even tell that it's them because there's no traceability there is no binding to the identity of
[3147.50 --> 3154.06]  whoever's making the call and so on so i kind of look at the environment and i said that's not for
[3154.06 --> 3161.58]  me like i i'm not going to use it um and so i started playing with um two protocols uh oz and hawk
[3162.22 --> 3167.34]  uh if you if you uh familiar with like you know of one terminology there was the three-legged and the
[3167.34 --> 3174.38]  two-legged um where basically if it's just client server um and you're just using the signature stuff
[3174.38 --> 3179.02]  you're not really doing any of the the dance of you know authorizing it you're just using it as
[3179.02 --> 3184.06]  basically replacing for basic off that was the two-legged use case and then the three-legged was
[3184.06 --> 3189.02]  when there is an app a server and a user and the user is authorizing third-party access
[3189.82 --> 3196.86]  so i kind of split those two concerns um and hawk is the authentication protocol it's basically like
[3196.86 --> 3202.70]  basic off which i say digest off it's just a client server authentication that's using holder of key
[3202.70 --> 3210.38]  principles uh a little bit of crypto um if you look at the code um unlike of one it's super simple
[3210.38 --> 3218.22]  it's basically taking off one in terms of signature and bringing it to the modern era so off one is so
[3218.22 --> 3225.34]  awful because it was designed to support php4 and php4 didn't give you access to the raw request uri
[3225.34 --> 3231.02]  so we had to reconstruct it this is why we're doing all this um encoding and sorting and all that stuff
[3231.02 --> 3237.58]  it's all php4 fault um and at the time it was a requirement because php4 was the only available
[3238.30 --> 3242.94]  cloud hosting environment you could buy and we wanted something that is accessible to everybody
[3243.66 --> 3250.06]  and and so that's kind of where off one came from um and so i basically said that you know all the
[3250.06 --> 3254.94]  principles around it were solid uh you know they all came from if you look at the people who developed
[3254.94 --> 3262.62]  all of one um some of the best security experts in the world um no exploit known so far against it
[3262.62 --> 3269.34]  so why reinvent something if we can just simplify it um so that's what i did with hawk and um that has been
[3269.98 --> 3276.86]  published for a few years now um it's pretty widely used and um if you're using node requests you already
[3276.86 --> 3283.34]  have an a hawk client available to you it has been bundled with requests for a few years now um
[3283.34 --> 3290.22]  um it's a very simple protocol and it works really well for for client server authentication and then
[3290.22 --> 3297.42]  what oz does is basically takes that and adds the the whole uh third party authorization on top of it
[3297.98 --> 3306.78]  now in in the beginning uh both of these protocols were part of oaf2 so hawk originally was the uh mac
[3306.78 --> 3313.26]  token that was supposed to ship with oaf2 and when i quit um the interest in maintaining that
[3313.26 --> 3320.70]  work uh disappeared and it just died uh died in committee as they say um people just felt that
[3320.70 --> 3325.66]  the bear token was just good enough and then after that they kind of decided that the right way to do
[3325.66 --> 3332.14]  it is with uh json web tokens um instead of anything else and digital web tokens come with their own set
[3332.14 --> 3338.86]  of security but i don't find them to be good enough um to be honest um because they're not bound to
[3338.86 --> 3346.30]  the request at all so i kind of looked around and i said okay here's my problem i'm not going to use
[3346.30 --> 3353.10]  oaf1 because i'm already over it you know it was great you know in 07 but i need something else i'm
[3353.10 --> 3360.94]  not using off 2 because i rather poke my eyes with needles and so what do i use and what i did is i
[3360.94 --> 3367.26]  basically said you know i'll take what was good of both of these protocols um and the pieces i liked
[3367.26 --> 3371.50]  and i'll throw away everything that's just garbage i'll throw away all the extensibility
[3371.50 --> 3377.50]  of oaf2 that i just don't care about um i'll throw away all the stuff that is not secure enough like
[3377.50 --> 3384.54]  bear tokens and i'll combine um you know the best of both worlds the best of oaf1 the best of oaf2
[3384.54 --> 3393.66]  and produce something else now oz could easily be a fully compatible oaf2 implementation um there's
[3393.66 --> 3400.62]  nothing in it that cannot just be an add-on on top of it but i kind of felt that would be
[3400.62 --> 3408.54]  counterproductive because the the oaf2 mindset the culture around it at this point is so hostile to
[3408.54 --> 3414.62]  any meaningful security anything that is a little bit inconvenient uh if you have to use anything of
[3414.62 --> 3419.34]  like you know oh my god i have to use some client code now to make api calls no that's that's no longer
[3419.34 --> 3427.74]  acceptable and so you you go to that that crowd and you're not really adding any value because nobody
[3427.74 --> 3433.58]  will use in that context so i felt that um instead of trying to stay um
[3435.82 --> 3442.86]  stay committed to the to the oaf2 uh track i'm just gonna throw it out um and so if you you know when
[3442.86 --> 3449.10]  when this was part of uh the original post mile code it was basically all off two so you know what is called
[3449.10 --> 3456.54]  oz now was just oaf2 with a bunch of uh add-ons um you know the self-encrypted ticket with uh um
[3457.42 --> 3463.26]  with with um request authenticity and all those things were just add-ons and what i did is i just
[3463.26 --> 3471.98]  kind of threw out all the oaf2 compliant pieces and gave it a new name and that thing sat there for a
[3471.98 --> 3478.30]  while um i haven't done much work on it for about two years now um most of this code has been written
[3478.30 --> 3488.14]  shortly um after i um i left yahoo um and the reason why i didn't work on it much because uh
[3489.42 --> 3495.42]  i didn't really need any use for it and i don't like working in a vacuum where i'm you know developing
[3495.42 --> 3504.54]  solutions for um unknown soon-to-be problems and now that i have my startup i needed something again and
[3504.54 --> 3508.86]  and that's kind of why this work kind of got resuscitated and and i decided to kind of go
[3508.86 --> 3515.02]  ahead and just finish it and properly document and all that so that's kind of why it became like news a
[3515.02 --> 3523.26]  few weeks ago um but in practice this was kind of done a long time ago there's parts of the project
[3523.26 --> 3527.98]  that that like you said go back a couple years so what uh was just perfect timing i guess with
[3527.98 --> 3533.98]  your departure from walmart and you know maybe some sponsored time from your current company which is
[3533.98 --> 3539.82]  your startup that uh that this became you know your forefront attention or is this just like good
[3539.82 --> 3544.22]  timing for you like this is a good time to solve this problem it was mostly because i needed something
[3544.86 --> 3550.86]  so i i said okay i'm building this app and i need a security protocol um i need exactly what oaf1
[3550.86 --> 3556.62]  and off to provide um i don't want to use either one of them so now what and it's it's actually kind
[3556.62 --> 3562.86]  of sad that uh you know in the last you know oaf1 was in 07 so it's been eight years now eight years
[3562.86 --> 3568.14]  should be you know like if you look at most other protocols look at uh javascript look at html look at
[3568.14 --> 3574.94]  pretty much every technology over eight years um yeah people can kind of like you know eager to to
[3574.94 --> 3579.98]  change and fix and grow and improve and this work has kind of been stale for a long time
[3579.98 --> 3586.30]  um and so i needed something and i kind of looked at what what are my options and i said okay um i
[3586.30 --> 3592.62]  started this thing a couple years ago um i liked using it when it was you know in its previous
[3592.62 --> 3598.62]  incarnation um and i just decided to go ahead and finish it and you know to be honest like you know
[3598.62 --> 3604.94]  it's i wrote it for me you know like you know i do a lot of happy work and and that's kind of a lot
[3604.94 --> 3609.18]  of the work i'm doing for happy is not for me um you know i'm just trying to help other people and and
[3609.18 --> 3615.82]  kind of grow a community with with hawk and oz i at this point i mostly care about my use cases
[3617.50 --> 3624.22]  and i'm also it's a very tricky project to talk about and answer question about because you're kind
[3624.22 --> 3631.58]  of making security recommendation guarantees which i don't want to do um because it's just the wrong
[3631.58 --> 3635.34]  thing to do to advise people on security on unknown projects that i don't understand
[3635.34 --> 3641.74]  um so the it's it's a really interesting project right now that there's a bunch of code and stuff
[3641.74 --> 3646.30]  sitting there and when people open issues and asking me really deep questions about you know
[3646.30 --> 3652.70]  what how i would recommend them using it i'm kind of go well sorry can't help you really you kind of
[3652.70 --> 3658.78]  have to read the code and figure it out on your own um because it's these are all pretty complex
[3658.78 --> 3666.70]  security issues and the tool is really designed for people who who really understand you know oaf and
[3666.70 --> 3672.46]  these principles well and just want to use something cleaner with the with a different feature set yeah
[3673.26 --> 3678.46]  maybe speak to the security aspect a little bit because um like you said you know making security
[3678.46 --> 3685.50]  claims is is big deal and you know one thing you can say about a committee or a working group at least
[3685.50 --> 3690.94]  you would think you'd be able to say is there you know a a group of experts working together to come
[3690.94 --> 3695.82]  to sort of some sort of solution now in practice you know that sometimes is successful and sometimes
[3695.82 --> 3701.90]  fails miserably but um it's a group of experts and i think my first thought when i saw your
[3701.90 --> 3706.22]  oz announcement was aaron oh yeah aaron hammer he does happy js and he's the walmart
[3706.78 --> 3711.50]  guy that we had on the show wow he knows security uh when i see an announcement of like oh
[3711.50 --> 3718.30]  i'm replacing oaf too it's like who's replacing oaf too like there's this question of authority and
[3718.30 --> 3723.66]  and expert uh expertness i don't know the word but maybe just give a little bit of you know
[3723.66 --> 3728.94]  background or i mean after reading your code a little bit and reading your your readmes you know
[3728.94 --> 3735.42]  i was convinced that okay he actually knows what he's talking about um but do you have to uh give
[3735.42 --> 3740.22]  authority sometimes or do you have people questioning your ability to create security protocols
[3740.22 --> 3748.54]  um i mean if you know my background you know and if you look at the um the oaf specs you know my
[3748.54 --> 3754.70]  name is all over it um well there was the example you said earlier at uh i don't mean to interrupt it
[3754.70 --> 3759.74]  it was the example you had earlier when you were at walmart with the infosec people you know badging
[3759.74 --> 3764.54]  about the the gists that you were posting you're like well you know who i am so you had to throw
[3764.54 --> 3769.66]  in throw around kind of like your your uh your authority there too yeah i do it once in a while when
[3769.66 --> 3775.42]  when i absolutely have to um but basically um yeah i'm just like you know go on the go on wikipedia
[3775.42 --> 3785.42]  and uh and look up oaf and then come back um but it's i'm not a security expert i mean i'm i'm very
[3785.42 --> 3792.06]  well versed in security and i am an oaf expert um you know after spending uh a few years uh you know
[3792.06 --> 3803.10]  serving my time um and what is really really key here is that one um i'm not trying to invent anything
[3803.10 --> 3810.06]  new uh if you look at what this does from a protocol perspective it's exactly the same as what oaf and
[3810.06 --> 3816.70]  oaf2 are doing and if you look at the implementation that's really where the scrutiny should be
[3816.70 --> 3823.74]  uh focused on and nobody does that and and so one of the complaints i always had about you know people
[3823.74 --> 3829.58]  saying oh is this a compliant and oaf compliant implementation and i said well on that's a you
[3829.58 --> 3833.98]  look at npm and you find an oaf module and it says it's compliant and you're trying it out and working
[3833.98 --> 3838.86]  well um that doesn't make it secure because you have to look at the source code and understand how
[3838.86 --> 3844.86]  it's operating and where it's storing its information and how it's uh generating its its randomness and and all
[3844.86 --> 3850.86]  and is it actually verifying the nonce or not and is it you know is it if you look at oaf2 it requires
[3850.86 --> 3857.10]  a whole bunch of server validation that um if you don't perform the protocol will still work perfectly
[3857.10 --> 3865.34]  well you know it's not going to fail you and so it's very misleading to say that the spec is secure
[3865.34 --> 3870.54]  um implementation can be secure specs are not secure you know they're just paper which is just words
[3870.54 --> 3877.98]  and so that's has been kind of my my gripe against i'll get most of the the off to and all and even
[3877.98 --> 3884.78]  some of the off one um crowd is that you know people saying i'm going to pick off two and that
[3884.78 --> 3892.06]  makes my system secure like no it doesn't and what i want people to do is to um there's a little bit of
[3892.06 --> 3897.10]  protocols like you can look at oz and hawk and scrutinizer protocol um it's if you know what you're
[3897.10 --> 3904.54]  doing it's very easy to do uh and and i did have a bunch of um you know the same you know top level
[3904.54 --> 3910.78]  security experts that have looked at at oaf um have looked at oz and and and hawk and and gave it their
[3910.78 --> 3915.42]  blessing um you know there's a lot of liability involving security so nobody i'm not gonna put their
[3915.42 --> 3922.38]  name and say this has been approved by you know x and y um but i feel very confident that the protocol
[3922.38 --> 3928.70]  itself is solid and it's basically identical to off you know parameter names are changed and you know
[3928.70 --> 3933.18]  some of those things are different but fundamentally it's exactly the same protocol what's much more
[3933.18 --> 3937.58]  interesting and important is the code i wrote and how it's implemented and i'll give you you know one
[3937.58 --> 3945.42]  concrete example um oaf 2 was created specifically to help yahoo and google and microsoft scale their
[3945.42 --> 3950.46]  oaf operations that was the main concern they had the secondary goal was to make it easier for
[3950.46 --> 3956.22]  developers to use but the primary goal for them is to scale it and what they wanted to do was to make
[3956.22 --> 3962.78]  the the tokens um self-encoded so that when they get a token they don't have to do a database lookup
[3962.78 --> 3967.18]  to find out if the token is still valid what they want to do is to decode the token using you know
[3967.82 --> 3972.06]  some some kind of crypto and then inside of it they'll find the information they needed and that was
[3972.06 --> 3976.38]  good enough the thing is that once you have this kind of design it's a very it's highly scalable
[3976.38 --> 3981.18]  design because there's no data center um you don't have to synchronize your storage across you know
[3981.18 --> 3987.98]  multiple um locations and all that so it's great but now you have credentials that don't expire
[3989.02 --> 3994.86]  because if the credential is self-encoded if the credential itself includes what you need in order to
[3994.86 --> 4001.66]  use it then there's no lookup then you can never invalidate it you can revoke it um and so what they
[4001.66 --> 4006.54]  wanted to do is they want to issue short-lived credentials in like yahoo cases i think it was an
[4006.54 --> 4014.86]  hour um and you can use that for up to an hour but after an hour you have to go and come and get a new
[4014.86 --> 4021.26]  one that's kind of where the off to refresh token came in so if you're using all of two and you're not
[4021.26 --> 4027.58]  using refresh tokens you're actually doing a really big disservice to yourself because you're issuing these
[4027.58 --> 4034.38]  um these long-lasting credentials now if you are doing a database lookup for every request then well
[4035.26 --> 4040.22]  maybe you should reconsider that if you have any any kind of scale for your for your authentication
[4040.22 --> 4045.82]  then every api call now has a database lookup just for the for the token which is um challenging
[4046.54 --> 4054.54]  so if you kind of think about it um now you need to have some kind of self-expiring encrypted token
[4054.54 --> 4062.30]  um so uh the jwt work is is doing some of that um but then there's other layers that are missing
[4062.30 --> 4071.02]  um and i can you know i can like i could talk about this for hours but but basically what i've done is
[4071.02 --> 4077.74]  i said okay i'm going to produce a token that is self-encrypted that expires that can do password
[4077.74 --> 4083.18]  rotation um that can do all those things that is going to give you both privacy and authenticity
[4083.18 --> 4088.62]  um and i'll just do it in a way that is going to be solid so i i talked to a bunch of my crypto friends
[4089.10 --> 4093.50]  and i sat with them and i said okay how do i do it in the absolutely right way and what is the right
[4093.50 --> 4098.06]  algorithm to use and the right crypto to use and how do you generate the keys and all that stuff
[4098.70 --> 4103.90]  and i wrote a module called iron and iron basically does that it takes a json object and turn into an
[4103.90 --> 4112.86]  an opaque string that is um fortified and if you if you don't understand how to do that then you can't
[4112.86 --> 4118.70]  really properly use oaf2 and that's kind of all in my point is that to to properly use oaf2 you have to
[4118.70 --> 4124.78]  be a pretty advanced developer and understand security and crypto really well uh which most people don't
[4126.38 --> 4131.74]  so what what us is trying to do is take all these great engineering principles and implementation
[4131.74 --> 4135.90]  principles and just put them together and say you know what let's see let's forget about this this
[4135.90 --> 4139.42]  interrupt and all this standard nonsense because nobody really cared when was the last time you
[4139.42 --> 4143.90]  were trying to like reuse code across multiple providers like you know that was like that was
[4143.90 --> 4150.14]  the grand vision of like you know 2005 2006 uh when we were trying to kind of like you know make api
[4150.14 --> 4155.34]  standards across the web and open up the social web walls and at this point nobody cares about this
[4155.34 --> 4161.34]  anymore you know that's all dead and so since we don't care about you know making sure that the
[4161.34 --> 4165.98]  twitter api and the facebook api are compatible to each other and because there's only two of
[4165.98 --> 4172.22]  them now and we don't care you know when there was like a hundred of them it was painful um why are we
[4172.22 --> 4178.46]  bothering with interrupt so if you throw away interrupt now you can do whatever you want and now what i
[4178.46 --> 4183.10]  wanted was a great solution for a javascript based environment that will work well on the server
[4183.10 --> 4189.74]  we're on the client get me all the security i want and what i want people to do is to take the code i wrote
[4189.74 --> 4196.22]  and scrutinize that go line by line and find where i'm doing something stupid uh versus you know here's
[4196.22 --> 4200.70]  the protocol documentation and you can kind of say oh here's the flow and this is where you know you
[4200.70 --> 4205.02]  send the parameter in like that's not really interesting um it's kind of needed just to
[4205.02 --> 4209.42]  understand what i'm doing but it's not really helping you understand if this is secure or not
[4209.42 --> 4218.94]  so i think that's that's like a key uh goal of of this work is that i'm trying to shift the focus from
[4218.94 --> 4226.54]  an academic exercise of writing a security specification to a very practical exercise of writing a piece of
[4226.54 --> 4233.90]  code that you can reason about in absolute terms because it's a piece of code it does one thing and
[4233.90 --> 4243.26]  and and then you can find out if that is secure as an as an end product versus um a theoretical um secure
[4243.82 --> 4251.74]  protocol so you got three modules you have iron which you said was the cryptic wrong word cryptographic
[4251.74 --> 4257.82]  piece which basically just takes a json object and does i'm assuming it's like symmetric encryption on it
[4257.82 --> 4265.42]  yep um just encodes that or encrypts that thing then you have hawk which is the authentication protocol
[4266.22 --> 4273.42]  or scheme as you call it um and then oz is kind of the that's the authorization layer um
[4274.62 --> 4279.18]  am i breaking those three out correctly yep exactly right okay so when we're talking about hawk
[4279.90 --> 4285.02]  one of the things that you say in the introduction to hawk as a primary design goal is that it simplifies
[4285.02 --> 4291.98]  it improves http auth for services that are unwilling or unable to deploy tls for all resources and i
[4291.98 --> 4299.82]  i thought i stopped there for a second and thought why is this necessary can't we just you know what can't
[4299.82 --> 4307.82]  we just be willing and able to deploy tls and use basic auth and would that require not having this
[4307.82 --> 4313.98]  library well is that just a perfect world looking at it and and in the real world that's not the case
[4313.98 --> 4325.10]  um so it's it's part of the answer um so there is um there's a really important principle in any
[4325.10 --> 4332.94]  secure system and that's to have um separation of concerns and layering of defenses um also known as
[4332.94 --> 4342.06]  don't put all your eggs in one basket and the reality is that even if you are deploying tls everywhere
[4342.06 --> 4351.18]  you don't have control over your clients i mean this the the the the tls protocol doesn't ensure
[4351.18 --> 4356.70]  that the client is doing the right thing right the server can make sure that the channel is encrypted
[4356.70 --> 4361.02]  doesn't know if the channel if the client is leaking stuff it has no way of knowing it doesn't know if
[4361.02 --> 4366.70]  the client is properly validating the server certificates which in most cases it doesn't um yeah the
[4366.70 --> 4372.38]  advancement i think rails still doesn't validate client certificate by default if i'm correct um i
[4372.38 --> 4379.10]  know node uh i had to eat like you know scream and yell for node um dot 10 to change the default to
[4380.14 --> 4386.06]  throw on invalid server set assert instead of um ignore it by default and so
[4388.22 --> 4391.34]  if you just have to assume that the developer will do stupid things
[4391.34 --> 4398.14]  things and it's just because code does stupid things a lot of time and is that good enough for
[4398.14 --> 4407.18]  you so if you think about in a perfect world where the credential is guaranteed to be sent over tls
[4407.82 --> 4414.46]  to the right server and not leak anywhere then yes bear tokens are just fine
[4414.46 --> 4424.46]  but it's never a perfect world and so you have to ask yourself should i you know do anything else
[4424.46 --> 4430.30]  and the reality is that if you're sending a bear token to the wrong server right either it's typo or
[4430.94 --> 4436.94]  um or you fail to check your your uh tls certificate you know you're on an airport wi-fi and someone is
[4436.94 --> 4443.18]  basically giving you bad certs and and you have a code that ignores bad certs because that's what most
[4443.18 --> 4447.34]  developers do because like hey look you know it wasn't working and i put this ignore and now it's
[4447.34 --> 4454.38]  working awesome um and and you go on stack overflow see how many people answer questions about bed certs
[4454.38 --> 4461.42]  by saying oh just add this flag of ignore um problem solved and and if that's the case then
[4461.42 --> 4466.78]  whatever app is not validating properly is not fully exposed because they don't know who they're talking
[4466.78 --> 4472.38]  to so you don't you don't actually get tls protection so i think that's a really important um
[4472.94 --> 4479.98]  point to make is that it's just not enough and and there's a lot of different ways where you can
[4479.98 --> 4487.42]  leak those those credentials um that's one thing the other thing is that without some kind of um
[4489.42 --> 4496.14]  crypto it's very hard to know that the request came from the right person and and it's meant for the
[4496.14 --> 4503.66]  right um server and i'm gonna try to keep this you know as simple as i can but basically if you think
[4503.66 --> 4510.94]  about uh a simple scenario let's say there's facebook and then i have an app i have two apps
[4510.94 --> 4519.98]  that uses facebook to log in into them because the the they both use uh the facebook uh token as the
[4519.98 --> 4525.18]  authentication key because what they do is you go to facebook you come back to the app with a tip with
[4525.18 --> 4530.86]  the token and then the app goes back to facebook and says who is this token uh who does this belong
[4530.86 --> 4539.42]  to and then facebook say oh it's steve great now we can log in steve um so that that that token is really
[4539.42 --> 4547.42]  powerful what happens if i trick you into logging into my app using facebook then i take that ticket
[4547.42 --> 4553.34]  that i got for you from facebook and i got now go back and log into another app that's using facebook
[4553.34 --> 4561.18]  to log in i can now log in as you to the other app i don't i can't really attack you on facebook itself
[4561.18 --> 4565.98]  that doesn't work but i can now because those tokens are not bound to any you know if you remember
[4565.98 --> 4571.34]  if you remember in off one we had everything had to be signed by both the the uh client secret and
[4571.34 --> 4577.66]  the token secret in all of two because there's no signatures there's nothing that binds the tokens
[4578.22 --> 4584.70]  to whoever is making the request so i can now trick another app to thinking that i'm you using your
[4585.42 --> 4592.94]  facebook ticket that you gave me perfectly legitimately and so once you start removing these
[4592.94 --> 4597.74]  layers you have all these outcomes and and for example facebook has a feature to solve that
[4598.38 --> 4605.18]  when you make the uh you know the who am i uh api call facebook gives you an option to include with
[4605.18 --> 4611.74]  it a hash of i think your client id or something and then they'll check for you if the ticket was issued
[4611.74 --> 4616.46]  for you and if it's not they'll say oh sorry you're using a ticket that wasn't really a token that wasn't
[4616.46 --> 4622.70]  really meant for you someone is tricking you um but it's an option it's an optional argument and if
[4622.70 --> 4629.26]  you look for example at the uh i mean at least last time i looked at the node um express passport
[4629.26 --> 4636.78]  facebook implementation that feature is off by default so you you get all these details and look you know
[4636.78 --> 4642.38]  everything i just said i'm sure most of the audience you know has never heard about it and not aware of it
[4642.38 --> 4647.58]  and doesn't even know that facebook has this feature that allows you to protect your app from um wrong
[4647.58 --> 4653.98]  logins but the whole point is that they shouldn't need to and if the protocol is it is written
[4653.98 --> 4658.46]  correctly then the protocol might be a little more difficult to use but at least it does the work
[4659.10 --> 4664.70]  for you and it gives you the protection that you need it doesn't require you to go and invent uh your
[4664.70 --> 4669.90]  own extension so for example that extension is a twitter it's a facebook invention they edited to
[4669.90 --> 4675.10]  the protocol because they had some attacks on on some um i don't know if they're calling it the
[4675.10 --> 4681.18]  canvas apps or whatever they're calling it um people were able to like trick one and and kind of
[4681.18 --> 4685.18]  like log into another and i don't remember the specific of the of the export that someone found
[4685.18 --> 4691.74]  but that's kind of what what they've done to solve it and there was no standard for that so now you know
[4691.74 --> 4697.50]  a secure facebook implementation is no longer compliant with any other off to implementation because they
[4697.50 --> 4704.30]  had to add their own parameter to the mix so it's that's kind of the reality of it um which is why you
[4704.30 --> 4711.58]  you know all this all this crypto stuff it really matters um the other thing is being able to you
[4711.58 --> 4715.98]  know invalidate these credentials and being able to validate that they're that they were issued you
[4715.98 --> 4722.70]  know that they're still um that they haven't expired like you know all those requirements um are all
[4722.70 --> 4731.34]  implementation details so in a perfect world if your client you know to your question if you can guarantee
[4731.34 --> 4735.90]  if you control your client code let's say you're running your own private client server implementation
[4736.54 --> 4741.50]  so you have full control of your client you know what you're doing uh it will never run on hostile
[4741.50 --> 4747.02]  networks you're fully checking the credentials uh no one will ever see those credentials outside of you
[4747.58 --> 4753.42]  um you know like if you put all these constraints on on it um you don't actually have
[4753.42 --> 4758.54]  third-party apps accessing your your api it's just that you're just your own software then yes
[4758.54 --> 4761.42]  right basic off over tls is just fine
[4764.14 --> 4768.86]  all right that's an excellent answer that's like if you disconnect your server from the network it's
[4768.86 --> 4774.94]  it's completely secure i mean it's you know it um there was a really there was a really interesting
[4774.94 --> 4783.26]  debate um really interesting debate going on uh on the express um session middleware a few weeks ago a few
[4783.26 --> 4795.34]  months ago um where express um uses an age mac to uh to hash every session id so that it cannot be uh
[4795.34 --> 4802.30]  messed with and you know all the all the people who play uh crypto expert on the internet um showed up
[4802.30 --> 4808.54]  and let me say that if you use a properly randomized session id it's as secure and you don't need to do
[4808.54 --> 4817.82]  any crypto to it um and that kind of brought all the same arguments that yes you know in theory of
[4817.82 --> 4825.50]  an extremely well randomized hard impossible to guess session identifier doesn't need to be you know
[4825.50 --> 4832.78]  hashed or any kind of crypto protection but it's that's not where the story ends um and there's so many
[4832.78 --> 4839.74]  ways in which that can fail um you use the wrong crypto function you use math random instead of you
[4839.74 --> 4845.74]  know properly you know secure crypto generator um or you just don't know it and you kind of somewhere
[4845.74 --> 4851.18]  in you're fudging a different identifier because you like to have them sequential um or it comes from
[4851.18 --> 4857.26]  a database and the database can be hacked and the the database id generator can be managed can be changed to
[4857.26 --> 4863.98]  be um non-random like there's all these layers so it's at the end of the day when it comes to security
[4864.78 --> 4869.50]  it's always you know eggs and basket is what you know the two words you have to like ask yourself
[4870.54 --> 4875.66]  now i think that's a strong point and i think the layering is a compelling argument of why you'd want
[4875.66 --> 4882.62]  to use hawk even in scenario described um we're gonna stop here for our final break here from uh
[4882.62 --> 4886.94]  another one of our amazing sponsors and when we get back we're gonna close up this conversation
[4887.58 --> 4893.74]  with more on oz and we're gonna have aaron describe the protocol a little bit and maybe compare and
[4893.74 --> 4903.66]  contrast um specifics with oaf2 so we'll be right back imagex is a real-time image processing proxy
[4903.66 --> 4911.26]  in cdn and let me tell you this is way more than image magic running on ec2 this is way better it's
[4911.26 --> 4919.18]  everything your friend and developers have dreamt of output to png jpeg jiff jpeg 2000 and several other
[4919.18 --> 4925.26]  formats and if you're like me you've ever argued with your boss or a teammate about serving retina
[4925.26 --> 4932.14]  images to non-retina devices you'll appreciate their open source dependency free javascript library that
[4932.14 --> 4937.58]  allows you to easily use the imagex api to make your images responsive to any device
[4937.58 --> 4944.86]  now all this takes a platform and the imagex platform is built on three core values flexibility
[4944.86 --> 4952.14]  and quality performance and affordability when it comes to flexibility and quality imagex has over
[4952.14 --> 4959.10]  90 url parameters that you can mix and match to provide an unlimited amount of transformations that
[4959.10 --> 4964.38]  you need for your images and they take quality very seriously and because of their commitment to
[4964.38 --> 4971.74]  quality several top 1000 websites in the world trust them to serve their images now when it comes to
[4971.74 --> 4978.54]  performance imagex operates out of data centers filled with top of the line mac pros and mac minis
[4978.54 --> 4984.38]  and they're set up for a completely streaming solution this means your images never hit the disc
[4984.38 --> 4991.58]  images are served by the best ssd based cdm for delivery around the world anywhere extremely fast
[4991.58 --> 4997.50]  and while we're talking about speed almost all the image processing happens on gpus this means
[4997.50 --> 5003.90]  transformations are super fast when compared to competing virtualized environments and lastly it's all
[5003.90 --> 5010.30]  about affordability everyone wants to save a buck that's how the world works because imagex processes
[5010.30 --> 5017.50]  close to a billion with a b images per day they're able to make certain optimizations at scale and pass
[5017.50 --> 5024.62]  those savings on to you to learn more about imagex and what they're all about head to imgix.com
[5025.10 --> 5033.02]  change log once again imgix.com change log and tell them adam from the change log sent you
[5033.02 --> 5042.62]  all right we are back with aaron hammer discussing oz his web auth protocol based on industry best
[5042.62 --> 5050.14]  standards aaron you said oz is not a spec it's an implementation you don't really care if it's
[5050.14 --> 5056.46]  ported to other environments because what you want is an awesome javascript implementation um
[5057.74 --> 5062.94]  tell us a little bit more about oz and specifically from my perspective as a as an oauth
[5062.94 --> 5068.94]  user um i've never written a provider i've dealt with as an application developer quite often
[5069.74 --> 5076.30]  reading through it you know on the surface it kind of does look like oauth 2 um so i know you've done
[5076.30 --> 5082.30]  it a little bit surface during the intro but maybe give us a little bit of deeper dive into oz itself
[5082.30 --> 5089.82]  we've talked about hawk and iron and the compare and contrast it with oauth 2 perhaps from the
[5089.82 --> 5105.82]  the perspective of a of a user sure so um oauth 2 is focused on on two main uh pieces one is the um
[5106.62 --> 5114.46]  the authorization flow which is how do you go about redirecting the user from one place to another to
[5114.46 --> 5121.26]  authorize and kind of move and pass along the necessary credentials um whether the authorization
[5121.26 --> 5127.18]  code or the the grant or i honestly don't remember all the terminology i made up for off to at this point
[5128.06 --> 5137.34]  and that's one part of what it's doing and the other part is once you have obtained a token is how do you
[5137.34 --> 5144.54]  use that token to make authenticate requests so those are the two pieces um and in oaf one they're kind of
[5144.54 --> 5152.54]  like all mushed together into one one flow and all in off two we kind of separate that um and it ended up
[5152.54 --> 5158.06]  being two specs one was the the authorization protocol and the other one was the bear authentication scheme
[5158.06 --> 5169.58]  um and then the bear authentication scheme um was enhanced later on to use uh jwt tokens uh which are
[5169.58 --> 5176.62]  the json web token it's a protocol of taking a json object which is very similar to saml principles um
[5177.58 --> 5183.34]  taking those into creating some kind of credential that is uh self-describing uh versus just a random
[5183.34 --> 5191.66]  uh bear token string that you use so that's kind of what off two provides um if you look at uh the
[5191.66 --> 5199.34]  the three protocols that i have um i think the parallel would be that iron is uh in a way similar to jwt
[5199.34 --> 5206.86]  so it's a it's basically a a token format um the diff the main difference is that uh iron tokens are opaque
[5207.34 --> 5213.10]  um to the to the client um but they are meaningful to the server it's basically taking
[5213.34 --> 5220.62]  a json object stringifying it uh encrypting it uh and then uh calculating a hash on top of that
[5221.26 --> 5229.42]  um and then also baking into the structure uh additional features for expiration um and um
[5230.06 --> 5235.34]  password rotation which is really important for proper crypto hygiene and so that's kind of what that
[5235.34 --> 5243.58]  gives you it gives you a a token format that you can use um what hawk does is take the part that is
[5243.58 --> 5252.62]  completely missing from oaf2 which is uh an authentication um authentication scheme that is using some kind of
[5252.62 --> 5261.50]  crypto um similar to how uh oaf1 was written um it's basically requiring you to sign every request so every
[5261.50 --> 5267.26]  token comes with a token and a secret you use the secret to calculate a hash and you send the hash with
[5267.26 --> 5274.30]  the request so in you know in in those terms it's very simple it's basically competing with the oaf bear
[5274.30 --> 5280.62]  token scheme only it adds uh some some layer of cryptography and extra security uh to the security
[5280.62 --> 5290.78]  layers and then what oz does is um oz is more of an implementation component versus a protocol component
[5291.42 --> 5299.10]  it's basically taking the elements from oaf2 so if you think about oaf2 it's basically um in in the in
[5299.10 --> 5308.06]  the traditional off to flow where um you go and you uh send the user to a page to authorize they come back
[5308.06 --> 5314.06]  with the authorization code uh then you exchange the authorization code for a ticket for a token um
[5315.66 --> 5320.38]  what oz does is basically says you know what we're not going to tell you how to do the flow itself
[5320.38 --> 5325.02]  like you know we're not going to tell you how to redirect that's that's at the end of the day that's
[5325.02 --> 5334.22]  how you're implementing your app um but we are going to introduce um the the the basic um building
[5334.22 --> 5342.38]  blocks and so the first building block is that the application itself needs to authenticate and obtain
[5342.38 --> 5350.14]  its own uh hawk credentials so the same with oaf where you uh pre-register your client with the client
[5350.14 --> 5356.14]  secret and all that you do the same thing with oz you establish that relationship out of bound um and
[5356.14 --> 5363.98]  once you do that you cannot use your uh client credentials because basically everything is always
[5363.98 --> 5371.90]  hawk so if you think about oaf2 the first step is you're using basically either basic auth or um some
[5371.90 --> 5380.46]  kind of you know form encoded um credentials to get the initial interaction with the server in in in oz
[5380.46 --> 5386.86]  everything is hawk so it's it's all secure from the very beginning and what happens is that the only
[5386.86 --> 5394.30]  thing you can do um with your hawk credentials is exchanging for oz credentials oz credentials are called
[5394.30 --> 5400.46]  tickets um and basically it's instead of calling it a token it's called a ticket you need a ticket to get in
[5402.14 --> 5408.70]  and a ticket can be provisioned for either the the app or the user so you have two kinds of tickets
[5408.70 --> 5414.54]  tickets the ticket itself is just an iron object so that's kind of where it's using that that piece
[5416.22 --> 5424.22]  the the flow is very similar the user goes um the user is being told to go to some server page to
[5424.22 --> 5430.46]  authorize access they go there and when they authorize access they come back to the app with an rsvp
[5431.58 --> 5436.86]  and that rsvp is basically authorization code it's a it's a smart authorization code so it has some stuff
[5436.86 --> 5444.38]  encoded in it um and then they go back to the server and the server can take that rsvp and issue you
[5444.38 --> 5450.78]  uh your your ticket it's exactly the same as the traditional off to flow the only difference is that
[5450.78 --> 5458.38]  um oz gives you apis to build it and doesn't forces you to do any kind of the redirection or you know
[5458.38 --> 5463.90]  which query parameter should i stick the the rsvp in none of that stuff is is really interesting
[5463.90 --> 5469.10]  that's that's up to you you can implement any way you want um for example one implementation i've done
[5469.66 --> 5476.06]  doesn't even use those flows it's just using cookies so what it's doing is um you go to a
[5476.06 --> 5480.38]  login page and you log in with twitter and when you're done you end up with a valid session cookie
[5480.38 --> 5485.10]  on your server and then what you do is you make a call and say hey can you exchange this server this
[5485.10 --> 5491.18]  this cookie basically and issue me a ticket that has the same permissions um and internally it's using all
[5491.18 --> 5497.66]  these um elements in order to do that um and you can see that all in you know you can see how it
[5497.66 --> 5505.34]  works there is the the original uh post mile project uh that was working on at yahoo um is using a
[5505.34 --> 5510.22]  slightly older version of oz right now but it's all the same principle and you can see exactly how the
[5510.22 --> 5516.86]  flow works there in terms of you come to the website you log in and then those credentials are sent
[5516.86 --> 5521.82]  to the one page app and then from there you're just doing um uh authentication now
[5522.46 --> 5528.06]  also authentication is basically just hawk authentication with two extra parameters which
[5528.06 --> 5534.14]  gives you built-in support for delegating access so you can have one app delegating access to another
[5534.14 --> 5542.54]  app if they're allowed to that's already built in and it also gives you um some support for scoping so
[5542.54 --> 5548.54]  you can scope apis and it's part of the ticket um so there's all these extra features that it gives
[5548.54 --> 5556.46]  you out of the box um as part of the solution so that's that's kind of what it does it's in in practice
[5556.46 --> 5566.54]  you can very easily adopt this protocol to be exactly off two um you can use you know iron uh and and even use
[5566.54 --> 5573.74]  uh uh uh oz ticket as oaf tokens that will work just fine um as long as you you know properly signed
[5573.74 --> 5584.62]  the request you can use uh hawk authentication as just a valid uh off uh two um token type and in fact
[5584.62 --> 5593.10]  it used to be that if you you know kind of google the oaf to mac mac authentication scheme you'll find a
[5593.10 --> 5599.98]  very old draft that i wrote that was basically what hawk is now uh before i quit the working group um
[5601.10 --> 5608.54]  so these are all very old principles um i think the big change here is that i'm shifting focus from
[5609.42 --> 5616.14]  protocol to code and and i'm focusing on this implementation instead of trying to kind of
[5616.14 --> 5623.02]  create an ecosystem around it so has that been successful from the perspective of code review
[5623.02 --> 5629.98]  and criticism like have you drawn to your code base the eyes that you uh have hoped for um
[5631.18 --> 5638.46]  yes for hawk and for iron those two have been thoroughly reviewed and and scrutinized um
[5639.34 --> 5643.50]  less for oz mostly because up until a couple weeks ago it wasn't even documented
[5644.06 --> 5651.82]  um so it wasn't at all accessible i think that now that it is it might get some more scrutiny um people
[5651.82 --> 5655.10]  have been using it i'm always surprised when i'm getting email from someone saying
[5655.66 --> 5659.50]  you know we've been using this thing and we you know in production for the last year and a half and
[5659.50 --> 5667.10]  we have a question about something and i was like oh okay that's interesting and so it has been getting
[5667.10 --> 5672.54]  you know some traction it's nowhere near the numbers right it's like uh it's wouldn't be even
[5672.54 --> 5677.82]  like you know a full percentage you know in comparison to where oaf2 is it's it's completely insignificant
[5677.82 --> 5686.54]  um but it's there and and i think that um if you look at the the pieces that all itself brings if
[5686.54 --> 5693.66]  you look at the code itself it does there's not much there so you know if if if you accept the fact
[5693.66 --> 5701.82]  that that iron and hawk are solid and have been thoroughly reviewed and and they're all um basically um
[5701.82 --> 5708.06]  uh to provide a very strong security in the area that they focus on then oz itself doesn't really
[5708.70 --> 5715.26]  change as much um because it's it's just an implementation detail on top of the other two
[5715.82 --> 5721.90]  um and the flow itself that it's using is basically oaf2 um so i mean and if you look at the code you
[5721.90 --> 5727.34]  can basically see it you know it's it's it's very little code there's always a nice thing to see for
[5727.34 --> 5733.42]  any project focused on security as a small surface area uh what does uh what does success look like
[5733.42 --> 5739.34]  for oz like what's an end goal what would you look back and smile and say i did it it works for me
[5740.78 --> 5745.66]  well so you've already we're there you're already there no not i mean not quite if you know like i
[5745.66 --> 5750.14]  need i for my my startup needs to be successful right and then i can say hey look i have millions of
[5750.14 --> 5756.70]  users using my my product and it's all powered by this um i see it's to me success
[5756.70 --> 5764.54]  um in there's two ways of looking at the there's there's the success of uh no i wrote a piece of
[5764.54 --> 5770.46]  software and it's doing what it's meant to do um no known exploits you know nobody getting hacked
[5770.46 --> 5774.94]  because they're using it um it's whoever is using it's working well for them and it's primarily
[5774.94 --> 5779.42]  working well for me because you know i'm putting the effort into it and i need it and so it needs to
[5779.42 --> 5784.46]  provide me with a good solution at some point um sideway will have a public api
[5784.46 --> 5790.14]  and when that happens you know the the test is going to be whether developers are willing to
[5790.14 --> 5797.42]  learn a new kind of protocol to work with the api or not right that's a big one um if you know if i
[5797.42 --> 5801.58]  put a public api people looking at like oh why is that using off too i don't want to touch this it's
[5801.58 --> 5806.54]  another one of those stupid you know custom made security thing i'm not dealing with it um so it's
[5806.54 --> 5811.10]  you know that's that's another another that will be another test you know in the future um
[5812.62 --> 5817.74]  and just you know whoever is you know stumbling upon this and and playing with it um and if they
[5817.74 --> 5823.82]  like it and decide to participate that's great now on the open source front what i really want to get
[5823.82 --> 5831.02]  out of it is to kind of give people um a reference implementation that they can then use for whatever
[5831.02 --> 5838.78]  they want it's super easy to take the the pieces um you know as modules or um or just as code to cut
[5838.78 --> 5844.06]  and paste and write your own you know awesome off to implementation so if you're looking at off two
[5844.06 --> 5847.98]  and you're saying you know i want all these features that it was designed for you know i want these
[5847.98 --> 5855.58]  you know really strong refresh token uh um expressions and i want to have all these uh self-encoded uh you
[5855.58 --> 5860.78]  know tokens and like all these features that you want and you can use the building blocks that that
[5860.78 --> 5866.46]  these three modules provide uh or just cut and paste code from them that's great you know it it can
[5866.46 --> 5872.70]  make your off implementation awesome um even if you're not a world expert on it because you can
[5872.70 --> 5881.98]  you can see how it's done and you can either reuse it or imitate it so it's um the focus really is not
[5881.98 --> 5889.66]  on um on getting people to stop using off two and off one and just using oz from now on it's more of
[5889.66 --> 5894.70]  saying hey look here's a bunch of code written by someone who hopefully knows what he's doing um
[5895.34 --> 5900.38]  you know using all these same principles and you can use it you know to learn you can use it to to
[5900.38 --> 5908.30]  imitate you can reuse it as is um and i think that's that's a more interesting aspect um it because if if
[5908.30 --> 5916.86]  you're if if you you know if you missed it by now my attitude here is that there is very little value in
[5916.86 --> 5923.98]  a standard in this space there's a lot of value in in thoroughly tested and proven piece of code
[5923.98 --> 5930.86]  um you know i mean how many people have read the the tls spec and can understand how tls works almost
[5930.86 --> 5939.66]  nobody um what you do is you use an implementation and so what my my you know my political agenda here
[5939.66 --> 5947.34]  is really to kind of shift the focus from writing security specs to writing fantastic implementations
[5947.34 --> 5954.22]  that provide you actual security where we can reason about the the implementation and fix bugs in it
[5954.22 --> 5960.94]  um versus the debate of the you know what what to call the parameter where we're sending it back and forth
[5960.94 --> 5968.30]  more doing that's calling it kind of like uh uh that commercial less let's talk more doing what's
[5968.30 --> 5971.82]  i'm trying to get the commercial right now it's like a home depot commercial i think it's home depot
[5971.82 --> 5977.34]  yeah yeah so it's like more doing you know it's like come on man let's just let's just make this happen
[5978.06 --> 5984.06]  well in light of that uh i was just gonna say can you give us the status as far as like version numbers
[5984.06 --> 5989.82]  are these 1.0 are they done are there roadmaps uh what's kind of the status of all these projects i know
[5989.82 --> 5995.58]  they're kind of old as far as yeah that's the awesome thing is you know they're all they're all
[5995.58 --> 6002.46]  been there for a long time and they haven't changed um there will be i'm sure there will be versions um
[6002.46 --> 6012.54]  coming um iron it mostly needs better documentation um because it has i think only like 10 of the
[6012.54 --> 6019.26]  features are actually documented in the example on the readme um the rest of them are not documented
[6019.26 --> 6024.22]  didn't stop people from uh from using them in some really smart ways because iron is actually
[6024.78 --> 6033.50]  bundled within with happy so the for example all the happy um secure cookies are using iron inside
[6034.30 --> 6039.50]  and so that has already been widely deployed i mean you can look at the npm download numbers right
[6039.50 --> 6043.58]  the the the hot code numbers are misleading because it's basically getting request numbers
[6043.58 --> 6050.30]  um because it's it's shipped it's shipping with requests and so it's giving a a distorted picture
[6050.30 --> 6055.74]  of how many people are using it because it's everyone who's using a request is using uh is has a piece of
[6055.74 --> 6063.42]  code of hawk in their application um but iron is pretty heavily used right now um it's it hasn't changed
[6063.42 --> 6069.02]  in a long time there is no reason to change it um if you want stronger crypto algorithm you just
[6069.02 --> 6073.10]  configure it with stronger crypto algorithm even though it ships with pretty secure settings out of
[6073.10 --> 6084.14]  the box um hawk has been um has been also very stable um we had no protocol changes um in hawk um
[6084.14 --> 6090.38]  hawk is the one place where there is some interoperability and actually if you look at the uh port label on
[6090.38 --> 6094.22]  the project it's kind of incredible it's like already poured to like nine or ten different platforms
[6094.22 --> 6101.98]  um i never talked about the project i never blogged about it i never gave talks about except for when i
[6101.98 --> 6110.54]  gave the the real-time kind of talk about oaf 2 um and somehow people found that module and adapted it
[6110.54 --> 6118.70]  and used it and ported it which is kind of kind of awesome um uh mozilla actually used hawk as as one of
[6118.70 --> 6126.30]  the security uh components of the when they were doing identity um for browser id um they use that
[6126.30 --> 6131.90]  for some of their security um i think they still do i don't know how active that project is but it was
[6131.90 --> 6141.34]  last i know they were using it um and so these two pieces are solid um they're very simple they have great
[6141.34 --> 6148.54]  browser support at this point um and they're widely used the the only piece that you can't knew in terms
[6148.54 --> 6158.78]  of uh outside attention is oz and oz is 1.0 and my guess is that um if it's going to have breaking
[6158.78 --> 6165.42]  changes it's going to be breaking changes in the node api not really in how it works um not in the
[6165.42 --> 6174.22]  internal structure um of the um of the tickets so it's pretty stable now so i guess uh now it's about
[6174.22 --> 6180.14]  the time we wrap up the show uh aaron i think we got a couple closing questions we'd like to ask
[6180.14 --> 6186.94]  our guests you've answered some of them in the past um so we won't ask you the hero question uh but
[6187.50 --> 6191.66]  a good staple would be if you can help the the listeners who've been listening to the show
[6192.54 --> 6197.98]  know how they can step into iron step into oz how can they support these projects
[6197.98 --> 6202.22]  projects uh or even hawk you know what's some of the needs that these projects have that the open
[6202.22 --> 6206.70]  source community can come in and step in and help out with i mean i've been really looking for people
[6206.70 --> 6214.38]  to to use it and play with it and and um it would be great if people who are experts can come in and
[6214.38 --> 6219.98]  look at it and and say whether public or privately that they looked at it and it looks good um
[6219.98 --> 6228.22]  uh iron and and hawk don't really need much at this point um they're used and they're pretty stable
[6228.78 --> 6234.06]  uh only occasionally someone will post a question um but i mean those two as far as i'm concerned are
[6234.06 --> 6240.62]  kind of finished um on the odd side um that's going to get more interesting so um if people are
[6240.62 --> 6246.46]  building new applications and they're kind of trying to decide what to use oaf1 or of two what but you
[6246.46 --> 6251.74]  know run with their own thing um you know take a look at it and see if you know if it works for you
[6251.74 --> 6257.82]  and if it does kind of join the conversation the the caveat is that because it's security protocol and
[6257.82 --> 6265.50]  you know and it's very hard for me to help people with their own implementation of it um or how they're
[6265.50 --> 6270.78]  going to use it because it's basically amounting to giving them security advice which is something that i
[6270.78 --> 6279.02]  don't do on principle um but if people who who feel proficient in that space who would if you're
[6279.02 --> 6282.54]  looking at oaf2 and you say i feel confident that i can go and write my own implementation
[6283.10 --> 6288.54]  then then you would be the right person to use oz and the right person to interact with with me on
[6288.54 --> 6293.50]  the project and you know one of the one of the directions that i want to take the project is to have
[6293.50 --> 6299.02]  really good story about mobile apps kind of that's where my next need is uh i think oaf2 does a
[6299.02 --> 6306.78]  terrible job with with uh native clients and um nobody really has a good story about native clients
[6306.78 --> 6311.42]  you know it's all kind of like security theater you know like encrypting secrets inside the client and
[6311.42 --> 6315.98]  people are like you know extracting them and posting them on the web and all this nonsense so i want to
[6315.98 --> 6322.14]  have a better story there um so that's going to be the next area to focus on all just kind of getting
[6322.14 --> 6328.62]  the the mobile experience uh figured out um how to use the authorization page with two factor off and
[6328.62 --> 6335.42]  all those things um so it's kind of more of an usability perspective of the of the space um
[6336.06 --> 6344.38]  implemented through and a specific implementation cool and our uh our last question i think this one
[6344.38 --> 6347.90]  is it kind of depends it's been a while since we've talked to you so it kind of depends on how you can
[6347.90 --> 6352.70]  answer this i imagine you're still in the same areas of your interest but what's something
[6352.70 --> 6357.90]  interesting out there that if you had more time or uh you wish you had more time to play with like
[6357.90 --> 6365.82]  what's on your open source radar um i wish i had time to do more node core work um there's two areas
[6365.82 --> 6372.78]  in particular that i find to be absolutely disgusting in node one is domains um and the other one is the http
[6372.78 --> 6380.78]  implementation um and i really wish that i had the time to go and um kind of like take over one of
[6380.78 --> 6388.86]  those areas and and like you know like rewrite them and submit it back to the the core team um i think
[6388.86 --> 6395.26]  those are two areas where it's going to be interesting i think the um kind of more of a meta area right now
[6395.26 --> 6403.98]  um is how the node community is going to um adopt all the new features that are available to them um i
[6403.98 --> 6411.34]  think that's a really interesting question of as we're migrating people from node 0 10 to 4 um
[6412.54 --> 6418.30]  you know how to to keep the module ecosystem you know going without kind of like alienating half the
[6418.30 --> 6424.38]  the community because they can't upgrade just yet um so i think that's an interesting one to solve and
[6424.38 --> 6429.34]  then once you have that like you know everybody will have to adapt their style guide and coding
[6429.34 --> 6435.10]  convention and everything to use all these new features so that's going to be um that'll be like
[6435.10 --> 6441.42]  presenting a whole new set of challenges um especially when you're in an established community that that
[6441.42 --> 6447.18]  that does follow strict guidelines like happy does um you know for example we having we have an open
[6447.18 --> 6452.94]  casting right now within the community is like which you know es6 features are we allowing people to use in
[6452.94 --> 6460.54]  um in happy modules you know because we do have a style guide and we kind of require everybody to
[6460.54 --> 6467.02]  follow it and so do we allow people to use const and symbols and let and error error function and
[6467.02 --> 6474.62]  promises and so on um because we want to make sure that the code remains readable by the entire community
[6474.62 --> 6481.82]  around the project we don't want to have one uh one module that you know is using features that nobody
[6481.82 --> 6487.50]  understands yet and so nobody can maintain it now especially if it's a dependency within happy core
[6488.06 --> 6493.74]  so those are the things the most interesting areas going on right now and um if i had more time i would
[6493.74 --> 6500.14]  definitely be diving more into node core to have more time would be just awesome everybody wants more time
[6500.14 --> 6507.34]  right well aaron i want to thank you uh for joining us for such a lengthy conversation about uh about oz and
[6507.34 --> 6514.14]  you know more importantly your passion for you know solving these problems and being uh you know a leader
[6514.14 --> 6519.98]  enough to to lead us there but also share it back through open source and just such a such an inspiration
[6519.98 --> 6525.58]  for those in the community to to aspire to be like and to to lead like so thank you for coming on the show
[6525.58 --> 6529.02]  i also want to thank our loyal listeners for listening to the show without you wouldn't be possible
[6529.02 --> 6535.02]  and also to our members and sponsors for sponsoring the show uh the sponsors for this show actually were
[6535.02 --> 6542.94]  code ship top tile casper the bed maker which was interesting for us as a sponsor and also imagex and
[6542.94 --> 6549.18]  next week we're talking to matthew holt about his h2 as we learned with the conversation with ilia we can
[6549.18 --> 6555.66]  shorten http2 to h2 we're talking about his h2 web server called caddy so stick around for that
[6555.66 --> 6569.66]  and uh at this time guys let's say goodbye so bye bye bye
[6569.66 --> 6575.66]  you
[6585.66 --> 6591.66]  you
[6591.66 --> 6605.66]  you
[6605.66 --> 6607.66]  you
