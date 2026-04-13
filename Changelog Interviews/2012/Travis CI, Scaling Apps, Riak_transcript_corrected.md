[0.00 → 6.22] The Change Log is brought to you by Pusher, and they're looking for system engineers who specialize in vented systems.
[6.66 → 15.60] If you're happy to work with multiple languages, and you have experience in building vented systems, our friends at Pusher want to talk to you.
[15.98 → 23.72] This is a real hands-on job at Pusher, so relocation or London-based residents are the prime targets they're seeking out.
[23.84 → 29.94] Send a cover letter about how you will make Pusher more awesome, your GitHub profile link, and your CV.
[30.44 → 32.40] To jobs at pusher.com.
[48.04 → 51.32] Welcome to The Change Log, episode 0.7.5.
[51.32 → 52.54] I'm Adam Stachowiak.
[53.02 → 53.86] And I'm Won Netherlands.
[54.08 → 55.00] This is The Change Log.
[55.08 → 56.68] We cover what's fresh and new in open source.
[57.18 → 59.80] If you found us on iTunes, we're also on the web at thechangelog.com.
[60.00 → 60.78] We're also up on GitHub.
[61.24 → 62.02] Head to GitHub.com.
[62.40 → 66.66] You'll find some training repos, some feature repos from our blog, as well as the audio podcast.
[66.94 → 69.44] And if you're on Twitter, don't follow The Change Log Show.
[69.56 → 70.72] Follow The Change Log.
[70.88 → 72.02] And I'm Adam Stack.
[72.40 → 73.00] And I'm Penguin.
[73.14 → 74.48] P-E-N-G-W-Y-N-N.
[75.20 → 75.98] Fun episode this week.
[76.06 → 82.40] Talk to Josh and Matias over at Travis CI about hosted continuous integration in the sky.
[83.40 → 85.44] That was a very fun conversation.
[85.44 → 88.24] It seems like they're trying to do a lot of fun stuff.
[88.30 → 90.62] But they're also supporting a lot of different languages as well.
[91.22 → 91.34] Yeah.
[91.60 → 94.68] Ruby's been supported out of the box since its inception.
[94.84 → 100.44] But now we've got PHP, Python, Perl support, as well as Java, Scala, the usual suspects.
[100.70 → 106.92] So if you're looking for a hosted CI solution for your open source project, private projects are coming,
[107.46 → 112.26] and you don't want to stand up your own Jenkins box, then you might look at Travis CI.
[112.26 → 114.66] It seems like it's pretty easy to get started with it too.
[115.40 → 115.50] Yeah.
[115.58 → 118.40] You just go in and configure it right there in your GitHub project page.
[118.60 → 120.58] And you can embed an image in your README.
[120.66 → 124.40] You see this a lot of times when it has the build status right there in the README of the project.
[124.64 → 124.82] Right.
[124.94 → 129.16] It just has the image tag phone home to check the status of the build.
[129.28 → 132.28] And you see red, green, or yellow right there in the README.
[132.34 → 132.74] It's pretty cool.
[133.06 → 133.88] Colours accordingly.
[134.04 → 137.36] And then not only that, but they're also using Pusher, which is quite nice.
[137.42 → 138.02] And they're our sponsor.
[138.28 → 138.44] Yeah.
[138.44 → 139.70] We talk about that in the episode.
[139.70 → 144.60] It's a neat way to power the real-time UI that they've got in Travis.
[144.72 → 149.02] You can just sit there and watch the output from your project or someone else's project as it's happening.
[149.50 → 150.38] Well, that sounds like a fun episode.
[150.50 → 151.10] You want to get to it?
[151.40 → 152.04] Let's do it.
[161.28 → 164.80] We're talking today with Josh Matias from the Travis CI project.
[164.80 → 167.54] So you guys want to introduce yourself and a little bit about Travis.
[167.64 → 168.40] So Josh, you go first.
[168.40 → 169.90] Well, my name's Josh Calderas.
[170.16 → 173.40] I'm one of the core team members of the Travis CI project.
[173.72 → 178.54] I've been working on the project since February 2011 with Sven Fuchs.
[178.78 → 182.24] And we've since grown to four team members.
[183.52 → 183.84] Matias?
[184.62 → 185.88] My name is Matias Meyer.
[185.88 → 189.74] I'm the infrastructure guy on the Travis team.
[189.74 → 192.96] Well, I've hopped on rather recently.
[193.98 → 196.90] And I'm also the author of the React handbook.
[197.46 → 199.86] So yeah, that is my introduction.
[200.86 → 203.28] Definitely want to talk more about React later in the episode.
[203.64 → 209.66] So for the folks that don't know, Josh, why don't you give a little bit, a big picture of what Travis is and what it does.
[209.66 → 216.52] Well, Travis CI is a distributed continuous integration system for open source projects.
[216.72 → 219.10] It's also technically open source as well.
[219.22 → 222.46] But we try to emphasize that it's for open source projects.
[222.46 → 236.30] So if you think about Rails or Symfony, even Node.js, Ruinous, they're all using Travis because not only are your logs out in the open, but it just makes testing dead simple.
[236.72 → 240.96] So we've been testing Rails for the last eight months now, nine months.
[240.96 → 249.84] We've done 2,500 builds across different matrix variations so we can help test Rails projects, for example, against different Ruby versions.
[250.92 → 261.94] Previous to Rails 4.0, which is in master at the moment or still in development, we were testing against three different Ruby versions, 1.8.7, 192, and 193.
[261.94 → 272.10] And now that Rails master has moved to, well, 4.0, it's only against 193.
[273.98 → 280.62] We've got some big plans on how we can help increase testing as well to make it even better.
[280.98 → 288.32] For example, testing against different architectures for systems, if it is Windows or 32 or 64-bit Linux.
[288.32 → 304.14] But essentially, we're just trying to make testing easy for open source developers because who wants to actually set up a CI system for their little library in-house and hire a server or remember to run it against 10 different Rubies?
[304.72 → 305.86] You guys have some big news.
[306.20 → 308.34] Last couple of weeks, you know, support Python.
[309.04 → 311.04] So adding Python support was fantastic.
[311.24 → 313.34] It was a great reception in the Python community.
[313.46 → 315.22] It was actually one of our biggest growth days.
[315.22 → 319.16] It wasn't just Python supports that we had last week.
[319.24 → 319.98] It was Perl.
[320.16 → 326.42] And in fact, a week earlier, we added Java, Clojure, and Scala, and Groovy.
[327.22 → 331.94] We've actually technically had all of these languages supported for a long time now.
[332.20 → 337.20] Just we only supported one version of the language, only one VM version.
[337.20 → 343.18] So if you think about when we added Ruby, we had Ruby 187 and 192 and 193.
[343.92 → 345.78] And that's what we call first-class support.
[346.56 → 349.82] And for a long time, Python and Perl didn't have first-class support.
[349.90 → 354.20] You could only use one variation of the VM, of their VM.
[355.32 → 365.00] And now we essentially support, I think it's 10 different languages, with most of those having different versions of the language available.
[365.00 → 376.34] So even when you think about Ruby, you can test against Ruby head and Ruby 193, Ruby in 19 mode, Ruinous in 18 mode and 19 mode.
[376.48 → 380.94] There are so many different possibilities of what a normal developer can test against now.
[381.80 → 393.20] And we generally think that every language developer, all open-source developers, should have the benefit of Travis for their open-source community.
[393.20 → 401.88] So with all of those languages, that entire list of languages that you support, what about the different testing frameworks for each of those languages?
[403.44 → 409.16] So part of the idea that we've got in our worker at the moment is what we call the builder.
[410.40 → 416.72] And Sven extracted that to its own repo, so it makes it very easy for other people to add different language support.
[416.72 → 423.92] And the builder encompasses a lot of standard defaults that that community might use.
[424.24 → 432.26] If we think about Ruby, we know that Bundler and using Rake are some of the very basic defaults that we use.
[432.34 → 434.12] So we can detect if there's a gem file.
[434.46 → 436.48] If there's a gem file, we'll run bundle install.
[437.06 → 439.24] If there's a gem file, then we'll use bundle exec rake.
[439.24 → 443.00] And we apply that to different languages in different ways.
[443.18 → 450.14] So in PHP, there is no standard way of doing dependency installation.
[450.66 → 453.74] But there is a standard way of running the tests.
[454.38 → 458.06] And in Python, there are various standards for each of these.
[458.06 → 470.14] But the consensus within the community is instead we should just prompt them to define that in their Travis ML, which is the configuration for Travis for your project.
[470.80 → 477.90] When we had Dr. Nick on a previous episode, we brought up Travis had just come out, or I think you had just contacted me.
[478.44 → 480.46] You guys were just getting started with it.
[480.52 → 482.56] And he's a big Jenkins fan.
[483.92 → 487.02] What's the selling point of Travis over Jenkins?
[488.06 → 490.02] I'm definitely going to leave this one to Matthias.
[490.08 → 491.76] He's been working with Jenkins a lot recently.
[493.66 → 496.24] Yeah, I just used Jenkins on a project recently.
[496.78 → 500.62] And, well, I've got to say, the ideas are very similar.
[500.96 → 502.00] You know, it's continuous integration.
[502.30 → 506.18] There's not – the ideas behind that are, you know, very straightforward.
[506.54 → 510.52] And you find a lot of similarities in Jenkins compared to Travis, for example.
[512.10 → 517.80] But what repelled me a little bit from Jenkins was the user interface.
[518.06 → 522.24] And the point of Travis is to hide all that from the developer.
[522.78 → 530.32] So in Travis, you only have a YAML file where you define your complete build matrix and stuff like that.
[530.32 → 533.50] And in Jenkins, you do all of that through user interface.
[533.50 → 538.16] And that's not the main selling point.
[538.38 → 543.82] But, yeah, it's just – I didn't have a lot of fun using that user interface because there are a lot of options you can set on Jenkins.
[544.06 → 546.76] And it becomes a bit of a pain to use for me.
[546.86 → 557.74] That's why GitHub, for example, built their own Jacky bridge for Jenkins so that they can hook up their U-bot to Jenkins and not worry about the user interface at all.
[558.42 → 564.24] Speaking of the user interface, the Travis CI interface is, you know, real-time, powered by Pusher, I take it.
[564.30 → 568.80] What sort of challenges have you found just scaling that for so many projects?
[569.46 → 572.60] It's been an interesting ride over the last year.
[572.60 → 584.20] And if you look how the code has changed over that year time – so it's been one of the talks I've given at conferences about how we've really deconstructed Travis into separate deployable apps.
[584.26 → 585.70] And that's helped us scale tremendously.
[585.70 → 593.72] We run – we're pretty much entirely on Heroku for the platform part.
[594.28 → 603.58] And we use dedicated workers or dedicated machines with the most inefficient way of using a VM technology, which is VirtualBox, because it was handy for development.
[604.88 → 607.74] It's definitely a pain for maintaining, but it works.
[607.74 → 616.34] So on the platform side where we're using Heroku, we're using 192 and what we call the Travis CI.
[616.60 → 617.52] It's just Travis CI.
[618.22 → 620.76] And that's using Unicorn and 192.
[622.38 → 625.56] We've also got Travis Hub, which is a Ruby app.
[625.78 → 631.80] And that's using the AMP Java library for its communications.
[631.80 → 636.94] So we're using Ruby for Travis Hub on Heroku as well.
[637.38 → 642.74] And that uses Hot Bunnies, which is actually a Ruby wrapper around the Java AMP library.
[644.18 → 652.88] That's actually allowed us to scale quite well, because we just use native threading, and we spin up about 10, 12 different threads for managing the different queues.
[652.88 → 665.22] And we've also got another project, which isn't fully live yet, called Travis Listener, which allows us to take the various components of Travis offline, but still listen to the GitHub pings.
[666.42 → 671.82] And also behind the scenes, we're using RabbitMQ for messaging between all of these projects or applications.
[671.82 → 679.86] I know it's not a fair comparison, since you usually have to set up your own Jenkins box as opposed to a hosted system like Travis.
[680.02 → 685.20] But what's the comparison of setup if you wanted to set up a project on CI between the two?
[685.86 → 699.24] I wish I could use swear words right now, but I would highly recommend people don't try and use Travis internally right now, because it is a huge undertaking.
[699.24 → 703.36] It's much harder than just setting up a Jenkins in-house.
[704.54 → 708.06] It's not to say that I'm a huge fan of Jenkins.
[708.48 → 723.72] What I am really appreciative for them for, what I really do respect them for, is that they've come a long way in building up a CI system that is easy for people to install, or generally easy for people to install, and it works.
[723.72 → 733.84] But if you've got an open source project, let's say a Ruby Gem project out there, and you want to make sure that it works across several different versions of Ruby, what's the process to set it up on GitHub with Travis?
[734.50 → 740.96] So to set up your project on Travis is tremendously easy, and I think this is definitely one of the reasons why it's taken off.
[741.74 → 747.04] There is no huge setup process to go, and we try and get it up and running.
[747.04 → 751.62] And also, we automatically detect a lot of the defaults.
[751.94 → 754.38] So it's as simple as logging with GitHub on Travis.
[754.68 → 756.42] You can see all of your projects.
[756.78 → 765.56] You can turn on the service hook, and then you can either push your code to GitHub, and we'll automatically pick it up, or you can go to GitHub, and you can send a test hook.
[765.56 → 778.20] The trouble is that if you're a Python Perl or Java developer, then you'll definitely want to add a.travels.AML file.
[778.28 → 784.08] Even if you're a Ruby developer, you'll want to add that file, because by default, you don't want to just test against 187.
[784.32 → 790.06] You'd like to add different Rubies to be quite compatible, to make sure you've got compatibility.
[790.06 → 796.18] Which version of Ruby gives you the most fits to maintain with Travis?
[797.92 → 798.66] Sorry, how do you mean?
[800.30 → 802.22] So how many versions of Ruby do you support?
[802.32 → 804.18] We're talking MRI.
[805.92 → 810.58] Oh, I think we're up to 11 different versions of Ruby.
[811.54 → 812.98] Two of them are temporary.
[814.80 → 815.04] Yeah.
[815.04 → 822.98] Which versions of those are the most problematic to work with Travis, just getting it to run?
[823.82 → 830.70] I'd actually – well, we – so Michael Freshmen, so we've actually got kind of five team members on Travis.
[831.52 → 838.46] We've got Constantine House and Matthias, who recently joined, Sven Fuchs and me, and also Michael Freshmen.
[838.46 → 843.78] And Michael Freshmen has done an amazing job in maintaining our workers and our cookbooks.
[843.78 → 852.30] The great thing about using cookbooks is that anyone can start contributing and saying, oh, can you add the service here as a cookbook for it?
[853.00 → 861.74] So Pat Allen from Thinking Sphinx fame, he did the cookbooks for adding different versions of Sphinx, so he could then test against different versions.
[864.20 → 872.86] Michael has put a huge amount of effort into getting the cookbooks and the recipes right for RVM testing, or for adding different Rubies into RVM.
[872.86 → 878.40] And we have to give huge credit and huge thanks to the whole RVM team.
[879.40 → 890.60] They've put a lot of work in making – or adding extra configuration options, so we could get adding Ruinous in 1.8 and 1.9 mode and Ruby in 1.8 and 1.9 mode.
[890.60 → 903.54] So it makes it a lot easier within your YAML, when you're Travis YAML, to say, I want to test against 1.8.7, 1.9.2, 1.9.3, and Ruby in 1.8 mode, Ruby in 1.9 mode, et cetera.
[904.86 → 907.10] So recently you had the Love Travis campaign.
[908.12 → 908.88] How's that going?
[908.88 → 913.66] I'm really happy with how that's gone.
[913.84 → 916.56] I'm so appreciative for the community and to the community.
[916.72 → 918.32] They've helped us so much.
[918.98 → 925.56] A lot of companies have jumped on board and helped us with just being able to pay our rent effectively.
[927.26 → 934.84] Sven and I have spent the last six months kind of, I guess, job-free, just working on Travis.
[934.84 → 939.98] And being able to have the community help us out like this is just amazing.
[940.62 → 942.36] We've got some big features in the pipeline.
[942.76 → 945.34] Konstantin is currently working on the pull request support.
[946.52 → 948.14] I think that's going to be a game changer.
[948.26 → 951.72] I think this is going to explode Travis as well.
[951.80 → 955.74] We're going to have to throw workers at it like I can't believe.
[956.78 → 962.24] If you think about Spree or Symfony, even Rails.
[962.24 → 963.72] Rails is a perfect example.
[964.84 → 971.64] The usual workflow of a lot of Rails core is they'll get a lot of pull requests to come in.
[972.52 → 976.04] They'll check through the code on GitHub, and then they'll hit the merge button.
[977.02 → 981.42] And if it fails, then they have to go into their console, and they'll have to revert that and then push it back.
[982.66 → 987.94] And testing pull requests will now mean that you do a pull request for Rails, we will test it,
[988.16 → 991.56] and then we'll leave a comment in the pull request to say if it passed or failed.
[991.56 → 995.84] And this will just be an absolute game changer for open source projects.
[995.96 → 1000.08] It means accepting pull requests is all about did the tests pass?
[1000.18 → 1001.28] Did Travis say it passed?
[1001.72 → 1005.66] And can I look over the code to see, you know, is it clean?
[1005.82 → 1006.82] Is it doing things right?
[1007.42 → 1008.44] And then you can hit merge.
[1008.44 → 1017.68] Yeah, I'm surprised that all the low-tech solutions we're finding to integrate with GitHub around like badges and the readies for build status and things of that sort.
[1017.72 → 1019.46] And you're talking about build comments.
[1020.14 → 1024.72] Do you wish GitHub had more like meta hooks that you could hook into at the repo level?
[1024.72 → 1031.90] Actually, it's only because of Rick Olson, Technogenic, that we're able to start adding the support.
[1032.56 → 1037.50] We talked to him last year at Frozen Rails about how we really want to work on pull request support.
[1038.36 → 1043.44] And the thing that was partially holding us back is that we needed some APIs for when people add pull requests.
[1043.44 → 1053.66] Because for us to pull GitHub over the 6,000 projects we've currently got on there to see if a pull request is being added isn't really going to scale on our end.
[1054.22 → 1058.44] And we just needed to get some notifications if a pull request is added and if it's updated.
[1059.50 → 1064.52] So he worked really, or he added that specifically for us, which was fantastic.
[1065.38 → 1070.54] And now we can actually work on that feature, which Konstantin is most of the way through.
[1070.54 → 1075.54] I think we're probably about two or three weeks off until we can start rolling that out incrementally.
[1078.34 → 1085.36] Once we've got those notifications, then when you update your pull request, we can then retest it as well.
[1085.52 → 1089.30] So think about pull requests as a discussion.
[1090.08 → 1093.10] You add a little bit of code, we'll tell you it fails.
[1093.78 → 1095.90] You add some more code, now it passes.
[1096.30 → 1099.12] You add another feature to that code, it fails again.
[1099.12 → 1103.54] It becomes something where all of those Travis comments are going to stay within the discussion.
[1103.86 → 1106.22] And then eventually it will be, hey, it passes, time to merge.
[1106.94 → 1110.74] What's your roadmap for private repos and when you can turn that on for everybody?
[1111.74 → 1114.50] Well, we're looking into the options right now.
[1114.90 → 1119.08] We're actually actively, Win just started actively working on it.
[1119.08 → 1125.40] On getting what we're calling Travis Pro codename Magnum set up.
[1126.34 → 1131.82] And we've been looking at different options on how we can make that scale better.
[1131.98 → 1141.98] Because obviously when you offer commercial solutions, you have to think a lot more about SLAs and ensuring a quality of service and stuff like that.
[1141.98 → 1149.94] And so we've been looking at the options of what we can use, for example, instead of VirtualBox for virtualization on machines.
[1150.90 → 1156.52] And, well, we figured out ways to actually shorten the path to getting to an alpha.
[1156.78 → 1161.50] So I'm not sure if I'm ready to announce a date for that yet.
[1161.76 → 1162.04] But, yeah.
[1162.04 → 1164.36] How much more complex of a problem is it?
[1164.40 → 1167.46] Do you have to add multi-tenancy to cover things like that?
[1167.50 → 1172.88] Or is it the same platform you're just having to worry more about how to scale that?
[1173.30 → 1175.72] Yeah, it's actually the multi-tenancy thing.
[1175.86 → 1177.66] That's what's going to keep us busy the most.
[1177.90 → 1181.78] And to make sure, you know, security issues and stuff like that.
[1181.84 → 1186.32] Because obviously we're going to be dealing with people's private source codes and stuff like that.
[1186.32 → 1186.80] But, yeah.
[1187.76 → 1191.06] On the application side, it's mostly a multi-tenancy.
[1191.06 → 1193.60] And that's what Sven is actually currently working on.
[1194.68 → 1198.94] So if you want to speed that up as a listener, you can donate, pitch in.
[1199.76 → 1202.16] Open source is free, but it's not cheap.
[1202.32 → 1205.90] So, Josh, tell them what they've won if they do donate to Travis.
[1207.72 → 1210.30] Well, we'll send you a beautiful picture of Sven Fuchs.
[1213.04 → 1215.68] Well, we've got a whole range of donation options.
[1215.92 → 1217.14] We just love anything.
[1217.24 → 1219.32] If you want to donate a buck, that's perfect.
[1219.32 → 1224.06] If you want to donate the top, which is like 500, that would also be amazing.
[1224.40 → 1232.60] In fact, the one thing that we haven't really highlighted enough on the site is that we had a whole range of amazing developers come out.
[1232.60 → 1242.14] Like Aaron Patterson, Yehuda Katz, Jose Valid, John – now, I keep pronouncing John Leighton's name or John Leighton's name as Leighton.
[1242.24 → 1244.26] And he loves that because he's like, oh, that's so leet.
[1244.76 → 1248.76] But you can also program with John Leighton as well.
[1248.76 → 1253.92] So, if you donate 500, you'll get an hour online peer programming with them.
[1255.10 → 1259.76] Aaron's ready to take a day off, you know, the job, of his job just to help out with this.
[1260.58 → 1261.64] Sponsored peer programming.
[1261.74 → 1262.14] I love it.
[1262.60 → 1265.60] And you get some credit on Travis Pro when we're all ready to go live.
[1265.68 → 1266.92] And you get beta access.
[1266.92 → 1273.00] But anything that anyone wants to donate is just fantastic by us.
[1273.46 → 1276.36] So, speaking of sponsorship, Pusher backs this podcast.
[1276.52 → 1278.04] We're so very thankful for them.
[1278.74 → 1280.94] Matthias, what has Pusher meant to Travis?
[1280.94 → 1288.62] Well, mostly allowing us to have a pretty nicely responsive real-time user interface.
[1288.84 → 1291.92] That's probably, well, that's the one thing we really use it for.
[1292.02 → 1293.76] And that's what it's been really fantastic for.
[1293.88 → 1301.68] To have a really short loop user feedback that when a build starts, we can immediately pop up the new library and the user interface.
[1301.90 → 1309.00] And we can keep, you know, as a build proceeds, as new log output comes up from the build, we can immediately push it out to the user interface.
[1309.00 → 1310.54] And it's just fantastic for that.
[1310.94 → 1313.66] Complete with syntax highlighting and colour coding.
[1313.88 → 1314.48] It's awesome.
[1314.80 → 1316.50] I love the UI on Travis.
[1317.68 → 1322.02] So, Matthias, you're also an author of the React handbook we mentioned earlier.
[1322.24 → 1324.62] So, what's the backstory on that?
[1325.96 → 1329.30] Well, the backstory is that I wanted to write a book on NoSQL databases.
[1329.78 → 1333.78] And the other part of the backstory is that I worked for Basho for a while.
[1333.78 → 1344.46] And, yeah, that book kind of came about to be the collective, well, brain dump of everything I learned about React up until that point.
[1344.54 → 1345.26] And it still is.
[1345.32 → 1350.74] So, I'm still working on it to get updates out and, well, to produce more content.
[1350.88 → 1354.00] For example, just recently they released React 1.1.
[1354.00 → 1358.32] And 1.1.1 is actually still in the works.
[1358.66 → 1362.12] And they added some new features, which I would like to cover in the book as well.
[1362.28 → 1364.66] So, I'm pretty much still working on it.
[1364.84 → 1365.94] It's still a work in progress.
[1366.14 → 1368.04] But, yeah, it's been really fantastic to sell.
[1368.72 → 1370.62] And, yeah, I self-published the book.
[1371.40 → 1374.82] Kind of built my own production chain for the book.
[1375.14 → 1377.08] And, yeah, it's just been going very well.
[1377.18 → 1379.24] Much better than I originally expected, actually.
[1380.02 → 1382.22] Is React your favourite NoSQL solution?
[1384.76 → 1387.04] Oh, the answer to this could get me in trouble.
[1387.22 → 1387.60] I don't know.
[1388.56 → 1389.68] It depends, right?
[1389.80 → 1390.04] Yeah.
[1390.56 → 1393.20] I don't really have a favourite database in general.
[1393.66 → 1399.82] You know, to me, I don't make the difference that much anymore between NoSQL databases and relational databases.
[1399.82 → 1401.42] To me, they're all just databases.
[1401.66 → 1403.02] And they have their strengths and weaknesses.
[1403.58 → 1406.28] And, yeah, that's pretty much how I look at things right now.
[1406.28 → 1410.84] So, but I do like React a lot.
[1411.42 → 1414.52] What sort of use cases is React just made for?
[1415.14 → 1421.04] Well, the one use case that most people that come to React have is to really have high availability.
[1421.40 → 1425.78] To have a database that can, you know, even when stuff falls on its face, when servers fall down,
[1426.22 → 1430.46] you still have availability to accept read or write requests no matter what.
[1430.64 → 1432.04] And that's where React really shines.
[1432.16 → 1433.52] And that's where I really like it for.
[1433.52 → 1439.04] And, yeah, the problem with that is that it obviously brings a lot of trade-offs.
[1439.16 → 1447.68] And a lot of people have some difficulties, you know, getting into these trade-offs or changing the mindset from relational databases where you have stronger consistency,
[1448.36 → 1451.12] where you have different data models and things like that.
[1451.12 → 1454.24] And that's where people struggle a little bit with React.
[1454.38 → 1458.68] And that was kind of the point of the book originally, to make that part a lot easier.
[1458.94 → 1466.18] Because it's just right up to right until the end, I added stuff on how you would model data for eventual consistency, for example.
[1466.26 → 1469.54] And that was kind of fun because it's kind of mind-bending to do that.
[1469.54 → 1473.58] And just to show people how you would, you know, how you would do that with React.
[1473.96 → 1478.60] And it's just what you have to do when you have a lot of writes, and you have a lot of updates on the same data.
[1478.74 → 1480.54] You just have to prepare your data for that.
[1480.86 → 1488.48] And, but, yeah, in scenarios like that where high availability and fault tolerance is just really important, React is just awesome.
[1488.64 → 1489.44] I love it for that.
[1489.44 → 1503.18] I want to take a moment to talk to you about Hover.com, our latest sponsor that we're actually quite stoked about because Won and I, we use GoDaddy primarily for all of our domain purchases in the past.
[1503.36 → 1512.40] And with all the recent fiascos, and I'm sure you know what I'm talking about, there was some major need in the area of domain registrations and taking care of that stuff.
[1512.40 → 1517.14] So, lo and behold, we actually found Hover, decided to start using them.
[1517.20 → 1521.06] They became a sponsor of the show, which is kind of neat as well.
[1521.20 → 1527.88] But if you go to hover.com slash the changelog, you can save 10% on all orders.
[1529.08 → 1533.66] They actually have this valet service that will move your domains for you.
[1533.68 → 1539.58] So if you're at GoDaddy or anywhere else, doesn't matter where, they'll – you give them a phone call.
[1539.58 → 1540.82] You talk to a human being.
[1541.20 → 1542.92] They go through all the details with you.
[1543.48 → 1550.92] Now, obviously, there are fees applied to moving your domains, which they can help, but that service to you is no cost whatsoever.
[1551.30 → 1559.58] They do all the valet, all the moving, all the MX records, all the DNS reset up for you, and that's no cost.
[1559.66 → 1563.58] You go in and give a final approval, and they go ahead and take care of it.
[1563.58 → 1572.48] If you have lots of domains, like we have, like, 30 or more domains, they can actually break that up into chunks so it's not just one big hit, and it's quite nice.
[1572.48 → 1575.18] So hover.com is a fantastic new sponsor.
[1575.30 → 1578.78] We gladly thank them for supporting the show, and we hope that you do the same.
[1579.26 → 1586.94] Again, you can use the changelog to save 10% on all orders at hover.com or just go to hover.com slash the change logging to be grandfathered right in.
[1586.94 → 1590.68] It seems like almost every app has a big data problem now.
[1590.78 → 1591.58] What about Travis?
[1592.08 → 1596.82] What sorts of data do you guys have in the back end, or is it mostly just within Git indexes?
[1597.76 → 1602.98] I think the biggest data we actually have are the result logs.
[1603.38 → 1612.40] For example, the Rails log, when a build fails because something changes in the database adapter and everything breaks, a Rails log can grow quite significantly.
[1614.26 → 1615.84] It's more than quite significantly.
[1615.84 → 1631.68] We had some huge issues for a while where if something went wrong in Rails or even other big test suites, you know, so Rails, their test suite, when we first approached it, tried to get on Travis, ran for two hours.
[1632.62 → 1634.70] So their feedback loop was tremendous.
[1635.58 → 1639.66] And the first thing that Sven worked on was to break that up into five units.
[1639.96 → 1642.20] So you can now have 20-minute units.
[1642.20 → 1645.42] So if we could have them running concurrently, it would only take 20 minutes.
[1645.84 → 1652.20] But it's still – Active Record, for example, has a huge test suite, which will take a long time.
[1652.74 → 1664.22] And if you have warnings pop up on every single test, it can grow a 100-kilobyte log to I think our largest log that we saw clog up Travis.
[1664.44 → 1666.28] Like it brought the entire system to a halt.
[1666.68 → 1668.82] It was 184 legs.
[1668.82 → 1669.30] Wow.
[1669.84 → 1673.22] And we were storing that in a single database column.
[1674.72 → 1676.64] And it was quite funny.
[1676.84 → 1680.74] Like we're like, oh, God, we're having another warning in someone's test suite.
[1680.86 → 1686.08] Like someone would update their Rails, and now it was all over their test suite and everything would stop.
[1686.08 → 1689.30] So we added log limiting to that.
[1689.40 → 1693.54] So now a test log can only be a maximum of four legs.
[1693.60 → 1698.20] And then we add a warning to the bottom to say, I'm sorry, your log is too long.
[1698.46 → 1699.42] It's over four legs.
[1699.46 → 1700.48] We've had to halt the test.
[1701.94 → 1705.22] But, yeah, other than that, Travis doesn't really have a big data problem.
[1706.50 → 1709.42] I don't know about you, Josh, but I'm fine with that.
[1709.42 → 1711.78] But I'm quite happy with that.
[1711.98 → 1713.94] What parts are the most challenging to scale?
[1714.26 → 1717.30] Where are you focusing your brain power on right now?
[1719.80 → 1729.42] Well, the one part that is actually harder to scale is being able to scale out the hub part and making it redundant and fault-tolerant in that way.
[1730.44 → 1733.22] But that's mostly the solution to that is actually not that hard.
[1733.22 → 1737.60] But it's mostly related to an ordering of events.
[1737.60 → 1747.26] So, for example, when we push stuff, when the worker just continuously keeps pushing a log output through pusher out to the user interface.
[1747.64 → 1751.16] And right now it's assumed that always comes up in order.
[1751.60 → 1758.32] And the simplest fix to that problem would be to make sure it doesn't come up in order, if you know what I mean.
[1758.32 → 1769.48] And that you have some sort of buffering in the client that can keep track of sequences where the log currently left off and where this chunk that just came in belongs.
[1769.48 → 1777.90] And if there's a hole in the data the client still has, it holds out on displaying that chunk of data until the rest arrives and stuff like that.
[1778.16 → 1781.18] So, from my point of view, that's the hardest part to scale.
[1781.84 → 1784.18] The rest is pretty easygoing.
[1784.18 → 1786.90] So, I wanted to get personal here a little bit.
[1787.04 → 1789.02] So, Josh, you are quite the globetrotter.
[1789.30 → 1792.98] You speak at various conferences across the globe.
[1794.24 → 1798.82] What areas have the most vibrant Ruby community that you've noticed?
[1800.26 → 1802.16] The States is completely vibrant.
[1802.26 → 1803.92] It's been vibrant for a long time now.
[1803.92 → 1811.82] What I was surprised about was I went to Ukraine and Russia recently.
[1812.58 → 1816.14] And they've got really great communities, but they're still quite growing.
[1817.48 → 1823.22] And there are a lot of really, you know, they just want to learn more about open source and how it can benefit them.
[1823.22 → 1830.86] And there's probably a little bit of hesitation to jump in and make as much of your code open source.
[1830.98 → 1834.12] And I think that's where a lot of the Ruby community has kind of grown.
[1834.12 → 1845.36] It's like by having an open source movement, we've become very active of talking online and pull requests and issues and helping each other.
[1845.36 → 1848.90] I really enjoyed the Cape Town guys as well.
[1850.04 → 1856.68] Cape Town in some ways reminds me of New Zealand in that it's quite far removed from a lot of areas.
[1856.92 → 1858.74] Like it's a long flight from Europe.
[1858.88 → 1860.36] It's a long flight from America.
[1860.92 → 1862.40] It's a long flight to Australia.
[1864.32 → 1869.52] But it reminds me of New Zealand a lot in the wineries and the friendliness of the people.
[1869.52 → 1878.74] And it's got a fantastic developer community where Ruby Food, which is run by the Mad Mimi guys every year.
[1879.24 → 1880.54] It's a fantastic conference.
[1880.66 → 1888.14] If there was a conference I could recommend some people to go to, it'd be head to Cape Town and stay there for a month and just enjoy.
[1888.82 → 1890.36] That's a good question of each of you now.
[1890.42 → 1891.48] Who's your programming hero?
[1893.26 → 1894.06] Matthias, you go first.
[1894.60 → 1895.64] Josh, can you go first?
[1896.94 → 1899.22] I was going to be cheesy and say it was you, Matthias.
[1899.52 → 1900.90] Okay, then I'm going to say Josh.
[1903.50 → 1905.46] No, personally I don't have heroes.
[1905.58 → 1908.44] I have a lot of people who I respect for doing what they do.
[1909.24 → 1911.82] But yeah, I don't have any hero in particular, I'm afraid.
[1913.00 → 1915.72] Actually, I think I'm going to go for Jose Selling.
[1917.60 → 1919.44] He puts out a lot of code.
[1919.86 → 1924.50] He puts out a lot of code, but he also puts out a lot of community effort.
[1924.50 → 1935.96] You can code, and you can commit, and you can push to GitHub, but it's also about being available and answering questions and mentoring people.
[1936.64 → 1941.32] He was the guy that helped me get a lot of commits into Rails.
[1941.32 → 1946.50] I'd be sitting on I'm with him, and I'd ask him questions, how to fix this, approach that.
[1947.14 → 1948.90] And he doesn't have to do that.
[1949.20 → 1950.40] People have their day jobs.
[1951.36 → 1955.42] But he puts in a lot of love and helps a lot of people out.
[1955.48 → 1956.58] So I really respect that.
[1957.60 → 1959.20] So Matthias, let me put it a different way.
[1959.20 → 1963.60] If you could pair program with anybody in the community, who would it be?
[1966.16 → 1966.56] Hmm.
[1967.80 → 1969.36] I still have to think about that.
[1972.64 → 1974.12] Well, Matthias is going to email us.
[1974.18 → 1974.96] We'll put it in the show notes.
[1976.48 → 1981.16] So when you're not hacking on Travis, you're not hacking on React,
[1981.88 → 1987.38] what open source software out there just has you excited that you just want to play with?
[1987.38 → 1990.14] Oh, well, I can start with that.
[1990.68 → 1992.14] That's what I'm actually prepared for.
[1993.30 → 1997.26] Well, currently I'm very interested in distributed message queues.
[1997.50 → 2001.86] So currently I have my eyes on Kafka and Cottrell.
[2002.52 → 2009.16] Cottrell is kind of what Twitter built as a replacement for their Ruby Starling, I think, if I remember correctly.
[2009.96 → 2011.82] And Kafka was built at LinkedIn.
[2012.36 → 2014.60] And they're both pretty fantastic.
[2014.60 → 2017.68] And I would definitely want to spend more time playing with them.
[2017.90 → 2022.32] And also with Zookeeper, which powers Kafka in a way.
[2022.52 → 2025.82] Zookeeper is like a distributed process coordination framework.
[2026.40 → 2028.50] And it looks fascinating.
[2028.88 → 2030.68] That kind of has me really excited.
[2030.68 → 2039.78] But the other part from the Ruby world I'm excited about is Tony Archer's Celluloid and all the libraries he's been pushing out.
[2039.82 → 2041.76] He's been pushing out an amazing amount of code.
[2042.86 → 2052.22] And yeah, I definitely need to play with that more because Celluloid in particular would be a nice fit for some of the things I have in mind for some parts of Travis.
[2052.22 → 2054.88] I completely agree there.
[2055.06 → 2059.82] I'm really impressed with Celluloid and Sidekick as well.
[2060.14 → 2060.36] Mm-hmm.
[2060.90 → 2062.30] Oh, but that's by Mike.
[2062.30 → 2063.02] That's Mike Pelham.
[2063.64 → 2064.82] Mike's a friend of the show.
[2065.78 → 2070.96] Basically, Sidekick is rescue in a more thread-safe manner.
[2071.02 → 2071.32] Is that right?
[2071.32 → 2073.58] Well, it's based on Celluloid.
[2073.68 → 2076.46] But yeah, it's an in-process rescue, if you will.
[2078.16 → 2083.46] I think a lot of Ruby developers at the moment are still a little bit hesitant to use threading.
[2084.20 → 2088.98] Because threading is seen as, well, you know, there are threading issues all over the show.
[2089.08 → 2090.02] How do I solve that?
[2090.06 → 2090.96] How do I work with it?
[2091.56 → 2097.26] And I think we need to kind of get over that hang-up and learn how to use threading properly.
[2097.26 → 2107.38] Because if it's implemented in a VM like Ruby or Ruinous, you've got a whole set of fantastic concurrency models available,
[2107.66 → 2111.24] which can really utilize the VM in many different ways.
[2111.86 → 2113.24] So we shouldn't be scared of that.
[2113.48 → 2117.52] And that's why I really like Sidekick, is that instead of going for this process model,
[2117.92 → 2121.36] we can use it within a single code base in a single instance.
[2121.50 → 2124.16] We don't have to do a lot of crazy stuff.
[2124.22 → 2125.98] We've got a great threading model available.
[2127.26 → 2134.26] Are tools like this going to just make it easier to architect our applications as just small atomic services that we can consume?
[2134.82 → 2136.70] How many services are in Travis? Put it that way.
[2137.62 → 2137.96] Oh.
[2140.04 → 2141.74] It's not one giant Rails app.
[2143.00 → 2143.28] No.
[2145.10 → 2147.40] We've got four deployable apps.
[2147.96 → 2150.92] And we've got a total of about 11 GitHub repos.
[2150.92 → 2159.16] I just added new Relic messaging to the Travis Hub today to test on staging.
[2159.64 → 2164.12] And it's interesting to see kind of like what's going on under the hood and what are the slow bits.
[2164.84 → 2169.90] But we're using things like Couch DB at the moment for some of our archiving.
[2169.90 → 2174.14] We've got pusher, IRC notifications, email.
[2176.76 → 2178.52] It's utilizing a lot of services.
[2179.46 → 2183.20] But we've got four distinct Travis services.
[2184.60 → 2187.74] I can talk about external services we use, but I'm not sure.
[2187.86 → 2188.68] Sure. Go for it.
[2188.90 → 2189.24] Well, yeah.
[2189.24 → 2191.26] We have a couple of internal services.
[2191.50 → 2195.66] And just as Josh said, we use New Relic for monitoring the performance and stuff like that.
[2195.80 → 2201.34] And I just, well, I'm a big fan of using external services myself because I've been, well, we're building one.
[2201.42 → 2203.46] And I've always been building infrastructure services.
[2203.66 → 2212.72] I recently added Libra do's metrics, which is a pretty nice way to have to get real-time graphs and stuff that happens inside of Travis.
[2212.72 → 2217.46] And, yeah, we're using a pretty funny setup for that.
[2217.60 → 2220.90] We're basically, the metrics are regularly dumped to our log files.
[2221.12 → 2223.68] And from there, they're aggregated into a log collector.
[2224.66 → 2232.12] And from that log collector, they're sent to a tiny app on Heroku that aggregates the data again.
[2232.24 → 2235.72] And then it's pushed from that app into Libra do's metrics.
[2236.00 → 2241.98] So our app itself is totally oblivious to the fact that there is some metrics collecting going on.
[2241.98 → 2244.06] And it just dumps them into the log.
[2244.34 → 2247.74] And some other part of the service will take care of it.
[2248.04 → 2251.38] So, yeah, I just increase complexity of Travis by a lot.
[2251.92 → 2254.40] But it's pretty transparent.
[2254.64 → 2259.84] It doesn't matter to the app if the metrics are actually, if they actually end up somewhere.
[2260.16 → 2262.14] And it's just a really nice way.
[2262.34 → 2268.06] And I have to say, Eric Lindwall from Paper Trail and 7Scale, he built the libraries for that.
[2268.12 → 2269.52] And I'm very thankful for that.
[2269.58 → 2271.02] And they're actually both open source.
[2271.02 → 2274.28] So, and what else do we use?
[2274.34 → 2277.92] We use Pusher for the real-time communication.
[2278.14 → 2280.60] We use RabbitMQ as a service.
[2280.90 → 2283.80] We use, Josh, what else do we use?
[2285.48 → 2287.96] We're using Postgres for the database, which I really love.
[2290.06 → 2291.92] I think those are the majority of the services.
[2292.08 → 2296.74] I'd like to look into using Elasticsearch for some of our search and faceting.
[2296.74 → 2303.72] I'd also like to potentially look into Zero in the future for our job queuing.
[2304.32 → 2306.18] RabbitMQ is great as a messaging protocol.
[2306.18 → 2311.54] It has, it's a little bit tricky to put in really fine-grained controls.
[2311.70 → 2316.08] Like if we wanted a worker to say, give me, you know, these are my capabilities.
[2316.34 → 2317.36] Give me X job.
[2317.44 → 2319.50] If it's available otherwise, give me Y job.
[2320.28 → 2324.06] We have to do, we have to actually set up two different queues.
[2324.18 → 2330.60] And then we have to set up, either way, like what we have to do with Rabbit is more constricting.
[2330.60 → 2335.32] And then what you could do with maybe Zero where you've got a lot, it's much more bare bones.
[2335.82 → 2338.80] So we can put in a lot of our own custom business logic for that.
[2342.14 → 2347.50] I'm hesitant of adding Zero, though, because it adds extra complexity onto the Travis model.
[2347.62 → 2349.40] We're trying to keep it as simple as possible as well.
[2349.50 → 2352.82] I think that's the main selling point from the outside looking in is, you know,
[2352.88 → 2357.60] I'm not sure that you're competing with other CI platforms as much as you're just growing the tent
[2357.60 → 2362.38] for folks that may not be doing CI just to make it, you know,
[2362.44 → 2365.90] dead easy for them to add CI to their open source projects that are hosted on GitHub.
[2366.44 → 2369.50] We're excited about what you guys are doing and the whole team
[2369.50 → 2371.74] and look forward to seeing what's coming out of Travis.
[2371.90 → 2377.06] And if you're out there listening as a user or as a company and want to pitch in,
[2377.22 → 2380.20] be sure and go to love.travis-ci.org.
[2380.34 → 2383.96] Can I do a really shameless plug, though?
[2384.50 → 2384.68] Sure.
[2384.68 → 2388.94] I actually really want to thank a lot of our sponsors that have helped us out.
[2390.56 → 2396.82] So I really want to thank a lot of our sponsors like Wood, Bendy works as well.
[2396.90 → 2402.68] Bendy works built a really cool iOS open source app for Travis,
[2402.80 → 2406.14] so you can check out the log streaming live on your phone.
[2407.22 → 2409.18] Also, Cloud Control and Zing.
[2409.26 → 2410.54] These guys have really helped us out.
[2410.54 → 2413.88] Heroku and SoundCloud, Net App, Mongol.
[2414.02 → 2414.92] I mean, the list goes on.
[2415.92 → 2417.92] Can Banner, Ticket Evolution.
[2418.72 → 2423.06] And this is – I'm probably not saying this right, but Zweig?
[2423.72 → 2424.92] No, you said it right.
[2425.66 → 2426.14] Oh, perfect.
[2426.58 → 2428.34] These guys have really helped us out,
[2428.54 → 2431.42] and we've raised a lot of our money through company sponsorship.
[2431.42 → 2436.98] So, you know, these are the companies that are helping keep Travis alive
[2436.98 → 2438.32] and helping us pay our rent.
[2438.48 → 2441.90] So, you know, if you're either looking for a job
[2441.90 → 2444.30] or just want to send some thanks to them, that would be fantastic.
[2445.12 → 2446.38] Thanks for joining us today, guys.
[2446.84 → 2447.66] Oh, our pleasure.
[2447.78 → 2448.12] Thank you.
[2448.12 → 2449.12] Thank you.
[2449.12 → 2479.10] Thank you.
[2479.12 → 2480.20] Thank you.
[2480.66 → 2482.00] Thank you.
[2482.02 → 2484.04] Thank you.
[2484.26 → 2486.78] Thank you.
