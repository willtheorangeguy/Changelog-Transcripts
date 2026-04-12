[0.00 --> 2.52]  Bandwidth for change log is provided by Fastly.
[2.92 --> 5.40]  Learn more at Fastly.com.
[5.76 --> 8.40]  I'm Filippo Valsorda and it is Go Time.
[20.84 --> 28.06]  It's Go Time, a weekly podcast where we discuss interesting topics around the Go programming language, the community, and everything in between.
[28.06 --> 32.54]  If you currently write Go or aspire to, this is the show for you.
[42.70 --> 46.70]  Welcome back, everybody, to another episode of Go Time.
[46.94 --> 48.94]  It is episode number 32.
[49.32 --> 51.84]  We are recording this today on January 26th.
[52.16 --> 57.54]  Today's show is sponsored by Stack Impact and Arden Labs' series of Go Training.
[58.06 --> 60.26]  Today on the show, we have myself, Eric St. Martin.
[60.82 --> 62.28]  Brian Kettleson is also here.
[62.44 --> 62.96]  Say hello, Brian.
[63.56 --> 64.04]  Hello, Brian.
[64.62 --> 65.86]  And Carlicia Pinto.
[66.44 --> 67.04]  Hi, everybody.
[67.66 --> 70.92]  And our special guest today is Filippo Valsorda.
[71.34 --> 74.40]  Why don't you give everybody kind of a quick background about yourself?
[74.56 --> 77.22]  Tell us a little bit about yourself and kind of the things you're working on.
[77.60 --> 80.28]  And then we'll kind of get into some of the projects you've been working on.
[80.86 --> 81.14]  All right.
[81.14 --> 81.86]  Hello, everyone.
[82.20 --> 82.88]  I'm Filippo.
[83.06 --> 85.26]  I'm from Italy and I work at Cloudflare.
[85.76 --> 90.26]  I did a number of different things with Go at Cloudflare.
[90.42 --> 95.52]  But the most recent one is a small project that I recently published called Hello Gopher.
[95.94 --> 100.64]  Before that, I was working on the Cloudflare DNS server, which is your Go.
[101.16 --> 102.28]  And yeah.
[102.28 --> 102.56]  Yeah.
[102.92 --> 107.78]  So recently, we've been looking at one of your projects, which was the Hello Gopher,
[108.04 --> 113.08]  which was kind of an easy way to bootstrap a project for people who might not be familiar
[113.08 --> 114.48]  with using GoPath.
[114.78 --> 116.46]  You want to talk a little bit about that?
[117.14 --> 117.58]  Yeah, sure.
[118.10 --> 123.92]  So at Gopher, we're hiring a lot of developers and we don't really like hire Go developers.
[124.22 --> 129.66]  We hire developers and then we train them to work on Go because we know how nice and easy
[129.66 --> 131.28]  it is to pick up the language, right?
[131.28 --> 137.10]  So I've been looking at how to smooth that process and also how to make it easier for
[137.10 --> 142.46]  other people in the company to interact with all these repositories that are in Go when they're
[142.46 --> 143.28]  not Go developers.
[144.24 --> 147.56]  And I was going through this process.
[148.20 --> 154.94]  And then on a drive home from Napa with a lot of wine involved, I was in a car with two
[154.94 --> 160.62]  senior engineering managers and they started ranting at me about GoPath.
[161.28 --> 163.64]  And I was like, what?
[163.84 --> 164.46]  Wait, wait, wait, wait.
[165.10 --> 169.76]  I mean, they started running, telling me how Go was hard to use and they never could figure
[169.76 --> 170.12]  it out.
[170.64 --> 174.88]  And every time they have to pick it back up, it's confusing and it takes them 30, 40 minutes
[174.88 --> 175.64]  just to pick it up.
[175.66 --> 176.80]  And I was like, what?
[177.10 --> 178.14]  What are you talking about?
[178.14 --> 179.14]  Yeah.
[179.14 --> 180.64]  And yeah, you can guess it.
[180.82 --> 185.92]  It was all about the GoPath and the fact that you have to clone this repository in the right
[185.92 --> 187.38]  place in your first system.
[187.62 --> 193.52]  And that's a completely extraneous process to any developer that comes from other languages.
[193.52 --> 196.38]  So that's what Hello Gopher is solving.
[197.08 --> 197.20]  Yeah.
[197.28 --> 202.26]  It's funny because it was yesterday or the day before I had a friend who had a similar
[202.26 --> 205.28]  issue with that kind of like, where do you check out the code to?
[205.38 --> 209.72]  Because most of the time you're used to just pulling it to wherever you happen to store
[209.72 --> 210.20]  your code.
[210.30 --> 213.50]  It doesn't have to be in a specific spot on your hard drive.
[214.36 --> 218.16]  And then the other side of it that gets confusing is how do you contribute back?
[218.16 --> 220.28]  You know, that's a common confusion.
[220.54 --> 222.52]  Like, OK, so I want to commit something.
[222.66 --> 227.40]  So I fork this repo, but now it's not in the right place.
[227.40 --> 229.28]  And how do I change my import path?
[229.36 --> 235.78]  And it's not immediately clear that you could just set your fork as a different remote for
[235.78 --> 236.92]  the Git repository.
[237.42 --> 242.44]  So there is a lot of confusion with that because the paths are explicit that way.
[243.02 --> 243.18]  Yeah.
[243.18 --> 248.74]  A number of times I've seen like PRs that have all the import paths changed to the fork
[248.74 --> 251.84]  and the person being like, oh, yeah, you can remove that.
[251.90 --> 255.48]  I just had to do that to make it work on my machine.
[256.06 --> 258.74]  And every time it's this little, you know, learning process.
[259.44 --> 263.98]  So Hello Gopher is actually meant to like get you through your first PR without needing
[263.98 --> 265.56]  to set up GoPath at all.
[265.56 --> 273.18]  So the project just builds, tests, runs GoFMT, GoInports without any need to set up GoPath.
[273.72 --> 277.98]  So have you had pretty good success at Cloudflare with that, with people being able to just
[277.98 --> 279.92]  grab a project and work on it?
[280.30 --> 285.66]  Yeah, I definitely like shadowed a number of people through the different revisions of
[285.66 --> 286.10]  Hello Gopher.
[286.38 --> 287.82]  It looks like a simple project.
[288.00 --> 294.34]  It's, you know, 110 lines of makefile, but it went through so many changes even before
[294.34 --> 295.24]  the Git history.
[295.56 --> 298.08]  And I like try to smooth over.
[298.18 --> 302.12]  I'm pretty happy about like how people pick it up and use it these days.
[302.74 --> 308.92]  A user at some point like reported an issue and I just like nudged them towards one section
[308.92 --> 313.22]  of the docs and they reported immediately after being like, oh, yes, got it.
[313.28 --> 313.98]  It worked.
[314.32 --> 315.36]  That was awesome.
[316.18 --> 319.10]  That was like, yes, this works moment.
[320.16 --> 320.96]  That's nice.
[321.48 --> 323.80]  Brian, Carly, have you guys had a chance to play with it yet?
[324.24 --> 324.54]  No.
[324.54 --> 330.00]  No, I've been watching the video on the GitHub repository and actually I'm watching it again
[330.00 --> 330.22]  now.
[330.32 --> 330.94]  It's kind of cool.
[331.50 --> 334.48]  I'm surprised that you were able to do this so elegantly.
[334.48 --> 339.36]  I didn't play with it and I actually didn't know about it until today.
[339.36 --> 345.66]  And I wish I had because I helped organize the Gopher meetup in San Diego.
[346.26 --> 349.90]  And at every meeting there is somebody, at least one person who doesn't have the GoPath
[349.90 --> 350.36]  set up.
[350.46 --> 354.32]  And I would have been glad to just point them to this instruction.
[354.32 --> 361.98]  I feel like every language has like that hurdle to get set up when you're not familiar with
[361.98 --> 362.62]  the environment.
[362.94 --> 367.04]  You know, like I did Ruby for a long time and it never really occurred to me how complicated
[367.04 --> 369.56]  it is to set up a Ruby development environment.
[369.78 --> 370.34]  Oh, my gosh.
[370.68 --> 370.94]  Yeah.
[371.16 --> 372.52]  Until you try to help somebody.
[373.16 --> 373.34]  Yeah.
[373.34 --> 376.10]  I had to build a whole Linux live CD for that.
[376.22 --> 377.90]  Like how many steps there are.
[377.98 --> 383.70]  It's like you have to start explaining Bundler and RBMV or what was the other one?
[384.62 --> 385.06]  RVM.
[385.52 --> 385.72]  Yeah.
[385.84 --> 386.16]  RVM.
[386.32 --> 391.54]  And then they have now they have like a Ruby build one where it kind of builds tools in
[391.54 --> 392.30]  your path too.
[392.44 --> 396.78]  But still, you know, it gets confusing having to remember all these things and set them up.
[396.94 --> 402.26]  And, you know, now we have GoPath and we have vendoring and you're downloading projects
[402.26 --> 403.80]  with the vendor stuff.
[403.80 --> 408.20]  So, yeah, it gets confusing and we forget about it because we've been doing it for so long.
[408.30 --> 412.74]  It's just kind of part of what we do until somebody who's not familiar with the environment
[412.74 --> 414.48]  is like, well, how do I set this thing up?
[415.06 --> 418.28]  But with 1.8, we're not going to have this problem anymore, right?
[418.74 --> 420.36]  This is all going to go away.
[420.84 --> 422.60]  This particular problem won't go away.
[422.78 --> 422.98]  No.
[423.28 --> 426.58]  If you're setting it up the first time, unless you want in a specific place.
[427.16 --> 428.68]  You're still going to have a GoPath.
[428.80 --> 432.68]  It will just be automatically set for you if you haven't set it.
[433.26 --> 438.28]  So we'll still have the confusion that new developers get when they still don't understand
[438.28 --> 440.28]  what a GoPath is and why they need to use it.
[440.80 --> 440.90]  Yeah.
[440.94 --> 442.76]  The default GoPath solves one problem.
[442.76 --> 445.40]  And it's that now you can just write GoGet.
[445.94 --> 451.12]  And that is enough as instructions to install something, probably, most of the times.
[451.56 --> 455.22]  But it's definitely not enough for anyone that just wants to Git clone.
[455.44 --> 459.66]  And it's not enough for someone that wants to contribute because they will still have opinions
[459.66 --> 462.12]  about where they want the project to be, et cetera.
[462.12 --> 469.44]  Now, do you require any special project organization or will this work with any project structure?
[470.18 --> 476.46]  So the point of Hello Gopher, also to avoid that Ruby 100 different tools scenario, is that
[476.46 --> 479.80]  it works drop-in on normal GoGetable projects.
[480.28 --> 482.22]  It's not a different build tool.
[482.22 --> 487.68]  It's just something that wraps things and does horrible black magic with sim links that you
[487.68 --> 494.18]  shouldn't look into so that it just has a fake GoPath that points to your repository.
[494.52 --> 498.28]  But it's still the normal Go structure that we're used to.
[498.28 --> 501.78]  It's also completely compatible with anything you already have.
[501.96 --> 507.12]  And it doesn't get on your colleague's toes if they actually have GoPath set up, et cetera.
[507.74 --> 508.08]  Nice.
[508.66 --> 512.72]  And now this is agnostic to what you use for your vendoring tool, right?
[513.30 --> 513.92]  Yeah, correct.
[514.08 --> 516.16]  You can vendor with whatever you want.
[516.24 --> 522.74]  A few tools will freak out if you are not in GoPath, which is kind of legitimate because
[522.74 --> 525.82]  vendoring doesn't even turn on outside GoPath.
[525.82 --> 531.96]  But if you can get them to actually do their job and vendor stuff, any tool that you use
[531.96 --> 533.04]  for vendoring will do.
[533.54 --> 536.84]  I patched GVT so that it doesn't complain if there's a make file.
[537.60 --> 540.06]  So that's how I sold it in GVT.
[540.64 --> 541.10]  Nice.
[541.80 --> 544.90]  And now you actually work on all kinds of cool stuff.
[545.24 --> 548.94]  I've been following you for a long time because of all the security stuff you do.
[549.40 --> 553.48]  One of my favorite things you did was the WhoAmI SSH server.
[553.48 --> 555.30]  I still love this.
[555.52 --> 556.22]  It's creepy.
[557.06 --> 562.86]  Yeah, you can understand how SSH works and how keys are exchanged, but it doesn't really
[562.86 --> 565.08]  connect how you could leverage that.
[565.40 --> 571.72]  Actually, for anybody who's not familiar with it, do an SSH to WhoAmI.philippo.io.
[572.38 --> 573.52]  It's a lot of fun.
[573.62 --> 575.62]  Do you want to tell everybody kind of what it is and explain?
[575.62 --> 580.60]  I should tail the logs and say hi to people, but that would be even more creepy.
[582.52 --> 589.74]  So, yeah, WhoAmI is this little demo that came out because my flatmate, who deserves
[589.74 --> 594.98]  a lot of the credit, had dumped all the public SSH keys of GitHub.
[594.98 --> 600.32]  I don't know if you might not realize, but if you go to github.com slash your username
[600.32 --> 603.56]  dot keys, it will show you your SSH keys.
[603.80 --> 605.68]  That's super handy for a number of reasons.
[605.68 --> 609.20]  Like I want to give this person access to my box or something like that.
[609.64 --> 616.00]  But, you know, you can just scrape the whole, not even scrape, just use the GitHub API to
[616.00 --> 618.80]  get a list of all users, download all the keys.
[618.80 --> 626.56]  And now you have a pretty good idea of a huge chunk of the SSH keys to whom they belong.
[627.36 --> 631.52]  And at the same time, I was like studying the SSH protocol and trying to figure out a
[631.52 --> 633.18]  bit of the internals and such.
[633.48 --> 640.62]  And I realized that the default behavior is just to send preemptively the public keys you're
[640.62 --> 641.60]  willing to use.
[641.98 --> 645.20]  Then the server responds, oh, yes, I like this one.
[645.20 --> 651.88]  So if the server responds that, then you make a signature with that key to log in.
[652.36 --> 656.08]  But if the server refuses them all, it will still see them all.
[656.56 --> 664.02]  So I built this little tool with the golang.org slash x slash SSH package that would ask you
[664.02 --> 671.70]  to use your public keys, refuse them all, but like log them, then ask you to do keyboard
[671.70 --> 676.90]  interactive login, which is a weird thing that I could just like make happen automatically.
[677.18 --> 679.44]  So log you in, in any case.
[679.92 --> 684.24]  And then if I found you in the database, I would tell you your name and surname and GitHub
[684.24 --> 687.40]  account because I cross-referenced it to the database.
[688.26 --> 695.66]  And once you explain it is kind of trivial, but like the surprise, the impact is pretty strong.
[695.66 --> 700.50]  So I ran it on my machine and it didn't find my GitHub public key.
[700.68 --> 706.98]  I'm wondering if it's because I have multiple ones and you grabbed one that wasn't active?
[707.58 --> 713.26]  So the way the SSH protocol works is when you do public key authentication is it will pass
[713.26 --> 714.40]  all of your public keys.
[714.62 --> 721.42]  So anything that's in your .SSH directory, you'll see like the ID underscore RSA.pubs
[721.42 --> 722.78]  and things like that.
[723.36 --> 726.86]  It will pass that, which contains your email address in it.
[727.26 --> 727.70]  Oh, yeah.
[727.86 --> 730.64]  I mean, there's that, but I don't even use that.
[730.88 --> 733.66]  I use the matching of the actual public key.
[733.80 --> 734.38]  Oh, that's right.
[734.46 --> 734.62]  Yeah.
[734.62 --> 736.48]  Because you have a list of the actual keys.
[736.86 --> 737.00]  Yeah.
[737.30 --> 739.28]  So I'm trying to figure out why I didn't find mine.
[739.62 --> 742.00]  Is that key added to your GitHub account?
[742.52 --> 745.30]  I'm using this computer to log into push to GitHub.
[745.74 --> 746.10]  Interesting.
[746.56 --> 746.74]  Yeah.
[746.82 --> 749.88]  So what's happening is probably that the database is out of date.
[750.04 --> 750.32]  Yeah.
[750.32 --> 754.22]  We should like wait for Ben to get home and ask him that, I think.
[756.50 --> 757.06]  Call him.
[757.08 --> 759.64]  Sorry, our DBA isn't available right now.
[760.18 --> 761.10]  Phone a friend.
[762.76 --> 765.56]  Yeah, I want to use the help from home.
[767.72 --> 768.12]  Nice.
[768.20 --> 771.02]  I just added a function to my bash functions directory.
[771.20 --> 776.74]  So now I could just type hello go for any directory and it will use wget to get the hello go for make
[776.74 --> 778.54]  file and add it to the current directory.
[778.70 --> 779.96]  I can't wait to go try that out.
[779.96 --> 780.32]  Nice.
[780.54 --> 780.90]  Nice.
[781.32 --> 782.26]  All about some aliases.
[782.78 --> 782.92]  Yeah.
[782.92 --> 787.12]  The cool thing about that who's there thing is, is it really makes you connect with how
[787.12 --> 789.02]  much information leakage there is.
[789.28 --> 793.92]  Like you don't really consider that when you try to SSH a server that you're leaking information
[793.92 --> 800.48]  that you, you could be giving away, say, email addresses or, or those keys could be used
[800.48 --> 803.16]  to, you know, match you against other databases.
[803.16 --> 804.54]  So really interesting.
[804.54 --> 804.94]  Yeah.
[804.94 --> 805.26]  Yeah.
[805.26 --> 810.70]  I didn't even go full creep on it because from the GitHub account, you can probably jump
[810.70 --> 817.74]  to the key base account if you have key base and, or like use the links you have in your bio.
[817.74 --> 820.96]  And from there, jump to your Facebook or your Twitter.
[820.96 --> 826.12]  And from there, jump to your bio, maybe your home address, maybe your phone number.
[826.78 --> 827.80]  That would have been nice.
[827.90 --> 832.26]  Like, hello, you're trying to association to a server where you're going to get a phone call in a minute.
[832.26 --> 833.32]  Oh yeah.
[833.40 --> 837.08]  I mean, you really could go full on creeper because you could basically take like the domain
[837.08 --> 841.26]  from their, their email address and then start doing who is, is on it.
[841.36 --> 843.54]  And yeah, you could get all kinds of information.
[844.04 --> 844.20]  Yep.
[844.60 --> 846.46]  So what other things are you working on?
[846.54 --> 848.52]  I know you're doing some TLS stuff as well.
[848.96 --> 849.14]  Yeah.
[849.32 --> 854.84]  So the project I've been working on for the last few months, quite a few months now.
[854.98 --> 855.20]  Wow.
[855.88 --> 857.28]  Is TLS 1.3.
[857.28 --> 863.96]  So the short version of the crypto like pitch is that TLS 1.3 is the new version of TLS.
[864.26 --> 871.04]  It's not about getting cryptographers jobs security, but instead about making the protocol
[871.04 --> 873.80]  actually more robust against future attacks.
[874.04 --> 879.78]  So it's a complete like rework and it takes one less round trip to connect to things.
[879.78 --> 883.82]  So it's faster and a bunch of other things that if you're interested in,
[883.82 --> 888.00]  there's a talk at CCC 33 C3 that you should watch.
[888.70 --> 895.48]  But point is we wanted to implement TLS 1.3 and, you know, participate in the standardization
[895.48 --> 898.28]  process with a real implementation deployed.
[898.52 --> 903.32]  So we wanted to take a TLS stack and add 1.3 ourselves.
[904.14 --> 909.98]  And I essentially threatened to quit if they've made me do it on OpenSSL.
[909.98 --> 912.50]  Well, no, I'm joking.
[912.64 --> 913.52]  Nobody asked me.
[913.94 --> 917.04]  They just asked me what to use as a base.
[917.18 --> 924.00]  So I just jumped straight to CryptoTLS, the standard library of Go, which is a wonderful
[924.00 --> 929.94]  stack written originally by Adam Langley, which a lot of people in the industry say that it's
[929.94 --> 932.52]  what they go to to understand TLS.
[932.52 --> 938.08]  Like they read the spec, they fail to understand it, they go to CryptoTLS, they read the code,
[938.18 --> 940.26]  they go code, and now they understand things.
[940.64 --> 942.20]  So that was the starting point.
[942.84 --> 946.22]  And we extended it to have TLS 1.3 support.
[946.56 --> 948.74]  We worked most on the server side.
[949.36 --> 954.20]  And it's now deployed globally on millions of cloud for sites.
[954.62 --> 957.80]  Literally, like if you just sign up for a free account, it's on by default.
[957.80 --> 963.44]  And the nice thing we like don't talk that much about, but you can definitely like gather
[963.44 --> 969.90]  is that if our TLS 1.3 stack is in Go and you can use Go to connect to Cloudflare sites,
[970.50 --> 975.56]  it means that sometimes when you connect to Cloudflare, actually in the HTTP pipeline,
[975.84 --> 979.30]  there is a Go HTTP reverse proxy.
[980.10 --> 983.44]  So all of the Cloudflare reverse proxy stuff is written in Go?
[984.00 --> 984.86]  So no, no, no.
[985.38 --> 987.48]  Cloudflare is a Nginx shop mostly.
[988.22 --> 996.08]  But if you connect with TLS 1.3 enabled, Nginx will poke our Go stack and ask if the Go
[996.08 --> 997.62]  stack wants to take over the connection.
[998.50 --> 1003.34]  And if it wants, it will just pass on the file descriptor and the rest of the connection
[1003.34 --> 1006.94]  will be passed through a Go reverse proxy.
[1007.80 --> 1010.38]  Does the Go stack get to have like a bad day?
[1010.56 --> 1012.64]  So can it say, you know, I'm just not interested today?
[1013.38 --> 1014.20]  Yes, yes.
[1014.34 --> 1016.74]  That was actually one of the like safeguards.
[1016.74 --> 1024.10]  I was like, you know, as a team of three people total on the crypto team, mostly me working on it.
[1024.16 --> 1029.74]  I'm not going to like take over the main Cloudflare reverse proxy.
[1029.74 --> 1038.60]  But like we have this nice fallback system where Go SSL can literally explode and only like open connections will suffer.
[1038.76 --> 1041.52]  Everything else will just downgrade to TLS 1.2.
[1042.06 --> 1042.40]  Nice.
[1042.40 --> 1045.64]  So I'm trying to follow the beginning of the conversation.
[1045.90 --> 1050.66]  Did you say that the crypto TLS package can be used in the place of open SSL?
[1051.32 --> 1051.48]  Yeah.
[1051.82 --> 1060.88]  You almost never, you essentially never use open SSL when you host a Go server that has HTTPS and TLS.
[1061.32 --> 1065.02]  You use the native Go implementation of TLS.
[1065.02 --> 1070.08]  And we build TLS 1.3 into it and we're looking to upstream it.
[1070.66 --> 1073.12]  So I know that open SSL has a lot of bugs.
[1073.64 --> 1081.78]  And would you recommend to people to use script TLS and use Go instead of using whatever they're using with open SSL?
[1082.34 --> 1084.26]  In your opinion, is it a lot better?
[1085.04 --> 1086.02]  Is it less buggy?
[1086.78 --> 1092.50]  So it's definitely like it has a better security track record at this point, we can say it.
[1093.12 --> 1094.52]  It's less battle tested.
[1094.76 --> 1098.94]  I think we are currently the widest deployment of it, I suspect.
[1099.80 --> 1100.98]  It did pass an audit.
[1101.42 --> 1102.50]  We paid for an audit.
[1102.70 --> 1103.30]  It passed.
[1104.34 --> 1110.86]  But let's say that if you are just putting Nginx in front of your site just to have open SSL in front of your site,
[1110.94 --> 1114.46]  but your site is a Go service, you should probably stop doing that.
[1114.66 --> 1115.24]  There's no need.
[1115.24 --> 1122.28]  If saying that I'm suggesting to actually go out of your way to remove open SSL by adding some Go in front,
[1122.90 --> 1125.90]  I mean, there are architectural decisions to be made there.
[1126.44 --> 1132.36]  Performance-wise, it's probably slightly slower or more CPU intensive, at least.
[1132.98 --> 1133.18]  Gotcha.
[1133.88 --> 1137.72]  And now, what does TLS 1.3 offer over 1.2?
[1138.12 --> 1140.62]  What was the motivation to kind of write that now?
[1141.10 --> 1142.60]  So it's twofold.
[1142.60 --> 1144.58]  There's better robustness.
[1144.86 --> 1150.06]  A lot of things that were creaky and we weren't really sure about were just removed.
[1150.06 --> 1157.88]  The policy was, if it doesn't have a very good reason to be in the protocol, cuff, cuff, heartbeat, cuff, cuff.
[1158.28 --> 1160.36]  It's not going to be in the protocol.
[1160.36 --> 1166.30]  And on the other hand, performance-wise, it cuts an entire round trip.
[1166.30 --> 1173.06]  So when you connect to a website, you first do the TCP handshake and that still happens.
[1173.60 --> 1182.88]  And then in TLS 1.2, you had to do two round trips to the server and back to the server and back before you could start sending real data on the connection.
[1182.88 --> 1185.42]  Now, with TLS 1.3, you do only one.
[1186.10 --> 1192.46]  You send the client, send something, the server responds, and we're ready to go with one less round trip.
[1192.92 --> 1199.36]  And round trips on mobile networks or in some countries, we are talking seconds sometimes.
[1200.02 --> 1207.70]  Yeah, I can see that, especially if it's a lot of connections kind of opening and closing rather than keep alive-based connections.
[1208.30 --> 1211.14]  There's a lot of added latency there for that additional round trip.
[1211.14 --> 1212.48]  Yeah, indeed.
[1213.08 --> 1216.30]  So is that mostly what you work on at Cloudflare is crypto?
[1216.92 --> 1220.80]  Yeah, these days I'm full-time on the crypto team.
[1221.34 --> 1224.18]  It's a young team that is growing.
[1224.56 --> 1225.46]  It's pretty fun.
[1225.64 --> 1229.98]  It's a research team that gets to actually deploy code to the world.
[1230.50 --> 1231.26]  It's fun, definitely.
[1231.26 --> 1241.44]  And for anybody who has not seen it, Filippo actually gave a talk at GopherCon last year about crypto and the different ciphers and things like that.
[1241.70 --> 1248.52]  And you closed that with some recommendations on which specifically to use and which not to use, if I recall.
[1248.52 --> 1253.66]  You might be mixing me up with George Dunkesley.
[1254.24 --> 1254.86]  Oh, that's right.
[1254.94 --> 1256.42]  Yeah, that was George that did that.
[1256.58 --> 1262.48]  But that's understandable because, I mean, not at the time, but in the meantime, he became a colleague of mine.
[1262.48 --> 1268.58]  And he's now the second member plus the manager of the Cloudflare crypto team.
[1269.18 --> 1273.80]  Well, I think that's because we were all up until 2 a.m. in one of your hotel rooms listening to those talks.
[1274.10 --> 1274.54]  Correct.
[1274.54 --> 1279.44]  So you did the Vigo talk.
[1279.94 --> 1282.12]  But yeah, we were all hanging out with doing it.
[1282.24 --> 1284.02]  Yeah, Filippo wrote the blog post.
[1284.42 --> 1284.76]  Yes.
[1285.30 --> 1289.38]  But by the way, I have to say, I'm extremely grateful for that talk rehearsal.
[1290.72 --> 1291.52]  That's good.
[1292.28 --> 1295.62]  But both you and, you know, you know who you are for everyone else.
[1296.10 --> 1301.28]  Yeah, it was me, Brian, Dave Cheney, who else?
[1301.28 --> 1301.68]  Yes.
[1302.24 --> 1302.54]  But yeah.
[1302.94 --> 1303.10]  Yeah.
[1303.18 --> 1304.78]  So living proof here.
[1305.04 --> 1305.20]  Yeah.
[1305.32 --> 1311.00]  If you want to rehearse early, we are always welcome to have people in our hotel rooms and rehearse.
[1311.62 --> 1314.46]  And by early, that means 2 a.m. the night before you're going to talk.
[1317.16 --> 1320.62]  That's part of the burden of being a GopherCon organizer.
[1320.62 --> 1325.06]  So I'll make two YouTube recommendations then.
[1325.38 --> 1327.80]  There's the one I'm just mistakenly confused.
[1328.02 --> 1332.38]  George Tankersley did the talk about crypto, but Filippo is just really good, too, about Sego.
[1332.90 --> 1333.36]  Yeah.
[1333.54 --> 1337.76]  The black magic of Sego and how you definitely shouldn't use it.
[1337.84 --> 1342.78]  But if you really, really, really have to, well, then this is how you can make it tolerable.
[1342.78 --> 1346.18]  That was the punchline.
[1347.38 --> 1349.00]  How to make Sego tolerable.
[1351.04 --> 1354.56]  Filippo does have a talk on TLS 1.3.
[1355.10 --> 1356.56]  Where did you give that talk?
[1357.18 --> 1363.16]  That would be 33C3, the Coast Computing Club conference in Hamburg.
[1363.16 --> 1368.36]  And, yeah, you can find it if you search for 33C3 TLS 1.3.
[1368.88 --> 1373.72]  There we go through all the crypto parts of this TLS 1.3 effort.
[1374.38 --> 1379.10]  And about the Go part, there's nothing published just yet.
[1379.64 --> 1384.52]  You can find a blog post on the Gopher Academy Advent list,
[1384.94 --> 1389.52]  which is a bunch of lessons learned from exposing Go server to the Internet,
[1389.52 --> 1394.38]  because that's effectively what we did with the Go reverse proxy.
[1395.06 --> 1399.94]  And the more crypto part, I don't know, I mean, maybe Gopher call?
[1400.60 --> 1402.08]  This is probably in bad taste.
[1402.32 --> 1403.00]  I'll shut up.
[1404.98 --> 1407.66]  I think somebody in the Gotime FM channel just said,
[1407.76 --> 1409.68]  I think everybody crashed your server.
[1410.72 --> 1412.34]  Oh, boy, did you?
[1413.04 --> 1413.52]  Oh, no.
[1414.04 --> 1416.84]  No, no, I think it's the HTTP part.
[1417.44 --> 1418.74]  Oh, yeah.
[1418.74 --> 1418.88]  Yeah.
[1419.52 --> 1421.32]  You can't SSH to an HTTP server.
[1421.70 --> 1422.10]  Oh, wait.
[1422.46 --> 1422.86]  Corey.
[1423.68 --> 1426.54]  Corey Lanoue trying to SSH into an HTTP server.
[1426.98 --> 1428.48]  Two different protocols there, Turbo.
[1429.56 --> 1430.66]  Hey, you never know.
[1432.96 --> 1433.84]  Copy the tweet.
[1433.94 --> 1435.18]  Oh, it's the tweets problem.
[1435.86 --> 1436.14]  Oops.
[1436.58 --> 1436.88]  Adam.
[1437.70 --> 1438.62]  Oh, that was Adam.
[1441.16 --> 1446.20]  So I think now is probably a good time to take our first sponsor break.
[1446.20 --> 1449.20]  And our first sponsor today is Stack Impact.
[1449.52 --> 1455.74]  When it comes to profiling and monitoring the performance of your Go applications,
[1456.20 --> 1460.44]  Stack Impact is a great service to help you and your team laser focus on hotspot profiling,
[1460.68 --> 1462.94]  bottleneck tracing, health monitoring, and more.
[1463.32 --> 1467.04]  Stack Impact gives you the necessary historical deep dive performance visibility
[1467.04 --> 1471.40]  into your Go application's execution so you can discover and resolve performance bottlenecks
[1471.40 --> 1472.90]  with line of code precision.
[1473.30 --> 1478.32]  Technically, Stack Impact makes Go's built-in profiling capabilities usable in a production
[1478.32 --> 1478.84]  environment.
[1479.18 --> 1480.84]  Stack Impact does everything automatically.
[1480.98 --> 1484.12]  There's no need to run commands or waste time specifying what to monitor.
[1484.36 --> 1487.50]  They've even put their Go agent on GitHub under the BSD license.
[1487.50 --> 1491.64]  So if you need to focus on the performance of your Go applications, check out Stack Impact.
[1492.06 --> 1496.60]  Head over to stackimpact.com slash GoTime to learn more and tell them Brian from GoTime
[1496.60 --> 1497.08]  sent you.
[1497.08 --> 1508.40]  We are back talking to Filippo about crypto and TLS and all the great things he's doing
[1508.40 --> 1509.46]  at Cloudflare.
[1510.18 --> 1512.94]  So what else are you working on these days?
[1512.94 --> 1517.06]  I know that you've had some interest in Caddy as well, and we've had Matt Holt on the show
[1517.06 --> 1517.42]  too.
[1517.42 --> 1518.78]  Oh, yeah, yeah.
[1518.88 --> 1520.90]  I mean, I like what Matt is doing a lot.
[1521.16 --> 1525.26]  And I planned to use Caddy for a little experiment of mine.
[1525.80 --> 1528.14]  Now, this is a complete, complete aside project.
[1528.80 --> 1534.24]  Something that I don't know if people realize or actually care about not being huge crypto
[1534.24 --> 1537.98]  nerds is that the Go binaries are completely reproducible.
[1538.16 --> 1545.36]  So if you take the same Go path, the same Go root, the same Go compiler, and the same code
[1545.36 --> 1552.94]  base, of course, and compile it on an OpenBSD machine and a completely different Linux machine
[1552.94 --> 1559.44]  and cross-compile them to the same target, the resulting binaries are identical, like
[1559.44 --> 1560.54]  byte by byte.
[1561.00 --> 1563.36]  And they will be forever, whoever builds that.
[1563.90 --> 1568.88]  Now, that's super nice because it means that you can take, for example, the Caddy build
[1568.88 --> 1573.40]  server, which is a nice server that does builds for you and gets you to this single binary
[1573.40 --> 1574.32]  that you can deploy.
[1574.76 --> 1580.58]  And you can prove that Matt is not an evil spy with a plan to conquer the world.
[1580.94 --> 1581.36]  Sorry, Matt.
[1582.08 --> 1588.36]  And you can reproduce the binary and prove that it matches what the build server builds.
[1588.36 --> 1590.20]  So you can prove there is no backdoor.
[1590.86 --> 1597.16]  So what I plan to do is to do the first experiment, reproducing the builds of Caddy, but then build
[1597.16 --> 1604.02]  some small tools to allow anyone to reproduce builds and publish signatures, maybe with key
[1604.02 --> 1606.84]  base to show that they match.
[1606.98 --> 1610.60]  Maybe even publish them to a key transparency log, which is like CT.
[1610.98 --> 1613.20]  But now I'm crypto nerding too hard.
[1614.16 --> 1615.10]  You lost me there.
[1615.20 --> 1615.72]  What's CT?
[1616.86 --> 1617.42]  Yeah.
[1617.52 --> 1619.38]  Sorry, that was too much of a tangent.
[1619.78 --> 1626.72]  CT is a way to get CAs, the ones that sign TLS certificates, more accountable by forcing
[1626.72 --> 1632.24]  them to disclose all the certificates they sign to a log where, long story short, they can't
[1632.24 --> 1634.18]  be hidden or removed.
[1634.60 --> 1640.62]  So you could use the same ideas to make a build server publish all the things it builds to
[1640.62 --> 1642.70]  a log where they can't be removed.
[1642.70 --> 1648.38]  So if they build something with a backdoor in it, it will show they can't hide it and
[1648.38 --> 1650.12]  only provide it to some people.
[1650.12 --> 1656.82]  And then you can prove it has a backdoor because it doesn't reproduce because you can't build
[1656.82 --> 1657.72]  it from another machine.
[1658.28 --> 1659.64]  Now, that's one step further.
[1659.88 --> 1661.26]  It's called binary transparency.
[1661.54 --> 1666.44]  It doesn't have that much to do with Go, but Go is a very good language to start this
[1666.44 --> 1671.68]  because getting reproducible builds is incredibly hard with anything else.
[1671.68 --> 1678.54]  Like the Debian project has been trying very hard to get the whole like dev repositories
[1678.54 --> 1682.96]  reproducible and they're jumping through hoops that you can imagine.
[1683.54 --> 1687.14]  With Go instead, you just set the same Go path and you're done.
[1687.76 --> 1687.86]  Yeah.
[1687.90 --> 1691.84]  I mean, you would just have to make sure you have the same Go tool chain, right?
[1692.24 --> 1696.82]  The right Go version, because theoretically it wouldn't be, you wouldn't produce the same
[1696.82 --> 1698.84]  binary if you upgraded your Go version.
[1698.84 --> 1699.52]  Yep.
[1699.76 --> 1704.16]  And I guess you would have to track the binary for each platform too.
[1704.58 --> 1704.80]  Yeah.
[1704.92 --> 1709.52]  Because the resulting binary would change for the Windows build versus the Linux build versus
[1709.52 --> 1711.32]  the ARM builder.
[1711.80 --> 1712.06]  Yeah.
[1712.16 --> 1717.84]  You have the whole matrix architectures and operating systems, but those are like, I don't
[1717.84 --> 1719.04]  know, 20 or something.
[1719.56 --> 1720.66]  It gets bigger every release.
[1720.74 --> 1721.38]  That's the best part.
[1722.04 --> 1722.64]  Yep.
[1723.16 --> 1726.34]  We're supporting 32-bit Spark on a Raspberry Pi now.
[1726.34 --> 1727.34]  32-bit Spark.
[1727.34 --> 1728.34]  32-bit Spark.
[1728.34 --> 1728.80]  32-bit Spark.
[1728.80 --> 1730.00]  Is there really 32-bit Spark?
[1730.38 --> 1731.70]  Not on a Raspberry Pi, no.
[1732.56 --> 1736.70]  No, I made that up, but it was apparently nowhere near as funny as it should have been.
[1737.34 --> 1738.88]  I'm like, you're confusing me here.
[1739.68 --> 1741.46]  I can run Go on my Deck Alpha.
[1741.58 --> 1742.00]  How's that?
[1744.56 --> 1745.78]  Break out the Commodore.
[1746.42 --> 1749.22]  I remember back in the days when a Deck Alpha was a big deal.
[1749.22 --> 1751.32]  I mean, not even joking.
[1751.44 --> 1753.12]  You can run Go on mainframes now.
[1753.82 --> 1753.92]  Yeah.
[1754.10 --> 1754.32]  Yeah.
[1754.72 --> 1754.98]  Yeah.
[1755.50 --> 1758.22]  It's just insane watching Go take off.
[1758.44 --> 1762.04]  It blows my mind in just a couple of years everywhere that we see Go.
[1762.56 --> 1769.46]  So you mentioned something in our show document about latency profiling and Camly Store too.
[1769.98 --> 1770.36]  Oh, yeah.
[1770.52 --> 1770.76]  Okay.
[1770.94 --> 1772.60]  So let's see.
[1773.04 --> 1774.66]  Let's go for spoilers first.
[1774.66 --> 1780.32]  But latency profiling is what I plan to talk about at Go4Con India.
[1781.08 --> 1787.76]  And essentially, the story there is that we are used to all the profiling tools, and they're super nice, super easy to use, right?
[1787.88 --> 1792.40]  And you can figure out what functions take the most CPU in your program.
[1792.96 --> 1794.04]  And that's nice, right?
[1794.72 --> 1801.20]  But then at the end of the day, you realize that that's not really what we are optimizing for most of the time.
[1801.20 --> 1806.52]  It's very hard to build an application that takes 100% of CPU.
[1807.10 --> 1809.30]  So what is it doing all the rest of the time?
[1809.82 --> 1811.68]  Well, it's blocking on something.
[1811.84 --> 1812.74]  It's waiting on something.
[1812.94 --> 1815.24]  And what metric does that worsen?
[1815.50 --> 1819.54]  Of course, latency, which a lot of the times is the one we care the most about.
[1819.54 --> 1827.20]  Like, it's rare that APIs are about throughput, about how many things concurrently they can process.
[1827.38 --> 1828.72]  It's absolutely possible.
[1829.20 --> 1832.34]  But like most of the times, but like this is debatable.
[1832.64 --> 1838.62]  But surely there is like a huge interest in reducing latency, making APIs return as quickly as possible.
[1838.62 --> 1846.70]  So Go does provide the tools to inspect what functions are slow, are just, you know, taking a long time.
[1847.08 --> 1852.20]  But they're not as well surfaced and publicized as their CPU counterparts.
[1852.20 --> 1865.54]  So they involve mostly the GoTracer, which can then generate profiles for blocking, for I.O., for network, and for scheduling poses.
[1866.04 --> 1869.08]  And these are the things that will actually make you, like, suffer.
[1869.24 --> 1874.98]  Imagine having some function somewhere that downloads, I don't know, a tarball from the Internet.
[1874.98 --> 1879.94]  That will not show up in the CPU profile, maybe, but it will take a long time.
[1880.12 --> 1883.00]  And if your API is blocking on that, it will take forever, right?
[1883.56 --> 1893.02]  Yeah, so that's actually really interesting because that debate comes up a lot, especially even talking about garbage collection, the difference between latency and throughput.
[1893.82 --> 1897.04]  You know, both of them kind of represent speed, right?
[1897.36 --> 1897.62]  Right.
[1898.02 --> 1901.30]  And deciding which one you want to optimize for is difficult.
[1901.96 --> 1902.96]  That's a very good point.
[1902.96 --> 1918.08]  Like, in Go, we almost explicitly stated that we optimize for latency by making the, at least in the garbage collector, by making it faster and faster in terms of poses, but slightly slower in terms of CPU and, you know, throughput.
[1918.60 --> 1923.84]  So it's interesting that the profiling tools haven't caught up to the same priorities.
[1924.52 --> 1924.64]  Right.
[1924.94 --> 1926.40]  Yeah, that's true.
[1926.64 --> 1928.98]  So you're talking about this at GopherCon India?
[1929.50 --> 1929.70]  Yeah.
[1929.96 --> 1930.66]  Yeah, that's the plan.
[1930.66 --> 1933.52]  Which is, that's coming up in February.
[1933.92 --> 1935.46]  I'm trying to remember the exact date.
[1936.00 --> 1937.20]  Does anybody remember a MoFan?
[1937.64 --> 1938.30]  I don't.
[1938.38 --> 1940.12]  February 21st?
[1940.60 --> 1944.66]  I mean, don't book tickets based on my collection, but...
[1944.66 --> 1948.18]  Check the website first before buying plane tickets in hotels.
[1949.40 --> 1950.66]  You might be early or late.
[1950.82 --> 1951.38]  24th.
[1951.56 --> 1952.48]  I was wrong.
[1953.14 --> 1953.78]  Like, right, right.
[1954.04 --> 1955.60]  21st, landing, 24th.
[1955.60 --> 1959.80]  Because you're Italian, I'm going to ask you, did you go to the GopherCon in Italy?
[1960.50 --> 1960.90]  Yeah.
[1961.30 --> 1961.60]  GoLab.
[1961.94 --> 1962.40]  GoLab.
[1962.80 --> 1963.36]  I'm sorry.
[1963.46 --> 1963.96]  Not GopherCon.
[1964.06 --> 1964.36]  GoLab.
[1964.70 --> 1964.88]  Yep.
[1964.98 --> 1966.56]  It was a very nice crowd.
[1966.94 --> 1968.82]  And my keynote was about Hello Gopher.
[1969.58 --> 1972.04]  It's actually like where I introduced the Hello Gopher.
[1972.44 --> 1974.50]  First time I showed it outside the Clouffer.
[1974.50 --> 1976.62]  Did they record the talks?
[1977.14 --> 1982.36]  So I'm not positive, but there is a recording of my screen and voice, which I usually take
[1982.36 --> 1983.04]  during talks.
[1983.72 --> 1987.48]  I've published it on my Twitter and on the video.
[1987.70 --> 1990.78]  I'll find you a link real quick and post it on the Slack.
[1991.04 --> 1991.40]  Awesome.
[1991.76 --> 1992.14]  There you go.
[1992.62 --> 1993.08]  Thank you.
[1993.62 --> 1997.80]  So Bill Kennedy just corrected us from the GoTime Slack.
[1998.08 --> 2000.30]  He said February 22nd to 25th.
[2000.52 --> 2001.50]  Now you can book tickets.
[2001.50 --> 2002.26]  Mm-hmm.
[2002.26 --> 2009.70]  So you guys want to talk about projects and news and interesting things that we've seen
[2009.70 --> 2010.34]  this week?
[2010.82 --> 2011.54]  There's been a lot.
[2012.20 --> 2012.46]  Yeah.
[2012.70 --> 2015.10]  The most fun one, I think, is the Gopher Eyes one.
[2015.84 --> 2016.24]  Absolutely.
[2017.06 --> 2017.28]  Mm-hmm.
[2017.82 --> 2018.90]  And Brian started it.
[2019.44 --> 2020.30]  Yeah, it's all my fault.
[2020.46 --> 2020.72]  Sorry.
[2021.16 --> 2022.68]  And apparently that's only the beginning.
[2022.88 --> 2023.32]  Every day.
[2023.50 --> 2025.08]  Every day, new things are getting added.
[2025.16 --> 2025.54]  That's right.
[2025.88 --> 2026.12]  Yeah.
[2026.18 --> 2027.26]  Ashley's kicking butt.
[2027.66 --> 2029.38]  So we should give the story behind that.
[2029.38 --> 2036.82]  If you go to gopherize, G-O-P-H-E-R-I-Z-E dot me, you can create your own Gopher avatar
[2036.82 --> 2039.24]  out of lots of different choices.
[2039.24 --> 2041.18]  And it's built for you live on the screen.
[2041.38 --> 2045.80]  It was built by Matt Reier with images supplied by Ashley McNamara.
[2046.44 --> 2051.10]  And the whole thing started because I asked Ashley for a custom Gopher avatar and then changed
[2051.10 --> 2052.76]  my avatar on Twitter.
[2052.76 --> 2055.74]  And then she made one for Eric and then she made one for Bill.
[2056.14 --> 2058.42]  And the next thing you know, the whole internet's asking for one.
[2058.58 --> 2062.74]  So they decided to just go make a site and give Ashley a break so she didn't have to make
[2062.74 --> 2064.12]  custom avatars for everybody.
[2064.72 --> 2066.42]  I have a request for Ashley and Matt.
[2066.86 --> 2069.74]  We need to have a t-shirt with the GoTime logo.
[2070.58 --> 2072.22]  Oh, we need a GoTime logo.
[2072.50 --> 2072.82]  Yeah.
[2072.94 --> 2077.28]  So they actually have a page there for companies to reach out if they want like a corporate
[2077.28 --> 2078.60]  logo on a shirt or something.
[2078.60 --> 2081.50]  So, but yeah, we do need a GoTime one.
[2081.66 --> 2082.78]  Why did I not think of that?
[2083.22 --> 2083.60]  I don't know.
[2083.94 --> 2088.98]  I was selecting the shorts and I was like, the GoTime is what I really want.
[2090.82 --> 2093.36]  So correct me if I'm wrong, though.
[2093.44 --> 2095.66]  I think the code base, it is written in Go.
[2095.76 --> 2100.10]  And I want to say it's based off of one of the Google holiday images or something.
[2100.44 --> 2101.36]  Yeah, the turkey.
[2101.90 --> 2102.28]  Remember that?
[2102.28 --> 2102.58]  Yeah.
[2102.82 --> 2103.96]  The Google turkey doodle.
[2104.36 --> 2105.04]  That's right.
[2105.62 --> 2106.92]  And that was all written in Go.
[2106.92 --> 2109.68]  And then this was kind of created based off of that.
[2109.80 --> 2111.80]  But yeah, a lot of fun.
[2111.86 --> 2113.74]  And I love hitting the randomized thing.
[2114.26 --> 2119.46]  And I also love like the key components based off of members of the community, like the Dave
[2119.46 --> 2120.28]  Cheney beard.
[2120.42 --> 2121.44]  Dave Cheney beard.
[2122.30 --> 2123.82]  And Ryan Kettleson hair.
[2124.46 --> 2125.74]  And Bill Kennedy hat.
[2125.78 --> 2126.24]  Bill hat.
[2126.70 --> 2127.02]  Yes.
[2128.68 --> 2129.66]  Great stuff.
[2130.90 --> 2132.42]  It's just too much fun.
[2132.42 --> 2137.18]  And I'm really looking forward to some of this stuff because this is only 24 hours, maybe,
[2137.38 --> 2138.72]  since it's gone live.
[2139.16 --> 2139.70]  If that.
[2140.28 --> 2142.02]  Yeah, more and more stuff keeps getting added.
[2142.26 --> 2143.78]  Just too much fun.
[2144.52 --> 2151.32]  So another cool project that I saw was, I guess it's Chrome DP would be the pronunciation
[2151.32 --> 2152.00]  of it.
[2152.00 --> 2158.94]  But basically able to steer browsers using the Chrome debugging protocol, which is written
[2158.94 --> 2159.32]  in Go.
[2159.44 --> 2163.42]  And for anybody who's suffered through like using Selenium and things like that, like
[2163.42 --> 2165.32]  this, this looks really cool.
[2166.04 --> 2166.58]  Ooh.
[2167.26 --> 2168.02]  Oh, God.
[2168.42 --> 2168.82]  Oh, God.
[2168.92 --> 2169.20]  Oh, God.
[2169.24 --> 2169.46]  Oh, God.
[2169.52 --> 2169.72]  Oh, God.
[2169.78 --> 2170.04]  Oh, God.
[2170.50 --> 2170.66]  Oh, God.
[2170.66 --> 2170.76]  No.
[2170.76 --> 2175.06]  Like the Camlistor thing is like, I'm, I'm a pack rat.
[2175.36 --> 2176.66]  I archive everything.
[2177.00 --> 2181.96]  And like, I, I, I'm trying to archive everything into Camlistor, which is like this content address
[2181.96 --> 2184.66]  storage that we don't really have time to talk about.
[2184.72 --> 2191.16]  But the point is something I wanted was like load pages into a real headless browser and
[2191.16 --> 2194.56]  then like take snapshots of them and archive those.
[2195.24 --> 2196.66]  And oh, God, oh, God, oh, God, oh, God, oh, God.
[2197.34 --> 2197.74]  Wow.
[2197.74 --> 2198.86]  Problem solved.
[2198.86 --> 2200.86]  Oh, God.
[2201.42 --> 2205.06]  At this point, I'll just drop off the call and start hacking with this.
[2205.40 --> 2206.22]  So sorry.
[2206.34 --> 2206.52]  Bye.
[2207.14 --> 2208.10]  It'll be hacking now.
[2208.22 --> 2208.40]  Sorry.
[2208.48 --> 2208.82]  I got to go.
[2209.40 --> 2214.72]  So if you are on the road and not able to pull up this project, basically, you can steer
[2214.72 --> 2215.24]  the browser.
[2215.44 --> 2220.04]  You can tell it to click inputs with basically like jQuery, like selectors.
[2220.18 --> 2221.64]  You can tell it to sleep.
[2222.12 --> 2224.20]  You can take screenshots using it.
[2224.20 --> 2227.76]  And this is all kind of written in Go, which is just a ton of fun.
[2227.76 --> 2233.00]  So and yeah, I mean, integration tests actually steering the browser of your app.
[2233.64 --> 2234.42]  Huge win.
[2235.22 --> 2236.54]  Anybody else have anything fun?
[2237.38 --> 2238.18]  Oh, where's my list?
[2238.26 --> 2239.46]  I have a million things.
[2239.46 --> 2245.78]  So I want to give a shout out to the pre-alpha dep tool.
[2246.12 --> 2251.70]  The team that is working on giving a blessed answer to how do you fill your vendor folder
[2251.70 --> 2257.76]  has published like a first tool that uses this library called GPS, which is meant to become
[2257.76 --> 2261.80]  like the shared backend for all the rendering tools.
[2261.80 --> 2263.34]  If my understanding is correct.
[2263.50 --> 2265.52]  I have like no affiliation to that.
[2265.62 --> 2268.90]  But having like the LGBT, I know how much pain is involved.
[2269.08 --> 2270.54]  So huge shout out.
[2271.12 --> 2271.26]  Yeah.
[2271.32 --> 2274.58]  So we're going to try to get Sam Boyer on the show.
[2275.08 --> 2279.14]  We've actually been communicating right now while we're on this call.
[2279.14 --> 2284.26]  So hopefully in the next couple episodes, we will actually get him on and talk about this
[2284.26 --> 2286.34]  tool and some of the stuff going on behind the scenes.
[2286.46 --> 2288.34]  I'm really looking forward to that.
[2288.64 --> 2293.84]  Also because like, I don't know how related it is, but like part of the idea of HelloDouffer
[2293.84 --> 2302.02]  is to just show a user flow that users like or need and eventually get that user flow into
[2302.02 --> 2302.88]  the standard tooling.
[2302.88 --> 2311.42]  And I've seen Raskox 2017 resolutions and one of them was making sure that work outside
[2311.42 --> 2314.04]  GoPath worked as well as inside GoPath.
[2314.46 --> 2322.10]  And it had some remark like, make sure that users can get clone CD and just go build a
[2322.10 --> 2325.10]  project and literally match the HelloGopher tagline.
[2325.30 --> 2326.64]  So I was super happy about that.
[2327.14 --> 2331.80]  But it makes us come full circle because when I started Go back in NOM, we had to use make
[2331.80 --> 2332.80]  files then too.
[2332.88 --> 2336.20]  Yeah, I remember the make files.
[2337.10 --> 2340.16]  So it's kind of interesting circling back.
[2342.06 --> 2344.56]  But I mean, make is super powerful though, too.
[2344.64 --> 2346.64]  So I can't really hate using make files.
[2347.24 --> 2349.12]  I mean, I put make files in everything.
[2349.46 --> 2355.14]  It's for me, it's more of not being a workflow, but being a recipe for what you expect people
[2355.14 --> 2356.22]  to do with your application.
[2356.22 --> 2360.54]  You know, and my make file may just say, go build under make build.
[2360.54 --> 2368.24]  But it more often has very explicit directions in each recipe on what needs to be done.
[2368.36 --> 2373.40]  So I think it's its own form of documentation that's more canonical for each project.
[2373.40 --> 2374.40]  Yeah.
[2374.40 --> 2381.60]  And I mean, I put like handy development and deployment type scripts in my make file, basically.
[2381.80 --> 2385.26]  So they don't have to have like a directory of like utility scripts for like bootstrapping
[2385.26 --> 2389.10]  the environment or, you know, building the container or things like that.
[2389.16 --> 2392.80]  You don't have to node CD into this directory or run this Docker command or something.
[2392.80 --> 2396.02]  You just, you know, make a container or whatever.
[2396.72 --> 2397.06]  And yeah.
[2397.78 --> 2399.78]  And they're extremely standard.
[2400.12 --> 2404.56]  So, you know, you're making any developer feel at home because they've seen make files
[2404.56 --> 2404.88]  before.
[2405.38 --> 2405.54]  Yeah.
[2405.58 --> 2407.14]  Or something very close to it.
[2407.74 --> 2410.86]  I don't know if feeling at home is the right way to say it because I never feel at home in
[2410.86 --> 2411.20]  a make file.
[2411.28 --> 2414.22]  I've seen some make file ninjas, but I am not one of them.
[2414.78 --> 2415.04]  Yeah.
[2415.16 --> 2416.46]  It amazes me.
[2416.54 --> 2419.98]  Some of the stuff people know about make it is ridiculously powerful.
[2419.98 --> 2424.90]  My knowledge of make is like about equivalent to my knowledge of bash.
[2425.08 --> 2426.96]  It's like just enough to make it work.
[2427.78 --> 2430.26]  Look, I work with John Garhan coming.
[2430.64 --> 2430.92]  Okay.
[2431.52 --> 2434.36]  He wrote the book on the GNU make.
[2434.74 --> 2435.58]  He wrote the book.
[2435.90 --> 2436.40]  Hello Gopher.
[2437.08 --> 2439.40]  Hello Gopher required him at some point.
[2440.24 --> 2440.62]  So like.
[2440.86 --> 2441.26]  That's awesome.
[2441.44 --> 2441.68]  Yes.
[2441.80 --> 2443.40]  Like at some point I was like, no, no, no.
[2443.44 --> 2444.10]  This is enough.
[2444.20 --> 2445.68]  I'm like, just where's John?
[2446.34 --> 2446.50]  Yeah.
[2446.50 --> 2448.70]  Just bring your book over here and tell me what I'm doing wrong.
[2449.40 --> 2449.84]  Yep.
[2449.98 --> 2452.64]  And no, he actually pulled the page out of his book.
[2453.04 --> 2454.92]  He actually literally did that.
[2455.60 --> 2456.30]  Oh, that's awesome.
[2457.22 --> 2463.92]  Oh, see, like, so I've gotten beaten up in some code reviews before, but has anybody ever,
[2464.04 --> 2467.80]  aside from you, like ever gotten beaten up about a make file?
[2468.54 --> 2470.74]  Like, did somebody destroy your make file?
[2470.84 --> 2471.80]  Like, no, don't do that.
[2471.86 --> 2472.74]  You should have done this.
[2472.74 --> 2478.44]  Usually the make file and the review is just like, if it works, leave it.
[2479.10 --> 2483.66]  I'm not brave enough to submit a make file to anybody who would understand how to review it.
[2484.10 --> 2484.98]  It would be ugly.
[2484.98 --> 2491.22]  My make file always consists of copy from someone that works and paste into my project.
[2491.68 --> 2492.12]  Yeah.
[2492.84 --> 2493.72]  Copy pasta file.
[2494.04 --> 2495.78]  I feel like it's just like bash.
[2495.90 --> 2499.80]  Every time I got to do something, I got to look up, you know, how do you do a for loop and bash again?
[2499.80 --> 2510.00]  Oh, so I think it is about time for our second sponsor break, and then we'll get into some more projects and news.
[2510.72 --> 2515.40]  Our second sponsor today is actually Arden Labs with their Ultimate Go training series.
[2517.44 --> 2523.28]  Our friends at Arden Labs offer some of the best training classes for Go, web, and data science folks.
[2523.44 --> 2527.48]  They've trained over a thousand students from all over the world over the past two years.
[2527.48 --> 2533.90]  They offer corporate training in Go, web, and data science taught by Bill Kennedy, Daniel Whitenack, and John Gossett.
[2534.30 --> 2539.30]  Bill wrote the Go in Action book, and all three have given talks at conferences and events all over the world.
[2539.58 --> 2544.58]  They offer two and three full-day intensive courses that literally take any developer to a whole new level.
[2544.98 --> 2551.64]  The classes teach specification, implementation, mechanics, guidelines, and best practices with a lot of personal experience.
[2551.64 --> 2557.44]  They also provide a high-energy environment to keep those involved excited and focused throughout the class.
[2557.48 --> 2561.24]  Even your most experienced developers will get something out of every class.
[2561.56 --> 2566.58]  To learn more, head to ArdenLabs.com slash GoTime and tell them Eric from GoTime sent you.
[2570.58 --> 2574.42]  All right, and we are back talking to Filippo.
[2574.66 --> 2580.30]  For anybody who is listening live, we were just kind of joking about makefiles and the use of phony
[2580.30 --> 2583.42]  and how it makes Brian feel like a phony when he reads it.
[2583.42 --> 2585.54]  No, it doesn't make...
[2585.54 --> 2588.16]  It means my makefile is declaring itself as phony.
[2588.24 --> 2589.72]  My makefiles have imposter syndrome.
[2590.38 --> 2590.82]  Ah.
[2591.60 --> 2593.64]  Does anybody have Twitter open right now?
[2594.54 --> 2600.84]  I literally see like a nonstop stream of people and their gopher versions of themselves.
[2603.18 --> 2604.56]  Everybody's getting gopherized.
[2605.40 --> 2606.16]  That's awesome.
[2606.64 --> 2607.40]  Just priceless.
[2607.40 --> 2608.40]  All right, so...
[2609.40 --> 2615.70]  Imagine being someone that doesn't do Go and everyone around you on Slack and Twitter and
[2615.70 --> 2622.98]  everything else starts turning into these weird avatars and you feel like you're outside of the joke or the conspiracy.
[2622.98 --> 2623.12]  See?
[2624.04 --> 2638.82]  That's actually happened to me a couple of times for like political reasons where like I'll just get on one day and like everybody has like they're now a cartoon character or, you know, they've changed their avatar to a flag and I haven't yet read the news yet to see why people are doing that.
[2638.94 --> 2641.78]  Like, why is everybody a cartoon character today?
[2641.88 --> 2642.90]  Like, what did I miss?
[2643.54 --> 2644.38]  You also left out.
[2644.88 --> 2646.48]  There's an entire subreddit for that.
[2646.60 --> 2647.96]  It's called Out of the Loop.
[2648.70 --> 2649.56]  Oh, nice.
[2649.56 --> 2662.58]  You have to go there and there are people that are like, yes, so these are the things that happened that could make you feel out of the loop or you can just ask and people will be like, oh, yeah, that's a meme from 2013 that started in this thread.
[2663.90 --> 2666.92]  See, these are people that don't have 14 year olds living in their house.
[2667.30 --> 2667.60]  Correct.
[2669.12 --> 2672.26]  If you had a 14 year old living in your house, they know everything.
[2672.94 --> 2676.48]  I have an eight year old in my house that thinks I'm dumb.
[2677.34 --> 2678.72]  Like, he knows everything.
[2679.56 --> 2681.68]  So I think it's just kids.
[2682.30 --> 2683.92]  They try to shock you.
[2684.08 --> 2684.64]  You're like, yep.
[2685.32 --> 2686.92]  No, I didn't know that.
[2688.86 --> 2691.50]  OK, so any other interesting projects?
[2692.08 --> 2697.26]  Oh, I found a really cool plugin for Kubernetes called Mate.
[2697.40 --> 2703.86]  It's at github.com slash Z-A-L-A-N-D-O dash incubator slash mate.
[2703.86 --> 2711.12]  And it does DNS and load balancing for Amazon cloud services and GCS.
[2711.60 --> 2716.66]  And the thing that's really cool about it is that it will manage your Route 53 DNS for you, too.
[2716.82 --> 2720.98]  And it will also create named endpoints in your load balancer.
[2720.98 --> 2731.88]  So if you've got a Kubernetes service called www and you expose it using mate, it will create www.yourdomain.com and in the load balancer.
[2732.12 --> 2734.92]  And then it will also fix DNS to point to those load balancers.
[2734.92 --> 2742.64]  So it's taking Kubernetes load balancing and endpoints to their logical extreme when you're on AWS and GCP.
[2743.06 --> 2744.96]  And it's written in Go and it's really cool.
[2745.02 --> 2745.80]  I can't wait to try it out.
[2745.80 --> 2746.96]  It looks really cool.
[2747.16 --> 2751.30]  So the load balancers assume to already be set up with a public IP address.
[2751.54 --> 2753.90]  And this is just routing new DNS names of that?
[2754.00 --> 2755.62]  No, it creates the load balancer.
[2755.88 --> 2757.20]  It does it all.
[2757.46 --> 2765.36]  OK, so it creates a load balancer with a public IP and then load balances to the private IPs of Kubernetes.
[2766.06 --> 2766.26]  OK.
[2766.32 --> 2766.70]  You got it.
[2767.24 --> 2768.10]  That's awesome sauce.
[2768.68 --> 2768.88]  Yeah.
[2769.34 --> 2771.76]  I mean, it's a common question people have, right?
[2771.78 --> 2774.82]  Like, how do they get this thing exposed publicly?
[2774.82 --> 2777.80]  So, yeah, that's that's pretty sweet.
[2778.46 --> 2779.24]  Yeah, very nice.
[2779.70 --> 2783.04]  Or in Kelsey Hightower rating, it's super dope.
[2783.48 --> 2784.40]  It's super dope.
[2784.92 --> 2786.12]  It's super dope.
[2787.40 --> 2788.98]  Hopefully, Kelsey doesn't sue me.
[2789.04 --> 2790.82]  He's a friend, but you never know.
[2792.08 --> 2793.58]  I'm going to I'm going to tweet that.
[2795.02 --> 2796.62]  Yeah, I have a project.
[2797.10 --> 2797.82]  I'm sorry.
[2797.92 --> 2798.44]  Were you done?
[2798.92 --> 2802.20]  No, I was going to I was going to ask if you ran across anything you wanted to talk about.
[2802.94 --> 2803.80]  I did.
[2803.80 --> 2811.76]  So Sourcegraph is now in general availability with the Go language.
[2812.66 --> 2821.04]  And for people who don't know, Sourcegraph is like a code navigation tool, but you use it on your browser.
[2821.04 --> 2828.72]  And the cool thing over all the normal code navigation tools is that it will take you across repos.
[2828.72 --> 2836.52]  And if you go to a function, for example, you can see where it is used in the entire GitHub universe.
[2837.14 --> 2841.82]  And I think even in other source control systems, maybe GitLab.
[2841.96 --> 2844.26]  I'm not sure about that, but GitHub definitely.
[2844.26 --> 2846.14]  And that is super cool.
[2846.88 --> 2853.38]  For example, when I am looking for when I run into something new and I want to see how people are using it.
[2853.38 --> 2858.54]  I just use Sourcegraph and I'm able to see it.
[2859.02 --> 2865.62]  And it also gives you Git plane and it gives you the last time the file was updated and a bunch of other awesome things.
[2866.20 --> 2867.84]  Yeah, I love their interface.
[2867.84 --> 2872.68]  I use it all the time also building the studying the TLS crypto library.
[2872.96 --> 2874.46]  It works on the standard library too.
[2874.92 --> 2880.82]  And you can just like click around and click to jump to definition, which is something that I always wanted.
[2880.82 --> 2890.00]  There used to be a web interface to what is now called the Guru, which was called ETA maybe or something like that.
[2890.08 --> 2895.52]  Anyway, but yeah, Sourcegraph does that and it's wonderful just clicking around too.
[2896.38 --> 2899.08]  Yeah, so it will work with anything that's open source.
[2899.30 --> 2905.38]  And if you want to use on your private repos, they have a pricing structure there.
[2905.94 --> 2909.88]  You probably need to talk to your security team, find out if you can do it.
[2909.88 --> 2914.56]  Yeah, I would assume it runs on on-prem or something like that for that.
[2914.78 --> 2915.78]  I'm not really sure.
[2916.44 --> 2919.42]  But yeah, I mean, they have a browser extension that's cool too.
[2919.54 --> 2926.72]  So even if you're just kind of like browsing around GitHub looking, you can just kind of click and follow along and jump to definition.
[2927.14 --> 2933.50]  And one of the things I love is being able to see examples of where this is used in other repos.
[2933.74 --> 2939.28]  Like that's always really useful to me, especially if the project itself doesn't have a lot of documentation on the usage.
[2939.88 --> 2943.90]  Of the library, you can kind of follow along and see projects that are using it.
[2944.16 --> 2944.38]  Yeah.
[2944.84 --> 2947.74]  It's like Stack Overflow without the stack.
[2948.62 --> 2954.08]  It's hard to explain how good and useful it is, but you have to use it.
[2954.12 --> 2954.96]  It's one of those things.
[2955.22 --> 2959.12]  And I know the next one you are particularly excited about, Brian.
[2959.78 --> 2960.58]  Which one's that?
[2961.58 --> 2962.50]  The...
[2962.50 --> 2963.36]  Play with Docker?
[2963.36 --> 2964.60]  Yeah, play with Docker.
[2965.00 --> 2966.20]  Yeah, this one's really cool.
[2966.38 --> 2969.60]  So I found out about this just the other day.
[2969.82 --> 2971.66]  And I'm going to kill poor Marcus's name.
[2971.76 --> 2972.08]  I'm sorry.
[2972.78 --> 2974.56]  Marcos Liljadal?
[2974.86 --> 2975.86]  I'm not sure.
[2976.06 --> 2981.26]  But on GitHub, it's F-R-A-N-E-L-A, Frenella, github.com slash Frenella.
[2981.78 --> 2984.20]  And there's a project called Play with Docker.
[2984.20 --> 2992.08]  And it embeds a Docker in Docker instance and then allows you to connect to it from a web browser.
[2992.66 --> 3002.06]  And inside the web browser, you have up to five Docker terminals embedded in Term.js or Xterm, whatever, terminal in your web browser.
[3002.16 --> 3008.02]  So you can have embedded terminals in your web browser that are backed by a Docker in Docker system,
[3008.02 --> 3015.38]  which means if you've got five terminals, they're all in the same network and you can do cool things like create Kubernetes clusters in your web browser.
[3016.40 --> 3017.78]  Wow, that's brave.
[3018.08 --> 3019.86]  And I get excited by that kind of stuff.
[3020.44 --> 3023.88]  And of course, it's open source and all written in Go and I've already forked it.
[3026.48 --> 3027.64]  We know what that means.
[3029.72 --> 3031.88]  Something new and fun is going to come out of this.
[3032.48 --> 3034.94]  It's going to be very prolific in the next few days.
[3035.62 --> 3036.10]  All right.
[3036.10 --> 3041.88]  So did anybody come across anything else, any new news, or do we want to jump into Free Software Friday?
[3042.68 --> 3043.54]  It's time for the hashtag.
[3044.12 --> 3044.52]  All right.
[3045.60 --> 3048.52]  So you actually added something, Filippo.
[3048.64 --> 3050.42]  So yeah, we tend to fill everybody in.
[3050.86 --> 3059.44]  We typically every week do a Free Software Friday where we shout out to projects and or maintainers of open source projects that are making our lives easier.
[3059.80 --> 3061.28]  They don't necessarily have to be Go.
[3061.40 --> 3062.54]  They just have to be open source.
[3063.02 --> 3064.34]  So who wants to start this week off?
[3064.34 --> 3070.32]  I'll give it a start because I had a busy weekend this weekend putting out the GopherCon website.
[3071.04 --> 3075.58]  And these are two projects that I've probably talked about before, but I used them together.
[3075.58 --> 3081.62]  And it turned out to be a peanut butter and chocolate sort of situation where everything just tasted better.
[3081.62 --> 3084.64]  So I used the new Ponzu CMS.
[3084.90 --> 3088.56]  And I think we talked a little bit about that on the interesting projects last week.
[3089.02 --> 3090.08]  I didn't waste any time.
[3090.16 --> 3092.18]  I just put it in production at GopherCon.com.
[3092.18 --> 3095.64]  And it's backed by a Buffalo website.
[3096.12 --> 3099.46]  So the combination of those two together is absolutely amazing.
[3100.00 --> 3102.64]  Ashley McNamara did the design and the images.
[3103.20 --> 3105.62]  And I built the code side of it.
[3105.84 --> 3107.50]  And we put up the GopherCon site.
[3107.80 --> 3110.86]  Well, it was kind of up before, but not really up.
[3110.86 --> 3114.30]  And we made it a real site in just a weekend.
[3114.62 --> 3115.62]  And it was really awesome.
[3115.90 --> 3119.20]  I strongly encourage you to take a look at that combination.
[3119.98 --> 3124.88]  And to make it just a little bit easier for myself, I built a code generator called Ponzi.
[3125.24 --> 3130.50]  So under my GitHub repository, bkettleson slash ponzi and bkettleson slash ponzi gen.
[3131.44 --> 3134.00]  Because Brian can't build anything without a generator.
[3134.34 --> 3134.50]  Yeah.
[3134.52 --> 3136.34]  If you're not generating code, you're doing it wrong.
[3136.34 --> 3146.66]  So while we're mentioning the GopherCon site, this episode will probably be released just before the CFP closes.
[3146.96 --> 3153.62]  So if you're listening to this now and you want to see your face on that website, it's probably going to be your last moment to race.
[3154.04 --> 3157.68]  Along with the 200 other people who are going to submit in the last 48 hours.
[3158.18 --> 3159.84]  The organizers are great.
[3160.12 --> 3163.54]  And you can just ask them to rehearse in their room the night before.
[3164.30 --> 3164.90]  And it works.
[3165.54 --> 3165.74]  Yeah.
[3166.34 --> 3166.78]  All right.
[3166.86 --> 3167.82]  Carlisa, do you have anything?
[3168.32 --> 3169.58]  I don't have anything today.
[3170.26 --> 3170.54]  All right.
[3170.58 --> 3171.36]  How about you, Filippo?
[3171.88 --> 3172.10]  Yeah.
[3172.36 --> 3181.60]  So my shout out is for, I'm not sure the pronunciation, but Dominic Honef, hopefully, who makes a static check.
[3181.76 --> 3189.46]  Static check is like a wider version of GoVet that does static analysis and looks for like things that are clearly wrong.
[3189.90 --> 3193.02]  Aiming for, you know, low or zero false positives.
[3193.02 --> 3196.78]  I run it across all the good bases I could find at CloudFer.
[3196.78 --> 3207.52]  And I think I found one false positives, two real bugs and a bunch of like things that happen not to be a bug only because we are lucky.
[3207.52 --> 3209.52]  So it's a great tool.
[3209.52 --> 3219.06]  And every time I open an issue suggesting it would be nice if static check did this, being, you know, the usual entitled open source community member.
[3219.06 --> 3225.80]  He actually goes out of his way and implements stuff in like, I don't know, 48 hours is my experience.
[3226.24 --> 3227.48]  So, yeah, it's great.
[3227.48 --> 3232.80]  It's a fantastic tool to run on your code base before committing, for sure.
[3233.02 --> 3234.76]  And it only continues to evolve.
[3235.34 --> 3238.64]  And I guess that's largely thanks to you antagonizing him.
[3238.68 --> 3239.04]  Right.
[3239.04 --> 3249.34]  I did notice in the Golang dev mailing, no, Golang nuts mailing list, one of the Golang mailing lists that they're changing the import paths of those.
[3249.46 --> 3256.90]  So if you rely on those, double check your repository locations because I know that he just renamed them.
[3257.38 --> 3257.74]  Oh, nice.
[3258.00 --> 3259.46]  A little plug here.
[3259.84 --> 3264.52]  Florin and the GoTime FM channel also just listed as Patreon.
[3265.12 --> 3265.74]  How do you pronounce it?
[3265.78 --> 3266.30]  Patreon?
[3266.54 --> 3266.88]  Patreon.
[3267.22 --> 3267.48]  Patreon.
[3267.48 --> 3268.94]  Patreon account.
[3269.04 --> 3271.22]  If you want to support Dominic's work.
[3271.76 --> 3272.32]  Oh, that's awesome.
[3272.82 --> 3273.24]  Please do.
[3273.34 --> 3273.74]  Yes, definitely.
[3273.84 --> 3280.12]  Think of how many cycles it will save to your developers and, you know, just consider the dollar amount of that.
[3280.68 --> 3283.58]  That's actually what I did for the Patreon for VimGo.
[3283.98 --> 3294.86]  So I took the amount of money I would pay on a commercial IDE and I just kind of averaged out, you know, two or three hundred dollars a year license for a commercial IDE and divided it by 12.
[3294.86 --> 3296.80]  And that's that's how much I give VimGo every month.
[3297.06 --> 3297.18]  Yep.
[3297.32 --> 3298.52]  Because it makes me happy.
[3299.04 --> 3300.60]  That's actually a good way to look at it.
[3301.32 --> 3301.84]  All right.
[3301.84 --> 3306.76]  So my project this week is by someone named Matt Hamilton and it's called Zim.
[3307.40 --> 3315.64]  So I've been like a ZSH user for a long time and I've kind of gone through like, oh, my ZSH and ZPresto and all that.
[3315.86 --> 3321.54]  And it's hard because you love these things and then your shell kind of gets more and more bloated.
[3321.54 --> 3327.26]  But Zim actually is really cool and has a bunch of different modules for stuff and super fast.
[3327.26 --> 3334.98]  So you get a lot of the same features with like the get branch info and all that stuff in your PS1 without kind of the lag.
[3335.28 --> 3337.46]  Some of the other ones have recently started gaining.
[3337.98 --> 3339.36]  So super cool project.
[3339.36 --> 3341.28]  I love having a sparkly PS1.
[3341.40 --> 3347.16]  But the last time I used all my ZSH, it blew up something and I can't remember what it blew up, but it was bad.
[3347.64 --> 3349.82]  It was enough where you switched like straight back.
[3350.54 --> 3354.24]  We've got breaking news live from the GoTime FM channel.
[3354.50 --> 3358.20]  Go 1.7.5 and Go 1.8 RC3 are out.
[3358.42 --> 3358.72]  Nice.
[3358.92 --> 3359.96]  Fire up your downloaders.
[3359.96 --> 3365.64]  Remember that there is the wonderful GoGet way to download the RCs.
[3365.94 --> 3367.20]  I absolutely love that.
[3367.74 --> 3367.86]  Yeah.
[3367.98 --> 3382.90]  And with 1.8 being right at the five yard line, 1.9 discussions have started to, I think it was a Golang Nuts thread that Brad Fitzpatrick started about discussions for things that are going to take place in 1.9.
[3383.16 --> 3388.20]  So we will link to that in the show notes if you want to be involved in those conversations too.
[3388.20 --> 3392.34]  I think more interesting than Go 1.9 is Go 2.0 discussions.
[3392.94 --> 3394.02]  Those will be interesting.
[3394.82 --> 3396.14]  They will be very interesting.
[3396.66 --> 3397.24]  Stay tuned.
[3397.76 --> 3400.02]  I think we're getting generics and ponies.
[3403.46 --> 3405.52]  There'll be some unicorns.
[3405.60 --> 3405.84]  Yep.
[3407.50 --> 3409.16]  And a JVM backend.
[3409.76 --> 3410.74]  And a JVM backend.
[3413.12 --> 3415.80]  Remember there was a Go JVM backend in the beginning.
[3416.14 --> 3417.60]  I don't even remember that.
[3417.60 --> 3418.06]  Was there?
[3418.42 --> 3418.88]  There was.
[3418.94 --> 3422.84]  There was a Go cross compiler or Go something.
[3423.06 --> 3424.28]  Go JVM backend.
[3424.52 --> 3426.02]  But it was really early.
[3427.00 --> 3430.24]  And I don't remember it working very well at all.
[3430.72 --> 3432.30]  And they just kind of fizzled.
[3432.54 --> 3439.12]  I wonder if you could still do that through either GCC Go or CLang backends.
[3439.12 --> 3443.58]  You can do lots of stuff with LLVM and CLang.
[3443.76 --> 3444.62]  So yeah.
[3444.72 --> 3447.46]  I know that's how Gopher.js is getting a lot of things done.
[3447.76 --> 3447.86]  Yep.
[3448.20 --> 3453.48]  Speaking of GCC Go, does anybody know how widely used that is?
[3454.20 --> 3454.60]  No.
[3455.14 --> 3455.32]  Yeah.
[3455.36 --> 3455.78]  Me either.
[3455.78 --> 3457.90]  It seems to be still maintained.
[3457.90 --> 3463.36]  But I haven't really heard much about it or any particular projects using it.
[3463.50 --> 3464.58]  So it'd be interesting.
[3464.92 --> 3465.12]  All right.
[3465.24 --> 3466.08]  Maybe Ian knows.
[3466.22 --> 3471.04]  Ian Lance Taylor, if you're out there, we need to know who's using GCC Go and where and
[3471.04 --> 3471.34]  why.
[3471.88 --> 3475.14]  So this is an open invitation to come on the show and talk to us about GCC Go.
[3475.78 --> 3476.24]  That's true.
[3476.32 --> 3477.92]  We should get him on the show and talk about it.
[3478.90 --> 3481.80]  Which reminds me of an embarrassing moment at the first Gopher Con.
[3481.84 --> 3482.78]  This is totally an aside.
[3483.22 --> 3487.10]  Somebody walked up to me and said they were using GCC Go and they had this big problem
[3487.10 --> 3488.84]  and they didn't know what to do or how to fix it.
[3489.06 --> 3492.78]  So I just walked over to Ian and I said, hey, Ian, somebody's got a GCC Go problem.
[3492.84 --> 3493.42]  Can you help him out?
[3493.46 --> 3494.04]  And he's like, sure.
[3494.28 --> 3495.48]  And I said, that guy right there.
[3496.20 --> 3496.84]  That's kind of fun.
[3497.74 --> 3498.40]  That's what I do.
[3498.40 --> 3499.78]  I put people together.
[3499.78 --> 3505.80]  At the last Gopher Con, I had a bit of embarrassing moment when I discovered after the fact that
[3505.80 --> 3512.30]  one of the questions that I kind of quickly answered slash brushed off at my C-Go talk
[3512.30 --> 3513.50]  was from Ian.
[3514.82 --> 3517.38]  So yeah, I felt pretty bad about that.
[3518.10 --> 3523.48]  Who was it we were at the speaker's dinner and they were sitting next to Dimitri?
[3523.94 --> 3524.78]  Oh, shush.
[3525.02 --> 3526.14]  We don't need to bring this up.
[3526.76 --> 3528.04]  No, no, no, no, no.
[3528.04 --> 3529.30]  That was me.
[3529.78 --> 3530.82]  No, no, no, no.
[3530.90 --> 3534.42]  It was one of the other speakers was talking about the race detector.
[3535.26 --> 3536.96]  And Dimitri was just like, thank you.
[3539.56 --> 3540.76]  All right.
[3540.76 --> 3544.70]  Did anybody have any other projects or news they want to talk about before we wrap this
[3544.70 --> 3545.06]  thing up?
[3545.58 --> 3546.20]  We hit it all.
[3546.72 --> 3547.14]  All right.
[3547.48 --> 3548.00]  Good work.
[3548.42 --> 3548.90]  Well, huge.
[3548.98 --> 3550.86]  Thank you to everybody on the show.
[3551.10 --> 3553.24]  Thanks to all the listeners listening right now.
[3553.76 --> 3556.92]  Huge shout out to our sponsors, Stack Impact and Arden Labs.
[3556.92 --> 3558.90]  If you haven't checked them out, please do.
[3559.24 --> 3561.10]  We will put links in the show notes.
[3561.74 --> 3564.68]  Definitely share this show with friends and colleagues.
[3565.24 --> 3568.54]  Easy way to subscribe is to go to gotime.fm.
[3569.10 --> 3571.70]  We will have a weekly email coming out shortly.
[3571.70 --> 3573.26]  So go ahead and get signed up to that.
[3573.40 --> 3575.10]  We are gotime.fm on Twitter.
[3575.66 --> 3579.64]  We have gotime.fm channel and the Gopher Slack.
[3580.26 --> 3586.82]  If you want to be on the show or have suggestions for topics or guests for the show, github.com
[3586.82 --> 3589.16]  slash gotime.fm slash ping.
[3589.98 --> 3591.16]  And with that, goodbye, everybody.
[3591.24 --> 3592.08]  We'll see you next week.
[3592.34 --> 3595.92]  And Matt Ryer will be joining us next week's show.
[3595.92 --> 3600.60]  You know, he probably rushed to finish the Gopher Eyes Me thing just before he was going to be on the show.
[3601.38 --> 3602.56]  Good for us.
[3602.98 --> 3604.56]  Now I understand everything.
[3606.48 --> 3610.30]  Well, everyone, thank you very much for having me.
[3611.20 --> 3612.30]  Last fun fact.
[3612.88 --> 3619.56]  In Florence, after Gola, I was just, you know, going around looking for a place to have lunch.
[3620.02 --> 3621.58]  We literally pick a random one.
[3622.32 --> 3625.66]  And don't I meet Matt Ryer while I'm getting out?
[3625.92 --> 3628.88]  Sitting at a table just across the room.
[3629.42 --> 3630.92]  Gophers attract Gophers.
[3631.20 --> 3631.52]  Wow.
[3632.54 --> 3633.06]  Yep.
[3633.46 --> 3633.82]  All right.
[3633.96 --> 3634.46]  Thank you, everyone.
[3634.64 --> 3634.96]  Thank you.
[3635.36 --> 3636.42]  Thank you, Filippo.
[3636.64 --> 3637.02]  Bye.
[3637.32 --> 3637.60]  Bye.
[3640.20 --> 3643.26]  Special thanks to our sponsors, Backtrace and Arden Labs.
[3643.54 --> 3646.00]  I also want to thank Breakmaster Cylinder for the awesome beats.
[3646.38 --> 3648.02]  Jonathan Youngblood for his editing skills.
[3648.30 --> 3650.34]  And, of course, Fastly for the bandwidth.
[3655.92 --> 3674.48]  Thank you, everyone.
[3674.54 --> 3675.18]  We're happy.
[3675.24 --> 3675.50]  Thanks.
[3675.54 --> 3676.46]  We're there.
[3676.46 --> 3676.50]  Thanks.
