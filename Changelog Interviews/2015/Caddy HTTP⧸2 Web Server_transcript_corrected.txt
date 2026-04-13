[0.00 → 15.52] welcome back everyone this is the change log and I'm your host Adam stekowiak this is episode 179
[15.52 → 22.52] and on today's show jerry went solo talking to Matt Holt and Sebastian Earhart talking about caddy the
[22.52 → 29.68] h2 web server written and go made for everyone and a special thanks goes out to Justin Dorfman
[29.68 → 35.60] for creating the issue and Carissa Campos and many others for thumbs upping this suggested show
[35.60 → 40.60], so thanks for your support and if you want to suggest a show go to our ping repo on GitHub
[40.60 → 47.46] that's GitHub.com slash the change log slash ping you will find issues there submit one and at mention
[47.46 → 52.70] any developer out there on a project, and we'll do our best to dig deep and get them on the show
[52.70 → 59.56] we have four awesome sponsors making the show possible code ship top towel image
[59.56 → 66.56] and also Linde our first sponsor is code ship a hosted continuous delivery service focusing on
[66.56 → 71.74] speed security and customizability easily set up continuous integration for your app today
[71.74 → 77.78] in just a few steps and deploy when all your tests pass code ship has great support for lots of
[77.78 → 83.84] languages test frameworks and notification services they even integrate with GitHub and Bitbucket and
[83.84 → 88.90] you can deploy the cloud services or even your own servers get started today with their free plan
[88.90 → 95.78] when you upgrade to a premium plan use the code the change law podcast and save 20 off any plan you
[95.78 → 102.64] choose for three months again the code is the change law podcast head to codeship.com slash the
[102.64 → 105.34] change law to get started and now on to the show
[105.34 → 118.92] all right everybody we are back, and we are excited today this show actually came to us by popular
[118.92 → 125.84] demand um two of our members Justin Dorfman and Carissa Campos were advocating
[125.84 → 134.88] for a show on the caddy web server uh they opened up an issue in ping and didn't stop there I think they
[134.88 → 140.50] were tweeting about it many plus ones came in, and we finally relented and said man I guess we have
[140.50 → 149.10] to have a show about caddy so we're excited we're here joined by Matt Holt and Sebastian air hart guys
[149.10 → 155.86] welcome to the change law thank you glad to be here so Matt uh were you surprised that you had such a
[155.86 → 164.14] uh a group of people excited to hear all about your fledgling web server yeah um it seems to excite a
[164.14 → 171.12] lot of people and I mean I'm glad i just I am surprised because it's its a web server it
[171.12 → 176.54] didn't seem that exciting on the surface well you know us developers we get excited about all sorts of
[176.54 → 185.74] things uh and by the way I'm quite excited as well as a bit of a web server uh nerd as well i I do
[185.74 → 189.06] geek out on these things so I'm quite excited about caddy had not actually even heard of it
[189.06 → 194.92] um previous to them opening up that issue and I think they even had a little bit of a back channel
[194.92 → 200.80] conversation in our members only slack room about it and they Justin Carissa ganged up and decided
[200.80 → 207.36] they were going to bombard our GitHub issues um so let's let's learn a little bit about you guys and
[207.36 → 212.60] then we'll get into caddy, and we'll find out all about it and uh why it's cool why so many folks are
[212.60 → 218.16] interested in it uh Matt let's start with you uh can you go ahead and give a little bit of your
[218.16 → 225.00] background and just tell us who you are sure uh so I'm currently a student at bring am young university
[225.00 → 229.12] and we'll be graduating here in December actually with a computer science degree
[229.12 → 235.64] um I love I don't know I love getting outside uh hiking in the mountains is great bicycling
[235.64 → 242.16] uh down mountain roads is really fun uh and programming in when I'm not doing homework so i
[242.16 → 248.30] look forward to the day when I don't have to do homework after you know a day of programming um
[248.30 → 253.36] and I actually started caddy during my hardest semester at college here it was just earlier this
[253.36 → 259.48] year uh the winter semester January through April when I was in four really intense programming uh
[259.48 → 265.20] senior level programming classes and I just had to step away from that for a while and
[265.20 → 271.56] work on a side project so it actually brought me a lot of sanity as well so you were slacking
[271.56 → 275.66] so to speak, or you were distracting yourself from all your programming tasks by
[275.66 → 280.28] starting up a web server is that what you're saying uh more or less I mean I did all right in the classes
[280.28 → 288.58] well that's good to hear you know uh most people and when they want to relax they'll watch TV or play
[288.58 → 293.36] video games but uh they're also not here on the changelog so I guess it's paying off for you
[293.36 → 299.82] um very cool so you're it's still in college do you have plans uh post-graduation are you still
[299.82 → 306.56] just feeling things out still feeling things out all right well maybe we'll have to catch back up
[306.56 → 314.90] with you here after a while and see what happened yeah Sebastian yeah um nice to meet you welcome to
[314.90 → 320.80] the changelog why don't you go ahead and introduce yourself to the listeners all right um I'm an
[320.80 → 330.04] uh information technology security student I'm from Austria and I'm going for my bachelor's degree at the
[330.04 → 339.40] moment um I started programming when I was about nine or ten years old and doing that um
[339.40 → 351.36] when I've got nothing other to do and um I got into caddy because I was looking for a cool um open source
[351.36 → 361.08] project to join and started off with a pretty small um pull request for adding something to
[361.08 → 372.40] to a middleware and then um mat tasked if someone wants to do the lets encrypt thing for caddy and i
[372.40 → 380.34] volunteered and well here I am just like that yeah just like that so you were just looking for some
[380.34 → 385.82] open source to contribute to uh what yeah right what sparked that interest that desire to get into open
[385.82 → 396.00] source oh well um I worked as a programmer for about three years and um there is nothing really I could
[396.00 → 403.08] show off to somebody who asked me what have you done with your life so I figured I'd join an open
[403.08 → 411.74] source uh project to have something to show off yeah good reason to do open source right out there
[411.74 → 419.46] in the open people can see your technical chops um mad same question so you know at BYU doing
[419.46 → 425.20] computer science things when were you first exposed to open source software and what got you
[425.20 → 434.68] interested and involved um i think I started doing open source in about 2011 um it's about my
[434.68 → 442.60] sophomore year of college and uh i I don't know I think I just started writing code and putting it up
[442.60 → 449.34] on GitHub and then I realized that coding could be a very social thing to do and I really liked that
[449.34 → 456.02] because i kind of grew up on a farm in Iowa kind of away from people, and it was neat to be able to work
[456.02 → 461.78] with people remotely uh and doing this kind of work, and so I really enjoyed the collaboration aspect
[461.78 → 467.00] once I started putting some code out there and contributing to a few projects in little ways
[467.00 → 476.56] it was just very satisfying caddy notably is a go project I'm curious your interest in go and how
[476.56 → 484.92] that got started I picked up go at my last job um we were looking to swap out our dot net code base
[484.92 → 493.82] with some uh some leaner technologies and go was definitely a good match and so um I was assigned
[493.82 → 499.74] to write a new service in go for our company and uh so that was really fun that's how I started it but
[499.74 → 508.00] i just I love the language it's very productive uh it's very simple elegant um in most ways it's not
[508.00 → 515.48] perfect but um I found that using it in school in my assignments I've um I've had kind of a competitive
[515.48 → 521.62] advantage over other students because I can crank out code um productive code more quickly than my
[521.62 → 526.86] classmates who are using java for example, so your classes are just they just let you pick your own
[526.86 → 532.78] language I think when I was in school you pretty much did what they told you to do yeah in the senior
[532.78 → 540.38] level classes a lot of it is kind of up to you that's awesome yeah Sebastian how about yourself
[540.38 → 550.20] you have been doing go for long well um on and off for a few years but um as the major language to
[550.20 → 559.74] write coding it's about since April this year okay um I followed the go development since its
[559.74 → 568.26] initial release but um I just got really into it this year very cool all right well let's get to
[568.26 → 574.52] the heart of the matter here which is the caddy web server so from the home page it says that caddy is a
[574.52 → 582.88] lightweight general purpose web server for windows mac Linux BSD and android which got my eye it is a
[582.88 → 589.70] capable alternative to other popular and easy to use web servers now Matt I went back on
[589.70 → 594.58] and I saw on your Twitter you have a pinned tweet which was your announcement of caddy back in April
[594.58 → 600.68] and in that tweet it says a capable alternative to nginx or Apache it seems like you've slightly
[600.68 → 607.70] altered your language there yeah I figure it wasn't a good idea um after I didn't actually expect it to
[607.70 → 613.28] to get much attention but I figured once it did I probably shouldn't call out other
[613.28 → 620.66] other products by name that's their actually great attention yeah um so they're actually great
[620.66 → 626.12] um I'm an I'm a nginx fan myself um but I just wanted to make it more generic
[626.12 → 633.14] yeah so I mean I'm also a nginx fan and I've uh I cut my teeth on Apache back in the day cut more
[633.14 → 640.94] than just teeth probably um we all know that we all have been there, and you know very thankful for
[640.94 → 647.02] the Apache project it's uh served many web pages over the years and done so admirably but also an
[647.02 → 654.60] nginx fan and curious you know this seems like an audacious project even more audacious perhaps when
[654.60 → 658.06] you first launched it when you're like I'm here to take on nginx and Apache now you've kind of
[658.06 → 666.42] settled down from that a little bit and uh I'm just wondering you know what what got
[666.42 → 675.46] into you when it's just like I'm going to write a web server um I think the uh you know I make a lot of
[675.46 → 681.56] little websites either for myself or for software projects or for other people or for school and i
[681.56 → 688.08] just needed a quick way to get a production capable web server up and running really quickly
[688.08 → 694.36] and easily and nginx is pretty good um it just makes it can be a little tricky to configure sometimes
[694.36 → 698.86] I don't know if you've ever had those half day projects where you set up your web server
[698.86 → 708.88] and that's like all you do um it can be hard to get it just right um and so I just wanted to
[708.88 → 714.00] to kind of whip up something that I don't know if you've ever tried um setting up like nginx to
[714.00 → 721.54] front a fast CGI application for like a PHP site that's the worst thing yeah indeed yeah nginx is
[721.54 → 727.86] much better as a know more of a pure reverse proxy it seems like the fast CGI stuff I mean there's
[727.86 → 732.86] there's just more hoops to jump through with that particular setup um so whenever you have a
[732.86 → 738.08] situation or I've had a situation where I have perhaps the same server that's serving a rails
[738.08 → 742.38] application and like a WordPress install or something like that for the blog section
[742.38 → 749.72] and yeah the WordPress side with nginx it's gotten better but historically has been a bit of a pain to
[749.72 → 756.82] get set up yeah and so what I noticed is that um a lot of my sites that used for example PHP back in
[756.82 → 763.90] the day when i was a big PHP fan um I used the PHP mostly for simple things that were kind of
[763.90 → 767.84] like minutiae that i kind of wish my web server would just take care of but I just need a little
[767.84 → 773.60] dynamic element but I felt like it was a pretty common use case um and then there were other
[773.60 → 781.10] complications like again googling how to set up fast CGI with nginx and PHP all the tutorials are
[781.10 → 786.68] different it's a bunch of security whoop-Dee-doos that you need to worry about and um I just didn't
[786.68 → 791.46] even want to go there but so I'm like you know I'll just write a web server and go seems like a
[791.46 → 797.10] great language for this I'll just write something that's simple and I can just type in the name of
[797.10 → 801.62] the server and the command line hit enter and bam it just kind of works and another thing that i
[801.62 → 808.54] really wanted I wanted my configuration file my website config to live with my website not with
[808.54 → 815.48] my web server so why do you want you to know because I just like to CD into the directory where
[815.48 → 820.68] the site is and then just run the web server from there, and then it'll just pick out the config file
[820.68 → 825.52] in the present working directory just found that so much more convenient than having to go over to a
[825.52 → 832.54] system folder or a central folder for the web server and then change some config files there and
[832.54 → 838.86] worrying about including and ordering as well yeah so well maybe getting ahead of ourselves a little
[838.86 → 844.82] bit, but caddy does support virtual hosts so in that case you know you have multiple websites under the
[844.82 → 850.54] same host in that situation is it run from an Etsy directory or from some sort of common configuration
[850.54 → 855.78] directory I mean you can specify from the command line where you want to get the
[855.78 → 860.90] configuration file from but by default it just pulls the caddy file from the current directory
[860.90 → 867.12] so it's just very convenient options people love options of course options lead to configurations and
[867.12 → 874.54] yeah always love configurations um let's talk about your audience you mentioned you make a lot of small
[874.54 → 882.12] small you know somewhat static somewhat dynamic sites um who's caddy built for is it built just for Matt
[882.12 → 889.38] Holt or are there other audiences in mind it was built for me um met my needs pretty well and then
[889.38 → 896.40] people started opening issues and I figured well I guess I better get to work, and so I think the caddy is
[896.40 → 906.46] is really well suited for people who don't want to well they're suited it's definitely suited for people who run
[906.46 → 913.82] lightweight small websites, and you can use caddy in production not saying that it's perfect, but you can use it in
[913.82 → 926.26] production um if you have kind of a complex site or a site that runs on some um dynamic um
[926.26 → 932.68] platform like rails or Django or something it might be a little trickier to configure it um
[932.68 → 941.20] but you know we're working on that my main focus right now is static websites and um really bringing
[941.20 → 947.88] the power uh of the go standard library out in making the web server do what you need it to do
[947.88 → 954.30] without having to make a dynamic website if that makes sense so if you can get away with a static website
[954.30 → 960.40] that just has a few dynamic um functions that you need maybe caddy is a good fit for you if you have
[960.40 → 968.26] like this really like dynamic and kind of heavy website going on then you know stick with nginx or
[968.26 → 973.22] if you're serving you know 100 000 requests a second like definitely stick with something very
[973.22 → 978.76] high performing um but caddy's pretty good it's pretty competitive for most things I think
[978.76 → 984.14] you said bringing out the power of the go standard library can you give me a for instance or an
[984.14 → 990.78] example what exactly do you mean by that so uh yeah so nginx uh and Apache for example I'm used
[990.78 → 996.88] to um to server side includes so if I want to make a static site but I don't want to have to keep
[996.88 → 1003.50] repeating the footer on all of these HTML pages um then I just do a little server side include
[1003.50 → 1009.18] and the web server will kind of pull these pages in and serve them statically
[1009.18 → 1015.48] uh caddy can do this too, but it uses go's template library which is actually really powerful
[1015.48 → 1021.46] um, and you can do some really cool stuff, and it just parses the whole HTML file as a template
[1021.46 → 1028.60] and so anything that goes template library you can um lets you do you can do with your HTML file
[1028.60 → 1035.70] without having to make a dynamic site kind of okay so it's its akin to having a static site generator
[1035.70 → 1045.48] kind of built into the web server kind of yeah interesting so it's built for Matt Holt it's
[1045.48 → 1053.88] built for people who have pretty simple sites that are um have a little bit of you know magic going on
[1053.88 → 1059.80] but not too much it also seems like it's built for cross-platform as many things can go take
[1059.80 → 1065.04] advantage of that universal binary or that ability to compile cross-platform yeah that's actually a good
[1065.04 → 1070.52] point um you ever tried setting up a web server like a production web server other than you know
[1070.52 → 1076.56] on Windows other than like IAS um can be a little never tried yeah it can be a little
[1076.56 → 1083.80] weird uh because these web servers are made for Linux basically Unix systems um but yeah caddy
[1083.80 → 1089.90] like first class support for windows kind of thing so if you need to use windows, or you know caddy's
[1089.90 → 1096.02] great too for um we're not just targeting technical people here but like designers and writers who
[1096.02 → 1102.48] just use windows that's the environment they feel comfortable in they can use caddy it's a great fit
[1102.48 → 1106.94] for them, they don't have to learn the technical ins and outs of like a real hardcore web server
[1106.94 → 1112.76] very cool you one thing I mentioned at the top of the show was that it is promotes its android support
[1112.76 → 1119.44] there can you speak to that how that works and what that's all about um yeah so go compiles to android
[1119.44 → 1127.22] and actually recently it's compiles in a way to iOS which is kind of cool but if you download the
[1127.22 → 1136.06] caddy build for arm Linux you can sideload it onto your android device and actually run it there
[1136.06 → 1144.24] and that's kind of fun uh because you can, I don't know if you have a folder with files that you want to
[1144.24 → 1151.36] share with your local area network from your phone you can do that now um it's kind of a it's its kind
[1151.36 → 1157.32] of a cutting edge way to do it like this is not a refined feature, or you know use case yet, but it can
[1157.32 → 1162.32] be done very cool that sounds like a good place for a break when we get back we're going to talk
[1162.32 → 1167.92] about configuration as it seems like that was an area that you focused on quite a bit is getting that
[1167.92 → 1173.58] user experience just right um we'll take a break here from one of our sponsors and on the other side of the
[1174.24 → 1176.18] we'll talk about caddy files we'll be right back
[1176.18 → 1188.88] say hello to top towel designers our friends at top towel have done something really, really awesome
[1188.88 → 1196.12] they've expanded into a new market they're talking designers top dot has been known as a thriving
[1196.12 → 1202.12] network of some of the best software developers and engineers out there many of the developers in
[1202.12 → 1207.70] their network know extremely talented designers, and they've always had this sort of informal
[1207.70 → 1213.40] relationship with designer involvement in top town they've done a little bit you know, but it hasn't
[1213.40 → 1220.06] been an exact um you know product so to speak or internal model, and so they've expanded they've
[1220.06 → 1227.78] evolved today uh they're extremely excited to announce the official launch of top towel designers
[1227.78 → 1232.98] what this means now is the same experience that you've had on both sides of the fence whether you're
[1232.98 → 1237.86] someone that's looking for really awesome designers or you're a really awesome designer
[1237.86 → 1243.60] looking for really awesome opportunities this is the place for you not only if you're engineers but also
[1243.60 → 1248.86] if you're designers out there as well so designers listen up it is time to go check out
[1248.86 → 1257.00] top towel.com slash designers that's t-o-p-t-a-l dot com slash designers and tell them the change law sent you
[1257.00 → 1265.64] all right we are back speaking with Matt Holt and Sebastian air hart about the caddy web server
[1265.64 → 1272.84] and http2 web server, but before we get into the feature set let's talk about configuration that's
[1272.84 → 1281.48] where most people who are dealing with web servers live sometimes die uh you have a caddy file so when i
[1281.48 → 1289.62] first saw this I thought oh no another file uh seems like this uh thing file naming convention
[1289.62 → 1295.84] meme continues to propagate I'm not going to hold against you too much, but we got gem files and proc
[1295.84 → 1303.88] files and now caddy files and there's all these files um just we don't have to we don't have to
[1303.88 → 1308.66] hang out here all day but maybe just speak on where that inspiration came from you liked you like that
[1308.66 → 1315.34] format uh yeah I mean as far as the name caddy file it just seemed to kind of flow off the tongue
[1315.34 → 1324.66] um but the idea for an actual configuration file um is in a way it's actually kind of a stopgap
[1324.66 → 1330.48] um but a configuration file is and I'll get to that in a second but an actual configuration file is
[1330.48 → 1336.70] kind of the standard it's the normal way to configure a web server uh you make a file you put
[1336.70 → 1341.54] some directives in there that tell the web server what to do and then when you run the web server
[1341.54 → 1350.24] it just loads the file and configures itself in memory and off you know on its way um and that
[1350.24 → 1355.48] was just really easy and I just wanted a configuration that I could persist with my website so I have my
[1355.48 → 1360.10] website folder and then I have a caddy file in that folder uh and I can just run caddy from there
[1360.10 → 1367.34] and it'll read the contents of the file consistently every time on any platform and pretty much every
[1367.34 → 1373.66] environment um, and it'll work the same way and this config file though is not actually the
[1373.66 → 1378.90] the end goal here I don't intend for caddy to only be configurable via a file
[1378.90 → 1388.64] do tell us more so uh in the future and there's some you know there's a roadmap here but in the future I do
[1388.64 → 1397.32] intend to write an uh an API so that you can actually dynamically uh set up caddy while it's
[1397.32 → 1403.24] running and change its configuration while it's running without having to rely on just a file in
[1403.24 → 1411.50] the file system oh that'll be awesome so any you're going to give us a launch date Christmas 2015 right
[1411.50 → 1420.40] I wish no i I don't know the date yet I've actually started kind of stubbing out an API on a branch
[1420.40 → 1427.22] and you can try it uh it's a little racy, and it's a little clunky so I think I need to
[1427.22 → 1434.50] redesign some things, but it will happen I definitely want it to I envision a nice web front end for people
[1434.50 → 1439.34] to just open in their browser and be able to configure their server from there with this nice
[1439.34 → 1447.64] gooey and having maybe stats and monitoring built in one day if they want yeah well I wasn't expecting
[1447.64 → 1452.32] an actual date this is just an old hobby of mine which is i asked developers to commit to a
[1452.32 → 1459.28] ship date and I watched them recoil oh that's nice of you oh yeah gotta stay entertained somehow
[1459.28 → 1465.64] uh very cool so let's talk about the caddy file itself uh syntax uh inspiration does it you come
[1465.64 → 1470.22] up with your brand new your own thing is it inspired by something it looks like it's pretty simple you
[1470.22 → 1476.92] have some directives, but they're they're just like bare like keywords like you type in uh I like this one
[1476.92 → 1483.20] browse for instance, and then you give a path and that's like setting up directory indexes um for a
[1483.20 → 1489.26] specific I'm assuming subfolder of your system there um where was the inspiration
[1489.28 → 1496.10] for your syntax of the caddy file um the inspiration was me wanting not to type very much and not having
[1496.10 → 1503.30] to be very like clumsy with my typing so not much punctuation um I didn't want to think about syntax
[1503.30 → 1507.62] really i just kind of wanted it to flow so when I go to set up a web server what's the first thing I am
[1507.62 → 1512.98] thinking of well probably the website address the URL the domain name so type that in that's always
[1512.98 → 1519.02] the top of the caddy file it enters a couple of times and then okay I want to serve clean URLs for HTML files
[1519.02 → 1526.00] so ext and then dot HTML so it'll automatically serve HTML files without needing a dot HTML in the
[1526.00 → 1531.48] URL then let's see I want to be able to share files in my photos' directory because I have this
[1531.48 → 1538.06] album of pictures so then I do browse and then slash photos you don't have to think about curly
[1538.06 → 1543.66] braces and colons and quotation marks typically in the caddy file which is really nice yeah I mean I think a
[1543.66 → 1549.24] recent trend with configuration files as well we'll just type it out in Jason because uh we all love
[1549.24 → 1556.14] that format and um it seems like that is more focused on implementation because it's really easy
[1556.14 → 1561.56] just to suck in a know string of Jason and parse it I'm sure go has a built-in Jason parsing in the
[1561.56 → 1567.32] standard library does um so you had to write your own parser for this or how's it implemented on the go
[1567.32 → 1574.44] yep it's its an it's a home-brewed parser um and I've actually gotten a little bit of flack for
[1574.44 → 1580.26] creating in yet another uh configuration syntax this one's very specific to this use case though
[1580.26 → 1585.64] this is not a general purpose config syntax it meets some needs that Jason doesn't for example using
[1585.64 → 1594.24] arrays as keys um ultimately you have you maybe have a set of server blocks um in a caddy file where
[1594.24 → 1604.14] each server block configures one or more hosts so instead of having to um set up a host as a key
[1604.14 → 1608.54] and then have it point to some configuration because following pointers is kind of confusing
[1608.54 → 1613.56] and then you have to like to teach people about that and I just didn't want to go there so just specify
[1613.56 → 1622.52] multiple hosts the key, and then they all share that same configuration is one example so yes i I know
[1622.52 → 1628.02] that Jason serialization and deserialization is very easy but I wanted to focus on the user here this is
[1628.02 → 1633.52] about the experience I want to make it easy for people to create for the web and make the web better
[1633.52 → 1640.46] that way more accessible I'm all for that so you know another aspect of this you have of the caddy file
[1640.46 → 1648.22] is placeholders I think that's part of the caddy file uh can you explain what placeholders are and
[1648.22 → 1653.70] what they're good for yeah they're just um they're just little strings uh enclosing curly braces this is
[1653.70 → 1660.64] one rare case where you would use a curly brace or punctuation um, but it just fills in a value um
[1660.64 → 1665.92] specific to the request or the response usually so let's say that you're setting up your log
[1665.92 → 1672.38] um directive you can say log, and then you can specify the file name, and you can specify a format
[1672.38 → 1679.26] a custom format if you wish um and that format you would use placeholders because you don't know
[1679.26 → 1684.90] the request time for all the requests you can't hard code the method and the URL, so these are kind
[1684.90 → 1692.98] of like dynamic replaceable values um they give you access to various things like the URL of the
[1692.98 → 1699.08] request and the time of the request or the response body length and stuff like that yeah headers host body
[1699.08 → 1704.12] method so on and so forth pretty much anything that you could pull out of a request you can use it and
[1704.12 → 1710.60] key on that and basically modify your configuration based on that correct yeah kind of like uh kind of
[1710.60 → 1715.36] like a variable in a nginx config no dollar sign whatever but not scriptable I don't want to go
[1715.36 → 1723.86] the scriptable route why not you know as much fun as it is uh it's kind of a can of worms yeah uh it's
[1723.86 → 1727.82] like a rabbit hole well I think it's kind of a fine line because what you have here is you have some
[1727.82 → 1736.02] you have some dynamicism right you have emulating uh for your server site includes you have you're
[1736.02 → 1741.94] like almost in a full-on programming environment right like you're almost there, and then it's like
[1741.94 → 1749.34] where do you draw that line so where do you draw that line um it's a good question drawing the line at
[1749.34 → 1755.26] giving you just enough power to be dangerous but not enough to kind of hang yourself
[1755.26 → 1760.72] not enough where the learning curve is beyond what someone who doesn't know how to program can do
[1760.72 → 1767.16] um not enough to the point where you have to like get super frustrated at things
[1767.16 → 1771.44] so I feel like if you're using it and something's not obvious there's either a bug in the documentation
[1771.44 → 1777.16] or in the implementation and that needs to be fixed so if o'Reilly calls you to write a book
[1777.16 → 1780.22] about it then you probably have taken it too far in this case
[1780.22 → 1786.80] right come write a book about how to program the caddy web server oh yeah at that point you'd be
[1786.80 → 1793.54] like oh man yeah I think I went too far but I got a book deal exactly blog posts are okay but yeah
[1793.54 → 1799.32] you shouldn't have to script caddy I think that's a little far taking a little far I guess uh
[1799.32 → 1803.68] some of the features play into the caddy file of course because you're going to be enabling or
[1803.68 → 1810.00] disabling features um your headline feature of course is h2 support out of the box
[1810.00 → 1818.12] um maybe Sebastian why don't you explain uh h2 support in caddy and how it works and
[1818.12 → 1823.12] and all that stuff for us well uh we use a library
[1823.12 → 1831.38] um so we didn't actually implement it ourselves, but we use a go library for it
[1831.38 → 1837.66] but um it was the beauty of open source right yeah it's open source it's on GitHub I think
[1837.66 → 1843.84] supposed to be the better version of http but not everyone agrees on that me neither
[1843.84 → 1849.68] oh really yeah well now we're getting interesting tell us more why do you know that
[1849.68 → 1855.24] uh-oh Matt dissension you have dissension oh do we really want to go down the rabbit hole
[1855.24 → 1864.72] um i kind of do uh, but it sounds like your kind of don't so let's just uh let me add you can turn
[1864.72 → 1871.22] off http 2 if you want with caddy no, no I don't I don't I don't in principle have a problem with it
[1871.22 → 1877.90] being there just it is could have turned out way better than it has I see so it's just the lack
[1877.90 → 1884.06] it could have been better yeah right not that it's bad just no it's not bad it's just some features
[1884.06 → 1893.60] which got in and some features which didn't um well it could have been better yeah we'll see h2
[1893.60 → 1900.06] should be much easier to improve upon than h1 was yeah of course yeah with time yeah and if
[1900.06 → 1907.50] you are interested in h2 uh the nitty-gritty details of the protocol go back to changelog.com
[1907.50 → 1913.76] slash 161 with ilia grig rich we did a kind of comprehensive overview of all of its features
[1913.76 → 1923.00] pipelining multiplexing um pack all the things that h2 has and um we will not you know talk about
[1923.00 → 1927.54] those today because we talked about them in detail there and as you guys mentioned um the beauty of
[1927.54 → 1933.00] open source is that you're building on top of other people's work and in this case you guys got to
[1933.00 → 1938.58] use I think it was brad Fitz's uh h2 library yeah and that's an awesome thing because now you know so
[1938.58 → 1944.70] many people get the benefit of it who are using caddy without having to know those uh intimate details so
[1944.70 → 1952.40] nothing wrong with that right and actually his uh the brad Fitz h2 library just got moved into the
[1952.40 → 1959.52] uh the go standard library on tip and is enabled by default now um now obviously caddy's not using go tip
[1959.52 → 1966.96] but uh it will come soon enough we'll have full hdp2 support whereas up to this point it's been kind
[1966.96 → 1974.62] of experimental but pretty soon it will be a full like production ready hdp2 library what's go tip is
[1974.62 → 1981.64] that like the master branch of the development or uh yeah basically okay, okay so you have h2 and you
[1981.64 → 1989.06] can turn it off it's on by default of course it's only for clients I assume that support HDPS or TLS
[1989.06 → 1995.74] um you also have some other things ipv6 markdown we can talk about that a little bit web sockets
[1995.74 → 2002.54] virtual hosts as we mentioned before uh server name indicators and extensions why don't you uh pick
[2002.54 → 2008.14] your favourite of those mark or excuse me Matt, and we'll uh I read markdown and then I just pronounced
[2008.14 → 2014.42] your name mark um, and we'll talk about that what's the most exciting thing beyond h2 that's not let's
[2014.42 → 2025.62] um I'm a huge fan of uh SNI server name indication which is a TLS extension and this is pretty standard
[2025.62 → 2032.68] like this is not a mind-blowing feature, but it's so convenient and important because now with the same
[2032.68 → 2041.60] socket you can serve multiple post names um that are over secure channel so that's that's a really
[2041.60 → 2047.32] important um thing in fact caddy's virtual host feature which allows you to set up multiple sites
[2047.32 → 2054.80] in the same caddy file and serve them from the same port uh would not work for HTTPS sites without SNI
[2054.80 → 2061.64] so that's pretty cool, so the big win there is and correct me if I'm wrong is that if you're hosting a
[2061.64 → 2069.74] series of websites perhaps on a digital ocean uh VPS you do not need a new static IP address for each
[2069.74 → 2077.70] of those hosts exactly, and you can secure those channels on even the same exact port um just
[2077.70 → 2084.62] with a single IP address and port combination you can have all these different HTTPS hosts yep exactly
[2084.62 → 2091.48] love that I think that is you know like you said that's not like a unique feature of uh of caddy but
[2091.48 → 2097.96] definitely awesome to see it there it also doesn't have it doesn't work on Windows XP which is finally i
[2097.96 → 2103.40] guess starting to become not too much of an issue I know that was a blocker for some people yeah that's
[2103.40 → 2109.86] pretty old now it is it's still out there unfortunately um I don't mind pushing the envelope
[2109.86 → 2116.36] a little bit I think people need to upgrade uh I absolutely agree I think there's you know your
[2116.36 → 2121.66] mileage may vary there are certain people who are still supporting ie8 and whatnot um and some
[2121.66 → 2129.58] people on XP so in those cases yes unfortunate souls um in those cases they can't use SNI but I think
[2129.58 → 2136.90] especially if you're building a modern web server um for the modern web of course gotta have that I think
[2136.90 → 2142.64] one other a couple other little technical features I want to point out too is that caddy is a multicore
[2142.64 → 2149.76] server and so it's multithreaded in the sense that it will spin up new go routines or lightweight threads
[2149.76 → 2156.00] per request so it's very fast and efficient that way it has a different model than for example nginx
[2156.00 → 2165.10] which is multi-process um but uh caddy can utilize all the cores uh just kind of like nginx can except
[2165.10 → 2170.42] that it doesn't have to rely on the operating system scheduler because the go scheduler actually
[2170.42 → 2175.68] understands go code and can make more intelligent scheduling decisions um which is really cool for
[2175.68 → 2181.52] high performance uh sites and that's all on by default and just kind of works let's talk about
[2181.52 → 2188.18] I was going to say let's talk about extension extensions seems like an interesting one um as you browse the
[2188.18 → 2194.42] docs, and you're looking at the different directives there's a handful of them that are marked as add-ons
[2194.42 → 2203.08] um such as the cms support get IP filtering search and as you click on those it seems like these are using
[2203.08 → 2211.06] your extension feature uh can you speak about that sure um anyone can write an extension for caddy um
[2211.06 → 2215.98] you can choose to publish it on the website like some of these are here or just use it internally
[2215.98 → 2221.76] but basically the idea is we don't want caddy's code base to grow too large and become unwieldy
[2221.76 → 2227.24] and have a lot of cruft that would kind of defeat the lightweight aspect of it which really is a feature
[2227.24 → 2232.92] it's easier to maintain um, so these add-ons is how we decided to deal with this because some
[2232.92 → 2239.34] people including me like for example i I wanted a built-in site search I didn't want to have to
[2239.34 → 2245.84] set up and maintain some other search infrastructure or use an external search service which can get a
[2245.84 → 2251.72] little dicey so what better way to do it than to have it written and go built into the web server
[2251.72 → 2257.42] having complete access to the config as needed that the web server's internal configuration and to be able
[2257.42 → 2262.96] to generate an index of your site and then have it searchable and so these are all built by um
[2262.96 → 2271.60] there's like a yeah there's the git add-on for example uh built by Amboina Ibrahim he uh he built
[2271.60 → 2275.84] this git add-on where you can deploy your site with git push and your web server will automatically pull
[2275.84 → 2284.12] in the new changes super convenient things that aren't um making the code base unmanageable, but you can
[2284.12 → 2289.58] just check them when you download caddy, and it will do a custom build for you, and you can use those
[2289.58 → 2295.16] so how do those get in is there like an ecosystem do they have to come and uh you know send you an
[2295.16 → 2302.12] email and say hey Matt throw me up on your website uh what's the situation there um it's just a pull
[2302.12 → 2306.86] request system just kind of open it's pretty casual you open an issue and say I'm going to work on this
[2306.86 → 2311.38] and then you can do that and there are some docs that kind of show you how to get started and
[2311.38 → 2317.00] little template, and then it's not too bad, and then you just submit a pull request to register
[2317.00 → 2324.12] your add-on in the build server repository and once we merge that in and deploy the new build server
[2324.12 → 2329.12] then there you go then you need to submit some documentation for the website I think the search
[2329.12 → 2334.62] add-on is really rad it's definitely something that comes up all the time with static sites is you
[2334.62 → 2339.30] just want to add a little bit of a search function on there, and you either have to do like the Google
[2339.30 → 2346.06] insight search which is wonky or use a third party I think on my website I use um
[2346.06 → 2350.82] now I'm forgetting their names I'm going to give them a shout-out I don't know a third party
[2350.82 → 2355.24] who provides you know they index your site and provide a search API that you can
[2355.24 → 2361.08] you know query with JavaScript but having that built right in that's pretty handy cool yeah and
[2361.08 → 2365.88] it's a perfect way to give some go library some exposure the search add-on built by
[2365.88 → 2373.08] uh Pedro Nasser lets you uh it uses the Levy library which is written in go and uh yeah so
[2373.08 → 2379.80] it's really, really nice all right anything else as far as the major features we know there's one
[2379.80 → 2383.54] coming down the pipeline well let's touch on Markdown uh it seems like it kind of stands out a little
[2383.54 → 2389.14] bit it's like well you know we support ipv6, and we support markdown it seemed like completely
[2389.14 → 2392.96] different things what was the logic behind supporting markdown it's kind of a first-class citizen
[2392.96 → 2398.88] uh the fact that some people hate touching HTML and just love to write web pages in markdown
[2398.88 → 2403.84] so with this ad or with this it's actually not an add-on it's an it's built into the core you can
[2403.84 → 2411.08] serve markdown files uh, and they'll render as HTML on the fly, or you can pre-generate the HTML
[2411.08 → 2417.48] hmm so is this scratching a specific if you had or was this thinking of more general users
[2417.48 → 2423.20] more general users initially but I find myself using it more and more because you can specify
[2423.20 → 2431.38] a HTML template and still serve really nice authentic HTML pages using just markdown um and
[2431.38 → 2437.76] than of course we have this Hugo add-on with caddy so you can actually Hugo is a static site generator
[2437.76 → 2443.86] written in go it's really popular um and so that kind of does something similar markdown is just kind
[2443.86 → 2449.72] of a more very simplified lightweight version very cool well I think we've hit up against our next
[2449.72 → 2456.82] sponsor break so let's stop here take a break on the other side we will talk about let's encrypt which
[2456.82 → 2464.06] is very exciting to me and uh apparently to you all as a future awesome feature of caddy we'll talk
[2464.06 → 2472.58] about that on the other side of the break image is a real-time image processing proxy in CDN and let me
[2472.58 → 2479.30] tell you this is way more than image magic running on ec2 this is way better it's everything your
[2479.30 → 2487.06] friend and developers have dreamt of output to PNG JPEG if JPEG 2000 and several other formats
[2487.06 → 2492.90] and if you're like me, you've ever argued with your boss or a teammate about serving retina images
[2492.90 → 2499.44] to non-retina devices you'll appreciate their open source dependency free JavaScript library that
[2499.44 → 2506.48] allows you to easily use the image API to make your images responsive to any device now all this
[2506.48 → 2514.00] takes a platform and the image platform is built on three core values flexibility and quality performance
[2514.00 → 2521.60] and affordability when it comes to flexibility and quality image has over 90 URL parameters that you can
[2521.60 → 2527.52] mix and match to provide an unlimited amount of transformations that you need for your images
[2527.52 → 2533.84] and they take quality very seriously and because of their commitment to quality several top 1000
[2533.84 → 2541.44] websites in the world trust them to serve their images now when it comes to performance image operates
[2541.44 → 2546.88] out of data centres filled with top of the line mac pros and mac minis, and they're set up for a
[2546.88 → 2553.76] completely streaming solution this means your images never hit the disk images are served by the best
[2553.76 → 2559.92] SSD based CDM for delivery around the world anywhere extremely fast and while we're talking about
[2559.92 → 2566.96] speed almost all the image processing happens on GPUs this means transformations are superfast when
[2566.96 → 2573.20] compared to competing virtualized environments, and lastly it's all about affordability everyone wants to
[2573.20 → 2580.56] save a buck that's how the world works because image processes close to a billion with a b images per day
[2580.56 → 2587.68] they're able to make certain optimizations at scale and pass those savings on to you to learn more
[2587.68 → 2596.64] about image and what they're all about head to imgix.com slash changelog once again imgix.com
[2597.20 → 2600.32] slash changelog and tell the madam from the changelog sent you
[2602.48 → 2609.44] all right we are back and yes I found out who's providing my site search I think that's the kind
[2609.44 → 2615.76] of thing that you just know but uh they've been just quietly uh serving me for years so I will
[2615.76 → 2621.52] give them a shout-out swift type.com they will index your static site and provide a nice
[2621.52 → 2629.04] easy API for you to add search to your site unless you're so lucky to be using caddy at which point you
[2629.04 → 2634.88] have that built right in there as an add-on so moving on let's talk about something that's coming
[2634.88 → 2642.24] down the pipeline currently being worked on which I'm excited about which is let's encrypt support
[2642.24 → 2647.60] Sebastian can you first start off by telling us what let's encrypt is, and then we'll go into how that
[2647.60 → 2659.12] works into caddy yeah sure so let's encrypt is a new thing where you can get um valid SSL certificates
[2659.12 → 2670.88] for your servers fully automatically um without really going to an um to a ca and um throwing money down
[2670.88 → 2680.80] its throat to get your certificate um they offer um basic SSL certificates so no extended validation or
[2680.80 → 2691.28] something um but for the normal user it's better it's its the best thing that could happen in my
[2691.28 → 2699.52] opinion yeah they're free right yeah they're free SSL certs yep free and valid so you're free and
[2699.52 → 2706.56] valid and uh the green symbol in your browser I'm super excited about it, I think it's been something is
[2706.56 → 2712.80] to eff that's doing this I can't remember who all's involved with its less encrypt.org um but
[2712.80 → 2717.84] it seems like they have had liked it's gonna it's coming its coming its coming, and we're all sitting
[2717.84 → 2724.32] here waiting um to save some money and get all of our all of our sites on http seven the ones that right
[2724.32 → 2728.96] now it's like it's my personal site do I really want to spend you know x dollars a year to encrypt it
[2728.96 → 2736.00] yeah um is it going to come is it going to come or is it just going to keep coming yeah so the last thing
[2736.00 → 2743.28] I've heard is that they went to launch officially uh mid-November okay so it definitely is coming
[2744.88 → 2753.12] that's why we um started to get pressure on for getting uh let's encrypt integrated into caddy
[2753.84 → 2759.04] so let's lets but lets we'll go into how that works but first let's talk about the perfect end
[2759.04 → 2765.84] user experience like when it's totally done and I'm a caddy user yeah tell me how it will work like i just
[2765.84 → 2771.44] flip a switch and I'm encrypted tell me how it'll work yeah you put your site into your uh
[2771.44 → 2780.48] into your caddy file um hit caddy up and there you go you are h you are SSL encrypted without anything
[2782.16 → 2783.60] just shut up and take my money
[2783.60 → 2792.88] that'll be you can't do that well figure out a way oh you got a donate button because that's
[2792.88 → 2799.12] going to be amazing for a lot of people um I think you know SSL, but we talk about the free aspect of it
[2799.12 → 2807.20] and that's part of it um but just the pain and the technical uh drudgery setting up a certificate
[2807.20 → 2813.44] over all these years has been too much of a high bar for many people who otherwise would
[2813.44 → 2818.16] be happy to just flip that switch, so this is going to be awesome um maybe talk about the
[2819.44 → 2824.96] where you've been so far and where you're going with it and give us some of the technical details of
[2824.96 → 2835.60] how this works yeah sure um well I started a few months ago to uh implement it in go because um we
[2835.60 → 2843.60] wanted it in caddy, and we just wanted it to be native in go so um we decided to write a new library
[2843.60 → 2854.08] in go to handle it um because the the the command line utility which comes from the let's encrypt guys
[2854.08 → 2863.52] is in python and uh we can't really interface in a good and meaningful way with python code from go
[2863.52 → 2870.72] so we thought it's a good idea to write our own so have they published an API that you're coding
[2870.72 → 2878.56] against yeah they published an and uh RFC for their so-called acme spec
[2880.64 → 2891.36] acme spec yeah acme automatic certificate management environment oh man yeah it's the RFC
[2891.36 → 2902.64] no, no they are now at draft number four um I think I started at the initial in the initial uh draft
[2903.20 → 2909.12] and there were a few changes over the course of the month first I started integrating it
[2910.48 → 2918.64] riding it quite fast and that stopped a bit after the first two changes because I wanted to uh
[2918.64 → 2926.96] wait a bit until it gets more stable with the API yeah um well basically the API for let's encrypt is
[2926.96 → 2941.60] an is a Jason API um it operates with Jason web keys JFK and JWS Jason web signing the technical details are that
[2941.60 → 2950.88] you as a user create a private key for yourself, and you tie that to an account on the let's encrypt server
[2950.88 → 2958.80] so you register with your email address for instance and that's private key and from there on you can
[2958.80 → 2968.88] request certificates with your private key um of course that's that's pretty insecure so you have of
[2968.88 → 2976.24] course uh you have to somehow prove that the domain you want this certificate for is indeed yours
[2978.64 → 2988.48] and uh that's handled by a few challenges where you have to um fulfill certain tasks given by the server
[2989.20 → 2996.64] in order to uh authenticate the domain that it's really yours is that clear what I'm talking about yeah
[2996.64 → 3004.96] yes, so these are things like uh upload a file or set a header yeah the easiest challenge is
[3004.96 → 3013.28] the so-called simple http challenge so um you tell the server hey I want a certificate for the domain
[3013.28 → 3022.56] example.com yeah um and the server sends you back a token which it expects you to serve at the certain
[3022.56 → 3030.80] URL path on that domain, and it will resolve the p address of your server and look if it's really there
[3030.80 → 3036.56] if it's really there then you pass this challenge and that's it yeah you're done you have to do you have to
[3036.56 → 3048.24] pick one challenge oh well it depends as with many things in it is usually depends if is you can
[3048.24 → 3054.64] fulfill the challenge without any problems then yes this was it um you just have to ask for the
[3054.64 → 3061.20] certificates, and you get the certificates to download but if for some reason this challenge does not
[3062.00 → 3068.48] work out for you there are other challenges to do um, and they are always come they come in pairs
[3069.28 → 3074.80] so the server decides what it wants to see from you, you're not the one deciding what you want to show
[3074.80 → 3082.08] the server so how does the go library and then caddy thereafter know who I am and who my less encrypt
[3082.08 → 3088.56] account is do you have to like to set that in the config or something like that well we can, we generate
[3088.56 → 3097.76] a config for the user so um we have to get somehow the email address for example from the user um we haven't
[3097.76 → 3104.16] exactly worked out how we want to tie this into the user experience um
[3104.80 → 3113.52] but yes we save a configuration file along with uh certain other things we need to interface with
[3113.52 → 3122.24] that's encrypt in a folder uh that's not carry I think or Matt yeah there will be a dot caddy folder in
[3122.24 → 3132.80] the yeah on the file system in this folder there will be other sub folders per uh first uh certificate
[3132.80 → 3143.12] and per user and also per host so you can peek in there and copy stuff around, but actually it's all um
[3143.84 → 3149.20] managed for you that's that's the goal yeah I was working on that this morning that's going to be fun
[3151.28 → 3158.24] yeah you guys uh is it moving along are you stuck tell us how it's going well I think it's going
[3158.24 → 3167.28] along well yeah i I'm not stuck um Sebastian understands the ins and outs of the spec the
[3167.28 → 3175.28] protocol spec pretty well and um I'm just using his library now in caddy on a private branch still it's
[3175.28 → 3182.40] pretty early days but I have been able to successfully generate a new certificate at startup
[3182.40 → 3191.52] um from a local boulder ca boulder is the name of the let's encrypt certificate authority server um
[3192.32 → 3198.64] so in a purely test environment on my local machine I have been able to get a certificate in a
[3198.64 → 3206.40] private key and then a service site using that so definitely making progress the rest of this is going
[3206.40 → 3213.68] to have to focus now on the user experience making sure that it's as unobtrusive as possible
[3214.96 → 3222.80] and managing the certificates and keys and taking care of renewals um when the time is right yeah have
[3222.80 → 3225.52] you guys even thought about renewals yeah I mean obviously you've thought about it because you just
[3225.52 → 3234.32] mentioned it but I hadn't um how's that going to work every um certificate which is issued by uh let's
[3234.32 → 3244.08] encrypt ca gets its unique um URL on the server so you can issue a simple get request which is signed
[3244.88 → 3252.24] by either your private key or the private key which was used to create the site certificate
[3253.44 → 3262.00] and you either get a renewed certificate back from the server or you have to create an entirely new
[3262.00 → 3269.04] certificate so that's the renewal story and as far as the caddy integration of that i
[3269.68 → 3276.08] um I have some ideas still kicking around the details about renewals uh it will be automatic it will be
[3276.08 → 3285.84] transparent to the user um it will involve probably a graceful restart of the server um when renewal happens
[3285.84 → 3292.80] to to to plug in the new certificate, but again we expect it to be fully managed on by default um
[3293.52 → 3300.56] so I think all the pain thanks to let's encrypt and Sebastian's work I think all the pain of dealing
[3300.56 → 3308.08] with SSL certificates will finally be gone yeah I think that's the kind of feature that will
[3308.08 → 3316.56] will set caddy apart um and hopefully other web servers and other software packages will start to
[3316.56 → 3324.80] integrate because it's a huge thing and i actually I misspoke I said is the is it an eff thing um and i
[3324.80 → 3333.28] just want to clarify it's let's encrypt is put on by the internet security research group which is a
[3333.28 → 3338.80] California public benefit corporation, and it's sponsored by the eff and other major sponsors
[3338.80 → 3346.40] like Mozilla Akamai Cisco and a few others automatic of WordPress frame so uh it's a community effort with
[3346.40 → 3355.44] a lot of companies pouring um resources into it and I think it's hopefully arriving quarter four 2050 i
[3355.44 → 3363.12] remember when this said arriving summer 2015 so I'm sure there are a lot of uh moving parts is even
[3363.12 → 3367.04] just integrating for you guys there's a lot of moving parts, but hopefully it all comes together
[3367.04 → 3373.28] and you guys your goal I suppose would be you guys going to be ready to go you know kind of day one uh
[3373.28 → 3379.84] November or what's your integration roadmap look like time-wise well I can speak for the caddy
[3379.84 → 3386.16] integration probably not before their launch date um I want to fair enough we don't expect any major
[3386.16 → 3392.80] changes to their protocol uh as far as the underlying library goes um but regardless of that i
[3392.80 → 3400.96] I want to make sure that the um that the management of the certificates is working well so we'll
[3400.96 → 3407.44] probably um shortly after their launch we'll probably have like a special download that you can do of caddy or
[3407.44 → 3415.12] a special build that has let's encrypt and so a few people can try it um voluntarily without just kind of
[3415.12 → 3420.80] forcing it on everyone all of a sudden um because it might be kind of jarring to some because again
[3420.80 → 3429.60] HTTPS by default there are a lot of um considerations do we redirect the plain text the HTTPS and um
[3430.80 → 3436.24] just making sure everything goes smoothly we're gonna work really hard for that so hopefully shortly
[3436.24 → 3444.00] after they launch so that's definitely a headline feature that is upcoming of course h2 requiring that
[3444.00 → 3452.24] that that that encrypted connection this allows lots of folks um to easily get that optimized
[3452.24 → 3460.80] http connection instead of having to fall back to h1 so let's take our final sponsor break and when we come
[3460.80 → 3466.80] back we will wrap up the conversation talking more about caddy's roadmap future features that you're interested in
[3466.80 → 3473.28] building and are currently building and then finally how people can get started using caddy
[3474.00 → 3477.76] and our closing questions so we'll be right back after this break
[3479.76 → 3484.96] we're excited about our new sponsorship with Linde they're huge fans of the show and are excited to
[3484.96 → 3489.36] support what we're doing here, and they want to invite every single listener of the changelog to try out
[3489.36 → 3497.52] one of the fastest most efficient SSD cloud servers on the market get a Linde cloud server up and running
[3497.52 → 3504.16] in seconds with your choice of Linux distro resources and node location they've got eight data centres
[3504.16 → 3510.32] spread all across the world North America Europe and Asia pacific plans started just ten dollars a
[3510.32 → 3516.80] month with hourly billing and a monthly cap on all plans and add-on services like backups node balancers
[3516.80 → 3524.32] long view and even Linde managed and for those who are already familiar with Linde they recently switched from zen to KVM
[3524.32 → 3531.12] and the latest Unix benchmark showed a plus 300 performance increase we'll drop a link in the show notes for those
[3531.12 → 3538.32] benchmarks for you to check out get forward access for more control run VMS run containers or even a private git server
[3538.32 → 3546.72] enjoy native SSD cloud storage a 40 gigabit network and intel e5 processors use the code changelog
[3546.72 → 3554.72] 10 with unlimited uses tell your friends it doesn't expire this year it expires the end of next year so use it as much as you want
[3554.72 → 3561.52] again that code is changelog 10 head to linode.com slash changelog and tell them the changelog sent you
[3561.52 → 3570.32] all right we're back we've learned a lot about caddy what it's good for what it might not be so good for
[3570.32 → 3578.24] we've learned about let's encrypt and the built-in flip a switch get your site encrypted feature that
[3578.24 → 3585.36] is coming to a caddy near you um Matt what else is coming to caddy down the road um well like i
[3585.36 → 3592.32] referenced earlier i I really wanted to make an API um so that you can just run caddy on a server um
[3592.32 → 3599.84] um bare bones or from scratch without a configuration and then be able to say log into some web-based client
[3599.84 → 3605.20] and manage your server remotely with a nice GUI I think that'd be really nice uh and actually give
[3605.20 → 3611.12] access to web servers to a lot more people who don't understand even you know the command line
[3611.12 → 3618.56] and ssh or whatever um there's a lot of potential there, and it's not a unique feature other web servers
[3618.56 → 3626.16] have similar capabilities but um i uh I think that it's its still necessary
[3628.40 → 3639.12] uh so that's one anything else yeah so I also want to um to really work on well so we talked about
[3639.12 → 3646.40] let's encrypt oh the API and the API is not a user-facing feature directly uh the web-based control panel
[3646.40 → 3652.16] would be something else and I don't know if that's going to be a third-party thing or um or if I'm
[3652.16 → 3657.04] going to build one as well, but we'll see I think we'll see what the demand is and what the audience
[3657.04 → 3665.68] becomes here as time goes on very cool you know maybe one thing we should talk about briefly before
[3665.68 → 3671.04] we get into the getting started because I feel like it's the kind of question that many people will
[3671.04 → 3677.76] say why didn't you talk about performance um I know you mentioned it briefly earlier on but
[3677.76 → 3684.00] let's let's speak specifically to performance I know you have a benchmark out there uh seems like
[3684.00 → 3689.68] you know a pretty basic one, and you know you have a very strong and well-worded disclaimer about
[3689.68 → 3695.76] benchmarks um, but it doesn't seem like performance it seems like there are two things first go
[3695.76 → 3701.12] tends to be very performant especially with its concurrency primitives and then the other thing is
[3701.12 → 3705.28] you didn't seem like performance was one of your goals right it was user experience it was ease of
[3705.28 → 3713.44] use these things modern feature sets um but where does it stand and what can you say about caddy as
[3713.44 → 3720.96] far as its performance abilities um so it looks so right now caddy performs um using a bare
[3720.96 → 3727.36] bones configuration to compared to default configurations of a couple other popular web
[3727.36 → 3737.20] servers performs comp uh com competitively well that's the word okay and um so by that uh it does
[3737.20 → 3742.88] perform in my testing again this is just me as far as requests per second tends to perform better than
[3742.88 → 3752.32] Apache um without again without tuning um and almost as well as nginx but if you're serving 30 000
[3752.32 → 3758.72] requests per second or 50 000 requests per second you maybe performance should be your primary goal and
[3758.72 → 3767.28] maybe you aren't just the typical average Joe user yeah um so that is to be considered I don't want to like
[3767.28 → 3772.80] put performance under the rug and totally forget about it because if I wanted to do that um
[3774.00 → 3778.72] then this would be a much easier project right because just throw any amount of mountain of code into
[3778.72 → 3784.64] this project and make it do all the things that you want it to do right um not going to go there
[3784.64 → 3790.72] definitely performance is going to be um a concern not in a bad way but like it'll be on our minds
[3790.72 → 3797.04] it's going to be it's going to take a front uh front seat I think but not over the user
[3797.04 → 3803.36] experience it'd be a fine balance, and it's gonna we'll have to figure it out as we go
[3804.32 → 3809.12] yeah one thing I might mention is something that I read that you said which is that if there are any
[3809.12 → 3816.80] people who are very interested in performance and are good with those things a would appreciate if
[3816.80 → 3821.60] they brought benchmarks uh do their own testing and publish those results and then b if they have
[3821.60 → 3826.88] specific especially if they have go chops and know of ways of making it faster these are
[3826.88 → 3833.12] things that you're you're wide open to is that fair to say yes that's exactly right cool I thought
[3833.12 → 3838.80] you I thought that was fair because I did read it I didn't make it glad you read it a lot of people
[3838.80 → 3842.64] I always ask about performance they want to know requests per second they want to see the numbers they
[3842.64 → 3849.36] want to see memory allocations, and you know go do your own testing for your own use case um in mine i
[3849.36 → 3854.40] found it to be very like quite sufficient and there are several sites using caddy in production
[3855.12 → 3861.04] uh even under load, and it's its fine go is a pretty competent language for that and that's I mean
[3861.04 → 3864.80] they're sitting on 480 or 443 in production mode right like there's no
[3866.24 → 3873.52] it's exposed to the wide open internet, and it's running in production, so yeah yeah very cool well lets uh
[3873.52 → 3881.20] let's close up with getting started so say I'm sold and I'm uh interested in using caddy for my next
[3881.20 → 3889.12] website to serve it in production maybe with some http2 going on how do I do that I'd say download it for
[3889.12 → 3897.76] your platform um deploy it to your machine and run it you'll need a caddy file so when you download
[3897.76 → 3902.48] caddy you just create a caddy file typically it goes again in the folder where your site is
[3902.48 → 3909.84] um very easy to set up you can read the docs on the web page um about how to do that but once you
[3909.84 → 3915.12] got a caddy file there just run caddy, and it'll just start serving your site so is there sort of
[3915.12 → 3921.76] any sort of demonization or backgrounding um I mean I'm not going there you'll have to do that on your
[3921.76 → 3929.20] own okay uh I admit it's true you'll have to you'll have to do that on your own um and also don't run
[3929.20 → 3935.84] caddy as root I mean you can but probably not a good idea just in case so you can use the set cap
[3936.40 → 3942.88] utility in Linux to uh to give caddy permission to bind to ports lower than 1024 without having to be
[3942.88 → 3949.52] root so I do that in production works pretty well okay that sounds like some opportunities to contribute
[3949.52 → 3956.24] at least maybe not into caddy core, but even a tool around caddy uh some sort of wrapper that would allow
[3956.24 → 3962.00] it to run as a system service or um in the background and manage the demonization of it
[3962.00 → 3966.24] or I mean there are tools out there that do this kind of things in general with binaries so maybe
[3966.24 → 3972.16] even just a tutorial on that would be good for folks yeah I agree there are a couple blog posts about it
[3972.72 → 3977.44] and actually that's a really great opportunity if you're a writer a technical writer um writing about
[3977.44 → 3984.16] ways to use caddy effectively in production is a perfect um post that you could do probably draw
[3984.16 → 3989.28] some traffic to your site I know people are searching for it, I see it in the analytics logs so
[3989.84 → 3992.40] oh there you go analytic log driven development
[3992.96 → 4003.60] that's the new development there yes, yes search your logs and shows people want it yeah that's true
[4004.16 → 4010.08] that's true all right well very cool I'm excited I think this is a very cool young project what's the
[4010.08 → 4016.08] status are you out of 1.0 yet are you getting close no we're working toward it, we want uh i
[4016.08 → 4020.80] honestly want let's encrypt I want the API to be part of it so it's kind of a ambitious goal but
[4020.80 → 4025.76] we'll get there and caddy is a great can I just put a shout-out to the all the contributors
[4025.76 → 4032.08] you do yeah cat caddy is a great project um as far as the community goes it is a young project it
[4032.08 → 4037.92] just uh launched in April this year so it's only a few months old, but we have contributors from all
[4037.92 → 4044.64] over the world um you know Sebastian joining us today is in Austria we have contributors representing
[4044.64 → 4052.32] every continent all sorts of skill sets and backgrounds um and the contributions like it would
[4052.32 → 4058.24] not be what it is today without them there's no way I could do it so huge thank you and feel free to
[4058.24 → 4065.28] get involved there are definitely many opportunities for new go developers but also experienced ones to
[4065.28 → 4070.40] contribute in very meaningful ways without you know without having to commit to doing too much
[4071.36 → 4079.04] if that's a concern very good i i can echo those sentiments just seeing the community around
[4079.04 → 4085.44] you that even promoted you onto the changelog um you know we have a lot of people on our ping repo
[4085.44 → 4088.80] coming out and telling us you should have this show or that show we appreciate all those requests
[4088.80 → 4094.32] and we try to um you know fulfill all the requests that make sense for the show and timing and whatnot
[4095.28 → 4102.24] but rarely do we have such support that you got so quickly um with all the plus ones to get you
[4102.24 → 4107.68] on and I think that's a testament a little bit to the go community and to the people who are genuinely
[4107.68 → 4116.40] excited and involved with caddy so that's if nothing else a very fun thing to be involved in yeah I agree
[4116.40 → 4120.16] all right well let's do our closing questions and Sebastian I'm going to start with you on this one
[4120.16 → 4131.20] right um who is your programming hero and why um well I guess I don't really have one single person
[4131.20 → 4143.04] but uh I really enjoy um reading code from um many different open source repositories and i just really
[4143.04 → 4150.96] like open source code just so it's so vast learning experience, and you can get so much from all the code
[4151.52 → 4161.04] which is available for free out there, so everyone is my hero hey I like it, I like it i
[4161.04 → 4168.48] i I agree with you in the terms of how much you can learn from open source I think one uh area of
[4168.48 → 4175.68] my life where I went really from a novice developer to uh more of an um a medium range I don't know what
[4175.68 → 4181.12] you call the next level up what I really levelled up in development was when i decided to peek
[4181.12 → 4187.04] behind the curtains and read the code of the libraries that I was using and I think GitHub really
[4187.04 → 4192.32] helped with that because you know pre-GitHub days on source forge you could get open source software
[4192.32 → 4197.52] you could use it, but it wasn't obvious how to read the code, and it was very kind of black box
[4198.24 → 4204.64] um once I realized I can just go read all this and I can find out how it's working and I can see why
[4204.64 → 4210.16] it's eroding even though the docs say it shouldn't be uh I really started to learn just you know by
[4210.16 → 4216.96] reading other people's code so I will just echo your sentiment there um Matt let's move to you do
[4216.96 → 4222.80] you have a specific programming hero or is it everybody it's gonna sound like a cop-out but I have to
[4223.36 → 4232.64] I have to echo his answer oh no I know it's terrible i I respect anyone who um faces a challenge in
[4232.64 → 4242.32] coding and learns and strives to overcome it um so and i i I do watch I see when people um have
[4242.32 → 4247.20] overcome challenges, and it's not just with coding but I know there's also like um social stigmas
[4248.08 → 4257.04] in tech um so people who just stand up to being themselves I highly respect those kinds of people
[4257.04 → 4263.60] we're getting an awful lot of meta answers here where it's never like lately it's not been specific
[4263.60 → 4268.48] people but like certain types of people so it's an it's a trend it's a trend I'm spotting here on
[4268.48 → 4275.92] changelog um very cool next question and probably the final one for today is well let's do two more so
[4276.48 → 4283.28] not the final one but what would you be doing if you weren't doing x where x is what you're currently
[4283.28 → 4290.00] doing in open source or for a living so if you weren't doing caddy and uh computer science Matt
[4290.00 → 4292.72] if you had to go completely a different direction what would you be doing instead
[4293.52 → 4301.44] that's a good question i would love to be working with people uh maybe teaching them how
[4301.44 → 4307.92] to code teaching them how to think like a programmer I think is really valuable um or if I wasn't
[4307.92 → 4315.76] doing that I would probably be improving like focus solely on user experience um I think that's
[4315.76 → 4322.64] just really important to me how we interact with computers and the software Sebastian same question
[4322.64 → 4336.24] for you, I'll probably be a law by now be a what an attorney a lawyer oh an attorney okay gotcha I thought
[4336.24 → 4344.00] you said a carny like somebody who goes in a carnival no, no not really i mean it would be kind of
[4344.00 → 4351.76] funny but no it would have been a valid answer I just couldn't tell exactly what you said so okay
[4351.76 → 4360.08] an attorney at law yeah very cool so okay that's a different direction yeah if it were still dealing
[4360.08 → 4366.40] if it were for my mom I'll, I'll do that i see you'd still be dealing with code, but it'd be
[4366.40 → 4374.72] different kinds of code yeah anyway all right now the last question which is a bit of a call to arms
[4374.72 → 4381.84] or um if you had the ear of the open source community which you kind of do here on the show
[4382.40 → 4386.88] and there's people who are excited about caddy they want to get involved they want to not just use it but
[4386.88 → 4392.88] they want to help what is the best ways that we as an open source community can help you guys
[4393.60 → 4401.84] and the caddy web server succeed hmm it's a loaded question in a good way um thank you know
[4401.84 → 4411.20] a good way the uh I think that when we get let's encrypt at least functional at least hobbling along
[4411.20 → 4416.56] integrated uh I think refining that and getting it ready for like a mass release is going to be
[4416.56 → 4423.04] really important contributions to that is gonna hopefully i I want it to change the web a little
[4423.04 → 4429.12] bit I want it I want to make sure that people are serving HTTPS I'm a strong believer in that
[4429.84 → 4437.04] um and I think it's time that we secure our transmissions from surveillance and attackers and um
[4437.04 → 4443.92] um I think there's no better way to do it to reach the average Joe user than to work on this
[4444.48 → 4451.44] so I think if you feel strongly about privacy and encryption then get on board with this help with
[4451.44 → 4458.08] the Lego library that Sebastian's worked on and help with let's encrypt integration and any other open
[4458.08 → 4465.28] issues frankly good answer and I guess worth noting there uh you mentioned Lego in the break we were all
[4465.28 → 4471.36] enjoying Sebastian's library name which is Lego uh that will be in the show notes that's the
[4472.00 → 4478.24] let's encrypt go library that caddy uses as or is going to use as they get it integrated yeah it's
[4478.24 → 4483.84] still a work in progress awesome well Matt and Sebastian thanks so much for joining us today
[4483.84 → 4490.64] this was a lot of fun um you got me excited I like to see advances even in web servers, and it seems
[4490.64 → 4496.80] like caddy has a lot of good ideas in it hopefully it will spawn um other people to get involved and
[4496.80 → 4503.28] to improve on existing web servers and to build caddy into something that do you know put a dent in the
[4503.28 → 4511.60] inner what internet next week we are joined by Mitchell Hashimoto of vagrant fame and hash corp where
[4511.60 → 4516.88] we'll be discussing their latest open source product which you may have heard of recently made a splash
[4516.88 → 4523.76] auto so if you haven't subscribed yet go ahead and subscribe in iTunes or your favourite pod catcher
[4523.76 → 4529.20] so you don't miss out on that show we want to thank our listeners our members who support us thanks
[4529.20 → 4544.88] everybody who uh requested this show and made sure that it became a thing, and we will see you next week
[4546.88 → 4558.62] bye
