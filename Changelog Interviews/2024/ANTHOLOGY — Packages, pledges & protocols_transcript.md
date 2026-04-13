[0.00 --> 13.08]  okay friends this is the changelog and we're going back to the hallway track at all things open 2024
[13.08 --> 20.02]  in raleigh north carolina this episode features carl george principal software engineer at red hat
[20.02 --> 26.30]  for discussion on the state of open source enterprise linux and rel better known as red
[26.30 --> 34.58]  enterprise linux we talked to max howe creator of homebrew and the t protocol at t.xyz which offers
[34.58 --> 40.84]  rewards and recognition to open source maintainers and last we talked to chad whitaker head of open
[40.84 --> 46.90]  source at century about the launch of open source pledge and their plans to help businesses and
[46.90 --> 53.50]  orgs do the right thing and support open source a massive thank you to our friends at fly.io
[53.50 --> 61.42]  that is the home of changelog.com to pull your app in five minutes at fly.io okay let's do this
[61.90 --> 74.30]  what's up friends i'm here with dave rosenthal cto of century so dave when i look at century i see you
[74.30 --> 80.30]  driving towards full application health air monitoring where things began session replay being
[80.30 --> 86.14]  able to replay a view of the interface a user had going on when they experienced an issue with full
[86.14 --> 92.40]  tracing full data the advancements you're making with tracing and profiling chrome monitoring co-coverage
[92.40 --> 99.44]  user feedback and just tons of integrations give me a glimpse into the inevitable future what are you
[99.44 --> 104.84]  driving towards yeah one of the things that we're seeing is that in the past people had separate
[104.84 --> 110.68]  systems where they had like logs on servers written files they were maybe sending some metrics to datadog
[110.68 --> 115.18]  or something like that or some other system they were monitoring for errors with some product maybe
[115.18 --> 120.98]  it was century but more and more what we see is people want all of these sources of telemetry logically
[120.98 --> 127.72]  tied together somehow and that's really what we're pursuing at century now we have this concept of a trace id
[127.72 --> 133.88]  which is kind of a key that ties together all of the pieces of data that are associated with user action
[133.88 --> 139.86]  so if user loads a web page we want to tie together all the server requests that happened any errors that
[139.86 --> 145.86]  happened any metrics that were collected and what that allows on the back end you don't just have to
[145.86 --> 150.50]  look at like three different graphs and sort of line them up in time and you know try to draw your own
[150.50 --> 155.80]  conclusions you can actually like analyze and slice and dice the data and say hey what did this metric
[155.80 --> 159.86]  look like for people with this operating system versus this metric looked like for people with this
[159.86 --> 166.94]  operating system and actually get into those details so this kind of idea of tying all of the telemetry data
[166.94 --> 174.40]  together using this concept of a trace id or basically some key i think is uh is a big win for developers trying
[174.40 --> 180.64]  to diagnose and debug real world systems and something that is uh we're kind of charge the path for that for
[180.64 --> 186.02]  everybody okay let's see you get there let's see you get there tomorrow yeah perfectly how will systems be
[186.02 --> 191.84]  different how will teams be different as a result yeah i mean i i guess again i just keep saying and
[191.84 --> 196.52]  maybe but i think it kind of goes back to this debuggability experience when you are digging into an
[196.52 --> 202.08]  issue you know having a sort of a richer data model that's you know your logs are structured they're sort
[202.08 --> 206.94]  of this hierarchical structure with spans and not only is it just the spans that are structured they're tied
[206.94 --> 211.48]  to errors they're tied to other things so when you have the data model that's kind of interconnected
[211.48 --> 218.94]  it opens up all different kinds of analysis that were just kind of either very manual before kind of
[218.94 --> 223.94]  guessing that maybe this log was you know happened at the same time as this other thing or we're just
[223.94 --> 228.58]  impossible we get excited not only about the new kinds of issues that we can detect with that
[228.58 --> 233.04]  interconnected data model but also just for every issue that we do detect how easy it is to get to
[233.04 --> 238.42]  the bottom of it i love it okay so they mean it when they say code breaks fix it faster with century
[238.42 --> 244.62]  more than 100 000 growing teams use century to find problems fast and you can too learn more at
[244.62 --> 254.86]  century.io that's s-e-n-t-r-y dot i-o and use our code changelog get 100 off the team plan
[254.86 --> 260.78]  that's almost four months free for you to try out century once again century.io
[260.78 --> 289.94]  all right hard question first carl you ready for this recording
[290.78 --> 298.94]  should i introduce myself no carl george good jerry you got one teed up i was just trying to get
[298.94 --> 303.84]  his name on the record here just in case he says something that we need to be like he might run away
[303.84 --> 308.94]  my name's benny vasquez there's actually get a little closer to the mic and give me a sound check
[308.94 --> 315.00]  sound check one two i like barbecue how about that tacos are good too i love eating do you make
[315.00 --> 320.04]  your own barbecue oh yeah do you i mean i'm a good amateur i'm not professional level you're a
[320.04 --> 324.28]  backyard barbecue guy what's your backyard barbecue tell me about your tools your tooling your cooking
[324.28 --> 328.76]  methods so my smoker that i have uh my my father-in-law gave it to me before he passed away
[328.76 --> 333.78]  he had uh it was in his backyard for a while and i was picking up my kiddos from uh staying at grandma
[333.78 --> 339.00]  and grandpa's house one weekend and my mother-in-law mentions oh i told i told catherine my wife she's like
[339.00 --> 343.44]  i told catherine that uh you could have that smoker and i'm like what she never told me that and my
[343.44 --> 347.30]  wife denies it to this day she's like she never told me that she's making that up i was over there
[347.30 --> 351.16]  in like 12 hours i had like four full grown men over there lifting this smoker in the back of my
[351.16 --> 357.30]  truck like yes i will take a free smoker how many gallons uh i don't know it's not it's not huge um
[357.30 --> 362.98]  well four guys to carry it yeah i mean it was like 18 gauge steel thick steel yeah it was very thick
[362.98 --> 366.94]  and heavy i got one of their cousins made it for him for an anniversary present i think that's
[366.94 --> 371.92]  very old but very good smoker gotta love a good smoker hand-me-down you know really i mean better
[371.92 --> 375.16]  than paying you know it's already seasoned yeah better than paying a grand or two for a brand new
[375.16 --> 379.58]  one right absolutely that's where i'm at i'm like i don't have a hand-me-down so i'm like my only
[379.58 --> 388.04]  option is to either build one myself which i will probably not do or spend money on a mill scale or
[388.04 --> 393.60]  something else could you build it yourself you know how to weld i have friends okay yeah i could i can
[393.60 --> 398.76]  get it done if i wanted to but it's heavy you know you gotta bother your friends it almost probably
[398.76 --> 402.36]  you want to build it on site so you don't have to move it i don't have the expertise i thought it's
[402.36 --> 407.98]  like i want to like leverage aaron franklin's right expertise or mill skills expertise like why do i
[407.98 --> 414.82]  got to become a yeah a barbecue manufacturer expert just to become a backyard amateur yeah i don't have
[414.82 --> 418.72]  any other tricks in that other than like you want to use a good smoker volume matters like you said i
[418.72 --> 422.24]  don't know how many gallons this one is but i noticed that where like you have like a backyard
[422.24 --> 426.48]  smoker compared to what you get at the restaurants the real professional stuff you have a tall stack
[426.48 --> 431.16]  they've got like you know like 10 000 gallon or thousand gallon propane tanks that have been
[431.16 --> 435.30]  converted into smokers and i think i think the volume makes a huge difference on that on how
[435.30 --> 439.88]  how much you can control the temperature variation it's huge yeah there's a lot of
[439.88 --> 446.62]  ongoing barbecue science yeah it's endless in texas the smaller it is the harder it is like i have
[446.62 --> 450.34]  trouble sometimes keeping the temperature even because it's not a huge smoker it's a decent size but yeah
[450.34 --> 454.30]  yeah that's how i think the big that's the the real secret from the big professional
[454.30 --> 458.70]  joints is they can they can afford the massive smokers doing you know 20 briskets at a time
[458.70 --> 464.92]  and that volume helps them keep the temperature so consistent like one maybe two you know yeah i mean
[464.92 --> 470.48]  brisket alone is expensive so i'm gonna afford one you don't want to mess it up yeah i mean wings
[470.48 --> 476.34]  stuff like that but i could talk about barbecue all day same but that's not why we're here let's talk
[476.34 --> 484.76]  about the confusion i suppose around red hat enterprise linux the history of centos to some
[484.76 --> 492.74]  degree and really the state of open source enterprise linux sure what could you share you've shared we've
[492.74 --> 500.82]  had conversations none of them so far recorded and here we are good so help me demystify for those
[500.82 --> 506.44]  listeners out there you work at red hat to be clear you are a principal software engineer and you
[506.44 --> 512.52]  work on what was it the the extras extra packages for enterprise linux it's a it's an add-on repo uh
[512.52 --> 516.62]  the closest analogy for like people that are i like to compare it to ubuntu's universe the main
[516.62 --> 520.40]  difference is ubuntu they enable their universe their community packages out of the box like you
[520.40 --> 524.56]  just have it they're available but they're not uh for a long i think they've changed it a little bit
[524.56 --> 528.78]  with the new ubuntu pro stuff but for the longest time ubuntu's universe repo was these are the
[528.78 --> 533.00]  community things canonical doesn't handle these and that's basically what apple is for rel it's just
[533.00 --> 536.62]  we don't have it enabled out of the box we make it an opt-in thing you have to go out of your way
[536.62 --> 540.94]  add the apple repository and then install the community maintain packages you want and a good
[540.94 --> 545.24]  thing to note is apple is it's not its own project it's part of the fedora project and the way that
[545.24 --> 550.56]  the whole thing fits together it's much easier visually with the diagram so i'm trying to think how i
[550.56 --> 555.22]  can just show you the pic describe the picture in my head yeah but there's like this this line going
[555.22 --> 559.34]  across that's fedora rawhide that's our rolling release and that's where all the newest stuff goes
[559.34 --> 563.90]  right away uh kind of like debian sid but after this point the debian analogies fall apart it doesn't
[563.90 --> 568.86]  work we do our fedora releases every six months fedora 41 i think just got released today those
[568.86 --> 573.82]  branch off of fedora rawhide but then that's like something like i think the last time i looked it was
[573.82 --> 578.80]  something like 60 000 packages that are in fedora red hat doesn't want to support all of those in in
[578.80 --> 584.08]  the product eventually where it gets into into rel red hat enterprise linux so it's only a subset i think
[584.08 --> 590.56]  roughly around 10 of the fedora packages like 6 000 or so actually make it into rel and that happens
[590.56 --> 595.62]  through going by going through centos uh or centos stream rather there's a whole bunch of confusion
[595.62 --> 601.22]  around the name the name change we did um it's still the centos project centos is not dead uh it's
[601.22 --> 606.12]  just a little bit available right yep for those who think it's not there yeah it is there there's been
[606.12 --> 611.18]  a lot of misleading messaging around centos is dead or you have to replace centos no here there's
[611.18 --> 614.06]  differences you should understand them but i think there are a lot of positive changes
[614.06 --> 617.48]  that people are missing out on it because they're not just buying you know buying the marketing line
[617.48 --> 622.22]  of somebody that says i want to be the new centos well that's kind of flawed why don't you just be
[622.22 --> 626.46]  a distro on your own make your own reputation and then see what centos is doing if it works for you
[626.46 --> 630.62]  then keep using it i think it would work for a lot of people there are some people that uh i think
[630.62 --> 635.18]  there's one guy i know that at work that says that um if you have a rel size hole we want to sell
[635.18 --> 642.04]  you rel like that's and you know 10 year life cycle vendor escalation assurances yeah assurances the
[642.04 --> 647.08]  partner ecosystem before we started recording i was telling adam that one of the big value
[647.08 --> 651.56]  propositions that i know red hat talks about a lot but i think a lot of people miss out on whether
[651.56 --> 656.80]  it's just phrasing or that doesn't convey well is that red hat has spent literal decades and
[656.80 --> 661.66]  countless amounts of money building a partner ecosystem with hardware vendors software vendors
[661.66 --> 666.62]  and upstream communities right and the big value premise you're paying for when you buy
[666.62 --> 669.86]  by rel and i'm not a rel salesman this is going to sound very sales pitchy but you're an engineer
[669.86 --> 674.54]  yeah i'm very low in the weeds we purposely wanted to have you on here we could have had others talk
[674.54 --> 678.46]  and it's not we don't want to talk to them it's that we want to hear from an engineer that doesn't
[678.46 --> 682.18]  have a dog in the fight insofar as you're trying to sell something or market right we want to hear
[682.18 --> 687.14]  from an engineer who cares about sure and has been at red hat since 2019 is that right 19. so you've been
[687.14 --> 691.02]  there for a while i think a good bit of nuance to that is that yeah i've only been there since 2019
[691.02 --> 695.96]  relatively short i've been in the cento s and fedora and apple communities before that i got hired out of
[695.96 --> 700.56]  those communities to do it full time at red hat which is another huge value that they do is
[700.56 --> 705.04]  employing people in open source projects to keep making open source which we have there's a whole
[705.04 --> 709.74]  track yesterday here at the conference about open source sustainability and sustainability versus
[709.74 --> 714.76]  freedom and choice and open source purists and things like that and yeah a lot of people they the
[714.76 --> 720.00]  dream is to get paid to work in open source i've i feel great i've achieved that dream like other
[720.00 --> 723.90]  people aren't as lucky or they get it like i know my last employer had a thing where it's like well you can
[723.90 --> 727.72]  do open source part-time and then this much time you have to do these things inside the company
[727.72 --> 731.94]  you have a lot of that and i know a lot of companies their ospo offices open source programs
[731.94 --> 737.54]  office or equivalent name they struggle around how do we get our engineers to be better open source
[737.54 --> 742.04]  citizens they're using consuming all this open source how do we turn them in from just consumers
[742.04 --> 747.38]  into making sure the things we depend on continue to exist long term which is a theme that i'd like to
[747.38 --> 751.30]  segue off of in the cento s yeah let's go back to that yeah we've set the premise that you're
[751.30 --> 757.62]  a credible person to talk to you're not selling it you're not selling anything yeah you're not
[757.62 --> 760.90]  marketing not that they're bad people but we're not we don't want to be marketed to we want to hear
[760.90 --> 769.38]  the from an engineer from the inside so right layout centos it's not dead it's still there
[769.38 --> 776.26]  how that relates to rel how that relates to fedora and the whole life cycle of how you get to these
[776.26 --> 782.02]  packages that people can rebuild off of and this sort of conundrum of the open source enterprise
[782.02 --> 787.66]  linux we live in so big question right i started going on a little bit started talking about how
[787.66 --> 792.38]  i wish i had a diagram of like fedora branching it from rawhide into its releases every three years or
[792.38 --> 798.04]  so we'll take one of those fedora releases and we'll start we'll branch it again and start building
[798.04 --> 803.20]  the next major version of rel that starts as cento s stream but before we've like announced it it's
[803.20 --> 806.84]  still very early we're still forming like you know pre-alpha days we're building all putting all this
[806.84 --> 810.90]  stuff together and then at a certain point they have enough of the changes that they want to go
[810.90 --> 815.22]  into the next major version of rel like we want this version of apache this version of open ssl
[815.22 --> 819.44]  maybe it's the same ones at the exact time they branched maybe they go one forward one back
[819.44 --> 824.38]  maybe they add a few other features build a few things differently but they that that is the process
[824.38 --> 830.26]  of turning the fedora fast-moving innovative project into the enterprise product and that happens
[830.26 --> 835.56]  through centos there's a lot of chat about how they talk about rel compatible and like the
[835.56 --> 840.44]  enterprise linux standard uh other other other people with other projects there isn't really a
[840.44 --> 845.62]  standard there's red hat making a product and to whatever extent there is a standard of enterprise
[845.62 --> 851.78]  linux centos defines that that is where it happens and so because it's happening there you can
[851.78 --> 856.74]  influence it you can actually contribute to it i know you have a big developer audience and the
[856.74 --> 861.18]  analogy i used earlier was that you know if you've got a choice between two libraries one that is like
[861.18 --> 866.26]  active development have you know getting features you can contribute to it whether or not you you have
[866.26 --> 871.74]  the ability to or or the intent to the fact that you can contribute to a vibrant project that's growing
[871.74 --> 877.52]  and active would you rather use that or something else that says yeah we're going to be exactly the
[877.52 --> 881.32]  same as the other thing and if you send us a bug report if it's in the other thing we're just going
[881.32 --> 886.14]  to close it and you can't contribute here we are bug for bug compatible there's this whole myth mythos
[886.14 --> 891.00]  about uh bug for bug compatible and really what that trans when someone says i want bug for bug
[891.00 --> 894.76]  compatible with rel what they mean is i want rel without paying for it that's really what it boils
[894.76 --> 900.00]  down to it's a pretty blunt statement but it's true and what's different from the past when centos
[900.00 --> 906.10]  originally started was that you can get just rel for free there's a lot of free programs there's the
[906.10 --> 908.88]  and this is going to sound sales pitch again but i'm telling you how to get free stuff
[908.88 --> 914.56]  there's the red hat developer for subscription for individuals anyone can sign up and get 16 free
[914.56 --> 918.84]  rel instances to do whatever they want to with no limits you can even use it in a business it's just
[918.84 --> 923.28]  a little fuzzy because it is individual right you can't agree to the terms on behalf of an org so
[923.28 --> 928.22]  for most businesses the more than one person it's not really going to work yeah there is also another
[928.22 --> 932.58]  program developer subscription for teams that'll give you i don't remember the exact number it's high
[932.58 --> 936.92]  it's in the thousands of free rel instances in your non-production environments if you're paying for
[936.92 --> 941.72]  rel in production and then there's also programs for giving open source projects free rel there's
[941.72 --> 946.52]  programs for giving educational institutions free or heavily discounted rel there's a tons of way
[946.52 --> 951.54]  to get rel without paying for it but there are definitely scenarios where red hat once thinks that
[951.54 --> 956.30]  yes this person should pay for rel and a lot of those people are the ones that they use centos
[956.30 --> 961.26]  rather than just i want an operating system they wanted just to get rel without paying for it or get
[961.26 --> 966.02]  a discount on their rel they'd use you know 10 of their fleet on rel and then the rest on centos to
[966.02 --> 971.08]  cut cost that was never a good fit for it because of small subtle differences in the engineering and
[971.08 --> 976.20]  how it's built one of those is that red hat enterprise linux actually has overlapping minor versions
[976.20 --> 983.98]  you can stay on say 9.0 after 9.1 and 9.2 come out still get security updates and some third parties
[983.98 --> 988.50]  only certify on specific minor versions so if you've got you know third party vendor software that
[988.50 --> 994.20]  require hard requires 9.2 using anything that's on you know like one of the one of the other rebuilds
[994.20 --> 999.62]  that's on 9.4 on centos stream that basically has 9.6 content right now it's a little bit ahead on minor
[999.62 --> 1006.30]  versions then you know if a vendor requires 9.0 strictly then it might not work but red hat will sell
[1006.30 --> 1011.84]  you 9.0 still with security updates it might be 9.2 might be a better example because it doesn't last
[1011.84 --> 1015.84]  forever you can't stay there forever it's just an extension but those overlapping things are things
[1015.84 --> 1021.02]  that community projects have never had centos never had them and the new new rail rebuilds that
[1021.02 --> 1025.32]  are trying to trying to claim that they're the new centos they don't have them either they also have
[1025.32 --> 1029.34]  corporate sponsors that sell those extensions they're trying to make their buck too which is
[1029.34 --> 1034.98]  understandable we're all trying to make money in open source but the the big value prop that i talked
[1034.98 --> 1039.52]  about with red hat with the ecosystem stuff is that not that you'll just go use this and it's a cheaper
[1039.52 --> 1044.16]  price than rail it's that you can go to the people creating this software a lot of times they're
[1044.16 --> 1048.72]  they're maintaining it in rail they're maintaining it in centos and oftentimes they're maintaining in
[1048.72 --> 1053.16]  fedora too not always but there's a huge huge participation from red hat in fedora all the way
[1053.16 --> 1058.30]  it is separate from red hat but we're very involved at every step of the process so if you can you can
[1058.30 --> 1063.48]  make a feature request and say i wish you know this software did this thing red hat can say all right
[1063.48 --> 1067.42]  that's a good idea here's how we'd go about it first we're going to put it in the upstream project
[1067.42 --> 1072.82]  where we're also participating then we'll build it in fedora and then it'll go into either the next minor
[1072.82 --> 1076.18]  version of rel or the next major version of rel depending on how disruptive the change is
[1076.18 --> 1083.24]  and then they put it in centos stream next and then it goes into rel after that so having people
[1083.24 --> 1088.18]  that are holistic across the entire pipeline that's the expertise thing that from the engineering angle
[1088.18 --> 1093.30]  like that's the real value i see looking at it with a set of engineering eyes any thoughts jared
[1093.30 --> 1098.42]  where you at with this i guess i'm just still confused not because you're not doing a good job
[1098.42 --> 1103.06]  sure because it's a lot of information it's a lot of information it seems like you need a diagram
[1103.06 --> 1109.74]  perhaps yes because i'm i'm jumping kind of from noun to noun i can put a diagram in your show notes
[1109.74 --> 1113.72]  yeah that would that would probably be helpful the uh you mentioned about how the how it works
[1113.72 --> 1117.98]  differently now i want to go into that a little more if i can so what do you mean by that centos and
[1117.98 --> 1121.66]  working differently right okay working differently than what differently prior to acquisition the
[1121.66 --> 1126.06]  acquisition the ibm acquisition stuff is kind of tangential right no no i mean the acquisition of
[1126.06 --> 1131.38]  centos open oh yeah yeah so to centos so i can go through that control right so centos started
[1131.38 --> 1137.96]  outside of red hat and then uh i think it started around 2004 about 10 years later the project was
[1137.96 --> 1142.16]  kind of kind of on the ropes maintainers were burned out they were had day jobs no one was getting paid
[1142.16 --> 1149.06]  to work on it and uh what red hat saw was that um it's kind of weird it's a bit of incompetence thing
[1149.06 --> 1154.62]  we had internal inside red hat development teams using centos to build with because we couldn't get out of
[1154.62 --> 1159.66]  our own way and give our own teams free rail it's super messy and it's gotten better since then but
[1159.66 --> 1164.56]  at the time that was kind of the state of things so red hat was that's pretty funny yeah uh maybe i
[1164.56 --> 1167.38]  should talk about that but i think it's hilarious it's too late nobody's told me i'm just kidding
[1167.38 --> 1172.36]  nobody's told me i can't say that uh but that kind of drove it they basically red hat was like we want
[1172.36 --> 1177.52]  this this project to keep existing and so we're gonna you know they made job offers to all of the
[1177.52 --> 1182.36]  developers most of them took it a few of them turned it down and then um they basically came into
[1182.36 --> 1186.12]  red hat partially they were still kind of kept off to the side they're like well you're still kind of
[1186.12 --> 1191.30]  duplicating this product but we want you to keep going and and uh exist and so they kind of sat in
[1191.30 --> 1194.70]  that limbo for a while where they weren't growing they weren't getting uh they weren't getting people
[1194.70 --> 1198.78]  resources but they had the resources they need like to focus their full time on it get a paycheck
[1198.78 --> 1203.98]  and keep the project going uh that was a little bit of infusion but we still had this problem around
[1203.98 --> 1208.82]  this whole bug for bug thing and also being a duplicate of the product there would never be a
[1208.82 --> 1212.86]  business incentive to have to put the same engineering resources into your product and
[1212.86 --> 1216.64]  this project that is trying to match it as close as possible that would never make sense no business
[1216.64 --> 1221.10]  person would agree to that but because of all the nuance around how things it was being used as a
[1221.10 --> 1225.72]  development platform but we also saw the pain points of it being a development platform that lagged
[1225.72 --> 1231.46]  behind the thing it was trying to match right centos would typically lag about a month behind on the
[1231.46 --> 1237.20]  minor versions like rel 7.6 would come out and then centos 7.6 would be it'd be 7.5 for a while
[1237.20 --> 1242.02]  they'd finish the rebuild and publish it and about a month later you'd get it so those those rebuild
[1242.02 --> 1246.44]  gaps were real painful for the developers trying to use it as a platform to build on because at that
[1246.44 --> 1253.52]  time centos was behind rel and the transition that a lot of people got upset about was they were using
[1253.52 --> 1260.70]  centos as this open source rel-like operating system in production which was the bigger backlash
[1260.70 --> 1268.42]  and then red hats move was to push centos in front of rel let it be centos stream that push wasn't
[1268.42 --> 1272.48]  about that reaction that reaction came later but yeah i get you it's kind of like it's kind of like
[1272.48 --> 1277.60]  if you're painting this visual centos used to be behind rel yeah where rel is in front of it and then
[1277.60 --> 1282.80]  it became centos stream which was in front of rel the innovation was happening in fedora landing in
[1282.80 --> 1287.12]  centos stream and then ultimately rel as a product that's where we're at now it was just a really messy
[1287.12 --> 1291.30]  transition part of that was that's a compression of a lot of time yeah definitely i'm not trying to
[1291.30 --> 1295.38]  like not go into the details we don't have a lot of time that was that was the dream originally of
[1295.38 --> 1300.62]  it right we had uh we had centos lagging behind rel it was painful for you know it needed to exist
[1300.62 --> 1305.78]  but we had you know developers frustrated that okay well i'm making this change but then it changed in
[1305.78 --> 1309.40]  the next minor version and i didn't find out about it till a month later so they wanted to get ahead
[1309.40 --> 1314.64]  of those things and um they basically wanted rel a little bit earlier than it was you know then they
[1314.64 --> 1319.70]  were getting rel like things in centos uh in what i call classic or legacy centos the official
[1319.70 --> 1323.66]  distro name is centos linux what i think should have had the way it should have gone down was we
[1323.66 --> 1328.76]  just did a clean break at a new major version and said for example centos 9 is here early and it's
[1328.76 --> 1332.50]  different now but because of some compressed timelines and people were excited to get it out
[1332.50 --> 1337.42]  there we ended up doing two variants in version 8 we had the classic variant which was a rebuild
[1337.42 --> 1342.08]  following rel centos linux 8 and then we had to make a new name to distinguish the variant which
[1342.08 --> 1347.24]  became centos streaming it's still the same basic operating system just released on a different
[1347.24 --> 1352.56]  cadence and i can say that because at the time that was my my full-time job i'm working on apple now but
[1352.56 --> 1356.88]  that was what i got hired by red hat to work on right i was doing those builds it was still
[1356.88 --> 1362.72]  and i mentioned uh earlier that the rail maintainers are taking over control and doing all that work in
[1362.72 --> 1368.18]  centos now the early transition wasn't that way the small group of people uh like three or four of us
[1368.18 --> 1373.46]  that were building classic centos started having to do two rebuilds the rebuild of centos linux following
[1373.46 --> 1378.88]  rel and then the rebuild of centos stream that was ahead of rel and it was really messy for a while
[1378.88 --> 1383.22]  until we could get it actually properly onboarded in version 9 we started we ended up putting it on
[1383.22 --> 1388.18]  git lab and so all the rail maintainers would build do their packages there create them and do all their
[1388.18 --> 1392.62]  development and then there wouldn't be a rebuild process they would just build it and it would become
[1392.62 --> 1398.26]  centos stream but in the early days we'd have builds and uh they were all rebuilds we'd tag them
[1398.26 --> 1401.80]  at different times and basically just release them at different times and some of them would be
[1401.80 --> 1406.40]  classic centos linux and some of them be centos stream 8 but it was all from the same build system
[1406.40 --> 1410.54]  all from the same people all from the centos project so that's one of the things that irkspan people
[1410.54 --> 1416.74]  say this this isn't the same centos i'm like no but yes it is like it's the same people it's the
[1416.74 --> 1422.26]  same project centos isn't dead it's technically centos is the project centos linux and centos stream
[1422.26 --> 1427.08]  were the distributions but thankfully we don't have that double double thing anymore we onboarded
[1427.08 --> 1431.48]  all the rail people and it's just centos stream and i think my personal opinion is that we should
[1431.48 --> 1435.50]  one day just drop the stream and just say yeah this is just centos most people just call it centos
[1435.50 --> 1440.12]  and let's avoid the confusion we should have never had the overlap it should have just been a clean
[1440.12 --> 1444.22]  break at a new major version and leave all the old major versions on the old model that's not the
[1444.22 --> 1448.34]  way the transition happened clean breaks are good poorly executed transition in my opinion some of it
[1448.34 --> 1452.24]  predated me some of it i was front row and center but and doing what i could yes
[1452.24 --> 1459.04]  where are the open source lines drawn across these distributions like fedora centos stream and then
[1459.04 --> 1463.80]  so it's all it's all open source so and everything in fedora is just out there in the open built in
[1463.80 --> 1467.72]  the open there's nothing private everything in centos stream is the same way it's built in the public
[1467.72 --> 1473.42]  it's all public and you can contribute to it rel the contribution path into rel is through centos
[1473.42 --> 1479.28]  because functionally the way it works is it's the major version of rel you've got like centos stream 9 now
[1479.28 --> 1485.54]  is where all the rel 9 development happens and then periodically they branch that into 9.4 9.5 9.6
[1485.54 --> 1490.88]  so you can't actually contribute directly into a rel minor version because those are built inside red hat
[1490.88 --> 1496.12]  but then the major version you can get it on there so from the developer angle like you can do pull
[1496.12 --> 1501.66]  requests to master but you can't do pull requests to the 9.4 branch okay some sometimes the rel maintainers
[1501.66 --> 1506.12]  will say yeah we also have customer pressure to get it in these older minor versions and then they can do
[1506.12 --> 1511.38]  that part internally but then the after effects is it's still all open source it's still all published
[1511.38 --> 1516.24]  all compliance with all the licenses rel once you have rel you have access to the source for every
[1516.24 --> 1522.44]  package even even the ones with licenses that don't require it like mit or bsd license so it's fully
[1522.44 --> 1531.26]  open source top to bottom so it sounds like we're in this rebuilder world where you have the rockies and
[1531.26 --> 1537.52]  the almas and the many others i don't fully understand it it seems like from an outside
[1537.52 --> 1544.20]  point of view or from a purview sort of point of view that it is more about trying to get what is
[1544.20 --> 1550.52]  literally the rel product which is a product and you can say it's open source and you can get access
[1550.52 --> 1558.42]  to packages and rpms etc i tried last night with your help to find a way to download today in a
[1558.42 --> 1564.20]  moment rel you said it's open source i have to sign up for an account with right hat i have to go
[1564.20 --> 1568.96]  through hoops essentially to get it and it may be literally open source but it's very challenging to
[1568.96 --> 1575.22]  play with what is the rel product and what i mean by product it is open source derived as a trademark
[1575.22 --> 1581.66]  product given to customers who pay for it with a license more so for for support and assurances
[1581.66 --> 1587.92]  and security totally cool right i'll push back on you a little bit okay uh you tried real quick on
[1587.92 --> 1592.32]  your phone while we were drinking at the bar that's i wasn't drinking you were drinking i wasn't drinking
[1592.32 --> 1597.24]  i was i was drinking water ah so well very quick attempt on your phone it's not the same as like
[1597.24 --> 1600.16]  sitting down like yeah let me create this account like i won't create accounts on my phone i'm gonna sit
[1600.16 --> 1604.04]  wait till i get on my laptop again right but it is okay let me push back there's a little bit of a
[1604.04 --> 1608.54]  barrier yes you let me push back to that if i want to go play with the product called ubuntu
[1608.54 --> 1618.54]  what's the latest version 2404 yes i can go and tap a download 2410 now 2410 well lts lts right sure
[1618.54 --> 1624.84]  yeah i can no account required yeah no account required so there's no hoops to get to that product
[1624.84 --> 1631.64]  but there is hoops to the rail product yeah so that's my point it's challenging give you a throwback
[1631.64 --> 1636.30]  20 or older episodes when you interviewed uh adam jacob sure fantastic interview and he brings up
[1636.30 --> 1641.10]  the point of like you make a product and you sell it you don't give it away for free i agree
[1641.10 --> 1646.34]  ubuntu's model is that they are giving their product away for free which there are pros and cons to that
[1646.34 --> 1649.70]  and i'm not gonna i don't want to criticize another company's business model you know i wish
[1649.70 --> 1654.56]  them all luck i've got friends that work in ubuntu and work for canonical or x canonical but the
[1654.56 --> 1658.56]  you know it gets back to that problem you can have all of the market share you want by giving away
[1658.56 --> 1663.52]  your product for free and it's hugely successful and popular but then i know that my canonical
[1663.52 --> 1668.26]  friends have told me before that uh canonical ubuntu's biggest challenger was always free ubuntu
[1668.26 --> 1673.20]  like everyone that's getting it for free because they can and convert the conversion rate of people
[1673.20 --> 1678.32]  that are like should be paying for it to help sustain the engineering of that product is a vanishingly
[1678.32 --> 1683.08]  small number and it's extremely hard sell to say here's why you should pay us when you can just get
[1683.08 --> 1687.18]  it get the product for free right so reddit tries to take a different stance yeah i'm talking about
[1687.18 --> 1692.02]  access not sure selling a product in this case well the access is the same thing right because
[1692.02 --> 1696.76]  access is part of that subscription part i'm not trying to say what i'm trying to say is the angst
[1696.76 --> 1703.66]  the angst is there was centos prior to red hat's acquisition of the open source project and a lot
[1703.66 --> 1708.20]  of that is confusion right people looked at it as this is the free access right this is the rel
[1708.20 --> 1714.82]  yeah alternative to rel that's open source that i can use in production it is blessed for production
[1714.82 --> 1719.14]  what would i what would i tell you if uh what would you say if i told you that one it was never
[1719.14 --> 1724.96]  blessed for production and two that there's even a website marketed as that no it definitely wasn't
[1724.96 --> 1729.22]  show me show me a page that says it was blessed for production but anyways that's a tangent wasn't
[1729.22 --> 1732.68]  that the case though i mean didn't every i mean that's the that's the major issues that people are
[1732.68 --> 1737.06]  using in production that's what people said there was no blessing right but that's a minor point
[1737.06 --> 1742.30]  yeah there's some nuance to it there is nuance there um that's not the point what would you say if i could
[1742.30 --> 1745.96]  if i told you that i can show you a page right now on the red hat website that says rel is not
[1745.96 --> 1751.02]  intended for production we had this conversation last night i'm down for it yeah it's because on
[1751.02 --> 1755.88]  the page i'm talking about it's the in the product store where they say it's a self-support rel where
[1755.88 --> 1760.56]  you can buy just access to rel and can't file support cases and it says this is not intended for
[1760.56 --> 1767.52]  production because red hat one thinks that you should have production on or support for your
[1767.52 --> 1772.04]  production instances it's that simple so when they say that you know there's also a block
[1772.04 --> 1775.68]  post that says centoist stream is not designed for a production or intended for production
[1775.68 --> 1780.06]  because it doesn't have support it's around that part but it's been misinterpreted to say
[1780.06 --> 1784.14]  even red hat says this isn't good enough for production right and there's other interviews
[1784.14 --> 1789.38]  with other red hatters like uh from the fedora flock conference brian exelbeard uh he said that you
[1789.38 --> 1793.50]  know just because we don't say you should use it for production or we don't intend it for production
[1793.50 --> 1797.84]  doesn't mean you can't and there's lots of companies that do i've got some friends over at meta
[1797.84 --> 1802.32]  facebook their fleet is this one of the it's probably the largest fleet of servers in the
[1802.32 --> 1808.40]  world i think the last you know pr approved term they got to use was millions plural of instances and
[1808.40 --> 1812.48]  they're running centoist stream everywhere um and they get on the new versions as soon as they can
[1812.48 --> 1816.84]  they're they're active contributors and they're deploying this stuff regularly they use it at
[1816.84 --> 1821.52]  massive scale in production so it certainly can be it's still real life and it can be used
[1821.52 --> 1827.22]  your models may vary right your risk factor is is your risk factor what i'm trying to get to is not
[1827.22 --> 1833.22]  to say you are wrong or right meaning the proverbial you is in terms of red hat sure it's this angst
[1833.22 --> 1843.16]  that allows or creates the need for the rebuilds yeah alma rocky and the angst there is they want
[1843.16 --> 1849.34]  rel for free yep basically right and there's even more detail to that we talked about that partner
[1849.34 --> 1854.76]  ecosystem stuff the whole idea of being rel compatible is because they want access to that
[1854.76 --> 1858.34]  the real brand name ecosystem even the brand name yeah a little bit of that there's some of the
[1858.34 --> 1862.66]  confusion and you know they're that's going on now with the whole automatic and wp engine stuff around
[1862.66 --> 1866.80]  brand name and how you identify that but the bigger thing is you know they're like oh i don't care
[1866.80 --> 1871.02]  about having real i care about that this app i can install and it works on this hardware that whole
[1871.02 --> 1876.16]  ecosystem that is what they're buying into and that is what red hat sells and as a product yeah
[1876.16 --> 1881.18]  which i'm cool with the whole idea of being like exactly rel compatible is the idea of getting into
[1881.18 --> 1885.70]  that you know getting a foot into that ecosystem and taking advantage of that ecosystem from people
[1885.70 --> 1890.66]  that did not spend decades building it and countless dollars building it right and it's just weird that
[1890.66 --> 1895.62]  there's this angst out there because they essentially want if there were other people here could argue
[1895.62 --> 1902.20]  against it they would probably argue against it but my opinion my my uh summarization of what i
[1902.20 --> 1909.68]  understand about it is they essentially want what rel gives as a product for free as in freedom of
[1909.68 --> 1914.56]  open source and free as in cost yeah and that conflation is a sticking point for a lot of people
[1914.56 --> 1921.62]  and centos centos used to give it i'm quoting used to give it prior to being acquired by red hat
[1921.62 --> 1928.14]  now it's upstream from rel in terms of a visual diagram yeah it was acquired by as an open
[1928.14 --> 1934.06]  acquired by now it is where the active development happens which ultimately lands in rel the product
[1934.06 --> 1943.16]  and so the angst there is they the folks want what is enterprise grade linux rel you're considered
[1943.16 --> 1948.56]  the standard the gold standard of enterprise grade linux they want it for free that's the angst what i
[1948.56 --> 1953.96]  realized around that angst is that uh we made all those changes and some of it predates me some of
[1953.96 --> 1957.48]  it was right around when i was getting hired but what i learned about the centos community was
[1957.48 --> 1961.66]  they're basically two different personas there and it kind of splits evenly in the life cycle
[1961.66 --> 1966.16]  there were the people using centos in the first five years of the life cycle new version would come
[1966.16 --> 1970.80]  out they would say yes i want these new features i want these new capabilities and i'm also frustrated
[1970.80 --> 1974.28]  those were happen to be the same people that were frustrated that they couldn't contribute to it and
[1974.28 --> 1979.32]  make changes to it then there are people kind of using it in the last five years as instead of just
[1979.32 --> 1984.18]  instead of using rel for them it was just the free unbranded rel they were never going to contribute
[1984.18 --> 1988.56]  they don't care about being able being able to contribute they just want to get the product for
[1988.56 --> 1994.06]  free and they want it to let be you know be maintained for as long as possible so those two personas were
[1994.06 --> 1999.72]  kind of where we unintentionally divided the community people that liked what we were doing with centos
[1999.72 --> 2004.24]  stream being able to contribute and it still has a five and a half year life cycle which i mean that's
[2004.24 --> 2008.86]  the same thing ubuntu lts gives you without the pro subscription five years so it's still a pretty long
[2008.86 --> 2013.44]  time it's still an lts those people they're like yeah i like these changes this makes a lot of sense
[2013.44 --> 2018.06]  to me and the people that do not care about contributing do not care about getting their
[2018.06 --> 2021.68]  bugs answered they just want to get the product for free they're like oh no i'm going to go to these
[2021.68 --> 2026.58]  other guys that give me the give me the same thing the big big change is that because it got actually
[2026.58 --> 2031.74]  harder on centos and red hat once the aqua hire thing happened and they were paying the centos
[2031.74 --> 2037.00]  maintainers because customers would come in and say well you use your you know you're you're making both of
[2037.00 --> 2041.74]  these things so why should i pay you for one and not the other or why should i pay you for the one
[2041.74 --> 2046.64]  when this other one's free and that conflation of having uh having red hat sponsorship it helped the
[2046.64 --> 2052.10]  project not fail and collapse but it also made it harder to have those conversations to draw that line
[2052.10 --> 2058.54]  between the product and the project um and so now the new rebuilds like i heard uh one guy inside red
[2058.54 --> 2063.38]  hat described it as these changes are red hat getting out of the rebuild business like we decided that's
[2063.38 --> 2067.50]  not where we want to spend our time here's the way that building an operating system works in our
[2067.50 --> 2072.32]  pipeline holistically to make a better product and it's still really close to rail and you can still
[2072.32 --> 2076.54]  use it for whatever you want to but it's not going to be trying to match rail identically anymore it's
[2076.54 --> 2082.46]  getting you know six months ahead of rail on features and fixes um but like you said a lot of those people
[2082.46 --> 2086.78]  that are going to different different alternatives now they're in that latter group the five you know five
[2086.78 --> 2091.68]  plus year usage where they just want the same thing they don't want anything to change ever
[2091.68 --> 2095.46]  and they don't want to think about like being able to contribute being a benefit
[2095.46 --> 2101.68]  it's mostly what i wanted to cover i know we can probably go deeper wherever you want and i got
[2101.68 --> 2104.66]  more i can say but i don't know how much more we want to go how much we want to spend on this jared
[2104.66 --> 2111.40]  five minutes i want to hear about the future man yeah juicy juicy future stuff well real quick before
[2111.40 --> 2117.40]  that how does meta get their support when their senta stream doesn't do what he needs to do like what
[2117.40 --> 2120.84]  do they do they're self-supporting they they're active in the projects they're contributing
[2120.84 --> 2126.06]  they identify a feature that they want or something that's broken that they want to fix a bug and
[2126.06 --> 2130.86]  they're contributing that into cento stream they're active contributors contributors there they're
[2130.86 --> 2135.46]  contributing to upstream projects i know they're heavily involved in system d uh they they participate
[2135.46 --> 2139.00]  there a lot of times you'll find talks from them at conferences like scale where they're talking
[2139.00 --> 2143.58]  about the internals of system d because they employ a lot of system d developers uh they have kernel
[2143.58 --> 2148.14]  developers butterfs developers all kinds of stuff so they have a lot of that expertise in-house
[2148.14 --> 2152.76]  gotcha so they're not really what they don't really need to leverage that support any more
[2152.76 --> 2157.94]  than just interacting with those communities already all right so the future stuff juicy future juicy
[2157.94 --> 2162.90]  so the major version right now of rel is nine everyone knows that same for all these you know
[2162.90 --> 2167.92]  rel likes and sento stream which is still rel like it's all major version nine everyone can count and
[2167.92 --> 2173.72]  knows that the next number after that is 10 is it 10 yes was it eight nine so there's a i mean i'm
[2173.72 --> 2179.04]  making this joke and it's lost because there was actually a time before i got hired where uh there's
[2179.04 --> 2182.64]  some weird marketing thing around it where they were telling engineers that they couldn't say that
[2182.64 --> 2187.14]  the next version was eight and i don't know what where it originated or why oh wow but then like
[2187.14 --> 2191.94]  some real marketing folks showed up at the um i think it was the fedora flock conference with uh
[2191.94 --> 2196.24]  stickers with the rocket ship and the number eight on it and after you know all the messaging to the
[2196.24 --> 2199.78]  engineers was like don't say the number eight just say oh whatever you know whatever the next version
[2199.78 --> 2203.38]  is and so the engineers were all mad they're like oh these guys showed up with the number eight on a
[2203.38 --> 2207.40]  sticker and they told us we can't say it that's so stupid like why do we even have this problem okay
[2207.40 --> 2212.20]  i missed that joke big company inner things whatever yes the next version is 10 juicy stuff go
[2212.20 --> 2217.94]  uh so we're on a rel's on a three-year major version cycle now six month minor version cycle
[2217.94 --> 2222.22]  be a little more reliable it used to be kind of hit or miss and one of the feedback we got from
[2222.22 --> 2226.32]  customers was uh you know bringing it back to ubuntu they have their schedule where they're like yeah
[2226.32 --> 2230.58]  we're publishing this month you can count on it and a lot of people a lot of customers really value that so
[2230.58 --> 2236.24]  eventually in version eight was when they adopted that in 2019 uh so three year three year cycles you
[2236.24 --> 2243.38]  can see that rel 9 came out in 2021 uh sorry 2022 so 2025 is when rel 10 is going to come out like
[2243.38 --> 2249.18]  and it's going to be there's all we don't we can't officially say dates but there's an event in uh in
[2249.18 --> 2255.08]  2025 in the spring uh that red hat puts on that might make sense for there to be product announcements
[2255.08 --> 2258.82]  that you know anyone can figure that out just by looking at public websites it's not that hard
[2258.82 --> 2263.54]  um not that that would be the exact day but probably pretty close is a good time frame to
[2263.54 --> 2268.48]  expect it cinto a stream 10 has already branched off from fedora it's getting that initial productization
[2268.48 --> 2275.54]  uh to become to stabilization to become rel eventually uh it's in a state now you can get it install it
[2275.54 --> 2281.42]  today but we haven't announced it as you know ready is a weird word we i think we usually use
[2281.42 --> 2285.86]  launched or released but there's going to be a launch announcement or release announcement for
[2285.86 --> 2291.36]  cinto a stream 10 pretty soon because it's getting to the point now it's not that high pace of you
[2291.36 --> 2296.46]  know stabilization it is okay well everything it's we basically have all the features we want we might
[2296.46 --> 2301.74]  make a few more changes before it gets released as rel 10 but it's basically stabilized and this is
[2301.74 --> 2307.96]  what you can expect rel 10.0 to be and you know whenever it comes out next year so we're gonna have
[2307.96 --> 2312.54]  that announcement pretty soon probably next month or the month after where we announce cinto a stream 10
[2312.54 --> 2317.62]  is here you can use it now it's pretty good we like it also apple 10 the thing that i work on
[2317.62 --> 2322.30]  directly um we're gonna announce that about the same time usually when we when we've announced
[2322.30 --> 2326.70]  them separately we usually have the feedback that well why would you announce you know if we announce
[2326.70 --> 2330.30]  one immediately the question is well i want the other one to use them together i want those extra
[2330.30 --> 2333.86]  packages and i want the base operating system they're useless without each other and a lot of
[2333.86 --> 2338.14]  people's opinions so we're gonna do kind of a joint announcement uh probably the same day or the
[2338.14 --> 2342.48]  same week where we say yep apple 10 is here we've got all these package extra things you can add the
[2342.48 --> 2346.18]  community's been building building them for the last few months and we've had the infrastructure
[2346.18 --> 2351.56]  online but we're doing a like a flag day like here it is it's it's as ready as it will be but you know
[2351.56 --> 2356.34]  it's it's the thing like do we say it's ready at 2 000 packages do we say it's ready at 3 000 like
[2356.34 --> 2360.12]  we're going to keep adding stuff and even after we announce it it doesn't stop growing
[2360.12 --> 2366.70]  all right so we've got those things coming up uh and timeline timeline wise you can look at it as
[2366.70 --> 2372.58]  that's about six months before the rel 10 launch yeah so spring of 2025 is when rel 10 is going to
[2372.58 --> 2377.12]  be coming out and then we're about a little bit more than six months before that right now we're
[2377.12 --> 2381.74]  getting all this stuff buttoned up to say yeah cinto a stream 10 is here you can use it it's a
[2381.74 --> 2386.68]  major version stable operating system it doesn't have minor versions but it's going to be maintained for
[2386.68 --> 2391.08]  five and a half years it's very rel like you can add all these apple packages we've been working on
[2391.08 --> 2397.50]  and use it right now and it'll be good to go i love it that's the good stuff coming up what exactly
[2397.50 --> 2404.70]  is extra in the extra okay that is just the mentality of it of it's only packages that you
[2404.70 --> 2409.40]  can't get in the base operating system so i kind of mentioned that the there's like 60 something
[2409.40 --> 2414.04]  thousand packages in fedora and only about 10 of those go into centos and then eventually go into rel
[2414.04 --> 2421.16]  everything else in fedora that isn't that 10 is eligible to go into apple so like i can say i
[2421.16 --> 2425.78]  maintain uh like the caddy web server i maintain that package in fedora and i also maintain it in
[2425.78 --> 2430.88]  apple branches up to date there i haven't seen anyone say like we need to put caddy into rel we
[2430.88 --> 2436.38]  have customers asking for caddy maybe that changes in the future but for now i maintain it in fedora and
[2436.38 --> 2442.10]  i put it in the apple branches for each release apple 7 apple 8 apple 9 and apple 10 now put it in there
[2442.10 --> 2446.86]  so people can use it on that rel release or that centos release or any of the other rel like things
[2446.86 --> 2451.90]  that are out there they use it there but it's not a rel package it's not maintained by red hat you
[2451.90 --> 2455.38]  can't file a support case for it so that's the that's what the extra in the name is for it's only
[2455.38 --> 2461.94]  additional things if for example caddy if red hat decided to add that into rel and into the product
[2461.94 --> 2466.00]  it would then become ineligible for apple and we'd retire from there and you'd get it instead of
[2466.00 --> 2469.96]  getting it from the community repo you'd get it from the main repos gotcha
[2469.96 --> 2474.40]  that'll clear that up that was a good summary i think i think it that's what i wanted to cover
[2474.40 --> 2480.20]  for a while i think it's been challenging to from the outside as a non red hat enterprise linux user
[2480.20 --> 2484.96]  i'm not i'm not that person yeah uh but i care about enterprise linux because i have friends who
[2484.96 --> 2490.56]  care about enterprise linux using it at work or at home all over the place you know friends at facebook
[2490.56 --> 2496.94]  even that rely upon centos of course and it's just kind of crazy that how the world is fractured
[2496.94 --> 2503.34]  yeah and then the parts we can't that i won't really go into but like that other side on the
[2503.34 --> 2511.00]  rebuild side is also offering support and financial financially backed services so why not just buy
[2511.00 --> 2516.08]  red hat enterprise linux in the first place it's like we've talked about that in the inside
[2516.08 --> 2520.86]  conversations jared i know you won't but like what do you think about that jared like we've talked about
[2520.86 --> 2528.78]  that like it seems strange to go through all this and have these rebuilds that is either bug for bug
[2528.78 --> 2536.20]  compatible or there's words that leverage the rail brand to be rail like that says it's free and open
[2536.20 --> 2542.86]  source they're trading on the rail brand but then they're but then they're offering support or other
[2542.86 --> 2549.38]  financially backed services that's basically what red has doing to rail in the first place the rabbit
[2549.38 --> 2555.20]  hole goes deep it is carl thank you for sharing that uh that story yeah i'm always happy to talk
[2555.20 --> 2559.38]  about it going deep with us we appreciate it thanks carl appreciate it thanks thanks for having me on
[2559.38 --> 2585.14]  what's up friends i'm here in the breaks with kyle carberry co-founder and cto over at coder.com
[2585.14 --> 2591.12]  coder is an open source cloud development environment a cde you can host this in your
[2591.12 --> 2597.30]  cloud or on premise so cal walk me through the process a cde lets developers put their development
[2597.30 --> 2601.44]  environment in the cloud walk me through the process they get an invite from their platform
[2601.44 --> 2607.70]  team to join their coder instance they gotta sign in set up their keys set up their code editor
[2607.70 --> 2613.22]  how's it work step one for them we try to make it remarkably easy for the dev we never gate
[2613.22 --> 2618.48]  any features ever for the developer they'll click that link that their platform team sends out
[2618.48 --> 2624.24]  they'll sign in with oidc or google and they'll really just press one button to create a development
[2624.24 --> 2630.16]  environment now that might provision like a kubernetes pod or an aws vm you know we'll show the
[2630.16 --> 2633.94]  user what's provisioned but they don't really have to care from that point you'll see a couple
[2633.94 --> 2639.02]  buttons appear to open the editors that you're used to like vs code desktop or you know vs code
[2639.02 --> 2644.70]  through the web or you can install our cli through our cli you really just log into coder and we take
[2644.70 --> 2648.88]  care of everything for you when you ssh into a workspace you don't have to worry about keys it
[2648.88 --> 2653.00]  really just kind of like beautifully magically works in the background for you and connects you
[2653.00 --> 2657.58]  to your workspace we actually connect peer-to-peer as well you know if the coder server goes down for
[2657.58 --> 2660.94]  a second because of an upgrade you don't have to worry about disconnects and we always get you the
[2660.94 --> 2666.36]  lowest latency possible one of our core values is we'll never be slower than ssh period full stop and so
[2666.36 --> 2670.44]  we connect you peer-to-peer directly to the workspace so it feels just as native as it possibly could
[2670.44 --> 2676.06]  very cool thank you kyle well friends it might be time to consider a cloud development environment
[2676.06 --> 2683.14]  a cde and open source is awesome and coder is fully open source you can go to coder.com right now
[2683.14 --> 2690.84]  install coder open source start a premium trial or get a demo for me my first step i installed it on my
[2690.84 --> 2696.32]  proxbox box and play with it it was so cool i loved it again coder.com that's c-o-d-e
[2696.32 --> 2703.10]  r.com and also by our friends over at eight sleep check them out eight sleep.com i love my eight
[2703.10 --> 2709.90]  sleep i've never slept better and you know i love biohacking i love sleep science and this is all
[2709.90 --> 2717.30]  about sleep science mixed with ai to keep you at your best while you sleep this technology is pushing
[2717.30 --> 2721.74]  the boundaries of what's possible in our bedrooms let me tell you about eight sleep and their cutting
[2721.74 --> 2729.16]  edge pod for ultra so what exactly is the pod imagine a high-tech mattress cover that you can
[2729.16 --> 2737.38]  easily add to any bed but this isn't just any cover it's packed with sensors heating and cooling elements
[2737.38 --> 2743.72]  and it's all controlled by sophisticated ai algorithms it's like having a sleep lab a smart
[2743.72 --> 2750.28]  thermostat and a personal sleep coach all rolled into one single device and the pod uses a network of
[2750.28 --> 2756.74]  sensors to track a wide array of biometrics while you sleep it tracks sleep stages heart rate
[2756.74 --> 2763.16]  variability respiratory rate temperature and more and the really cool part is this it does all this
[2763.16 --> 2769.24]  without you having to wear any devices the accuracy of this thing rivals what you would get in a
[2769.24 --> 2774.62]  professional sleep lab now let me tell you about my personal favorite thing autopilot recap every day
[2774.62 --> 2779.82]  my eight sleep tells me what my autopilot did for me to help me sleep better at night here's what it
[2779.82 --> 2787.78]  said last night last night autopilot made adjustments to boost your REM sleep by 62 percent wow 62 percent that
[2787.78 --> 2796.30]  means that it updated and changed my temperature to cool to warm and helped me fine-tune exactly where i
[2796.30 --> 2802.58]  wanted to be with precision temperature control to get to that maximum REM sleep and sleep is the most
[2802.58 --> 2807.74]  important function we do every single day as you can probably tell i'm a massive fan of my eight
[2807.74 --> 2813.56]  sleep and i think you should get one so go to eightsleep.com slash changelog and use our code
[2813.56 --> 2821.34]  changelog and you'll get 350 off your very own pod for ultra you can try it free for 30 days but i am
[2821.34 --> 2826.38]  confident i sleep on this thing every night i'm confident you will not want to return it trust me
[2826.38 --> 2833.18]  once you experience this ai optimized sleep you'll wonder how you ever slept without it how do i know
[2833.18 --> 2838.84]  because that's exactly how i feel they're currently shipping to the u.s canada united kingdom europe and
[2838.84 --> 2847.12]  australia once again eightsleep.com slash changelog and use our code changelog and get 350 off your very
[2847.12 --> 2859.24]  own pod for ultra max howell creator of homebrew creator of tea protocol did i cover all the gamut
[2859.24 --> 2864.30]  or is there more oh there's more but those are the uh the things that people care about there you go
[2864.30 --> 2872.10]  i do like to hit on what people care about now i think the last time you and i crossed paths was
[2872.10 --> 2878.92]  some sort of announcement around tea i think and maybe that was txcl or something there's more to
[2878.92 --> 2883.38]  it i'm it's been a while but i remember you put something out i covered it on changelog news
[2883.38 --> 2887.66]  and i wrote something about it like i feel like they're trying to boil the ocean i don't know what
[2887.66 --> 2893.50]  i said oh yeah yeah and that affected your game plans by some way yeah yeah it was it was an important
[2893.50 --> 2899.14]  little pointer for me i appreciate that okay that's all i remember yeah i was trying to do too much
[2899.14 --> 2908.22]  that was uh what was tkly which we'd now call package x okay and uh well i was very much aware
[2908.22 --> 2915.06]  of the fact that homebrew is enormous and here i was trying to do like homebrew 2.0 right something
[2915.06 --> 2922.48]  i said i'd never do and you know i think uh ryan doll with dino is seeing the same kind of problems
[2922.48 --> 2927.84]  right like once you've had something that's a huge success how do you make something that is
[2927.84 --> 2935.20]  as big even as that like you've got this enormous momentum behind the previous thing so i was very
[2935.20 --> 2941.40]  much aware of that when i was building out tkly and so i put too much into it thinking well that's
[2941.40 --> 2946.62]  the only way i'm going to get people to like come on board with it right right and uh you point out
[2946.62 --> 2952.36]  quite sagely i think it made me realize that yeah it was doing too many things and that was just
[2952.36 --> 2959.82]  confusing so we whittled it down to just what it is now which is uh like an executor for packages so
[2959.82 --> 2964.62]  you don't think about installing them you just run them and uh that's enormously powerful actually
[2964.62 --> 2969.34]  i think over the next few years people are going to start seeing that okay because so good for
[2969.34 --> 2976.36]  scripting for example uh you can write a package x shebang in your script and then add all the
[2976.36 --> 2980.14]  packages you want and then you've got a portable script you can just pass around
[2980.14 --> 2984.56]  that you don't have to worry about if people have things installed or not it like opens up the
[2984.56 --> 2990.12]  entire open source ecosystem to it okay so i got a few things planned to use that but we realized along
[2990.12 --> 2995.80]  the way this is all part of t protocol right that um even though we thought initially we would be
[2995.80 --> 3003.98]  putting like functionality for the protocol into tkly actually no that doesn't make sense it's diffusing
[3003.98 --> 3009.94]  the messaging once again i think i was a little too influenced by our investors and that's why we went
[3009.94 --> 3015.44]  down that path but we course corrected so now we're completely focused on just the protocol which
[3015.44 --> 3022.46]  you know that was the original vision that i had to build something that could help uh people who
[3022.46 --> 3029.26]  create open source to actually you know uh get some of that value that they create back to themselves
[3029.26 --> 3035.24]  rather than just creating value for people who build on top of it right the people beneath the
[3035.24 --> 3040.16]  people beneath the people right like the dependency of the dependency and letting that value chain
[3040.16 --> 3044.42]  trickle down or trickle up whatever direction you're looking at it from so how does that work then
[3044.42 --> 3051.86]  yeah so we built it we've been running the test net since february and uh we got 1.7 million people
[3051.86 --> 3058.10]  who've signed up to to use this test net which uh pretty great numbers by any standards but especially
[3058.10 --> 3063.92]  in the web3 space like you don't get those that kind of users yeah i think it's a testament to like
[3063.92 --> 3069.82]  people understanding that what we're doing is important but also that we've cracked it that we
[3069.82 --> 3075.26]  understand how to take the value of open source and actually expose it so until now right we all
[3075.26 --> 3081.02]  understand the value of open source everyone builds everything on top of it yeah but uh very little of
[3081.02 --> 3087.20]  that value ends up going back to the people who maintain it like that's my story homebrew was a passion
[3087.20 --> 3094.30]  project that became my full-time job for free and uh you know i had to keep taking new jobs quitting
[3094.30 --> 3099.06]  them after i'd saved up some money working on it and um you know that's why i found the t protocol i was
[3099.06 --> 3105.06]  once again in that position wanting to work on open source full time so our system yeah it changes the
[3105.06 --> 3111.04]  economics of open source like that was one of my conclusions before founding t protocols that the
[3111.04 --> 3116.70]  system of economics that we use in this world uh it doesn't fit cleanly onto how open source works
[3116.70 --> 3122.26]  open source is really weird there's no real thing that's like it elsewhere in the world so it was
[3122.26 --> 3127.62]  necessary to build something new that used economics in a new fashion so what that's what we built we have
[3127.62 --> 3134.26]  a on-chain oracle called chai that computes the impact of all the open source projects all 10.5 million
[3134.26 --> 3140.84]  of them using package manager data and dependency data to calculate that the higher your impacts the
[3140.84 --> 3147.12]  higher your rewards every 24 hours we just give you free t token and then we have uh like with the
[3147.12 --> 3152.18]  1.7 million people who signed up only a third of them are developers two-thirds of them are people
[3152.18 --> 3157.86]  that maybe didn't even know about open source before once they heard the story of how everything
[3157.86 --> 3163.50]  they've used on the internet for the last 30 years is built on top of this open source they understood
[3163.50 --> 3169.24]  that there's a huge amount of untapped value there that they want to participate in so they're the input
[3169.24 --> 3175.52]  for the uh the monetary parts that allow the open source to be remunerated and uh i've had loads of
[3175.52 --> 3180.20]  tokenomics experts looking at it over the last three years you know you have to calculate the sell and
[3180.20 --> 3185.56]  the buy pressure correctly in order to make it so the token price stabilizes it something which then
[3185.56 --> 3191.84]  makes it so the open source maintainers can sell their token and use it to uh fund them fund the
[3191.84 --> 3198.28]  development right because if they received a bunch of token for their package getting popular and they
[3198.28 --> 3203.40]  went to go sell it and they were just dumping on the market and the demand wasn't there then the price
[3203.40 --> 3209.48]  would crash and you'd have your typical you know peaks and valleys of the crypto sphere so you're
[3209.48 --> 3215.68]  trying to like stabilize the coin basically or what's the tokenomics you're trying to stabilize the
[3215.68 --> 3220.36]  value of the of the token or yeah exactly it's very important that we do that otherwise it will be a
[3220.36 --> 3226.18]  project that just goes whoop and down as you were saying right and uh you know then it hasn't succeeded
[3226.18 --> 3231.66]  at all and uh you know that was a difficult problem to solve we have lots of mechanisms in there that will
[3231.66 --> 3237.74]  be there for the launch we're having to launch later this year or early next year gotcha so it's not live
[3237.74 --> 3244.98]  yet no but uh the testnet is so people can sign up uh we have 17 000 open source projects that have
[3244.98 --> 3252.42]  onboarded 2t protocol during the testnet so uh you know we've we've got good traction i'm hoping when
[3252.42 --> 3257.46]  mainnet goes live the proof will be in the pudding you know people will see that this is something that
[3257.46 --> 3264.06]  actually could fix these fundamental issues with how open source is funded and it's really a no-brainer
[3264.06 --> 3270.00]  if you're an open source project with any clout onboarding is free it's very low effort to do so
[3270.00 --> 3274.76]  too low effort as you probably saw some of the negative press we had over the last year or so
[3274.76 --> 3281.84]  yeah there's been some spammers spamming yeah we incentivize people to try and break t rank or chai
[3281.84 --> 3290.22]  and uh they found a way to do it by creating more than 200 000 packages on npm we're glad they found a
[3290.22 --> 3295.30]  way to break it because that meant we could fix it and that's what the testnet is for but yeah uh
[3295.30 --> 3300.48]  don't feel good about it but you know when you're building new things there's always unanticipated
[3300.48 --> 3305.36]  consequences to that a lot of people think i should have seen this coming i kind of agree with them
[3305.36 --> 3310.58]  i should have seen it coming but you know when you're building stuff you only have so much time
[3310.58 --> 3315.68]  yeah yeah i mean sometimes you're learning as you go i remember that happening i don't remember what
[3315.68 --> 3321.82]  my comment was at the time but once i saw it i was like yeah this seems like a natural progression
[3321.82 --> 3329.24]  so yeah you live and learn right live and learn and it was still early so that's good yeah and it
[3329.24 --> 3337.16]  won't happen again we've uh closed the gap cool what exactly is tea well the main purpose of tea at least
[3337.16 --> 3343.22]  you know what i wanted to accomplish when i came up with the idea was to use cryptocurrency to fix
[3343.22 --> 3348.62]  what we call the nebraska problem after that famous xkcd comic you know the power blocks
[3348.62 --> 3353.74]  representing all of open source as it gets stacked on top of each other and those little projects
[3353.74 --> 3359.70]  near the bottom that are you know fragile because the people who maintain them don't have the time or
[3359.70 --> 3365.86]  the incentive to do so and yet it's holding up so much critical infrastructure so yeah it's a
[3365.86 --> 3372.54]  cryptocurrency project that uses a unique tokenomics model in order to give open source developers
[3372.54 --> 3381.02]  token rewards on a 24-hour basis and you know a lot of the other pieces of it are designed to
[3381.02 --> 3386.72]  attract the interests of like typical crypto investors or just like normal developers who want to show
[3386.72 --> 3393.84]  real support for their open source projects a key differentiator between us and most ways of
[3393.84 --> 3399.90]  supporting open source is that there is no donations in our system you uh you can buy token and then
[3399.90 --> 3408.38]  stake it against projects so both you and the project is gaining from this there's no uh there's no gift
[3408.38 --> 3416.54]  this is it's more like an investment mm-hmm so what would so say there's a piece of software that's
[3416.54 --> 3428.70]  signed up for the t protocol and so i can use t to execute it right am i then required to also buy into the
[3428.70 --> 3434.06]  like to give back value or is it still i can just use that without doing it if i want to like it'll lock
[3434.06 --> 3441.10]  you in so uh nothing's different like going into it i knew that this wouldn't work if we changed
[3441.10 --> 3445.82]  anything about how open source already works right you know you can't charge for open source you can't
[3445.82 --> 3450.78]  make it so you have to you know buy token and stake it even if you you can get that token back before you
[3450.78 --> 3458.06]  can use things so uh it works based on calculating the impact of open source projects and then you
[3458.06 --> 3463.50]  are creating a yield on top of those projects that then goes to the project maintainers they then
[3463.50 --> 3469.66]  distribute the token however they see fit but yeah as a user nothing's different and as a maintainer
[3470.22 --> 3475.18]  nothing's different i didn't want to change the incentives in open source either it's still
[3475.18 --> 3480.86]  incentivized in exactly the same way it's just now you're getting token for doing that rather than
[3480.86 --> 3490.22]  right where all you get is reputation or you know uh kudos satisfaction perhaps now inside of the t
[3490.22 --> 3498.46]  protocol can i place like specific bets or like buy into specific packages you can stake against specific
[3498.46 --> 3504.94]  packages so let's say i know my buddy adam is about to release a new npm package a javascript thing
[3504.94 --> 3511.26]  it's going to take the world by storm i could stake his package when it first comes out and as that
[3511.26 --> 3517.42]  package gains in usage i would benefit from that is that how it works not exactly currently like this
[3517.42 --> 3523.18]  is an idea we're playing with yeah you know you should be rewarded for seeing up and coming open
[3523.18 --> 3528.14]  source right that's that's fun right but also plus i can do it on my own packages right
[3528.14 --> 3534.38]  it's good for the package because they get more stake yields right initially that way but currently
[3534.86 --> 3541.58]  if something isn't very staked by many people the yield you get is higher so there is an incentive to
[3541.58 --> 3549.10]  go and find open source that isn't yet popular but you think will become popular getting that early
[3549.10 --> 3554.94]  because your yield is also depending on the impact of that project the t-rank of that project so
[3554.94 --> 3559.98]  okay initially the t-rank of any new project is going to be close to zero you don't get any rewards
[3559.98 --> 3566.22]  for less than 25. it's necessary to have a cut off because otherwise people would just create fake
[3566.22 --> 3571.58]  open source packages right stick them in the system and try to gain rewards that way the t-rank only
[3571.58 --> 3579.26]  uh grows as you become something other projects use the dependency tree okay so you do have to convince
[3579.26 --> 3584.06]  other projects other projects you're worthy and that's exactly how open source already works right
[3584.06 --> 3590.78]  you release something new it takes time for the community to trust that your package is worthy and use
[3590.78 --> 3598.94]  it so we don't fix the uh the initial uptake problem but you know that's that's the case as it is right now
[3599.50 --> 3606.06]  gotcha what is the idea of staking i understand it in like crypto as normal but like if i bought
[3606.06 --> 3612.06]  in and i staked against a project what does that do for it you get a yield describe that to me i mean
[3612.06 --> 3620.06]  like four five percent like a percentage back why would i do that because you want to have a yield of
[3620.06 --> 3625.74]  four or five percent what does the project maintainer get they also get a slightly increased yield because
[3625.74 --> 3633.26]  they're encouraging people to stake now the pro uh t we gain from people staking because it locks the token up
[3633.26 --> 3639.82]  prevents people from uh suddenly selling it there's an unstake period uh this is common with crypto
[3639.82 --> 3647.58]  projects to prevent like rapid fluctuations in token price yeah interesting when i buy in initially who am
[3647.58 --> 3653.82]  i buying the token from uh so we'll be going to launch with several major exchanges still haven't
[3653.82 --> 3660.86]  announced them uh so most likely you will buy from them but you know there will be other ways the token is
[3660.86 --> 3671.90]  distributed initially gotcha do you all keep a a large percentage of the token as creators of the token uh
[3671.90 --> 3679.66]  there is a distribution of some of the token to the investors of my company uh the founders like myself
[3680.38 --> 3687.18]  and some advisors as well but it's a small percentage we're doing what was considered a
[3687.18 --> 3693.74]  a fair launch where more than 50 of the token goes to the community right and it makes sense because like you're
[3694.86 --> 3698.86]  investing in it making it there's there's obviously economic incentives
[3699.42 --> 3703.42]  across the board for it if i knew then what i know now
[3704.22 --> 3708.06]  i wouldn't have done it with vc i would have just launched the token myself
[3708.62 --> 3716.22]  taken none myself and then made it so 100 just goes to open source but you know too late it's fine
[3716.22 --> 3724.46]  can't do it can't change uh not if i don't want to be sued personally yeah okay so but it's it's a
[3724.46 --> 3729.90]  very small percentage relatively and yeah the one of the things we're doing is we're launching the token
[3729.90 --> 3736.30]  from a completely separate company in switzerland it's a non-profit and the long-term goals for that
[3736.30 --> 3743.26]  company are to have it be governed and run by the open source community as well but none of my investors
[3743.26 --> 3748.30]  or any of the other people that are related to the company they invested in have any say in how that
[3748.30 --> 3754.30]  company runs it's very important to me that this is a open source project for the open source community
[3754.30 --> 3760.38]  that's governed by the open source community in the long run how do you go about onboarding then so you
[3760.38 --> 3766.86]  said you mentioned there was how many like a lot of projects onboarded 17 000 17 000 so that's a lot of
[3766.86 --> 3772.14]  you have a decent amount of projects what does it take to onboard what's the incentive obviously the
[3772.14 --> 3779.82]  incentive is to be able to have what is it called t is it called t or chai t token okay t token chai is
[3779.82 --> 3785.10]  the technology the oracle that runs sorry i'm uninitiated here so a lot of my questions are from the
[3785.10 --> 3792.30]  uninitiated standpoint here okay so you have the t token and me as an open source maintainer developer
[3792.30 --> 3801.66]  i go and put my open source t enabled i onboard what is that like yeah so um the way the system
[3801.66 --> 3808.22]  works is it's project based so we declare that a project will receive x amount of t token rewards
[3808.22 --> 3815.58]  every 24 hours in order to have that token go to that project's wallet it's a project wallet one of the
[3815.58 --> 3822.22]  maintainers of the project needs to commit a file the t constitution as we call it to the github repo or
[3822.22 --> 3829.26]  any git repo we're not github specific uh once our system sees that file then the the rewards start
[3829.26 --> 3835.58]  coming in is it challenging to determine ownership at that standpoint from because you got multiple
[3835.58 --> 3840.62]  maintainers core maintainers yeah we trademark holders especially with the wordpress world you got
[3840.62 --> 3846.62]  lots of you know a lot of things happening in this you know ownership state of open source
[3846.62 --> 3851.82]  there's a lot of luck can happen how do you determine who is the true owner i guess of the token
[3851.82 --> 3858.46]  when it comes in if it does become valuable enough to cash in so to speak uh the token goes to the
[3858.46 --> 3865.58]  project wallet and then uh whoever commits that t constitution can declare any number of people
[3865.58 --> 3871.50]  that are considered core contributors to the project they all have control over that wallet now we
[3871.50 --> 3876.14]  haven't made any deliberate decisions on what should happen next every project's different right
[3876.94 --> 3881.50]  most projects really are just one person so it's very simple for them it gets a lot more complicated when
[3881.50 --> 3886.94]  you have like large projects like you know python or node or whatever with wordpress loads of people
[3886.94 --> 3892.78]  and wordpress exactly yeah so we're waiting to see what they're going to do about it but it's on the
[3892.78 --> 3898.78]  blockchain it's an evm compatible blockchain using coinbase's base which uh you know it's just a
[3898.78 --> 3904.70]  layer two on top of ethereum and uh you can write smart contracts to distribute the token so that's what i'm
[3904.70 --> 3910.14]  hoping i'll see is like the open source community stepping up writing smart contracts to fairly distribute the token
[3910.14 --> 3915.58]  like the uh the you know one easy way to do it it's like here's a list of people split it equally
[3915.58 --> 3921.58]  uh much harder way to do it would be based on like pull requests or code contribution and you could
[3921.58 --> 3925.82]  even lines of code just just kidding just kidding just kidding i wouldn't say yeah i've already thought
[3925.82 --> 3931.10]  this through like i was kidding around yeah it'd be a great metric for sure uh incentivize people to
[3931.10 --> 3936.38]  make pr's that are longer and longer for no reason do you anticipate challenges there that you
[3936.38 --> 3941.18]  will get mud on your face from regardless if i guess maybe egg in your face might be the better
[3941.18 --> 3945.34]  term yeah because you don't have you know you're kind of leaving it to them to decide and it might
[3946.06 --> 3953.82]  cause drama oh um on that front i'm i don't think we'll get egg on our face but who knows mud in your
[3953.82 --> 3960.30]  eye egg in your face yeah like one thing i've certainly learned during this project is um there's
[3960.30 --> 3965.82]  there's going to be people that really just don't like it don't like what you're doing and uh they're
[3965.82 --> 3970.46]  going to be angry no matter what you do like when you're doing things that are genuinely new
[3971.26 --> 3975.58]  you know you've got to cross your fingers that you're doing it right and uh let see what see what
[3975.58 --> 3980.38]  the community yes in the end sometimes it's easy to squash that to some degree with the why
[3981.10 --> 3986.14]  like why did you do this like it's one thing to have a capitalistic intent either personally because
[3986.14 --> 3991.58]  you're creating a company around this with venture capital and incentives and then to enable open
[3991.58 --> 3996.06]  source developers to get paid so there's lots of reasons why i'm sure but like what is your personal
[3996.06 --> 4001.50]  reason why like why did you do this so yeah we're going to be quite transparent like as transparent as
[4001.50 --> 4006.62]  possible we're going to be open sourcing most of the uh like probably all of it by the end of the
[4006.62 --> 4012.22]  year actually even the website who cares but my personal reason for doing this is because um three years
[4012.22 --> 4017.90]  ago i was in between full-time work trying to work on open source once again and i looked to see if
[4017.90 --> 4023.66]  anyone had come up with something that could pay me to work on it full time for you know this time
[4023.66 --> 4029.58]  this time i've tried things in the past like patreon spent half my time marketing myself rather than
[4029.58 --> 4033.90]  writing code when i was trying to get out patreon working and uh there wasn't anything new everything
[4033.90 --> 4038.54]  treats open source like all it is is charity all you can expect is a cup of coffee and five bucks
[4038.54 --> 4045.18]  so i decided that maybe it had to be me who fixed this problem and i went down the rabbit hole finding
[4045.18 --> 4050.06]  you know new new ideas trying to find new ideas about it it was like a moment of inspiration one
[4050.06 --> 4056.94]  evening i've had some weed and uh i realized that you know crypto smart contracts and that package
[4056.94 --> 4063.10]  manager data that dependency information i could use that i could do something with that maybe that
[4063.10 --> 4070.30]  would be the solution so we're gonna see we're gonna see when are we gonna see when when yeah so
[4070.30 --> 4075.66]  hopefully by the end of the year maybe early next year and how long will it take everything's built
[4075.66 --> 4080.22]  everything's ready well why aren't we hitting go it turns out crypto's got a lot of legal red tape
[4081.18 --> 4088.54]  yeah as you might expect yeah yeah i think i appreciate people trying new stuff i think there's a large
[4088.54 --> 4094.62]  number of developers who are just so anti-crypto yeah that it's gonna be a stumbling block or
[4094.62 --> 4101.50]  something you'll have to overcome now if it starts to work and work well and it's on ethereum you said
[4101.50 --> 4106.46]  so that's proof of stake right so it's not just it's not the proof of work like bitcoin which a lot of
[4106.46 --> 4111.26]  people have problem with energy draw so it doesn't have that particular problem you know maybe you can
[4111.26 --> 4118.46]  overcome some of the anti-crypto stance of the developer community at large is that fair to say i think so
[4118.46 --> 4122.78]  i've been always more on the fence because i think there's potentially cool and interesting
[4122.78 --> 4127.10]  new things you can do that you couldn't do before and i'm waiting to see them kind of where i've been
[4127.10 --> 4133.02]  you know and so maybe this is one where we say here's a cool use of crypto that actually does what
[4133.02 --> 4138.38]  it's supposed to do and brings value and all that i hope it works out yeah as he was describing the
[4138.94 --> 4146.22]  the dependency graph it reminded me of the way i suppose google or a search engine attributes weight to
[4146.22 --> 4150.78]  or importance to a website which is backlinks it's the same kind of idea where you sort of
[4151.66 --> 4159.82]  define some sort of perceived value based on being in the dependency graph of a project and i'm
[4159.82 --> 4165.10]  imagining that's that totally makes sense and it's not based on whether i think your thing is cool
[4165.10 --> 4169.66]  whether i think your thing is worth funding like it's a matter of yeah it's like is it literally being
[4169.66 --> 4177.98]  used how deep is its importance then you can't scrutinize back to the nebraska xkcd you know drawing
[4177.98 --> 4185.50]  and cartoon because you can see the weight you can you can see the the graph there that says it truly is
[4185.50 --> 4192.22]  important and going back to what you said with patreon or even get up sponsors you spend most of your time
[4192.22 --> 4197.42]  marketing and promoting the fact that you could be paid not doing the things that should get you paid
[4197.42 --> 4203.82]  which provides the value and so it seems like if you can get past this i don't know how to describe
[4203.82 --> 4210.06]  but i guess the idea of crypto anti-crypto yeah the anti yeah the anti-crypto sentiment if it couldn't
[4210.06 --> 4216.14]  play out well because it seems like it should because you can't argue with the the graph you can't argue
[4216.14 --> 4220.70]  with the importance that gets placed on or the weight the perceived weight and value that comes from that
[4221.26 --> 4226.86]  as a result and the developer can keep doing what they're doing not remapping around this new idea of how
[4226.86 --> 4231.26]  to get paid they can just keep doing what they're doing the dependency graph predicts their future
[4232.30 --> 4238.22]  he can stick against it if he wants to which increases my yield increases his yield seems like
[4238.22 --> 4244.54]  it has the right kind of ideas what's the reception so far like you're in the percolation stage
[4245.10 --> 4251.18]  what's the sentiment uh well you're totally right that uh a lot of developers are very anti-crypto and so
[4251.18 --> 4259.66]  that's been a battle from the start uh hacker news hate me even more than usual um but uh inside the
[4259.66 --> 4269.26]  crypto sphere it's uh very popular like 1.7 million signups is pretty unheard of and what it turns out to
[4269.26 --> 4276.22]  be the case to my surprise i've spoken to over 300 open source devs uh over the last three years just you
[4276.22 --> 4282.22]  know for market research reasons a lot of them don't care if it's crypto or not they they like
[4282.22 --> 4288.62]  crypto in the respect that they like technology open source devs aren't as anti-crypto as the others
[4288.62 --> 4295.58]  the rest of the devs you know and yeah i think we have a reasonable chance of showing that crypto is
[4295.58 --> 4301.98]  just a technology um we're not a scam there's nothing scammy about what's going on with us at all
[4301.98 --> 4307.02]  they'll see that once we've gone live and like no one's you know rucking the token or anything like
[4307.02 --> 4311.34]  that right and uh you know it's all open that's one of the beautiful things about web3 all those
[4311.34 --> 4316.86]  smart contracts are transparent readable you can see what's going on right so i'm hoping a few success
[4316.86 --> 4325.18]  stories after the launch people will start to reconsider i have an idea for you or at least let me see if i
[4325.18 --> 4331.58]  understand this right and this is where my idea comes from what if let's play out a scenario what if the
[4331.58 --> 4339.02]  developer world rejects this because they're anti-crypto what if t because you can still
[4339.02 --> 4344.30]  determine the dependency graph with or without onboarding right you can still determine the graph
[4344.30 --> 4348.78]  because it's in get so long as it's open source and available you can determine that graph and
[4348.78 --> 4356.70]  its importance what if it becomes a speculation engine so the people who do care about speculating
[4356.70 --> 4362.14]  can leverage it as crypto whether developers or not and now it's sort of like maybe this adjacent
[4363.42 --> 4371.66]  this adjacent proxy to value and not me saying this but i'm gonna say it who cares if the developers
[4371.66 --> 4377.42]  are anti or for crypto and who cares that they truly adopt this or not it can be a way to speculate
[4377.98 --> 4385.58]  the value of the loan developer in nebraska's thing and create value whether they take it or not
[4385.58 --> 4391.74]  because you can now have a betting world basically against all of open source yeah and there's a
[4391.74 --> 4398.94]  way to make money from or make money slash create value or speculate value and take away that value if
[4398.94 --> 4404.06]  you want it seems like a pretty genius idea to be honest i might have to give you an advisory token
[4404.06 --> 4409.98]  allocation but yeah like um you got a wallet i can't tell if he's being serious or not there's certainly
[4409.98 --> 4416.06]  stuff we could do if like the main idea doesn't work out but like my my uh my passion won't be in
[4416.06 --> 4423.50]  it plan b how about plan b yeah that's plan b yeah because i mean it's it's possible you'll be rejected
[4424.14 --> 4426.86]  that would suck right because you spent years
[4428.54 --> 4434.54]  three years yes doing this that would suck right it would suck but not everything always works out you
[4434.54 --> 4439.58]  know you come to accept that when you're building things yeah i think it would be a real shame if the
[4439.58 --> 4445.58]  only reason it doesn't work out is uh crypto skepticism yeah i hope it's because it doesn't
[4445.58 --> 4450.94]  i mean i hope it works out a but b if it fails i hope it's because it just the idea fails not because
[4451.74 --> 4457.98]  haters i just you know did a bad job i don't know though i think with my idea if it truly is a good idea
[4457.98 --> 4463.26]  i think you could do both it doesn't have to be just because you're rejected plan b is x i think it
[4463.26 --> 4470.14]  could be both based on what i hear now this is 20 minutes of podcasting which i haven't dug into
[4470.14 --> 4475.50]  the white paper or the details and stuff like that but i can't see based on what i've heard so far why
[4475.50 --> 4480.86]  it couldn't be both because it's already doing that it already can be speculated against if i have a
[4480.86 --> 4487.02]  project and jared wants to stick against it he can so that's all you're doing it's it's about perception
[4487.02 --> 4491.10]  and mechanics and marketing really a story than it is simply what it can or can't do
[4491.10 --> 4497.50]  yeah i'll certainly go away and think about it i don't think it's likely we would launch with both
[4498.30 --> 4502.78]  partly because you know well i don't mean you could do both though it's still possible to do
[4504.22 --> 4507.58]  just because you don't market it that way doesn't mean i can't use it that way
[4507.58 --> 4512.62]  is my point well they would have to do a dependency graph against all projects everywhere right true
[4512.62 --> 4517.58]  versus the ones that are registered you're currently tracking you do the depends against all projects
[4517.58 --> 4525.42]  everywhere already yeah i mean and then you give a you give a pathway to this thing that's one
[4526.86 --> 4531.74]  software's eating the world open source is eating software kind of thing now anybody who ever wants to
[4531.74 --> 4538.06]  speculate against open source can not saying they would i have no idea about that but it's it's an
[4538.06 --> 4543.50]  interesting something to chew on something to chew on for sure yeah there's certainly lots of things
[4543.50 --> 4549.26]  we can do with the data like the chai database on chain oracle uh-huh scroll the dependency data and
[4549.26 --> 4555.98]  it's got the uh the the rankings uh we're exploring the idea of building out uh s bombs based on that
[4555.98 --> 4563.10]  which give you actual impact your stack yeah and uh you know threat identification essentially allowing
[4563.10 --> 4569.18]  companies to donate or stake based on you know the uh the s bomb we're generating yeah totally cool
[4569.18 --> 4574.94]  the idea of like building out some sort of like polymarket-esque thing as well but you know as as you
[4574.94 --> 4579.50]  say that other people can do that right like the data is on the chain you can build against it yeah
[4580.06 --> 4583.66]  all right it's one of the things we're looking forward to actually seeing what the oversource community
[4583.66 --> 4590.78]  just do on top of these primitives that we've built for them interesting so is this limited to libraries then
[4590.78 --> 4599.02]  um almost you know because uh like i was saying it wouldn't solve homebrew's problem uh not itself
[4599.02 --> 4605.90]  no interestingly homebrew isn't even actually in the system because it's not packaged by anything right
[4607.98 --> 4615.18]  pretty popular project though kind of embarrassing for me um but it's a limitation of the current model
[4615.18 --> 4622.70]  yeah like uh once chai is open sourced which uh spoiler alert i'm doing that during my keynote in
[4622.70 --> 4628.54]  in an hour nice we're hoping that people will come forward with suggestions for how to fill in these gaps
[4628.54 --> 4634.22]  and i help us help us to build it out yeah that would be cool because right now it would be limited by
[4634.22 --> 4638.70]  the dependency graph so you need to have dependencies yeah so you can't be a command line tool or an
[4638.70 --> 4644.62]  application or these other open source projects to use this particular well sometimes you can be a command
[4644.62 --> 4649.34]  line tool because some of the command line tools are dependencies of other command line tools sure
[4650.06 --> 4656.46]  but it wouldn't track your actual usage right uh well we don't really track usage either of course but
[4656.46 --> 4661.42]  but you would want to right like if if homebrew gets more used i know it's not in there but if you
[4661.42 --> 4667.98]  if you imaginarily covered it it would be based on usage right well we have a new idea that we've been
[4667.98 --> 4673.10]  developing over the last few months oh yeah we'll fix this that we'll be uh announcing next year oh
[4673.10 --> 4680.86]  uh it's a different you want to spoiler alert us on uh i they're not they're not but it's rather
[4680.86 --> 4687.26]  lovely and very excited about it and it does solve some of these issues uh for a different different
[4687.82 --> 4696.54]  use like it tries to tap into the fundamental utility of open source so phase one we're releasing this um
[4696.54 --> 4702.86]  essentially a remuneration platform for open source maintainers phase two is exposing
[4702.86 --> 4708.78]  the the real value of what open source represents wow and uh yeah should be pretty exciting and this
[4708.78 --> 4713.10]  is you said it's trackable on coinbase is that right because of the way it's protocol you didn't name a
[4713.10 --> 4721.66]  specific one uh no you said something i used we use base which is coinbase's blockchain okay so certainly
[4721.66 --> 4728.62]  it's going to be on coinbase but he hasn't said where you can buy this token to be uh disclosed where we
[4728.62 --> 4735.98]  we will be selling is there a way that you could um leverage this to secure the open source supply
[4735.98 --> 4742.78]  chain as it said i don't really like the term supply chain but that's the accepted term of open
[4742.78 --> 4747.82]  source supply chain is there a way to like leverage what you're doing with t not just to incentivize to
[4747.82 --> 4754.14]  maybe gain value but maybe leverage that in a way that can ensure security for open source packages or
[4754.14 --> 4758.78]  reward those who are more secure or just anything that like just bolsters the security of open source
[4759.34 --> 4766.30]  yeah so going into this that was definitely one of the things i wanted to achieve and we have ideas
[4766.30 --> 4771.58]  for how that could play out with what we built already like we're kind of securing it to some extent
[4771.58 --> 4778.06]  because we're securing the maintainer's ability to actually work on these things but we have plans
[4778.06 --> 4781.74]  later one of them is inside the thing i was just talking about that we're going to be announcing
[4781.74 --> 4789.66]  early next year uh which do have tangible as extra security benefits to the open source ecosystem
[4790.22 --> 4795.02]  so yeah so it's in our best it's in our best interest to find a way to make this play out
[4796.06 --> 4801.98]  me and yours like generally we as in the community because if they have these kind of plans and there's
[4802.46 --> 4807.74]  altruistic ways to get there we certainly want to know what he's going to disclose in early next year
[4807.74 --> 4813.74]  that's what i'm trying to tell you after the podcast well max best of luck t.xyz is that right
[4813.74 --> 4821.66]  yeah t.xyz t the drink t-e-a-t-e-a-t-e-e-e or just the letter t-t yeah with hindsight the name
[4821.66 --> 4828.46]  wasn't great a lot of hindsight well hopefully some foresight i'm excited to see what happens when you uh
[4829.10 --> 4835.26]  when you launch so launch yeah well thank you get to it forward to it end of year it's very soon
[4835.26 --> 4840.62]  hopefully very soon all right famous s words good luck with your keynote as well yeah all right max
[4840.62 --> 4841.58]  all right thanks
[4848.62 --> 4855.42]  what's up friends i'm here with a new friend of ours over at assembly ai founder and ceo dylan fox
[4855.82 --> 4863.02]  assembly ai is where you can turn voice data into insights chapters transcripts summaries and so much
[4863.02 --> 4868.30]  more with their leading speech ai models so dylan give me a glimpse into what you're doing with
[4868.30 --> 4875.26]  speech ai models at assembly ai so at assembly we're building industry leading speech ai models for
[4875.26 --> 4881.34]  various tasks like speech to text streaming speech to text speech understanding to help developers
[4881.34 --> 4887.26]  easily convert voice data whether it's live or pre-recorded into super accurate text and then to help
[4887.26 --> 4892.86]  developers extract a ton of information and metadata around voice data or even around the text that they
[4892.86 --> 4899.50]  just were able to convert from that audio data so these are things like picking out entities or pii that
[4899.50 --> 4908.70]  was spoken in voice files or summarizing voice and audio data down into custom summaries it's things like
[4908.70 --> 4913.18]  being able to detect how many speakers spoke and who said what and what the names of different speakers
[4913.18 --> 4920.22]  were so we bundle all those things into a super simple api with really great docs that developers can
[4920.22 --> 4926.62]  just sign up to for free to start use the api build into their apps and then build these really cool ai apps and
[4926.62 --> 4932.78]  products and workflows and automations on top of voice data with i dig it okay can you take me a little deeper
[4932.78 --> 4938.38]  into the opportunity for developers because it seems like there's a lot of voice data out there and there's a lot of
[4938.38 --> 4944.46]  trapped value in that voice data there's so much voice data being created on the internet now
[4944.46 --> 4952.54]  podcasts videos phone calls voice messages audiobooks virtual meetings it's crazy and you can now
[4952.54 --> 4958.22]  transform and understand all this voice and audio data in ways that were not even possible a year 18
[4958.22 --> 4964.06]  months ago so what we're seeing with the help of these new ai models that we're creating at assembly
[4964.06 --> 4970.38]  developers and organizations are just racing to build all these new applications workflows automations
[4970.38 --> 4975.82]  that leverage the voice data they have either within their organization or within their product
[4975.82 --> 4981.50]  build really cool new products and services workflows that are just like taking off in the market so at
[4981.50 --> 4986.62]  assembly we're building the industry leading models for all those different apps and workflows whether
[4986.62 --> 4992.30]  it's speech to text or speaker diarization or speech understanding capabilities to summarize voice data or
[4992.30 --> 4998.78]  extract entities voice data or mask pii from phone calls for various types of automations that might
[4998.78 --> 5003.74]  be built and we're exposing that through a super simple super scalable api that's just constantly
[5003.74 --> 5009.10]  being updated and constantly getting better and so we're seeing a crazy amount of developers and
[5009.10 --> 5015.10]  companies just build really cool apps and services on top of our api every day uh it's really only just
[5015.10 --> 5019.66]  getting started especially with the the model updates that we have planned over the second half of the
[5019.66 --> 5024.62]  year that are coming out they're really excited to launch to the developers on our api okay
[5024.62 --> 5032.06]  constantly updated speech ai models at your fingertips well at your api fingertips that is a good next step is
[5032.06 --> 5037.42]  to go to their playground you can test out their models for free right there in the browser or you can get
[5037.42 --> 5047.10]  started with a 50 credit at assemblyai.com practical ai again that's assemblyai.com practical ai
[5047.10 --> 5056.78]  tell us about this uh yeah what do you guys want to hear about the state of open source funding
[5057.34 --> 5059.50]  sustainability pledging
[5059.50 --> 5065.26]  osspledge.com this is your new thing funds well open source funds what's the state so we got a
[5065.26 --> 5070.70]  couple things so the state of funding there's a couple ways we could take this and since we're
[5070.70 --> 5076.06]  going to cap this to 20 minutes i'm going to say the words fair source okay i'm just going to put that
[5076.06 --> 5082.22]  there and maybe we'll come back to that later so don't don't don't bite on that i i know i know
[5082.22 --> 5087.82]  that maybe something we could have a little more vigorous conversation about let's do it but yeah man no the
[5087.82 --> 5094.94]  the past past year launched two initiatives fair source and open source pledge both kind of coming
[5094.94 --> 5099.66]  out of this place of trying to balance the user freedom that we enjoy in open source with the
[5100.22 --> 5105.82]  pragmatic practical realities so you're not idealist either correct we're not idealist
[5105.82 --> 5109.82]  either correct correct okay yeah balancing freedom and sustainability is how we think about
[5109.82 --> 5114.54]  it developer sustainability so pledge in particular is really exciting we launched this
[5114.54 --> 5120.78]  on october 8th what day is it today it's like the 28th or something right so not quite three weeks
[5120.78 --> 5127.90]  about three weeks ago three weeks tomorrow we put up three billboards in san francisco we rented three
[5127.90 --> 5133.82]  of the most expensive billboards in the world to tell a story about the change that we need in the
[5133.82 --> 5140.86]  industry to pay the maintainers and this is the pledge the pledge is a group of companies that are
[5140.86 --> 5147.02]  working together to change the status quo in open source sustainability okay companies that join
[5147.98 --> 5152.30]  make a commitment so there's there's two two parts to joining number one is you go pay maintainers
[5153.10 --> 5159.74]  number two is you blog about it okay so the pay maintainers we have a barrier to entry we have a
[5160.86 --> 5167.26]  an entrance fee if you will so we use this dollars per developer number so that companies of very
[5167.26 --> 5173.50]  different sizes can kind of you know we can compare across two thousand dollars per developer on staff
[5173.50 --> 5179.18]  to open source maintainers meaning no strings attached payments to your dependencies essentially okay
[5179.98 --> 5185.82]  could be foundations could be github sponsors open collective whatever so pledge itself is not
[5185.82 --> 5192.70]  actually touching any money what we're doing is bringing kind of the social validation layer to it
[5192.70 --> 5197.42]  and saying we've already got get up sponsors we already got open collective thanks dev platforms
[5197.42 --> 5203.98]  that'll help you do this we already got all the foundations so number one go pay maintainers so a
[5203.98 --> 5209.82]  company has a hundred developers they would pay two hundred thousand dollars per year to maintainers and
[5209.82 --> 5217.34]  then number two is blog about it blog about it means you tell us who you paid uh and how much that's
[5217.34 --> 5222.54]  your annual report and that does two things number one it drives awareness because now we've got
[5222.78 --> 5227.34]  blogs on everybody's blog out in the world talking about the open source pledge so building kind of
[5227.34 --> 5231.98]  that social validation piece but then it's also the accountability so that people in the community
[5231.98 --> 5236.62]  can you know we're looking for receipts who did you actually pay what right so it gives the community
[5236.62 --> 5242.62]  a way to go and look and say uh you know all right century says they're you know paying 750
[5242.62 --> 5248.46]  000 to open source who'd they actually pay right look for those receipts yes that's the pledge so two inputs
[5248.46 --> 5253.90]  one being money and the other being the blog post blog post annual blog post and what do they get
[5253.90 --> 5261.58]  out of it what do they get json jace always jason yes man jason all right that's how you pay
[5261.58 --> 5268.78]  maintainers jason yeah tell me more some pretty good jason that's it uh yeah always down for a good jason
[5268.78 --> 5273.82]  schema you know yeah so what do you get out of it is you get essentially it's a lightweight
[5273.82 --> 5278.94]  certification you get a member badge it says open source pledge member so then you can go out you
[5278.94 --> 5283.18]  know a lot of who we're going for at the beginning is developer tools companies you want to sell
[5283.18 --> 5287.66]  to developers you want to demonstrate your goodwill in the open source community you get that badge it
[5287.66 --> 5292.22]  says open source pledge member and then you know as we build this thing out that starts to mean
[5292.22 --> 5297.42]  something right so i want to make my decisions about what tooling i'm going to use if i see that open
[5297.42 --> 5302.94]  source pledge member badge in the footer i know that this company is actually paying maintainers
[5302.94 --> 5307.90]  uh in a real way so that's that's the number one thing you get is that kind of cred yeah i mean
[5307.90 --> 5312.86]  it's really about the branding the marketing you know and and companies who want to tell you know
[5312.86 --> 5317.18]  who want to tell a good story about open source saying all right you know you want to talk game
[5317.18 --> 5323.50]  like this is how you do it this is how you actually support open source okay you buy it i don't know i
[5323.50 --> 5327.74]  mean i think i'm on the fence still yet what's that you're on the fence i'm on the fence still yet i think
[5327.74 --> 5334.86]  that i guess like if you get the company like if you actually if it becomes a thing yeah right so
[5334.86 --> 5339.18]  it's kind of a it's not really a thing yet you're trying to make it a thing if it becomes a thing
[5339.18 --> 5344.38]  then i get a thing but in the meantime yeah nobody cares about it then i don't care about it just
[5344.38 --> 5348.30]  thinking as a guy who's running a company yeah it's like well if i don't currently care about
[5348.30 --> 5353.34]  supporting my dependencies yeah because of all the reasons why i should instead i'm going to do it
[5353.34 --> 5357.66]  because the pledge exists and i want to look good i don't know if i'm sold right now because
[5357.66 --> 5363.34]  it's brand new right and you got a handful of companies doing it but so we launched so it was
[5363.34 --> 5369.66]  brand new on august 28th so what that's two months ago exactly right pretty new so it's brand new on
[5369.66 --> 5376.62]  august 28th sure the two companies that were the first to join were century my employer and you want
[5376.62 --> 5382.78]  to guess who the other one was it was a i was surprised too i was paying attention i think it was
[5382.78 --> 5387.82]  like a i don't know tell me but yeah i was surprised it was astral do you know astral
[5387.82 --> 5395.18]  astro.build astro.build is also coming along astral a-s-t-r-a-l oh yeah they're the ones
[5395.18 --> 5400.54]  that are doing like python tooling and rust yes yes yeah yeah and they are venture backed by excel
[5400.54 --> 5406.86]  correct okay just like century is okay actually excel so excel partners are kind of like so i mean
[5406.86 --> 5411.50]  it's networking man this is all the social like this is social networking this is like
[5412.70 --> 5420.06]  herd mentality i mean what company is not an ai company today sure three years ago you know we
[5420.06 --> 5425.58]  weren't talking about at all right like for better for worse humans are herd animals companies are
[5425.58 --> 5429.34]  herd animals and that's kind of what we're trying to work with here you know when you're you talk about
[5429.34 --> 5436.30]  sustaining open source i see there's three levers that we can pull number one is commercialization
[5436.30 --> 5440.78]  so you build a company around your project open source itself is not a business model but you know
[5440.78 --> 5445.10]  over the past decades we've come up with business models yeah so commercialization is one way to
[5445.10 --> 5451.02]  sustain open source to subsidize an open source product on the other end is taxation so sovereign
[5451.02 --> 5455.90]  tech fund is doing this they're spending german taxpayers money on critical digital infrastructure
[5455.90 --> 5460.78]  yeah okay so both those are fine that's good what we're going after with pledge is this middle
[5460.78 --> 5468.86]  lever which i think of as validation social validation right again you want to be seen another way i think
[5468.86 --> 5475.74]  of it is it's not an exactly perfect analogy but open source is kind of like a restaurant okay
[5477.02 --> 5484.38]  here's what i mean by that please yes tell us more i'm excited what what's on the menu okay open source
[5484.38 --> 5490.70]  is kind of like a restaurant it's not perfect but bear with me i go into a grocery store and i pay for
[5490.70 --> 5497.18]  my food first and then i take it home and i eat it okay i go into a soup kitchen and somebody else pays
[5497.18 --> 5504.30]  for it it's a charity and i get to eat okay i go into a restaurant and you know we go in together it's
[5504.30 --> 5508.86]  social first of all we go in we sit down we have a nice meal and it's at the end of the meal when the
[5508.86 --> 5515.02]  food's in our bellies that we settle up and we pay the tab right so it's like a restaurant in that
[5515.02 --> 5519.42]  you're paying for this thing you already ate you know you already consumed it so year after year
[5519.42 --> 5524.46]  our companies are consuming open source we're feasting at the open source table okay and what
[5524.46 --> 5530.38]  we're doing with pledge is saying all right now it's time to settle up to pay for the open source
[5530.38 --> 5534.54]  that we've consumed yeah year over year and this i get there because of the social aspect right
[5534.54 --> 5538.62]  yeah i understand that's the part you're trying to drill down on yeah see i saw it differently then
[5538.62 --> 5542.30]  okay not the analogy i don't disagree with the analogy necessarily but all right what are you
[5542.30 --> 5546.62]  seeing i saw what you were doing with the open source pledge or oss pledge to be more clear
[5547.50 --> 5552.46]  was an extension from what we did a while back with maintainer month and maintainer week okay it
[5552.46 --> 5556.94]  was maintainer week and the maintainer month and it was oss fund it's the same idea that you started
[5556.94 --> 5561.82]  with century which was for every developer yeah whatever your number is is your number but you said
[5561.82 --> 5565.82]  two thousand dollars per developer was the good algorithm to use yeah that's our minimum yep
[5565.82 --> 5570.78]  right and so i also i saw open source pledge this oss pledge yeah to be an extension of that but more
[5570.78 --> 5575.58]  with an awareness piece to it because it was hard it was like you were pushing this uphill battle to say
[5576.54 --> 5580.78]  companies should have an oss fund yeah which is a great thing to say but then it was like well how
[5580.78 --> 5586.86]  do we do it yeah where's this yeah the foss fund yeah thank you for clarifying yeah i saw it as
[5586.86 --> 5592.30]  like an extension of that but potentially better marketable yeah you know and potentially with this
[5592.30 --> 5598.38]  social component yeah that is not so much a force multiplier but more like uh you should because
[5598.38 --> 5602.38]  this is where people who are doing this and believe in this model yeah are collecting whereas
[5602.38 --> 5607.74]  the other way it was more like soapbox yeah you know whereas here you're sort of like yeah
[5607.74 --> 5611.50]  what was that hands across america like back in the 80s remember that it's more like that you
[5611.50 --> 5616.70]  know like hand in hand across america feeding i think it was the hunger something like that no you're right i mean
[5616.70 --> 5621.58]  mean so foss funders i mean it still exists but foss funders isn't this is in some ways
[5622.54 --> 5629.18]  you know a version of that foss funders v2 so duane o'brien is leading foss funders love duane
[5629.18 --> 5635.66]  love foss funders open source pledge is yeah it's kind of a v2 where we're saying let's get
[5636.38 --> 5641.02]  an actual dollar amount because the thing with foss funders like i built a foss funders.com website i
[5641.02 --> 5644.86]  recruited companies to put a logo on it you know it links out to a blog post some of those same
[5644.86 --> 5649.10]  mechanics were there yeah what was missing was there was no threshold there was no consistency
[5649.10 --> 5653.18]  across that it's like one company gives ten thousand dollars another company gives a hundred
[5653.18 --> 5657.98]  thousand dollars and like how are you thinking you know it's got to mean something you know it's like
[5657.98 --> 5663.66]  when i see that a company's on open source pledge like when you see it here's what i want to say when
[5663.66 --> 5667.10]  you see that a company's on open source pledge or when your listeners see that a company's on open
[5667.10 --> 5671.82]  source pledge they should think oh this company's putting their money where their source is this is your
[5671.82 --> 5676.22]  meme all right speaking of memes and credit speak when you when you said that we picked up on it
[5676.22 --> 5681.34]  yeah we use that somewhere you said that i said it i've said it a few times over the years i said it
[5681.34 --> 5685.98]  on change dog news and and you picked it up yeah that's something i uh all right so shout out to
[5685.98 --> 5690.38]  jerry right in there adam putting your money where your source is yeah send us the bill for the
[5690.38 --> 5693.82]  copywriting jared i'll uh yeah i will no we like that one put your money where your source
[5694.38 --> 5698.70]  up to the buffet you've had your meal yeah now it's time to put your money where your source
[5698.70 --> 5703.74]  yeah i mean that's the main message it's like when you see that open source pledge
[5703.74 --> 5708.78]  member badge you should know wow this company they put their money where their source is that's what
[5708.78 --> 5713.98]  we're going for but yeah man early days so two months ago we launched with two that was a soft
[5713.98 --> 5717.82]  launch we put these billboards up i don't know how much time we have to get in all the billboards
[5717.82 --> 5723.66]  and everything but we put these billboards up on october 8th so that's the three weeks ago yeah by the
[5723.66 --> 5728.54]  the time we put the billboards up we had 25 companies on board so we went from two to 25
[5728.54 --> 5733.10]  and i'll tell you when we add those two i was like what are we going to have on october 8th because we
[5733.10 --> 5736.78]  signed a contract for billboards and we're going one way or another and i don't know if it's just us
[5736.78 --> 5742.14]  and astral then it's just us and astral but we had yeah 25 companies join us for that launch so we
[5742.14 --> 5748.70]  feel really good about that yeah we had seven well six open source foundations that gave us endorsements
[5748.70 --> 5753.66]  you know because the pledge is companies but you know on the essay equations all the foundations and
[5753.66 --> 5759.26]  the maintainers and so we got endorsements from osi and five other open source foundations php and
[5759.26 --> 5765.50]  jango and whatnot yeah so i feel like we had a lot of good momentum for launch but yeah man it's all
[5765.50 --> 5771.50]  about what happens next right it's like next three six months i'm i'm a salesman now you guys i'm like
[5771.50 --> 5775.18]  he's selling it this is what i signed up for now i got to go door to door and be like right
[5775.18 --> 5780.70]  hey who wants to this is your baby well it's it's david kramer's baby let's be honest but you're
[5780.70 --> 5786.46]  carrying the torch exactly fair enough that's your job that's my role these days but all right
[5787.50 --> 5790.94]  keep an eye on it keep an eye on it yeah i'm excited to see what happens
[5792.06 --> 5797.50]  two to 25 is definitely a move yeah that's a move if you went two to four i'd be like right
[5797.50 --> 5802.62]  two to 25 is legit 24 is no if you went from two to four i was like two to four i'm like
[5802.62 --> 5808.78]  oh i put out the twitter poll and i was like where are we going to be at launch and everybody
[5808.78 --> 5814.70]  had me at five to launch okay so i feel pretty good about 25 yeah yeah yeah for sure but it's
[5814.70 --> 5820.86]  what happens next right is it on the honor system well so there's no there's no vetting and verification
[5820.86 --> 5826.62]  right blogging the blog the blog is there the blog is there and we we do go look at the blog when
[5826.62 --> 5830.22]  you get onboarded right we look at your blog and we go back and forth you know this is what we're
[5830.22 --> 5835.90]  looking for who's we so there's four of us on the core team okay two of us from century two
[5836.46 --> 5842.86]  organic community members that showed up to participate vlad and ethan are are not employed
[5842.86 --> 5847.98]  by century myself and michael are at century so that's the we and you know we'll grow that kind
[5847.98 --> 5855.74]  of formality of it over time as as we grow but um yeah we we launched with 25 we got so we do vet
[5855.74 --> 5861.10]  here's what i want to say on that going back to what i was saying earlier get up sponsors thanks
[5861.10 --> 5867.58]  dev open collective these platforms that do this our goal is to build that up so that they help with
[5867.58 --> 5873.74]  the receipts so thanks thanks devs helped me out a ton okay so i'm doing i'm gonna you know past years
[5873.74 --> 5877.82]  you guys and i have talked about century's own funding program so this is kind of the extension of
[5877.82 --> 5881.66]  that where we say all right now can we get other companies to join us with this right so century's own
[5881.66 --> 5885.90]  funding program for this year uh it's gonna launch in a couple weeks we'll land that in a couple weeks
[5885.90 --> 5891.42]  had to push it back because i was distracted by the pledge thanks dev is my main vendor for that
[5891.42 --> 5897.50]  and they yeah they're helping us out with all right what kind of reporting do we want for the pledge
[5897.50 --> 5902.06]  and how can these vendors help us with those receipts so that it's not just an honor system
[5902.06 --> 5906.22]  there's a little more meat to it so really trying to incentivize that ecosystem well whoever would put
[5906.22 --> 5911.98]  out a blog post saying you funded open source and you didn't fund open source i made a face by the
[5911.98 --> 5916.30]  way it was not a good face well there is this happens there's not just saying like that if you
[5916.30 --> 5920.22]  didn't if it did happen right yeah if you would put out if you would go through the motion of saying
[5920.22 --> 5927.82]  i pledge yeah i blog and that blog was non-factual yeah i mean big time you know yeah yeah yeah yeah
[5927.82 --> 5933.58]  so yeah receipts and so i joked about the json earlier and you never close a loop yeah what's the
[5933.58 --> 5943.10]  json deal there is json there is close a loop of the json okay so there is uh well so what we have
[5943.10 --> 5947.10]  people do and i don't know if we'll do this forever but we're the way the system is set up we're going
[5947.10 --> 5953.02]  to geek out for a second here to join the pledge a company publishes a json file they publish their
[5953.02 --> 5960.14]  blog post but then they publish a json file because this is an annual thing right it's an annual thing so
[5960.14 --> 5964.14]  every year you got to pay every year you got to publish a blog post so i built a system where
[5964.14 --> 5968.62]  they publish a json file that says here's the number of developers we have here's the amount
[5968.62 --> 5973.18]  of money we spent and here's the link to our blog post about it and then they can update that year
[5973.18 --> 5977.58]  over year and then we pull that in with a github action or whatever on our side yeah so that's where
[5977.58 --> 5983.74]  the json comes yeah anyway so they give a json they don't get a json that's just more given
[5983.74 --> 5989.98]  yeah but they become part of i mean you're gonna like report that or i mean somehow that thing
[5989.98 --> 5993.58]  you should pull together to a master json file they do get a json though because when they go
[5993.58 --> 5999.10]  through the flow yeah they they generate the json file for them who does we have it we built that
[5999.10 --> 6003.90]  out of source plays.com vlad one of the one of the folks working on it built that out on the website so
[6003.90 --> 6009.98]  if you are at a company that wants to join the pledge then you go to open source pledge dot com dot com
[6009.98 --> 6015.90]  okay you'll see a join button there open source pledge dot com slash join um we'll walk you through
[6015.90 --> 6021.10]  the steps including yeah we'll build that json for you we'll give you a gift of a json file
[6021.10 --> 6025.42]  they gift you a json but what do i do with that then you put that on your domain to validate that
[6025.42 --> 6031.98]  it's legit more work for me that's more work we'll streamline it early days early days yeah cool
[6031.98 --> 6039.42]  well good stuff yeah yeah keep an eye on us so let's wave a magic wand okay okay yeah put it here
[6039.42 --> 6043.66]  down right now all right how much time you got three minutes yes three minutes three minutes okay
[6043.66 --> 6049.82]  he's got less than three minutes to wave this magic wand it is pick your number of years from now yeah
[6049.82 --> 6055.66]  one two five whatever what's the goal what do you want to like what would be best case scenario yeah
[6056.54 --> 6064.14]  you know so when i go to san francisco i like to read embarrassingly basic cringy business books on the
[6064.14 --> 6069.34]  plane you know so i was there two weeks ago i was reading crossing the chasm okay i want everyone on
[6069.34 --> 6074.46]  the plane to know that i'm reading michael brenich chasm yeah exactly yes exactly crossing the chasm
[6074.46 --> 6080.14]  that's it right innovators dilemma sorry you know crossing the enterprise chasm is really the long term
[6080.14 --> 6086.46]  that's kind of the playbook that i'm seeing for this for this to be successful the intent is really to
[6086.46 --> 6090.94]  have as much of the industry as we can participate so we're looking at this whole thing with the
[6090.94 --> 6096.46]  the innovators the early adopters the early majority and the late majority you know wave the
[6096.46 --> 6104.70]  wand if it's five years from now and we're across the chasm and we've got a thousand companies on board
[6104.70 --> 6110.78]  and some of those companies have 5 000 developers on board we're doing great if it's a year from now
[6110.78 --> 6118.14]  we've got i mean 100 companies maybe 200 companies you know and there's some of those centuries 135
[6118.14 --> 6123.02]  developers if we have a develop a company that has 500 developers on board a year from now i'm feeling
[6123.02 --> 6127.42]  really good about it you know you're currently the biggest one yeah absolutely yeah yeah so you need
[6127.42 --> 6131.42]  some big fish you want a lot of fish but you want some big fish yeah so we're we're going broad and
[6131.42 --> 6136.46]  then we'll grow it up you know because it's about it's about i want to say peer pressure but it's about
[6136.46 --> 6141.90]  that you know validation that we're doing this together century 135 developers like microsoft's not
[6141.90 --> 6145.58]  joining tomorrow you know what i mean it's like we got to make the environment a little different
[6145.58 --> 6150.94]  before we can get there build it over time all right thanks chad opensource pledge dot com go
[6150.94 --> 6156.86]  there now yeah and look for that badge get the get your json on that's it all right thanks guys
[6160.46 --> 6166.86]  okay to the many people we saw in the hallway at all things open well hey it's good to see you
[6166.86 --> 6174.38]  we met a lot of people who were there on the coupon code we gave out the free one in most cases
[6175.10 --> 6183.18]  and in some cases the discounted version and that's so cool lots and lots of listeners of the changelog
[6183.18 --> 6191.66]  at this conference and that that's even cooler so this anthology episode covered lots of stuff the state of
[6191.66 --> 6204.86]  enterprise linux rel centos fedora ubuntu alma rocky the list is long we cover t dot xyz this new protocol
[6204.86 --> 6213.10]  that may give value back may give rewards back to open source maintainers that's cool and of course
[6213.10 --> 6220.30]  open source pledge dot com and chad's work and david kramer's hard work on this from century to
[6220.30 --> 6228.38]  support open source maintainers to find ways to find models for organizations and teams to adhere to
[6228.38 --> 6233.10]  so they can give back so they could do the right thing and to support their open source that they're
[6233.10 --> 6240.22]  using and that's cool too lots of cool stuff okay on friday a fun friends episode from the hallway
[6240.22 --> 6246.86]  track again at all things open different people different conversations maybe a little more fun
[6246.86 --> 6252.14]  i don't know you tell me but a massive thank you to our friends at century who happen to be also a
[6252.14 --> 6258.46]  sponsor of this episode just happenstance we love century we use century century is awesome
[6258.46 --> 6265.82]  and our friends over at coder coder.com eight sleep eight sleep.com slash changelog my gosh get one of
[6265.82 --> 6272.46]  these sleep on it it would change your sleep life trust me and of course our friends at assembly
[6272.46 --> 6280.22]  ai check them out assembly ai.com and those beats they're banging banging banging thank you
[6280.22 --> 6286.38]  break mess of cylinder for those banging beats the beat freak in residence always bringing the beats
[6287.02 --> 6292.54]  so good okay that's it this show's done what are you still doing here it's time to go we'll see
[6292.54 --> 6301.18]  you on friday okay we'll see you on friday
[6301.18 --> 6305.18]  so
[6305.18 --> 6307.18]  so
[6322.54 --> 6335.18]  you
