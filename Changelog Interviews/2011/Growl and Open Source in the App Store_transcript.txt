[0.00 --> 18.34]  Welcome to the ChangeLog episode 0.6.8.
[18.60 --> 19.62]  I'm Adam Stachowiak.
[19.78 --> 20.60]  And I'm Wend Netherland.
[20.74 --> 21.76]  This is the ChangeLog.
[21.80 --> 23.52]  We cover what's fresh and new and open source.
[24.04 --> 26.64]  If you found us on iTunes, we're also on the web at thechangelog.com.
[26.74 --> 27.68]  We're also up on GitHub.
[27.68 --> 27.78]  What's up?
[28.12 --> 29.84]  Head to GitHub.com slash explore.
[29.96 --> 34.30]  You'll find some trending repos, some feature repos from our blog, as well as the audio podcast.
[34.60 --> 37.02]  And if you're on Twitter, follow ChangeLogShow.
[37.80 --> 38.78]  And me, Adam Stach.
[39.06 --> 41.32]  And I'm Penguin, P-E-N-G-W-I-N-N.
[41.86 --> 42.96]  Fun episode this week.
[43.02 --> 45.44]  Talk to Chris Forsyth over at Growl.
[45.52 --> 49.10]  And he's also with, formerly at ADM, but also with Perian.
[49.62 --> 50.28]  This guy's busy.
[50.36 --> 51.96]  He's doing so much open source stuff.
[52.24 --> 52.54]  I know.
[52.54 --> 56.46]  And Growl's one of those projects that a lot of people use and don't even know they have it.
[56.46 --> 59.00]  It comes bundled with a lot of apps.
[59.20 --> 62.64]  And it's just that little notification window that you get on the Mac.
[62.76 --> 67.68]  But they're working to make some cross-platform features of Growl.
[67.70 --> 74.12]  And it's fun to see an app that's open source that we've used for years now make it into the App Store and start paying back some of the developers behind it.
[74.40 --> 74.54]  Yeah.
[74.58 --> 76.26]  When you say years, you mean eight years.
[76.44 --> 77.08]  Eight years.
[77.14 --> 77.76]  Can you believe it?
[77.96 --> 78.56]  That's crazy.
[78.56 --> 81.38]  So it's been quiet around the changelog.
[81.48 --> 81.92]  We're fun.
[82.10 --> 83.42]  Glad to be back on the air.
[83.48 --> 84.46]  It's fun to be back on the air.
[84.92 --> 87.42]  We're lifting the curtain on a beta refresh.
[87.64 --> 89.22]  Some of you guys have seen this.
[89.48 --> 92.38]  If you haven't, then keep an eye out on the changelog.com.
[92.44 --> 94.88]  We're moving off of Tumblr over to Nesta CMS.
[95.12 --> 97.36]  And can't wait to show off what we've been working on.
[97.90 --> 100.46]  We've also been working on another site called the SAS Way.
[100.46 --> 108.34]  So if you go to thesasway.com for all of you people who don't like CSS but love SAS, we can teach a few things there.
[108.94 --> 109.30]  Absolutely.
[109.56 --> 116.94]  And these sites are powered by Nesta CMS, which we're going to have Graham on the show soon to talk about our favorite little Ruby-based CMS.
[117.42 --> 117.82]  Absolutely.
[118.34 --> 119.08]  One episode this week.
[119.14 --> 119.66]  Should we get to it?
[119.96 --> 120.58]  Let's do it.
[120.58 --> 132.02]  We're chatting today with Chris Forsyth from the Growl Project.
[132.24 --> 136.46]  So, Chris, for those that may not know, what is Growl and what is your role over there?
[137.00 --> 139.72]  Growl is a notification system for OS X.
[139.72 --> 148.72]  It allows you to get notifications from things like email or your FTP client or whatever the case may be.
[148.72 --> 154.94]  And just find out what's going on in your Mac without having to switch between different applications all at once.
[156.18 --> 157.28]  And I'm Chris Forsyth.
[157.36 --> 159.62]  I've worked on the Growl Project for eight years.
[159.80 --> 162.50]  I'm the project lead, and I thought up the Growl Project.
[163.50 --> 165.30]  You know, and that makes us sound old for eight years.
[165.30 --> 169.90]  But I think my first contact with Growl was probably through the ADM project.
[170.10 --> 171.38]  So you're involved in that as well?
[171.70 --> 172.10]  I was.
[172.14 --> 175.82]  I was the project manager for ADM for about four years.
[176.08 --> 178.38]  I actually stepped down a few years ago.
[178.72 --> 186.68]  But I was responsible for just getting resources together and making sure everyone had what they needed.
[187.28 --> 193.58]  And I helped get the release out to 1.0 and went from there.
[193.92 --> 198.56]  So, yeah, ADM was a stepping stone, put it that way.
[198.56 --> 198.60]  Yeah.
[199.48 --> 204.52]  I think the big milestone that we wanted to cover with this episode is Growl is now in the App Store.
[204.60 --> 205.34]  Tell us about that.
[205.70 --> 205.84]  Yeah.
[205.92 --> 209.94]  So Growl has been a preference pane for years.
[209.94 --> 214.78]  It's up until this version that's in the App Store and has been in the App Store since Monday.
[216.40 --> 218.56]  It's been a system preference pane.
[218.56 --> 225.40]  And we wanted to change that up a little bit because a lot of people were getting confused about where's Growl at and all that sort of thing.
[225.88 --> 234.56]  Also, Apple is requiring in November, starting November, that applications that get submitted to the App Store get sandboxed.
[235.26 --> 242.04]  It's a technical term that basically means that you cannot access things in the system without asking for access.
[242.04 --> 244.48]  And that would include Growl.
[244.60 --> 247.88]  So we needed to take drastic measures to make sure Growl worked.
[248.40 --> 249.46]  And that was part of it.
[250.52 --> 253.68]  So that's the gist of what we changed.
[253.90 --> 258.42]  And we went from a preference pane to an application that sits in the menu bar.
[260.22 --> 264.14]  And we improved Growl dramatically in the way the preferences look.
[264.24 --> 268.02]  I mean, we have new icons and new system-looking things.
[268.02 --> 272.80]  We added a roll-up feature so that when you're away, you don't have a screen full of notifications.
[273.06 --> 277.44]  Instead, you get a little screen that says, hey, here's what happened.
[278.74 --> 281.16]  And overall, things have definitely improved.
[281.22 --> 282.66]  We've got a long way to go still.
[282.86 --> 287.52]  But things have definitely improved for the way just using Growl has worked out.
[288.38 --> 292.28]  Some would also say that another change would be that there's actually a price now to it.
[292.40 --> 295.66]  It was free before, and now it's, what, $1.99?
[295.66 --> 298.30]  Yeah, it's $1.99 in the App Store.
[298.84 --> 302.52]  And that's just helped fund development from then on out.
[302.92 --> 308.10]  The problem is that for the last, I don't know, three years, basically,
[308.10 --> 311.88]  we had effectively about two developers working on Growl.
[311.96 --> 312.34]  And that's it.
[312.76 --> 318.66]  And that's a dramatic change from about five years ago when we had about 60 people working on Growl.
[318.66 --> 321.96]  So we weren't able to maintain, for instance, Growl mail.
[322.74 --> 331.32]  For the entire, every time Apple releases an update to OS X, they break our Growl mail.
[331.86 --> 336.24]  So we just, you know, it would take a month to two months to update that.
[336.56 --> 338.76]  And it wasn't acceptable, put it that way.
[338.76 --> 345.18]  So we actually dropped Growl mail, and the lead developer for Growl picked it up as a side project.
[345.82 --> 349.46]  And he's going to keep it updated on a very regular basis.
[349.78 --> 354.18]  I mean, he's already got the 10.7.2 update ready to go whenever that comes out.
[355.44 --> 359.64]  And there's all sorts of different things that we will be able to do.
[359.72 --> 361.66]  Like, I've never been to WWDC.
[361.96 --> 364.60]  I've worked in Macintosh applications for almost 10 years now.
[365.40 --> 366.36]  That doesn't sound right.
[366.36 --> 366.60]  No.
[366.90 --> 373.54]  So there's things that effectively charging for the application at a small price.
[373.66 --> 376.02]  Like, I think Growl's worth more than $1.99.
[376.20 --> 376.76]  Don't get me wrong.
[377.08 --> 381.56]  I wouldn't work on something for eight years and think it's not worth more than $1.99.
[381.78 --> 385.28]  But it's a low price of entry for people.
[385.44 --> 393.12]  So we felt that that would enable more people to use it, while at the same time helping us to get things we want done.
[393.12 --> 396.60]  But so that's the reason.
[396.86 --> 404.04]  I mean, at some point you have to look and say, look, either we work on this in a professional fashion or we just don't.
[404.58 --> 408.24]  And that was either sell it or drop the project.
[408.54 --> 408.64]  Yeah.
[408.76 --> 411.22]  Well, we can certainly appreciate you getting paid for your work for sure.
[411.86 --> 416.36]  And you said you're eight years in and you're at a 1.3 version number.
[416.36 --> 420.68]  So what's changed over the roadmap of Growl since these past eight years?
[421.76 --> 426.22]  So, I mean, initially Growl.5 was the first version.
[426.66 --> 428.24]  And it's more or less just a proof of concept.
[428.54 --> 434.56]  I got promises from 15 different developers to look at it, not even implement it, just look at it.
[435.02 --> 436.90]  A few of those did.
[436.90 --> 441.98]  And ADM was one of the big ones in the beginning that helped out.
[443.54 --> 457.56]  But more or less it's gone from just kind of a geeky little tool to something a lot of people use to just, I mean, the last five years it's become just the first thing people install on their Macs.
[457.56 --> 468.50]  It's either that or Perrin or ADM or Skype or whatever applications they use all just use Growl in some way.
[468.98 --> 474.90]  And it's really cool that the stuff I work on people pick up and they like.
[475.88 --> 484.68]  You know, one of the biggest testaments, I guess, to the success of Growl isn't necessarily the user adoption, but the applications that have hooked into it and support it.
[485.26 --> 486.56]  Roughly how many do you have?
[486.56 --> 489.32]  I think at last count there was over 200.
[489.74 --> 495.22]  I'm actually going to go through the application lists today or tomorrow and make sure all the links work.
[495.52 --> 498.34]  But, yeah, it's over 200.
[498.48 --> 498.80]  I know that.
[498.92 --> 501.32]  Like we have Yahoo Messenger supports Growl.
[501.42 --> 503.36]  We have World of Warcraft supports Growl.
[504.12 --> 505.16]  AOL Instant Messenger.
[505.56 --> 507.34]  I mean, there's some big names in there.
[508.16 --> 511.48]  There's also – it's kind of a testament.
[511.48 --> 521.58]  We stuck with the idea that Growl should be something that the developer maybe spends 30 minutes on and they have notification.
[521.58 --> 529.74]  Before Growl, a developer would spend weeks developing a notification for some of their user base that liked it, and that's it.
[530.78 --> 533.32]  And, yeah, usually it wouldn't look that great.
[533.38 --> 537.28]  Or if it did, they spent a whole lot of time that they could have been spending on something else.
[537.28 --> 539.68]  So Growl solved that problem for them.
[539.78 --> 540.98]  It's a no-brainer for them.
[542.02 --> 552.08]  And, in fact, in the Growl 1.3 framework, which we are almost done beta testing, if Growl is not installed, they can still send a notification out to their end user.
[552.08 --> 555.70]  So that's something that the developer can control.
[556.26 --> 560.96]  That way, if they don't want to present the notification without Growl installed, they don't have to.
[561.20 --> 572.48]  But it's – the argument is that if Growl is for pay and users aren't going to buy it now, which is contradictory, by the way.
[572.54 --> 573.88]  Users are buying it galore.
[573.88 --> 586.18]  But, yeah, if Growl isn't installed and the argument is that developers will want it, well, it doesn't make sense because developers want something that's not going to take very long to implement.
[586.64 --> 587.82]  It saves them a lot of time.
[587.98 --> 589.02]  It looks good.
[589.10 --> 590.72]  People like it already.
[590.88 --> 592.26]  People already have it installed.
[592.42 --> 596.86]  There's a large user base, and it's relatively easy.
[597.00 --> 597.90]  They're going to pick it up.
[597.90 --> 607.40]  So that's – it says volumes about what our theory was back in the day about making it easy and people will come.
[607.80 --> 608.92]  And it came true.
[609.28 --> 612.80]  It took a while, but it – and we've got a lot of developers.
[613.02 --> 616.74]  In fact, I just got an email this week from a new developer that added support.
[617.52 --> 623.44]  What's cool about this, too, is that you've even gotten some external third-party support through different designs for the Growl styles.
[623.78 --> 624.84]  Talk about that a little bit.
[624.84 --> 630.12]  Yeah, so I think it was .7 or something.
[630.72 --> 631.52]  It's been a while.
[632.60 --> 642.22]  We added the ability for people to make styles on their own, and they can do it through just simple web technology, CSS, HTML.
[642.92 --> 650.84]  If you're a geek, you can write them up in Coda or you can write them up in Subeth Edit or whatever text editor of your choice is.
[651.00 --> 653.50]  And it's three or four files, and you're done.
[653.50 --> 656.06]  And you can make them look really pretty.
[656.20 --> 659.56]  Like, we've got a couple that we asked to just include with Growl.
[659.56 --> 666.26]  Like, there's one that looks sort of like Star Wars stuff coming in called Strawl, and it's just like Star Wars Growl.
[666.94 --> 673.10]  There's another one called Roaring Lion that looks like a lion dialogue box that you can download.
[673.10 --> 680.24]  And there's one that's called Black Glass, and it looks like a black piece of glass that comes up on your screen.
[680.24 --> 693.42]  And these developers of the different designs, they just write for however long it takes to make it look pretty, and they put it out on their website.
[693.98 --> 698.82]  And people can install it, and their notifications just then look how that developer made it.
[698.90 --> 700.00]  It's pretty cool.
[700.00 --> 703.12]  We've got a lot of different people making that stuff.
[703.64 --> 706.24]  It's awesome that these are crafted with CSS3 and HTML.
[706.48 --> 713.86]  I've been rocking the HUD style from Raji King for a while, and now I think I'm going to try the black glass that you just turned me on to.
[713.98 --> 716.38]  Yeah, it's pretty cool.
[716.48 --> 718.38]  I'll send you the link to it after this, actually.
[718.38 --> 725.34]  But that guy, he even made it so that the close button looks different.
[726.40 --> 736.04]  So it's red instead of black, and I don't know if that's a good thing or not, but he was able to do that with just some CSS or some HTML.
[736.38 --> 737.76]  And it's really simple.
[737.86 --> 743.10]  If you know a lot of CSS, it can be really complicated, and it's basically just WebKit.
[743.10 --> 748.12]  So whatever Apple provides through Safari, basically, is what you can use with Growl.
[748.38 --> 760.58]  That's just kind of beauty about that, too, is that if you're on a Mac since Growl is a Mac app, that you can kind of depend on the bleeding-edge WebKit slash CSS support so they can really push the edge of the design style, too.
[761.44 --> 763.74]  Yeah, if they really want to do that, they can.
[764.04 --> 768.28]  I don't know anybody doing that right now, but that would be cool to see.
[769.50 --> 774.66]  You know, a lot of our audience is on a Mac, but I'm sure substantial portions on Linux.
[774.66 --> 782.02]  But you guys have standardized on a network protocol to deliver Growl messages or notifications over the wire, too, with GNTP.
[782.20 --> 782.80]  Talk about that.
[783.08 --> 790.00]  Yeah, so GNTP, or Growl Network Transport Protocol, I think is what the acronym is.
[790.12 --> 791.22]  I'd have to go look to make sure.
[791.22 --> 804.86]  More or less, it's a standard that started out by the Adobe Air team contacting us and saying they couldn't talk to Growl because it's on UDP and not TCP for the really geeky portion of your audience.
[806.04 --> 806.76]  That's most of them.
[807.14 --> 809.78]  Yeah, so that's good.
[809.78 --> 813.80]  So most of your audience will appreciate the rest of this.
[814.04 --> 821.72]  So they hired one of our developers as a contractor, and he implemented most of the protocol.
[821.72 --> 830.76]  Well, then he went on to become a doctor, and that pretty much ended that from getting implemented in 2009.
[830.76 --> 842.58]  So in the meantime, the Growl for Windows and the SNAR projects, the Windows clones or the projects inspired by our project, picked it up.
[843.04 --> 850.98]  So SNAR and Growl for Windows have both had GNTP in their product for probably a year and a half now.
[850.98 --> 852.72]  So they've had a lot of testing.
[852.86 --> 857.38]  There's a lot of implementations out in the wild already.
[857.56 --> 858.76]  There's a Python.
[859.06 --> 859.86]  There's a PHP.
[860.08 --> 861.16]  I think I saw a Perl.
[861.58 --> 866.40]  I know there's a Java and a JavaScript somewhere.
[866.68 --> 871.74]  So there's already a lot of different tools out there to use this.
[871.74 --> 879.56]  And we finally said, you know, this old protocol we have doesn't really work that well, except for some people get it working.
[879.56 --> 881.68]  And this new protocol is really awesome.
[881.84 --> 888.48]  Why don't we just get rid of the old protocol, add the new one in, and it worked out really great.
[888.82 --> 897.74]  Now everyone that's tested Growl 1.3 with their networking setup, if you have two Macs, they can talk to each other, and it works beautifully.
[898.12 --> 906.46]  And actually, the internal communication for Growl going forward from applications to Growl will be over GNTP locally.
[906.46 --> 910.14]  So it's one protocol instead of maintaining three or four.
[910.74 --> 916.58]  You know, it's hard for me to, I think, pick one application that is enhanced the most by Growl.
[916.74 --> 922.42]  I look at my Twitter client and some of the other applications that are popping up Growl messages all day long.
[922.42 --> 928.38]  I think one of my favorites is my auto test loop that in the background in a terminal window, I've got tests that are running on a loop.
[928.44 --> 938.48]  And every time the loop completes, I've got the guy from Doom with either a regular face or a bloody face being whether or not my test have passed or failed.
[938.56 --> 942.40]  What application that you use personally is enhanced the most by Growl?
[942.40 --> 947.52]  It's going to sound stupid, but TextWrangler is probably the most enhanced.
[947.60 --> 955.04]  I don't think that TextWrangler or even BBEdit or any other text editor would even think about implementing a notification.
[955.04 --> 968.80]  But for me, when I do a search and a file for something, and it's a 10,000 line of code file, and it comes back and finds eight instances, it sends a notification to Growl that it got finished.
[968.90 --> 973.50]  Well, if it takes five minutes to do that search, it's great.
[974.08 --> 980.70]  I also, you know, I use Sparrow, and it actually doesn't work with 1.3 yet, but they're working on fixing that.
[980.70 --> 983.98]  But Sparrow was pretty nice.
[984.82 --> 990.64]  You know, Skype, I ran Skype today, and it told me when you guys contacted me, that was beneficial.
[990.86 --> 992.82]  I probably wouldn't have noticed for half an hour.
[993.80 --> 999.26]  Well, besides Growl, you've actually got some other open source experience with Perian.
[999.60 --> 1001.10]  What role do you play in that project?
[1001.72 --> 1005.46]  I'm the project manager, and I helped found Perian.
[1005.46 --> 1013.04]  Perian was actually a project that died a long time ago called FFusion, and it was the same thing.
[1013.24 --> 1015.16]  It was a QuickTime component.
[1015.56 --> 1024.54]  Let me back up and say, for those who don't know, Perian is a QuickTime component for the Mac that allows you to play pretty much anything you can download,
[1024.84 --> 1031.30]  except for a few minor things like Windows Media Player and Real Media and things like that.
[1031.30 --> 1040.24]  But so it's not the entire solution, but it's a majority of the solution for the random video files that you download.
[1041.68 --> 1047.78]  So I kind of was a person that said, let's hold back on preferences.
[1048.44 --> 1053.42]  Let's not add preferences for subtitles, for instance.
[1053.50 --> 1055.34]  Like, why do you need a preference for subtitles?
[1055.34 --> 1064.30]  We made the preferences pretty simple, so it's more or less an install and go type thing and not an install and play with it forever type thing.
[1065.32 --> 1067.78]  So it's worked out pretty well.
[1067.96 --> 1078.12]  We have this thing in Perian for auto detection of display sizes so that if you have a 23-inch screen, the subtitles should show up right.
[1078.20 --> 1081.92]  If you have a 13-inch screen, the subtitles should show up right.
[1081.92 --> 1083.88]  That sort of thing.
[1084.08 --> 1091.86]  And it's worked out pretty well up to the point that Perian has the problem Growl had for the last couple of years,
[1092.00 --> 1095.02]  where we really don't have that many developers anymore.
[1095.52 --> 1100.66]  So we've got a couple of guys that work on it, but they don't have time to work on it anymore.
[1100.66 --> 1115.08]  And effectively, we can't sell Perian because it has LGPL and GPL components, and we can sell Growl.
[1115.24 --> 1125.16]  So it'll be interesting to see if Perian lasts while Growl lasts or if Perian doesn't last because of the difference there.
[1125.16 --> 1132.44]  Yeah, I was going to ask you because you've got Growl in the App Store now, so I was going to ask you if the same path is going to be taken for Perian, but it sounds like it's not possible.
[1133.06 --> 1134.04]  No, it's not possible.
[1134.72 --> 1139.06]  So the GPL kind of makes that null.
[1139.06 --> 1146.58]  If we had consent from every single contributor that I ever worked on, everything that is included in Perian, we could do it.
[1146.74 --> 1155.20]  But we don't, and we won't be able to get that from – we use a lot of different open source technology like FFmpeg and LibMKV.
[1156.36 --> 1163.04]  And those things are great, and I'm not discounting the benefits of the GPL.
[1163.04 --> 1169.88]  Well, it's more of a – here's the difference with the BSD license, which is – Growl is a three-clause BSD license.
[1170.08 --> 1171.50]  We're able to do that.
[1171.80 --> 1179.88]  We're able to sell Growl and use that money to help the project move forward, whereas with Perian, we're not able to do that.
[1180.46 --> 1184.18]  And it's just a difference in mentality, and that's it.
[1184.34 --> 1189.78]  So I usually wouldn't bring this up in a podcast, but you guys said this was a pretty technical podcast.
[1189.78 --> 1193.26]  I mean we've actually had a series.
[1193.48 --> 1207.60]  We've been working on – Steve Glabnett works with us on the blog, and the licensing and naming license and which ones to use and why to use them is a topic that I think more and more people are going to be running into as they become more and more prolific and open source.
[1208.90 --> 1215.02]  And we've got a lot of people that follow the show that have been open source for just a number of years or have been drug into it because they use certain technologies.
[1215.02 --> 1219.50]  And they're contributing, and they're not really sure what license they're putting things under.
[1219.64 --> 1225.62]  And it sounds like that this could be a real issue if you don't know what you're talking about or which license to use.
[1226.34 --> 1226.54]  Yeah.
[1226.82 --> 1228.38]  So more or less.
[1228.50 --> 1232.38]  So the GPL has a few requirements, and it depends on what version of the GPL you have.
[1232.94 --> 1235.74]  I didn't think I would be talking about licensing today, but here we go.
[1235.74 --> 1252.32]  So the GPL has requirements that if you release a binary, which is built code to the world, and someone requests that code, that you should require – you are required and compelled to provide that code to them.
[1253.02 --> 1257.90]  Most open source projects that use the GPL, though, they just provide the code.
[1258.28 --> 1259.32]  Look at Linux.
[1259.54 --> 1260.54]  Look at the kernel.
[1260.82 --> 1263.28]  They provide the code to everyone.
[1263.28 --> 1266.12]  If you look at other things, it's the same way.
[1266.98 --> 1274.14]  The BSD license, and I'm going to fold the MIT license in the same way because they're pretty similar.
[1274.60 --> 1280.52]  If you use a three-clause BSD license or the MIT license, they don't require that.
[1281.04 --> 1289.16]  They require – specifically with the BSD three-clause, and I think I remember that MIT has those as well, but you might want to check.
[1289.16 --> 1297.62]  They require that you just attribute that you use code from, for instance, the Growl project.
[1298.24 --> 1306.58]  So with every application that supports Growl, if they use the framework, they should have in their about somewhere that they use code from the Growl project.
[1307.44 --> 1307.96]  And that's it.
[1308.52 --> 1310.32]  It's more about –
[1310.32 --> 1311.32]  Just simple attribution.
[1312.14 --> 1312.74]  Yeah, exactly.
[1312.84 --> 1318.04]  It's more about just getting people to use your code versus getting people to contribute back to the code that you write.
[1318.04 --> 1318.28]  Right.
[1318.76 --> 1321.22]  And the different mentalities, they're different purposes.
[1321.94 --> 1330.04]  So if you want your code that you write for open source to go into shareware or commercial products, you shouldn't use the GPL.
[1330.74 --> 1331.94]  And there's differences.
[1332.20 --> 1341.86]  Like there's the LGPL, which is – if you can use this, but if you modify it, give me back the code that you wrote.
[1341.86 --> 1344.60]  And I'm paraphrasing.
[1344.76 --> 1345.50]  I'm not a lawyer.
[1345.74 --> 1349.86]  So if you're using this podcast as legal advice –
[1350.50 --> 1350.92]  Double check.
[1351.04 --> 1351.60]  You're at your sources.
[1352.12 --> 1352.48]  Yeah.
[1352.62 --> 1354.78]  Go contact a lawyer and get them to read it.
[1354.78 --> 1362.76]  The other dramatic difference is that the BSD license is really short and the GPL is really long.
[1364.08 --> 1369.32]  I think it's – GPL has three clauses and they're about a sentence or two apiece.
[1370.00 --> 1375.78]  And there's just something about if you use this and it causes you problems and it causes the world to blow up, it's not our fault.
[1375.78 --> 1384.80]  So versus the GPL has that and it's – version two is so long and version three is even longer.
[1384.80 --> 1392.20]  So it sounds to me like you can probably get into some legal situations in terms of which license to use and how they end up getting used.
[1392.28 --> 1395.84]  I mean how did you learn more about these licenses?
[1395.98 --> 1404.80]  Was it just trial and error or just doing your due diligence and reading or is there certain sources that you've sourced up or do you actually have legal help that works with you and is part of the organization?
[1405.80 --> 1408.14]  So it was all of the above.
[1409.08 --> 1418.66]  So I learned about the GPL because I read it and I learned about the BSD license because I was like I'm not going to read another license that long and it wasn't that long.
[1418.82 --> 1419.62]  It was very short.
[1420.36 --> 1425.02]  And then there's this group called the OSI which is the – I think they're the open source initiative.
[1425.02 --> 1430.34]  I mean I could be wrong about what the acronym means but if you look for OSI, you can find them.
[1430.34 --> 1435.78]  And they kind of tell you what the different licenses are.
[1436.16 --> 1437.36]  I mean there's Creative Commons.
[1437.58 --> 1439.94]  There's like 40 different versions of that license alone.
[1440.80 --> 1445.88]  And there's all sorts of different licenses you can use and they're all qualified as open source.
[1445.88 --> 1455.74]  The dramatic difference for the BSD – well I'll put it this way.
[1455.88 --> 1460.02]  The two popular ones seem to be the GPL and the BSD three clause.
[1460.02 --> 1468.46]  That seems to be what most projects are going towards or are using at least when I looked at statistics in 2009.
[1469.88 --> 1475.46]  So I learned about them just by asking questions of people already using them on different open source projects.
[1475.46 --> 1477.06]  Like why did you use these licenses?
[1478.10 --> 1481.30]  Reading them, talking to lawyer friends I have in person.
[1482.68 --> 1485.50]  If I want to do this, what do I need to do?
[1486.32 --> 1495.80]  Like with Growl for instance, if someone wants to commit to the project and they're interested in working on the project and we get along with them, which is the most important part,
[1495.80 --> 1507.22]  then they get a commit bit right away, which is different than a traditional open source project where you submit a patch and you work on a patch for a while and you submit four or five different patches.
[1507.22 --> 1510.42]  And if people trust you, then you get to work on the project.
[1511.02 --> 1516.94]  Growl is more of a we trust you and we can just revert your changes if need be type thing.
[1517.96 --> 1522.20]  So bringing it back to Perian, you'd mentioned – I mean I know we talked about the licensing.
[1522.20 --> 1532.60]  And this is going to tie back into the licensing on that as well, but it sounds like Perian is at a potential stop because of licensing slash developer needs.
[1532.60 --> 1539.14]  And it sounds like maybe there's a way that the licensing thing can maybe help out because you might be able to put it into the store.
[1539.26 --> 1546.18]  But is it possible to maybe reach out to these different technologies that are using licensing and work something out with them?
[1546.22 --> 1547.44]  Is that something the community can help with?
[1547.44 --> 1548.62]  Because part of –
[1548.62 --> 1554.12]  So if there were five contributors to FFmpeg, that would be reasonable.
[1554.30 --> 1559.30]  But there's thousands, literally thousands of contributors to FFmpeg.
[1559.32 --> 1561.74]  And they all have different opinions on what a license is.
[1562.98 --> 1568.72]  And with Perian, it's not really an issue of licensing with the App Store.
[1568.72 --> 1570.28]  The App Store doesn't allow preference payments.
[1570.28 --> 1577.26]  They don't allow installers that install things, which is contrary to their Xcode installer that is in the App Store.
[1577.40 --> 1579.16]  But it is what it is.
[1580.80 --> 1583.52]  So Perian just couldn't make it into the App Store.
[1583.70 --> 1584.88]  And that's how it is.
[1585.00 --> 1586.94]  It's not designed to work in the App Store.
[1587.06 --> 1588.10]  It won't work in the App Store.
[1588.72 --> 1590.68]  But that doesn't kill its popularity.
[1591.88 --> 1594.14]  It's more popular than ADM is.
[1594.46 --> 1598.20]  I mean, the first week we had millions of users already.
[1598.20 --> 1602.28]  So it's more or less just manpower.
[1602.44 --> 1610.64]  I mean, we need probably about two more developers that spend 10 hours a week on Perian to work on Perian to make it move forward.
[1610.82 --> 1612.96]  We can do some work on it.
[1613.48 --> 1617.36]  But some of the bigger problems we just can't address without that.
[1617.52 --> 1623.18]  And there's some bugs with QuickTime X and OS X that don't allow it to go forward.
[1623.18 --> 1628.06]  But it's – I mean, overall, Perian still works and works fine.
[1628.20 --> 1630.10]  In most situations.
[1630.58 --> 1633.76]  And we don't really have a lot of user requests about things.
[1634.02 --> 1644.34]  And if you have a problem in QuickTime X, you can run Nice Player, which is this really cool little QuickTime-based application that plays media.
[1644.54 --> 1645.42]  That should work fine.
[1645.78 --> 1650.68]  And if that doesn't work, you can use QuickTime 7, which should work fine because it worked in 10.6.
[1650.68 --> 1661.24]  So there's a few different ways that Perian has problems or a few different routes or I'm going to stumble like Rick Perry did.
[1661.24 --> 1666.42]  There's a few different problems that Perian has with resources.
[1667.32 --> 1669.90]  But that doesn't stop it from being useful.
[1670.22 --> 1673.22]  But it will never make it into the App Store as it is designed.
[1674.22 --> 1678.82]  All of these projects, Perian, Growl, and ADM have long histories.
[1679.14 --> 1682.04]  And I'm pretty sure they predate the move to Intel.
[1682.24 --> 1683.32]  You guys were doing this in PPC.
[1683.32 --> 1690.86]  What shift did that cause in adoption of these projects?
[1692.70 --> 1698.20]  So with open source projects I've worked on, the developers pay for their own hardware.
[1699.50 --> 1706.04]  So it really takes the people working on it to pick up the new hardware.
[1706.04 --> 1714.30]  So with Intel, the move to Intel, for instance, some of the developers didn't have Intel machines for two years after that because their machine worked fine.
[1714.44 --> 1717.16]  So why would they want to go buy a new machine just for Intel?
[1718.04 --> 1721.46]  Some moved it right away because their machine was horrible.
[1721.80 --> 1724.56]  So they bought it right away.
[1724.74 --> 1726.92]  So we have some of that.
[1727.26 --> 1729.64]  There was – this is years ago.
[1730.08 --> 1731.90]  We had the universal binary stuff.
[1731.98 --> 1733.14]  We had to make it work right.
[1733.14 --> 1742.14]  But the thing that was promoted back then about the one click and it works, well, that wasn't quite true.
[1742.24 --> 1743.66]  You had to make your code work too.
[1744.80 --> 1747.80]  But those are just the small speed bumps of development.
[1748.00 --> 1752.58]  I mean, every time there's an OS update, something is going to break.
[1752.96 --> 1756.62]  With Growl, our stop button in the preference pane stopped working.
[1757.36 --> 1759.80]  There's a few other things that just stopped working.
[1759.80 --> 1765.24]  With pairing, I haven't seen anything that is broken, but that's because I don't use QuickTime X.
[1765.28 --> 1766.44]  I use QuickTime 7.
[1768.20 --> 1771.64]  And QuickTime X doesn't open subtitles, and it won't.
[1771.88 --> 1777.54]  And it, as is, will never open subtitles how we figured out how to make subtitles work.
[1778.06 --> 1779.50]  And we don't have a workaround.
[1779.50 --> 1787.88]  So there's a lot to do with keeping up with the Joneses in the development world.
[1789.20 --> 1791.46]  And there's some downside to that.
[1791.58 --> 1796.42]  I mean, with open source, if you don't want to work on a project anymore, you don't have to.
[1796.56 --> 1798.30]  You're not compelled to work on it.
[1798.36 --> 1798.94]  You're not paid.
[1799.06 --> 1799.94]  That's not your job.
[1800.60 --> 1803.62]  I mean, working on an open source project is just fun.
[1803.68 --> 1805.42]  And if it's not fun, you don't do it anymore.
[1805.42 --> 1809.52]  So, like I said, we had 60 people working on Growl at one point.
[1810.20 --> 1812.84]  And those people stopped working on it because Growl did what they needed.
[1813.68 --> 1818.06]  And, you know, we're cool to hang out with, but we don't hang out all the time.
[1818.64 --> 1822.64]  So eventually, you know, real life comes and you need to pay for your ramen noodles.
[1822.64 --> 1836.02]  And, you know, people use Growl as a stepping stone and they use ADM as a stepping stone and even pairing it to go work at Apple and Amazon and Yahoo and all those different big companies that people want to work for.
[1836.64 --> 1846.94]  So for the majority of the open source projects that are group projects, people are using those as a way to get into bigger companies or to show what they can do.
[1846.94 --> 1860.16]  And at some point, you know, if they move to Intel, something that made you angry, because 10 years ago, Apple used to talk bad about Intel or 15 or I wasn't around then.
[1860.26 --> 1863.08]  I haven't been a Mac user until 10.2 came out.
[1863.08 --> 1865.60]  So don't quote me on any of that stuff.
[1865.88 --> 1878.82]  But it's more or less if you're angry for whatever reason, Apple does something and you want to stick with what you want to use or just reformat your Mac and turn it into a Linux box or a Windows machine,
[1880.16 --> 1887.42]  there's no repercussions of doing that in the open source world on the Mac because you're not getting paid to do anything.
[1887.42 --> 1895.54]  So there's some downside to working with, depending on open source project code work or manpower.
[1896.30 --> 1899.80]  But, I mean, on the upside, it's with ADM, it's a big community.
[1899.94 --> 1905.52]  There's people that they talk to each other every day about things that aren't development related.
[1905.64 --> 1906.68]  They just talk to each other.
[1907.08 --> 1908.26]  With Growl, it's the same thing.
[1908.68 --> 1911.72]  And with Pairing, it's the same as well.
[1911.80 --> 1914.70]  We just, we don't have as many people working on it.
[1914.70 --> 1925.56]  We've got effectively what I like to refer to as one and a half developers on it right now, which is the amount of people that are working 20 hours a week on it.
[1926.84 --> 1929.60]  Any plans for ADM to make it to the App Store?
[1930.64 --> 1933.76]  I don't work on ADM anymore, so I can't really say.
[1934.18 --> 1938.42]  But I do know the people that do work on it, and I talk to them on a regular basis.
[1938.88 --> 1940.86]  They'd like ADM to get into the App Store.
[1940.86 --> 1943.36]  They have the same problem that Pairing does.
[1943.66 --> 1953.84]  The library they use called LibPurple from the Pigeon project, which is an open source IAM client on Linux and Windows.
[1955.02 --> 1962.42]  It's GPL, and I highly doubt that half the people that work on Pigeon would ever want to see their code in the App Store.
[1962.42 --> 1967.48]  So I don't think that it's going to make it as is.
[1967.68 --> 1973.66]  So what they would have to do on ADM to make ADM go in the App Stores and rewrite the entire thing.
[1975.16 --> 1976.78]  And I don't see that happening.
[1978.08 --> 1981.32]  There's 200,000 to 400,000 lines of code.
[1981.82 --> 1984.20]  There's all sorts of different artwork.
[1984.20 --> 1993.76]  They're not even at a 2.0 yet, and they are older than Growl is.
[1994.08 --> 2003.92]  So if Growl is eight years old and ADM has been around for probably four years before that, it's not a palatable proposition.
[2004.76 --> 2006.28]  So what's the future hold for Growl?
[2006.28 --> 2013.50]  So Growl is – there's more changes to come.
[2014.36 --> 2017.18]  So sandboxing is important, like I mentioned earlier.
[2019.68 --> 2024.20]  Applications that are in the App Store will be required to sandbox, so we're going to support that.
[2024.50 --> 2028.62]  We're going to change the interface up so it looks prettier and it's easier to use.
[2028.70 --> 2031.32]  Like the Applications tab is not that great to use.
[2031.32 --> 2038.24]  One of the previous developers and I came up with it in a coffee shop after four hours of drinking caffeine.
[2039.50 --> 2042.60]  So it's awesome then, and it's not awesome now.
[2043.16 --> 2044.76]  So we're going to change that up.
[2045.46 --> 2051.60]  Growl is going to have Prowl integration built in along with Boxcar and a few other things.
[2052.12 --> 2058.26]  So those things that people have to download plugins for and keep updated separately, we're going to eliminate that.
[2058.26 --> 2060.24]  And I don't know.
[2060.32 --> 2061.62]  We're going to just go from there.
[2062.04 --> 2069.32]  It's definitely going to progress from where it's at, and we'll just see Growl just keep going.
[2070.32 --> 2074.76]  We're going to see a lot more cross-platform, I think, with it, and especially with the GNTP stuff,
[2074.82 --> 2083.08]  so people that write code on different platforms can talk to it, which will be cool because eventually there will be a Linux clone of some kind that can talk to Growl.
[2083.08 --> 2096.92]  And overall, it's very promising as to where Growl is going, basically because of the awesome response from people just purchasing Growl 1.3 in the App Store.
[2097.26 --> 2103.02]  I mean, I'm pretty sure I'm going to WWDC next year, and I've never said that before.
[2104.06 --> 2106.16]  So it's definitely interesting.
[2106.72 --> 2108.20]  Just curious about numbers.
[2108.32 --> 2111.44]  I always can't go past this, but is there any way you can talk about some of those numbers?
[2111.44 --> 2118.02]  No, we haven't discussed yet even if we're going to release that yet or not as a company.
[2118.44 --> 2125.76]  We have a company behind us now called the Growl Project LLC just so that we can get Growl submitted to the App Store.
[2127.28 --> 2131.18]  But, yeah, we haven't discussed as a company whether we're going to release those numbers or not.
[2131.76 --> 2134.24]  If we do, we'd probably have a blog set up.
[2134.42 --> 2135.78]  We don't even have a blog set up yet.
[2136.76 --> 2137.98]  We're looking into that.
[2137.98 --> 2144.84]  But if we do, we'd probably have a blog set up and we can talk about, you know, here's the numbers or here's what it looks like.
[2144.94 --> 2154.28]  But, yeah, I'd rather talk to the other guys first before I go spouting out about stuff to people just because.
[2154.52 --> 2157.48]  But it's been a pretty nice response, put it that way.
[2157.48 --> 2162.02]  You mentioned a couple of times now this will be your first WWDC next year.
[2162.24 --> 2174.04]  And this week, Mark, the passing of Steve Jobs and wanted to get your take as someone who's built three successful projects or helped build three successful projects on the Mac platform.
[2174.66 --> 2175.82]  I'll put it this way.
[2175.82 --> 2182.24]  Every application I've worked on, when there's a release, I would email Steve Jobs and ask him to try it.
[2183.72 --> 2186.68]  I didn't care if he replied.
[2187.04 --> 2188.34]  I just wanted him to try it.
[2188.92 --> 2190.50]  I didn't do that to anybody else.
[2191.80 --> 2192.96]  Did you ever get a response?
[2193.24 --> 2193.50]  No.
[2193.76 --> 2195.52]  No, I never got a response.
[2195.52 --> 2204.90]  But, you know, you're running a multi-billion dollar company versus this guy from Texas is asking you to try his application and, you know, which is going to happen.
[2205.56 --> 2216.74]  But ADM was used as examples on the Apple website for compile times between Intel and PPC, for instance, when they did the transition there.
[2216.74 --> 2224.46]  They used Growl and they used Parian at the WWDC talks and they used ADM to talk about how to implement things.
[2224.46 --> 2228.56]  So, you know, people know about what Growl is.
[2228.86 --> 2234.22]  One of the lead developers for Growl got hired in ADM partly because he was a lead developer for Growl.
[2235.98 --> 2238.50]  So it's that.
[2238.50 --> 2254.10]  But, I mean, Steve was – Steve – what I do with any computer was influenced by Steve entirely.
[2254.46 --> 2257.94]  I mean, Bill Gates and Steve were the industry.
[2258.10 --> 2259.02]  They are the industry.
[2259.42 --> 2262.56]  And, you know, it's just like for Windows if Bill Gates died.
[2262.66 --> 2271.22]  I mean, as much as Bill Gates is the butt of everyone's joke, it's – you know, he's a legend just like Steve is.
[2271.22 --> 2281.18]  And it's – it's probably the best thing I've heard about the whole thing is Stephen Colbert had a segment about this.
[2281.26 --> 2284.82]  And it was, you know, all jokes and funny like, you know, Stephen Colbert's show is.
[2284.88 --> 2293.94]  But the last ten seconds he spins – you know, he switches from sarcastic reverse mode that he normally is to, you know,
[2294.02 --> 2296.56]  Sirius Stephen Colbert that you rarely see on the show.
[2296.56 --> 2302.14]  So – and it was probably the most touching moment out of anything I've seen this week about it.
[2303.14 --> 2307.36]  And, you know, there's not much else you can really say about it.
[2307.46 --> 2309.76]  You know, the guy was great and he passed away.
[2309.86 --> 2310.68]  He's passed away too early.
[2310.76 --> 2312.06]  He worked his life away.
[2312.06 --> 2317.40]  But he gave us something that we can use for the next 20 years essentially.
[2318.78 --> 2321.82]  Well, I guess we're at that point where we can actually even talk about heroes I guess.
[2321.82 --> 2326.66]  This might be a good segue into our heroes moment where we talk about, you know, something in open source,
[2326.82 --> 2333.58]  something, someone in open source that you look up to, either a code base that you're looking forward to playing with on a weekend
[2333.58 --> 2338.92]  whenever you're not doing, you know, parrying or growl work or planning this new business you're working on.
[2339.02 --> 2342.58]  So, you know, what out there in open source or who out there in open source is something you look up to
[2342.58 --> 2343.56]  or something you want to play with?
[2343.56 --> 2348.94]  So, it's – so there's this guy that works on ADM.
[2349.04 --> 2350.40]  His name is Evan Schoenberg.
[2350.58 --> 2352.64]  And he's worked with ADM since forever.
[2354.06 --> 2355.66]  And he's also a doctor.
[2355.80 --> 2356.80]  And he's also this.
[2356.86 --> 2357.50]  And he's also that.
[2357.54 --> 2359.44]  He's like 50 app store apps.
[2360.00 --> 2362.06]  And, you know, he works a full-time job.
[2362.10 --> 2363.38]  He's a wife and a kid.
[2363.64 --> 2365.08]  You know, they have a dog.
[2365.30 --> 2368.92]  And I don't know how he does all of it at all.
[2369.04 --> 2370.50]  I mean, that's just crazy.
[2370.50 --> 2376.76]  I mean, just as someone to look up to, like, he and I ran a shareware business.
[2376.94 --> 2379.34]  We sold this product called Family a while back.
[2379.42 --> 2380.46]  We eventually sold that off.
[2380.70 --> 2386.78]  But, you know, it's – the guy is, like, phenomenally everywhere.
[2387.36 --> 2391.88]  So, just from a person's perspective, someone to look up to, you know, you look him up sometime.
[2392.60 --> 2396.30]  And it's definitely interesting.
[2396.64 --> 2398.62]  As a – you know, he's a good friend and all that too.
[2398.62 --> 2406.54]  But as a code base, you know, it's – I'll look at new tools and all that and whatnot.
[2406.74 --> 2412.82]  But I don't go digging around in source code from other people unless it's something where I need to fix something.
[2413.38 --> 2414.12]  And it's really that.
[2414.20 --> 2416.18]  I usually just complain to them until they fix it.
[2417.30 --> 2422.70]  It's – you know, sometimes I'll look at things like, you know, how can I make this work with our stuff?
[2422.70 --> 2430.42]  But, I mean, for the most part, it's, you know, people you look up to are, like, you know, my dad, for instance.
[2430.78 --> 2436.46]  And everyone looks up to their dad if their dad was in their life and their mom if they were in their life and all that.
[2436.46 --> 2441.26]  And, you know, the typical responses you see.
[2441.42 --> 2447.64]  But, I mean, the people that work on the different open source projects are the people I look up to, to be honest with you.
[2447.70 --> 2453.52]  I mean, they spend a dramatic amount of their time working on stuff so that other people can use this offer they write.
[2453.66 --> 2454.30]  And that's it.
[2454.70 --> 2456.00]  That's all they want.
[2456.00 --> 2469.92]  And it's crazy that it'll last 25 years that this has happened is that people just want to spend a portion of their life so that it makes other people's lives better.
[2470.74 --> 2472.26]  And it's everyone.
[2472.48 --> 2474.82]  It's not just, you know, just one person.
[2476.16 --> 2483.22]  There's what Stallman on the Linux side, he has his opinions, and I may not agree with them.
[2483.22 --> 2489.24]  But he stands up for people and what he thinks is right, and it's admirable.
[2490.02 --> 2494.36]  And, you know, as long as people do things that are admirable, it's worth looking at.
[2494.96 --> 2500.72]  So I don't think there's a single person I can point out except for Evan because he's crazy.
[2500.90 --> 2503.62]  But that's just a size point.
[2504.58 --> 2508.58]  But, yeah, there's a lot of people I can name, put it that way.
[2508.58 --> 2515.36]  Well, this is the part of the show where we actually turn it back on to you to say if there's anything that you didn't plug that you want to plug,
[2515.48 --> 2521.00]  like such as the IRC channel for Growl or something special that you just want to plug before we head off.
[2522.16 --> 2527.84]  Yeah, so, yeah, for contacting us, if anybody needs to contact us, the best way is through IRC.
[2527.84 --> 2530.62]  It's pound growl on a free note.
[2532.18 --> 2537.70]  Lots of thanks to Google Code for hosting us, Network Redux for hosting us, and Cashfly for hosting us.
[2539.76 --> 2543.36]  I like my email client, Sparrow, if you like email.
[2544.86 --> 2547.52]  I mean, name the different apps.
[2547.52 --> 2553.96]  There is a cool, if you use source code version control stuff and you like Mercurile or JIT,
[2554.48 --> 2563.44]  there is this cool app called SourceTree, and it's probably the first GUI source control app that I've actually thought was decent.
[2564.42 --> 2567.42]  So if anybody does source control, check it out.
[2567.58 --> 2570.56]  It was free this week, a regular $35.
[2570.86 --> 2576.02]  I don't know if it is still free, but, you know, I think it's worth the $35.
[2576.02 --> 2580.14]  I mean, I'll probably pay them at some point anyways.
[2581.26 --> 2587.00]  So, but, yeah, I mean, if you have any questions on anything I use, come see me on the IRC channel.
[2587.12 --> 2593.86]  I'm usually, you know, around during the day, U.S. time, and if I'm not around, someone else will be.
[2594.10 --> 2595.14]  Because you're here in Texas, right?
[2596.08 --> 2596.98]  Yeah, I'm here in Texas.
[2597.14 --> 2597.68]  I'm in Houston.
[2598.08 --> 2598.64]  Oh, awesome.
[2598.70 --> 2599.74]  That's kind of where I'm at.
[2599.78 --> 2600.68]  I'm in Sugar Land, actually.
[2601.46 --> 2603.02]  Oh, I'm in Kingway.
[2603.24 --> 2603.84]  There you go.
[2603.84 --> 2609.66]  Well, Chris, I know that we certainly appreciate, you know, all your contributions to open source
[2609.66 --> 2614.44]  and certainly the education you gave us today on licensing and the direction of Growl
[2614.44 --> 2618.72]  and what it takes to get into the App Store and Parian and everything you've done.
[2618.88 --> 2622.16]  So we really appreciate the time you've taken to chat with us,
[2622.20 --> 2624.82]  and we look forward to using more of your codes.
[2625.78 --> 2628.20]  And if you're a Growl user, go and download it from the App Store.
[2628.46 --> 2632.52]  Two bucks is definitely worth the price for what you've gotten in the last eight years.
[2632.52 --> 2633.58]  Thanks.
[2633.76 --> 2633.90]  Yeah, that's true.
[2634.30 --> 2634.84]  Thanks, Chris.
[2635.08 --> 2635.84]  Yeah, thank you, guys.
[2635.84 --> 2636.46]  Thank you.
[2656.80 --> 2657.22]  We'll see you next time.
[2657.26 --> 2657.40]  Bye.
[2657.40 --> 2657.72]  Bye.
[2657.72 --> 2658.30]  Bye.
[2658.30 --> 2658.64]  Bye.
[2658.64 --> 2659.22]  Bye.
[2659.22 --> 2659.50]  Bye.
[2659.80 --> 2660.06]  Bye.
[2660.26 --> 2660.84]  Bye.
[2660.94 --> 2661.44]  Bye.
[2661.44 --> 2662.10]  Bye.
