[0.00 --> 14.32]  welcome back everyone this is the change log and i'm your host adam stankowiak this is
[14.32 --> 19.62]  episode 132 and on today's show we have dave canada joining us to talk about buckets
[19.62 --> 26.92]  it's his project he's building on assembly it's a cms built on node.js great show today for you
[26.92 --> 31.68]  our sponsors for the show are code ship digital ocean and top tile we'll tell you a bit more about
[31.68 --> 36.74]  digital ocean and top tile later in the show but code ship hosted continuous deployment service
[36.74 --> 41.40]  that just works you can easily set up continuous integration for your application in just a few
[41.40 --> 46.74]  steps and automatically deploy when all your tests pass code ship has great support for lots of
[46.74 --> 52.26]  languages test frameworks as well as notification services they easily integrate with github or
[52.26 --> 59.46]  bitbucket and can deploy to cloud services like heroku aws nojitsu google app engine or even your
[59.46 --> 64.50]  own servers setup takes setup takes just three minutes get started today with their free plan
[64.50 --> 71.54]  and make sure you use our code the changelog podcast again the changelog podcast to get a 20 discount
[71.54 --> 78.34]  for three months on any plan you choose head to code ship.io slash the changelog and tell them the
[78.34 --> 89.12]  changelog sent you and now on to the show all right we're back this is uh adam i got david on the line
[89.12 --> 95.06]  as well jared on the line jared say hello hey everybody that uh sort of a bum voice this time
[95.06 --> 102.20]  around so we'll keep your talking to a to a minimum but david canada is with us he uh hey everyone
[102.20 --> 106.34]  he's no stranger to the show david you had to remind me sorry that that you were on the show
[106.34 --> 113.12]  way back when that's okay i think what was it five years ago or that was a very yeah let me go find
[113.12 --> 122.64]  the episode number uh you were on episode 30 and that was like forever ago july 27th 2010 there you go
[122.64 --> 128.90]  that's that's a long time ago and you were talking about sentia at the time too so yeah that jogs i
[128.90 --> 135.12]  remember it was like i forget like a couple months after i first moved to california and i've been here
[135.12 --> 140.24]  just about four or five years now gotcha and so we're having you on the show today because uh
[140.24 --> 148.88]  you're building an open source cms on node.js with mongodb you're building it on assembly it's totally
[148.88 --> 153.30]  a side gig so full-time you're a ux designer at google so you've got some you know you've got some
[153.30 --> 158.18]  history and the world knows some and probably uses several pieces of software that you've helped build
[158.18 --> 164.40]  or uh or uh or prop up and whatnot but that's what we have on the show today uh i think it was about
[164.40 --> 168.02]  two months ago two or three months ago we reached out and you weren't quite ready to come on the show
[168.02 --> 175.18]  and now you're i think you're at what uh 0.7.0 now is that right yeah yeah i mean it's still super early
[175.18 --> 182.32]  in the project but um but yeah it's i gotta tell somebody about it at some point yeah so i guess for
[182.32 --> 186.92]  those who don't uh know who you are and a bit more than what we just explained about you how do you
[186.92 --> 192.52]  introduce yourself i i say in terms of like the whole title thing i just say designer generally
[192.52 --> 200.28]  um although you know for the past five years or so i i definitely write way more code than i spend in
[200.28 --> 207.16]  photoshop or anything like that now but um i identify as a designer i started in print design
[207.16 --> 214.76]  uh got into the web started doing flash you know sort of all types of sites and then
[214.76 --> 222.36]  sort of around that time about five years ago i did jq touch which was a javascript library for
[222.36 --> 228.54]  creating native like experiences on the iphone and then that just sort of led into a whole sort of
[228.54 --> 235.34]  avalanche of doing mobile work and i think a lot of designers especially like web designers sort of
[235.34 --> 241.62]  fell down that path of getting into mobile what year was that i remember being a jq touch user back in
[241.62 --> 250.36]  the day it was uh i remember being amazed by it too thanks i think that was like six or seven years
[250.36 --> 258.14]  ago that first came out and uh and yeah it it blew me away like in terms of you know i just made this
[258.14 --> 264.88]  thing and i had you know sort of vaguely seen and used open source software but i just thought you
[264.88 --> 270.62]  know what am i going to do i'm not going to sell this thing but um but i think it's powerful so i so i put it
[270.62 --> 276.38]  out there and um you know this is like a little bit of a humble brag but i was just kind of blown away
[276.38 --> 282.34]  to see you know thousands of people starting to use it didn't that transition to something else at
[282.34 --> 289.26]  some point it went from jq touch to to something else i believe a paid product or so uh two things i i
[289.26 --> 299.08]  basically uh sent you which was called extjs then hired me uh and uh we formed a small team to work
[299.08 --> 304.72]  go and sent you touch and that um that was like commercial for like a month and then it became
[304.72 --> 311.86]  free and all that it's you know some corporate stuff and then um uh and then jq touch itself was
[311.86 --> 320.40]  renamed to jqt at some point because somebody like got angry for some reason crazy trademarks
[320.40 --> 326.06]  trademarks were you gonna ask jade before i jumped in there i was just gonna say i think that it just
[326.06 --> 331.20]  it struck a chord there was a big need or at least we thought we had a need for those types of
[331.20 --> 336.22]  toolkits at that time right when mobile just started kind of exploding it's funny these days
[336.22 --> 343.10]  because you still see them yeah all the time there's ionic now there's uh that one came out from the
[343.10 --> 351.90]  bootstrap uh team like uh ratchet i guess um but yeah it's it's interesting so tell us about buckets
[351.90 --> 357.04]  i was gonna say this is uh it's being built on assembly let's dive into this product and what's
[357.04 --> 364.86]  yeah so i mean i guess even before assembly like buckets is just a thing i've wanted to do for a long
[364.86 --> 372.88]  time i mean i i think i i would imagine the majority of web designers have either wished for a better cms
[372.88 --> 381.18]  or tried to build one or you know it's definitely not a new issue or problem um but i just
[381.18 --> 389.06]  as i as i as i left sentia about two years ago um i had spent pretty much my entire time there
[389.06 --> 398.64]  doing this sort of front-end heavy uh javascript and css you know framework and um was kind of eager
[398.64 --> 405.26]  to to get back onto doing some server-side logic doing just building apps uh on both sides
[405.26 --> 413.96]  and it was sort of just a thing i toyed around with the idea and i um about a year ago i was a
[413.96 --> 422.04]  designer in residence at benchmark a uh a vc firm here and they i i sort of told them about it and
[422.04 --> 428.50]  and what i wanted to do with it and they expressed interest um possibly raising a seed fund or a seed
[428.50 --> 435.20]  round for it um and so they said uh just get started just you know build the thing or at least like
[435.20 --> 441.04]  throw together a prototype and uh we'll see where it goes and after about a month of working on it i
[441.04 --> 448.44]  just kind of like threw in the towel because it was it was kind of uh isolating to to just work on it
[448.44 --> 455.92]  you know day in day out uh here out of my house and not sort of be sharing it and i the goal was always
[455.92 --> 464.28]  to open source it but it just you know it had to run first anyway uh so it was uh matthew smith
[464.28 --> 472.48]  uh whale on twitter who uh mentioned assembly and i saw that about six months ago and i thought well
[472.48 --> 479.14]  i love the idea i've always just kind of loved the idea of mixing uh some sort of commercial incentive
[479.14 --> 486.50]  with open source and i think just like without a doubt something to be done in that space um
[486.50 --> 493.36]  and so i thought this would be a great place to just throw buckets on there and see how people
[493.36 --> 498.82]  respond because you know i'd already basically given up on it or not even given up on it but just
[498.82 --> 506.74]  you know i had already burned myself out on it um and so in the beginning it was really just to seek
[506.74 --> 511.22]  you know some sort of validation of the idea like is this something people would be interested
[511.22 --> 515.58]  a lot of the especially when you're getting started especially when it's something like this
[515.58 --> 520.42]  that's sort of homegrown to a degree and and as you mentioned there quite possibly something you
[520.42 --> 525.62]  might even give up on if it's not something that other people can sort of encourage you in um you
[525.62 --> 530.46]  sort of need a tribe to to sort of validate whether it's something you should pursue or not like you
[530.46 --> 536.48]  said it's a cms isn't a new idea um some of the questions i have are you know
[536.48 --> 541.06]  why this over others that are out there what is this going to do better than some of those but
[541.06 --> 547.98]  that'll come a bit later but sure i i think if we can camp out this quickly on like taking it to
[547.98 --> 552.08]  assembly um i want to camp out there just for a little bit because it's it's sort of being built
[552.08 --> 557.10]  by the community as they say being built by the assembly community um and that validated the idea
[557.10 --> 561.22]  so what was about how long ago was that and what was the initial reaction you got
[561.22 --> 567.32]  first let's can you give us uh jennifer everybody just a general thing of what assembly is and then
[567.32 --> 574.12]  then go into the details so assembly um and i think they're still pretty early on themselves and so
[574.12 --> 579.76]  they're still figuring out but the sort of high level concept is you know you can create projects
[579.76 --> 587.00]  that are either open source or just like open source uh where anybody can contribute and that ranges from
[587.00 --> 596.56]  development like directly on github or uh design mocks or marketing even or copywriting and you
[596.56 --> 603.94]  basically you have bounties which are similar to github issues uh you say oh we need uh this feature or we need
[603.94 --> 610.08]  to be able to sign in with facebook and then as the uh project creator or as the core team you're
[610.08 --> 617.66]  actually able to assign a value um to that bounty and assembly sort of makes these values uh they use
[617.66 --> 624.90]  sort of like a cute coin system but ultimately it translates to uh just a percentage of of the
[624.90 --> 632.92]  product's potential uh profit at one point so um as pro as assembly products start making money
[632.92 --> 639.72]  they start to calculate a monthly profit fee and just simply distribute that every month
[639.72 --> 648.70]  to all of the coin holders based on how many they have that's a very sort of uh good thing but it's
[648.70 --> 654.94]  still even hard for me to grasp because it feels like it feels like it's potential like you said then
[654.94 --> 659.00]  you're not really sure how much it's going to be it feels like it's sort of upon the sky at least to me
[659.00 --> 664.06]  but that's why i'm not on assembly contributing to anything but it's it's it's a neat thing for those
[664.06 --> 671.38]  who have like one thing i liked about that though of just outside of you know the idea of not just
[671.38 --> 675.28]  contributing code like if you go to the different bounties that are there you can sort them by
[675.28 --> 679.38]  all these different things and if we sort yours by different tags you've got back end front end
[679.38 --> 684.36]  development simple challenging product you know copy marketing that's kind of neat because like if i'm a
[684.36 --> 689.90]  marketing guy that wants to jump into a product or i'm trying to you know get some notoriety some
[689.90 --> 694.36]  authority for my name or i'm just starting out you know i can hop on assembly and start
[694.36 --> 700.72]  throwing ideas at different products here and and land a team and have ownership is what you're saying
[700.72 --> 708.02]  with that those coins on bounty or on assembly and and like you said i think like i've always been sort of
[708.02 --> 715.72]  a general product kind of guy i like design i like marketing i i like copywriting and i've always sort of
[715.72 --> 721.02]  enjoyed both ends of it whether you're doing the actual hands-on work or more of a directing like
[721.02 --> 726.78]  sort of a creative directing position or something um and so like i think a great example is just our
[726.78 --> 733.70]  logo um and that's actually a good thread i like that one too a bucket yeah uh with a sort of a little
[733.70 --> 739.06]  smiley face kind of built in and that was something i mean it's simple and it's it's straightforward
[739.06 --> 747.76]  and uh a friend john peele made that um but uh it was something i i just kind of had it had a very
[747.76 --> 753.28]  rough idea i think if you saw that thread i i actually just grabbed a photo off of google image
[753.28 --> 759.04]  search literally like took four minutes um drew some eyes on it and said here's kind of like the
[759.04 --> 765.00]  concept i'm thinking and somebody illustrated and and with a great style to it and i sort of
[765.00 --> 769.86]  wanted the yellow background and everything but but ultimately it came came out as something that
[769.86 --> 776.24]  was just super simple super friendly and that's all i wanted it to be you know and it was it was
[776.24 --> 780.26]  perfect you can see the you can see the riffing too back and forth between you and the contributors
[780.26 --> 784.94]  and whale who you mentioned earlier yeah um you know sort of the iterative process too through
[784.94 --> 792.22]  this bounty slash kind of github issue ish kind of thing and see you can sort of see the morphing and
[792.22 --> 797.34]  and even the collaboration that's i like how nita came out too i think it's a it's a good direction
[797.34 --> 804.88]  but let's let's jump on sort of getting to assembly um and what that did for for you and your inertia
[804.88 --> 813.90]  towards buckets yeah i mean again i think just having people say oh hey that that would be nice uh is is a
[813.90 --> 821.54]  huge thing you know because uh especially in the like uh creating a product that is so overdone or done
[821.54 --> 829.64]  so many times um like even within the node community which is way you know way newer way younger than
[829.64 --> 835.84]  php or anything like that even within the node community there's already four or five sort of
[835.84 --> 843.00]  prominent and still they they don't really compare in terms of uh scope to wordpress or expression engine
[843.00 --> 850.74]  or drupal yet but um but still there's there's competition kind of everywhere and so you know when
[850.74 --> 857.38]  you're going to throw your hat in the ring so to speak and and try to do your own uh yeah you first
[857.38 --> 863.26]  went okay is there somebody out there who would like to see it done differently or that kind of thing
[863.26 --> 871.24]  yeah when i searched for node cms on google what there's several that came up but one that looked
[871.24 --> 876.80]  like it was decent and i sorry if i haven't seen this one before um i'm not hanging out in the
[876.80 --> 881.10]  the community too much but enough to know it's there and what's going on there keystone js was
[881.10 --> 886.42]  one of the examples and they got a decent design they've got you know a decent product direction in
[886.42 --> 893.58]  terms of what is happening with it so like you said it's for sure that's new they terrify me uh no no
[893.58 --> 901.32]  it seems super cool um and same feature set too it's node and mongo so yeah it's it's a similar
[901.32 --> 909.08]  kind of feel i think yeah um and then just to throw out the others like uh well there was one
[909.08 --> 914.92]  called calypso but it seems like that one died down and that was never uh i want to be nice on
[914.92 --> 922.18]  the show but like it was never 404 right now too pretty it was not like you know like um but then
[922.18 --> 926.82]  there's there's ghost as well which ghost is tremendously beautiful you know kickstarter project
[926.82 --> 933.30]  and it's very beautiful well designed and and actually a very similar architectural setup to
[933.30 --> 938.92]  what we have um which kind of happened by happenstance i swear i didn't copy them but um
[938.92 --> 944.18]  but the interesting thing was always that you know i knew about ghost when i started buckets but
[944.18 --> 950.70]  i i actually wanted to do something that was kind of completely the opposite in some ways uh so ghost
[950.70 --> 956.48]  basically came like looked at something like wordpress and said okay this has grown to the point where it's
[956.48 --> 964.14]  not even really great for blogging anymore uh so let's like strip it back down to to what made it
[964.14 --> 970.42]  great for blogging whereas with buckets i wanted to create a tool that was more for these big websites
[970.42 --> 974.92]  you know when you're like a web designer and you have to do a website for a university or something
[974.92 --> 981.52]  it's not so much about okay does it give you that single panel uh text area with a nice preview
[981.52 --> 990.08]  it's more about is the content structured uh correctly and and how easy is it for the um
[990.08 --> 997.48]  end user to just input content right yeah it's a there's pros and cons on on both sides that that's
[997.48 --> 1002.68]  that's where i was wondering too what you might think um of ghost versus buckets because you know
[1002.68 --> 1007.42]  people tend to take a blog software and try to make it more than it is
[1007.42 --> 1013.90]  and then you'd sometimes try to take a cms and make it a blog software and a cms and they end up
[1013.90 --> 1019.50]  doing too many jobs and not enough focus on the end user and the content because that's yeah so part of
[1019.50 --> 1024.56]  the huge piece of being a cms too is actually managing the content not just theming or design
[1024.56 --> 1030.30]  it's it's got several different totally and i look at it as like i not to say that we'll never have
[1030.30 --> 1039.60]  a full page full screen markdown editor similar to ia writer or something like that uh but that's
[1039.60 --> 1046.64]  definitely not going to be a place that we head soon i see it like in in terms of like the experience i
[1046.64 --> 1051.46]  want to deliver and i think you bring you bring up a good point in that like cms's have have two
[1051.46 --> 1058.40]  audiences which is sort of the content administrators and then the designers the web designers right um and
[1058.40 --> 1064.34]  so for the content people i want it to feel like tumblr um and that was like sort of a big inspiration
[1064.34 --> 1071.18]  for buckets was this idea that you go into tumblr you have these five sort of types of posts you can
[1071.18 --> 1081.12]  create which are uh text video chat photo and link and they're just extremely well designed well tailored
[1081.12 --> 1087.60]  uh sort of input fields for these types of content and then when you're working with a system like
[1087.60 --> 1093.70]  expression engine or drupal or one of these bigger cms's you define content into these like sort of
[1093.70 --> 1101.46]  distinct blobs in a similar way uh but usually the ux just isn't even anywhere close to that tumblr
[1101.46 --> 1107.56]  experience right right and so that was sort of that's sort of the driving force for me on the
[1107.56 --> 1114.36]  the content creator side is to to make it feel like that to make more of a tumblr than a medium
[1114.36 --> 1121.74]  so i guess to those who because we've had john nolan on the show before to talk about ghost
[1121.74 --> 1127.72]  for those who think they might want to use ghost versus something else how does this differentiate
[1127.72 --> 1133.42]  from blogging software i guess in the in the bigger picture it's full-on cms where what is some of the
[1133.42 --> 1142.26]  vision for um the cms pieces so a couple things one like you create buckets and you define the fields on
[1142.26 --> 1150.10]  those buckets so you know you could create a recipe and every you say every recipe has a cover photo a
[1150.10 --> 1159.18]  title a uh list of ingredients and a uh steps let's say you know and you can sort of fine tune those
[1159.18 --> 1166.14]  fields and and uh manipulate those fields and i and i want those fields to be sort of very rich at the
[1166.14 --> 1173.28]  when you say manipulate you mean like validation um validation just sorting uh most fields come with
[1173.28 --> 1178.64]  a good amount of options but but there's still a lot of work to be done in that area but essentially
[1178.64 --> 1185.80]  that's the idea as opposed to you know every item in your cms has a title a body and an excerpt
[1185.80 --> 1192.70]  um it's much more define it yourself and so you come up with these you end up with these forms that
[1192.70 --> 1198.96]  are just sort of very specific to your content that's helpful too like you said earlier on
[1198.96 --> 1204.84]  whenever the designer the builder of this throws it over the the fence to the end user and says okay
[1204.84 --> 1210.76]  university here's your site they don't have to you know give a ton of docs it's like go here and
[1210.76 --> 1216.42]  create and exactly the form exactly like at the end of the day that that side of it if you look at
[1216.42 --> 1223.80]  all social networks or you know of a certain type that manage content you know people use them every
[1223.80 --> 1230.80]  day and and sign up for them by themselves and and figure them out right and and that essentially is
[1230.80 --> 1236.96]  what a cms is like if you look at something like pinterest it gathers photos and and puts them into this
[1236.96 --> 1242.70]  nice layout but you know that's essentially a theme that grid that you get to the content that you're
[1242.70 --> 1249.96]  adding in and there's no reason that a cms can't provide that same ease to to sort of get into it
[1249.96 --> 1258.98]  um yeah let's pause the show for a minute give a shout out to a sponsor digital ocean simple cloud
[1258.98 --> 1266.32]  hosting built for developers in 55 seconds you'll have a cloud server with full root access and it just
[1266.32 --> 1272.06]  doesn't get any easier than that pricing plan started only five bucks a month for half a year ram
[1272.06 --> 1280.70]  20 gigs of ssd drive space one cpu and one terabyte a transfer that's a lot for five bucks a month
[1280.70 --> 1288.24]  digital ocean also has data centers all across the world new york san francisco amsterdam singapore and
[1288.24 --> 1293.32]  their newest region london you can easily migrate your data between those regions making your
[1293.32 --> 1301.14]  data always closest to your users use the promo code changelog november in lowercase it's important that
[1301.14 --> 1307.20]  use lowercase changelog november to get a ten dollar hosting credit when you sign up head to
[1307.20 --> 1313.56]  digital ocean.com right now to get started and back to the show so we're talking about some of the
[1313.56 --> 1318.12]  philosophies around it where and i think you might even say we're getting there we're not quite there
[1318.12 --> 1324.32]  yet where exactly are you you know we know you're at 0.7.0 but what does that mean what yeah so the
[1324.32 --> 1329.86]  features that are built out now and like admittedly development has slowed down the past couple weeks
[1329.86 --> 1336.40]  i think partly due to uh just getting into some stuff at at the google and and sort of putting
[1336.40 --> 1344.48]  into time uh but also um i've been sort of i guess just mentally kind to trying to figure out the next
[1344.48 --> 1351.40]  place well i'll go back so at first like the the first two months or so the development was very heavy
[1351.40 --> 1358.46]  because i was i was sort of focused on that uh the admin panel which is sort of my you know what i
[1358.46 --> 1367.00]  am best at focusing on uh in terms of like ui ux the javascript uh architecture uh the whole thing is a
[1367.00 --> 1373.30]  single page app which again compared to a lot of systems out there is a lot different and which which
[1373.30 --> 1380.92]  also means it's like sort of crazy fast um when you're using the admin so i i worked on a lot of the
[1380.92 --> 1388.28]  sort of interface which is still very basic but um kind of rich in in a lot of ways and then
[1388.28 --> 1393.80]  i worked on uh search for a little while that actually hasn't even shipped yet i've just kind of
[1393.80 --> 1398.44]  kept that off to the side because i'm i'm still not 100 sure i want to go with elastic search
[1398.44 --> 1404.66]  but um but anyway it was sort of just this you know creating features creating the template
[1404.66 --> 1410.72]  parser um which is sort of based on handlebars right now and those types of things and to the
[1410.72 --> 1418.16]  point where it can now create a very basic website and and we have maybe six or seven different types
[1418.16 --> 1424.40]  of uh fields that you can add on to each bucket so now i'm i'm sort of hitting a point where
[1424.40 --> 1431.28]  i know that eventually i do want to offer this as a as a sas offering uh the more i think about it
[1431.28 --> 1439.98]  the more i think i i am in no place in terms of uh sys ops to be um sort of kicking off managed
[1439.98 --> 1445.56]  instances of buckets you know because it is node and it does have to run in a cloud environment
[1445.56 --> 1453.70]  and so sort of the clearer and and obviously much simpler path for buckets to take is is to become sort
[1453.70 --> 1460.06]  of multi-tenant and to allow you know multiple not just multiple users which it which it already
[1460.06 --> 1465.56]  supports but multiple accounts that are all creating their own websites and i'm i've been
[1465.56 --> 1471.72]  sort of been wrestling with this idea for the past two weeks because i on one hand i want the system
[1471.72 --> 1477.60]  and in some ways even though it's very different in terms of being node the architecture i want it to
[1477.60 --> 1485.26]  feel like wordpress or text pattern or those older php ones where okay i install it on my computer i can
[1485.26 --> 1492.96]  run it at localhost i move it to a server i run it over there um where if we switch to this sort of
[1492.96 --> 1502.52]  platform uh approach obviously a lot of that ease sort of goes away um it's a hard line to follow too
[1502.52 --> 1507.46]  when you make that twist because it's going to impact you know you work full-time right so you got
[1507.46 --> 1511.92]  little time and so the time you do spend you want to you want to spend on progress not exactly
[1511.92 --> 1517.84]  now you're seeing exactly why i've been uh twiddling my thumbs a little bit the past week but
[1517.84 --> 1523.40]  maybe you can come to some of these decisions here on the show i don't know but to me i feel like
[1523.40 --> 1527.56]  it comes down to figuring out your target audience right like and that's sort of a question i have
[1527.56 --> 1532.92]  next is like you know when you ship this when it's ready at whatever stage it's at the 1.0
[1532.92 --> 1540.04]  who is you know who's your short list of the kind of people that you're going to see god is it people
[1540.04 --> 1545.82]  on squarespace is it people using wordpress as a php developers yeah tinkering with javascript and node
[1545.82 --> 1552.20]  because i'm you know because of the ubiquitousness of it lately and not lately but just the the trend
[1552.20 --> 1556.92]  of the upper trend of the last few years towards javascript and you know is it people that hack on
[1556.92 --> 1561.94]  ruby that make their own stuff like who's your customer it's definitely web designers okay and
[1561.94 --> 1571.08]  like a hundred percent i can say initially people with html and css uh experience and who want to use
[1571.08 --> 1579.72]  html and css um the the idea being that i've just always sort of thought content management uh and
[1579.72 --> 1586.00]  especially when you look at these web content management systems like you know i don't think a
[1586.00 --> 1590.14]  lot of them handle that content creation side well like we were talking about sort of on the user
[1590.14 --> 1597.08]  experience angle um but then also on the web designer angle or web developer like grabbing
[1597.08 --> 1605.12]  that content and then like putting it into a page should be extremely easy yeah um and and i you know
[1605.12 --> 1613.30]  i've always personally just cringed when i see like uh wordpress templates using raw php um things like
[1613.30 --> 1617.84]  that but so you mentioned wordpress is there anything about wordpress that you've used before that sort of
[1617.84 --> 1623.04]  because if you take the 37 signals approach it's always like have an enemy right yeah and i don't
[1623.04 --> 1626.54]  use gantt charts was base camps original thing and that's sort of what kicked that off and it was
[1626.54 --> 1632.14]  like you know it's about conversations and people not and things to do not gantt charts and graphs and
[1632.14 --> 1636.92]  whatnot so totally who's your enemy so it wouldn't be wordpress i always just say wordpress because like
[1636.92 --> 1644.12]  when you're you know it's the lowest common denominator of the net yeah um but it's really drupal uh i would
[1644.12 --> 1651.80]  definitely uh i would say drupal okay uh anything that feels like well they've got a pretty cult-like
[1651.80 --> 1659.50]  following though like anybody who does use drupal community and it's a somewhat kind of gross product
[1659.50 --> 1665.18]  uh and i i feel bad putting down anything you know at any time even on twitter and stuff but um
[1665.18 --> 1671.10]  but if i had to you know obviously i'm i'm making a competitor so there has to be some stuff out there i
[1671.10 --> 1678.16]  don't like um but drupal drupal sort of represents that you know it you look like you're using
[1678.16 --> 1684.42]  php my admin or some you know like database administration tool um
[1684.42 --> 1692.36]  yeah and and and i would say even like systems that i i'm really fond of like uh craft came out
[1692.36 --> 1698.14]  and and that came sort of out of the expression engine community one of the developers i think his
[1698.14 --> 1704.64]  name is brandon kelly i hope i get that right um who who did a lot of plugins and and sort of the
[1704.64 --> 1710.44]  most popular plugins for expression engine made his own cms and and it's really elegant there's like
[1710.44 --> 1718.36]  a lot of extremely impressive pieces to it but it's still to me just at a certain point feels a little
[1718.36 --> 1724.88]  bit like just rows you know tables of lists and then you click and you're in a detail view and you know
[1724.88 --> 1733.10]  like uh that very sort of straightforward um database administration feel well now that we've
[1733.10 --> 1739.76]  talked a bit about i guess some of maybe your your competitors enemies inspiration whatever however
[1739.76 --> 1743.98]  you want to word that obviously you're building this around the community on assembly so how does
[1743.98 --> 1749.66]  how has and how does and how is the the community that's sort of because you've got 294 followers on
[1749.66 --> 1754.86]  assembly for this project i don't know how many are really actively involved or involved or
[1754.86 --> 1761.64]  contributing ideas but how do they help funnel this idea of monetization and the overall what
[1761.64 --> 1767.30]  would be the architecture of how you build this product so this is kind of like a weird answer but
[1767.30 --> 1774.22]  kind of not enough in some ways i i wish there was a little bit more or i wish you know i knew of
[1774.22 --> 1778.84]  people that i could just say okay this is my team of five people that i can ask these sort of
[1778.84 --> 1786.58]  high level big questions too regarding the multi-tenant sort of ambitions i think that i am
[1786.58 --> 1792.98]  planning a blog post i might put it out tomorrow or monday about this and sort of asking the community
[1792.98 --> 1797.70]  what do they think do they have ideas that kind of thing um i didn't want to publish that blog post
[1797.70 --> 1804.80]  until i had a little bit more concrete plan on how we would do it which um i'm going to outline in
[1804.80 --> 1814.08]  there but uh in some ways like and and it also sort of goes up and down like uh some weeks uh there
[1814.08 --> 1821.26]  will be no activity on assembly and i'll um i'll like sort of post things in the chat and and it just
[1821.26 --> 1826.92]  goes quiet for a couple days or like a week um and then other weeks i'll get you know people making
[1826.92 --> 1833.78]  bounties people adding pull requests sort of every day yeah um and i guess that's kind of typical for
[1833.78 --> 1839.72]  all open source software or at least in the beginning in the early stages but it's it's an
[1839.72 --> 1849.22]  odd thing to create a cms i think because or even any sort of big uh i guess app and not just something
[1849.22 --> 1855.94]  that's a framework or a tool or a library uh which i guess is what i'm used to because like
[1855.94 --> 1861.16]  you know your trajectory is so far right i mean you go so many different directions and everybody has an
[1861.16 --> 1867.50]  opinion and and i also just don't like if i put myself in somebody else's shoes like i would never
[1867.50 --> 1875.16]  use buckets like who who um who wants to build he just say that jerry i think he did i'm trying to
[1875.16 --> 1882.70]  wait for the for the rest of the sentence at this stage i i shall uh supplement it with at this at this
[1882.70 --> 1891.02]  stage like who would build a website um you know for a client on alpha software um yeah personally i
[1891.02 --> 1897.60]  would not uh and and i don't expect anyone to but at the same time it's you know it's hard for somebody
[1897.60 --> 1904.92]  to play with something or to you know experiment or uh test something uh you know 10-15 hours a week
[1904.92 --> 1910.26]  when they're not doing something productive with it at the same time you know unless though unless they
[1910.26 --> 1916.00]  have the same pain as you and they want buckets to exist just because of the same ideas and the
[1916.00 --> 1920.68]  same pain points you've experienced which is exactly a good builder experience and a good client level
[1920.68 --> 1928.60]  experience that surpasses others that are in your space yep totally and i think i've had uh from
[1928.60 --> 1936.70]  assembly maybe two or three people who have really um done a surprising amount more than i expected
[1936.70 --> 1944.06]  uh with certain parts of the the app so how does that work when somebody wants to get involved with
[1944.06 --> 1951.62]  buckets via assembly do they just sign up and say i'm here i can help i think this is cool and you say
[1951.62 --> 1960.84]  okay can you say no um no i can't say no interestingly i just had a spam sign up the first one ever like uh
[1960.84 --> 1966.20]  a week ago i don't know if it was spam maybe the guy really like his grandma's really sick or something but
[1966.20 --> 1972.28]  um but i can't i can't get him out of there i think they're going to help me out with that at some
[1972.28 --> 1979.10]  point but um no they uh it's actually it's very much like you just described in fact if you go to
[1979.10 --> 1986.38]  assembly.com slash buckets like uh they just revamped the uh sort of home page feed and you can see
[1986.38 --> 1992.22]  people's bios as they're signing up um they just pop in and i think when they sign up for a project
[1992.22 --> 1997.46]  uh assembly ask them hey say a little bit about yourself why why are you interested in buckets
[1997.46 --> 2003.48]  and so they usually say you know oh i've uh you know i'm a java developer i've played around with
[2003.48 --> 2009.20]  uh some node or you know uh i'm more on the marketing side but i'd love to help that type of thing
[2009.20 --> 2016.78]  and then i typically you know i i try to sort of give everybody a custom hello and and make sure
[2016.78 --> 2022.88]  you know they can find the things uh if if they want to help if they want to contribute like i i i'm
[2022.88 --> 2028.60]  always telling people if if you need a bounty like i think there's like a hundred some on assembly right
[2028.60 --> 2035.56]  now um because i basically will throw any idea i have into the bounties um if you want a bounty
[2035.56 --> 2043.08]  literally just ping me either im me or twitter dm me or or hit me up in the assembly chat and just say
[2043.08 --> 2049.12]  this is the type of stuff i like to do um and i'll find one for you i can find one within 10 minutes
[2049.12 --> 2055.88]  so as a project owner you create the bounties um i think anybody can create the bounties i hope
[2055.88 --> 2060.88]  anybody can yeah any so if you sign up anybody can create a bounty anybody can create a discussion
[2060.88 --> 2067.16]  yeah and then um i don't know how the assignment of coins applies to that but i'm assuming that's
[2067.16 --> 2074.02]  probably something that's on your side um i i don't know yeah again because uh i don't i want
[2074.02 --> 2078.48]  to but i don't play with sort of other people's projects much i just don't have enough time i would
[2078.48 --> 2084.88]  love to like just jump in on somebody else's too but um yeah so i know what it's like for me when i
[2084.88 --> 2091.10]  create a bounty and it gives me sort of the coin um interface but i i don't know what it looks like
[2091.10 --> 2096.88]  to anyone else i doubt they would just let you create a bounty with zero coin value yeah
[2097.16 --> 2103.68]  you gotta give up something right yeah and then the interesting thing is every bounty uh dilutes
[2103.68 --> 2109.62]  the pull of coins is simply added on top um so you're not subtracting from a hole you're actually
[2109.62 --> 2117.52]  just adding yeah like a lot you know because yeah that's better like let's say you own 10 percent of
[2117.52 --> 2123.94]  buckets um it sort of guarantees that you have to keep doing something not a not a lot but in fact
[2123.94 --> 2130.32]  less so sort of exponentially over time but uh you have to do something to maintain that 10 percent
[2130.32 --> 2139.28]  level you know right so man it sounds like this is a little bit wild west in the sense of okay from
[2139.28 --> 2145.04]  from a from a person who's trying to get involved it's very speculative it's you're investing it's
[2145.04 --> 2149.92]  kind of like kickstarter for open source to a certain degree as far as you're not selling people
[2149.92 --> 2153.50]  you're not trying to get people's money you're trying to get their time and you pitch them on
[2153.50 --> 2158.30]  your project and for them they're investing their time and their skills into something that they hope
[2158.30 --> 2163.54]  will make money some at some point yeah and yet somebody somebody could come in and just completely
[2163.54 --> 2170.20]  harpoon this thing right by just being like a total loser contributor totally and that's where
[2170.20 --> 2178.88]  that's where we're a little bit i think we're on the more um special side of assembly in that way
[2178.88 --> 2184.86]  you know there are products on assembly that are already making money okay um and you know and
[2184.86 --> 2189.08]  again i think this also comes back to like a cms is a little bit different in that it's it's
[2189.08 --> 2195.84]  clearly like a long tail thing it's it means establishing a community a plug-in system you know all those
[2195.84 --> 2201.32]  things that that are not going to be you know six months away but i almost feel like they should be a
[2201.32 --> 2208.24]  little restrictive though because if you can't i feel like the for you for buckets for this open source
[2208.24 --> 2214.80]  cms that hopes to one day be a sas product that generates some revenue i feel like for you you
[2214.80 --> 2219.22]  want to be able to assemble a team that you don't personally know that you can attract people to and
[2219.22 --> 2225.36]  join a collaborative community that isn't on github because github's more open source than it is
[2225.36 --> 2232.16]  assembly um but still have free reign of like who can join the team or not like who earns their way
[2232.16 --> 2237.72]  so no no but um but you don't earn any coins unless you complete a bounty right right of course
[2237.72 --> 2243.96]  but like joining you know the discussions and just sort of like spamming like like the one person you
[2243.96 --> 2249.14]  mentioned i feel like i'm actually i'm kind of okay with i mean there's like that was only one
[2249.14 --> 2256.30]  sign up and he had a weird uh thing about his grandmother and his bio but um but aside from that
[2256.30 --> 2262.00]  you know it would get very little noise and and i actually i would actually up to the other side of
[2262.00 --> 2268.58]  that where um i i've actually and you know i talked to the assembly guys and and i'm i'm kind of friendly
[2268.58 --> 2277.12]  with them and i actually pushed them to to allow more anonymity within the app um you know for example
[2277.12 --> 2283.82]  the chat it would be great if uh anonymous people could join into the chat i think and i realize that's
[2283.82 --> 2289.52]  asking for a whole world of hurt but at the same time like i'm sure you've seen products or sites
[2289.52 --> 2295.92]  where they have sort of an open slack room that you can join if you have some sort of pre-install or
[2295.92 --> 2302.12]  pre-sales questions um yeah and i i actually like that you know and if hopefully there are tools you
[2302.12 --> 2308.72]  know for banning or whatever uh spam types of things but um but in general even like you know on github
[2308.72 --> 2314.54]  i like getting issues from random people uh and that's another thing i've discussed and we're sort
[2314.54 --> 2321.34]  of i'm sort of in the process of discussing with assembly is uh we're sort of debating whether or not
[2321.34 --> 2328.04]  to allow uh github issues because you know it's clearly creates like a little bit of confusion over
[2328.04 --> 2335.46]  okay where do i put this bug you know is it bounty or is it a uh github issue right i kind of want
[2335.46 --> 2342.76]  them to open it up because uh you know my sort of thought is not everybody who uses buckets is going
[2342.76 --> 2350.02]  to come from assembly uh and and github is clearly in the developer community a pretty well-known
[2350.02 --> 2356.36]  prominent tool everybody has an account everybody has used the issues before um but i you know i see
[2356.36 --> 2363.44]  both sides of the coin there but yeah in general i love the idea of as open as possible let's pause the
[2363.44 --> 2367.40]  show for a minute give a shout out to a sponsor top towel if you've listened to the show over the
[2367.40 --> 2372.54]  last year you've definitely heard us talk about top towel we uh we've seen firsthand the the fruits
[2372.54 --> 2377.30]  and benefits of having top time the community helping marry really great opportunities for
[2377.30 --> 2384.14]  developers with really great developers uh as top towel says elite engineers um i wanted to mention
[2384.14 --> 2390.04]  because this is a node.js focus show um you can actually hire top node.js developers right now on top
[2390.04 --> 2395.54]  towel and if you are a top node.js developer and you are not working with top towel and you'd like
[2395.54 --> 2400.70]  to check out freelancing or go into some of that kind of stuff you can go to top towel.com slash node.js
[2400.70 --> 2406.50]  you'll find uh really awesome node.js developers in their community already um and at the very top of
[2406.50 --> 2410.58]  the screen you can see apply as a developer click that button right there it'll take you through the
[2410.58 --> 2415.82]  process of actually becoming an elite engineer with top towel go to top towel.com slash node.js
[2415.82 --> 2423.08]  and now back to the show we've talked a while i guess we try to establish what what size of the
[2423.08 --> 2427.82]  team you do have or don't have so it seems like you're the core team right now yeah who else is
[2427.82 --> 2435.06]  on the team with you i would say um so nobody i i keep myself as the core team for now like i would
[2435.06 --> 2442.02]  i would absolutely adore to sort of promote somebody else to the core team but uh i think as a core team
[2442.02 --> 2450.64]  you get sort of i forget i think it's like three to five percent of all um bounties is just sort of
[2450.64 --> 2456.74]  reserved for you and it and that five percent i think is split among the core team uh and not like
[2456.74 --> 2461.18]  i'm trying to sound greedy but you know uh if somebody's going to if we if i start splitting that
[2461.18 --> 2466.40]  and we get 2.5 percent each like i just want to make sure it's somebody that's committed committed yeah
[2466.40 --> 2472.92]  into it yeah yeah and uh you know so if somebody was just sort of knocking out bounties for like
[2472.92 --> 2481.28]  two months straight um i i i wouldn't hesitate but anyway for now i'm i'm the core team i think if you
[2481.28 --> 2487.38]  were to look at our github i think we've had about 15 or so contributors um some of them smaller than
[2487.38 --> 2495.14]  others but um i would say 10 to 15 people in general have really jumped up on the the code side
[2495.14 --> 2502.18]  so maybe 20 to 25 people total in terms of also design things uh etc on assembly
[2502.18 --> 2509.14]  shout out to uh charles pletcher he's got uh let's see how many commits he's got 69 commits so he actually
[2509.14 --> 2516.00]  he's part of assembly and uh oh there you go he jumped on early on uh he did he did some awesome
[2516.00 --> 2522.08]  fantastic stuff for the templates and everything um i've been sitting over here thinking it just sounds
[2522.08 --> 2527.80]  like what you're missing is a is a partner in crime like you like a second person somebody more
[2527.80 --> 2534.04]  on the system back end ops side that really would just complement your talents it seems like you're
[2534.04 --> 2539.56]  pretty well rounded but to help make those big decisions you know uh i was thinking a lot about
[2539.56 --> 2544.40]  last year as i was like trying to do this sort of on my own was i just thought oh if i just had that
[2544.40 --> 2550.06]  that technical co-founder you know that like dream thing everybody around here wants but but at the
[2550.06 --> 2558.32]  same time i don't you know i've i've done businesses and and sort of apps and things uh with partners
[2558.32 --> 2563.06]  that i've met and just sort of reached out to and all kinds of things and i just sort of thought
[2563.06 --> 2570.76]  this is for me personally like much more of a long tail thing and if there was that person like i would want
[2570.76 --> 2576.04]  a lot of trust in that person you know i i just wouldn't want it to be something i i you know
[2576.04 --> 2583.88]  post an ad on weekendhacker.com and somebody's yeah that's a great idea um you know because it's just
[2583.88 --> 2589.72]  that's it's great for getting off the ground but it's that like you know two years in and you guys
[2589.72 --> 2594.76]  have different ideas of how it becomes a business i just didn't want to deal with any of that which is
[2594.76 --> 2600.40]  a little not narcissistic but you know it's a little limiting in that i'm like putting a lot on
[2600.40 --> 2608.16]  myself for now but um but like i said i'm i'm open to it i if somebody you know seems like assembly is
[2608.16 --> 2613.44]  a decent vetting solution for that where you can you know they can come and put their time in get
[2613.44 --> 2619.50]  get some i guess equity over time build up trust show that they've got the skills and then eventually
[2619.50 --> 2627.00]  could become that person i actually did offer it to charles to uh charles pletcher uh like a few
[2627.00 --> 2632.26]  months ago i said you should become part of the core team because he clearly sort of knew what was
[2632.26 --> 2636.98]  going on in the architecture and and i think he had a good idea of where i was going but he was like
[2636.98 --> 2642.24]  you know uh i'm gonna eventually i'm gonna have to spend some time on other assembly projects and
[2642.24 --> 2652.30]  actually put in time for assembly itself um so he declined but um hopefully one day so if you're out
[2652.30 --> 2659.14]  there and you're a back-end hacker as jared just uh described and and you like david and you think
[2659.14 --> 2665.92]  that buckets has a good direction and you could just hop in work hardcore for two months and he'll
[2665.92 --> 2673.40]  promote you to core totally right yeah i mean if i were to describe my dream situation if like i've
[2673.40 --> 2679.30]  completely loved working on the node side and i love working with node um but like you said like
[2679.30 --> 2685.56]  it's sort of more in that sysops realm that i i just it's not as fun for me like if i got to spend
[2685.56 --> 2692.52]  you know twice as much time just kicking out the user interface and doing more custom fields you know
[2692.52 --> 2700.60]  we need like relationships um types of fields we need repeater types of fields anyway so we talked a ton
[2700.60 --> 2705.60]  about the the product itself but we're obviously this is the change log we like to get a little technical
[2705.60 --> 2712.58]  um on this show so you mentioned node obviously mongodb i i saw earlier in in your history too you
[2712.58 --> 2719.02]  moved from rethink to to mongo i think that was for windows is that still like what were some of the
[2719.02 --> 2726.10]  reasons why you chose node and chose mongo and and why node so node was the easy choice because i just
[2726.10 --> 2735.22]  knew i wanted to do it in node um the reasons for that are um you know partly convenience because i'm a
[2735.22 --> 2742.82]  front-end guy and so javascript feels natural to me um it was partly an experiment because i just
[2742.82 --> 2750.20]  wanted to try something new um i think you know and again i'm more of a front-end guy so i i don't
[2750.20 --> 2755.36]  want to like say the wrong thing but like looking at sort of the spectrum of all the different
[2755.36 --> 2762.46]  server-side tools and things you have now um you know i'm personally i'll just never build a java app
[2762.46 --> 2772.56]  um ruby is to me just ruby seems like the uh i'm gonna get in trouble here but sort of a childish
[2772.56 --> 2786.06]  equivalent of node oh yikes not yikes not quite as no no i think uh yeah um how so how so it's it's
[2786.06 --> 2795.70]  just not quite as impressive in terms of its scalability right um and the the sort of
[2795.70 --> 2805.32]  asynchronous evented nature of of node um actually allows for certain things like i think on the the
[2805.32 --> 2812.44]  surface they seem quite similar um but at the end of the day in a lot of situations node is much much
[2812.44 --> 2822.84]  faster um and for me easier to develop in because it is javascript the evented model provides for that
[2822.84 --> 2830.70]  right so yeah and um which you can do in ruby but it's not the typical web frameworks are not using
[2830.70 --> 2838.90]  event machine so they don't have that built right in whereas node does yeah what about the the back
[2838.90 --> 2844.94]  end um i think a document-based database makes a lot of sense because your cmss are basically just
[2844.94 --> 2849.64]  storing a bunch of documents is that kind of where you started and then you yeah and and that again
[2849.64 --> 2856.30]  was partly an experimentation and and i still have people once a week warn me that mongodb is gonna
[2856.30 --> 2863.84]  start vomiting in my face at some point but um but so far it's been great uh you know it was something
[2863.84 --> 2871.42]  that again during while i was at censia i basically only worked on client-side projects for for three
[2871.42 --> 2879.80]  years or so and i and i saw sort of these uh you know no sequel or document-based databases were
[2879.80 --> 2885.68]  becoming really popular around then um i mean that's a bit of a miss it was obviously i was probably late
[2885.68 --> 2892.42]  to the bandwagon but um but i i saw a lot of that while i was there without actually using one and i just
[2892.42 --> 2897.60]  you know after you when you spend so much time with javascript and working with objects the idea
[2897.60 --> 2904.34]  of using objects to query your database or to be able to inject objects into places within your
[2904.34 --> 2911.92]  database is just sort of extremely appealing and that was sort of the initial uh impetus and i did i
[2911.92 --> 2919.80]  started with rethink just because i had heard sort of various war stories of of mongo and uh rethink
[2919.80 --> 2925.74]  seems to be sort of one of the cooler new kids on the block but you know a big reason i went with
[2925.74 --> 2933.94]  mongo was just because of mongoose in the node ecosystem it's it's just i to me at least far
[2933.94 --> 2942.72]  sort of further ahead than any other sort of orm odb type thing that's interesting so the the mongoose
[2942.72 --> 2947.70]  library itself was the kind of the deciding factor there for you yeah definitely one of the bigger
[2947.70 --> 2956.50]  uh decision makers you know just the built-in validation the uh relationship management it
[2956.50 --> 2962.46]  was all just super super straightforward i guess there's some there's some symmetry there with
[2962.46 --> 2967.82]  you know your desire for uh clean user interfaces and thinking about that user experience if you find
[2967.82 --> 2973.64]  an api that you really love it makes sense it you know it's it's a huge factor and that's another
[2973.64 --> 2980.64]  thing which i put a lot of sort of focus on within buckets and and you know it's it's i do say like
[2980.64 --> 2986.96]  it's it's my project and so i i do stuff in it that um not everybody's gonna like it's how i like to
[2986.96 --> 2995.22]  program certain things but in reality again this is highly contentious um buckets is like 90 percent
[2995.22 --> 3002.54]  like if you look at the stats on github it's like 90 percent coffee script um like pretty much the
[3002.54 --> 3008.30]  entirety of buckets whether it's the front end user interface or it's the server side uh models and
[3008.30 --> 3014.02]  database connections uh is all written in coffee script well you're not going to have any arguments
[3014.02 --> 3020.32]  for me on that one but i think most people would you know it's it's one of those contentious things but
[3020.32 --> 3026.22]  it yes i just thought in the beginning especially in the beginning like you know this is not something
[3026.22 --> 3030.66]  that people are just going to jump in and i'm going to start getting 20 pull requests a week
[3030.66 --> 3036.48]  no matter what i write it in right and so i might as well write it in the thing that keeps me motivated
[3036.48 --> 3044.18]  and keeps you know makes it the lowest sort of um cognitive overhead for me to jump in and fix a bug
[3044.18 --> 3048.22]  interesting do you think that that has paid off as an early decision
[3048.22 --> 3055.12]  um i don't know it's hard to say like i you know there's always that sort of worry in the back of my
[3055.12 --> 3062.32]  mind that i'd have you know 10x the contributors if it was in raw javascript but again it's it's that
[3062.32 --> 3070.02]  like i like how the app looks you know like in terms of the source code like and the dependency
[3070.02 --> 3077.56]  management and the modules you know it's it's um it's it's somewhat artificial which i think is the
[3077.56 --> 3080.72]  problem but i think people are getting more and more comfortable with that you know with
[3080.72 --> 3088.62]  grunt and gulp and browserify and all these things people are starting to see how uh javascript can be
[3088.62 --> 3097.46]  sort of crafted in kind of a less gross kind of loosey-goosey way right uh and and uh i'm gonna
[3097.46 --> 3102.58]  bring it old school now but it's like javascript for me at least especially with action script is
[3102.58 --> 3110.70]  starting to look like sort of action script three of like you know eight years ago or so where you're
[3110.70 --> 3115.44]  you know you're importing classes or you're requiring classes you're extending things you know
[3115.44 --> 3123.90]  it's it's um it's a whole different space sure is uh i think one thing we're gonna link out to
[3123.90 --> 3129.08]  that may not uh quite fit into this call but you've sort of talked in and around it but uh
[3129.08 --> 3134.70]  is your vision document which i think is pretty neat to have on um on your repo it's just talking
[3134.70 --> 3138.62]  about the general philosophies and where you're heading for the future so i think is some of that
[3138.62 --> 3143.78]  replicated back in assembly to to sort of because it's it's back in that space where do you send
[3143.78 --> 3148.36]  people to github to the repo to a readme or a markdown file or do you send them to assembly
[3148.36 --> 3157.56]  like where do they i am at to kind of get interested yeah and so so far like assembly has a sort of main
[3157.56 --> 3164.24]  descriptor for the project and then it's just sort of replaced that on the main page with a timeline
[3164.24 --> 3170.68]  for the project but um but in general like they've always been sort of assembly has always been
[3170.68 --> 3177.08]  sort of more geared around the flow of things and and the bounties and and things like that like it's
[3177.08 --> 3182.34]  not like base camp where you have those uh uh i forget what they called them but they were write
[3182.34 --> 3187.14]  board like 10 years ago you know these like permanent like we're going to edit copy together
[3187.14 --> 3195.88]  kind of uh mini application um and so i just wanted uh sort of a permanent place to store copy
[3195.88 --> 3202.28]  uh and just decided to throw it in there with github i do wish i was better about keeping these things
[3202.28 --> 3207.16]  in sync you know it's like it's like keeping your avatars in sync across different profiles like i just
[3207.16 --> 3214.24]  find myself i'm just always tweaking copy for buckets like whether it's the their the twitter uh bio
[3214.24 --> 3221.84]  or it's the github home page readme or it's the assembly front page you know um i don't have like
[3221.84 --> 3229.28]  one central thing and then i you know like a press app or something well that that leads into probably
[3229.28 --> 3234.04]  the first of our closing questions which is you know sort of a call to arm so you sort of talked
[3234.04 --> 3240.26]  about your own uh keeping things in sync issues but like if someone's listening to this they love node
[3240.26 --> 3245.58]  they love javascript they are they're getting into node for you know node or just in javascript in
[3245.58 --> 3250.78]  general and they're a front-end designer hacker and they want to sort of jump in or that that
[3250.78 --> 3256.90]  back-end person that's listening to the show where do they go what what um you know in what ways can
[3256.90 --> 3262.30]  the community step in and start helping you make this real if they want to i think the clearest path
[3262.30 --> 3267.90]  is is definitely assembly i think that's you know that's what it's there for if you go to
[3267.90 --> 3275.40]  assembly.com slash buckets you get a lot of great basic info uh just sign up it takes like a minute
[3275.40 --> 3280.60]  and then and then you can just browse the the bounties and like i said there's like a hundred
[3280.60 --> 3287.54]  of them you can um if if literally none of them look interesting to you just tell me what you are
[3287.54 --> 3291.96]  interested in doing and i'll see if there's something there i tell a lot of people you know
[3291.96 --> 3297.62]  it's not just about it's it's like not github it's not just about development and it's also not just
[3297.62 --> 3303.98]  about design i think like i would love to eventually maybe it's a little soon for this but like
[3303.98 --> 3311.06]  eventually just have sort of an advisory panel of people who make websites for other people and just
[3311.06 --> 3317.02]  what do they want out of their systems like what did drupal users really wish was part of it or or what
[3317.02 --> 3322.38]  is somebody's pain points with expression engine those types of things you know however minor even
[3322.38 --> 3328.48]  just you know recommendations or um just feature requests are are totally appreciated
[3328.48 --> 3335.92]  and our our famous question jared which is uh which is who is your programming hero some people come on
[3335.92 --> 3340.42]  the show they mention a few some mention one you know the it's it's open-ended who's your who's your
[3340.42 --> 3348.38]  hero so i've been trying to think about this for the past hour um i i i'm gonna go with uh
[3348.38 --> 3357.16]  37 signals is a generally a huge source of inspiration uh a lot of their inspiration is
[3357.16 --> 3364.16]  what goes into buckets it's the idea that we could do something small profitable that's not vc backed
[3364.16 --> 3372.18]  that is um you know profitable enough to sustain the people that work on it and not necessarily start
[3372.18 --> 3378.94]  bringing in 50 million a year but you know that sort of mentality and the mentality that that it can be
[3378.94 --> 3385.28]  a small team it can be um you know 10 people that make this thing that that hundreds of thousands of
[3385.28 --> 3394.08]  people use um it's definitely a big inspiration wow well dave i i know that uh you know we've been
[3394.08 --> 3399.70]  we've had you on the show like i said once before back at episode 30 uh that's at uh that's on the site
[3399.70 --> 3403.90]  you can you can go back and listen to him talk about central with wind back in the day but you
[3403.90 --> 3407.54]  know we're a fan of what you're doing however we can support we obviously want to support you in
[3407.54 --> 3412.24]  in that endeavor and anybody who's listened to the show follow follow dave and figure out what he's
[3412.24 --> 3417.12]  doing with buckets and and uh see how you can plug in we got uh a couple sponsors we want to give
[3417.12 --> 3420.98]  some thanks to for the show because that's how we make this show possible along with our awesome
[3420.98 --> 3426.96]  members who make it possible as well uh code ship digital ocean and top tile super awesome partners
[3426.96 --> 3432.50]  those guys all three of those sponsors pretty much help keep the change log alive so if you
[3432.50 --> 3437.56]  don't use code ship you're not hosted on digital ocean and you don't hire developers or you're not an
[3437.56 --> 3443.04]  elite engineer through top tile we're just we're just showing big old emoji sad faces around here so
[3443.04 --> 3450.68]  um next next week we do have all things pearl with codis poe curtis uh curtis right that's what i said
[3450.68 --> 3455.32]  curtis yep that's right yeah curtis we're excited about that because this is i think this might be our
[3455.32 --> 3461.52]  first eric of having pearl on the show we probably mentioned it but never a project or someone that
[3461.52 --> 3467.88]  can come and speak to pearl the language um i'm gonna get caught up yeah we're excited so that's
[3467.88 --> 3473.10]  next friday we'll record but uh that's what's coming up next so that has been it for this show
[3473.10 --> 3479.14]  everybody on here let's say goodbye bye all right thank you guys so much bye
[3479.14 --> 3498.70]  a little bit of a unusual ending there on my side sorry about that but uh
[3498.70 --> 3502.42]  codis you said okay i literally couldn't name a designer
[3502.42 --> 3509.76]  i was gonna tell you just name a couple but i could swear i said curtis not codis well you know
[3509.76 --> 3514.84]  the audio the audio won't lie aaron i'll tell you i could have heard it wrong but i thought you said
[3514.84 --> 3520.28]  codis poe uh no maybe maybe i did i don't know listen to it back
[3520.28 --> 3530.94]  next week we do have all things pearl with codis poe curtis uh curtis right that's what i said
[3530.94 --> 3532.68]  curtis yep that's right
[3532.68 --> 3532.74]  yep that's right
[3532.74 --> 3532.98]  yep that's right
[3532.98 --> 3533.18]  yep that's right
[3533.18 --> 3533.22]  yep that's right
[3533.22 --> 3544.22]  yep that's right
[3544.22 --> 3558.42]  yep that's right
