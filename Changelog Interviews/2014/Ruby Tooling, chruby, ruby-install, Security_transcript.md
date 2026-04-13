[0.00 --> 14.54]  welcome back everyone this is the changelog where remember supportive blog podcast and
[14.54 --> 19.22]  weekly email covering what's fresh and what's new in open source check out the blog at the
[19.22 --> 26.16]  changelog.com our past shows at five by five dot tv slash changelog and you're listening to episode
[26.16 --> 33.34]  120 andrew and i talked to postmodern about his open source projects ch ruby ruby install ch gems
[33.34 --> 40.16]  ronin and more today's show is sponsored by ninefold code ship and new relic we'll tell you a
[40.16 --> 45.00]  more about code ship and new relic later in the show but ninefold is our our first sponsor they're
[45.00 --> 50.46]  a high performance platform for deploying and hosting ruby on rails applications the platform
[50.46 --> 57.16]  is built on ninefold's own infrastructure with servers in u.s and asia pacific because ninefold
[57.16 --> 62.26]  owns the entire stack from the hardware up they provide you with quantifiably superior performance
[62.26 --> 67.52]  compared to the competition with more economical scaling ninefold makes it extremely easy to deploy
[67.52 --> 72.14]  your rails application straight from your git repo by either using the online wizard or the command
[72.14 --> 79.46]  line interface ninefold also offers great support zero downtime deployment ssl redis memcache load
[79.46 --> 85.68]  balancers and firewalls for free straight out of the box experience ninefold superior performance
[85.68 --> 94.76]  and easy deployment with a 30-day free trial just visit ninefold.com to sign up and now on to the show
[94.76 --> 103.54]  welcome back everybody we are joined today by postmodern to talk about ch ruby or truby um not
[103.54 --> 107.58]  really sure the correct pronunciation there we'll let postmodern give us the definitive answer at some
[107.58 --> 113.92]  point uh ronin ch gems and a number of other projects that uh postmodern has been working on so
[113.92 --> 117.72]  to get started here why don't you give us an introduction of kind of who you are and where
[117.72 --> 124.16]  you come from and projects that you're working on hello um i'm postmodern uh i write a lot of ruby by
[124.16 --> 130.72]  trade um kind of uh ch ruby and ruby install were kind of more recent projects i wrote just out of uh
[130.72 --> 137.88]  sheer need of them so it's it's not like a real passionate kind of backgrounds um yeah so i hail
[137.88 --> 145.16]  from the the pacific northwest or cascadia as we like to call it got some friends there yep yep uh it's
[145.16 --> 154.36]  up in a little little teeny town uh portland's and uh kind of native uh for a long time but yeah um
[154.36 --> 161.34]  so mostly i do a lot of like security research i like developing tools and kind of automated attacks
[161.34 --> 168.22]  that that's really what i'm into and tickles my fancy and like as i kind of got more into using
[168.22 --> 174.82]  ruby forts i kind of like got into noticing the pain points and i thought well you know i've i've
[174.82 --> 179.74]  been working in ruby for a long time you know maybe i could try my hand at actually you know fixing
[179.74 --> 185.40]  some of these or making tools that uh kind of like fit and met my needs or you know solve my problems
[185.40 --> 191.86]  so that's uh that's kind of what i've been doing and you know yeah gotcha so real quick um just to
[191.86 --> 197.98]  just to kind of get a get an answer here i've always called it uh ch root but i could be wrong you're the
[197.98 --> 203.48]  security person so give us a uh what do you call it you call it ch root and then subsequently do you
[203.48 --> 209.62]  call it ch ruby or what should we be calling it man so i think it really depends on kind of the
[209.62 --> 215.62]  the people or the persons um everyone has their own weird pronunciation of all these unix utilities
[215.62 --> 220.82]  uh because they're kind of like they were designed to be easy to type out not really necessarily
[220.82 --> 230.18]  pronounce and so like i've heard uh ch roots i have heard ch roots um there are people actually like
[230.18 --> 235.80]  i don't know maybe once i've heard someone say like change roots actually like spell out the actual
[235.80 --> 241.98]  word so i really don't know um i don't know what the actual pronunciation is and i think it's more
[241.98 --> 246.64]  just like we it's not really necessary to actually say it out loud because we just type it so it's
[246.64 --> 251.98]  kind of like one of those things you're just like you know that thing yeah that thing yeah yeah yeah
[251.98 --> 256.98]  yeah i think i uh i'll stick with ch ruby then uh and whatever tickles your fancy i guess is the
[256.98 --> 261.64]  appropriate answer here in the pre-show you mentioned a funny one what was the funny one that uh for linux
[261.64 --> 268.26]  that that uh could be said kind of a funny way oh well um i don't know like it's kind of a weird
[268.26 --> 272.02]  thing like a lot of talking a lot of people everyone has their own pronunciations but um
[272.02 --> 278.78]  one of my friends was actually a while back doing research into using uh the upa np protocol or
[278.78 --> 284.80]  universal plug and play protocol which allows you know routers to open up ports uh for services and
[284.80 --> 289.56]  stuff like that um port forwarding and that but you can actually use it for punching holes in like
[289.56 --> 295.30]  you know firewalls on shitty neck your routers but uh he kept referring to the protocol as like
[295.30 --> 301.36]  up and up and so he's like yeah i'm looking into this uh up and up protocol like what is that well
[301.36 --> 306.52]  up and up is the protocol that lets you open up ports right it's it's on the up and up yeah
[306.52 --> 312.64]  no that's awesome so why don't you just for everybody that i don't know if you work in ruby and a lot of
[312.64 --> 318.22]  our listeners do i'm sure they've heard of rvm or rbm or chruby or whatever so why don't you kind of
[318.22 --> 325.10]  give us an introduction to just what what what is chruby what's the reason that it's here okay so
[325.10 --> 334.92]  um so i before chruby i actually used rvm a lot and i used it primarily on kind of like fedora
[334.92 --> 342.86]  that's kind of like my main operating system of choice um before that uh basically i kind of only
[342.86 --> 350.34]  used actually system ruby um because before that i was on gen 2 and actually no um so kind of a side
[350.34 --> 354.82]  note is fedora actually does a really good job of packaging ruby and they actually configure it
[354.82 --> 361.46]  they configure ruby gems to install into your local home directory for gems and when you're actually a
[361.46 --> 368.28]  normal user and when your roots it installs into usr local share wherever um so it really wasn't
[368.28 --> 375.14]  necessary to use rvm a lot because a lot of times i was just using the most recent version of ruby but
[375.14 --> 380.36]  you know when i actually needed to upgrade and you know test uh newer versions of 1.9 and 2.0
[380.36 --> 385.76]  then i kind of like okay i actually started using uh rvm and i was recommended to a lot of my other
[385.76 --> 391.26]  friends where i try and get up to speed in ruby and so they could help out with like open source
[391.26 --> 397.56]  projects collaborate together but anyways um one of the problems there's like a lot of the pain points that
[397.56 --> 403.10]  developed along with using the rvm extensively for a long time and one of the kind of the main ones is
[403.10 --> 409.74]  like yeah it's a huge collection of bash scripts and um bash is kind of a really terrible programming
[409.74 --> 415.38]  language and environments and that kind of contributes to the bugs and there's also platform
[415.38 --> 421.84]  specific issues where certain platforms will change things um and it has to be cognizant of all this
[421.84 --> 428.46]  and then there's also issues with how it organizes rubies um like if for instance you basically
[428.46 --> 432.88]  assumes that it should be installed into your home directory you can install it system-wide but
[432.88 --> 439.36]  the installation of the software is coupled to the location where it actually installs the rubies and
[439.36 --> 444.82]  that really kind of annoyed me because i really kind of wanted all my rubies out of my home directory
[444.82 --> 450.76]  i wanted my software installed globally so other users on my system maybe like i have some
[450.76 --> 456.94]  automated scripts that ran under like a you know dummy user account for safety reasons i wanted it
[456.94 --> 462.22]  to have access to it and i want to have rubies installed in some global location and then also
[462.22 --> 467.06]  have rubies installed in some like you know my home directory or you know i have other partitions
[467.06 --> 472.70]  where i usually just like a dump code where i want to like check out the latest version of rubinius
[472.70 --> 478.20]  so i'll pull that down some other directory and build it build it there and that really wasn't
[478.20 --> 485.26]  possible if rvm uh it will be possible if rvm2 with the ability to mount arbitrary installation
[485.26 --> 491.64]  paths where ruby is installed maybe you threw it in the opt directory or somewhere else so that was
[491.64 --> 497.46]  kind of one of the things and then eventually i like that just got so many bugs where i kind of
[497.46 --> 503.04]  like went back to using system ruby because it was just really useful and most of my work involved
[503.04 --> 510.30]  uh just developing against like you know 2.0 right and then using travis ci to test all the other
[510.30 --> 516.02]  versions right but then um i got like started a contract and i was like oh crap i'm gonna really
[516.02 --> 522.72]  need to get a working environment here that i can just you know use any sort of um version so i kind
[522.72 --> 526.56]  of got thinking about it and it's like you know usually when i start projects there's always this
[526.56 --> 532.06]  period of like deep thought and kind of research so i was kind of like do i really want to spend the
[532.06 --> 537.56]  time developing like a ruby switcher i mean there's rvm it's giant am i gonna like fall down the same
[537.56 --> 545.14]  path that um you know kind of like the the developers of rvm have like uh i believe uh wayne
[545.14 --> 550.28]  kind of got burnt out with dealing with all the issues and michael pappas is uh or michael pappas is
[550.28 --> 555.40]  doing a really good job of maintaining it but still like really stressful so i was like i went around
[555.40 --> 562.62]  and kind of like researched how rvm um basically like changed manipulate the path and then i also
[562.62 --> 568.88]  got uh i looked at rbm as i started like okay well let's let's look at the alternatives before i jump
[568.88 --> 573.72]  into like starting a huge project right before a contract job where i'm gonna have to be like
[573.72 --> 579.64]  heads down dedicated and so there's like lots of various other ruby switchers out there
[579.64 --> 586.94]  and um rbm is pretty much the only shims based ruby switcher and so there's kind of like issues
[586.94 --> 592.88]  when uh because i tried it when it was still kind of pretty new and fresh and so and it was kind of
[592.88 --> 599.50]  confused with how the shims worked and this they had like different levels of setting which desired
[599.50 --> 605.08]  ruby do you want like you had like that was it shell local system global or something like that yeah
[605.08 --> 612.66]  and then also i've i felt like it it copied a lot of features not copied but you know it re-implemented
[612.66 --> 620.32]  a lot of rvm ish features so i kind of felt like it wasn't really thinking outside the box it wasn't
[620.32 --> 626.14]  like unthinking it was still kind of following in the shadow or the footsteps of kind of like how all
[626.14 --> 632.60]  of us rubyist have sort of like grew grew up expecting the environment to work in the tools and
[632.60 --> 638.42]  you know like even has a sub command feature which is like a very rvm ish thing in my opinion
[638.42 --> 643.12]  and instead of having multiple separate utilities and scripts that work together in conjunction
[643.12 --> 649.54]  has this huge like sub command thing um but yeah there's also lots of other weird ruby switchers it
[649.54 --> 653.96]  turns out that is like kind of looking around by the way i define ruby switcher as something that
[653.96 --> 660.30]  only switches the ruby version uh that seems to be the the thing that you say most is like this is just
[660.30 --> 666.24]  a switcher it doesn't install like rvm does it's one job of one job only which i guess falls back on
[666.24 --> 672.64]  your linux unix background too of of you know one job really well right and there's lots of other
[672.64 --> 677.46]  basically implement implementations of this and i found that like i kind of went through and kind of
[677.46 --> 684.00]  rated them or scored them on like uh features and it's uh one of the kind of the probably the most
[684.00 --> 693.58]  well-developed ones was uh rbfoo uh were by hmans that's his github handle and so i tried that i was
[693.58 --> 697.74]  like okay this might be it's not what i'm looking for and because they just need something really
[697.74 --> 703.24]  minimal that just manipulates path and you know sets some couple environment variables you know it
[703.24 --> 709.48]  shouldn't be this hard and so i looked at it and like some of the things were nice um but one of the
[709.48 --> 713.62]  things that kind of annoyed me with it was kind of the syntax so when you actually type the version
[713.62 --> 719.76]  for some reason he like began the versions with an at sign and then there was also kind of the whole
[719.76 --> 724.92]  coupling where it expected the rubies to be in your home directory and sure you could probably sim
[724.92 --> 729.16]  link them out but i really want to have like a configurable list where i just give arbitrary paths
[729.16 --> 734.92]  right and then also i noticed a lot of these ruby switchers would always sets what they would hard
[734.92 --> 741.28]  code the gem path and gem uh gem home which are kind of the locations where it should look up the
[741.28 --> 749.30]  ruby gems and one of the things that kind of annoyed me is the so when you install since was it ruby 1.9
[749.30 --> 756.40]  ruby gems has been uh shipped with ruby so it actually ruby gems has its own main gem directory
[756.40 --> 763.06]  inside ruby and actually now ruby comes with some uh pre-installed gems like a big decimal
[763.06 --> 770.82]  um what was it io console uh some other ones i can't remember off the top of my head but anyways
[770.82 --> 778.54]  so it's really important that first of all you're not supposed to assume that the gem directory of
[778.54 --> 785.50]  that's in the main ruby install is always in that location because rubinius actually has its own also
[785.50 --> 790.56]  gem directory that they that's you know kind of in when you install rubinius it also installs its own
[790.56 --> 795.84]  gem directory and said not in the same location which is kind of a little annoyance but um also
[795.84 --> 803.00]  the fact that the uh you need the actual api version of the ruby so for instance uh this is not the
[803.00 --> 808.62]  actual version of the ruby but the actual kind of overarching api version like you know um all the
[808.62 --> 816.42]  1.8 series it was just 1.8 but since uh mri 1.9.0 was kind of a botched release that had like some
[816.42 --> 822.72]  showstopper bugs in it they actually bumped the api version to 1.9.1 so that's kind of another kind
[822.72 --> 830.78]  of like hiccup you have to detect and then also um the gem directory might not be writable um people
[830.78 --> 835.12]  assume it's going to be writable because the ruby install is in your home directory and you probably
[835.12 --> 839.40]  have a writable access to that and i kind of felt that that was kind of violating the whole unix
[839.40 --> 845.84]  principle of uh keeping software separate from the users so you don't actually delete it or you know
[845.84 --> 851.04]  download some weird virus and you know embeds itself in the software you have writable permission
[851.04 --> 857.10]  separation where you you would separate the gems you installed as a user versus the gems you install
[857.10 --> 863.48]  as roots which is something also i i you know copied from how fedora sets theirs up and i think uh
[863.48 --> 870.64]  deviant also has updated has done something similar and also wanted basically be able to switch between
[870.64 --> 875.78]  rubies from arbitrary locations and it would just automatically detect the gem directory
[875.78 --> 881.70]  and calculate it all out the other thing uh that also annoyed me about using rvm was the fact
[881.70 --> 887.08]  that they made gem directories specific to each patch level which was really annoying when you upgrade
[887.08 --> 891.82]  because you have to upgrade all your gems and like it's only a patch level guys it's not like
[891.82 --> 899.30]  a big feature feature breaking version release um so that's kind of like that i put all that together
[899.30 --> 903.08]  i think i spent about a week week and a half kind of like doing all this research and
[903.08 --> 908.98]  kind of like figuring out the features and how to go about doing them and uh kind of wrote up my
[908.98 --> 914.02]  first initial version and so so you spent the the couple weeks trying to figure out the features
[914.02 --> 919.50]  and then the feature you landed on uh the feature set you landed on is like very very small it's
[919.50 --> 926.46]  interesting and just to clarify like we've had kind of the longer this show goes on like in terms of
[926.46 --> 932.06]  the changelog as a whole not this particular show uh we've obviously had like predecessors and then
[932.06 --> 938.04]  like current the new hot and then you know the the future people will inevitably come but just to
[938.04 --> 943.50]  just to make sure that nobody here it thinks this way like we're not here to disparage against any of
[943.50 --> 947.96]  the previous ones because what they do is they they set up a path and like a you know you can learn
[947.96 --> 955.14]  lessons and ch ruby has in postmodern has benefited greatly from the things that the the ones before
[955.14 --> 963.64]  him have done and so yeah go ahead uh also i was going to point out that uh uh michael pappas uh the
[963.64 --> 969.52]  current maintainer of rvm1 and also who's working on rvm2 basically i kind of showed it to him and
[969.52 --> 975.12]  this was like the first version of ch ruby which didn't even support auto switching and he was like
[975.12 --> 982.36]  oh great another ruby switcher you know oh you're gonna gonna just you know disparage rvm and you know
[982.36 --> 987.86]  poo poo on it and like it was like no no no it's just completely different scale down it only does
[987.86 --> 992.96]  this one thing it's not supposed to try it's not trying to compete with rvm or even rbm as far as i
[992.96 --> 998.64]  can tell too when michael was on the show recently too he was saying that rvm 2.0 was going to expand
[998.64 --> 1004.42]  not only into ruby but also python and be and go beyond so i mean i think he had like this much
[1004.42 --> 1010.48]  larger scope to go towards yeah he's talking about basically um also integrating with the package
[1010.48 --> 1017.02]  manager and so it's very similar to certain things like um oh red had has a single was it software
[1017.02 --> 1022.26]  collection layers or something like that but basically he wants uh an environment manager
[1022.26 --> 1028.34]  literally and it's something that can install my sequel and dump a really nice auto you know
[1028.34 --> 1034.70]  basic configuration so you can you know start using it out of the box um yeah but and also he's
[1034.70 --> 1039.92]  helped me a lot with a lot of the bash issues and sort of bouncing ideas off him like well how did rvm
[1039.92 --> 1044.94]  handle this weird obscure that's awesome honestly i mean michael's a good guy i know he took over for
[1044.94 --> 1051.52]  wayne when when things kind of got harder for him and we've had uh several people on the show come and
[1051.52 --> 1059.14]  talk about um burnout i can't recall his name andrew helped me out but he was um on just like four or
[1059.14 --> 1064.52]  five shows back names gap me right now i have to look at our show list but i think to andrew's point
[1064.52 --> 1069.88]  was to say that you know we're not here to bash any predecessors we're here to this is open source
[1069.88 --> 1076.76]  things change software is the most complex volatile market ever so i mean obviously that's the case we
[1076.76 --> 1082.30]  love mike we love rvm and but we we lift up everybody to to kind of get their word out and what they're
[1082.30 --> 1088.54]  doing and why it's important and why rubia should care yeah yeah definitely let's pause the show for just
[1088.54 --> 1093.54]  a minute give a shout out to our sponsor code chip they're also a partner of ours so super excited to be
[1093.54 --> 1098.44]  working with code chip they're a hosted continuous deployment service that just works you can easily
[1098.44 --> 1104.40]  set up continuous integration for your application today in just a few steps and automatically deploy
[1104.40 --> 1109.68]  when all your tests pass code chip has great support for lots of languages test frameworks as well as
[1109.68 --> 1116.38]  notification services they easily integrate with github or bitbucket and can deploy to cloud services like
[1116.38 --> 1123.50]  heroku aws nojitsu google app engine or even your own servers get started today with
[1123.50 --> 1130.44]  their free plan setup only takes three minutes head to code chip.io and also check out their blog
[1130.44 --> 1139.44]  blog.coachip.io and one more thing to mention for our members you can save between $294 and $2,994
[1139.44 --> 1145.34]  on your first year with code chips so make sure you take advantage of that head to the change all.com
[1145.34 --> 1155.34]  benefits to learn more once again code chip.io try it today so to kind of move forward the when i first
[1155.34 --> 1162.28]  found chruby which was i don't you know maybe 10 months ago a year ago 15 i don't know so somewhere in
[1162.28 --> 1169.50]  the past uh the way that everyone was using it was uh basically using ruby build which was built by sam
[1169.50 --> 1177.62]  stevenson and others um i think originally just was supposed to be purely for rbm and then they
[1177.62 --> 1184.14]  decided to like make it easier to use as a standalone thing and so chruby was just a switcher and a lot
[1184.14 --> 1190.94]  of people were using ruby build to actually install rubies um and uh just recently i you know went back
[1190.94 --> 1197.68]  and started evaluating these things again and i saw that now there's ruby install um which essentially
[1197.68 --> 1204.24]  does the same thing as ruby build it actually allows you to install rubies so why so i obviously
[1204.24 --> 1208.46]  we see why you you created chruby and you know looking at all the other ones what about that
[1208.46 --> 1214.84]  why did you create ruby install so initially i also used ruby build because you know it's it was a nice
[1214.84 --> 1219.90]  decoupled tool and i could just use it for its one specific purpose but there's lots of things about
[1219.90 --> 1225.00]  it that kind of got under my skin and so i started this whole process of kind of like evaluating it
[1225.00 --> 1231.62]  and evaluating how rvm also handles uh compiling installing and of course they go into way more
[1231.62 --> 1238.54]  detail of handling weird obscure uh platform specific issues but um so what the way ruby build
[1238.54 --> 1246.26]  works is it has basically definitions for every single version so literally you can you can you have to
[1246.26 --> 1250.94]  actually specify the fully qualified version and that was kind of one annoyance because literally i just
[1250.94 --> 1257.16]  i when i install uh you know some version i really don't care just won't give me the most recent 193
[1257.16 --> 1264.20]  that you know of um or you know literally copy and paste the version from uh the the news the news
[1264.20 --> 1268.76]  announcement on ruby lang when they release a new version they're it's going to be there so just copy
[1268.76 --> 1274.52]  and paste in the command line but then as i kind of like dug into it more um that was kind of a minor
[1274.52 --> 1280.28]  nuisance but um i dug into it a lot more i found that it does lots of really weird things with
[1280.28 --> 1288.18]  trying to detect um kind of when libraries are available and it also can download um its own
[1288.18 --> 1294.26]  versions of open ssl and compiles those and then links ruby against that and that kind of like that
[1294.26 --> 1298.22]  worried me because i automatically knew that eventually there's going to be a vulnerability
[1298.22 --> 1304.18]  in these libraries and there's not going to be an easy way to to update them you can't just go
[1304.18 --> 1309.48]  like oh update the library like it's it's compile installed into its own directory and literally you
[1309.48 --> 1314.16]  have to reinstall the rubies to cause to force the newer version to get downloaded and then
[1314.16 --> 1319.14]  the ruby compiled against the newer version so i was kind of like well obviously that's kind of a
[1319.14 --> 1324.88]  that should be another feature is just use the package manager uh because every system the packages are
[1324.88 --> 1331.12]  there available you can compile against them and they die the ruby dynamically links against them and so
[1331.12 --> 1336.96]  when there's a vulnerability you just update the package you're good go and also distributions are
[1336.96 --> 1341.78]  really good about backporting security fixes and so you can update and not worry about getting weird
[1341.78 --> 1348.76]  api breakage um you literally just get that one fix so that was kind of another thing that inspired me and
[1348.76 --> 1356.36]  and i really just want something that would work on as many systems against many package managers as
[1356.36 --> 1362.72]  possible and of course it's a lot easier because uh chruby has to work in both bash and zsh
[1362.72 --> 1368.90]  whereas ruby install was a utility and so i could just write against bash 3 and uh do that
[1368.90 --> 1379.00]  yeah and so and i basically kind of took a very um declarative uh design to it where literally you
[1379.00 --> 1384.94]  have like individual files build files for each major implementation and they define the configuration
[1384.94 --> 1391.82]  step the compile step and the install step and then kind of like any sort of specific uh package
[1391.82 --> 1396.20]  manager configuration like you have to do some weird things with homebrew because its packages
[1396.20 --> 1404.08]  aren't in like a place where a lot of the um the auto the auto conf scripts of mri can find them so
[1404.08 --> 1409.68]  you have to literally hint at it which is something i learned from uh rvm where there's an option call
[1409.68 --> 1416.30]  was it with opter and you have to pass that in specifically for homebrew and and mac ports also
[1416.30 --> 1423.16]  because mac ports installs in that's still around um yeah yeah actually and i got a recently got a uh
[1423.16 --> 1431.10]  a bug report from a user who was attempting to use think which is like super old yeah and like back in
[1431.10 --> 1436.60]  the day actually i had was at the uh the last generation ibook and it's i ran osx for a while and
[1436.60 --> 1443.36]  then uh back when it's like power pc and i went back to uh running like linux on it so i knew about think
[1443.36 --> 1450.54]  and i was like whoa that's still what's people use that still but yeah oh yeah just glancing at the
[1450.54 --> 1455.58]  glancing at the project home page they are still getting regular releases which is pretty cool to
[1455.58 --> 1462.66]  see it lasting this long yeah that's cool so i guess that's a you kind of hit on uh you had a a
[1462.66 --> 1470.92]  not a feature request but a bug report and uh you do the ch ruby and ruby install they do such
[1470.92 --> 1478.52]  small things so how often like ch ruby is 90 lines of code right so maintaining this seemingly would
[1478.52 --> 1484.56]  be much easier than maintaining rvm uh so how much of your time do you have to dedicate to actually
[1484.56 --> 1491.04]  maintaining ch ruby um it's pretty much feature complete at this point uh basically i'm sort of
[1491.04 --> 1495.30]  waiting it's kind of one of the first projects where i've been really skeptical about feature
[1495.30 --> 1500.90]  requests uh normally a lot of my projects i'm like always trying to please whoever is submitting the
[1500.90 --> 1505.32]  issue and you know thinking up crazy new features to add this is the first one where i actually
[1505.32 --> 1511.06]  really constrained myself and that was caused primarily because the lot of the line uh line
[1511.06 --> 1517.90]  count uh limitation because i want to keep it the core of it in 100 lines and um of course there's
[1517.90 --> 1522.80]  other additional things like the the auto switching but that's in a separate file that you can choose not
[1522.80 --> 1529.02]  to load because a lot of um on a previous job there's worked with this system administrator who just
[1529.02 --> 1534.62]  like cringed at the idea of having some sort of crazy bass script that you know auto detects and
[1534.62 --> 1540.64]  switches rubies when you see the injured directories and so um but yeah so that really has kind of
[1540.64 --> 1544.48]  constrained me and that's going to kind of really interesting where i actually really critically look
[1544.48 --> 1549.52]  at features and whether they can be uh implemented by like third party tools or if they have to
[1549.52 --> 1555.02]  integrate it or do we even really need them because a lot of the feature requests were uh basically
[1555.02 --> 1561.82]  things that people are used to coming from rvm and i kind of think like well do we really need this
[1561.82 --> 1568.54]  like or is this is something we're really kind of familiar with and we miss did i miss why you said
[1568.54 --> 1574.50]  that there's a constraint why the hunter line constraint so basically i wanted to keep it as small as
[1574.50 --> 1581.12]  possible i didn't want to like go out of control and you know develop a you know a sub command system
[1581.12 --> 1586.90]  or any of these other things that the bigger kind of ruby switchers managers have and so i kind of
[1586.90 --> 1591.50]  like i always kind of like look down on the whole idea of like putting line constraints line count
[1591.50 --> 1596.52]  constraints on projects as kind of like it's kind of like a hat trick you know it's kind of like vim golf
[1596.52 --> 1603.62]  yeah but really it does it does help you it forces you it like it sets a real kind of like um
[1603.62 --> 1610.02]  like risk points or danger point where it's like you cannot pass this line that's this invisible barrier
[1610.02 --> 1617.30]  once you do you're in some danger right and um yeah and so that that's that's kind of helped me
[1617.30 --> 1622.04]  um dealing with maintenance uh there was a period when i first rolled out the auto switching that i
[1622.04 --> 1627.36]  did have to deal with tons of bugs and weird shell issues and so i spent a lot of time asking stupid
[1627.36 --> 1633.32]  questions in the bass irc channel and getting really kind of like burnt out uh disgruntled replies
[1633.32 --> 1643.32]  and um stop asking yeah i know it's like rtfm dude but um yeah so that that kind of did take up
[1643.32 --> 1648.64]  some time but since it was so small a lot of the changes just required thinking really carefully
[1648.64 --> 1655.10]  about kind of the trade-offs that's another thing about shell scripting is it seems simple on on its
[1655.10 --> 1661.10]  face but every single command every serve behavior has like a dozen or so edge cases you have to be
[1661.10 --> 1667.58]  cognizant of and then there's also implementation differences between the shells uh based on like
[1667.58 --> 1674.72]  what's how they evolved because like bash came from ash um and there's also dash which is the
[1674.72 --> 1681.12]  bin sh on dbian systems which is like super minimal it has barely anything like most bash code will not run
[1681.12 --> 1689.56]  on it um and then zh zsh actually came from ksh and they have their own weird bizarre features um that many
[1689.56 --> 1694.46]  people probably don't know about for instance arrays and zsh are index starting at one not zero
[1694.46 --> 1700.00]  so i can't really rely on that yeah i know they they thought it was a really cool feature that's
[1700.00 --> 1705.80]  stupid sorry yeah i know yeah but uh yeah the kind of way to get into that the more you have to like
[1705.80 --> 1710.72]  sit there and actually test and ponder and that's actually the other thing is i was really super
[1710.72 --> 1717.04]  aggressive about unit testing shell scripts and it always seems like when you when new languages
[1717.04 --> 1724.40]  come about that don't have like test suites or people kind of like misinterpret the language or
[1724.40 --> 1729.32]  like i don't know they think it's really simple they always like say oh we don't need a test why
[1729.32 --> 1734.72]  would you test that just just run it from the command line yeah you don't need unit tests here
[1734.72 --> 1739.36]  and people said this for like javascript when it was first starting out when like you know most code was
[1739.36 --> 1745.22]  just like three functions and then they also said about bash script but then once the testing tools get
[1745.22 --> 1751.98]  developed and people get you know used to them it really does help and that helped uh kill a lot
[1751.98 --> 1758.50]  of bugs and actually it was really cool because a lot of the other people who developed their own
[1758.50 --> 1764.52]  ruby switchers uh came in and started like uh suggesting features and you know how to solve
[1764.52 --> 1770.74]  various implement the auto switching so we actually were discussing this in issues by sending submitting
[1770.74 --> 1777.02]  pull requests for example unit tests so we really were just like speaking using the test as the
[1777.02 --> 1781.94]  implementation and so that's really cool to see uh instead of like you know getting these long-winded
[1781.94 --> 1788.04]  discussions and issues and we could just be like here's the code yeah and i can imagine that like
[1788.04 --> 1792.30]  looking through pull requests you know kind of as an aside here looking through pull requests and stuff
[1792.30 --> 1799.64]  for shell can kind of be kind of a disaster right somebody like submits all this code like yeah you
[1799.64 --> 1805.58]  have to understand it and like yeah everyone has their own weird styles yeah there is although um shell
[1805.58 --> 1813.52]  scripting does it's probably even more style obsessed than ruby is uh there's this one user who uh
[1813.52 --> 1819.10]  contributed came in and basically just like submit submitted this giant pull request that broke all the
[1819.10 --> 1823.54]  test and he's basically trying to rewrite it from scratch and like it's like whoa slow down let's
[1823.54 --> 1830.62]  take this one step at a time and basically kind of like he got me to um fix all the style issues
[1830.62 --> 1835.48]  and wow like for instance there's like very hardcore these style issues are not just like
[1835.48 --> 1840.14]  you're supposed to do it because it looks nice but there's actually safety reasons behind it
[1840.14 --> 1845.14]  for instance most people uh when they start doing shell script they always see uppercase uh variables
[1845.14 --> 1852.08]  so they just assume all variables are uppercase but all script local variables all function local
[1852.08 --> 1857.72]  variables are supposed to be lowercase so they don't overshadow the other global variables that
[1857.72 --> 1863.50]  are passed in as an environment variables quote um yeah so that's kind of like one of the major
[1863.50 --> 1869.36]  things we had to change and yeah there's other stuff that's crazy so awesome have you had any other
[1869.36 --> 1874.90]  projects that have gotten as popular in the open source community as these geez um
[1874.90 --> 1879.34]  trying to think here
[1879.34 --> 1889.90]  maybe maybe bundler audits that's that's probably it um or actually there's another um library i did where
[1889.90 --> 1896.28]  after ruby 1.9 came out ruby zip was kind of unmaintained for a long time it didn't work
[1896.28 --> 1901.18]  and so i just got frustrated and forked it and you know tried to get it working in 1.9
[1901.18 --> 1905.68]  and released kind of another gem and apparently that got a lot of downloads because a lot of
[1905.68 --> 1910.74]  people are just like i just need this library to freaking work yeah well the reason i ask is because
[1910.74 --> 1915.46]  you know you're we were talking about like ctfs before the show and just like your attitude um
[1915.46 --> 1923.92]  seems you know you go by an alias and so it seems like privacy is a important thing to you i mean you're
[1923.92 --> 1928.78]  into security and all that so i wonder like was there any implications for you of like just getting
[1928.78 --> 1935.34]  popular like and getting like notoriety and getting pointed at for a lot of stuff well um i'm very
[1935.34 --> 1942.08]  like i've always been very anti-celebrity anti kind of cult of personality um coming from like the
[1942.08 --> 1948.96]  security hacking world uh it's it's a huge problem um like there's like you there's like you go through
[1948.96 --> 1954.52]  cycles where like someone will rise to fame and they'll be speaking at every conference and usually
[1954.52 --> 1962.16]  uh often recycling their you know previous talk and um and kind of that that community has developed
[1962.16 --> 1968.20]  this huge kind of like immune response to that where if you're not putting out um actual useful
[1968.20 --> 1974.76]  information new information new research um they quickly kind of like forget about you and sort of
[1974.76 --> 1979.62]  just like whatever like if you're just sort of being a thought leader uh you're not really as valued as
[1979.62 --> 1985.58]  much as someone who's actually doing like really useful work so yeah i guess um i'm very cognizant
[1985.58 --> 1991.50]  about not doing not doing that and one of the things i make sure to do is always give credits to
[1991.50 --> 1999.84]  the contributors and i also got a shout out for um uh the user havenwood on github has been a huge help
[1999.84 --> 2006.92]  in maintaining uh ch ruby has helped with uh always submitting um the homebrew uh rest updated homebrew
[2006.92 --> 2012.14]  recipes to homebrew and testing things on osx because i don't have an osx system currently so
[2012.14 --> 2019.20]  and it's like huge help so it's just not me being all like i'm not super genius here developing it like
[2019.20 --> 2025.28]  in a vacuum uh no yeah actually that's one thing that that kind of struck me as surprising is that
[2025.28 --> 2031.14]  ch ruby has 30 contributors on github um so obviously there's a number of contributors that actually
[2031.14 --> 2035.92]  probably not obviously but i would assume there's a number of them that have not actually uh you know
[2035.92 --> 2040.08]  contributed to the shell scripts themselves but to other things around them but but it's still i
[2040.08 --> 2044.26]  mean like it's 90 lines of code in the shell script and you have 30 contributors it's like that's a
[2044.26 --> 2048.66]  pretty big ratio and i think that's neat i think that's cool to see so many people like pitch in and
[2048.66 --> 2052.62]  help on different angles and you said like with the homebrew and you probably have people that have
[2052.62 --> 2056.38]  just updated the readme but people care about this and what you're doing and that seems pretty cool
[2056.38 --> 2062.00]  and also i think what came out of it was i wrote a generic make file because i was kind of annoyed
[2062.00 --> 2068.14]  of how all these shell script projects either they had this really simple install.sh file or they like
[2068.14 --> 2072.92]  you know you curl down and install script i just really wanted a simple make file they just installed
[2072.92 --> 2078.72]  worked on bsd and linux and like because there's issues with the version of make on bsd and linux uh
[2078.72 --> 2084.54]  the gene you make versus the bsd make and so a lot of those like there's like i guess you have a lot of
[2084.54 --> 2088.90]  casual contributors and they fix kind of the minor things i think that's really also important open
[2088.90 --> 2094.92]  source too um if you see a minor bug you should probably at least report it or fix it um because
[2094.92 --> 2101.60]  every little fix counts it does add up and even if it's like typos in the readme or you know this is
[2101.60 --> 2106.42]  a jumping forward but just on the i hate to put a lot on me because i don't like to do that whatsoever
[2106.42 --> 2114.30]  but you know you talk about little fixes that had a little fix in your public uh ronin um which was
[2114.30 --> 2118.86]  like because i was doing some research for the call and i was like oh this link is off but the
[2118.86 --> 2124.10]  coolest thing about github is that let me easily click edit fix the link for you and submit a pull
[2124.10 --> 2130.10]  request you know in a couple clicks and you know steve kladnik had an awesome post on the changelog
[2130.10 --> 2134.08]  i think about a year and a half back that still gets tons and tons of reads we'll link out to in the
[2134.08 --> 2139.44]  show notes if you're listening to this but you know like he had said all those little fixes 30 contributors
[2139.44 --> 2144.78]  they may not have done the heavy lifting but they're they're keeping a line on the edges you
[2144.78 --> 2150.92]  know that that you forget or you miss it's sort of the uh long tail yeah long tail principle where
[2150.92 --> 2156.06]  the casual contributors do actually add up over time and it's also kind of minor things do actually turn
[2156.06 --> 2161.44]  away a lot of potential users and so that's kind of when you do release code you have to be kind of
[2161.44 --> 2167.30]  ocd about that um if you see a typo in the readme they're probably gonna like they're gonna be biased
[2167.30 --> 2172.00]  automatically against the against the project um but yeah the funny thing about that typo was
[2172.00 --> 2181.18]  uh when github changed to all the user pages to like github io um i have this git alias get said
[2181.18 --> 2187.44]  so i can actually do mass find replaces and i end up breaking the url on every single page and so
[2187.44 --> 2194.02]  i had to undo that yeah i'm sure that was fun to fix so good really easy using get said but well
[2194.02 --> 2198.18]  it was a noise yeah i literally changed two characters which was awesome
[2198.18 --> 2206.02]  so going then to ronin i think ronin uh look at through all the projects that were listed i think
[2206.02 --> 2211.86]  ronin was the probably the first one uh well not the first one but one of the bigger ones that i've
[2211.86 --> 2215.54]  heard about um from you so why don't you talk a little bit about ronin and what it is and what's
[2215.54 --> 2221.84]  the purpose oh yeah so uh back in the day i was working in a computer security research group uh we had
[2221.84 --> 2227.14]  this project um well i mean i was like thinking like well uh you know ruby is a really great
[2227.14 --> 2232.18]  language for doing dsls uh there's already like you know you could think of rails as kind of a
[2232.18 --> 2236.74]  dsl framework uh for doing web development because they kind of wrap everything up and
[2236.74 --> 2242.40]  nice helper methods and so it like it abstracts away a lot of the complexities like i'm talking
[2242.40 --> 2249.14]  like rails 2 old school um now it's really complex these days but uh so i kind of thought like
[2249.14 --> 2253.04]  well hey this ruby language might be pretty useful uh because like i was looking at the
[2253.04 --> 2258.80]  documentation for instance they have like a telnet module and it's really nice we can use the blocks
[2258.80 --> 2263.98]  to automatically set up the telnet session handle it and tear it down so i was like wow this can
[2263.98 --> 2269.14]  actually be pretty useful for writing exploits because exploits really aren't that complex code
[2269.14 --> 2275.90]  wise and you could also then write a lot of the helper methods and make everything basically one
[2275.90 --> 2281.34]  basically doable in one line of code where you just string together the helper methods
[2281.34 --> 2287.22]  and so that was kind of my um my project with ronin was to create an environments
[2287.22 --> 2292.64]  uh with kind of like active support type library called run support that provided all the helper
[2292.64 --> 2297.64]  methods which are called convenience methods uh for various things that like security research need to
[2297.64 --> 2304.34]  like all the time and then provide kind of a main kind of console environments and then a system for
[2304.34 --> 2310.04]  installing repositories of other people's code um because you know back back within people are
[2310.04 --> 2316.84]  still using ruby gems dot ruby forge dot org to distribute so it's a lot easier um for your kind
[2316.84 --> 2322.14]  of average security researcher who isn't really like a top level developer they're that's not what
[2322.14 --> 2327.22]  they're after they're like trying to do research and break things and find cool vulnerabilities and so
[2327.22 --> 2332.12]  it was kind of a lot easier in my mind it's like basically just have a repository system they can give
[2332.12 --> 2338.80]  a url and it'll pull down some svn or a git or whatever um directory of their code and
[2338.80 --> 2344.08]  pull it all together but yeah it's kind of one of my big one of my first big projects and that
[2344.08 --> 2351.38]  spawned a lot of different other libraries and gems and then because like a lot of code got pulled out of
[2351.38 --> 2357.34]  it as it kind of matured um so a lot of useful code kind of got split out of that so and i was kind of
[2357.34 --> 2364.36]  following the uh the model that data mapper uh followed that's basically they split everything up into
[2364.36 --> 2371.62]  uh smaller amounts smaller libraries over time and so i was kind of like doing that but um
[2371.62 --> 2377.36]  yeah so i kind of got caught up in work and so i like kind of like put ron more to the to the side
[2377.36 --> 2382.04]  but now i'm sort of like thinking about how things have changed and definitely want to get back on the
[2382.04 --> 2388.98]  project and simplify some various things so you do plan to get back into ronin that's oh yeah yeah
[2388.98 --> 2394.46]  gotcha there's a lot of unfinished code in there gotcha so this is an interesting i i think this is
[2394.46 --> 2399.06]  interesting to me because you were kind of doing security research with ruby four years ago and
[2399.06 --> 2407.10]  the amount that ruby has changed in the last four years or you know in the last x years uh
[2407.10 --> 2411.86]  i mean you've had to keep up with a lot of change so what has the process been like maintained i think
[2411.86 --> 2417.28]  this might be one of the oldest uh actual like uh projects that is still maintained that we've
[2417.28 --> 2422.94]  actually had on the show what's that been like oh yeah well i mean there's those periods of rapid
[2422.94 --> 2428.12]  growth in the ruby community where we had things like uh you know we switched uh we switched
[2428.12 --> 2433.64]  jeweler and then we switched off jeweler and then we had bundler and then we kind of like
[2433.64 --> 2438.14]  there's all these kind of evolution of tools and so it's kind of really difficult to keep up and we
[2438.14 --> 2444.20]  you know we went we transitioned from ruby forge to ruby gems uh then rvm came along so it's kind of
[2444.20 --> 2449.92]  difficult to keep up all these tools and actually found myself kind of like gradually moving away from
[2449.92 --> 2456.32]  the tools or not just like it seemed like when any of these tools came out we everyone just sort of
[2456.32 --> 2461.96]  like we must use this everywhere possible all the time irregardless and i kind of found myself that
[2461.96 --> 2468.72]  it's really not that necessary for instance if your library has like one or two dependencies and
[2468.72 --> 2474.10]  they're probably installed anyways like the json gem or rake you probably don't you don't need bundler
[2474.10 --> 2481.68]  and um so yeah i'm like and also kind of developing these tools that these libraries they were kind of
[2481.68 --> 2486.40]  my like personal playground and so i did kind of like develop tools based out of that because i got
[2486.40 --> 2493.96]  tired of like having to always edit the read me that was generated by jeweler or or by hoe or by uh
[2493.96 --> 2498.96]  bundler i just wanted to like project set up automatically with like rspec and all that stuff
[2498.96 --> 2506.82]  and so i kind of wrote like a uh or which is like a project skeletoning tool and says it has been a bumpy
[2506.82 --> 2512.54]  road and it's especially annoying when there's like issues with ruby upstream um like kind of the
[2512.54 --> 2519.32]  major like whatever like open ssl would break things or um but at the same time it has been nice where we
[2519.32 --> 2524.44]  did develop tools to deal with that's where i for instance like a long time i just always recommend
[2524.44 --> 2531.18]  people to install rvm first and then you know before installing ronin and like install the latest version
[2531.18 --> 2537.32]  but at the same time i kind of felt like you know we were moving a little too quickly and maybe it
[2537.32 --> 2542.48]  would have been a little better to sit back and kind of like reevaluate what what our actual needs
[2542.48 --> 2549.16]  are because like for instance the same thing with how um rbm kind of um inherits a lot of the features
[2549.16 --> 2556.96]  and like uh ways of doing things from rvm you kind of also saw that in bundler about how bundler
[2556.96 --> 2564.76]  basically also developed its own little static project generation tool and which like was basically
[2564.76 --> 2571.84]  constantly being changed and updated and because it's really hard to get get rights first um because
[2571.84 --> 2578.90]  everyone has like little nitpicky uh changes to like how they want projects generated and um or it also
[2578.90 --> 2584.28]  has like you know it embeds their own release tasks which are kind of like crummy they don't they
[2584.28 --> 2590.40]  don't use proper rake file tasks and so you know like always rebuild your gem irregardlessly of even
[2590.40 --> 2595.62]  if no files have changed so i kind of felt like uh you know maybe a little better to actually like
[2595.62 --> 2601.06]  slow down and kind of like take stock of things uh so i'm just constantly racing around trying to
[2601.06 --> 2610.00]  release versions all the time yeah so one thing i wanted to to kind of bring up the we forgot to talk
[2610.00 --> 2614.50]  about this before actually um with ch gems and and sorry to kind of do a huge context switch here
[2614.50 --> 2620.70]  uh we actually didn't talk about ch gems can you just give me a just uh kind of introduce what ch
[2620.70 --> 2626.30]  gems is real quick and i have a question about it for you so ch gems was sort of my attempt to kind
[2626.30 --> 2631.96]  of rethink gem sets because one of the kind of assumptions that go along with gem sets is they're
[2631.96 --> 2639.00]  always named and they always are stored in your dot gem directory wherever that is and i kind of want
[2639.00 --> 2644.56]  and then also they had to be implicitly uh like auto switched so which kind of did make sense
[2644.56 --> 2651.94]  because the majority of the time like you would have this like rvm gem set file and it would have
[2651.94 --> 2657.08]  a name in it and would use that gem set when you cd'd into the directory it would then activate the
[2657.08 --> 2662.34]  gem set and i kind of thought that this was like first of all like uh it didn't feel too comfortable
[2662.34 --> 2667.08]  of having like this automatic feature and i didn't really agree if always having the gem sets in
[2667.08 --> 2672.90]  and your home directory is like why not just put the gem set in the actual project directory
[2672.90 --> 2680.44]  in the same way that uh you know you can do uh bundler install and put everything in vendor gems
[2680.44 --> 2686.22]  and then i kind of decide well let's take a different approach because there's like apparently also a lot
[2686.22 --> 2692.52]  of people wrote their own kind of gem set replacement scripts there's like oh my gems there's is it rev
[2692.52 --> 2700.16]  that's one version and uh also it was a gs gem switcher and i basically just wanted to make
[2700.16 --> 2705.08]  something that instead of you actually have to like enter into a gem set and then leave because
[2705.08 --> 2709.90]  i always would find myself when using rvm gem sets forgetting that i was still in that gem set
[2709.90 --> 2715.28]  and being like oh hey that's that's why half my gems are missing yeah then you install a bunch of
[2715.28 --> 2719.20]  gems to the wrong gem set and get all pissed off and you have to clean it up right and like we're just
[2719.20 --> 2723.60]  like you forget about it you've made it for a project that like you know you wanted to make a
[2723.60 --> 2728.42]  couple line fixes to this like huge project that had zillions of dependencies and so you want to like
[2728.42 --> 2733.94]  isolate it some gem gem set and then you forget about it and like you don't remember it when you're
[2733.94 --> 2739.18]  like going around cleaning up your home directory wondering why you don't have any space left um
[2739.18 --> 2746.22]  yeah so i kind of like took the approach of uh ch root where you can uh basically explicitly
[2746.22 --> 2752.94]  enter into a project and then that starts a or like a system image and then it starts a subshell
[2752.94 --> 2757.50]  within that system directory and makes that the current route and it's kind of nice because you
[2757.50 --> 2763.44]  can basically exit out of the shell and you go back to your previous uh environments your previous
[2763.44 --> 2769.04]  system so i kind of felt that that was a really good model um basically explicitly like go into a
[2769.04 --> 2775.76]  project and then leave um but yeah there's actually some problems in rows with that and um
[2775.76 --> 2782.88]  because the way that ch ruby auto switching was expected to work uh people who use tmux for instance
[2782.88 --> 2791.20]  when they opened a uh split pane or another split terminal it didn't properly initialize or inherit the um
[2791.20 --> 2798.12]  the shell environments from the other terminal and so basically a lot of ch ruby i mean uh tmux users
[2798.12 --> 2809.16]  um requested that ch ruby always auto uh set the ruby version on on new subshells so uh so i had to
[2809.16 --> 2815.96]  make that change and that kind of ended up uh conflicting with ch gems because ch gems uh spawns a subshell
[2815.96 --> 2823.72]  and so there's kind of this weird kind of like race condition where um ch gems basically sets the gem home and
[2823.72 --> 2832.44]  gem path and then passes that to the uh subshell uh process and then when the subshell initializes uh
[2832.44 --> 2839.16]  basically then ch ruby loads and then it resets the gem home and gem path and so it's like it's
[2839.16 --> 2845.88]  it's a dicey kind of uh way to deal with it without coupling the tool the two uh tools together where right
[2845.88 --> 2851.88]  i didn't want to like have some sort of like flag of like you know do not reload ch ruby you know
[2851.88 --> 2856.56]  that would feel like a little too much coupling even though if even though if it was just one
[2856.56 --> 2863.38]  variable but like yeah yeah let's pause the show for just a minute give a shout out to our sponsors
[2863.38 --> 2868.46]  new relic if you've got a web or mobile application you need to know about new relic
[2868.46 --> 2875.24]  it's your new best friend basically it's your easy to use analytics dashboard that basically gives you
[2875.24 --> 2880.04]  powerful code level visibility into the real-time performance of your application so
[2880.04 --> 2886.14]  this means that you can spot bugs see bottlenecks and fix problems fast hopefully before they even
[2886.14 --> 2891.46]  affect your users and thanks new relic you no longer have to ship your app to production and
[2891.46 --> 2896.10]  then helplessly wait around hoping for the best until negative app reviews and tweets start to roll
[2896.10 --> 2902.80]  in new relic empowers you to to see what's going on and what's what is working and what isn't working
[2902.80 --> 2907.22]  all in real time and the way it works is really straightforward they give you a lightweight
[2907.22 --> 2912.94]  agent that you unpackage into your production level apps that agent sits around quietly and
[2912.94 --> 2917.84]  securely in the background kind of gathering real-time metrics across geographies devices
[2917.84 --> 2924.30]  platforms all the way down to the end user level and then displays all that data in real-time graphs
[2924.30 --> 2929.00]  so coders can have the visibility they need into the performance of their web applications
[2929.00 --> 2933.16]  and make everything awesome so go and check out new relic today by visiting
[2933.16 --> 2939.16]  newrelic.com slash the changelog to learn more and use the offer code the changelog and take advantage
[2939.16 --> 2946.46]  of this special 30-day extended free pro trial available exclusively to our listeners
[2946.46 --> 2953.72]  newrelic.com slash the changelog so it surprised me i don't know like i don't and i'm not really
[2953.72 --> 2959.34]  even necessarily sure why it surprised me but it surprised me that ch gems even exists in the first place
[2959.34 --> 2965.56]  yeah um it would be kind of nice if uh either this functionality was kind of like baked into
[2965.56 --> 2972.20]  ruby gems itself or uh which it actually you can do i mean literally just set gem home to some path and
[2972.20 --> 2980.82]  there you go uh just it's also the making sure that um the bin directory of the gem dur is uh you know
[2980.82 --> 2985.80]  takes precedence in the on the path so any serve executable in there you can just run and it'll go to
[2985.80 --> 2992.02]  that one and uh yeah and like that's another thing also kind of wish that uh bundler would kind of
[2992.02 --> 2997.90]  invest time into doing is provide some sort of shell script you can load that will automatically uh
[2997.90 --> 3004.06]  kind of like detect the bin stubs and put those in the path or use set up aliases or something
[3004.06 --> 3009.56]  just so you wouldn't have to bundle exec every time yeah or install or clutter your bin directory
[3009.56 --> 3015.52]  with bin stubs and like which can actually clobber existing files in there which is kind of annoying
[3015.52 --> 3022.36]  super annoying yeah and yeah so that was kind of like my kind of like trying to answer that but of
[3022.36 --> 3029.10]  course like it is kind of a difficult problem so is there a definitive blog post or write-up that
[3029.10 --> 3036.78]  kind of prescribes how to use uh ch ruby ruby install and ch gems just for i mean we got a lot of
[3036.78 --> 3042.80]  new listeners to the show that are just getting started and we have a lot of very seasoned developers
[3042.80 --> 3048.90]  also using it so we kind of have both chasms um and i'm not sure if i've ever seen a full write-up of
[3048.90 --> 3053.14]  like here's why you and i know you're kind of on the show to talk about it a little bit but here's why
[3053.14 --> 3058.36]  i did it here's you know why you should use it and here's the implications of using it these you know
[3058.36 --> 3064.58]  these several tools together is there a write-up that's just like clear as day so there's actually lots
[3064.58 --> 3069.66]  of write-ups um and i kind of let users write their own uh this is kind of the first usually
[3069.66 --> 3076.06]  um previous projects i'd always kind of like naively uh kind of put together this project and you know
[3076.06 --> 3081.32]  think like boy people are gonna love this and then i post it to reddit and then it just gets eviscerated
[3081.32 --> 3086.90]  yeah oops yeah and it's basically kind of like that whole uh i feel like some some of the some of the
[3086.90 --> 3090.98]  criticism is valid but i think a lot of people um like they kind of use that as a way to like
[3090.98 --> 3097.56]  pump themselves up of like kind of criticizing other projects that initial criticism can actually
[3097.56 --> 3102.94]  hinder the project and hold you back and so i literally just did word of mouth marketing kind
[3102.94 --> 3107.92]  of i just recommended it like hey here's this thing check it out you know you you make your up make your
[3107.92 --> 3114.08]  own uh decision on it so uh users have actually wrote up a lot of different blog posts about uh their
[3114.08 --> 3120.38]  experiences um so literally you could just google for like chruby and you'll find a dozen or so blog
[3120.38 --> 3125.74]  blog posts and a couple actually in japanese and spanish which is kind of cool um so we're
[3125.74 --> 3131.70]  crossing that language barrier and yeah it's kind of give the basic rundown of like here's how i set
[3131.70 --> 3136.08]  it up here's you know here's how you switch rubies here's how you install them and here's kind of caveats
[3136.08 --> 3143.96]  and like yeah because i know one thing that i've always gotten held up on was always having coming
[3143.96 --> 3151.98]  from you know rvm to chruby i you know kind of depended on gem sets and i've um i've you know
[3151.98 --> 3156.50]  with bundler and the way it handles things i've kind of gotten rid of gem sets i don't use it anymore
[3156.50 --> 3163.58]  obviously i don't use ch gems yet and i haven't really had a need for it but i i find myself um only
[3163.58 --> 3172.28]  here and there having conflicts um and is that in maybe maybe i don't do enough with ruby to
[3172.28 --> 3178.16]  understand why someone would want to obviously isolate their their gem into a their gem you know
[3178.16 --> 3185.06]  gems for a project into a gem set but most often the reason you know clearly is for you know just
[3185.06 --> 3190.08]  the fact that you don't have any any bumps there's clear isolation from other projects
[3190.08 --> 3197.04]  yeah and also you're using environment variables to achieve this and so you don't have a lot of the
[3197.04 --> 3204.00]  magic quote-unquote that uh bundler does to ensure that it isolates all the dependencies right and but
[3204.00 --> 3208.88]  i mean there you shouldn't you should be able to like get away with just uh migrating gem set projects
[3208.88 --> 3216.36]  to using uh bundler and uh kind of like sharing gems that way uh of course you can also just directly
[3216.36 --> 3223.06]  edit the path and gem home and gem path environment variables and set your gem set that that way and
[3223.06 --> 3229.10]  you just have to then ensure that every time that uh project is ran it's ran in a shell that loads up
[3229.10 --> 3236.92]  the configuration and um yeah so yeah actually i've been thinking about like uh there's this tool that
[3236.92 --> 3243.26]  someone wrote uh called rev which allows you to kind of like add you know set and uh reset gem sets
[3243.26 --> 3248.10]  and i thought it'd be kind of interesting if someone actually wrote a tool that basically just
[3248.10 --> 3254.28]  pushed and popped uh directories on the gem path and then uh set gem home accordingly and that would
[3254.28 --> 3261.02]  allow you to actually like more fine-grained control of the gem gem directory kind of like search uh
[3261.02 --> 3266.22]  search variable the order in which it you know checks all the directories for the for all your gems
[3266.22 --> 3271.78]  and so i kind of felt like you know that'd be kind of interesting uh way to do it but really i mean
[3271.78 --> 3279.26]  it seems like there's a lot of confusion about how gem sets work ideally and a lot of people are trying
[3279.26 --> 3283.90]  to kind of like reinvent them and explore different areas and so it's not kind of really a solved problem
[3283.90 --> 3289.80]  yet yeah mind does that answer it yeah i mean it's i mean like you said it's a tough problem to solve
[3289.80 --> 3295.66]  anyways and i don't think there's really a one way to do it but i you know i now don't even depend at all
[3295.66 --> 3300.52]  on obviously gem sets but i kind of miss them because i have had some conflicts then i end up
[3300.52 --> 3304.76]  doing something that andrew kind of mentioned earlier which is like obliterate all my gems which
[3304.76 --> 3312.96]  i have just uh um i am happy to be a zsh user so i just type uh fo and up a couple times and i find
[3312.96 --> 3318.16]  the most recent for loop that i've written you know that basically obliterates all my you know all my
[3318.16 --> 3322.74]  gems installed and i just because they're so easy to install and it probably even upticks the numbers
[3322.74 --> 3329.02]  of installs anyways i just obliterate all my gems and just you know bundle install and i'm good to go
[3329.02 --> 3333.14]  in happy world but you know so that's okay with me but it still feels a little dirty you know it feels
[3333.14 --> 3338.74]  dirty to not have that segregation yeah yeah and plus you know the fact that the default behavior of
[3338.74 --> 3343.70]  bundlers to install into the gem directory as opposed to like installing always into a vendor directory
[3343.70 --> 3349.04]  and kind of like you get that trade-off where it's like well i can clutter up my gem directory or you
[3349.04 --> 3353.46]  know i can blow it up the vendor directory so this might elongate the conversation a tiny bit further
[3353.46 --> 3360.96]  but you know it's it's it's uh impossible to kind of um miss the millions of dollars recently that npm
[3360.96 --> 3366.94]  has gotten to become npm inc and you've got other package managers they come up to play like what is
[3366.94 --> 3373.52]  is ruby playing catch up is there something new out there that's being done by npm and bauer and other
[3373.52 --> 3379.02]  package managers that simplify the way they're distributing and versioning for individual projects
[3379.02 --> 3386.62]  well um actually i haven't looked at npm yet i actually should do that but uh one of the
[3386.62 --> 3393.60]  things that is really interesting to me is haskell's package manager uh cabal and it apparently has its
[3393.60 --> 3399.32]  own concept of sandboxes and so and also what i really like about cabal is the fact that the
[3399.32 --> 3408.42]  specification for your project is literally um key value colon separated plain text and so we don't
[3408.42 --> 3414.92]  have this like crazy uh uh you know pure ruby gem spec which is really kind of like gem spec was
[3414.92 --> 3420.66]  originally kind of designed for internal usage of you know describing the gem and we turned it into
[3420.66 --> 3427.04]  this thing where we could actually uh because ruby gems uh it's faster for it to load actual ruby code
[3427.04 --> 3433.56]  as opposed to deserializing it so when you actually install a gem it uh unpacks the actual gem spec back
[3433.56 --> 3440.12]  into pure ruby and i guess this kind of gave people the idea of like well let's just put this gem spec in
[3440.12 --> 3445.48]  into the actual git repository for projects and we'll have it list you know you use git ls files
[3445.48 --> 3451.56]  but i kind of feel that like violates dry uh that we have this like random bit of code that we constantly
[3451.56 --> 3457.74]  regenerates and it has this like you know git commands embedded into it i kind of like the fact that
[3457.74 --> 3463.88]  like cabal uh hides a lot of that from you and what i actually do for a lot of my projects is i put all
[3463.88 --> 3469.44]  the metadata into a gem spec yaml file and then my gem spec is basically just boilerplate code that loads
[3469.44 --> 3477.80]  that file and sets all the fields um and also like cabal i mean cabal and haskell's ghc compiler uh
[3477.80 --> 3482.44]  has a really really kind of like advanced dependency tracking system where it can actually recompile code
[3482.44 --> 3487.52]  that you know if it detects some change somewhere so really interesting yeah i mean
[3487.52 --> 3494.38]  you mentioned you haven't looked into mpm much but one of the ways it does um package installation is
[3494.38 --> 3501.36]  you can pass it a fly to say um you know save to local basically so it's dash dash save or you can
[3501.36 --> 3509.72]  add a dash dash save dash dev onto it and it and it actually uh will either go global if you don't do
[3509.72 --> 3515.86]  dash save i think you might have to pass the flag dash g to it uh possibly so let me correct me if i'm
[3515.86 --> 3522.82]  wrong but but then it also just drops into your project um most often hidden if you're hiding it
[3522.82 --> 3527.62]  with your editor you know with your id or just sublime text whatever you use but then it drops it
[3527.62 --> 3532.56]  on to no modules and from there you have them locally with your project and that way you kind
[3532.56 --> 3538.48]  of don't have this gem set need you almost just have your project and you either save locally or you
[3538.48 --> 3543.66]  don't you just either install globally or install locally and it just pulls the version that way
[3543.66 --> 3549.38]  it's a i mean so far i've you know kind of been dabbling in some javascript development and it's been
[3549.38 --> 3554.10]  coming from the ruby world into that world i've saw kind of both sides of the fence and it's
[3554.10 --> 3560.86]  it's neat the way they handle it and no conflicts yet so it's yeah i don't quite have the job you do of
[3560.86 --> 3564.80]  maintaining this project and the and the dependencies it has against it but
[3564.80 --> 3570.46]  that kind of neat the way they do it oh yeah totally um yeah i definitely feel like kind of the
[3570.46 --> 3577.40]  uh challenges uh that ruby switchers have to deal with is kind of uh dealing with the environment
[3577.40 --> 3583.78]  variables that you use to then manipulate um how ruby gems operates and sometimes it would kind of be
[3583.78 --> 3589.48]  nice if if it did automatically detect uh gem direct dot gem directories and that's just how it
[3589.48 --> 3595.12]  works but of course there's like security issues with you know running into malicious gem gem
[3595.12 --> 3601.78]  directories and yeah you've got a security background so you're you're thinking not only how do you use
[3601.78 --> 3607.50]  it as a developer but how do you securely use it as a developer right right you know because you know
[3607.50 --> 3613.32]  we pull down tons of code every day off of trusted you know right yes quote unquote trusted and like
[3613.32 --> 3618.78]  it'd be very trivial for someone to have like um like for a lot of those tools that automatically load
[3618.78 --> 3623.82]  environment variables uh when you cd into the directory and you could totally convince someone
[3623.82 --> 3630.10]  to do that and like you would have some sort of a way to you know uh manipulate the path where you
[3630.10 --> 3635.54]  can actually redirect to it and like you know so instead of typing ls and using system ls it all of a
[3635.54 --> 3641.68]  sudden you know using their weird backdoored ls or alias version yeah right so that's kind of yeah
[3641.68 --> 3648.16]  so not to uh hijack the conversation too much but we are kind of running up against our our time limit
[3648.16 --> 3653.78]  here so i want to uh go ahead and ask our our standard set of questions for your postmodern if
[3653.78 --> 3658.66]  if you're okay with that um the the first one is for a call to arms or a call to action for
[3658.66 --> 3664.48]  uh the open source community on any any of the projects that we've talked about okay so um i
[3664.48 --> 3668.68]  actually been thinking about writing a blog post about this but it's probably better just to put it
[3668.68 --> 3675.80]  into words here uh so this is like super super radical thing to say but you do not need a ruby
[3675.80 --> 3682.56]  manager or switcher in production if you only have one ruby and this is just something that people
[3682.56 --> 3687.78]  i don't not necessarily the word cargo cults i think applies but we just have gotten used to doing it
[3687.78 --> 3693.70]  and then that's just how we do it and it's baked into all these configuration management tools like
[3693.70 --> 3701.04]  chef and puppets and you just don't first of all the package managers ruby is usually roughly up to
[3701.04 --> 3706.80]  dates um the latest version of ubuntu available on amazon uh it's it's recently up to i think it's
[3706.80 --> 3712.82]  193 still but they're they're going to bump that to 20 and of course there's like still gc issues with
[3712.82 --> 3719.70]  mri 2.1 and even if your system and the benefit of using the package manager is you can enable
[3719.70 --> 3724.94]  things like unattended upgrades where the package manager will automatically imply security updates
[3724.94 --> 3729.98]  and just have to restart your processes and that's really nice uh as opposed to actually then
[3729.98 --> 3735.66]  freaking out at you know 3 a.m in the morning and you know do like doing rvm get ahead and installing
[3735.66 --> 3742.70]  the latest version to deal with some sort of critical uh security vulnerability and also even if the package
[3742.70 --> 3748.38]  manager doesn't offer the most up-to-date package you can roll your own packages with fpm you can also
[3748.38 --> 3754.40]  install the ruby into usr local and that's the purpose of usr local and the whole unix file system
[3754.40 --> 3761.18]  hierarchy is that it's for all the software that you install that's not installed by the system
[3761.18 --> 3767.92]  so like usr is controlled by the package manager the administrator controls usr and on most systems
[3767.92 --> 3775.26]  usr local bin always comes before usr bin in the path and so any software install there overrides
[3775.26 --> 3782.02]  the system software and like i feel that a lot of people kind of like miss this and i feel like
[3782.02 --> 3787.68]  setting up a you know production environment shouldn't be that difficult and you just really
[3787.68 --> 3792.80]  need to like install a package or extract a tar of a pre-compiled ruby and like this is not that
[3792.80 --> 3799.04]  difficult so yeah i don't know so just just to clarify i believe this is the first time that the
[3799.04 --> 3805.26]  call to arms from our guests has been to not use their project in production yeah you don't it's it's
[3805.26 --> 3811.02]  just it adds so much more complexity of making sure it works with all these system components and
[3811.02 --> 3816.74]  it's really more the ruby switcher is more optimized for developments and you know testing
[3816.74 --> 3823.84]  things because like seriously it it it just makes it so much easier awesome so the second question if
[3823.84 --> 3830.52]  you weren't doing what you're doing now what would you be doing oh man um so you mean like open
[3830.52 --> 3836.44]  source or work wise or well anything surfing or work wise or what what would you do with your free
[3836.44 --> 3846.34]  time yeah yeah oh man probably uh probably uh probably writing uh like uh various security
[3846.34 --> 3852.94]  exploitation tools that's uh it's kind of on my list of things to do so which technically i do so i do for
[3852.94 --> 3859.66]  work but yeah there's a there's a back end to that that uh question too which is like maybe uh
[3859.66 --> 3863.82]  an open source project out there that you've wanted to hack on but you know you've got
[3863.82 --> 3868.08]  obviously a list of things you're doing but you haven't had a chance to hack on it what's
[3868.08 --> 3873.06]  you know what's uh what's something you've seen out there that you wish you had time to hack on that
[3873.06 --> 3878.20]  you would you don't and you would love to if you had a weekend oh man okay so there's actually a
[3878.20 --> 3883.50]  couple of projects that i feel that really could use some like extra help and simplifying things
[3883.50 --> 3888.48]  and kind of like exercising out the really bad ugly code that's kind of built up the technical debt
[3888.48 --> 3894.02]  and one of the projects i've really loved in recently is padrino um i feel it's a really nice
[3894.02 --> 3898.54]  layer on top and they they've been doing more than just building on top of sinatra they have their
[3898.54 --> 3904.64]  own custom router and it feels very structured has that nice really rails to structure feel but without
[3904.64 --> 3910.26]  all the complexity that now comes with you know default rails and but the law of the code in
[3910.26 --> 3914.86]  there is kind of messy and i feel like it would kind of benefit from more people kind of looking at it
[3914.86 --> 3919.58]  and figuring out maybe better ways of handling things because it's a lot of their features are
[3919.58 --> 3926.68]  built on top of um kind of like sinatra before filters uh conditions sinatra conditions and rack
[3926.68 --> 3932.20]  middleware and so kind of that there's there's some weird issues for instance when you want to like
[3932.20 --> 3939.80]  disable csrf protection on like certain routes only so yeah um really awesome project the other one
[3939.80 --> 3945.90]  also is the rom project ruby object mapper where is that that i've like been waiting for that forever
[3945.90 --> 3950.82]  i know same here um and basically i've been like always talking with the developers and i'm usually
[3950.82 --> 3956.84]  very skeptical because uh they kind of tend to take principles to the extreme and this kind of results
[3956.84 --> 3964.46]  in a lot of kind of like excess code that is more kind of writing the code to uh comply with the
[3964.46 --> 3971.40]  style checker or the co-complexity scanner or um you know something like that or so i've been going i've
[3971.40 --> 3976.16]  been slowly going through that project and just sort of like making small pull requests but i kind of
[3976.16 --> 3980.76]  you know i'm just one person trying to undo complexity and that's usually hard once it's like
[3980.76 --> 3988.32]  built uh you know yeah rom rom would definitely be on my list of of projects to help with i i i am like
[3988.32 --> 3994.04]  you i would imagine i like i love using sinatra and data mapper in the past and so like i've been
[3994.04 --> 4000.22]  waiting for rom for quite a while now oh yeah oh yeah because data mapper one definitely has its warrants
[4000.22 --> 4005.56]  yep um yeah uh definitely check it out and try to contribute uh they're actually pretty close they
[4005.56 --> 4013.08]  have read supports but they're they still need to uh get uh write supports uh okay so the i guess the
[4013.08 --> 4019.08]  last project i'd have to say uh worth checking out is mruby and ruby is really well designed i would
[4019.08 --> 4025.20]  have to say of kind of embeddable languages i've been i was looking at those a couple years ago and it
[4025.20 --> 4029.34]  seems like every kind of language that claims to be embeddable is basically more designed to be
[4029.34 --> 4035.22]  installed onto a system and then loads its additional modules via extra shared libraries
[4035.22 --> 4041.50]  and mruby is really interesting it has its own little build system that compiles all it's split
[4041.50 --> 4047.02]  into all of its features are split into what are called mrb gems and then those are all compiled down
[4047.02 --> 4053.50]  into one single static linked library that you can then embed into other programs and so man it's
[4053.50 --> 4058.96]  really nice and it's actually pretty decent documentation around it uh but like there's not a lot of
[4058.96 --> 4063.68]  projects around it so you do have to do kind of your research and tinker around with the code
[4063.68 --> 4070.12]  but uh it's really well put together and i think it has huge potential and just uh anywhere you could
[4070.12 --> 4076.16]  put lua uh the embeddable language lua you could probably put mruby and do a lot more because you
[4076.16 --> 4084.84]  know lua misses it lacks certain things basic things like bitwise operators yeah cool so the last question
[4084.84 --> 4089.84]  is uh for a programmer hero or just somebody that's been really influential in your life to this point
[4089.84 --> 4097.78]  oh man um so i try to be really anti-hero because anti-hero worship i feel like it really holds people
[4097.78 --> 4102.72]  back uh when they're always kind of looking up to someone and instead of some inspiring to you know
[4102.72 --> 4108.46]  improve themselves and challenge themselves but i definitely have to say like uh as as far as like
[4108.46 --> 4114.06]  programmer wisdom goes i feel like uh dan cubb who worked on the data mapper project uh
[4114.06 --> 4124.68]  uh uh piat solnick and then also uh marcus i'm gonna mispronounce his name marcus shriept mbj uh he he
[4124.68 --> 4131.08]  wrote mutants yeah and uh those people are kind of like the most interesting discussions about like
[4131.08 --> 4137.24]  design and you know when when principles are taken too far uh when they're not applied like pretty much
[4137.24 --> 4142.82]  anything solnick writes is like i pretty much agree with it so those are kind of like they're
[4142.82 --> 4150.10]  they're they're hip cats they know what's up yeah for sure awesome well i wanted to say thanks a lot
[4150.10 --> 4156.72]  for coming on this show i think that this is a uh i don't know you kind of get the sense with with
[4156.72 --> 4162.80]  ruby switchers and just with the this world that um we've we've almost gotten as simple as we can get
[4162.80 --> 4168.10]  but at the same time it feels like we've got a far a long way to go right i mean your call to arms kind
[4168.10 --> 4175.06]  of sums it up right and that like the goal would ultimately be to not really need these things and
[4175.06 --> 4180.48]  uh so you know i think that we've got a long way to go here but but i like the uh the simplicity that
[4180.48 --> 4184.74]  you're aiming for so once again i just want to say thanks a bunch for joining us today it was post
[4184.74 --> 4191.98]  modern um his uh real name has been redacted and uh no just kidding um but yeah no for sure we will uh
[4191.98 --> 4197.42]  we'll uh be back next week um so make sure you listen we are going to start doing this weekly
[4197.42 --> 4203.68]  again um now that everything has started to settle down so back to live too i think we're gonna be uh
[4203.68 --> 4209.16]  if you're listening to this obviously you are because you're hearing me say this but uh our uh our new date
[4209.16 --> 4216.80]  is friday live at 10 a.m central standard time um if for some reason we don't have a guest we're just
[4216.80 --> 4221.54]  gonna get on there anyways and just talk about awesome open source so we're we're aiming for weekly
[4221.54 --> 4228.58]  live um should be a fun time and a postmodern we've we've uh been playing some email tag for a bit
[4228.58 --> 4233.56]  too trying to get you on the show and just echo andrew's thoughts too just static static to have you
[4233.56 --> 4238.46]  on the show uh love the work you're doing in open source and just want to do as much as we can to
[4238.46 --> 4243.66]  encourage you to keep doing the awesome work that you're doing thanks man it was a fun time being
[4243.66 --> 4247.70]  on the show and hope to hear more awesome episodes of you guys absolutely go ahead andrew
[4247.70 --> 4254.04]  uh yeah that's it so until next time we'll just say goodbye bye-bye adios
[4254.04 --> 4256.70]  you
[4256.70 --> 4258.70]  you
[4258.70 --> 4272.70]  you
[4272.70 --> 4283.70]  you
[4283.70 --> 4285.70]  you
[4285.70 --> 4287.70]  you
