[0.00 → 13.34] you are listening to js party the award-winning weekly celebration of JavaScript and the web
[13.34 → 18.76] what up nerds have you heard I have a new project I love you to check out it's called changelog
[18.76 → 26.70] news a first of its kind weekly podcast plus newsletter combo big combo I'll tell you
[26.70 → 31.44] more about it in one of the breaks thanks to our friends at fast for shipping our shows super
[31.44 → 37.30] fast all around the world check them out at fastly.com and to our partners at fly deploy your
[37.30 → 45.90] app servers and database close to your users no ops required check them out at fly.io okay hey it's
[45.90 → 46.62] party time you all
[56.70 → 69.88] hello world it's your internet friend it's me jarred and I am here with my friend Chris what's up Chris
[69.88 → 77.42] what's up how you're doing happy to see you once again I'm doing all right how are you doing I'm just
[77.42 → 85.66] great sarcasm detected for Ross is also here what's up frost how's it going jarred it's always
[85.66 → 92.04] good to have you on the pod, and we are joined by a special guest Bradley arias friends call him
[92.04 → 98.46] bubbles enemies call him bubbles maybe even Bradley works with ferocity socket Bradley welcome to js party
[98.46 → 104.50] hey good to be here happy to have you as well we're here to talk about some of your recent work
[104.50 → 111.24] on accomplishing the impossible which is taking NPM and making it not dangerous making it safe
[111.24 → 118.84] you guys recently announced this CLI tool from socket safe NPM or NPM safe depending on your
[118.84 → 124.46] affectation or just socket NPM if you will, and we're here to talk about we want to learn about
[124.46 → 128.98] how it works why you built it how you built it maybe dive into some of the details hopefully
[128.98 → 133.66] we can learn a little bit more along the way about how NPM works the command line
[133.66 → 140.62] how NP works why they're dangerous and so on so maybe we start off with that NPM install
[140.62 → 148.02] something we've all typed hundreds of times most likely maybe even every day yeah it turns out
[148.02 → 155.70] and by the way spoiler alert NPM uninstall also fraught with danger which I learned as reading your
[155.70 → 159.26] guy's announcement I didn't realize it could install things it's supposed to uninstall things anyway
[159.26 → 165.32] we'll save that for later let's start with NPM install why it's problematic and what you all have
[165.32 → 174.38] been doing to fix that take it away brad sure so I was trying to figure out a little bit how to satisfy
[174.38 → 184.12] some customer stuff at socket we were seeing questions about how developer machines could be protected
[184.12 → 192.52] most of our product at socket uh was done through GitHub analysis you've done plenty of shows where people have
[192.52 → 201.16] kind of GitHub CI workflows and things like that, but people were asking what do we do when we have an installation
[201.16 → 210.12] script or security problem on a developer machine this was a real world incident as well it happens every so often
[210.12 → 218.20] every few years I think developer machines have a fairly big incident from NPM and the question came up
[218.20 → 226.92] well why are things running on your machine and generally that's going to be when you run NPM install
[226.92 → 235.00] it might run install scripts, or it might install malware directly onto your machine both are possible
[235.00 → 243.40] and so we had to spend time trying to understand all the ways people are using NPM on a daily basis
[244.36 → 253.32] and so we had to basically write something that would let a developer transparently still type NPM install
[253.96 → 261.32] on their machine they wouldn't need to update any code, but it would add protections so we wrote a wrapper
[261.32 → 270.44] script around NPM in a way that would allow it to be used transparently while we injected essentially some
[270.44 → 280.20] stopping points where we could do some checks, and so we actually will check for risk and things to let
[280.20 → 287.56] people make that decision when it occurs it'll show the person the risk in your terminal after you type NPM
[287.56 → 295.88] install it'll be like oh this has a CVE this is a typo squat this has installed scripts, and it just gives
[295.88 → 305.56] developers a way to pause and understand what they're about to do is risky and even let them cancel everything
[305.56 → 313.72] okay so to make sure I'm tracking here, so socket has all these threat detection tools that you all have built
[313.72 → 320.28] and it does static analysis it does other things looking for typo squats and has this corpus of
[320.28 → 327.56] knowledge about NPM packages and their level of safety or danger or just what it thinks about them
[327.56 → 332.20] and there's like a ranking all that kind of stuff and that's all well and good for people who run it
[332.92 → 337.80] against their GitHub repos because if there's a problem inside your repo when you've pushed it to GitHub
[338.76 → 342.60] then socket's going to help you in that way right for us yeah it'll show up on the pull request as a
[342.60 → 346.76] GitHub check right but there's this other threat vector which is the actual developers machine
[347.32 → 354.60] themselves, and you can also be attacked on your machine not on your GitHub repo and so now when
[354.60 → 361.80] I'm running the NPM whatever I'm letting somebody else's code execute on my machine and that can cause
[361.80 → 366.20] all sorts of other problems such as well they can just run arbitrary code on my machine once they can
[366.20 → 372.44] do that of course they've hacked me locally, but then they can also take that power and leak my
[372.44 → 378.60] information or get you know production credentials off my machine etc to hack servers and so this
[379.24 → 384.36] tool is still using that same corpus of knowledge that you guys have built with socket, and it's
[384.36 → 391.08] extending where it works so now it works as a wrapper for NPM am I is that all right correct am I for
[391.08 → 396.60] us am I understanding everything yeah that's exactly correct so it transparently wraps the NPM command and
[396.60 → 402.68] and you can continue then using NPM in the same way that you normally do and if there are no risks we
[402.68 → 407.48] won't we won't interrupt the installation process it'll work just like it normally does but in that
[407.48 → 412.12] you know small percentage of cases where there's something you want to know about it'll it'll um
[412.12 → 419.08] give you a speed bump and ask you if you're really sure and I suppose this is like configurable, and so I can
[419.08 → 426.76] say no I actually don't care about this stupid CVE yeah actually so CV it's funny you mentioned caves
[426.76 → 431.88] because we don't even we don't actually warn about caves by default just because it's that's the typical
[431.88 → 438.44] reaction of the developer community so caves are not the focus of socket right now even though we do
[438.44 → 445.32] like have all that same information that you get from NPM audit or GitHub's advisory database
[445.32 → 451.56] yeah unfortunately the typical reaction of developers to seeing you know CVE information is like ah yeah
[451.56 → 459.32] I already know I got like hundreds of those so yeah you've seen plenty of NPM audit reports, but they do
[459.32 → 467.88] check caves, but they always just tell you already ran the code that has the problem so that's their
[467.88 → 474.52] normal behaviour so we're trying to move the like knowledge forward yeah before you install the
[474.52 → 479.56] dangerous thing not telling you already did something dangerous and to add to that too like
[479.56 → 483.80] we're looking for stuff that doesn't you know isn't even covered by caves because when you have a supply
[483.80 → 490.04] chain attack it's not in a CVE it's usually it's you know some packages compromised and nobody knows it
[490.04 → 496.28] yet and so you know anyone who's unlucky enough to install it you know for that period when it's when
[496.28 → 503.80] it's full of malware is going to have a sad really sad day uh and so you know that's that's why we want to
[503.80 → 510.12] step in and let people know what's in those packages before they install them and so on of the
[510.12 → 518.04] things that it will do then is if there's a new life cycle script like a post and self script it will
[518.04 → 527.56] tell you right, so this is a little interesting so if you use install scripts we treat all install scripts as
[528.36 → 535.24] effectively equivalent because you can run arbitrary code so if you can run arbitrary code a pre-installation
[535.24 → 541.00] versus post install if they change from pre-install to also having a post install we will not give you
[541.00 → 547.96] a new alert because you're already running arbitrary code when you run it, so there are a bunch of things that
[547.96 → 555.56] you might initially think are great to warn developers about, but it makes the tool completely unusable every time
[555.56 → 562.36] you add that speed bump so you see this in other tools as well like they will add a speed bump every
[562.36 → 569.96] single time you install something that has said an installation script, and you know it has an installation script
[570.60 → 578.12] some of the most popular packages on NPM have installed scripts, but after you've already run the risky
[578.12 → 584.92] thing you're effectively already hosed if you didn't agree with it before so we're only gonna
[585.80 → 593.72] alert you if something has changed and for particularly install scripts if they add an installation script and they
[593.72 → 600.44] didn't have any before that's something to be worried about, but there's not really a change in risk
[601.00 → 606.44] actually if you just change from pre-install to post-install or something like that
[606.44 → 613.00] right yeah that was too lengthy yes you answered my question but I asked it I asked it
[613.00 → 619.56] incorrectly I think, so okay ask it the right way this time well no, no he answered it it was uh
[620.44 → 627.64] you know does it alert if is somebody like adds a new script where they never happened before that's
[627.64 → 634.52] right that's you know that's what I meant yeah, but there's a real like we spent actually way more
[634.52 → 642.84] time than I loved on trying to get the developer actually able to use this tool every day and so it's
[642.84 → 650.44] really like detailed in how you have to approach meeting the developer where they're at like that's the key
[650.44 → 657.16] thing I think for this rollout that we've had we've had this feedback period and developers have shown us
[657.16 → 663.88] problems with us over alerting or under alerting and everybody wants different things which is
[663.88 → 669.00] interesting to see, and you've got to find that default middle ground when you say everybody wants
[669.64 → 676.44] different things you're meaning like their appetite for being interrupted or being talked to is
[676.44 → 681.96] dramatically different or varying so that some developers are like leave me alone unless this is an
[681.96 → 686.12] absolute emergency and other people are like actually I really appreciate being interrupted
[686.12 → 691.56] every time an installation script changes or every time and is that what you're saying like people just
[691.56 → 698.76] care about different things yeah so they care about different categories of issues is one some people
[698.76 → 706.12] aren't so concerned with things like licensing or stuff like that others really want everything they want
[706.12 → 715.16] any even the most minute of issues just the installation script has changed like one string in it, they want to
[715.16 → 722.36] stop what they're doing until their security team can audit it which is vastly different I think than
[722.36 → 730.84] most developers who need to be able to you know install a React component or something and get their day-to-day work done
[730.84 → 738.36] yeah Chris what's your appetite in this way I'm kind of a leave me alone kind of person um yeah I mean I've just been
[738.36 → 747.24] been it's just been way too noisy jaded yeah so yeah I'm just jaded and just like all of this is baloney I don't really care about any of it and
[748.44 → 754.04] I mean yeah i yeah I'm not the right person to ask
[755.88 → 762.92] part of the problem with most of the security tooling in my opinion is that by focusing on these
[762.92 → 770.60] vulnerabilities these are all theoretically going to affect you right, but they're not actually you know
[770.60 → 776.92] all affecting you in a real way they're all like potential ways that your app could get attacked or
[776.92 → 783.96] get compromised and the problem with the there are a lot of problems with the CVE system but the fundamental
[783.96 → 790.44] problem is they're all theoretical like problems in your app and not to mention like the severities are
[790.44 → 796.36] all really inflated on the reports, so everything is basically critical or high because in the if
[796.36 → 802.52] you use it in the exact correct way it could be really, really bad right, but it's probably not used that
[802.52 → 807.16] way the vast majority of these are just not going to affect you so I don't want to I don't want to
[807.16 → 813.80] downplay like I mean obviously there are very significant caves that can be a big deal for you but just if
[813.80 → 819.80] you just look at the kind of hundreds of warnings that you get on NPM audit right like how many of those are
[819.80 → 824.12] actually affecting you are going to lead to your application getting compromised it's like you
[824.12 → 830.52] know it's very small percentage of those and so that's the key like original sin or whatever of a
[830.52 → 839.16] lot of the security tooling which is why we've focused almost entirely on supply chain attacks and malware and
[839.16 → 845.88] stuff that basically if you have one of those in your in one of your dependencies you will not be upset that
[845.88 → 850.36] we told you about it, you will not see it as like an interruption or right like or like you know
[850.36 → 856.20] why is this tool annoying me like that's the stuff we're looking for so it's pretty different I think
[856.20 → 865.40] build what people need not what they want right so yeah, and it's interesting to hear you say that because
[865.40 → 873.80] what you want will drastically change once you get it um so one thing that this tool does that most other
[873.80 → 881.32] tools aren't doing this socket NPM is it actually compares what's on disk already most tools that you
[881.32 → 888.12] use they want big numbers they want to scare the people they want to like to be like yeah we're providing
[888.12 → 895.16] value by blocking your developers and that's not really what needs to happen we're not trying to scare
[895.16 → 902.68] people we're trying to let them just like oh you fat-fingered the name of a package you're going to
[902.68 → 908.76] install I did this last week, and it stopped me it was like that's a typo, but there was a package on
[908.76 → 917.24] NPM with that that did things, and it stopped it that I'm appreciative for but once you have like oh i
[917.24 → 925.16] want all the warnings in the world you really start to understand that all these security researchers
[925.88 → 932.28] are given value by over inflating everything every single possible way you can do prototype
[932.28 → 940.52] pollution is critical that's probably not true why aren't you using this like uh fuzzing library and
[940.52 → 947.24] you're testing or stuff like that and those don't actually affect that many people they do affect some
[947.24 → 954.04] but for your day-to-day developer there's actually much lower hanging fruit that malware authors are going
[954.04 → 960.84] to write towards there's no reason for them to go to those extremes normally yeah I mean when I was
[960.84 → 967.08] when like NPM audit first came out and sneak and all that I was like oh cool like look at all
[967.08 → 972.76] this stuff, but you know I wanted to see all the things that were wrong and I wanted to fix them
[972.76 → 979.32] but that got old really quick oh yeah so but yeah I'm which is why you're jaded which is why I'm jaded
[979.32 → 983.16] and I'm with you and this is one of the things I told you for us from the very beginning I think when
[983.16 → 988.52] you came on the changelog and talked about socket is like you need to be very careful with your false
[988.52 → 995.96] positives because you only have our attention our interest our patience for so long as a tool
[996.52 → 1002.84] until we just completely write you off and low context security tools that don't understand that
[1002.84 → 1008.60] that vulnerability is only run as a transitive dependency for webpack which only operates during
[1008.60 → 1014.84] builds of this thing and never runs in production at all like how many times I have to tell a tool
[1014.84 → 1020.20] that eventually I'm just completely done with that tool i just it doesn't it's just noise in my life
[1020.20 → 1025.24] and so it's a challenge I think where you guys sit because we have years and years and years of these
[1025.24 → 1031.08] types of tools meaning security tools that have been providing not much value because they've had
[1031.08 → 1038.44] very little context into what I'm actually doing and your opportunity with socket is like you can
[1038.44 → 1043.88] not be that, but then you also have to have that value moment that brad just described when it saves
[1043.88 → 1048.44] you from a typo squat when it saves you from this thing and like those happen very infrequently
[1049.32 → 1053.00] and which is great like we you know you're not you don't want to be vulnerable all the time you
[1053.00 → 1057.88] don't want to be constantly being attacked but when you do you finally have that aha moment, and you're like
[1057.88 → 1065.40] okay I get it, but it doesn't happen all that often the developers who are asking you to give me all
[1065.40 → 1070.84] the warnings and all the license things and all this and all that they're going to get sick of it maybe but
[1070.84 → 1080.52] uh there are companies that truly are like heavily security auditing sure everything they've run I mean
[1080.52 → 1085.96] then i I mean I don't you know I don't know about who you're like targeting for you know your customer
[1085.96 → 1092.60] base or anything so but yeah maybe you focus on those people maybe you have a one for somebody
[1092.60 → 1098.44] else that is normal all right or strike a balance I think the balance is like we want to have we want
[1098.44 → 1104.76] to be we want to like focus on the stuff that's most significant out of the box and keep the alert
[1104.76 → 1111.56] level really, really low so that every developer can just install this and have it as like a security
[1111.56 → 1118.60] blanket you know like a like kind of like how once you start using ES lint to catch I don't know you
[1118.60 → 1124.28] guys use ES lint to catch like bugs not just the style stuff but like the actual kind of bug catching
[1124.28 → 1128.52] features of it once you have that or even type script is a better example these days like
[1128.52 → 1134.12] you sort of feel unsafe when you're like programming without it because you're like oh well this would
[1134.12 → 1139.96] have caught this type of this class of bug that i now I'm not like getting protected from so it but it you
[1139.96 → 1144.12] don't want it to get in the way so that's kind of the way we want it to work out of the box and then
[1144.12 → 1149.16] if is some team is like really paranoid and says you know what like we want to be warned about every
[1149.16 → 1155.00] time a package you know reads a file uses the FS module to read a file on my disk like just tell
[1155.00 → 1159.40] it to warn me about that we can let them configure it that way if they want to, but that's not going to be
[1159.40 → 1166.52] how it works by default ever oh that would make me cry for most situations if people don't understand how
[1166.52 → 1180.68] many times people are writing the files
[1184.68 → 1192.52] what's up party people jarred here hey I made a thing it's called changelog news a podcast and newsletter
[1192.52 → 1196.68] a lot of people are writing the other combo I ship out on Mondays the podcast episodes are 10 minutes
[1196.68 → 1202.84] or less entertaining I hope and always on point the companion email includes the five big stories
[1202.84 → 1209.64] covered in audio plus a slew of other interesting links with commentary for me, I put a lot of love
[1209.64 → 1215.00] into this project and people really seem to enjoy it you can listen to changelog news by subscribing to
[1215.00 → 1221.72] the changelog podcast to get in on newsletter just head to changelog.com slash news and pop in your email
[1221.72 → 1227.72] address it's free it's easy, and it's pretty stinking good if you ask me, but you don't have to take my
[1227.72 → 1234.92] word for it just ask one of the 20 000 is readers who've already subscribed once again that's changelog.com
[1234.92 → 1243.40] slash news I'll put the link in your show notes and chapter data okay let's get back to it so when you
[1243.40 → 1250.68] set out brad to write this wrapper program surely there was I mean we can tell how much thought you put
[1250.68 → 1255.88] into even just the way that it operates but actually getting it to do what it does how do you build
[1255.88 → 1261.08] something like that I assume this is a binary that you install, and then you run it, and then it calls
[1261.08 → 1267.48] NPM or shells out or something and kind of you know it wraps it's a wrapper library we know that much
[1268.20 → 1273.24] how do you build such a thing so it actually went through around three iterations and three different
[1273.24 → 1283.00] attempts to do this the first attempt was okay we will match NPM's interface we'll make our own CLI it'll
[1283.00 → 1290.52] have the same commands that's a lot of maintenance especially if NPM updates, so this thing needs to work
[1290.52 → 1297.80] with multiple versions of NPM it needs to work on old NPM's it needs to work on new NPM's so that was
[1297.80 → 1307.24] scrapped pretty quickly the next kind of attempt we did was okay what if we just invoke the NPM CLI
[1307.24 → 1314.12] it has a dry run mode built by default maybe we could invoke it twice once in dry run mode once
[1314.12 → 1320.84] without dry run mode, so this actually doesn't provide enough information for you to have a good
[1320.84 → 1327.32] user experience it won't tell you exactly what's being installed it'll tell you the number it actually
[1327.32 → 1334.04] has all the data you just can't get it out of the CLI for what it's about to do or would do in a dry
[1334.04 → 1343.72] run mode so after that we reached once again a level deeper, and we actually wrote a wrapper script that
[1343.72 → 1354.60] will still invoke NPM, but it rips out a piece of NPM and replaces it with our like dry run wrapper that
[1354.60 → 1362.76] will run in a dry run mode before it does any sort of real behaviour that writes to disk this was actually
[1362.76 → 1370.60] fairly pleasant to write compared to some other ecosystems or package managers we looked at a few
[1370.60 → 1378.60] plugin systems on other package managers NPM actually was in a unique infrastructure position here where they use a
[1378.60 → 1386.04] library called arborist, and we only really needed to replace arborist it looked like so we just had to
[1386.04 → 1393.56] swap out arborist which is what it does if you set your log level really high you'll see this little thing
[1393.56 → 1401.16] logged called build ideal tree that is where NPM does a full resolution of the entire module graph before
[1401.16 → 1408.20] it does any sort of removal of packages or installation of new packages and that is the only thing we
[1408.20 → 1415.32] really needed to replace with our first iteration of this and so node happily uses common JS here
[1415.88 → 1424.36] this would be very hard if NPM was written in ES modules why is that so mocking ES modules I spent a lot of
[1424.36 → 1432.04] time I was on tc39 I helped write the loader spec for node there's a variety of reasons we actually have
[1432.04 → 1442.68] a spawn sync call at the front of our wrapper to invoke an ES only ES module only package to do something
[1443.40 → 1449.72] it has like timing issues it's very hard to mock and has some memory leaks let's go with it's very lucky
[1449.72 → 1457.64] that NPM is still writing common JS and so basically you load the entry point and then you monkey
[1457.64 → 1464.68] patch and then that's it we actually monkey patch before the entry point occurs and that's where the
[1464.68 → 1471.72] timing is problematic for ES modules right right yeah, so there's no way for them to really
[1471.72 → 1479.48] stop us well yeah I mean that's how like the module level mocking tools work anyway and CJS you don't
[1479.48 → 1486.36] you're careful not to load the thing, and then you configure it and then you tell it to load
[1486.36 → 1493.96] and it swaps it out right so the full dry run move was that your second iteration or that's still
[1493.96 → 1500.84] happening now like with your released version oh, so this is it's a little bit mixed now in our third
[1500.84 → 1508.44] iteration the second one was we tried a full dry run we would just invoke the NPM CLI using hyphen dry
[1508.44 → 1516.28] run this is kind of the recommended way to do it by NPM configuration currently, but it just tells you
[1516.28 → 1522.44] it added x number of packages and removed x number of packages that's the only information you can get
[1522.44 → 1528.28] out of the CLI I see you don't know what was removed or what was added which can get really confusing
[1528.28 → 1536.84] because what's removed and added can actually be the same package name, so arborist is what we're using now
[1536.84 → 1545.24] in the third iteration not the CLI, and we do a dry run with arborist, and it gives you a full list of
[1545.24 → 1553.08] where things are going to be installed what used to be there so if you're updating say you are patching a
[1553.08 → 1560.12] CVE or something if you're updating you can see the previous version and the new version, and so we do this
[1560.12 → 1567.40] dry run and then after we get all the package version information of what's new what's old we actually
[1567.40 → 1575.96] synchronize that up to our API and then throw away actually the dry run we don't use it again NPM has
[1575.96 → 1584.84] some global state going on a lot of NPM's code base is not really built to be hooked into, and so we have
[1584.84 → 1590.20] to throw away that tree even though it did a bunch of work and do an effectively fresh install and make
[1590.20 → 1596.36] sure it's only going to install what it said it would in the dry run did you ever consider trying
[1596.36 → 1602.44] to do something like swapping out FS and then having like a virtual file system or anything like that
[1603.08 → 1608.44] I've thought about it but having done that in the past no let's go with no
[1608.44 → 1618.84] fair enough there be dragons or what yeah so I have a like 2014 conference talk about writing an
[1618.84 → 1627.88] archive loader for node similar to what electron does with ASA files virtual file systems are
[1627.88 → 1634.60] very hard to write in a way where you won't get into edge cases it's much easier for us to
[1634.60 → 1640.84] intercept and take over a whole library because we're not changing how they're writing to disk we
[1640.84 → 1648.04] just don't want them to touch the disk at all so anything they do to disk would get really complicated
[1648.04 → 1654.12] really fast we'd have to understand how their cache system works because they synchronize tarballs down
[1654.84 → 1659.88] we'd have to prevent them from even downloading the tarball anyway because we don't want to download
[1659.88 → 1670.44] malware at all so now we're intercepting FS calls too also with HTTPS calls so yeah it gets super
[1670.44 → 1678.52] complicated, so the dry run doesn't grab the tarball at all no it only needs the metadata information to do
[1678.52 → 1686.12] version resolution what is it called the pack of fast pack you mint pack you
[1686.12 → 1694.60] oh my goodness who called it that and why I need to speak to the manager so is there a perceived or
[1694.60 → 1702.60] even maybe not tangible but still there performance hit with running this wrapper because it seems like
[1702.60 → 1708.92] you're doing some dancing before I actually get my commands called there's some there is a cache going
[1708.92 → 1717.88] on a NPM so it's not as big as doing the two different runs of a CLI but I'd say the most common
[1717.88 → 1726.04] thing I see is we encounter some really wild versions or packages we haven't crawled at socket yet
[1726.84 → 1734.36] and it has to pause if it encounters like a package we've never seen before waiting on the API to do a full
[1734.36 → 1741.24] like transitive crawl checking all the dependencies of it is doesn't take very long, but you might see
[1741.24 → 1747.64] like a spinner as it counts down the number of like transitive dependencies it's trying to analyze
[1748.28 → 1756.36] I was doing it this morning on one of ours, and it was like 2500 packages on a clean installation to be analyzed
[1756.92 → 1762.76] and so you just see this number just going down as fast as you can, but it's its visible the performance
[1762.76 → 1769.32] loss when you do that I want to say though that one of the benefits of the like the approach we took
[1769.32 → 1775.96] at socket is that the analysis isn't happening locally on your machine so when we do an analysis
[1775.96 → 1784.60] of a package it's done on our servers and that way we can cache the results for everybody so when you
[1784.60 → 1789.88] request you know a result when the CLI requests these results from the server most of them are cached but
[1789.88 → 1796.12] like Bradley said we're not doing it for we're not pre-analyzing every single package on NPM yet
[1796.12 → 1803.16] just because that would be incredibly expensive we've done kind of a pre-analysis on every latest
[1803.16 → 1810.52] version of every package over I think over 500 weekly downloads so that's almost everything that you would
[1810.52 → 1817.40] install by typing NPM install but if you do have some like a random old version of a package in your
[1817.40 → 1822.68] in your lock file it might be the first time we're seeing it so we'll analyze it and then save the
[1822.68 → 1827.48] results, and then it'll be fast after that for everybody else and including you to that's how
[1827.48 → 1833.16] we designed it that's also necessary so that we don't have to download malware tarballs onto your
[1833.16 → 1839.16] local machine we have to do it remotely makes sense so as an end user though I have two APIs I'm
[1839.16 → 1845.32] basically reliant upon being readily available and fast I have to have sockets API and then I have to have
[1845.32 → 1851.00] NPM as well and so potentially I have two points of failure for my stuff getting installed Chris go
[1851.00 → 1857.24] ahead oh I was just going to ask is this like an open source project or what it is open source we're
[1857.24 → 1863.80] not trying to make it generic, yet we have some designs on making things generic we actually had to do
[1863.80 → 1875.08] a major UX tweak in the last week so in particular around how people are using NP or NPM exec I don't
[1875.08 → 1882.52] know if you're using those in your installation scripts, but a bunch of people are apparently so even if it's
[1882.52 → 1889.16] open source it's a little unstable while we figure out all the interesting use cases in the open source
[1889.16 → 1896.60] ecosystem we use that, so there's like a life cycle script to do a clean reinstallation of everything right
[1897.24 → 1906.12] and um we want to birth some stuff, and so I don't have node modules so I use NP birth right
[1906.68 → 1914.44] yeah so we'll still intercept that we've always intercepted that but by default there is no ability
[1914.44 → 1922.68] from NPM to prompt and tell you're about to install something so NP will blindly install it
[1924.04 → 1930.68] normally it'll prompt you oh do you want to install birth but if it doesn't have a terminal
[1930.68 → 1938.12] to prompt you over standard in it'll just blindly install regardless that sounds like a security
[1938.12 → 1944.28] impossible problematic we used to error on it but this week we pushed an update we have it on
[1944.28 → 1951.08] our blog post we had to like to put down an inner process communication server and synchronize
[1951.64 → 1959.32] terminals this isn't too uncommon in things like VS Code do it, but it was just something that we
[1959.32 → 1965.24] weren't expecting to do we thought an error would be enough but too many people are using NP and install
[1965.24 → 1972.84] scripts even so yeah wait what did you do oh there are a lot of there are a lot of people who install things
[1972.84 → 1978.84] in their pre and post install scripts wait what is this oh no, no no sorry you said something about IPC
[1978.84 → 1987.00] and something I'm like what oh that part yeah so basically the problem is
[1987.88 → 1996.68] NPM normally will use a pipe and not standard Io when it spawns child processes for pre and post install
[1996.68 → 2005.00] scripts so you can't actually be like please tell me if you're okay with all these risks you're about to do
[2005.00 → 2012.60] right NPM would just log it to a file basically if you wanted you can change that behaviour using hyphen
[2012.60 → 2022.68] foreground scripts, and then it won't use a pipe it'll inherit standard Io to the child processes but if you do that it has a lot of weird effects
[2022.68 → 2030.52] like it suddenly can't do install scripts in parallel you get a lot of garbage printed to your console
[2030.52 → 2036.92] because people are putting debug things in their pre and post install scripts or uh asking for donations
[2036.92 → 2045.88] yeah there's a lot of that it's a lot of install scripts doing that so we had to put essentially a server
[2045.88 → 2055.72] down on disk which gets connected to by finding an environment variable, and it basically says hey I need to capture standard Io
[2056.28 → 2065.88] and it tells that to the root process doing the original impium install and so once it captures it then it can
[2065.88 → 2075.32] talk over standard Io through the root process wow that's a pain in the butt it's not too uncommon in a gooey world but I think
[2076.20 → 2084.76] it would be nice if more tools allowed this and the whole reason NP has that security concern is that it
[2084.76 → 2089.32] doesn't want to do this handshake
[2089.32 → 2107.40] do you find yourself itching to grow at work, but you're not getting the support you need from your
[2107.40 → 2112.04] manager, or maybe you're at a career transition and trying to figure out what you want and how to get it
[2112.04 → 2116.92] or you've got a great job but could use an external perspective on some tricky cross-functional
[2116.92 → 2122.20] relationships hi this is ball from js party and these are the exact types of problems I'm helping
[2122.20 → 2126.68] folks with in my new business I think about it as pair programming for non-technical problems
[2126.68 → 2131.64] if you're curious you can learn more and sign up for a free exploratory session at ball.LLC
[2131.64 → 2132.52] slash coaching
[2143.56 → 2148.20] let's take it back to the basics for a moment for those of us who are just thinking about well maybe
[2148.20 → 2154.68] I would use this right but maybe I'm just a person who uses NPM from the command line and NP I don't
[2154.68 → 2159.80] know very much about them and I'm thinking like how would I eat what's a wrapper program how would I
[2160.68 → 2168.44] what would I do in order to make my NPM safe like in regard to this program just give us like the ABCs of
[2168.44 → 2175.96] using it let's see the first thing you do is install our command line so it'd be like NPM install
[2176.52 → 2184.28] at socket security slash CLI dash g because your gang well if you want it to be global
[2184.28 → 2189.08] yeah well that's what that means I always thought it was the gangsta flag I always drop basically yeah
[2190.04 → 2197.80] and from there make sure that the socket command is in your path if it's dash g that'll be true
[2198.44 → 2206.84] and then you can, we made sure it works with command aliasing so you just if you're in Unix do alias
[2207.96 → 2221.64] NPM equals socket space NPM and then alias NP equals socket space NP and then do everything normally
[2221.64 → 2227.88] you don't have to update your code base or anything no API key or anything like that uh not for the defaults
[2227.88 → 2235.48] no so if you want other things like org settings then you're going to need an API key it's just too
[2235.48 → 2240.92] easy for us, it's just too easy yeah we like to make things easy we like to know that developers don't
[2240.92 → 2246.76] want to butts with stuff when it comes to this so just got to make it easy got to make it really
[2246.76 → 2252.36] straightforward what if I already have an alias in there that says NPM equals yarn then is this
[2252.36 → 2255.56] is it going to chain its just going to work magically I'm pretty sure it's not going to work
[2255.56 → 2261.56] with yarn is it no we looked at yarn's plug-in system, and it didn't have quite the right information
[2261.56 → 2268.60] that we wanted ppm just put up a PR yesterday to add the hooks we need, I have to double-check them
[2268.60 → 2275.24] today but are people using yarn still do you guys know the numbers on yarn I mean which one
[2275.24 → 2282.44] which number which yarn how many yarns are there uh so I counted six different integrations we'd have
[2282.44 → 2288.92] to do to support just if you say the word yarn we'd have to write like six different things but
[2288.92 → 2295.32] officially there are three versions that everyone uses right kind of like I'd say five there's five
[2295.96 → 2302.28] five officially because you have PNP mode which i I would actually separate out is it worth all that
[2302.28 → 2306.68] effort for us, I mean you're the businessman you guys gonna this is worth it for the business
[2306.68 → 2313.48] it's one of the most updated feature requests or most upvoted yeah yeah people really like yarn
[2313.48 → 2319.48] in especially in big companies like a lot of customers are using yarn I think we haven't committed
[2319.48 → 2325.16] to doing it yet but I mean if enough people keep asking us for it like Bradley said it's its like one
[2325.16 → 2330.28] of our top upvoted requests which is by the way it's always fun when you know you work super hard on
[2330.28 → 2335.24] a feature like this safe NPM, and then you put it out there and the first thing you get is can you
[2335.24 → 2339.56] make it work in yarn can you make it work in ppm can you make it work here, and it's like you know i
[2339.56 → 2344.76] mean obviously we'll do it eventually but yeah it's people always ask for the know the next thing
[2345.64 → 2352.12] we also have other languages and some of the other languages will be fairly easy once we get all the
[2352.12 → 2358.60] user experience story ironed out with this just one integration but python package management is a
[2358.60 → 2364.52] whole nother story I was going to make a joke about python go ahead let's hear it just like you know
[2364.52 → 2371.08] 500 integrations, and you know right people like to make fun of JavaScript for you know being crazy and
[2371.08 → 2375.56] yeah it's really eye-opening to look at the other ecosystems and realize actually we have it pretty
[2375.56 → 2382.20] good in JavaScript you know we have our package uh dependency you know format is a Jason file you know
[2382.20 → 2387.08] it's its easy to parse if it's really straightforward everyone else or not everyone else but a lot of other
[2387.08 → 2394.84] ecosystems have basically these arbitrary files where you can run anything in there, and it's just
[2394.84 → 2400.04] a convention that they follow a certain format, but theoretically you know you could have you know
[2400.04 → 2406.44] code doing anything in there like looping and if statements and http requests in the file that
[2406.44 → 2413.16] declares the dependencies right so that's craziness that's yeah we have it pretty good in JavaScript land
[2413.16 → 2422.60] I think well speaking of craziness riddle me this guys why would NPM uninstall ever install packages
[2423.56 → 2429.88] yeah this was a surprise this is what got me the best can I answer oh Chris knows why I want to try
[2429.88 → 2437.08] I want to try okay go ahead because you can add an uninstallation or post uninstall or pre-uninstall
[2437.08 → 2442.92] lifecycle script that does literally anything right that's one, but that's not the surprising
[2442.92 → 2450.20] one okay what's the surprising one so sometimes you have two dependencies that depend upon a third
[2450.20 → 2458.12] dependency so we're going to say a and b are two dependencies they all depend on c but a wants
[2458.12 → 2470.04] the 1.1.x so you're stuck on 1.1 but b wants anything greater than 1.0 so that means b can install
[2470.04 → 2481.72] 1.2 but not while an is installed so if you remove a NPM I said earlier builds the ideal tree the like
[2481.72 → 2488.12] perfect version of the world, and then it sees oh I could actually install a newer version of c
[2488.76 → 2498.28] because an is gone and so removing an updates and installs a new version of c which can then install
[2498.28 → 2503.80] you know more dependencies that never existed before or whatever I wonder if this is why if
[2503.80 → 2510.60] you went and you, and you did a NPM link, and then you go, and you run NPM install or uninstall on
[2510.60 → 2515.08] something else it kills all your sim links, and you have to do it all over again but I have a question
[2515.08 → 2521.16] Bradley like didn't we didn't NPM used to in the old days just you know install in that
[2521.16 → 2527.32] situation wouldn't it just install two versions of c and give a one it wants and give b the best
[2527.32 → 2534.04] one that it wants too so you'd have two copies of c oh now we're getting into package manager fights
[2534.04 → 2543.88] yes it originally did that and then people saw yarn and yarn deduped like this does so NPM adopted that
[2543.88 → 2553.56] behaviour, and now we're seeing NPM responding to ppm's kind of global shared cache as well, and it added
[2553.56 → 2561.08] that like two months ago or something and so it's an ever-evolving thing and so the only way to keep
[2561.08 → 2569.40] up to date is to get these hooks in some way, and we declare like this is the data we need, and we write
[2569.40 → 2577.08] them to each integration it's unfortunate that NPM was never really built to be extended maybe but
[2577.88 → 2585.48] even with these plug-in systems on other package managers we're having to go and change the hooks so
[2586.28 → 2593.16] it's hard to know what hooks you actually need until you write an actual thing to use them and a lot of
[2593.16 → 2599.32] the times people are using the hooks for things, and they aren't respecting what users have already
[2599.32 → 2604.68] installed on disk that's a big thing we've been talking to a couple of package managers about
[2604.68 → 2611.16] this, and they were surprised that we want to know what's already on disk so that's not usually in the
[2611.16 → 2618.60] plug-in system, so this affects your version of NPM because it can't simply say you're uninstalling so
[2618.60 → 2625.88] you should not ever install anything because that's actually a legitimate NPM feature you know whether
[2625.88 → 2631.24] it's misguided or not it's a real feature of the package manager and so now you have to be able to
[2631.24 → 2637.72] I guess what watch what it's doing at uninstall and making sure that it doesn't install things it
[2637.72 → 2644.60] shouldn't be but can install things it should be or do you just pond how do you deal with that yeah so
[2645.32 → 2654.60] NPM was probably the easiest to do even without a plug-in system this so arborist their library for
[2654.60 → 2661.56] basically doing all the version resolution and building your ideal tree will show you any
[2662.36 → 2667.32] operation it's about to do anything it's going to remove anything it's going to add and anything
[2667.32 → 2675.40] it's going to update and so instead of checking for this is an installation or uninstall command being run
[2675.40 → 2684.92] we always just completely take over arborist and whenever arborist generates an installation or a
[2685.56 → 2691.88] update that kind of stuff that is what we're checking against we have no consideration for the commands
[2691.88 → 2701.48] there are so many ways to install stuff using npm CI NPM install NPM update NPM uninstall
[2701.48 → 2710.36] yeah so help me understand if I understand this correctly when you install socket NPM
[2711.40 → 2717.56] are you taking your custom arborist are you monkey patching the existing NPM on my system are you
[2717.56 → 2724.68] shipping a custom NPM alongside it that I'm now using instead which one of those two is true so arborist
[2724.68 → 2731.64] hasn't changed in years luckily so we're actually monkey patching we're not doing it on disk we're
[2731.64 → 2737.72] not modifying it so you can still use your normal NPM okay, but we are monkey patching it if you go
[2737.72 → 2746.76] through the wrapper and this gets a little more complicated we actually ship a shim that will alias
[2746.76 → 2755.32] the NPM and NP commands there's like a little bin folder inside ours, but we don't actually ship
[2755.96 → 2764.92] vendored versions of NPM these little shims we put them on your path variable, so there are some cases
[2764.92 → 2770.68] where tools are trying to muck with your path, and we check that our NPM is still on the path
[2770.68 → 2781.08] and if you call into this shim it will monkey patch NPM right before it runs in memory it doesn't mess
[2781.08 → 2786.52] with your NPM at all you can have them both running next to each other and if you don't do
[2786.52 → 2791.72] the alias trick that we talked about then you can just decide if you want to run NPM install or socket
[2791.72 → 2796.20] NPM install you can have them both when we call it a wrapper though you're actually wrapping
[2796.20 → 2803.56] a different version of NPM than the one that's on my disk, or you're taking no you are you're shimming
[2803.56 → 2809.56] the one on my disk and changing it at runtime to operate a little differently okay we are using the
[2809.56 → 2817.16] one on your machine so it works I think on anything that's not end of life did you have to do anything
[2817.16 → 2823.48] specific in regard to windows you know NPM is famously having great windows support one of the reasons
[2823.48 → 2828.52] why I think it took off as an as an ecosystem was that windows developers could do lots of node
[2828.52 → 2833.00] things was there anything that you guys had to do for windows support or was it just kind of baked into
[2833.00 → 2840.60] the cake we actually had to disable windows support because we found some bugs so NPM when you run
[2840.60 → 2850.20] commands on Windows and particularly the standard way you interact with cmd.exe it creates wrapper files
[2850.20 → 2860.44] these dot bat files which use some like more complicated than I enjoy shell scripting in order to just invoke
[2860.44 → 2870.84] the proper command so we actually looked at how we could support windows, and we cannot programmatically
[2871.56 → 2879.56] safely that's the key word invoke those shell scripts to see what they're actually about to run so
[2880.20 → 2887.24] it's not supported for now unfortunately, but we haven't had any requests to add support for it either
[2887.72 → 2893.96] but to be clear we support Windows subsystem for Linux so that's what most people are most people are using
[2894.76 → 2902.28] WSL right so it'll work fine on that I think that's why we haven't had any requests yet
[2902.28 → 2908.52] does it work if you bundle NPM with your app
[2911.32 → 2920.12] so if is I have is I got a library or an app and I've added NPM as a dependency because I want control
[2920.12 → 2928.36] over what because my thing wants to run NPM I want control over what version of NPM I'm running and so
[2928.36 → 2935.24] how you do that you depend on a version of NPM right is safe IBM gonna hop in there is that
[2935.24 → 2945.00] going to be like I don't know about that as long as the NPM in question is in the path as NPM it should
[2945.00 → 2954.12] intercept it I mean it'll be in node modules NPM yeah, but it has to be in the path like you'd have to
[2954.12 → 2959.64] basically change your script to run socket NPM instead of your in your local NPM I think not
[2959.64 → 2967.72] normally if you like we're running it by requiring it from node modules it's not going to patch that
[2968.36 → 2973.80] but if you run it from the command line it should in all normal cases we actually go out of our way
[2973.80 → 2980.60] to like try to make sure your path looks correct today's extreme edge case brought to you by Chris
[2980.60 → 2986.68] Hitler Chris is this something you're doing I've considered if it's on the table it's on the table
[2987.48 → 2994.28] if it isn't working let us know because that one should be working I mean it's that NPM is not going
[2994.28 → 3001.16] to be in the path so it shouldn't work right if you use any sort of NPM run it will be in your path
[3002.44 → 3009.32] nope anyway so don't worry about it don't worry about it, I'm not going to give it a try Chris and let
[3009.32 → 3018.36] them know I mean it's just you know also know that NPM's bin directory is now considered deprecated
[3018.36 → 3026.44] so don't rely on that all right guys are there any other interesting implementation details dragons that
[3026.44 → 3031.24] you uncovered and slayed I don't know slew them in order to accomplish this is there
[3031.24 → 3038.84] or what you're anything else left on the table that we have to pick up and chew on uh there's
[3038.84 → 3045.96] certainly stuff still left on the table for us to do we got a bunch of specific requests on like edge
[3045.96 → 3052.92] cases particularly around installations from git repositories we saw some interesting oddities there
[3052.92 → 3061.48] like you can't ignore scripts from git dependencies even if you use like NPM's configuration to ignore
[3061.48 → 3069.32] scripts like it'll run them anyway and stuff like that so we could do better there some people want
[3069.32 → 3076.44] a bunch more configuration options all right for us any uh anything else that we haven't asked about this
[3076.44 → 3083.32] cool new tool no i just I mean i I'm I'm just glad we got it out it's been an uh one of the things i
[3083.32 → 3089.32] wanted to I wanted us to build since the beginning of socket because it always felt like a gap and you
[3089.32 → 3094.68] know we're trying to stop malware but we were stopping it in your pull requests and not right on your
[3094.68 → 3099.80] local machine so it's been um it's been like just one of those things we wanted to do but we never really
[3099.80 → 3105.32] have the time to just like to sit down and do it and now that we did it's its like its great yeah
[3105.32 → 3112.84] people really seem to like it and I wish we did it sooner but um better late than never so yeah awesome
[3112.84 → 3119.24] Chris are you going to give this a try you're going to use this tool are you too jaded what's your no i
[3119.24 → 3125.56] mean I'll give it a shot yeah all right I want like a like a VS Code plugin and I want it I want
[3125.56 → 3131.48] it when I open my package Jason file I want it to show squiggles and stuff oh the stuff that's bad
[3131.48 → 3137.08] from socket okay let's get on that so feature requests coming at you guys I don't know just go
[3137.08 → 3142.92] to the marketplace and install it oh it's already there it exists yeah awesome those are the best kind
[3142.92 → 3149.72] of feature requests you know I love it, and they already exist yeah squiggles Bradley also wrote our VS Code
[3149.72 → 3157.56] extension, so okay submit your bug reports to Bradley on that one as well keep them off Ross's desk i
[3157.56 → 3164.76] really want like usability improvements more than bug reports like because people are running these all
[3164.76 → 3171.96] day every day so all right we'll submit your usability improvements to Bradley not to cross was yeah I mean
[3171.96 → 3178.20] what I was told if you want to if you want to uh if anyone is interested in rolling this out as a
[3178.20 → 3186.12] default NPM wrapper for their whole company uh please get in touch i we're talking to a few
[3186.12 → 3193.48] people a few customers that want to do this uh so we'd love to understand the use case more, but we've
[3193.48 → 3200.68] gotten interest from people who just said we just want to your know on our default developer image on
[3200.68 → 3207.64] all new you know all new laptops just like you know give everybody the wrapper so that their NPM
[3208.20 → 3213.16] you know gets the gets that protection I know smaller companies don't usually do that type
[3213.16 → 3218.76] of stuff but larger companies do have lots of you know software running on the developer
[3218.76 → 3224.28] machine usually for security stuff so right if anyone's interested in that like please reach out
[3224.28 → 3231.16] to us and uh we'd love to learn more about how you'd want to do that and help support it very cool
[3231.16 → 3237.16] guys well thanks for coming on the show Bradley uh Chris and for Ross it's always a pleasure of course
[3237.16 → 3243.64] all the links to all the things that we referenced on today's show will be in your show notes that's
[3243.64 → 3245.80] js party for this week, and we'll catch you on the next one
[3252.52 → 3260.20] changelog plus members stick around we have a fun after show bonus more on yarn analyzing nose
[3260.20 → 3267.08] response to Dino and a spicy take by brad about bun versus Dino ah you know what I'm going to let
[3267.08 → 3272.28] everyone listen to this one if you aren't a plus member find one near you, and thank them for
[3272.28 → 3277.88] sharing the love or do the entire changelog community a solid and sign up today as a thanks
[3277.88 → 3282.84] for your support we make the ads disappear include regular bonuses like the one you're about to hear
[3282.84 → 3289.64] and more check it out at changelog.com slash plus shout out to our partners we have quickly
[3289.64 → 3296.36] serving static assets fly on dynamic requests break master cylinder on beats and you making
[3296.36 → 3302.92] everything we do worthwhile we appreciate you listening each and every week next up on the pod
[3302.92 → 3308.52] front end feud reigning champ Adam argyle is back not to feud though there's more where that came from
[3308.52 → 3314.44] this time he's talking with nick and Amelia about all the new hotness in CSS colours he even has a
[3314.44 → 3319.88] new gradient tool to announce for the first time right here on JS party stay tuned for that we'll have
[3319.88 → 3337.24] it readies for you next week I'm a yarn user so sorry guys not that I really have a preference to yarn it
[3337.24 → 3343.08] was like when it first came out it was so much faster that we just switched over to it and I think
[3343.08 → 3348.52] NPM is probably just about as fast now because they like did a bunch of work after that and now it just
[3348.52 → 3353.08] bugs me that I have to use yarn because I have I use NPM on, so many like small things and then on our
[3353.08 → 3359.56] main project I have to remember how to use yarn and then I'm like what's it yarn i instead of this or
[3359.56 → 3365.00] yarn add, and you switch back easily or is it too integrated at this point now I could switch back
[3365.00 → 3373.08] just like inertia based it's a huge amount of effort to make this work with yarn yeah I would
[3373.08 → 3379.40] almost just like wait it out you know maybe eventually will all of us yarn people will be
[3379.40 → 3387.24] dead or moved on I don't know because there's also bun now too which we talked to them all sorts of people
[3387.24 → 3394.52] and um what's the other one uh you know yeah also Dino which is all I guess they do package Jason now
[3395.08 → 3401.24] yeah Dino's a whole nother ball of wax I think yarn got so much help from um they got really
[3402.12 → 3408.84] the adoption really started when NPM was kind of, and it's it was like a little bad period where yeah
[3408.84 → 3414.44] much was happening, and it was this perfect competition that showed up that was like well why is
[3414.44 → 3421.88] NPM not deterministic and why is it slow and let's fix all this and yeah that competition made
[3421.88 → 3427.24] them up their game and now a lot of the benefit like workspaces and all that stuff was really
[3427.24 → 3432.52] good and then now right a lot of those reasons have gone away but yeah I don't know I'm not really
[3432.52 → 3437.88] a yarn user so I don't know what other reasons people would use it for as well but right well I'll tell
[3437.88 → 3442.04] you I told you what mine was it was just straight up I was in that malaise where it was like why is this
[3442.04 → 3447.72] taking so long and I was like oh another tool that does the same thing but faster easy switch over
[3447.72 → 3451.88] I was just like let's do this and then I just stayed there I wonder if like is that going to be
[3451.88 → 3457.40] the Dino story you know is it going to be like Dino came in and made node do a bunch of stuff and now
[3457.40 → 3463.64] they stepped up to the plate node got better and Dino kind of just like stayed fringe or not I don't
[3463.64 → 3469.72] know I don't think node has done anything in response to Dino no I mean they've done a bunch they
[3469.72 → 3477.88] have the HTTPS imports, but it's flagged due to like nightmare level security problems of just that
[3477.88 → 3486.68] security model we have the permissions model gets unflagged this month for all those like
[3486.68 → 3494.84] they have web APIs like the file API lobs and stuff um that's I mean I don't know they got a lot now
[3494.84 → 3500.92] the test runner but i think that's the problem of being the differentiating features we
[3500.92 → 3507.80] do this but more you're just telling the original people to ship more you're not you're not really
[3507.80 → 3514.04] bringing something new to the table brand new but if they were staying yeah maybe they that's
[3514.04 → 3519.32] just that just means they need to go faster and add more stuff and just be ahead right well they've
[3519.32 → 3526.44] had to carve backward they just added package Jason that's right they did I asked Ryan that when he's
[3526.44 → 3532.84] on the show about you know I feel like what you could come out and say is like with Dino you can
[3532.84 → 3538.92] build this type of application that you can't build with node like it's actually having something that's new
[3538.92 → 3543.24] and different that's like actually you're going to need a Dino thing to get that done does it have
[3543.24 → 3548.04] anything like that, and it was more like no it's like he's like you can build anything in the
[3548.04 → 3552.60] world you want with node it's just like this is me doing node the right way or what I think is a
[3552.60 → 3558.44] better way and so it's like better node it's not like by the way there's a brand-new class of apps
[3558.44 → 3564.12] like that's the kind of stuff that's I think more disruptive right versus like just more or just
[3564.12 → 3570.44] different or just better in certain minuscule ways that can be easily caught up to by effort I don't know
[3571.00 → 3574.60] yeah I mean isn't that the story of all of JavaScript right it's like you know like people have
[3574.60 → 3579.08] always said well if we could just do it over and do it the right way wouldn't everything be better
[3579.08 → 3584.12] like why are we using this bad language, or you know there's always that that like argument and then
[3584.12 → 3588.84] it's always never really panned out for those people not saying that's exactly the argument
[3588.84 → 3595.48] he was making, but it sounds a little like it, I mean like no one really cares about the warts in
[3595.48 → 3602.04] the language that much to like to switch everything over to something new if that's the only benefit is
[3602.04 → 3609.40] that oh you know it's like nicer in some aesthetic way that's not really going to make a difference for
[3609.40 → 3618.28] people enough it needs to be like 10x better to like right get over that that inertia that's a mic drop
[3618.28 → 3626.36] moment yeah honestly I think bun's gonna just be the biggest problem for Dino because it's going to steal
[3626.36 → 3633.88] some of their inertia their intention so Dino requires you to have a Greenfield project
[3633.88 → 3640.76] to really excel it requires you to write something that doesn't have as many tutorials
[3641.72 → 3649.00] it also requires you to have this security system that you always have to disable in production for the
[3649.00 → 3655.48] most part it's just a very strange thing and then bun came along and was like okay we're going to take
[3656.12 → 3665.56] the typescript integration idea we're going to take the not node modules install thing to speed it up
[3665.56 → 3675.48] and we're just going to strap that onto node and that is a much more compelling thing than having to rewrite
[3675.48 → 3683.48] any sort of software well I mean taking a cue from typescript playbook right like the fact that it's
[3683.48 → 3687.64] a superset, and it's just adoptable in this way you don't have to rewrite anything like you're literally
[3687.64 → 3693.40] already using it one of the reasons why people were like oh okay I can just change this to dot TS or not
[3693.40 → 3700.68] even have to do that and try this out that's a huge advantage for any sort of adoption is like well be a
[3700.68 → 3707.56] superset or be the same or be API compatible it's much harder to start brand new I mean, but you get
[3707.56 → 3712.52] more radical ideas that way I guess you know assuming that your ideas are radical in the first place
[3712.52 → 3718.52] changelog plus it's better
