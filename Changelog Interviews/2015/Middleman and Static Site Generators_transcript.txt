[0.00 --> 17.24]  welcome back everyone this is the changelog and i'm your host adam stekowiak this is episode 169
[17.24 --> 22.56]  and on today's show we're talking to thomas reynolds the maker of middleman we wanted
[22.56 --> 28.06]  to have this conversation for quite a while we're rubyists at our core here at the changelog and
[28.06 --> 33.56]  we use middleman every single week to ship changelog weekly we built that in middleman
[33.56 --> 40.00]  we're also building another site for beyond code in middleman check that out beyondcode.tv
[40.00 --> 45.94]  that's our brief interview series we shoot at conferences after parties but ruby's at our
[45.94 --> 51.30]  core here here at the changelog we love middleman great conversation today with thomas we have three
[51.30 --> 59.34]  awesome sponsors code ship top towel and digital ocean our first sponsor for the show is code ship
[59.34 --> 64.98]  they've launched a brand new feature called organizations and i've talked to several teams
[64.98 --> 70.72]  who love this new feature because now you can create teams set permissions for specific team members
[70.72 --> 77.22]  and improve collaboration in your continuous delivery workflows you can maintain centralized control
[77.22 --> 84.12]  of your organization's projects and teams with this brand new feature save 20 off any premium plan
[84.12 --> 91.14]  you choose for three months by using the code the changelog podcast again that code is the changelog podcast
[91.14 --> 98.20]  you'll save 20 off any premium plan you choose for three months head to code ship.com slash the changelog to
[98.20 --> 100.34]  get started and now on to the show
[100.34 --> 112.28]  all right we're back we got a great show lineup for you today we have been wanting to talk about
[112.28 --> 119.52]  middleman forever and when i say forever it's like the sandlot forever uh i've been using middleman for
[119.52 --> 123.62]  a long time jared how about you have you been using middleman for a while actually my first time with
[123.62 --> 127.98]  middleman was when you brought me in on changelog weekly okay so that was which was
[127.98 --> 134.02]  you know maybe six or seven months ago well luckily it was a lot lately yeah so we got thomas
[134.02 --> 138.50]  reynolds on the line here he is the creator of middleman thomas hey what's up hey how you doing
[138.50 --> 143.40]  all so you're the technical director at instrument it's an independent digital creative agency is that
[143.40 --> 148.00]  your thing or is that somebody else's thing that's someone else's thing um we're a company of about
[148.00 --> 153.86]  100 110 people in portland oregon okay um we're all centrally located no remote workers and
[153.86 --> 161.00]  we just do really high-end digital marketing nice man also the creator of middleman and a foodie
[161.00 --> 165.68]  book nerd writer and obviously a rubius because you couldn't be the creator of middleman without
[165.68 --> 170.34]  being a rubius first right yeah it doesn't happen accidentally so for those listening middleman
[170.34 --> 179.80]  is a ruby gem it's a static site generator uh and how long has it been around thomas uh in its
[179.80 --> 185.24]  current stable form it's been out for three years um i just checked on github uh time since first
[185.24 --> 190.96]  commit and the repo is just a little over seven years i was gonna say it feels like so long ancient
[190.96 --> 195.98]  ancient open source roots at this point definitely if you get past five it's it's getting into the
[195.98 --> 201.18]  it's like the cart or suddenly a classic yeah no it's like marriage like it's just i wake up every
[201.18 --> 205.42]  day and i do it and i keep doing it every single day and it'll always probably be here with me there you
[205.42 --> 210.68]  yeah so before we kick off the full-on show and dive deep into middleman let's figure out who you
[210.68 --> 214.68]  are a bit kind of give us a bit about who you are you already mentioned instrument and the things you
[214.68 --> 218.86]  do there so kind of give us a bit about your your history and who you are as a software developer
[218.86 --> 227.20]  yeah so um i've been in software development and mostly agency stuff uh for about 16 years now i got
[227.20 --> 232.44]  started really young um kind of grew up with the internet and was able to you know be a kid in high
[232.44 --> 237.82]  school and actually contribute uh to open source and also you know to just fan sites and stuff so
[237.82 --> 244.10]  i got my start programming uh making levels for tie fighter the flight sim video game for the pc way
[244.10 --> 249.96]  back in the day and then i moved from there to like fan sites for that and uh eventually it's like oh hey
[249.96 --> 255.58]  i need to learn this sequel thing hey i need to learn this html whatever three or whatever it was back
[255.58 --> 261.70]  then um and so yeah i got my starts like uh just doing super nerdy stuff on the internet um did that
[261.70 --> 266.36]  for a couple years and i went off to school for a cs degree and then realized i was writing less code
[266.36 --> 272.04]  at school than i had been in my own free time uh so i kind of dropped out switched to like a liberal
[272.04 --> 276.92]  uh more liberal degree and just you know with a lot of reading which was a lot more fun for me and then
[276.92 --> 281.00]  uh put all my passion back into software development on like the open source side
[281.00 --> 289.66]  um since becoming a full-grown adult uh i've been doing agency stuff now oh boy probably like
[289.66 --> 295.18]  eight to ten years uh pretty much non-stop so i've never really done any product stuff i've never
[295.18 --> 301.96]  really done any startup stuff uh i just kind of like the the heavy churn and like um frequent new
[301.96 --> 307.90]  kinds of ideas that you have to do like in an agency lifestyle you ever got the startup itch
[307.90 --> 315.66]  uh no not really i moved to portland to get away from that stuff so i'm happy i'm happy just uh
[315.66 --> 320.66]  i don't know i like doing new things i probably get a little bit bored other than middleman i i tend
[320.66 --> 327.80]  to like discard side projects so um yeah but uh yeah slightly off topic since you're living in
[327.80 --> 333.50]  portland um i'm a huge fan of portlandia i absolutely love that show are you do you watch
[333.50 --> 338.10]  the show since you sort of live it every day or do you just skip it i don't really watch it um
[338.10 --> 343.46]  but are you offended by it people yeah that's like exactly the question people have uh actually no i
[343.46 --> 348.30]  think it's um the way i try to phrase this to people is a lot of people would see those
[348.30 --> 352.20]  caricatures as an insult and we take them as a point of pride and that's just because we're weird
[352.20 --> 356.94]  like if we could get more people on weird bikes that would be perfectly cool for us
[356.94 --> 362.72]  that's why a lot of us moved here love portlandia man yeah it's a great show and they're well-meaning
[362.72 --> 367.06]  and like i know carrie grew up you know somewhere here in the northwest so right i'm pretty sure she's
[367.06 --> 371.08]  well-meaning about it all too i think it's the first time jared on the show i heard somebody say
[371.08 --> 379.32]  they quit their css css degree to go and code more yeah yeah so i went to arizona state which is
[379.32 --> 384.70]  not necessarily known for its computer science degree um but it was cheap uh they launched a
[384.70 --> 389.22]  rocket once to mars and it deactivated as soon as it landed so that pretty much tells you what you
[389.22 --> 395.58]  need to know about the program there um so i think java sun or i guess it was still sun then
[395.58 --> 399.94]  poured a ton of money into the school so i wrote two years of java which was not terribly exciting
[399.94 --> 406.56]  uh projects and given your turn on i'm sorry jared go ahead i was gonna say what what turned you on
[406.56 --> 414.22]  originally to the to the open source world that's a good question um trying to think back it was
[414.22 --> 421.48]  probably actually i just honestly don't remember um so as soon as i got into like agency stuff after
[421.48 --> 426.94]  college it was a lot of i did a lot of php um which is always kind of like a vaguely open source
[426.94 --> 432.76]  community i don't know the actual structure but they were pretty open um and there was pretty uh a
[432.76 --> 439.06]  large amount of community involvement like as that language grew so i did a lot of that and
[439.06 --> 444.52]  you know this is all pre-github so open source was like this thing that took place on mailing lists
[444.52 --> 449.40]  and maybe someone hosted a site you could download like a tarball or something and install it but
[449.40 --> 453.24]  there wasn't it didn't feel like there was as big of a community as there is now
[453.24 --> 458.58]  um there were irc channels that we could communicate but it was probably something php based
[458.58 --> 463.26]  you know one of the uh database wrappers or something like that i probably contributed stuff
[463.26 --> 470.26]  too early so yeah basically did a lot of php for years and years uh discovered ruby right as you know
[470.26 --> 475.88]  the great rails explosion happened um fell in love with it especially since php was basically pearl at
[475.88 --> 481.88]  the time uh got to use some things from cs that i hadn't used in a little while like objects and
[481.88 --> 485.72]  you know classes and all the you know core object oriented stuff that's in ruby
[485.72 --> 492.70]  and yeah it's pretty much it i started using ruby uh rake specifically um for a lot of tooling stuff
[492.70 --> 499.88]  for my front front end work so you know every time you know i was a okay agency but we did mostly
[499.88 --> 505.70]  email templates and it got to the point where it was like four to six email templates a day was the job
[505.70 --> 510.68]  and um most of that stuff can just be automated you know like mail chimp will automate all that stuff
[510.68 --> 515.56]  right now you just kind of upload a couple things to them right so started using rake and started uh
[515.56 --> 523.04]  you know building out uh just little helpers little tooling bits for myself interesting it might make
[523.04 --> 528.56]  uh some sense to rewind a little bit though i given your agency experience i do have a couple
[528.56 --> 535.34]  thoughts here mark for that getting closer to that subject but um might make sense since the you know
[535.34 --> 540.34]  in terms of the git history i think you said it was seven years git history you've got for middleman
[540.34 --> 545.54]  so we're definitely talking about quite a bit of space and you know in time in there in terms of
[545.54 --> 551.68]  the space that middleman occupies which is the static site generator space there's been lots out there
[551.68 --> 559.02]  in every kind of language you could think of um jared and i we both have ruby roots so we we kind of go
[559.02 --> 565.42]  back with with all of that but at the same time i think a lot of the at least what i can tell from my
[565.42 --> 569.76]  perspective is a lot of the static site generators came from the ruby world and sort of came you know
[569.76 --> 574.96]  spread out to the languages so what do you know of the history of of these generators and and where
[574.96 --> 581.08]  did middleman come from and what problems was it solving when it first uh became for you totally
[581.08 --> 585.56]  um so yeah kind of when i was like doing that email template work you know the other thing you
[585.56 --> 591.38]  wanted to automate the same time was html and css and um this is right about the time that hamel had
[591.38 --> 596.22]  come out and so that just took a lot of the work out of you know doing just incredible amounts of
[596.22 --> 601.26]  tables and all the stuff we had to do for emails back in the day uh so i started looking around for
[601.26 --> 607.36]  some tools at the time i think um nanoc existed yeah static matthic existed i'm not entirely sure
[607.36 --> 613.82]  if jekyll existed publicly yet but um it was all about that time looking back and jekyll looks like
[613.82 --> 621.20]  their initial launch was like end of 2008 it was probably out there yeah it was probably
[621.20 --> 628.42]  being talked about on the blog or sphere or whatever we called it right um yeah so i uh
[628.42 --> 633.78]  liked static matic personally uh it was already open source you could already you know check out
[633.78 --> 638.82]  all the code and it was pretty easy to get code back upstream uh with that team so i started using
[638.82 --> 644.82]  static matic for myself and you know got into the forums and um kind of got involved with that community
[644.82 --> 651.54]  uh and basically slowly over time i committed a larger and larger share of the pull requests uh
[651.54 --> 655.84]  until the point where the original creator was you know didn't have the time for it as much anymore
[655.84 --> 662.54]  so we basically you know the 1.0 of middleman is uh somewhat of a fork of static matic so we just
[662.54 --> 668.14]  kind of renamed it moved the repos and uh moved a lot of the community stuff over into my name i did not
[668.14 --> 672.86]  know that part that it was sort of a fork because i feel like static matic is where it all began
[672.86 --> 678.70]  and it sounds like that's what you said too is that right yeah at least for me i mean i i know
[678.70 --> 684.90]  natic existed and it seemed uh at a glance to be more complicated than i wanted to get into
[684.90 --> 689.02]  i never really went all the way down that road so i don't i can't actually say if that's true but
[689.02 --> 695.00]  static matic kind of uh matched up a little bit more to how i wanted to use the tool adam i don't know
[695.00 --> 701.38]  if you remember a little bit of my roots was in the pearl community in college and uh my first
[701.38 --> 707.84]  kind of exposure to blogging at all was because basically my professor told us we had to blog
[707.84 --> 712.62]  and they gave us this pearl thing i think it was called like blog some something like that
[712.62 --> 720.24]  and it was a static site generator um in pearl this is like 2005 2006 and i thought it was super lame
[720.24 --> 727.10]  uh and then i found wordpress and i was like why would i want to have static sites when i can have
[727.10 --> 733.98]  dynamic like changing database driven wordpress you know sites uh and then and then there were
[733.98 --> 737.04]  there's obviously reasons why you would want to have a static site we can get into all that but
[737.04 --> 741.58]  it was kind of funny because once jekyll dropped in these in static matic i started seeing this like
[741.58 --> 747.76]  rise of these static site generators i was like what is wrong with these people like why are we
[747.76 --> 753.38]  like wordpress and these things are cool like static files like that's i had a similar thought when i
[753.38 --> 758.04]  i don't think i've ever shared this story publicly but when win and i first so win and i started this
[758.04 --> 764.12]  show together way back in 2009 and the first time i met win was at a ruby meet up here in houston
[764.12 --> 770.60]  and he was doing a presentation on something new they had done and they had just rebuilt the squeegee
[770.60 --> 776.88]  website which was win's uh original consultancy before he uh sort of went independent and then
[776.88 --> 782.38]  ultimately went to github um he loved static matic and he was given a presentation on it and i was like
[782.38 --> 786.98]  same thing why and you know and i was a wordpress guy at the time like i was using that stuff
[786.98 --> 793.24]  why would i you know you know learn and write ruby only to create stack sites i don't get it
[793.24 --> 801.54]  and but it was a big big thing then yeah i think uh you know i like i said i got into it to make html
[801.54 --> 805.98]  email but it was there was no option other than static right just throw this thing over the wire and
[805.98 --> 810.26]  it's got all be um self-contained right but yeah i think it's kind of really interesting over the years
[810.26 --> 815.12]  like and as middleman has gained popularity there's something happened and i don't know if it was
[815.12 --> 820.98]  you know we got tired of the complexity we got tired of like the stack churn or the security issues
[820.98 --> 826.06]  around like full like back-end apps but there's definitely now you know you see all these blog posts
[826.06 --> 830.50]  coming around that are just like there's no reason not to do static i mean almost everything
[830.50 --> 835.16]  you can accomplish other than like a form and maybe e-commerce you know you can do statically
[835.16 --> 839.88]  and then you never have to worry about you know any security implications yeah i remember my tune
[839.88 --> 844.62]  started to change when i would consistently see different wordpress sites get taken down by i
[844.62 --> 849.40]  think it was dig back then yes um you know the dig effect or something like that and it would just
[849.40 --> 855.32]  crush under a little bit of load and that's when i started saying okay you know static html files
[855.32 --> 861.02]  makes a lot of sense in that regard yeah also i mean just because i come from an agency background
[861.02 --> 866.42]  before you know like the modern age um that's what we deliver that's what our contracts say we
[866.42 --> 871.36]  deliver we deliver like the static packet of a website and if you want to throw it into a rails app
[871.36 --> 876.96]  or if you want to just like drag ftp it to some you know go daddy server that's up to you um so it's also
[876.96 --> 882.50]  a lot of that kind of work is self-contained in that way that's that's kind of leading into i guess the
[882.50 --> 889.52]  slightly a good segue into the next step which is given your uh agency experience now at instrument
[889.52 --> 893.94]  i gotta imagine that a lot of what you've done with middleman over the years with the contributors
[893.94 --> 899.34]  and the contribute uh your core team and contributors who've who've helped get middleman to where it is
[899.34 --> 907.18]  now today i gotta imagine a lot of that's playing back into your full time uh a little bit um i pretty
[907.18 --> 913.74]  much do nothing but javascript on my day job um i manage a team of people as well uh but you know for
[913.74 --> 917.70]  the most part i've tried to i had tried to keep the two separate you know i didn't want to like
[917.70 --> 923.40]  you know i made this thing therefore we should use it especially before it got enough popularity
[923.40 --> 927.48]  to kind of justify that kind of stuff um so i've always just kind of left it on the side if people
[927.48 --> 932.24]  ask about it in like slack or something i'll be like oh yeah i know how that thing works um but
[932.24 --> 935.94]  yeah maybe in the last year we've actually been hiring people and they've come in the door knowing
[935.94 --> 940.40]  it so now we do tend to use it on a lot more projects and i am a little more hands-on with like
[940.40 --> 946.42]  actually adding features or you know fixing specific bugs from people in-house so you said the original
[946.42 --> 952.52]  crux that was sort of originally somewhat of a fork of static matic the problems initially were
[952.52 --> 959.98]  you know html email driven is is that when it was that was obviously middleman version one how has
[959.98 --> 965.14]  middleman changed over the years in terms of the problems it's been solving and and the evolving
[965.14 --> 971.16]  problem it's been solving yeah so i just looked um you know one and two were these kind of small
[971.16 --> 975.42]  releases that uh i don't know how many people were actually using it probably people who moved on
[975.42 --> 980.46]  from static matic um there's also a period of time there where jekyll went completely unmaintained
[980.46 --> 984.98]  other than like the octopress work that was happening uh so i think we got a lot of people
[984.98 --> 990.68]  from there but i just looked it up and we've been on the stable current stable branch since 2012
[990.68 --> 998.96]  um i think that's when uh it really kind of took off and that's when i was also doing rail stuff on
[998.96 --> 1005.00]  the side and i wanted to align um the two kind of workflows so rather than just being like it's a
[1005.00 --> 1009.08]  whole separate tool i wanted it to be like conceptually you could come directly over from
[1009.08 --> 1014.06]  rails and then you know you can just make a static site or you can put a static site in your rails if
[1014.06 --> 1019.20]  you want to like keep you know one piece separate or a little more secure uh so yeah i think version
[1019.20 --> 1026.34]  three was like the big leap forward uh built it on top of um some of the merb stuff which eventually
[1026.34 --> 1031.54]  became into rails but i used a lot of their tooling uh we still use internally for a lot of our code
[1031.54 --> 1039.14]  uh the padrino library yeah that's like a sinatra alike for um rails and then whenever we have like
[1039.14 --> 1043.90]  a discussion on api we try to go check out the rails api and make sure we're keeping things as
[1043.90 --> 1048.32]  similar as possible so we can bring people over from the rest of the ruby community do you mean things
[1048.32 --> 1053.18]  like uh rendering parcels uh different helpers that are available in rails that people sort of
[1053.18 --> 1059.12]  so people can essentially copy and paste views but to a degree potentially back into a rails app
[1059.12 --> 1064.98]  yeah i mean we still have like a huge reliance on yaml for like configuration we have um all the
[1064.98 --> 1070.02]  helpers like you said like your normal link helpers your localization helpers we bring over directly
[1070.02 --> 1076.84]  um most of the we support i think every templating language that could possibly exist in some fashion
[1076.84 --> 1081.88]  so definitely all the ruby stuff most of the javascript stuff you know pretty much any language that can be
[1081.88 --> 1088.80]  you know shelled out to and come back uh we support that very cool so there i mean there there have been
[1088.80 --> 1094.34]  tons of these tools over the years uh we've mentioned a few here i think there was one called
[1094.34 --> 1101.56]  stasis uh there's just there's been a lot of them uh webby was one i think i used webby back in the day
[1101.56 --> 1108.32]  all ruby tools and yet middleman what's that serve serve i don't know that one it's it's not being
[1108.32 --> 1112.74]  maintained now but it was one that was it was one that john long had mentioned we talked about that
[1112.74 --> 1120.20]  on the octopress show with the yeah with brandon mathis very cool so middleman has stood out from
[1120.20 --> 1125.24]  the crowd it's it's kind of been more successful it's gotten more uh it's obviously been sustained
[1125.24 --> 1131.24]  longer but it has more excitement around it more people using it uh big players like uh thought bot and
[1131.24 --> 1137.08]  um there's a couple more on your website that i can't think of off the top of my head mailchimp
[1137.08 --> 1143.14]  thank you so can you attribute that to anything in particular was it you know pure luck or is there
[1143.14 --> 1150.48]  something about middleman that stands out from the crowd um yeah i actually think uh i have a
[1150.48 --> 1156.38]  kind of different opinion about open source from the rest or at least the modern kind of javascript
[1156.38 --> 1160.92]  crowd which i don't think things should be throwaway i think there's a responsibility attached
[1160.92 --> 1166.48]  to saying you know i want you to spend your days and hopefully not your nights coding with my thing
[1166.48 --> 1171.82]  and that you know it kind of sucks when you have to maintain that for years and years and years but
[1171.82 --> 1176.54]  um that's like the bargain you're making by publicly saying hey go use my thing i put it on github
[1176.54 --> 1182.44]  uh so i think what i contribute most of middleman's success to is basically uh stability and like
[1182.44 --> 1190.44]  respect for people's time so you know we've been at 3.0 stable uh for a little over three years now
[1190.44 --> 1195.28]  the apis are pretty much the same if you can make a site like a year ago it's going to be exactly the
[1195.28 --> 1200.04]  same now um things aren't going to change under your feet and you're just going to have like a stable
[1200.04 --> 1205.12]  like platform it's not that complicated the things we do are pretty self-contained so we just do those
[1205.12 --> 1209.44]  things well and get out of your way as quickly as possible and we've done it for three years so
[1209.44 --> 1213.76]  you know there wasn't like oh i gotta switch i mean there will be soon but there wasn't like
[1213.76 --> 1217.92]  i gotta switch to the rails for rewrite like what am i going to do with myself right um
[1217.92 --> 1222.86]  i'm glad you said that because that's actually an issue i've had with the static generators over
[1222.86 --> 1228.32]  the years is that i would build something let's say a one-off simple static site for somebody and
[1228.32 --> 1231.92]  then have to go back and like make an update or something like that to it and then you know
[1231.92 --> 1235.98]  building it locally or something like that becomes an issue because the latest version breaks things
[1235.98 --> 1239.98]  and then i gotta spend another hour or so trying to fix things or link to helpers or just weird
[1239.98 --> 1245.50]  things that have changed in the apis of like the little things and the stability to me was a big
[1245.50 --> 1251.36]  thing for middleman because i'd gone through static matic and several others and then finally you know
[1251.36 --> 1256.76]  i'm using something like middleman you know almost every time i do something static unless it's actually
[1256.76 --> 1262.64]  really static um and and never having to deal with those those issues where i don't touch it for six
[1262.64 --> 1266.92]  months and it's still the same you know i can just run it yeah we want to fight that whole hype churn
[1266.92 --> 1274.30]  cycle yeah like there's no reason for that there are so few uh really revolutionary ideas and you
[1274.30 --> 1278.58]  know what i like maybe take the ember community stance on it like if they're really revolutionary
[1278.58 --> 1283.48]  we'll fold it in and we'll do it stably slowly over time and we'll document it well but i'm not going
[1283.48 --> 1288.16]  to jump on the hype train you know and break your site from a year ago it's great we have tools like
[1288.16 --> 1293.50]  a bundler now that can protect us from a lot of that kind of you know come back to a thing six
[1293.50 --> 1297.92]  months later and it's not working anymore um but you know you should also be able to do bundle update
[1297.92 --> 1306.10]  and not have your entire world explode i like that so you have this commitment to reliability and
[1306.10 --> 1312.74]  stability and you've been doing that over the years um that's pretty rare in open source um very
[1312.74 --> 1319.46]  and so i wonder like what why like what do you get out of it what is it i don't know what i get out
[1319.46 --> 1327.62]  of it okay inertia inertia um i like doing it i um i don't know i so we have a couple community
[1327.62 --> 1334.74]  like outlets from middleman so there's like public chat channels there's a public forum um
[1334.74 --> 1340.68]  what else is there uh i don't remember there was an email group at some point but basically i don't go
[1340.68 --> 1347.84]  there like i set up these systems for the community to you know self-help and then i only respond on
[1347.84 --> 1353.40]  github pull requests or you know twitter harassment um and i think that's also another thing like if
[1353.40 --> 1357.50]  you're just in the trenches there like you know managing the forum day in and day out i think it'll
[1357.50 --> 1362.88]  and you know you get to see people telling you that you kind of ruined their weekend because you
[1362.88 --> 1367.36]  wrote some bad bug um i think it maybe drags on you a little bit more but i try to keep myself
[1367.36 --> 1371.24]  completely separate from that and uh people in the community have stepped up and been those kind
[1371.24 --> 1376.76]  of like community leaders and it all works out for everyone yeah look at the forum now it's it's uh
[1376.76 --> 1381.82]  it's pretty active i mean a lot of people in there i mean i'm not uh diving into a lot of these
[1381.82 --> 1388.04]  notes here but i'm just scrolling this uh this endless scroll um a lot of stuff a lot of stuff
[1388.04 --> 1395.20]  happen yeah a lot of a lot of that is just holes in documentation where um uh all for documentation
[1395.20 --> 1401.36]  is on github it's all community um contributed to so i did like a bunch of the big chunks of initial
[1401.36 --> 1405.34]  writing but it's all kind of maintained itself uh through people you know not quite being able to
[1405.34 --> 1409.82]  parse a sentence or you know i'm not making the right point that they're trying to get to or i you
[1409.82 --> 1413.46]  know put something on the wrong page but uh you're never going to be able to document everything
[1413.46 --> 1420.26]  uh again kind of like the ember model i went with like a plain text tutorial style for my documentation
[1420.26 --> 1426.72]  as opposed to api docs which are a little more uh provide better coverage but uh are kind of harder
[1426.72 --> 1431.14]  to understand if you don't know what's going on inside the system um and so yeah so it just leaves
[1431.14 --> 1435.64]  like narratively like a feature missing just because i couldn't fit it onto any of the pages and i think
[1435.64 --> 1440.20]  the forum is really good about that uh just being like hey there's this thing why isn't it documented
[1440.20 --> 1446.54]  well like four people use it but you know here it is on the forums for you so if a doc needs updated
[1446.54 --> 1453.32]  someone could go to github fork it and let's say like a misspelling or you know something to change
[1453.32 --> 1459.00]  someone from the community uh whether they're in the core team or not could step in and help out
[1459.00 --> 1464.78]  as needed and there's uh there's a pull request button at the bottom of every page on the documentation
[1464.78 --> 1470.06]  site so we make that as easy as possible so we talked a little bit about
[1470.06 --> 1475.26]  you know its makeup can can we talk a little bit about let's say like a file structure you said
[1475.26 --> 1480.16]  it's a lot like the rails view layer was that on purpose did you look at the rails view layer and
[1480.16 --> 1484.64]  say this is how it should be this is how a middleman site should be structured and how it should be laid
[1484.64 --> 1490.82]  out is it really meant to be a lot of plug and play in between that and rails kind of i don't think we
[1490.82 --> 1497.48]  follow the file layout of rails because they've got a pretty deep named structure uh the way our
[1497.48 --> 1501.94]  philosophy works is you have a source directory and conceptually you look at everything in there
[1501.94 --> 1505.94]  and that's what you get on the way out you can do some meta program you can do all these fancy
[1505.94 --> 1511.24]  configuration options but we try to do a one-to-one from that folder to your build folder so if i have
[1511.24 --> 1517.74]  index.html.erb i'm going to get an index.html out uh so for most people's sites you should just you
[1517.74 --> 1521.86]  shouldn't have like all this magic happening you should just be able to say you know it's a pipeline
[1521.86 --> 1528.54]  you come in as sash you come out as css so it matches the structure of source matches but however
[1528.54 --> 1532.74]  you want to structure your code so if you want a fonts directory have at it if you want to put it
[1532.74 --> 1538.04]  inside your css that's fine with us too and the reason why i ask is because i i think what and i
[1538.04 --> 1542.86]  could be wrong here but it's at least happened to me several times is that you know i'm a rubyist
[1542.86 --> 1547.48]  only to a certain point or i'm a back-end developer only to a certain point that i don't do it because
[1547.48 --> 1552.76]  there's people who are better than it than me at it and i may want to go buck wild on the view
[1552.76 --> 1558.00]  and build out a site but i don't have you know all the routes in place and all these different things
[1558.00 --> 1562.24]  that sort of stay in your way when you work in a rails team and it felt always a lot easier to sort
[1562.24 --> 1566.60]  of like build out something statically you know with all the urls and all these different things that
[1566.60 --> 1572.98]  i think of as a ux or designer standpoint or a front-end builder standpoint and build you know a
[1572.98 --> 1578.52]  good portion of my prototype or even my prototypes to prove to the business team like hey we can build
[1578.52 --> 1583.12]  this or this is the direction we should go i'll build that middleman with almost zero resistance
[1583.12 --> 1589.46]  and really not a lot of ruby knowledge beyond you know what the docs could easily provide in terms of
[1589.46 --> 1595.26]  middleman routing and stuff and then give that over to my rails team or demonstrate that and be able
[1595.26 --> 1600.40]  to take a lot of what i've done already and just pull it right into the rails app with almost no no
[1600.40 --> 1607.50]  issues yeah i mean i kind of like we map to the way it used to be on the front end you just you pop
[1607.50 --> 1612.40]  open a new folder you open notepad or whatever and you just start making files your static files
[1612.40 --> 1617.74]  and you wrote all your html you wrote all your css and you put 50 script tags into your html and you
[1617.74 --> 1621.74]  know the reason we don't do some of those things now is because you know sas is faster um templating
[1621.74 --> 1628.32]  is faster uh you know we want to compress things smaller for the the end user but none of those are like
[1628.32 --> 1633.62]  changing the flow so middleman steps in and says i'll handle concatenating all your javascripts
[1633.62 --> 1638.20]  i'll handle your shortcuts in sas just keep writing you know the same kind of straightforward
[1638.20 --> 1642.32]  completely back-end free uh approach to you know front encoding
[1642.32 --> 1649.22]  the cool thing about long-term projects is there's lots of things that change over the years and then
[1649.22 --> 1653.48]  there's lots of things that stay the same and it seems like when you strike a chord early on
[1653.48 --> 1659.76]  um in architecture or you know those big decision making um you can just kind of refine over the
[1659.76 --> 1666.82]  years and thomas you recently wrote a post on your blog which i believe is award-winning fjords
[1666.82 --> 1672.76]  which that's correct right that's like the best website name i think i've ever heard i'm pretty
[1672.76 --> 1677.24]  jealous of it um i also have the fjords twitter account but i haven't figured out what to do with it
[1677.24 --> 1681.98]  yeah just hold on to that baby and just wait wait for the wait for the check there's a
[1681.98 --> 1687.54]  norwegian hardcore band who always who i always get subtweeted by which is pretty cool completely
[1687.54 --> 1693.90]  off topic but kind of related is whoever the guy who had the alphabet account on twitter
[1693.90 --> 1702.56]  oh man he's sitting on a gold mine there after google renamed but um so yeah maybe fjord maybe
[1702.56 --> 1706.54]  someday you know you'll have some large company rename themselves to fjord and you'll just be sitting
[1706.54 --> 1714.20]  on like it um but you've had uh you know over the years you refine your thoughts you refine even the
[1714.20 --> 1720.30]  way you write code and uh it seems like that is something that's happened to you in kind of dramatic
[1720.30 --> 1729.10]  ways um you recently published a post back in march called my weird ruby um where you go through
[1729.10 --> 1734.04]  kind of how you write ruby code today and how that's way different from probably back in 2010
[1734.04 --> 1739.30]  uh when you started middleman so i'm going to tee that up we need to take a break here from a
[1739.30 --> 1744.36]  sponsor but on the other side of the sponsor break i want to hear your thoughts on why your ruby is weird
[1744.36 --> 1751.64]  and how that has affected middleman for so we'll be right back you've heard me talk about top towel
[1751.64 --> 1757.52]  several times in this podcast but today is different i've got a special treat for you i went out and spoke
[1757.52 --> 1764.16]  with a listener who a year ago had never heard of top towel he listened to the show just like you're
[1764.16 --> 1768.86]  doing right here right now today and heard us talk about top towel and what they're all about and he
[1768.86 --> 1774.22]  decided to get in touch and now he's living the dream as a freelance software developer with top towel
[1774.22 --> 1779.98]  his name is daniel alzon and i sat down and i talked with him i said hey what is it that you love
[1779.98 --> 1786.78]  most about top towel take a listen well for me the the thing about top towel which i thought would be
[1786.78 --> 1794.28]  very hard for me personally as i transitioned to a more consulting role uh was the way i would have
[1794.28 --> 1800.66]  access to new clients and what quality of those would be so i found that i've had access to awesome
[1800.66 --> 1804.98]  clients through top towel and it hasn't been that hard to find because they have a lot of choice
[1804.98 --> 1811.28]  and even more than that uh there's enough choice and i i can actually be a little selective about
[1811.28 --> 1817.24]  what kinds of things i want to be working on so i use that as a way to sort of hone my skills and
[1817.24 --> 1822.80]  you know go towards the technology that i think are worth investing in for the future so whether it's
[1822.80 --> 1828.84]  you know including new front-end frameworks or doing a little devops work on the side i i usually am
[1828.84 --> 1834.10]  able to find clients who are have the needs of the things i want to get better at so that's been
[1834.10 --> 1839.92]  that's been uh truly useful all right that was daniel lazon a listener of the change log
[1839.92 --> 1846.58]  and also a freelance software developer with top towel if you want to follow in daniel's footsteps
[1846.58 --> 1856.82]  go to top towel.com slash developers that's t-o-p-t-a-l.com slash developers to learn more about what top
[1856.82 --> 1859.84]  towel's all about and tell them the change log sent you
[1859.84 --> 1869.36]  all right everybody we're back speaking with thomas reynolds about middleman and thomas you've
[1869.36 --> 1875.90]  been working on middleman for for a while now um you've recently published a blog post entitled
[1875.90 --> 1882.02]  my weird ruby um wherein you state over the past year i've been rewriting large portions of the
[1882.02 --> 1888.64]  middleman code base to better reflect how i like to write code as opposed to the silly version
[1888.64 --> 1897.24]  of of of mine of typo typo typos exposed breaking news here on the change log there's a typo in a
[1897.24 --> 1902.94]  blog post uh as opposed to the silly version of the old person six years ago so you've been rewriting
[1902.94 --> 1907.60]  a lot since you've learned things you've changed your style and that's kind of dramatically affected
[1907.60 --> 1913.38]  the middleman code base can you speak to that yeah totally um so kind of like i said i do a lot of
[1913.38 --> 1921.38]  javascript at work um i do ruby for middleman i have done closure i have done java and um got into
[1921.38 --> 1925.80]  some haskell and i like to like try as many different languages as possible and you know
[1925.80 --> 1929.70]  there's always good ideas you can bring them all back so i can write another post later called my
[1929.70 --> 1936.02]  weird javascript because it's equally silly but it's kind of got the same gist um yeah like when i
[1936.02 --> 1943.68]  started middleman uh ruby was getting popular but ruby is also kind of a minefield of features um
[1943.68 --> 1948.38]  some great stuff in there there's some stuff you should never ever use i think uh you know like
[1948.38 --> 1954.70]  rails too had a bunch of these like just mix-ins forever or you know duct typing and all these kind
[1954.70 --> 1959.78]  of very uh famously ruby features that you probably wouldn't want to use in production alias method
[1959.78 --> 1967.68]  yeah alias method yeah that was a good one yeah so you know that's how middleman 2 looked like that's
[1967.68 --> 1973.04]  what middleman 3 pretty much looked like with some more inspiration um from rails 3 which has a lot
[1973.04 --> 1979.44]  more of uh it's kind of i don't know they have a completely crazy uh mix-in inheritance chain thing
[1979.44 --> 1984.96]  that's still in there that i don't understand but um so that's what it looks a lot like rails but you
[1984.96 --> 1990.16]  know it's been two three years since that stable version i've just been making bug fixes on there
[1990.16 --> 1995.20]  and then i spend most of my day doing other languages so uh i've just come up with a bunch
[1995.20 --> 1998.16]  of things seen a bunch of things in other languages that i like and i want to bring them back
[1998.16 --> 2003.70]  so i don't every time i i would fix a bug um in the stable branch of middleman i would realize that
[2003.70 --> 2007.48]  this could have been solved like i would have if i had just used something from haskell if i just
[2007.48 --> 2012.78]  used something from closure um this would never have been a problem uh so i think the biggest one for me
[2012.78 --> 2019.38]  is uh maturing as a developer and deciding that i actually do like static typing and you know that
[2019.38 --> 2023.50]  all the loose typing of ruby was a really big selling point when it was first coming out because
[2023.50 --> 2028.40]  you know people are coming out of the java world and such um but you know what those things caught
[2028.40 --> 2033.54]  bugs they caught bugs without writing tests and i think uh being able to type your code especially
[2033.54 --> 2037.44]  public code that other people are going to want to interact with as like a public api
[2037.44 --> 2043.68]  is a really good approach so i discovered this library about a year ago um called contracts
[2043.68 --> 2051.90]  which uh uses a lot of metaprogramming magic to wrap every single um uh variable and every single
[2051.90 --> 2057.48]  uh method with like a little wrapper and then you define what kind of things should go into the
[2057.48 --> 2060.74]  function and what kind of things are about to come out of the function and this little wrapper will
[2060.74 --> 2066.10]  check them and throw exceptions uh if you're in like dev mode or test mode and so that just allows you
[2066.10 --> 2071.50]  to say you know there's a lot of places where in middleman and in ruby you say here's a method
[2071.50 --> 2076.74]  it's called you know i'm looking at one here find it could take a symbol it could take a string it
[2076.74 --> 2081.58]  could try to like turn those two into the same thing uh it could take a regex you never know and
[2081.58 --> 2087.38]  there's a lot of these kind of like open magical apis throughout rails in the ruby world uh i decided
[2087.38 --> 2092.46]  i didn't like that very much so i went whole hog with this contracts library and i added type
[2092.46 --> 2099.26]  information to every single um variable and definition uh inside of my middleman code and
[2099.26 --> 2106.72]  what that gave me was an insane number of uh bug reports that uh my test suite my test suite of you
[2106.72 --> 2112.38]  know something like 4200 tests didn't catch just like then people were probably saying oh yeah like
[2112.38 --> 2116.18]  i know to put a symbol here they don't know to put a symbol here um and the amount of documentation
[2116.18 --> 2120.84]  they need to figure that out it's just they're never going to look it up so uh that was like the first
[2120.84 --> 2127.10]  big refactor to middleman 4 and it's completely you know opaque to the user that's just for me
[2127.10 --> 2132.00]  so i can catch bugs earlier and so i feel a little safer when i'm working with this relatively large
[2132.00 --> 2138.80]  code base so that just begs the question uh you know you're basically adding like static type checking
[2138.80 --> 2145.64]  to ruby i guess why not just you know try a different language yeah i mean that's just back
[2145.64 --> 2152.28]  to my stability thing i mean the roots are in the community my contributors speak ruby uh the the big
[2152.28 --> 2156.30]  rewrite is always a terrible idea especially if you're switching languages you might as well just
[2156.30 --> 2162.06]  start a whole new thing um now it's been a lot of work it's not a tiny code base doing a lot of
[2162.06 --> 2169.98]  weird stuff i feel like if i could i would maybe have rewritten it in closure but then um at the time
[2169.98 --> 2173.88]  getting closure up and running was kind of a pain nowadays i think you can just run it right
[2173.88 --> 2179.92]  through node which is pretty cool but at the time it wasn't the best fit there has been uh rumors
[2179.92 --> 2186.36]  you know of gradual typing being added to future versions of ruby so this may be a feature that i
[2186.36 --> 2191.96]  just switched to the official support if that comes down the road i've never heard of this contracts
[2191.96 --> 2197.54]  library can you tell me where it's at or talk about it a bit uh it's just called contracts.ruby
[2197.54 --> 2203.90]  it's a little hard to find but it's um i think it's got such a general name it's really hard to
[2203.90 --> 2209.82]  search for yeah so like it's not really typing it's just designed by contract concept which is
[2209.82 --> 2215.38]  basically um lightly enforced types like things will still work it'll just be able to complain about
[2215.38 --> 2221.00]  it uh so i don't know where it came from but um the gentleman who runs it has started uh updating
[2221.00 --> 2225.50]  it a lot more recently and there's third-party contributors adding code to it now so it seems like
[2225.50 --> 2229.72]  it's kind of getting a little popularity um i would never use it in production the whole point
[2229.72 --> 2233.62]  of this thing is you know it throws an exception during your test suite not you know when someone's
[2233.62 --> 2238.96]  actually trying to use your code this is something that you've heard of jared well i heard of it in
[2238.96 --> 2244.70]  march when i read uh his blog post but i haven't heard of it elsewhere okay gotcha um yeah so it's
[2244.70 --> 2249.26]  active that's great um when i was using it actually was inactive it would just been like an experiment
[2249.26 --> 2254.96]  that someone had put together so uh a little bit risky but it's pretty easy to comment out it's just
[2254.96 --> 2258.98]  every single one of these definitions starts with the word contract it's a pretty easy search and
[2258.98 --> 2265.14]  replace to go back to the old buggy version but um i found i really enjoy it uh i'm looking to
[2265.14 --> 2270.32]  decorators and javascript to add some more functionality uh on the javascript side so i can
[2270.32 --> 2276.10]  add some type information have it copy the test suite so adam and i are in a bit of a unique position
[2276.10 --> 2282.78]  because we have a a site um which we use to to generate our weekly newsletter changelog weekly
[2282.78 --> 2289.40]  which is a middleman 3 site and we've also been working on a new site for our video series beyond
[2289.40 --> 2296.30]  code um which is a middleman 4 site because i hopped on the beta because i like pain i guess
[2296.30 --> 2302.46]  it hasn't been too painful a few a few things um and i can definitely attest to the fact that this
[2302.46 --> 2307.82]  contracts piece is completely invisible to an end user because um i would have never even known about
[2307.82 --> 2314.28]  it had not been for this post one thing i have felt as an end user is you've also introduced a lot
[2314.28 --> 2319.78]  of uh immutable data structures um can you speak about that and then maybe i can give you a little
[2319.78 --> 2325.80]  bit of feedback from from my perspective yeah yeah that also just comes from my experience and these
[2325.80 --> 2331.68]  kind of more functional languages um they tend to prevent a large class of bugs just because you're
[2331.68 --> 2336.18]  not doing weird loops and messing with your stuff um one bug we got a lot back in the day was
[2336.18 --> 2341.34]  we have these this directory of data files and there's yaml information in it and so from the
[2341.34 --> 2346.30]  templating side you can go ahead and say you know grab the first five people from this yaml file and
[2346.30 --> 2354.42]  people would go then go add another person to that array and then expect it to persist and also expect it
[2354.42 --> 2360.04]  to um somehow sync back to the data side to the actual file structure and so one of the main reasons
[2360.04 --> 2365.50]  for going with um it's still kind of an experiment i put in hamster which is one of these uh kind of
[2365.50 --> 2371.10]  wrapper libraries and so you talk about a hamster hash instead of like a native ruby hash and what
[2371.10 --> 2377.04]  it basically does is just doesn't give you methods uh to alter data that's not allowed to be altered
[2377.04 --> 2384.26]  like this kind of static yaml data um i put like a lot of things in in version four i think i try to
[2384.26 --> 2389.96]  refactor without touching the api to tools that i like a little bit more that one is definitely the
[2389.96 --> 2394.94]  newest and i've also run into surprises around it especially if you don't even know it's there
[2394.94 --> 2400.38]  and suddenly it's throwing these crazy errors at you um so yeah i would love to hear some uh stuff
[2400.38 --> 2405.04]  about that i think that's trying to get people on the beta so we can uh flush this out but that's
[2405.04 --> 2411.28]  going to be day one 4.0 stable right you know there'll be probably 30 bug reports and try to get
[2411.28 --> 2416.40]  the messaging right around it i think yeah i think my experience is mostly around what you said when you
[2416.40 --> 2420.66]  don't even know that that's what you're working with and it's kind of like the uncanny valley where it's
[2420.66 --> 2428.02]  like it's almost an array or it's almost a hash um until you find out that it's not um and the
[2428.02 --> 2435.04]  specific thing that i hit quite often um is probably difficult to explain on air like this um but i am
[2435.04 --> 2440.92]  using the the data directory and basically what we have is a bunch of seasons of of the of the show
[2440.92 --> 2447.72]  and then each season has some episodes uh kind of nested inside of it and uh in certain cases i was
[2447.72 --> 2452.64]  trying to like just flatten so i like mapping over the seasons to get the episodes and then flatten
[2452.64 --> 2462.56]  that into a single array of episodes um and you can't flatten a hamster data set um probably because
[2462.56 --> 2467.14]  it's immutable right although with the flattened call i was trying to i was trying to return a new
[2467.14 --> 2471.62]  one yeah i should just return a new one it really should have worked um but yeah that's a great call
[2471.62 --> 2477.88]  if it's not one of the ones like the native ruby stuff then that's definitely a problem um
[2477.88 --> 2485.38]  unfortunately like native ruby api is expansive and yeah exactly editable yeah uh yeah so i'll take a
[2485.38 --> 2489.42]  look at that and see if uh they just got some missing you know it might just be an alias right like
[2489.42 --> 2496.52]  right half the things on the ruby uh uh passion array libraries are aliases for three other things
[2496.52 --> 2501.16]  it's kind of crazy right yeah i guess it turns out we brought you on air just to bug report for you so
[2501.16 --> 2507.76]  the only thing more exciting than life coding is like bug reports uh why everybody's here
[2507.76 --> 2514.52]  facts please yeah exactly now it has to get fixed right because it's on air um yeah totally so you
[2514.52 --> 2519.98]  have okay so you got contracts um you know you're you're playing with uh immutability and i think
[2519.98 --> 2523.96]  that's just a great point that you know when you have a beta and even yours has been in beta for a
[2523.96 --> 2529.64]  while now like you the point of a beta is for people to hop on and and do the bug reporting but you
[2529.64 --> 2534.94]  actually don't get very many until you announce that you know that official release and then all
[2534.94 --> 2540.28]  of a sudden everything kind of just swarms in i wonder if there's like is there any way we can make
[2540.28 --> 2547.08]  that can we fix that problem is there any way i don't know uh i don't know so uh this is kind of
[2547.08 --> 2550.88]  a tangent but there was a pretty good blog post i'll dig up the url for you later but it was
[2550.88 --> 2556.34]  you know always use uh simple tools and it kind of has this philosophy it's like you know shouldn't
[2556.34 --> 2559.80]  surprise you it should just be simple and get out of the way its way and do its job and then you
[2559.80 --> 2563.84]  should go home so i don't know if i want to ask people to spend their weekends or their extra time
[2563.84 --> 2570.20]  making their work stuff work for my beta but um and actually i'm not entirely sure how smooth the
[2570.20 --> 2575.82]  upgrade process is going to be um we removed a lot of features we removed redundant features so
[2575.82 --> 2581.54]  uh a lot of like we didn't remove uh functionality but there might be a little bit of editing so
[2581.54 --> 2587.72]  we'll try to figure out um you know ember again does a really great job with these upgrade guides
[2587.72 --> 2592.46]  we're going to try to figure out a way to document and say like we expect this to take you an hour or
[2592.46 --> 2599.06]  two hours so you don't just go down a rabbit hole trying to upgrade to this so i find it i just back
[2599.06 --> 2605.30]  to the uh the conversation about the kind of the weird ruby style and uh a related question around
[2605.30 --> 2609.48]  that is you know you have years and years of writing ruby you're obviously a javascript developer as
[2609.48 --> 2616.00]  well and it sounds like you have some exposure to closure and a few other languages so here we are
[2616.00 --> 2622.92]  you know mid 2015 and there's a lot of new and exciting languages kind of out there um ones that
[2622.92 --> 2628.14]  are kind of capturing the the hearts of many developers are uh things like go i think rust is
[2628.14 --> 2632.56]  pretty exciting to a lot of people of course the functional languages like closure as well are you
[2632.56 --> 2637.78]  still bullish on ruby after all these years or are you are your eyes starting to to wander into these
[2637.78 --> 2643.94]  other camps um you know it just depends what kind of project you want to build uh i would never
[2643.94 --> 2649.80]  you know go and you know if you just want a straight fast api to just crank out some json uh
[2649.80 --> 2656.00]  go is really good for that if you want to build a web server you know rust is probably really good for
[2656.00 --> 2660.66]  that i would i would probably never build a web server in ruby that would be crazy yeah uh so i think
[2660.66 --> 2667.10]  everything's got its place i think ruby still reigns supreme for mostly because of rails um just like i need a
[2667.10 --> 2672.56]  website i need a traditional front and back end and this is the most stable um most secure one you
[2672.56 --> 2676.92]  can probably get other than maybe some php stuff but it's definitely the most fun to work in for that
[2676.92 --> 2681.82]  trade-off so i think it'll it'll have it'll be in that space for a while um we still use it at work
[2681.82 --> 2690.48]  so you know it's not going anywhere uh yeah all right i i am i am opposite was the opposite of
[2690.48 --> 2697.68]  bearish bearish yeah i am bearish on javascript still so are you really yeah so i mean uh you know
[2697.68 --> 2703.20]  i don't i don't i dread the day when you know i just remember like you're on the plane and like
[2703.20 --> 2708.30]  the kiosk crashes with a windows warning i dread the day when i see like javascript crashed in chrome
[2708.30 --> 2715.18]  right it's like my airplane warning uh i think it's probably one of the worst languages we have to use
[2715.18 --> 2721.82]  on a on a uh reasonable basis uh so i would not i would i would go to ruby for javascript in a lot
[2721.82 --> 2729.06]  of cases for similar tasks like task running or um you know exactly something like middleman so that
[2729.06 --> 2735.16]  leads me into the question about these uh about this the front end frameworks so middleman seems like
[2735.16 --> 2743.40]  it could be a decent uh generator for an app that is an ember or a angular based uh you know fat client
[2743.40 --> 2749.98]  is that the case or should you use their tools directly for um these kind of things that's a
[2749.98 --> 2755.66]  good question um i would probably just say use their tools the ember command line tool is really
[2755.66 --> 2761.10]  really good that's really really focused and you know if you're not writing a ton of uh html you know
[2761.10 --> 2765.44]  we don't solve a lot of problems for you and if you're all client side then we're not solving your
[2765.44 --> 2770.68]  routing or like your file structure problems for you either so probably use their tools uh but you
[2770.68 --> 2776.22]  know where we succeed now and where we're seeing a lot of heavy usage is uh large is blogs is large
[2776.22 --> 2781.98]  documentation sites a lot of like this kind of uh generated content from some other source so you
[2781.98 --> 2788.74]  have a pile of markdown files and you want a full localized documentation site so you know people like
[2788.74 --> 2794.46]  basho and nest and a bunch of all these uh you know uh mailchimp build these large documentation
[2794.46 --> 2799.24]  portals kind of on middleman because they can just do a couple loops do a couple templates and get
[2799.24 --> 2805.86]  these large large sites out the side uh that said i'm still trying to use it uh for my frontend work
[2805.86 --> 2811.70]  as well so uh version four probably the biggest feature that i use on a daily basis is this ability
[2811.70 --> 2817.56]  to uh run sub processes inside a middleman so basically what you say is i want you to boot up
[2817.56 --> 2823.76]  the ember cli web server and i want you to proxy from middleman to that so if two-thirds of your site
[2823.76 --> 2829.26]  and all of your css is in middleman then you let ember um return to javascript and then we all just
[2829.26 --> 2836.92]  build this one cohesive whole so i've been using webpack a lot just because uh webpack and babel
[2836.92 --> 2841.90]  give me some nice tools on the front end to use modern javascript and then that just fills kind of
[2841.90 --> 2846.00]  like the sprockets role in my middleman stack and then everything else is still middleman
[2846.00 --> 2852.26]  so we're experimenting with that it seems to be working pretty smoothly any other major uh middleman
[2852.26 --> 2856.76]  four features i know a lot of it has been pulling out old cruft is there is there anything else that
[2856.76 --> 2862.30]  you're excited about for the new version there's some light stuff uh we switched to a rail style
[2862.30 --> 2869.28]  environment split so before you just had you know are you building are you devving now it's like do you
[2869.28 --> 2873.94]  want to build for staging do you want to build for hotfix branch do you want to build for production
[2873.94 --> 2878.94]  so that gives a little bit more control for multiple environments for testing environments and
[2878.94 --> 2884.22]  um you know using stuff like travis to deploy builds that may be not ready to go into production
[2884.22 --> 2891.54]  uh the other big one i think is moving all of our base templating stuff to github so before you'd have
[2891.54 --> 2897.70]  to install ruby gem outside of bundler hope it's there globally and then initialize it through middleman
[2897.70 --> 2903.44]  now you just give it a github path or any git path and it'll just pull down that whole repo as
[2903.44 --> 2908.40]  like your starter template for a new project and then it'll run your custom code so it's a lot
[2908.40 --> 2913.60]  some more similar to something like yeoman um where we let everyone manage their own stuff rather than
[2913.60 --> 2919.38]  having to go through our like kind of ruby gem pipeline do you think it's a an issue since you
[2919.38 --> 2924.90]  mentioned you know who might be using middleman and what languages we talked about languages and
[2924.90 --> 2934.14]  you know choices and whatnot is the fact that middleman is a ruby uh gem does that stop people
[2934.14 --> 2938.46]  from using it those who care about languages is there is there a competitors to middleman and other
[2938.46 --> 2942.36]  languages that sort of make you think man i kind of uh they're stealing my thunder here
[2942.36 --> 2948.76]  yeah i mean the install setup story for ruby has always been pretty hard it's still really really bad
[2948.76 --> 2955.66]  on windows so yeah it's kind of it kind of sucks you know the the trade-off is this is a tool you use
[2955.66 --> 2961.52]  for work it's important it's going to save you time so spend the 30 minutes necessary to get your
[2961.52 --> 2968.96]  ruby gem set up but yeah that that's not great um there's one in go what was that called jaren
[2968.96 --> 2974.60]  we just talked about that it's like a hugo it's like a hugo yeah we call yeah uh super jealous of that
[2974.60 --> 2978.58]  because they get because go gets compiled to a single or not single but it compiles some
[2978.58 --> 2982.80]  multi-platform binaries so you just drag this file on your hard drive and everything's perfect
[2982.80 --> 2988.72]  um not going to rewrite for that but that's a pretty cool feature um and then now this the ubiquity of
[2988.72 --> 2995.36]  node gives something like uh metalsmith or uh a couple of the other node ones it's just it feels
[2995.36 --> 2999.60]  more natural for a front-end person to install those libraries now or they probably already have
[2999.60 --> 3004.40]  node because if your audience is a designer or a front-end person then you're front you know if
[3004.40 --> 3007.74]  you're coming from npm you're already in their world basically you're already in their tool set
[3007.74 --> 3013.42]  yeah there's no change there and to i always wondered if if ruby would hurt you over time
[3013.42 --> 3019.00]  considering that the people that are writing rails apps typically aren't building middleman sites
[3019.00 --> 3024.70]  i guess jared's an anomaly potentially but it's typically somebody that's you know more of a
[3024.70 --> 3030.94]  front-end player than than a back-end player right that's a thing yeah i mean a job anecdotally i think a
[3030.94 --> 3035.00]  lot of people do come from rails and though and then we also have a lot of people who classify
[3035.00 --> 3040.66]  themselves as designers but they can obviously code and for them they don't they didn't pick a side on
[3040.66 --> 3046.60]  the language war so they don't really care if they're installing npm or node or ruby i think just
[3046.60 --> 3054.14]  on the windows side i think nodes first class support for windows from the very beginning was a huge boon
[3054.14 --> 3059.74]  for its adoption i think that that served it really well and i think ruby's always had issues
[3059.74 --> 3066.44]  on windows and you know there's been huge efforts to improve that but it's always like after the fact
[3066.44 --> 3072.16]  you know it's kind of like a security practice you can't just bolt security on afterwards onto your
[3072.16 --> 3076.36]  onto your software it has to be you know something that you think of from day one and it seems like
[3076.36 --> 3081.20]  you know cross-platform support is another one of those things that once you don't prioritize it early
[3081.20 --> 3085.72]  on it's just really hard to get it right later i think the ruby community has probably suffered a
[3085.72 --> 3092.88]  bit from that yeah i uh as an aside i just built a gaming pc for myself and i haven't been using
[3092.88 --> 3097.62]  windows for about a decade now so i'm recently back in the flow of everything on the windows side
[3097.62 --> 3103.26]  it's like i can actually test bugs now it's amazing um but like everything sucks over here
[3103.26 --> 3109.68]  i just try to install like simple things and it's taking me like 15 clicks and i can't find the links and
[3109.68 --> 3117.18]  like i get why you know it's just brew install node is so easy and like that unless without some
[3117.18 --> 3121.34]  support from microsoft that'll never be you know a thing you can do on windows so there's always going
[3121.34 --> 3127.30]  to be i think a barrier uh just kind of unfortunate but i would love to see better windows support from
[3127.30 --> 3134.34]  ruby that's a hard hard job sure it is yeah so i got some questions about the core team and just
[3134.34 --> 3140.40]  how you formed the people that helped make middleman possible but uh to take a note from
[3140.40 --> 3145.22]  jerry do have to take a quick sponsor break um so let's take that break real quick when we come back
[3145.22 --> 3149.32]  we'll talk a bit about the core team and start tailing into some of our closing questions which
[3149.32 --> 3153.68]  i'm sure that the internet is just dying to hear so we'll take a break we'll be right back
[3153.68 --> 3160.78]  i have yet to meet a single person who doesn't love digital ocean if you've tried digital ocean
[3160.78 --> 3166.98]  you know how awesome it is and here at the changelog everything we have runs on blazing fast
[3166.98 --> 3173.18]  ssd cloud servers from digital ocean and i want you to use the code changelog when you sign up today
[3173.18 --> 3180.12]  to get a free month run a server with one gig of ram and 30 gigs of ssd drive space totally for free
[3180.12 --> 3187.14]  on digital ocean use the code changelog again that code is changelog use that when you sign up for a
[3187.14 --> 3191.82]  new account head to digitalocean.com to sign up and tell them the changelog sent you
[3191.82 --> 3199.82]  all right we're back with thomas reynolds maker of middleman been talking through quite a bit of history
[3199.82 --> 3207.82]  of static state generators a bit of uh you know go love there where you're i was trying to figure out a
[3207.82 --> 3214.20]  good way to say that but just like some some some uh impressedness if that's uh that's a thing to say
[3214.20 --> 3220.26]  from you towards the go community about the way they're doing things too and i'm kind of curious on that
[3220.26 --> 3227.38]  note before we go into the core team thoughts and whatnot but i'm curious if um if you were building
[3227.38 --> 3234.34]  middleman today and it was ground zero what would you build it in that's a great question i would
[3234.34 --> 3240.50]  probably go is probably uh where i would build it and i actually i have some negative thoughts about go
[3240.50 --> 3245.96]  such as their dependency management requiring git which is a little weird but uh other than that it's
[3245.96 --> 3250.60]  just it's a really slim language and their whole goal is to have one way of doing everything and that
[3250.60 --> 3256.16]  kind of aligns with you know a lot of the uh frustration from ruby of having like three ways to do
[3256.16 --> 3260.44]  everything so i think it's a nice slim language and it's compiled stories to different targets is pretty
[3260.44 --> 3268.26]  nice uh i also that's just a joy in coding i really really love closure uh closure has always
[3268.26 --> 3272.96]  been this close to working on node i think it's actually done now so the idea of just being able to
[3272.96 --> 3278.68]  you know npm install middleman or something i get to write it in the language with the features i like
[3278.68 --> 3283.70]  everyone else gets to use javascript for their configuration um i think that'd be pretty cool too
[3283.70 --> 3288.18]  so i was thinking of a name while you were talking there go man could be kind of cool
[3288.18 --> 3296.34]  go man go middle go there's no you're always trying to name things adam i know i know so go man go i like
[3296.34 --> 3303.80]  that actually so with a seven year history i gotta imagine that over these years you've uh made some
[3303.80 --> 3309.50]  friends those friends have become core team members contributors can you talk a bit about the
[3309.50 --> 3314.16]  history or even highlight some people over the years that have helped uh make middleman possible
[3314.16 --> 3320.32]  that may not have gotten recognition elsewhere totally um have about four core team members now
[3320.32 --> 3326.52]  i'm always looking for more uh but it's responsibility and it's you know not the funnest job uh to just be
[3326.52 --> 3332.06]  fielding bug reports or triaging so uh ben hollis has been my partner for three or four years now
[3332.06 --> 3338.52]  uh he is an engineer up at amazon and his cycle basically works so that when he's on a middleman project
[3338.52 --> 3343.30]  we're getting great support and great features and we're working together when he's not that's cool
[3343.30 --> 3348.24]  i'm probably on one so i'm also contributing features but you know i don't expect year-round
[3348.24 --> 3353.02]  or even like month-round uh contributions from people just having a little bit of backup and a
[3353.02 --> 3357.88]  little uh someone else to check my code and make sure i'm not making a huge mistake is um completely
[3357.88 --> 3363.70]  amazing um carl freeman has also helped out a lot he's pretty big in the node community
[3363.70 --> 3368.18]  i'm sorry not the node community the inbred community over in europe as well uh so he you
[3368.18 --> 3373.88]  know keeps me legit on uh making sure javascript doesn't get broken too badly uh let's see
[3373.88 --> 3381.12]  elliot appleford has recently jumped in and uh he's also in the united kingdom he's a ruby he's a much
[3381.12 --> 3385.94]  better ruby-ist than i so he's able to answer with like you know all these years back and experience
[3385.94 --> 3390.16]  a lot of my ruby questions uh to keep me again from suiting myself in the foot and he's doing a great
[3390.16 --> 3395.16]  job managing uh the github and you know closing out things reporting things as duplicates uh all
[3395.16 --> 3400.20]  that kind of squishy stuff that can eat up a lot of time and then recently we've had another
[3400.20 --> 3409.72]  contributor uh dennis guntwig that don't test my german uh he is uh a beast and like the pull
[3409.72 --> 3413.50]  requests coming out of him are amazing and it's just like holy cow he did this in a weekend uh so
[3413.50 --> 3417.52]  having like actual large feature development done by someone other than me has been really really great
[3417.52 --> 3423.40]  and then you know everyone who's ever contributed uh to the documentation site is absolutely amazing
[3423.40 --> 3430.16]  uh there's just let's see there's been 113 contributors to core and let's see there have been
[3430.16 --> 3439.54]  i'm not gonna make this come up there's been hundreds and hundreds how many 265 on middleman guides
[3439.54 --> 3444.68]  yeah 265 people who helped uh with the documentation made everyone's lives easier so
[3444.68 --> 3452.76]  they're all amazing and couldn't do without them so is everyone listed um under org slash middleman
[3452.76 --> 3458.56]  slash people are all those uh contributors then or just only a few those are all people who have the
[3458.56 --> 3463.88]  commit bit yep okay so we don't have like we don't have we have a couple email threads we don't have
[3463.88 --> 3468.40]  like a core you know email group or anything like that it's pretty light but um all those people have
[3468.40 --> 3472.84]  been making you know invaluable contributions over the seven years awesome i want to make sure we link
[3472.84 --> 3477.52]  that page so we'll if you're listening to this we'll link that link up as well as the other
[3477.52 --> 3482.92]  individuals that uh that thomas has mentioned in the show notes so the show notes would be i think
[3482.92 --> 3490.30]  what uh changelaw.com slash 169 sips of 169 jared i can't believe it man it's real it's crazy man
[3490.30 --> 3497.50]  believe it but uh i guess you know when we're talking about the people that have stepped up to help out
[3497.50 --> 3502.04]  and and uh you mentioned your forum earlier to allow the community to sort of step in and
[3502.04 --> 3507.46]  and you not be burnt out you know jared we've talked about sustaining open source on this show
[3507.46 --> 3512.92]  with mike perrin before and and several other times in other episodes but thomas what kind of
[3512.92 --> 3519.54]  insights can you share that you've done over the years to guard yourself against burnout and maybe even
[3519.54 --> 3526.18]  a touch on that could be um how you've how you've sort of fostered this community that's that's
[3526.18 --> 3528.72]  whether you've tried to or not has come up around middleman
[3528.72 --> 3536.60]  uh it's just for me i think you know just be nice to people there was a whole raft of github
[3536.60 --> 3542.26]  public github spats like on bug reports for like you know maintainers are yelling at contributors and
[3542.26 --> 3549.54]  just not you know you can shut that stuff down uh same old normal people soft skills uh i get to use
[3549.54 --> 3554.10]  them i'm a manager i do it all day uh so this is just managing random people on the internet which is a
[3554.10 --> 3558.24]  little harder but you know be nice everyone will be nice to you the ruby community has always
[3558.24 --> 3564.38]  been nice uh so i think that's mostly like and once you have a once you have this backup once you have
[3564.38 --> 3568.38]  this community behind you you know you're not gonna get me emails in the middle of the night you're not
[3568.38 --> 3573.84]  gonna feel as much stress i think uh about having to like i don't know constantly be working on this
[3573.84 --> 3580.96]  thing for me i check in like 9 a.m first thing at work uh do a little bug triaging if there's anything
[3580.96 --> 3585.44]  horrible i try to fix it on the spot but then i don't think about it until the next day or until
[3585.44 --> 3589.44]  i get inspiration i find a new language feature i want to do then i'll do that on my own free time
[3589.44 --> 3594.24]  but you know it hasn't been seven years of continuous development there's definitely you
[3594.24 --> 3599.46]  know these like i said we've been we've been stable for three years so it's just been little bug fixes
[3599.46 --> 3605.60]  and me exploring on my own i think that exploring also helps me you know avoid getting burnt out or
[3605.60 --> 3610.42]  avoid just having this fear that i don't even want to look at my own code anymore like you have to
[3610.42 --> 3614.82]  nip that in the bud you have to refactor as soon as you start hating your own code you can't just
[3614.82 --> 3620.78]  let it be there forever because you'll never go back that's interesting we've we've uh like i said
[3620.78 --> 3626.58]  we've talked about burnout several times on the show and it and it just seemed to me during the show
[3626.58 --> 3632.80]  that you've you've uh whether you've tried to purposely or not you've found something to avoid the
[3632.80 --> 3642.14]  burnout um and and jared we had that call on curl 17 years of curl i mean that guy was like two hours
[3642.14 --> 3649.14]  a day um and there's a commitment there's a commitment yeah on average two hours a day for
[3649.14 --> 3655.60]  17 years that's like a long time yeah it's incredible and it seems like somehow you you've
[3655.60 --> 3663.36]  found um the secret to not getting burnt out yeah that might just be my personality i've also been
[3663.36 --> 3668.54]  at the same job for like almost five or six years now too just i don't know walk away you can always
[3668.54 --> 3673.74]  walk away you can come back just don't burn any bridges and just know i've always known that i
[3673.74 --> 3678.60]  intend to support this for the long term so you know again keeping myself from burning out is super
[3678.60 --> 3682.54]  important to that right and when i said that guy meant daniel stemberg i always forget people's names
[3682.54 --> 3688.16]  i gotta go back on the list and look them up and not be offensive to people but uh daniel's pretty
[3688.16 --> 3694.06]  awesome shout out to daniel there was just uh that article going around by um i forget what library
[3694.06 --> 3698.02]  he was developer of but he's you know giving up active development because there's no money in it
[3698.02 --> 3703.60]  and try to zvl8 like you know people are getting rich off his work and he's not able you know to work
[3703.60 --> 3710.36]  this as a full-time job um but i think it frustrates anyone at a high level in open source so people are
[3710.36 --> 3715.14]  able to have like such a crucial piece that they can monetize it through support or you know
[3715.14 --> 3720.64]  contracting or even these special feature levels kind of like a sidekick is a really good example
[3720.64 --> 3729.18]  um but yeah so you know i like working i do agency work because i like to work so i like to be on the
[3729.18 --> 3732.32]  beach while people use middleman but i'm also probably just gonna go back to work the next weekend
[3732.32 --> 3739.34]  well now it's about the uh the time we turn it over to our super awesome ending show questions
[3739.34 --> 3747.36]  um the first question uh i'm gonna do you want to take you let me take it go for it bro so this is
[3747.36 --> 3754.04]  the easy one uh maybe maybe not maybe it's not or easy one to ask the easy one to ask it's always
[3754.04 --> 3759.94]  easy to ask right yeah uh so thomas you've you've been doing what you've been doing for quite a while
[3759.94 --> 3765.30]  i gotta imagine that over these years you've you've uh got a list of people whether you've made it
[3765.30 --> 3770.04]  purposely or not they're your heroes who out there in the programming world is your hero
[3770.04 --> 3776.46]  um yeah i think i mentioned i mean as a group i think the ember team has been spectacular i think
[3776.46 --> 3782.82]  i really respect those uh all those folks for you know having a commitment to commitment to stability
[3782.82 --> 3788.10]  having a commitment to documentation um then really guiding their community as like there's
[3788.10 --> 3791.94]  other bunch of shiny things around just basically saying you know we're gonna keep getting better
[3791.94 --> 3799.16]  and we're not going anywhere uh their documentation has been uh an example i've tried to follow and
[3799.16 --> 3804.60]  direct community management is even way way way better than mine uh so that whole team is absolutely
[3804.60 --> 3812.58]  amazing um judicats is a you know he's a he's a ruby master they use uh middleman over there at tilda
[3812.58 --> 3816.10]  and i've just kindly asked that he never look at my ruby for fear of
[3816.10 --> 3822.08]  the look the look of uh yeah i should probably give up ruby now and never do it again
[3822.08 --> 3830.44]  but that whole group is awesome very cool next up we mentioned contracts we mentioned hamster
[3830.44 --> 3836.06]  these are some ruby gems that have kind of been not just on your radar but uh in your toolkit lately
[3836.06 --> 3842.76]  but if you had a free weekend and you were gonna go hack on some stuff um what projects have you
[3842.76 --> 3846.48]  excited what's on your radar of cool open source projects that you want to check out
[3846.48 --> 3853.46]  uh so i've been using pixie js which is a front-end library for doing 2d graphics in webgl
[3853.46 --> 3858.68]  um been using that at work been using it on the side and it's just this kind of you know flash-like
[3858.68 --> 3863.56]  layer that allows you to get back um all kinds of amazing interaction and effects on the front end
[3863.56 --> 3868.70]  so i would definitely go throw together some kind of crazy 3d experiment um that whole project's
[3868.70 --> 3872.94]  open source and that whole team is also doing a great job of moving their project forward
[3872.94 --> 3879.18]  very interesting pixie is the fastest kid in town as they say i don't think i've seen it yeah it's
[3879.18 --> 3886.62]  amazing and it's no you know uh every single time i have to fight with a browser to animate like a square
[3886.62 --> 3890.46]  i get super angry i just want to throw the whole dom and the whole browser out the window
[3890.46 --> 3897.44]  um so if i can find refuge in webgl or find refuge in a tool like that and pretend flash still exists
[3897.44 --> 3904.00]  uh you know that comforts me at night awesome uh so for those out there that have listened to the
[3904.00 --> 3908.52]  show you know maybe they're like me and they've been following middleman for years they're new and
[3908.52 --> 3913.40]  they just met you for the first time here on the show uh and they want to help out they want to kind
[3913.40 --> 3917.78]  of dig in a little bit to middleman what's what's a call to arms to the community whether they're new
[3917.78 --> 3923.98]  to middleman or not new to middleman in ways they can step in either look at version 4 or help out
[3923.98 --> 3928.46]  on the community what are some ways to step in as the community can do can do uh to help out middleman
[3928.46 --> 3933.80]  yeah so i've always recommended um that people just write about it or talk about it you know
[3933.80 --> 3938.14]  tweet about it write about talk about it um everyone's going to have a unique use case they're
[3938.14 --> 3943.02]  going to have a unique perspective and that all doesn't fit into the core documentation so the more
[3943.02 --> 3948.80]  people you know i try to retweet retweet can't even say that word retweet uh as many blog posts as i can
[3948.80 --> 3953.28]  with these really interesting use cases uh i'm always surprised sometimes i see like middleman
[3953.28 --> 3958.32]  extensions that i would have never ever imagined could be written and it's really awesome to see so
[3958.32 --> 3963.92]  uh the more you can just google your question and you get an actual answer or even like a stack
[3963.92 --> 3968.34]  overflow answer uh the better it is for everyone you mentioned extensions that's something we didn't
[3968.34 --> 3973.42]  really dive too deeply into the show about because this isn't a comprehensive show like here's what
[3973.42 --> 3978.74]  middleman is um uh but maybe we could take a minute to mention the extensions the project
[3978.74 --> 3983.82]  project templates and the different deployment options you you have i mean you've got tons of
[3983.82 --> 3989.04]  extensions there made by the community some i gotta imagine are commissioned some that are just
[3989.04 --> 3993.62]  there because somebody needed it and then you can also search those extensions as well so it's pretty
[3993.62 --> 3997.62]  easy to sort of limit down to some things you want like let's say you want to deploy with
[3997.62 --> 4004.54]  onto aws there's there's an extension for that yeah absolutely uh that was something you know even
[4004.54 --> 4008.88]  in the rails days like the ability to have these plugins these extensions was super powerful to take
[4008.88 --> 4014.16]  the load off the core team so i tried to follow that example uh one of my philosophies with middleman
[4014.16 --> 4019.34]  which is pretty different from most static generators is uh we want you to write code it may not be very
[4019.34 --> 4025.18]  complicated ruby but at least you have all the tools and uh the power that code gives you uh to make your
[4025.18 --> 4030.46]  dreams you know real we don't want to be like one of these generators that all you have is one config
[4030.46 --> 4037.04]  file or one json file and try to like fit your entire stack your entire pipeline to you know that
[4037.04 --> 4042.52]  really rigorous structure so as part of that uh we farm out as much information as much api stuff as we
[4042.52 --> 4047.44]  can to the extension uh api and that lets people do you know pretty much whatever they want they can
[4047.44 --> 4052.90]  hook into most parts of the process they can replace parts of the process they can hook into uh new
[4052.90 --> 4057.64]  project template generation they can hook in and just you know add a single file to the page it
[4057.64 --> 4062.70]  doesn't or to the site that doesn't exist like you know do an api request get that bundle back make
[4062.70 --> 4068.06]  that a static api resource here there's all kinds of really good extensions because we've opened up as
[4068.06 --> 4074.88]  much ruby access as possible to the extension libraries cool so yeah some of the great ones um deploy
[4074.88 --> 4079.70]  middleman deploy which one of the core team members is actually the lead on well deployed everything you
[4079.70 --> 4084.78]  want to go to github pages you want to go to aws you want to go you know to any cdn it's all built
[4084.78 --> 4089.56]  into that one package um but you not have to worry about that you don't have to talk to an ops guy
[4089.56 --> 4095.42]  you can just get your website on the line very cool i'm hoping that one's middleman 4 compatible at
[4095.42 --> 4103.84]  this point yeah so that's me slowly realizing that uh i'll go look at like third party extensions
[4103.84 --> 4109.70]  like why did that break like in my mind i made no breaking api changes so there's like uh you know
[4109.70 --> 4115.62]  ruby makes it relatively hard to keep certain uh things out of scope so it's like oh i didn't
[4115.62 --> 4120.04]  realize that was a public method people were using so i gotta go through and either you know reopen
[4120.04 --> 4126.30]  a couple of those um apis for people make them stable in public or uh work with the extension authors
[4126.30 --> 4131.80]  to figure out you know why they're not using what i see to be as the canonical way to do the same thing
[4131.80 --> 4137.22]  speaking of uh deployed jared uh we mentioned a little earlier in the show when we were talking
[4137.22 --> 4142.06]  about middleman 4 and jared you were ranting a bit about amutable data structures and hamster and
[4142.06 --> 4148.24]  some of the things you've hit with middleman 4 in the efforts of building out our new site beyondcode.tv
[4148.24 --> 4153.52]  um so for those out there listening now it's a brand new thing we're launching but we've been
[4153.52 --> 4158.90]  producing beyondcode for a while it's a brief interview series we produce at conferences at the
[4158.90 --> 4163.86]  after parties and so the first one was at keep review weird uh the second one was at space cdjs
[4163.86 --> 4170.58]  the third one was at gopher con and the fourth one season four uh most recently was at your
[4170.58 --> 4176.82]  conference jared any js conf there in uh in omaha nebraska which was super awesome so we've got
[4176.82 --> 4183.26]  four seasons in the can we're about to launch beyondcode.tv which if you're listening to this
[4183.26 --> 4189.40]  right now you can go there now beyondcode.tv check it out it's probably days launched so if
[4189.40 --> 4194.28]  there's anything any issues you see report them on github it's open source on github find a link on
[4194.28 --> 4199.18]  the site i'm sure we'll link out to to uh the github repo because it'll be there so if you find bugs
[4199.18 --> 4205.34]  let us know uh and as jared mentioned also we have been producing change all weekly our weekly email
[4205.34 --> 4212.44]  using middleman for quite a while and uh thomas you mentioned your affinity for rake and that's how you
[4212.44 --> 4218.44]  kind of got into rubia early on uh a lot of change all weekly is a big old rake task that works with
[4218.44 --> 4225.08]  the trello api to allow us to use trello as a cms so we've been using middleman in some unique ways
[4225.08 --> 4233.96]  uh and and obviously raking in some ways as well to to boost both those sites um that's cool but uh
[4233.96 --> 4239.10]  i want to say that before we close the show so thomas thanks for so much for coming on the show i mean
[4239.10 --> 4243.84]  whether you know it or not uh we've wanted to have you on the show for quite a while because
[4243.84 --> 4248.42]  we've had this you know love affair with your software for a bit and it just would make sense
[4248.42 --> 4253.48]  to get you on the show and talk about what you've been doing and version four coming out and and a bit
[4253.48 --> 4257.58]  of your history and software development open source uh is there anything that we missed anything you
[4257.58 --> 4263.70]  want to say in closing before we wrap up the show no it's been great thanks for having me um i'm glad
[4263.70 --> 4268.74]  i haven't given you too many heartaches that's my number one fear is someone out there is cursing
[4268.74 --> 4273.20]  my name at all points in time as you get popular so i'm glad it's been good for you guys and um
[4273.20 --> 4277.38]  hit me up if you ever need anything awesome well thomas thanks so much for joining us on the show
[4277.38 --> 4282.94]  to everyone listening thanks so much i mentioned beyondcode.tv check that out you find any bugs or
[4282.94 --> 4288.20]  anything like that let us know hit us up on get up for that uh also changelog weekly that's a weekly
[4288.20 --> 4293.40]  email we ship out every saturday it it covers everything that jared and i and the rest of the team
[4293.40 --> 4299.22]  finds in open source every week everything from our latest episodes to the most cool headlines and
[4299.22 --> 4306.24]  links and repos that we find ourselves as well as our ping repo so jared we have uh a ping repo as you
[4306.24 --> 4311.30]  know on github that we tell everybody to submit things to so if you find something cool check out
[4311.30 --> 4317.62]  our ping repo it's slash change slash the changelog slash ping um submit something there to the issues
[4317.62 --> 4325.04]  we'll link it up in the weekly email and uh boom we'll go with the dynamite so changelog.com slash
[4325.04 --> 4331.68]  weekly until next week um we will say goodbye for now and i won't step on my foot today because
[4331.68 --> 4336.24]  because uh not knowing who the guest is next week i'm just not going to say it at all so
[4336.24 --> 4341.74]  we'll leave the show there we'll say goodbye now see ya thanks thomas take care
[4341.74 --> 4352.90]  you
[4352.90 --> 4353.70]  so
[4353.70 --> 4359.18]  you
[4359.18 --> 4359.70]  you
[4371.74 --> 4401.72]  Thank you.
