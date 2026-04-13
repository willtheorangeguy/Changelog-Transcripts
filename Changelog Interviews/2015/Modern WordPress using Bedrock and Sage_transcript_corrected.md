[0.00 → 16.16] welcome back everyone this is the changelog and I'm your host Adam Staravia this is episode 156
[16.16 → 21.70] and on today's show we're joined by Ben word and Scott Waukesha to talk about WordPress and
[21.70 → 26.64] more specifically Ben and Scott are from roots that's the organization that created bedrock
[26.64 → 33.04] and sage bedrock is a modern WordPress stack and sage is an awesome WordPress starter theme
[33.04 → 37.80] great conversation today with these two guys talking about WordPress and all sorts of stuff so
[37.80 → 45.14] stay tuned got three awesome sponsors code ship top towel and code school we'll tell you a bit more
[45.14 → 50.82] about top towel and code school but our first sponsor code ship is a hosted continuous delivery
[50.82 → 56.40] service focusing on speed security and customizability you can set up continuous integration
[56.40 → 60.94] for your app in a matter of seconds and automatically deploy when your tests have passed
[60.94 → 65.98] code ship supports your GitHub and your Bitbucket projects, and you can get started today with
[65.98 → 71.44] code ship's free plan should you decide to go with a premium plan you can save 20 off any plan you
[71.44 → 77.56] choose for three months by using this code the changelog podcast again that code is the changelog
[77.56 → 83.26] podcast head to code ship.com slash the changelog to get started and now on to the show
[83.26 → 90.20] all right everybody we're back this is Adam I'm joined by Ben word and Scott Wilkinson
[90.20 → 98.80] I think I poisoned you did this Scott you did that walking Shaw I'm going to leave that we're gonna
[98.80 → 103.20] we're going to leave that one in there because in the pre-call we were talking about Scott's last name
[103.20 → 107.82] and my last name because they're both above nine letters and Scott was saying how he gets called
[107.82 → 112.14] Wilkinson all the time or Wilkinson or something like that and I said there's no, no end at the end
[112.14 → 116.86] and he poisoned me so he got uh walking sin instead of walking Shaw so sorry about that Scott
[116.86 → 125.90] no problem um so you guys run this project called roots and around WordPress a lot of fun stuff you
[125.90 → 131.14] know a lot of people are sort of haters I guess to a degree on WordPress and uh mostly it comes with
[131.14 → 138.76] like a database and everybody loves Jekyll and no database and flat files and stuff um, but you know
[138.76 → 145.06] the changelog we use WordPress to run the changelog it's got obviously it's got multi-author all that
[145.06 → 151.30] fun stuff so we love WordPress to a degree, and we might get into some of that in this show and I'm sure
[151.30 → 156.20] you can probably both say the same thing that you love WordPress to a degree as well would you do
[156.20 → 162.96] agree with that yeah for sure so let's lets uh get some introductions out of the way Ben let's
[162.96 → 170.04] start with you who are you to roots and uh all the good stuff uh I am the creator and lead developer
[170.04 → 177.52] of roots I started working with WordPress back in 2004 uh I've been making themes for about the same
[177.52 → 184.72] time uh roots started because I worked at basically a website factory where I was pumping out a bunch
[184.72 → 190.56] of sites every day and I just wanted to stop repeating myself so roots was born and then the
[190.56 → 197.50] other projects came along further down the line what about you Scott sure um my involvement in roots
[197.50 → 204.00] started when soon after Ben started it he often needed some more complex PHP help uh since he's more
[204.00 → 209.64] of a front-end guy so us knowing each other before that he would always ask me for PHP help so I've been
[209.64 → 214.24] involved pretty much from the start but I mean started off in a more kind of unofficial just helping
[214.24 → 219.84] behind the scenes um as we started to get more popular I got more involved um that was with the
[219.84 → 225.58] roots theme itself over the years and then recently that's resulted in kind of projects that I've
[225.58 → 232.62] started such as bedrock, and it's kind of sister project bedrock Ansible when you go to roots.io right
[232.62 → 240.10] now the main headline you see is roots helps you build better WordPress sites faster uh it started
[240.10 → 246.98] out with roots was uh was originally a starter theme right Ben right, and then it's sort of this project
[246.98 → 253.26] has morphed as Scott came on and others will mention has come on Austin nick and Chris now it's sage now
[253.26 → 258.34] it's bedrock maybe let's start back at the beginning I think even in the pre-call you mentioned that you
[258.34 → 265.26] and Scott got introduced together through your passion for Call of Duty is that correct yeah we uh we used to
[265.26 → 272.04] run Call of Duty gaming tournaments for the pc version uh it was called survival of the fittest and
[272.04 → 279.04] I actually met scot the uh he jacketed me offline that was my first interaction with Scott Waukesha
[279.04 → 285.30] was him taking me offline um so there's that that's how I met Scott what does that mean taking you offline
[285.30 → 294.60] uh you know DDoSing Scott DDoS'd be yeah that's not nice Scott yeah yeah we were young it was back in uh
[294.60 → 300.96] 2003 I think okay so this is okay this is a while ago okay yeah so you guys have been you guys been
[300.96 → 306.88] doing some stuff together for a while yeah all right well let's go back to the beginning than I guess to
[306.88 → 314.18] a degree um more so with roots than I guess like maybe what was some of your early relationships was
[314.18 → 320.28] it around WordPress have you been using WordPress since I guess it was born in around 2004 2005 wasn't it
[320.28 → 326.52] uh roots well roots wasn't really born until 2009 well not really but WordPress WordPress was
[326.52 → 333.16] how old is WordPress you know WordPress is pretty old I want to say that WordPress is older than 2004
[333.16 → 340.04] for sure I first started using it around 2003 late uh 2004 was when I first started using it and I think
[340.04 → 346.92] it was between that and gray matter way way way back when I mean this is forever ago yeah I think that's
[346.92 → 351.90] like when they finally started implementing more cms type features, and it was moving away from just
[351.90 → 359.68] WordPress used for blogging pages was a hack basically right yeah all that yeah oh man what back in
[359.68 → 365.54] the day okay so I guess where did roots come from what you said that you were working at a consultancy is
[365.54 → 372.44] that right I was working for an agency uh in Colorado and man they just pump out sites like it's
[372.44 → 379.32] nothing it's basically a website factory so I would get templates throughout the day that I had to
[379.32 → 388.12] turn into WordPress themes basically and I was working um I want to say html5 boilerplate wasn't yet
[388.12 → 394.92] the official name of the project it was called frontend pro template so I took that from Paul Irish and
[394.92 → 402.12] I just threw blueprint CSS on top of it and then from there it just kind of evolved into more things like i
[402.12 → 407.48] added more things on it more specific to my use case for having to pump out like client sites
[407.48 → 415.68] three times a day um so roots also kind of had this reputation early on for being bloated and too
[415.68 → 422.46] opinionated and that's not really the case anymore like if you look at sage nowadays it's very lean it's
[422.46 → 430.78] very minimal it uses dependency managers and the actual amount of code in the theme I think it's like 600
[430.78 → 436.28] lines when you compare that to some of the other starter themes out there like it's very clear that
[436.28 → 444.72] sage is not a real bloated tool, so roots was the starter point which then became sage right so
[444.72 → 449.66] have you had some issues with the naming by any chance yeah, so the naming got a little weird once
[449.66 → 454.10] we introduced bedrock because it's like all right we've got the roots theme, and then we've got bedrock
[454.10 → 459.84] like this is getting confusing people started referring to the project as like roots.io once we got that
[459.84 → 467.82] domain name so I mean it just made sense to stop calling the theme roots and call it its own project
[467.82 → 473.38] name that is going to avoid confusion in the future like roots should just be known as the organization
[473.38 → 480.66] gotcha yeah that started when we actually got the roots' organization username on GitHub and at that
[480.66 → 486.62] point it was you know root slash roots for the theme and I mean it was over a period of months we went
[486.62 → 491.64] back and forth on kind of how to solve the branding issue, and we didn't really want to rename the theme
[491.64 → 496.76] because it's difficult when there's documentation all across the internet there are blogs about it there's
[496.76 → 502.58] stack overflow questions, and we knew it was going to be hard but at the end of the day I mean it was
[502.58 → 505.84] the right decision to make so how long ago was that because I remember when I first got introduced to
[505.84 → 510.72] if it was about a year and a half ago I want to say and I thought okay it's roots and then
[510.72 → 515.40] bed rocked and that was clear to me and then uh you know during the last year and a half has
[515.40 → 519.50] progressed as I've gone back to it again to reference it back to our team because I worked at a
[519.50 → 525.74] a non-profit called pure charity and one part of our I guess a little sneak peek into their business
[525.74 → 532.02] model is to leverage open source in a way that can help them uh build non-profit sites really easy
[532.02 → 536.66] because they're using WordPress you know open source plugins open source themes as you all know
[536.66 → 542.68] which is uh has been the way to go, and so we were starting to use WordPress more and more and tie
[542.68 → 549.76] back into our rails API uh to pull sort of data out of uh of this you know sort of larger site but uh
[549.76 → 554.60] long story short as I was as I went back to i was like what is this sage thing and so as somebody who
[554.60 → 561.50] came to it post the rename I was maybe twice as confused I was like so it changed I guess it was easy
[561.50 → 568.14] to replace my mind that it had changed but for a bit there I was like what's up with that yeah so
[568.14 → 573.48] we uh we renamed the theme from roots to sage with version 8 which came out at the end of February
[573.48 → 579.56] this year so it's a pretty recent change right okay um and yeah like we had discussed it
[579.56 → 587.34] internally before that, and we had come up with the name sage before version 8 and made it public uh I want
[587.34 → 592.08] to say a few weeks beforehand just to give people a heads-up but yeah I mean it's still a little bit
[592.08 → 597.10] confusing just because people associate roots with just the starter theme while we're in the
[597.10 → 601.60] clarification moment here uh could one of you break down sage and one of you break down bedrock
[601.60 → 608.40] for the listeners okay, so sage is a WordPress starter theme as in like you're going to start a new
[608.40 → 615.06] project, and you have you want to start from scratch with um your front-end templates and your CSS and your
[615.06 → 622.24] Jason all that you use sage to build your theme um it uses a theme wrapper which is a non-conventional
[622.24 → 629.60] WordPress thing um it's a don't repeat yourself method that a lot of people outside the WordPress
[629.60 → 637.26] world are familiar with um it also uses gulp uh for the build process we use bower to bring in front-end
[637.26 → 644.72] packages and bootstrap is the default um CSS framework that's included, but you shouldn't limit
[644.72 → 649.92] yourself uh to not using sage if you don't use bootstrap it takes literally three seconds to
[649.92 → 655.86] remove or replace with something else all right and maybe uh Scott you want to take bedrock
[655.86 → 662.32] yeah for sure so I wish I had a better history kind of how it started um it spun off from when we were
[662.32 → 668.72] recreating roots.io I come from the rails world and although it's not the best framework out there I'm
[668.72 → 673.66] not arguing that one of the things that has going for it is its whole uh convention over configuration
[673.66 → 679.76] and my experience of word with rails is you know it has a very well-defined folder structure
[679.76 → 683.84] it makes sense it's logical, and you know where things are that's basically the complete opposite
[683.84 → 689.46] of WordPress by default if you look in a typical WordPress project like if you download WordPress
[689.46 → 695.32] itself from their official website you'll get all a bunch of files mixed in the root which is the
[695.32 → 700.66] WordPress core and then there's an actual folder called you know content that contains plugins
[700.66 → 708.48] themes and so on, so the whole theory behind bedrock was give WordPress better structure and organization
[708.48 → 713.96] um so we refer to it as kind of WordPress stack which isn't the best term, but it was borrowed from
[713.96 → 718.66] one of the WordPress core team members mark Asquith and I hope I'm saying his name correctly
[718.66 → 723.76] uh he had two projects one called WordPress skeleton and one called uh WordPress stack
[723.76 → 731.20] WordPress skeleton was just a model of how do you how the WordPress core fits in its own subdirectory
[731.20 → 736.68] so instead of mixing that in the root folder it has its own subdirectory called WordPress or
[736.68 → 740.98] WordPress core whatever you want to call it, and he managed that as a git submodule
[740.98 → 747.92] git submodules aren't ideal so we switched to using composer it's the official PHP dependency
[747.92 → 753.28] package manager um so that's the two main things about bedrock is it gives you
[753.28 → 758.22] a better folder structure, and it uses composer for dependencies and those dependencies include
[758.22 → 765.46] the WordPress core itself and any plugins that you're going to add the folder structure I think
[765.46 → 769.68] maybe let's pause there on that mention because uh when we're talking about bedrock
[769.68 → 777.68] I guess who who says I know you said here but who else complains about the folder structure of
[777.68 → 783.22] WordPress because when i use WordPress I almost don't really care about I guess to a degree
[783.22 → 788.16] what WordPress itself is doing i just sort of care about my theme is that the consensus with most of
[788.16 → 791.96] the people you're working with when it comes to bedrock and the problems you're trying to solve
[791.96 → 795.72] um yeah well the other thing I should have introduced with bedrock is i kind of
[795.72 → 801.46] created it with uh teams in mind you know if you just have your own personal blog, or you're spinning off
[801.46 → 805.24] quick sites like Ben mentioned if you're kind of working at one of those agencies that does quick
[805.24 → 809.82] things and passes them off to a client it's not necessarily the best project to use but if you have a
[809.82 → 814.60] longer running more serious project where you might have multiple team members, and you know it's
[814.60 → 820.20] going to be kind of like a cms for your website for you know years to come um it's more important
[820.20 → 825.48] that you get into proper dependency management and if you keep WordPress's default folder structure
[825.48 → 830.82] it's really difficult to do that um and I mean you asked like is this a known problem do people
[830.82 → 836.08] complain, and they definitely do um I mean on the main WordPress uh documentation there's a whole
[836.08 → 840.84] article uh article about giving WordPress its own subdirectory and this has been around for
[840.84 → 845.92] years and years it's not common or sorry it's not new um and there are projects that existed like
[845.92 → 853.22] WP skeleton I guess I'm just not privy to this i so maybe um I don't want to I think let's start
[853.22 → 857.60] with bedrock then so I got some questions initially out of there I mean I think sure I'm interested in
[857.60 → 863.84] the sage but I think it's solving some pretty well-known problems that I think we'll dig into but when it
[863.84 → 867.88] comes to this folder structure can you break down can you like I know it's difficult without like a
[867.88 → 871.98] whiteboard in front of us but could you break down what that folder structure might be like
[871.98 → 879.02] you know can you describe it yeah I think I can so the very first thing that bedrock does is there
[879.02 → 884.88] there's a configuration there's a folder called config that contains the actual WordPress config files
[884.88 → 890.46] and then there's a top-level folder called web and so when you're setting up Apache or nginx and you
[890.46 → 894.58] you know you have to create your virtual site you have to set your document root to a folder
[894.58 → 900.64] usually you set it to just your WordPress root folder in this case we set it to the web folder
[900.64 → 906.76] so that you can securely keep configuration files a level above it so they can't be accessed publicly
[906.76 → 912.30] and you don't need to go through and kind of blacklist like individual files like you'll often see people
[912.30 → 919.30] say um oh I want to deny access to a dot git folder so one of the advantages with a top-level web folder
[919.30 → 924.42] is that's already taken care of automatically okay, so there's a there's a config folder
[924.42 → 932.40] and a top-level web folder and then there's also a vendor folder and that's where your composer
[932.40 → 936.92] dependencies are so what kind of things would go in there what kind of what is what are some of
[936.92 → 942.48] the things you see composer being installing for people that are dependencies sure well that's where
[942.48 → 945.88] it gets a little confusing is there are a couple kinds of dependencies on a WordPress project
[945.88 → 951.94] there's the WordPress core itself so that you have to kind of have a special rule that say hey install
[951.94 → 957.16] this it needs to be at the same level um it's in your web folder right yeah it's got to be one level
[957.16 → 962.08] they hard code it they say it has to either be at the same level as your config file which is
[962.08 → 967.38] everyone's used to configure modifying, or it has to be one level up so we take advantage of the one
[967.38 → 973.08] level up rule so in bedrock you have a folder called WP that's what we call it the nice thing is
[973.08 → 977.34] that you can delete that entire folder whenever you want and just rerun composer install, and it will
[977.34 → 983.26] regenerate it you can bump a version number so you know WordPress 4022 just comes out all you have to
[983.26 → 991.08] do is do composer update and the version number, and it will redownload that so um, so this is the WP
[991.08 → 995.66] folder at the same level as the web folder or is it an is it in the is it a child to the web folder
[995.66 → 1004.02] the WP folder is inside the web folder okay yeah gotcha okay and then uh yeah sorry just what Ben
[1004.02 → 1009.80] said and um so that like I'll get back to this a couple kinds of dependencies there is the core itself
[1009.80 → 1015.90] there's WordPress plugins and as you know WordPress plugins have to go in your WP content folder you
[1015.90 → 1020.78] know there are a plugins folder there's also your must-use plugins um, so there are also some special cases
[1020.78 → 1027.16] where if those package types are set to you know WordPress plugin we tell it install in this folder
[1027.16 → 1031.88] now the nice thing about composer is if let's say you have a theme, and you want to take advantage
[1031.88 → 1038.04] of trying to think of a really popular PHP package off the top of my head some other emulating
[1038.04 → 1042.18] language like I don't know if you've heard of moustache it's a popular emulating language yeah um
[1042.18 → 1048.00] so frequently if or in the past if a WordPress theme wanted to use moustache you would have to what we
[1048.00 → 1053.16] call vendor that whole library inside your theme so you'd have to download the whole moustache library
[1053.16 → 1058.44] embed it in your theme and commit it to the source code source repository and whenever you want to
[1058.44 → 1063.44] update that you need to pull in all their files and update it with this way you can say hey I've got a
[1063.44 → 1068.04] dependency on moustache and composer will handle all the downloading, and we'll stick it in this vendor
[1068.04 → 1073.00] folder and that every team member who kind of downloads it will have the exact same version
[1073.00 → 1079.72] you can recreate stuff from scratch, and you don't have to kind of pollute your own say git repository
[1079.72 → 1084.96] yes all this third-party code okay I'm feeling it now I'm now I'm getting the better folder structure
[1084.96 → 1089.18] that you're saying there because this is starting to make a lot more sense now it's a little hard to
[1089.18 → 1094.36] describe uh you know just over audio yeah obviously people are encouraged to go and uh check it out
[1094.36 → 1098.56] right in our GitHub repo, and you will be able to see exactly what we're talking about and the repo you're
[1098.56 → 1106.16] talking about is like a bedrock Cristiano or no it's just GitHub.com slash root slash bedrock
[1106.16 → 1112.56] okay, okay gotcha I'm following along so you got config you got scripts in there you got vendor you got web
[1112.56 → 1119.76] yeah and if you look in web you'll start to see the kind of more normal uh WordPress folder structure
[1119.76 → 1125.08] that you're used to although one little thing that I should mention is typically you have that content
[1125.08 → 1130.22] folder we've renamed that to just app and that might sound like you know why are we doing that
[1130.22 → 1135.58] it's just confusing it's for two reasons uh one we kind of want to get across that it contains your
[1135.58 → 1141.94] application code, and we're trying to take WordPress on a kind of higher level as a cms versus just
[1141.94 → 1148.28] um you know the blog yeah and it more mirrors um a lot of the other frameworks that exist things like rails
[1148.28 → 1153.82] and I believe even symphony in the PHP world um it more mirrors the expectations of existing
[1153.82 → 1157.92] frameworks that people are used to yeah so that's why we do that yeah looking at this I'm seeing the
[1157.92 → 1163.50] index file the in this case WP config because that's probably a naming convention that just
[1163.50 → 1168.16] you have to adopt from where you can't just change it to config because that's not what they want
[1168.16 → 1172.22] and then you're seeing the app folder which inside the app folder you've got things like your plugins
[1172.22 → 1178.10] your themes your uploads which is actually your site your real the real thing pretty much yeah
[1178.10 → 1184.48] the app folder is the WP content folder right yep what about uploads then I'm seeing uploads in
[1184.48 → 1191.48] here and I'm wondering that seems more like maybe it doesn't fit I guess to a degree it do I guess
[1191.48 → 1197.16] it is I mean yeah that's the standard uploads folder that would exist under WP content I mean we just
[1197.16 → 1202.72] added in there um because WordPress expects it exists although I think it will just be created uh if not
[1202.72 → 1207.96] so earlier before we got started on the call I asked you guys what would be something
[1207.96 → 1213.00] I can ask you um and maybe this is a good time to bring it out because it seems like you've done
[1213.00 → 1220.40] so much restructuring of like vanilla WordPress I guess one question is how well does WordPress
[1220.40 → 1224.88] support setting a variable for like here's where you find this here's where you find that now because
[1224.88 → 1229.40] moving these things around you've got to do that somehow um yeah so I'm thinking like when you do
[1229.40 → 1234.84] automatic installs you know you don't want to lose that great feature from WordPress so when you do
[1234.84 → 1239.50] installations WordPress has got to know where to put things uh how difficult is that to overcome
[1239.50 → 1245.46] so I'll address a few of those points um the creation of kind of bedrock involved a lot of
[1245.46 → 1252.08] a lot of trial and error like figuring out what WordPress supports how to work around things so it is
[1252.08 → 1258.42] definitely took a little while to learn and figure out um what it allowed what it didn't allow
[1258.42 → 1264.94] uh you know things that are hard coded like I mentioned they expect the um the config file and
[1264.94 → 1271.48] the WordPress core folder to be at relative like levels, and they don't you can't break that but now
[1271.48 → 1276.82] that it is set up it works just like a normal WordPress site I mean WordPress has constants that
[1276.82 → 1281.78] let you define where certain folders live where what certain URLs are going to be and because we've set
[1281.78 → 1287.22] those up you know we've done kind of the hard work for people it works perfectly fine with WordPress
[1287.22 → 1293.00] itself uh the kind of good or bad thing you could say about bedrock is occasionally we'll get people
[1293.00 → 1297.52] who come over and create an issue, and they say hey bedrock doesn't work with this plugin or this theme
[1297.52 → 1301.92] and right away we know that's because that theme or plugin is doing something they shouldn't be doing
[1301.92 → 1308.64] and that's because they're referencing a hard-coded path or URL when they should be using the either
[1308.64 → 1314.84] those like constants uh functions that WordPress provides to get the correct path or location to those
[1314.84 → 1320.78] things yeah it's real obvious to tell when plugins are doing things I guess the wrong way um for
[1320.78 → 1328.64] instance they'll try and load a core file and expect a specific path for someone's WordPress installation
[1328.64 → 1333.48] not even accounting for the fact that WordPress could be installed in the subdirectory no matter what
[1333.48 → 1338.44] so it's not even necessarily like an issue with bedrock it's just an issue with the way that
[1338.44 → 1344.80] someone was writing that plugin or theme yeah I wonder how difficult has it been to get some of
[1344.80 → 1351.06] those uh plugins updated not so much you guys doing it, but you know identifying that that's the issue
[1351.06 → 1356.64] and then you know the fact that WordPress plugins aren't hosted on GitHub so they're not quite the
[1356.64 → 1361.30] GitHub flow that everybody's used to um how difficult is it to like sort of reach out to those authors
[1361.30 → 1366.82] and maintainers and get those updates in place you know we don't actually really reach out to those
[1366.82 → 1372.70] plugin authors normally it'll usually be a situation where someone posts on our discourse saying like
[1372.70 → 1377.74] oh hey this is broken one of us will go in there and see what's happening like the plugins trying to
[1377.74 → 1386.44] load um wp-load.php directly um expecting a certain path at that point we just tell the user hey you know
[1386.44 → 1391.62] the plugins doing it wrong here are some resources showing why they're doing it wrong um there's already
[1391.62 → 1396.62] been like core contributors that have written blog posts on the subject as to like why these things break
[1396.62 → 1402.46] so it's easy to just reference them uh reference those blog posts to them, and then they can go and
[1402.46 → 1407.62] you know tell the plugin author who will hopefully get their act together all right lets uh let's
[1407.62 → 1412.08] talk about who bedrock is for because I'm thinking I've got a good friend who's probably listening to
[1412.08 → 1417.48] this and uh whenever I think about WordPress and getting even more advanced with WordPress i always
[1417.48 → 1422.32] think about this fella uh hi be nit's not the Ben word on the call it's the other bent hat's
[1422.32 → 1428.04] my friend but um I know he listens he's going to listen to the show because why wouldn't he um but
[1428.04 → 1434.68] he's who I think about when I think about WordPress and getting more advanced with it like who is going
[1434.68 → 1440.26] to use bedrock is it somebody who's familiar with the command line like what kind of developer is going
[1440.26 → 1448.22] to care about bedrock and what it does for WordPress it definitely caters to a more advanced WordPress
[1448.22 → 1454.64] developer one of the things about bedrock right off the bat is that it's a little harder to get set up
[1454.64 → 1459.70] on shared hosting for example if you're not using composer or bedrock in my opinion there's not much
[1459.70 → 1465.34] reason in using bedrock you can just use a normal WordPress uh subdirectory install or just a normal
[1465.34 → 1471.36] WordPress install um so right off the bat that kind of limits people it's almost it almost acts like a
[1471.36 → 1476.02] filter so composer if you're not using composer you don't want to use bedrock is that what you said yeah i
[1476.02 → 1481.38] mean they're that's the primary reason for kind of bedrock existing if you don't want like the
[1481.38 → 1486.60] dependency management then you know you can still get some of the advantages of the better folder
[1486.60 → 1493.92] structure in my opinion, but you can use other projects the deployment process the deployment process
[1493.92 → 1501.36] is again something that some people may not be used to a lot of people may use to just be ftping over
[1501.36 → 1509.40] files or r syncing or some a lot of um there are projects that just do like a straight git deployment
[1509.40 → 1515.42] and the main step that you need in a bedrock deployment the one internal WordPress site is
[1515.42 → 1519.96] that composer part of it so basically you need to ship your code off to the server somehow you can do
[1519.96 → 1525.90] that via git FDP SCP doesn't really matter, but the main part is that you need to run composer
[1525.90 → 1532.32] install after that to get those newest dependencies and packages and WordPress core and plugins
[1532.32 → 1539.36] so talking about um we got there by asking which is who is this for so it seems like
[1539.36 → 1545.18] somebody who's uh, and you know it's your to your credit Scott you came from a rail world where
[1545.18 → 1551.54] you know you've got Cristiano which you're using here and Cristiano is still ruby project, but it's
[1551.54 → 1555.82] usable by anything you know as long as you can run ruby locally or in your on your server so that's not a
[1555.82 → 1562.84] problem but as a rails' developer uh you're probably more fluent with those types of ways whereas those
[1562.84 → 1568.70] who live in the WordPress world aren't that privy to you know like command line deployments like
[1568.70 → 1575.18] Heroku might offer things like that so I'm wondering how big of a hurdle that is to get over like how
[1575.18 → 1581.42] what's the adoption of bedrock I guess your your your deeper developers are probably like yes this is
[1581.42 → 1587.66] awesome but even those who you might consider advanced WordPress users are still not quite
[1587.66 → 1595.94] command line users yeah well just quickly going back to kind of who uses it um and i it was designed
[1595.94 → 1601.18] for um teams and more professionals versus just someone you know creating a blog like I mentioned
[1601.18 → 1606.12] or maybe a freelancer who creates a lot of sites really quickly and then passes them off to a client
[1606.12 → 1611.08] you can still do that it's not for them, it's not okay it wasn't designed for them, but it can
[1611.08 → 1617.06] certainly still be used in any way um so obviously right there you've you know you've kind of limited
[1617.06 → 1623.52] your market if you will to a smaller subset and so, but we still see a wide range of people I mean
[1623.52 → 1630.16] some people on the core uh roots team I think we might talk about later on a lot of them came in and
[1630.16 → 1634.86] use bedrock for different things some of them are freelancers some people just appreciate um the structure
[1634.86 → 1639.86] and kind of how it takes it to an I'll say a more kind of rigorous or professional level with the
[1639.86 → 1646.32] dependency management and I definitely know of a lot of um I can say you know companies who have
[1646.32 → 1650.68] multiple developers working on long-term projects that's that's where you get the most
[1650.68 → 1656.20] advantages of it so pick your companies who've got an installation in place they don't plan on moving away
[1656.20 → 1661.00] from WordPress they have a team that's doing it they have developers who are willing to go the extra
[1661.00 → 1666.28] mile and let's say learn to learn how to use the command if they're not currently using it they're
[1666.28 → 1671.58] willing to take those extra steps to have a better team management and bedrock is really developed for
[1671.58 → 1677.66] that kind of team yeah definitely it's also perfect even if you're just working individually I mean
[1677.66 → 1682.60] because no matter what you're going to be working on your code, and it's going to be in a git repository
[1682.60 → 1687.52] right, and you don't want to be checking in the entire WordPress install into the git repository
[1687.52 → 1693.38] or any other dependencies or plugins it's much nicer to be using bedrock to pull on all those
[1693.38 → 1700.28] things just to not have that that code in your repo and then um as far as deployments go um I mean
[1700.28 → 1705.86] there's probably a lot of people that are using bedrock that aren't using one of the deployment
[1705.86 → 1712.16] methods that we offer um other than then just Cristiano we actually have Ansible based deploys as well
[1712.16 → 1720.30] and I mean take deploys completely out of the picture bedrock is still really useful to use as
[1720.30 → 1725.92] your WordPress stack you could have a completely different deployment method it could just be git
[1725.92 → 1732.40] based um you could use something like Laravel forge um I know people that use even like deploy HQ
[1732.40 → 1738.00] there are a lot of different ways you could deploy your site, but the bedrock project structure is
[1738.00 → 1742.98] probably the biggest advantage in my opinion I think we need to move the better folder structure
[1742.98 → 1749.84] uh feature up one bullet point yeah I feel like I feel like that's where the biggest
[1749.84 → 1758.74] gain is and then uh opt in to composer opt in to deployments uh is but I'm speaking out of turn
[1758.74 → 1764.04] because I'm still discovering with you guys but uh since you mentioned Ben uh deployments let's take a
[1764.04 → 1768.10] quick break but when we come back we're going to talk about deployments because that's a deep subject
[1768.10 → 1772.90] uh for me for sure and for anybody who develops WordPress sites so let's take a quick break
[1772.90 → 1774.94] and we'll come back and talk about deployments
[1774.94 → 1782.80] top tile is by far the best place to work as a freelance software developer I had a chance to sit
[1782.80 → 1788.30] down on top of Brendan banished the co-founder and coo of top tile and I asked Brendan to share some
[1788.30 → 1793.86] details about the foundation of top tile what makes top tile different and what makes their
[1793.86 → 1799.56] network of elite engineers so strong take a listen I mean I'm one of the co-founders and
[1799.56 → 1805.60] I'm an engineer um I studied chemical engineering and to pay for this super expensive degree I was
[1805.60 → 1810.64] freelancing as a software developer then by the time I finished realized that being a software
[1810.64 → 1817.08] developer was pretty awesome, and so I kept doing that, and my co-founder is in a similar situation as
[1817.08 → 1823.16] well, and so we wanted to solve a problem as engineers and do it from as a network of engineers
[1823.16 → 1830.10] kind of for engineers by engineers and having that perspective and consistently bringing
[1830.10 → 1836.20] on new team members who also share this really makes top tile different and that it's a network
[1836.20 → 1842.04] of engineers not kind of like you have top tile and then the developers it's never about us and
[1842.04 → 1847.42] them it's its always us like everybody at top tile for the most part refers to top tile as their
[1847.42 → 1850.88] company, and they feel like it's their company and everybody acts like a core team member
[1850.88 → 1856.06] even though they're freelancers within the top tile network and all of these things are extremely
[1856.06 → 1860.62] important to us all right if you're interested in learning more about what top tile is all about
[1860.62 → 1868.70] head to toptal.com slash developers that's t-o-p-t-a-l.com slash developers to learn more
[1868.70 → 1871.30] and make sure you tell them the changelog sent you
[1871.30 → 1878.64] all right we're back so deployments let's since we just talked about sort of the bullet pointed
[1878.64 → 1884.76] feature of better folder structure seems like that's the biggest win for bedrock and composers
[1884.76 → 1891.62] are nice to have for the developers who care about those things which I think a lot of people do care
[1891.62 → 1896.38] about them but to some people it's just like dependencies what are those um because that's
[1896.38 → 1900.92] more I think it's getting into your more modern developer and I'm not saying that we shouldn't
[1900.92 → 1906.70] strive to be modern developers, but some are just fine with being the old way some are fine with ftp
[1906.70 → 1915.94] you know and that's not wrong um because it works right I mean ftp is wrong I mean I'm not saying
[1915.94 → 1923.50] it's right in quotes but I mean if it works then it works right I'd go one step higher than you and
[1923.50 → 1930.44] I'd say for example you user sync i I would for that I would concede that it works it's fine ftp though
[1930.44 → 1936.78] I wouldn't any okay uh you got some of those developers out there who's just like you know
[1936.78 → 1942.72] what I'm not interested in the command line uh I got this thing here I drag and drop and boom goes
[1942.72 → 1948.44] dynamite oh I mean we're not we're not kind of ignorant of those people that exist because
[1948.44 → 1953.48] they find ourselves to our projects I mean we'll find them in our GitHub issues on our forum
[1953.48 → 1960.26] um we write blog posts, and we've written we've made screencasts to kind of educate and teach people
[1960.26 → 1965.86] how to use these more advanced topics so I mean we realize that there's people who are at kind of
[1965.86 → 1972.24] all levels of the WordPress kind of developer spectrum from people who either don't know about
[1972.24 → 1976.88] these things or do know and don't know why they're important or why they should be doing them
[1976.88 → 1982.64] or you know there's people who don't care and that's fine too right well you mentioned there Scott that
[1982.64 → 1988.30] uh you left a little cat out of the bag so here at the change law we use WordPress to run our site
[1988.30 → 1995.12] uh we like if it's great uh every time we've tried to move away from if it's pulled us right back and
[1995.12 → 2000.22] said you're just trying to rebuild me in some of the language and that's crazy so just keep me
[2000.86 → 2008.18] WordPress actually whispers those words to us, you know, and we deploy via our sync uh we use gulp
[2008.18 → 2014.84] we could use rake and i actually I'll put my hand up and I'll say it i I wanted to try it a cooler way
[2014.84 → 2023.32] I took my existing rake task that worked just fine to sync my theme only up to my server and then i
[2023.32 → 2027.20] changed it to use gulp so that's the only thing I use with gulp that I think and some other things but i
[2027.20 → 2033.98] I could definitely use it uh do review with it, so rake tasks are just fine too um but I'm a fan of
[2033.98 → 2039.10] finding a better way to deploy I knew that ftp didn't work for me, it works for some people it
[2039.10 → 2044.66] doesn't work for me um so I knew I wanted to do one thing I could, you know do SCP to do it I could
[2044.66 → 2050.92] use RC to do it I just figured I'm not that worried about it, I'm a one person you know jarred helps me
[2050.92 → 2056.48] with our stuff but not with WordPress you know not because he doesn't want to just because like
[2056.48 → 2061.96] he's better at other things so I pretty much take care of all that so being the only person who does
[2061.96 → 2066.62] design and development on our WordPress site I figured okay it's fine with just doing you know
[2066.62 → 2073.30] grunt deploy and dealing with it like that so at what does bedrock do above and beyond
[2073.30 → 2079.70] that kind of scenario so when bedrock was first created I mean the main thing to do with deployments
[2079.70 → 2085.28] was we kind of had Cristiano built in so again like you know I had rails experience and ruby it
[2085.28 → 2089.26] wasn't a big deal to me, you know I have ruby locally I've worked in other sites with Cristiano
[2089.26 → 2096.20] so what that meant was we just had Cristiano configs in the project that had the necessary
[2096.20 → 2101.34] settings to work kind of out of the box with bedrock, and we had documentation you know on how
[2101.34 → 2107.26] to get started with Cristiano and how to deploy and I mean really the only thing that was that you
[2107.26 → 2112.52] needed to add on to the default Cristiano deployment workflow was running composer which
[2112.52 → 2117.94] as I mentioned before is pretty much that only necessary step beyond just getting the code onto a
[2117.94 → 2123.32] remote server so that existed in bedrock for a long time, and we still support if it's actually
[2123.32 → 2129.32] been moved to another repository right now it's at root slash bedrock dash Cristiano and that's just
[2129.32 → 2136.06] I think we learned over time to kind of unbundle some things because sometimes someone will come in
[2136.06 → 2140.50] and they'll just say Cristiano and they'll just kind of leave without realizing it's really easy either
[2140.50 → 2146.44] not to use or remove themselves most of the projects that we create we say they're like delete key
[2146.44 → 2150.96] friendly if you would is you don't want something just remove it but so now Cristiano is in a
[2150.96 → 2158.08] different project but still supported works and we kind of have an accompanying project to bedrock
[2158.08 → 2164.58] which is a set of Ansible playbooks Ansible is just server configuration management if you've ever
[2164.58 → 2171.40] heard of chef puppet salt Ansible is just like that but different I'm sure folks are familiar with it to a
[2171.40 → 2175.86] degree, but we haven't really talked about Ansible really much on the show yet yeah if we want to get into
[2175.86 → 2181.94] that we can but just very briefly we kind of have a better integrated more official way of
[2181.94 → 2185.80] of not only provisioning and setting up servers for bedrock but also deploying
[2185.80 → 2192.50] so those are kind of our two official methods, and we haven't necessarily documented how to use
[2192.50 → 2198.84] other deployment tools Ben's Ben mentioned a couple like deploy HQ and Laravel forge but really
[2198.84 → 2205.20] any of those tools usually let you kind of hook into their deployment workflow and specify manual
[2205.20 → 2210.48] commands to be run so if you just kind of specify you know run composer install most deployment what
[2210.48 → 2216.30] methods will work fine well I'm very interested in the Ansible setup I'm interested in how vagrant
[2216.30 → 2223.06] plays into this I use vagrant quite a bit for development reasons and stuff like that where do we begin with
[2223.06 → 2229.10] going down that road with actually using Ansible or using because Cristiano's deployment Ansible sort of
[2229.10 → 2234.84] little bit of both and then vagrants sort of like localized version of it those out there who are
[2234.84 → 2240.02] tried and true WordPress developers probably know camp should know camp if you don't know camp that's a
[2240.02 → 2243.88] sad thing, but maybe it's a better thing now that you've listened to this show because you won't use
[2243.88 → 2250.44] camp any more hopefully right so I mean that's the interest for me is with vagrant
[2250.44 → 2255.86] when it comes to WordPress is I don't want to mess with my system you know I'm okay with it with the
[2255.86 → 2260.50] ways I can do it with like ruby and using RVM and things like that because there are necessary tools
[2260.50 → 2265.96] but I think that the WordPress and PHP ecosystem that I'm aware of isn't quite mature like those
[2265.96 → 2273.04] other uh other versions are, and it's easier to do it in a know Ansible created vagrant you know
[2273.04 → 2279.16] Ubuntu 1404 machine that I could just spin up destroy and so walk us through the process of
[2279.16 → 2285.24] of vagrant and Ansible and maybe even how deployments work at some point with uh with
[2285.24 → 2292.04] cadastral sure okay so I'll start with vagrants um hope I think of kind of any tool that we use
[2292.04 → 2296.60] in the roots organization vagrant might be the most well known most kind of communities have really
[2296.60 → 2304.08] picked it up which is great, so vagrant is a project to help uh create development virtual machines on
[2304.08 → 2309.62] your computer so like you said is you really want to avoid messing with your local system one because
[2309.62 → 2314.12] you might have incompatible versions you might have different software that you're running on your
[2314.12 → 2318.90] you know production server it's a little harder to modify versions and get the proper ones you want
[2318.90 → 2325.34] like macOS 10 comes with whatever default version at the time of things like PHP and ruby and python
[2325.34 → 2329.68] and those might be different versions than you need, and they don't worry about keeping them updated either
[2329.68 → 2333.56] and they're not going to concern themselves with what version it is because they're not trying to be a
[2333.56 → 2339.10] development server they're trying to just you know deliver an uh an operating system to you
[2339.10 → 2344.48] yeah so like you said vagrant you know creates a local virtual machine running on your machine so
[2344.48 → 2348.06] you can do whatever you want in there, and it's not going to interfere with your system so that's kind
[2348.06 → 2354.78] of the first step and most people when they get into vagrants they use it just for creating kind of a
[2354.78 → 2361.36] bare Ubuntu server right, and then they'll go in manually, and you know run apt get install nginx or
[2361.36 → 2366.96] whatever software you need my sequel so what we've done is created a set of Ansible playbooks
[2366.96 → 2372.16] so when you type vagrant up it automatically runs all these Ansible playbooks
[2372.16 → 2378.40] and it will give you a machine with all the software you need to run a WordPress site which is a little
[2378.40 → 2385.14] specific to bedrock, but it will work with you know any standard WordPress site as well and the benefit
[2385.14 → 2390.42] of the bedrock Ansible project is that the exact same playbooks that you use to create your development
[2390.42 → 2397.32] virtual machine you use to create your remote staging and production servers so it's one thing
[2397.32 → 2402.98] that we try to promote is parity between your environments as we call them so that you know
[2402.98 → 2409.28] that if you're developing locally in development you know with much higher confidence that if you push
[2409.28 → 2414.38] that code to staging and production that it's going to work because there's no mismatch between
[2414.38 → 2420.88] either types of software or versions of software or even things like you might need caching and
[2420.88 → 2426.58] test out teacake for example which most people wouldn't have running map locally yeah we have to get
[2426.58 → 2434.84] rid of the map's okay it's just it's what you said it's not parity for your local environment
[2434.84 → 2440.84] you're not it comes back to the reasons why bedrock exists period was to reduce the things you were
[2440.84 → 2446.00] redoing every time like even hopping into a vagrant machine, and you know running app get every single
[2446.00 → 2453.52] time it's its it's uh it's not a dry process so if you can reuse that process and match your
[2453.52 → 2458.32] development machine to your production machine then it's a lot easier to test bugs and things like that
[2458.32 → 2465.96] and that comes from I'm assuming it comes from your ruby roots yeah definitely I mean no pun intended of
[2465.96 → 2473.76] you like that um i I think that's kind of the biggest thing about bedrock and our Ansell
[2473.76 → 2479.56] project is we just we try and take like the best practices that a lot of other communities are a
[2479.56 → 2486.40] little um we're a little earlier to develop and I mean the PHP world and more specifically WordPress
[2486.40 → 2494.18] is getting better finally of kind of looking out and seeing what other you know languages frameworks or
[2494.18 → 2498.68] communities what tools and what best practices they're using and trying to integrate them back
[2498.68 → 2503.40] I would say it's really slow, and it's finally getting a little better and so that's what that's
[2503.40 → 2509.58] all we try to do like I'm I'm not claiming that we've invented things from scratch I mean I take a lot
[2509.58 → 2515.00] of stuff from rails like I said I took a lot of ideas the best way to do it yeah I mean it's the best
[2515.00 → 2522.00] way to do it we were using chef before we were using Ansible actually yeah i I like you know I'm you
[2522.00 → 2529.50] know a ruby is to my heart so I like chef and those who are DevOps you know super Devon people
[2529.50 → 2534.86] they love chef, and they love Ansible uh, and they may have a case where they prefer chef over Ansible
[2534.86 → 2540.16] but those are like those are different kind of people than I am and to me when I look at Ansible
[2540.16 → 2544.32] I'm like this is a lot easier it takes a little bit more learning, but it's a lot easier to read it
[2544.32 → 2550.72] um, and it's a lot easier to me to just work around with Ansible so i I like it a lot that's actually
[2550.72 → 2556.16] my favourite part is how easy it is to work with you might be familiar with a tool or a project called
[2556.16 → 2563.56] AVV um it uses vagrant to create you know WordPress development environment but what it uses
[2563.56 → 2569.48] is I forgot how many lines it is its just a giant bash script basically to provision the server so if
[2569.48 → 2573.90] you take that, and you compare it to what we've got in the bedrock Ansible repo it's just so much easier
[2573.90 → 2578.60] to work with these configuration files and not to mention you've got all these third-party packages
[2578.60 → 2584.26] through Ansible galaxy that you can also take advantage of as well yeah that's true yeah that's
[2584.26 → 2590.82] true varying vagrant vagrants we'll link out to that in the show notes because it's its a long one I'm
[2590.82 → 2596.60] not going to spell that URL on GitHub but AVV is its project name uh and I used that at one point that
[2596.60 → 2602.30] that was neat okay that got me into you know a better development environment, but it helped me scratch
[2602.30 → 2606.16] the itch that I already had which was I doingn't like what I'm doing currently I don't like using
[2606.16 → 2611.68] map I want to have better control over my local environment in comparison and with parity for my
[2611.68 → 2616.72] production environment and I want to be able to solve problems a little bit easier and most of all
[2616.72 → 2622.72] you know vagrants a cool tool anyway so uh let's take a quick pause we're going to come back I know we've
[2622.72 → 2628.78] talked quite a bit about bedrock I do want to dive a bit into sage and more so into the roots
[2628.78 → 2632.30] organization and some of the other stuff you guys are doing so let's take a quick break we'll come
[2632.30 → 2639.14] back we'll talk we'll tail off bedrock, and we'll dive into sage all right put them away put them back
[2639.14 → 2644.98] put the books back on the shelf you don't need them and learn to code by doing with code school
[2644.98 → 2655.98] code school offers a variety of courses JavaScript HTML CSS ruby iOS git and many more to help you
[2655.98 → 2662.42] expand your skills and learn new technologies code school knows that learning to code can be a
[2662.42 → 2667.94] daunting task, and they've combined experienced instructors with proven learning techniques to
[2667.94 → 2672.74] make coding educational and memorable gives you the confidence you need to continue past those
[2672.74 → 2677.90] rough tough hurdles that you will definitely face learning the code school also knows that
[2677.90 → 2682.48] languages are a moving target they're always updating their content to give you the latest
[2682.48 → 2688.10] and the greatest learning resources you can even try before you buy roughly one out of every five
[2688.10 → 2696.44] courses on code school is absolutely and totally free this includes instructor classes on git ruby jQuery
[2696.44 → 2702.94] and much more which allow free members to play full courses with coding challenges all included you can
[2702.94 → 2709.18] also pay as you go one monthly fee gives you access to every code school course and if you ever need a
[2709.18 → 2715.00] breather take a break you can suspend your account at any time don't worry your account history your
[2715.00 → 2720.08] points your badges they'll all be there when you're ready to pick things up again get started on sharpening
[2720.08 → 2724.96] your skills today at code school.com once again that is code school.com
[2724.96 → 2734.24] all right so what can we wrap up here with bedrock I know we've spent most of our time here today
[2734.24 → 2740.30] on today's call talking about bedrock which is important bedrock awesome it is awesome what else
[2740.30 → 2745.22] can we cover that makes a lot of sense and then what can we then lets uh let's go into sage
[2745.22 → 2751.48] sure I'll I mean I'll try and finish up with kind of I guess our overall vision and why we think it's
[2751.48 → 2755.54] important and I mean we've gone over a lot of the features and a lot of the things like dependency
[2755.54 → 2760.54] management and things you probably should use and may not um but I think the point where we're getting
[2760.54 → 2767.44] to now is a deep integration between bedrock and our Ansible project and once we get more
[2767.44 → 2774.00] integration between these it just becomes really easy to create that development VM where you can
[2774.00 → 2779.34] run one or multiple sites and then mirror that with staging and production servers I mean soon we're
[2779.34 → 2786.00] going to be adding anything to uh automate creating like a digital ocean droplet for example so with you
[2786.00 → 2790.34] know one command you could run big or not with another command you could spin up a digital ocean
[2790.34 → 2794.94] droplet, and it's going to run those same Ansible playbooks, and you'll get your staging and production
[2794.94 → 2801.52] servers and everything is tied together so that's where we're headed and I mean from what we see just
[2801.52 → 2807.60] talking to people they're already when it works it's great, and we're fixing you know bugs some of these
[2807.60 → 2813.80] things are new and they're really liking the kind of the higher vision of when they all these
[2813.80 → 2819.62] tools integrate together oh and actually the final thing I should mention is underneath our organization
[2819.62 → 2825.52] on GitHub we have a new project it's called roots example project there are dashes in there but just go
[2825.52 → 2830.46] to GitHub.com slash roots and I'm sure you'll link it I'll link it what we've yeah what we've done is
[2830.46 → 2835.62] we've a lot of people had questions about how to integrate these tools together so we have an example
[2835.62 → 2842.14] repository that uses bedrock Ansible and sage and some of our other plugins as well
[2842.14 → 2848.94] and it's a complete working repository it's running on a production site roots example project.com and
[2848.94 → 2853.74] so they can see exactly what settings they need to change how these things work together and the exact
[2853.74 → 2859.44] steps that we took to actually create it, and we're going to continue improving that but I think that's
[2859.44 → 2864.86] like one of the best starting points if someone kind of wants to see like what roots offers at a high
[2864.86 → 2870.86] level and the advantages of it this is uh definitely neat and being able to deploy the digital ocean and
[2870.86 → 2877.00] having commands for all that is super neat as well any direct an any direct collaboration with
[2877.00 → 2883.76] digital ocean on the on that front um yeah Ben can answer that not direct um they did sponsor us
[2883.76 → 2889.74] and they provide us with our hosting so that's very nice of them we do plan on adding um
[2889.74 → 2894.42] hopefully a one-click digital ocean install to the bedrock Ansible project as well though
[2894.42 → 2900.20] very cool yeah digital ocean is uh what we're actually hosted on so we're big fans of digital
[2900.20 → 2905.16] ocean and plus they support this podcast so that's awesome they support your project as well to move
[2905.16 → 2910.94] this forward because we all need support, and thank you digital ocean for that yeah so um
[2910.94 → 2918.50] any final words I guess Scott or ben on uh on the developers out there that are using
[2918.50 → 2923.34] WordPress that are not using bedrock that that should use bedrock because they're the kind of
[2923.34 → 2929.44] developer that bedrock is targeted for I would just encourage people to take a look at it that I mean
[2929.44 → 2935.82] that's the first thing is just check it out we've written a lot of um blog posts um we give a lot of
[2935.82 → 2939.78] support on their screencasts like if you want to learn about features if you want to find out how to use
[2939.78 → 2944.46] them why they're important I mean just take a look at it some people might dismiss it some people might
[2944.46 → 2950.16] just say hey you know I'm fine with what I have and why but i I guess all we can say is just for
[2950.16 → 2956.92] people to check it out and we and many other people believe that there are big advantages to it
[2956.92 → 2963.60] awesome and that must tie into I mean similar philosophies in what bedrock does for WordPress
[2963.60 → 2969.72] and deployments and dependency management must come into sage at the same way but at the theme level
[2969.72 → 2978.66] not the entire WordPress app level right uh we introduced sage a little earlier as a theme
[2978.66 → 2985.22] how do we how do we describe this as a start a theme based on html5 bullet plate gulp Bauer uh and
[2985.22 → 2990.74] bootstraps some of these things are optional I'm sure but uh the one thing in this it's to
[2990.74 → 2997.60] stands out to me is the workflow I know that everyone has their own crazy way to sort of organize
[2997.60 → 3004.52] our theme how does sage change that and then what's the workflow to I guess develop this theme
[3004.52 → 3012.00] okay, so the sage gulp file is pretty badass and that's pretty much all thanks to Austin prey
[3012.00 → 3020.14] um thanks Austin anyway um so our gulp file um it compiles and concatenates CSS and JavaScript you
[3020.14 → 3026.90] know the typical things it also does image modification, and we've got browser sync so
[3026.90 → 3032.44] basically when you have sage installed on your machine, and you're running gulp watch you've got
[3032.44 → 3037.80] a browser sync session that launches, and you load up the assets directory, and you start choosing what
[3037.80 → 3044.54] you want to do whether that's writing style sheets or writing JavaScript or even actually bringing in
[3044.54 → 3052.64] third party CSS or JS from Bauer so if you were to be developing your theme you could add a Bauer
[3052.64 → 3059.24] package, and it's automatically going to add that to the theme JavaScript and in your browser sync
[3059.24 → 3064.66] session it's going to automatically reload that so for instance if you're working on a new WordPress
[3064.66 → 3071.66] theme, and you wanted to add responsive videos you would just do Bauer install fit vids and before you
[3071.66 → 3079.00] know it your browser sync session is working with fit vids in addition to the things you mentioned
[3079.00 → 3084.16] there something unusual to those who are developing themes for WordPress is this theme wrapper and you
[3084.16 → 3090.12] mentioned before bent hat it was unconventional to WordPress um can you talk about that a little bit
[3090.12 → 3096.30] and what kind of hurdles you've had to deal with and what kind of gains you've had to I guess embrace
[3096.30 → 3104.06] because of it so if you bring up the sage code base um there's a file that we have called base.php
[3104.06 → 3111.72] and what this is it's the base wrapper file for a WordPress theme if you look at a normal WordPress
[3111.72 → 3118.22] theme, and you bring up the individual template files such as like index.php page and single etc
[3118.22 → 3125.92] every single one of those templates is going to be individually calling um the HTML doc type
[3125.92 → 3134.06] uh your HTML head uh as well as the footer and all the different separate parts of your WordPress
[3134.06 → 3140.32] theme so what the wrapper is doing is it's giving you one place to put your base markup, and then it's
[3140.32 → 3147.28] including individual templates uh from there so instead of having your markup scattered across
[3147.28 → 3153.20] maybe a dozen different template files the base markup is controlled from one place it encourages
[3153.20 → 3158.68] basically the separation of application logic from the templates you don't want to have templates
[3158.68 → 3165.12] with conditional statements um you just want to have a different partial that you include
[3165.12 → 3173.36] to keep things lean I've done something similar in hours I think i if I'm going from memory I don't have
[3173.36 → 3177.54] the project in front of me I can pull it open though while I'm sitting here talking about it though I think
[3177.54 → 3185.10] I did something a little similar to this I have kind of a and by no means am I trying to compete
[3185.10 → 3190.98] with sage but I know I have a loop file loop.php file which has a while have post calling it and
[3190.98 → 3196.72] an end while, and it does things like give me all my different sort of you know in the rails world
[3196.72 → 3202.40] parcels for the different post formats and things like that that's what I'm doing so how difficult
[3202.40 → 3208.72] is it to sort of retrain somebody doing things like I'm doing to embrace what's happening I guess
[3208.72 → 3215.40] in sage with this kind of main wrapper it's really not that hard the number one thing to
[3215.40 → 3220.66] keep in mind is that nothing changes as far as the WordPress template hierarchy goes for some reason
[3220.66 → 3226.82] people get confused as far as that goes, and they seem to think that things are different but
[3226.82 → 3234.44] extending page templates works the exact same way I haven't really heard of too much uh hassle with
[3234.44 → 3240.62] the wrapper lately I know at first when we implemented it there was a lot of people you know pushing back
[3240.62 → 3245.38] saying whoa this is weird this isn't the WordPress way of doing things it made them a little bit
[3245.38 → 3251.16] uncomfortable and then sure enough all these people that were hesitant to adopt the theme wrapper
[3251.16 → 3258.18] they then came back and said oh well this makes sense um why am I not going to implement something
[3258.18 → 3266.30] like this so we actually have um Austin prey I mentioned he's on the roots team he did not come
[3266.30 → 3273.34] from the WordPress world and his first um his first experience with WordPress theming was actually using sage
[3273.34 → 3281.02] and to him everything made sense as far as the WordPress theme wrapper went, and then he went to go work on
[3281.02 → 3287.26] another project that was a non-sage theme, and he was confused as to how the template files were working
[3287.26 → 3294.42] and why they were duplicating code across all the template files and to him, it was just like well
[3294.42 → 3301.40] that's weird the wrapper makes sense because he doesn't come from WordPress he came from outside
[3301.40 → 3308.06] WordPress land where that's the normal way of doing things so if you look at a normal WordPress theme and
[3308.06 → 3315.32] you bring up one of your templates you're doing get header to get the page header but inside there
[3315.32 → 3321.82] you're also calling your main content area and defining the markup for that as well and that's
[3321.82 → 3328.04] just not something that needs to be in those template files since that's going to be the same across the
[3328.04 → 3335.80] entire site yes in my index.php file I have got header get sidebar and then I have got template part
[3335.80 → 3340.90] and then I'm referencing the loop.php file and I'm saying get footer and that's what my index looks
[3340.90 → 3347.44] like and I can see how this wrapper would certainly change that quite a bit and probably
[3347.44 → 3351.44] help me reduce a little bit of the code repetition, but there's not too much because I'm trying to avoid
[3351.44 → 3357.50] that now but my version of it is you know not as advanced as is what you guys have got going on
[3357.50 → 3363.18] here and I can see where yours is definitely improving the process a lot better especially I think the
[3363.18 → 3369.28] question I have after this is um just like we did with bedrock who is sage for is it for everyone
[3369.28 → 3373.96] out there or is it for you know is it for the theme development companies who are going to use the
[3373.96 → 3382.32] the way sage says this is how you know a theme should be built um well that's a good question I wouldn't say
[3382.32 → 3386.94] that sage is for everybody, and we actually have a blog post that says sage should not be your first
[3386.94 → 3393.48] WordPress theme um okay you know it's nice for some people it is like a lot of people have told us
[3393.48 → 3399.78] that they've learned so much because of sage like we introduced them to tools such as gulp and Bauer
[3399.78 → 3405.46] things that these people have never used before um but at the same time as if you wanted to build a
[3405.46 → 3412.34] theme for WordPress.org we actually don't follow WordPress coding standards um we also don't include
[3412.34 → 3418.66] some of the things that they require in those themes I mean that said there are still themes in
[3418.66 → 3426.28] the WordPress theme repository that are built with sage it's more for in my opinion people doing client
[3426.28 → 3433.04] work or working on their own projects or building an app it's not necessarily meant for widespread theme
[3433.04 → 3440.06] distribution and that's because of the gulp build process for the most part I mean you could package up
[3440.06 → 3446.04] your theme with the dist folder that's got all the built assets but I mean that's not what we
[3446.04 → 3452.06] recommend in the first place we are all about keeping those sorts of files outside your git repository
[3452.06 → 3460.18] so I mean sage is definitely not for everybody I mean if you're just building a theme to sell it on
[3460.18 → 3467.86] something like theme forest sage might work for you um, but the front end side of things is probably not
[3467.86 → 3474.84] going to work um you're probably not going to want to include a gold file um to offer to someone
[3474.84 → 3479.28] that's going to be installing this WordPress theme on their marketing website, and they don't have any
[3479.28 → 3485.96] idea what CSS or JS is so I definitely say that sage is targeted more towards developers and also
[3485.96 → 3493.66] developers that are interested in you know these tools this is really for those sorry go ahead uh
[3493.66 → 3498.52] for the listeners we're still dealing with some robotic ness from Skype so that's why you might hear us
[3498.52 → 3507.94] lately talk together but um yeah I'm with you that this is more for teams that are or the who's
[3507.94 → 3513.94] really like managing their own site that wants to craft fully take care of their own site versus doing
[3513.94 → 3521.32] these antiquated ways they're using more modern ways to manage their own theme um could be an in-house
[3521.32 → 3527.90] could be an in-house marketing agency or marketing team for a larger company I know my wife and uh and
[3527.90 → 3533.64] Ben the guy mentioned earlier worked at a company like that where they um where they essentially
[3533.64 → 3538.14] have a WordPress install, and they don't plan to move away from if it's their you know it's their
[3538.14 → 3542.34] marketing funnel so they're putting a lot of people to it so it's really important, and they want to
[3542.34 → 3548.64] modernize and really craft fully take care of this WordPress install, and it seems like it's for people
[3548.64 → 3553.72] like that not so much those who are developing themes and selling them which is great too because
[3553.72 → 3558.96] I mean that's that's a whole different market, but you're trying to put better tools in developers
[3558.96 → 3565.10] hands to take care of their stuff and those stuff is a WordPress install, and a theme install to that
[3565.10 → 3571.40] to that WordPress install right well cool in addition to this I'm sure we could probably go on a bit more
[3571.40 → 3577.10] but we're running out of time um in addition to this you've got roots the organization
[3577.10 → 3582.06] itself you've got screencast talk a little bit about the organization because you've got these two
[3582.06 → 3586.74] larger pieces to the project you got soil which we haven't really talked about which maybe you could
[3586.74 → 3591.36] touch on a little bit, but you've got screencast you're doing some of those I think they're all paid
[3591.36 → 3597.08] if i recall correctly um paid screencast that you can learn how to use
[3597.08 → 3602.44] go up and Bauer for theme development Cristiano for WordPress deployment and composer for dependency
[3602.44 → 3607.82] management but talk about the organization the core team and what's going on behind the scenes
[3607.82 → 3611.90] that roots beyond these two projects we've talked about uh most of the time here on the show today
[3611.90 → 3619.20] so we've got quite a few people on the team the core team would be Scott and i along with
[3619.20 → 3624.80] nick fox Chris Carr and Austin prey um, but we also have a bunch of other people that help out with
[3624.80 → 3632.88] our projects um there is Michael from Florida we got Phil um we've got Julian Kaylin Nathaniel
[3632.88 → 3638.72] and Craig and all these guys help out on a daily basis whether it's on the forum or contributing code
[3638.72 → 3645.92] or just talking about WordPress and making things better um just internally and the direction of where
[3645.92 → 3652.80] we're going to go with our own projects one of the things that Craig on the team said a few weeks ago
[3652.80 → 3661.08] let me find it he said um I think we're all on the same page when it comes to WordPress WordPress is a
[3661.08 → 3667.26] lemon, but the industry likes WordPress so let's make lemonade that's basically the roots' organization
[3667.26 → 3672.72] right there yeah it shouldn't be like that though you know it really shouldn't be, but that's
[3672.72 → 3679.58] I'm with you like I said with the change law we've we built we rebuilt ourselves from Tumblr to
[3679.58 → 3685.50] WordPress and every time we've tried to do something alternative to WordPress like we could
[3685.50 → 3690.62] build our own ruby cms, and it would be ours, and we can open source it potentially, or we can use
[3690.62 → 3695.26] something that's already out that's open source we could use jackal we can use several other things
[3695.26 → 3700.28] but there are things that come with WordPress that don't come with other you know other software that
[3700.28 → 3705.26] you can use plus WordPress is open source we'll talk a bit about uh here in a second I'll give you
[3705.26 → 3710.58] guys a chance to talk about your most favourite thing to talk about which is how WordPress uh
[3710.58 → 3715.60] contributing to WordPress is broken so we'll talk a bit about that, but you know for us every time we
[3715.60 → 3720.46] try to do something different from WordPress we were always just trying to recreate what it does
[3720.46 → 3726.10] and i I'm I feel like what you are trying to do with roots and what you're trying to do with
[3726.10 → 3732.56] the organization roots and then bedrock and sage so far is improved upon this lemon you know make it a
[3732.56 → 3736.84] better lemon you know or put a little sweetener in that lemon if we're talking about some puns here
[3736.84 → 3743.00] something like that um you know something to make it a bit brighter environment to work in because
[3743.00 → 3749.68] those who come from the ruby world or other more modern deployment process worlds you know you come to
[3749.68 → 3755.88] WordPress, and you're like this is horrible not that WordPress is bad it's the workflows that don't
[3755.88 → 3759.50] help the team to be better and more efficient right and I think that's really what you're trying to
[3759.50 → 3765.76] solve is being better and more efficient with WordPress, and you know the fact that it's in PHP
[3765.76 → 3771.16] doesn't matter to me, I think PHP PHP is a great language to a degree uh some favour other languages
[3771.16 → 3778.34] but I'm fine with it um if I had my rather uh you know somebody might jump on the know somebody
[3778.34 → 3784.04] might jump on a different you know, but that doesn't matter you know it's the tool itself is so ingrained
[3784.04 → 3790.74] to the the the web there are so many sites on WordPress yeah you can't argue with the numbers
[3790.74 → 3795.94] yeah you can't fight it either so you know I think that's maybe the point who was it that said that
[3795.94 → 3800.00] oh it was Craig that said that Craig so it's probably the point that Craig's trying to make
[3800.00 → 3805.64] is like you know what we can't fight it you know there you go yeah and sorry just to underscore
[3805.64 → 3810.60] that I believe even the newest numbers that someone on loophole the WordPress conference just
[3810.60 → 3816.76] mentioned again was that it powers 23 of the web yeah I mean who knows how accurate the number is
[3816.76 → 3823.00] but we all know it's a lot I bet you it's accurate I mean that's well I'd like to know if is it the
[3823.00 → 3827.98] American web is the European web is the china web staggering numbers you know yeah it's a big number
[3827.98 → 3833.34] though and I'm sure that's the case because it's open source it's so easily deployed PHP is so vastly
[3833.34 → 3839.32] available on shared servers unlike other languages that have you know issues with getting there it's just
[3839.32 → 3844.96] so easy to launch a WordPress site so it's ubiquitous to the web so I think it makes
[3844.96 → 3848.98] sense to leverage it but I also think it makes sense to do what you guys are doing here which is
[3848.98 → 3854.26] to improve upon its workflows and just in general make it a better environment so let's
[3854.26 → 3860.40] let's let's zoom out a little bit and talk about I don't know which one of you guys want to take this
[3860.40 → 3866.76] one maybe you both can do it tag team on I don't care, but before the call was started I wanted to ask
[3866.76 → 3870.40] you guys a question that you wanted to answer you wanted to talk about, and you all want to talk
[3870.40 → 3875.96] about contributing to WordPress WordPress core and how it's a broken process what did you mean by that
[3875.96 → 3885.28] so if people who aren't familiar with WordPress core um they have always or up until very recently
[3885.28 → 3895.28] been on subversion for a source control, and they use their own wiki slash um repo host called track
[3895.28 → 3901.08] it's an open source project and the project itself is fine that's not necessarily the issue what we're
[3901.08 → 3905.74] talking about when kind of contributing to WordPress core is broken, and we don't just mean contributing
[3905.74 → 3912.86] as in writing code we also mean uh reporting issues responding to issues um keeping up to date with them
[3912.86 → 3920.64] and their workflow around you know patches bugs features things such as that I think the most common
[3920.64 → 3926.86] occurrence that's ever had chats between me and Ben our old hip chat channel our current Slack channel
[3926.86 → 3935.24] is searching track for some bug feature issue finding it pacing in the channel and then remarking how it
[3935.24 → 3942.04] was open for anywhere from four to seven years and still hasn't been dealt with we I think Ben has a
[3942.04 → 3948.64] list of maybe like a hundred track tickets and their average lifetime is in the uh four to six year
[3948.64 → 3955.70] range and I mean that's the first problem and the second problem is that I have a theory and I don't know if
[3955.70 → 3960.34] this is true so I don't want to step in their toes too much but I feel like WordPress likes kind of
[3960.34 → 3966.54] insulating themselves in their own world and that world is kind of track it's the internal WordPress community
[3966.54 → 3971.00] it's very weird that in this day and age you have a company like Microsoft who's famously
[3971.00 → 3976.02] kind of closed source doesn't embrace open source, and they're removing all their projects to GitHub
[3976.02 → 3982.04] and then here you have this great kind of open source organization and automatic and WordPress who's
[3982.04 → 3988.24] in kind of siloed off in their own world in this track project, and it makes it very hard to
[3988.24 → 3995.14] contribute um one of my pet peeves with it is to actually contribute code you need to generate you
[3995.14 → 3999.84] need to work with their subversion and generate patch files so you need to create an issue you need to
[3999.84 → 4004.72] create a patch file upload the patch file, and then you know when you contrast that with the typical
[4004.72 → 4009.70] GitHub workflow is you can open a pull request, and you can get a nice diff and people can comment
[4009.70 → 4014.48] right on lines and go back and forth with your code that's not really possible in WordPress's track
[4014.48 → 4019.50] you can't link to a line you can't comment on it like the whole kind of pull request contribution
[4019.50 → 4027.02] workflow is broken and that's the main thing that we talk about is like here you have a whole group of
[4027.02 → 4031.54] people in this rich organization who would love to give back and help WordPress but they kind of
[4031.54 → 4038.38] actively discourage that and make it very difficult for you to do yeah I mean I think on this show we've
[4038.38 → 4046.92] covered the blessing I think GitHub has been to the proliferation and the progress of open source
[4046.92 → 4054.58] and it does astound me that uh you got two parts you got some companies who want to stay in their
[4054.58 → 4059.04] systems they've already built out because they're used to it, and they have their own agendas, or they don't
[4059.04 → 4064.74] want to move or whatever the reasons are, and then you have other companies other organizations like
[4064.74 → 4071.18] we just had a show with the ruby heroes talking about ruby and how they don't want to move ruby
[4071.18 → 4077.32] fully onto GitHub because then that has an uh you know a company that has a profitable company a for-profit
[4077.32 → 4082.38] company that has liked their hands completely wrapped around this open source project, and they don't want
[4082.38 → 4087.76] to have that as dependency so you have all these different competing reasons of why GitHub may or may not be
[4087.76 → 4093.78] but as a community as a contributor as a user as a developer you want you just want access to
[4093.78 → 4099.22] contribute whether it's a comment whether it's better documentation an actual code commit sending
[4099.22 → 4105.42] patch files and diff files and you know it's just it's too much work and that's why GitHub exists that's
[4105.42 → 4112.80] why git has gone the way it has and that's why we're doing what we do now because GitHub has
[4112.80 → 4116.96] certainly pushed that envelope to the nth degree to make it possible definitely yeah now we're
[4116.96 → 4121.04] used to it yeah and I should just clarify like this isn't about oh you know move to GitHub because
[4121.04 → 4125.48] it's cool and it's popular and you know subversion's not cool anymore and it's not even necessarily about
[4125.48 → 4132.28] GitHub themselves like if is WordPress wanted to host their own um what is like a git lab and another
[4132.28 → 4136.58] one they may have merged um you know they let you create your own basically your own GitHub
[4136.58 → 4142.60] basically if they move to something like that that was much uh you know facilitated kind of like a pull
[4142.60 → 4147.36] request based workflow they'd see the same kind of benefits obviously you wouldn't have you know the
[4147.36 → 4154.64] built-in user base of GitHub but it's a combination of the know the large community on GitHub but
[4154.64 → 4160.38] also just the ease of contributing and uh and dealing with issues and pull requests
[4160.38 → 4168.18] so if uh is Matt Mullenweg or somebody high up on the team is listening to the show right now they
[4168.18 → 4173.60] can make a change what change would you guys request to the WordPress team to make it more
[4173.60 → 4177.68] accessible what are some of those I mean it might have been obvious but what's a clear directive for
[4177.68 → 4185.08] them well I mean in my opinion the easiest or most direct move would be move your project on to GitHub
[4185.08 → 4190.82] and you know kind of embrace that pull request based workflow um I mean like I said the main issue
[4190.82 → 4196.30] is it's just really hard to deal with patch files and code reviews and as someone who may have wanted
[4196.30 → 4203.52] to contribute patches I have not done that simply because and you're talking about someone who's been
[4203.52 → 4209.16] on GitHub for years has contributed to i can't even count the number of open source projects and this
[4209.16 → 4213.28] is me who doesn't even want to you know help out with WordPress so I can't imagine what it's like for
[4213.28 → 4219.50] others as well and I think the result of that is you get a very kind of insulated WordPress community
[4219.50 → 4228.60] of the same people yeah yeah I feel your pain, so anybody out there who has some pull to that team
[4228.60 → 4237.64] and can uh you know clue them into this show tell them uh to come and listen to what Ben and uh and
[4237.64 → 4242.84] Scott and the rest of our team have been doing their roots uh certainly enjoyed the conversation around
[4242.84 → 4248.12] bedrock certainly enjoyed the conversation around sage definitely want to encourage you guys to
[4248.12 → 4254.58] keep moving forward and adopting new members to your team uh what's a call to action for roots and
[4254.58 → 4260.82] sage I guess sorry bedrock see I'm I'm stuck again with the branding and the naming for bedrock
[4260.82 → 4265.42] and sage and the roots' organization which you guys have going on there what's the call to action for
[4265.42 → 4271.30] the community how can people step in and help you move the initiative uh forward that you have going
[4271.30 → 4277.84] um I mean really at this point there's not too much that needs to change on like the sage theme
[4277.84 → 4284.60] itself we're moving to a yo-man generator so I mean it would be great if people would like to fork sage and
[4284.60 → 4289.68] replace bootstrap with their own front-end framework I mean that's going to make things like the yo-man
[4289.68 → 4296.80] generator a lot easier for us um and then our bedrock Ansible project we're we're trying to get a 1.0
[4296.80 → 4302.00] out for that so the more people that use it and test it and give us feedback on that the better
[4302.00 → 4307.46] it is for us to improve it yeah and I was just going to mirror the last part and just say that
[4307.46 → 4313.28] more than anything uh we like to hear about people using it and their feedback and I think one of the
[4313.28 → 4319.26] bad things about kind of the uh open source world is that you tend to hear about you know the bugs and
[4319.26 → 4324.60] the things that don't work and then the people who it's working great for don't speak up and I mean
[4324.60 → 4328.54] they're both equally valuable it's great to get bug reports to get improvements and suggestions
[4328.54 → 4334.38] and things that don't work, but it's equally good to get you know that opposite um message of hey this
[4334.38 → 4340.14] is working great and these are the specific things we like and especially getting into yeah the Ansible
[4340.14 → 4344.52] side of things it's just we need more people using it, and we need more people reporting back
[4344.52 → 4352.10] either things that don't work or things that they like good deal well Bon Scott thank you so much for
[4352.10 → 4356.72] joining us today uh but for those who are listening uh thank you so much for tuning in
[4356.72 → 4362.52] all the links we talked about will be in the show notes so uh check out the episode show page for
[4362.52 → 4372.82] that uh this episode is I believe it's uh 156 so go to changelog.com slash 156 to get all the links
[4372.82 → 4377.72] uh definitely want to thank our sponsor for supporting the show digital ocean was mentioned not sure if
[4377.72 → 4382.30] there'll be a sponsor for this show or not because I do those i I record those in the aftermath
[4382.30 → 4389.68] but uh next week's show is uh is going to be a fun show let's see what that show is actually it's
[4389.68 → 4394.58] going to be with Sarah Allen if anybody's familiar with Sarah Allen so talk about the ruby world uh Sarah
[4394.58 → 4400.00] Allen was one of the founders of rails bridge a lot of cool stuff coming out of uh what Sarah Allen's
[4400.00 → 4406.16] doing such a contributor to educating uh those who want to become developers and junior developers
[4406.16 → 4410.74] there's a lot of a lot of passion from Sarah we're excited to have her on the show finally
[4410.74 → 4418.74] um and uh with that fellas let's let's say goodbye and uh call the show done awesome thanks a lot for
[4418.74 → 4424.88] having us Adam yeah, thanks it was great to be on its great having you guys on all right thanks guys
[4424.88 → 4425.34] bye
[4425.34 → 4436.62] fine
[4436.62 → 4442.46] so
[4442.46 → 4444.78] you
[4444.78 → 4450.12] you
[4450.12 → 4450.34] you
[4450.34 → 4480.32] Thank you.
