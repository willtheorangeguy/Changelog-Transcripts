[0.00 --> 6.98]  What's up, friends?
[7.04 --> 9.70]  This week on the ChangeLog, we're joined by Bridget Murtaugh,
[9.78 --> 12.96]  Product Manager on the Visual Studio Code team at Microsoft.
[13.40 --> 16.60]  And we're talking about development containers and the dev container spec.
[16.68 --> 18.56]  Ever since we had Corey Wilkerson on the show,
[18.78 --> 20.76]  talking about coding in the cloud with code spaces,
[21.12 --> 25.44]  we wanted to get the changelog.com code base set up with a dev environment in the cloud
[25.44 --> 27.50]  to more easily support contributions.
[27.50 --> 32.60]  After getting a drive-by contribution from Chris Eggert to add a dev container spec to our code base,
[32.78 --> 33.46]  we got curious.
[33.76 --> 36.98]  We reached out to Bridget and asked her to come on the show to give us all the details.
[37.46 --> 41.80]  And we also have a bonus on this show for our Plus Plus subscribers.
[42.34 --> 44.76]  But hey, if you're not a Plus Plus subscriber, it's too easy.
[45.20 --> 47.44]  changelog.com slash Plus Plus.
[47.70 --> 51.40]  A massive thank you to our friends and partners at Fastly and Fly.
[51.68 --> 56.52]  Those pods are fast to download globally because Fastly, well, they're fast globally.
[56.52 --> 58.56]  Check them out at Fastly.com.
[58.82 --> 63.08]  And our friends at Fly help us put our app and our database close to our users, no ops.
[63.56 --> 65.48]  Learn more at Fly.io.
[73.68 --> 76.92]  This episode is brought to you by our friends at Postman.
[77.32 --> 81.32]  Postman is an API platform for building and using APIs.
[81.32 --> 90.30]  They are most known for API testing, and you may already use them, but they've built a full-featured API platform to help developers along each step of the API lifecycle.
[90.94 --> 93.72]  But what does it mean for Postman to be an API platform?
[94.08 --> 101.44]  Well, from API design, testing, monitoring, documentation, mocking, to the sharing and discoverability of APIs,
[101.44 --> 106.04]  they've built a full suite of tools to help teams build APIs together faster.
[106.40 --> 111.38]  Over 20 million developers use Postman to deliver their APIs, plus they have a generous-free tier.
[111.64 --> 114.32]  Start designing, developing, and testing APIs.
[114.80 --> 119.62]  Organize all your API development into workspaces and share those workspaces with other developers.
[120.08 --> 122.58]  You can create public workspaces to collaborate with the world's developers.
[122.96 --> 124.62]  You can back up your work to Postman's cloud.
[124.62 --> 128.06]  You can get their core tooling and collaboration for up to three users.
[128.52 --> 132.72]  Sign up and start using Postman for free today at postman.com slash changelogpod.
[132.84 --> 139.12]  Or for our listeners already using Postman, we encourage you to explore the entire API platform that Postman has to offer.
[139.32 --> 141.62]  Again, postman.com slash changelogpod.
[141.62 --> 171.60]  So we are joined by Bridget Murtaugh, a product manager on the Visual Studio.
[171.62 --> 178.10]  Code team at Microsoft and one of the co-authors or the people working on the Dev Containers spec.
[178.24 --> 179.16]  Bridget, welcome to the show.
[179.64 --> 180.28]  Thank you so much.
[180.36 --> 181.14]  I'm excited to be here.
[181.46 --> 182.92]  We are excited to have you.
[182.96 --> 189.04]  We're just learning about Dev Containers by way of a contributor to our changelog.com repo
[189.04 --> 191.96]  who wanted to hack on the repo.
[192.20 --> 196.96]  And if you go to our repo at github.com slash the changelog slash changelog.com
[196.96 --> 199.52]  and you try to hack on it, there's a contributing doc.
[199.52 --> 201.46]  And it's like, here's how you get all set up.
[201.70 --> 203.06]  And it's macOS only.
[203.30 --> 204.50]  And it's like very manual.
[205.02 --> 207.06]  Install this, install that, blah, blah, blah.
[207.98 --> 210.60]  Kind of lame, but straightforward if you've done it before.
[210.80 --> 216.02]  But if you're just a casual contributor or you're just getting started and you'd like to contribute,
[216.02 --> 224.70]  there's really no easy on-ramp until recently when Chris Eggert, perhaps a colleague of yours also working,
[224.80 --> 229.52]  he works at on Azure Resource Manager, wanted to help us fix a bug.
[229.94 --> 235.06]  And before he could do that, he hooked us up with a devcontainer.json.
[235.06 --> 243.82]  And all of a sudden, boom, you could launch our repo in code spaces and be staring at our code and running our code super quick.
[243.94 --> 245.24]  And I was like, this is cool.
[245.42 --> 246.96]  And he pointed us to Dev Containers.
[247.28 --> 249.10]  We followed that trail and we found you.
[249.56 --> 250.50]  So here you are.
[250.58 --> 251.00]  Here we are.
[251.22 --> 253.96]  I'm glad the trail led to me and we can talk today.
[254.90 --> 255.76]  So are we.
[255.88 --> 256.48]  It was awesome.
[256.68 --> 258.48]  I'm glad that you agreed to join us.
[258.48 --> 266.52]  I think we hit you up six ways from Sunday, LinkedIn, GitHub, email, and then by way of our co-friend, Brett Cannon,
[266.68 --> 270.32]  who also put in a good word and we're like, we're getting bridged on the show one way or the other.
[270.46 --> 272.08]  I mean, you can't say no when you get that many.
[272.18 --> 273.16]  Well, you can say no.
[273.22 --> 274.04]  This wouldn't be polite.
[274.30 --> 274.50]  Yeah.
[274.58 --> 276.18]  You could just block us from everything.
[276.34 --> 277.36]  And so these guys are creepy.
[278.08 --> 279.50]  But thankfully you didn't.
[279.98 --> 286.76]  And yeah, we'd love to learn more about containers.dev, what it is and what y'all are up to.
[286.76 --> 290.40]  You want to open up with us and just tell us what containers.dev is.
[290.68 --> 291.78]  Yeah, that sounds good.
[291.98 --> 300.40]  So anyone listening, you can go to containers.dev in your browser and you're going to see our overview spec site for the Dev Container Specification.
[301.06 --> 314.10]  And like Jared was describing, Dev Containers are, if you haven't heard of them before, this really awesome tool to help you get up and running with applications or projects or repos that you're working on without having to really download anything locally.
[314.10 --> 322.14]  Especially depending on your setup, maybe you need Docker locally, but you can also do other cloud-based environments like GitHub Codespaces like Jared was describing.
[322.32 --> 325.10]  So that way you really don't even have to download or run anything locally.
[326.12 --> 329.26]  And essentially there's a couple of files that configure Dev Container.
[329.48 --> 331.70]  And so that's what was added to the changelogs repo.
[331.70 --> 337.96]  So there's a devcontainer.json, which just describes the metadata about what should go into your container.
[338.42 --> 348.88]  And then you can also link out to a Docker file, which you may have heard of or be familiar with if you've worked with containers at all that can talk about some other things to install or set up for your environment.
[349.84 --> 357.00]  And with Dev Container.json, you can really extend it with what you want specifically for a development environment.
[357.00 --> 367.44]  And so with containers in general, if you've heard of them or used up in other applications, you may think, okay, cool, that's a way to standardize what my app has when it's deployed or when it's off running in production.
[368.04 --> 376.78]  But there's a lot of other opportunities to standardize what your app is doing or how you're working on it earlier on from when you're developing it to doing CICD and testing.
[376.78 --> 387.46]  So then having a dev container now, which can have that same consistent tool set and languages, whatever your app needs from development all the way to production and testing, it really ensures that I know how it's running.
[387.68 --> 390.40]  When I'm testing it, I'm going to get that same experience that's deployed.
[390.94 --> 395.26]  Other teammates get that experience, too, because it can all be checked directly into the source code or the repo.
[395.26 --> 403.64]  And it tries to kind of take away some of the worries you may have, like, oh, Linux or Docker container seems hard or complex.
[403.64 --> 416.24]  We really try to simplify some things with scripts or other ways that it's like, hey, I can add this and I can add really advanced functionality, but I don't have to go learn everything about how to be a Linux scripting expert to get started.
[416.24 --> 426.96]  I love it conceptually. I know that when Docker first became a thing and people started using it, I thought of Docker as a thing to put production stuff in.
[427.22 --> 430.62]  And then I thought, well, I'll just put my development stuff in there.
[430.76 --> 436.66]  And then when I'm ready, I'll do like Docker go prod mode or something and I would be done.
[437.18 --> 441.02]  And what I realized quickly was it wasn't the case.
[441.02 --> 447.46]  Like it was kind of you could do them both, but most people use it for dev or like some people were using it for prod back then.
[447.52 --> 453.80]  Really, it was dev first and it was really cool to be able to like ship your dev environment around to people via this Docker file.
[454.16 --> 464.66]  But it was what burned in my mind back then was how different dev and prod really were with regard to the containers and I guess the concerns of those containers.
[465.22 --> 467.00]  They always seem to be slightly different.
[467.00 --> 474.20]  And that's something that you guys point out on the website is that dev containers and production containers often have different needs.
[474.28 --> 477.40]  And dev containers usually have a lot more needs.
[477.54 --> 478.20]  Is that right?
[478.68 --> 479.52]  Yeah, exactly.
[479.82 --> 486.12]  So you could think of if I'm opening up my favorite editor IDE and what am I typically using to work on my project?
[486.26 --> 494.50]  Like, yeah, if it's a Python app, I'm going to need Python installed and I'm going to need that whether I'm in the process of creating my project or if it's deployed.
[494.50 --> 501.30]  But also, maybe I have some specific editor settings that I like or maybe I have a theme or maybe I have extensions or plugins.
[501.30 --> 509.94]  It'd be awesome if, hey, that really helps with my development every time, especially if it's language specific extensions that really enhance my coding experience.
[510.34 --> 513.14]  If I can just make sure every time I'm opening up my editor, those are already there.
[513.24 --> 523.92]  That saves me time and that helps that if other people are working on this project too, I don't have to tell them, oh, hey, like, go check out this contributing file and figure out all these extra things you need to install.
[524.04 --> 528.52]  It's like, hey, just make sure that you have your dev container JSON and the branch you're working on and you're good to go.
[528.52 --> 532.26]  So, that is kind of beautiful that that can work like that.
[532.36 --> 534.56]  I mean, it's been a while since Docker.
[534.68 --> 536.46]  I mean, like, Docker's been around.
[536.64 --> 537.18]  It's gotten better.
[537.26 --> 538.02]  This has been more mature.
[538.10 --> 544.32]  And I kind of feel like the resistance is somewhat futile for this cloud world to take over our dev environments.
[544.42 --> 546.14]  We talked to Corda Wilkerson about a while back.
[546.80 --> 551.02]  I think it was called Coding in the Clouds, honestly, with Codespaces, which is a cool title for the show.
[551.02 --> 558.86]  But I think ever since then, we've had this idea to get changelog.com into a Codespace or into this, like, Codespace is friendly, essentially.
[559.70 --> 566.36]  And only until this commit to this drive-by contribution to help us are we somewhat there.
[566.94 --> 570.02]  And the cool thing is, is that person wanted to contribute.
[570.84 --> 572.66]  And I think this is really great for open source, right?
[572.66 --> 579.88]  Like, this is not just good for, like, dev environments and, like, plugins and extensions and themes and all these extra things that make your time go fast.
[579.88 --> 593.36]  But also, like, well, we would love to encourage folks not to just contribute, but, like, just to play a role in where our platform is going and where this community is going in terms of how we entertain and inform developers over many, many years, decades now.
[593.66 --> 594.72]  Or at least one decade.
[594.84 --> 596.96]  Maybe it would be two decades, Jerry, if we're lucky, right?
[597.14 --> 597.58]  Roundup.
[597.60 --> 598.76]  Decade, right?
[598.84 --> 599.72]  For a decade now.
[599.72 --> 601.88]  It started as a contribution to get into the cloud.
[601.98 --> 602.72]  I think this is kind of cool.
[602.84 --> 605.98]  But do you feel like, maybe, Jerry, this is more towards you.
[606.14 --> 612.62]  Like, do you feel like this is futile, this resistance towards, like, cloud, dev environments, running this thing like that?
[612.66 --> 615.00]  Like, do you think it's resistance to just, like, forget it?
[615.46 --> 618.28]  I feel like you are attacking me personally at this point because I am resistant.
[618.50 --> 626.74]  Well, as Bridget will probably point out, you know, Codespaces is very much in the cloud insofar as you're literally running it in a browser tab, right?
[627.42 --> 628.42]  And that's one thing.
[628.42 --> 637.26]  But what this dev container thing provides is not just, it's cloud-based coding, but you're still local with your VS Code, for instance.
[637.40 --> 644.92]  And, of course, as we talk about the spec and what your team's desires are for this spec is it's going to be more than just VS Code.
[645.36 --> 646.90]  It can be more than just Codespaces.
[646.90 --> 651.62]  Of course, Microsoft is really front-running this idea and this spec.
[651.94 --> 664.86]  I do think it's probably futile because there's so much upside to the containerization, to the repeatability, to the sort of, like, your dev infrastructure as code.
[664.94 --> 666.16]  Like, having it all right there.
[666.16 --> 668.62]  And then just teamwork, you know?
[669.02 --> 671.60]  Teamwork tends to be what makes the dream work.
[671.72 --> 672.08]  I don't know.
[672.26 --> 673.24]  What do you think, Bridget?
[673.28 --> 673.78]  Is it futile?
[674.00 --> 675.16]  I was going to say the same thing.
[675.32 --> 677.08]  I was like, maybe that's too cheesy.
[677.20 --> 678.42]  But you said it first, so.
[678.62 --> 678.96]  Sorry.
[678.96 --> 683.78]  Oh, I never let a cheesy moment go by.
[684.68 --> 685.08]  Yeah.
[685.30 --> 692.02]  I mean, I think as well as we're seeing all these kinds of systems and tools and tooling get better.
[692.22 --> 698.70]  Like, we're seeing cloud-based environment not be something where it's like, well, like, I'm probably going to lose all my work there.
[698.80 --> 699.76]  It's not going to run right.
[699.88 --> 703.34]  It's like, no, it probably is going to be a pretty consistent, reliable experience.
[703.34 --> 711.68]  And then, yeah, if maybe you don't have an internet connection or there's times where, yeah, like, I don't know, maybe I just prefer to have it locally on my machine.
[712.14 --> 717.72]  Having that same consistent dev container setups, that way I could use it in local VS code.
[717.80 --> 719.80]  And what we have is called the dev containers extension.
[720.10 --> 723.62]  Or I could even use it just on the CLI, so out of any kind of editor.
[724.02 --> 731.92]  Because what's backing the dev containers extension and what's backing GitHub Codespaces is a CLI that can read in, hey, your project has a dev container JSON.
[731.92 --> 738.24]  So let's go ahead and, like, set things up right so that way you can, like, develop in this development container.
[738.84 --> 740.74]  And so we've now open sourced that CLI.
[740.90 --> 745.06]  So, hey, no matter where you want to code, you can have a consistent dev environment anywhere.
[745.98 --> 746.08]  Yeah.
[746.68 --> 751.34]  I think for me the resistance has been against layers, like adding more and more layers.
[751.60 --> 755.58]  And for me, especially running on a Mac, Docker was always so slow.
[756.12 --> 758.06]  And I know there's been a lot of work put into that.
[758.14 --> 759.46]  I think it's gotten faster lately.
[759.46 --> 762.38]  I just never liked the Docker dev experience.
[762.38 --> 765.16]  That's why I was very excited that it was going to be, like, a production thing.
[765.22 --> 767.86]  And that eventually manifested, at least in terms of containers.
[768.42 --> 771.38]  But I just didn't want so many layers.
[771.78 --> 777.38]  And very little upside, especially working on small or individual projects, which I often do.
[777.78 --> 778.84]  And so that's my resistance.
[778.84 --> 788.90]  But when I see the upside and when I see the effect of the layering not be as dramatic as it has been in the past, we're like, wow, it's super slow now because I'm running through Docker.
[789.74 --> 793.14]  Whereas it could be super fast because I'm right here on my local machine.
[793.14 --> 799.34]  And I think that I will not be as resistant in the future as I have been in the past.
[799.70 --> 801.10]  At least I hope not to be.
[801.30 --> 802.20]  You know, I am getting older.
[802.66 --> 803.82]  We do get set in our ways.
[803.82 --> 810.26]  At a certain point, for a lot of us, at a certain point, progress just kind of goes on.
[810.60 --> 812.28]  And we just kind of stop at a certain place.
[812.36 --> 812.92]  Maybe I'll get there.
[812.98 --> 813.30]  I don't know.
[813.50 --> 814.86]  I hope not to as a developer.
[815.18 --> 817.28]  But I was just thinking this reminds me of like a smell.
[817.28 --> 821.36]  Like this is something that I think Steve Jobs kind of talked about back in the day.
[821.42 --> 826.04]  One of the more famous kind of interviews or quotes, I'm not really sure how you describe it.
[826.06 --> 829.94]  But one thing he said was you have to work backwards from the user experience.
[830.42 --> 830.56]  Right.
[830.60 --> 840.34]  I think this is an example of a smell like your user experience, Jared, you desired is just not what traditionally a cloud based environment would really give you or Docker would give you.
[840.40 --> 841.74]  It's sort of like as these layers.
[841.74 --> 857.64]  And so this is a problem that Bridget, you and her team, I'm sure, are probably very keen on and very sure of because you have to work from what's the user experience we desire back from the tech versus here's dev containers and what it offers and fit it into these non-round holes.
[858.42 --> 860.50]  You know, that's really what I think comes to mind here.
[860.54 --> 865.30]  It's like how close are we to this being the, I guess, magic slash silver bullet?
[865.30 --> 872.14]  Did you work backward from the experience to the tech or was it tech and then, hey, here's this beautiful tech.
[872.50 --> 873.42]  Where's the use for it?
[873.78 --> 887.50]  Yeah, I mean, I think definitely starting with user feedback, the users and what we want their experience to be, what we really hope to do with anything dev container related or even just beyond in general product VS Code sense and all that.
[887.50 --> 895.62]  So we first published the remote development extensions in VS Code where dev containers is one of them in 2019.
[896.06 --> 905.26]  And that was really with the mindset of, hey, like we're getting this customer feedback that I want to develop in something that has maybe the tools that I already need.
[905.26 --> 917.70]  And I don't need to clutter my local development environment or it can be overwhelming or for some of our other remote development experiences, like we have a remote SSH extension or we have a remote WSL or Windows for subsystem for Linux extension.
[918.54 --> 926.42]  And so with those, it's like we also got similar feedback of, hey, I want to use the Windows subsystem for Linux, but maybe it doesn't interface with VS Code super nicely.
[926.42 --> 927.46]  And I love VS Code too.
[927.46 --> 928.12]  What can I do?
[928.42 --> 938.46]  I'm always like developing on a VM or on my desktop in the office when I'm away, but it'd be great if I could just have something that's like faster and I don't have to upload and download files specifically.
[938.46 --> 941.34]  It's all just there already and feels more built in and more native.
[942.04 --> 948.42]  So I think like getting that feedback is really what's sculpted of, hey, let's start investing in remote development as that's something that people really need.
[948.48 --> 951.16]  And that's where the market and user needs are going.
[951.16 --> 958.14]  And then from there, yeah, as we design new things with dev containers and trying to make it easier for users to use and helping them a variety of apps.
[958.30 --> 960.72]  It's always coming back to like, what are they asking for?
[960.84 --> 964.04]  What are our top feature requests and issues and all that kind of stuff?
[964.08 --> 966.88]  Because all this, we really work in the open as much as possible.
[966.88 --> 971.56]  So getting that user feedback is something we really value and we really try to incorporate it every step of the way.
[972.66 --> 975.84]  Is this VS Code users is like Visual Studio Code?
[976.00 --> 979.08]  Is there a difference between like Visual Studio Code and VS Code?
[979.22 --> 979.90]  Same thing.
[979.90 --> 983.86]  If you want to write out the whole name of Visual Studio Code, you totally can.
[983.96 --> 985.02]  VS Code is the same.
[985.16 --> 985.94]  When did it merge?
[986.06 --> 988.04]  Wasn't there like a paid version that wasn't open source?
[988.32 --> 989.44]  Well, it's Visual Studio.
[989.76 --> 991.42]  Visual Studio is a separate IDE.
[991.78 --> 992.00]  Right.
[992.50 --> 992.86]  Okay.
[993.46 --> 994.72]  Such a confusing thing for me.
[994.76 --> 997.58]  I'm still, see, I'm still unclear to this moment right now.
[998.04 --> 998.30]  Clarity.
[998.74 --> 998.94]  Yeah.
[999.04 --> 999.26]  Yeah.
[999.36 --> 1003.04]  It's tough because it broke off of Visual Studio, which was Microsoft's big IDE.
[1003.42 --> 1004.60]  Still exists today, right?
[1004.64 --> 1005.54]  Still progressing.
[1005.54 --> 1011.06]  But VS Code, Visual Studio Code was, you know, we remember the story of VS Code, Adam.
[1011.12 --> 1013.48]  We told it back in the day at Microsoft Build.
[1013.72 --> 1014.10]  Yes.
[1014.52 --> 1015.96]  Bridget, perhaps we have you here.
[1016.00 --> 1018.16]  We have a VS Code representative with us.
[1018.74 --> 1022.92]  Maybe you can dispel this notion that I've floated into the ether before.
[1022.92 --> 1028.50]  As VS Code continues to get better, but also just get more stuff, more and more and more
[1028.50 --> 1029.06]  and more and more.
[1029.60 --> 1034.64]  It's like, is there a future where VS Code is basically an IDE?
[1034.90 --> 1039.52]  Like, is it going to get so much that you'd say, well, we have two IDEs?
[1039.68 --> 1044.52]  Or is it always going to be a text editor with a bunch of niceties and features?
[1044.90 --> 1046.48]  Just curious from your perspective.
[1046.66 --> 1050.62]  Is that something you all think about as a potentiality, something you're trying to avoid,
[1050.76 --> 1051.00]  et cetera?
[1051.00 --> 1056.82]  Yeah, I mean, I think at its core, we always call VS Code an editor rather than a full-fledged
[1056.82 --> 1058.94]  IDE or integrated development environment.
[1059.42 --> 1062.56]  And I think that it's kind of somewhere in between.
[1062.78 --> 1062.88]  Right.
[1062.96 --> 1068.20]  So it's like maybe more than just like a super simple editor without many additions, because
[1068.20 --> 1073.18]  when you can have extensions that can do basically anything you can think of and other kinds
[1073.18 --> 1078.40]  of support we're adding and everything with remote, it's I don't think we would go to,
[1078.40 --> 1080.28]  hey, eventually, yeah, it'll just be an IDE.
[1080.28 --> 1081.30]  That's what we'll call it.
[1081.36 --> 1085.36]  But I think we just want it to be the tool that you can edit anything from anywhere.
[1085.60 --> 1087.30]  It's kind of the tagline we've been adding on.
[1087.66 --> 1093.78]  So in 2021, we released VS Code for the Web or VS Code.dev.
[1094.06 --> 1099.26]  So you can just go in your browser, type in VS Code.dev, and you'll see a version of VS Code
[1099.26 --> 1100.80]  running just entirely there in the browser.
[1100.96 --> 1102.04]  You didn't have to download anything.
[1102.04 --> 1107.90]  So with that, and then as we have a growing set of remote experiences and just more extensions
[1107.90 --> 1112.74]  and features overall, I think it's cool to see how much we can push VS Code and scenarios
[1112.74 --> 1115.30]  users are interested in and contributing back as well.
[1115.44 --> 1119.96]  But we always keep things like performance and not being too overwhelming in mind as well.
[1120.08 --> 1124.74]  So we try to keep the bigger vision as well of meeting what users want and what is more
[1124.74 --> 1128.32]  modern development without being like, let's just build everything in.
[1128.32 --> 1132.30]  I think you can kind of see it as there's a series of extensions you install as well or
[1132.30 --> 1133.30]  different things like that.
[1133.36 --> 1137.32]  It's not just we're going to build in all of these extensions for you always or something.
[1138.18 --> 1138.80]  I think that's wise.
[1138.90 --> 1146.66]  I think it'd be a shame if VS Code became so full of stuff that it was a full-on IDE by default.
[1147.16 --> 1150.52]  I mean, heck, you wouldn't really want to run that inside your web browser necessarily
[1150.52 --> 1153.74]  because it takes so long to load up or so much memory to run.
[1153.74 --> 1158.18]  So I've always liked that you had a clear break from Visual Studio.
[1158.32 --> 1159.32]  And a fresh start.
[1159.74 --> 1165.46]  And I think the editor over time has stayed relatively fast and lightweight.
[1165.70 --> 1167.22]  And it feels like you can just launch it immediately.
[1168.06 --> 1171.56]  And then from afar, I just see all the additional improvements and stuff.
[1171.62 --> 1173.42]  And I'm just like, wow, it's getting very full featured.
[1174.02 --> 1176.36]  And then I'm like, do they need Visual Studio eventually?
[1176.56 --> 1177.60]  Does it become one?
[1177.86 --> 1180.20]  Do they merge branches there?
[1180.30 --> 1183.12]  But I think you guys have a clear vision of what you want to do.
[1183.12 --> 1185.56]  And I think it's a pretty good one.
[1185.98 --> 1191.24]  With regard to what you say, you said, code anything anywhere.
[1191.46 --> 1192.84]  Is that the slogan?
[1193.30 --> 1193.50]  Yeah.
[1193.78 --> 1197.76]  We like to say, yeah, you can work on, edit, code anything from anywhere.
[1198.40 --> 1199.34]  Anything from anywhere.
[1199.54 --> 1200.64]  That's a, I like that one.
[1200.72 --> 1202.22]  So you're kind of on the anywhere side, right?
[1202.22 --> 1208.64]  Like your focus and your work is on the remote aspect, the anywhere aspect.
[1209.20 --> 1213.06]  How long have you been working on this spec in particular, dev containers?
[1213.06 --> 1228.82]  And when did you decide to take it beyond just a VS Code internal thing that allows VS Code to do remote and containers and stuff to be like a spec that you want other people to contribute to and other products and tool chains to adopt?
[1228.82 --> 1229.22]  Yeah.
[1229.54 --> 1234.58]  So I've been on the VS Code team since 2020.
[1235.64 --> 1239.90]  And I first joined and focused on the remote extensions.
[1240.36 --> 1243.92]  We had three main remote extensions, WSL, SSH, and dev containers.
[1244.44 --> 1249.10]  And then over the next year as well, we work really closely with the GitHub Codespaces team.
[1249.26 --> 1250.82]  And they also support dev containers.
[1251.24 --> 1253.82]  Just it's in the cloud instead of on your local machine.
[1253.82 --> 1268.00]  And as we were working on our dev containers extension and working with Codespaces, we saw, hey, like dev containers can be something broadly useful beyond just VS Code or GitHub tooling or Microsoft tools.
[1268.20 --> 1272.90]  It's something that people want to use even if they don't use VS Code or maybe they can't.
[1272.96 --> 1276.92]  Maybe their company uses something else or maybe they're doing all their work in the command line.
[1276.92 --> 1284.70]  And it makes sense to open it up as, hey, this is kind of like a standard that other people, other tools, other scenarios can adopt.
[1284.90 --> 1287.76]  And it doesn't need to be inherently tied just to VS Code.
[1287.88 --> 1289.02]  It's a general concept.
[1289.54 --> 1297.00]  It supports instead of like becoming its own container orchestration format, we're seeking to just enrich other ones.
[1297.20 --> 1299.08]  So we're not trying to replace other things.
[1299.08 --> 1304.58]  We're trying to say, hey, how can we interact and interop with them and just support people with what they want to do and want to contribute?
[1304.58 --> 1313.40]  So then we started openly working on the dev container spec the beginning of last year, maybe the end of the year before.
[1313.64 --> 1315.86]  So it's been year, year and a half or so.
[1316.08 --> 1321.48]  But I think like a vision going in was, hey, we don't think dev containers have to be tied to VS Code.
[1321.58 --> 1326.06]  And that was even when they were only a dev containers extension and GitHub Codespaces thing.
[1326.50 --> 1328.72]  So that's why the file is like devcontainer.json.
[1328.82 --> 1332.96]  It doesn't have to say specific things about VS Code in the file name or in its content.
[1332.96 --> 1338.96]  And we've even been taking steps as we've been working on the spec to generalize it beyond VS Code or Codespaces.
[1339.24 --> 1345.68]  So for certain properties in dev container JSON, like settings or extensions that may not make sense in other tooling,
[1346.18 --> 1351.20]  we've now extracted them to a top level property for specifically VS Code and Codespaces.
[1351.44 --> 1353.32]  That way it's like, hey, use those tools.
[1353.42 --> 1353.70]  Awesome.
[1353.96 --> 1354.76]  They can handle it.
[1354.76 --> 1362.54]  And then over time, other supporting tools, as other tools decide to support the spec or contribute to it, could also reserve their own properties in there as well.
[1362.74 --> 1365.70]  So it's all under customizations.convision.
[1365.84 --> 1366.96]  There could be any tool in there.
[1366.96 --> 1376.96]  Yeah, I think it's really cool to open this up and have, you know, other tools, other sites, other cloud things adopted.
[1377.12 --> 1386.20]  I do think that Codespaces is such a killer intro to the possibility of using dev containers because it reminds me, I don't know about you, Adam,
[1386.20 --> 1393.02]  but it kind of reminds me of that deploy to Heroku experience, you know, the one click button where you could take this current thing you're looking at,
[1393.12 --> 1396.94]  deploy it as your own Heroku app and be running it in the cloud.
[1397.56 --> 1406.26]  Those have been replaced with, I don't know, deploy to Vercel, deploy to Netlify, deploy to whatever's, maybe not replaced, but augmented in recent years.
[1406.26 --> 1418.42]  That experience, like the fact that we can just say now, just go to our repo, click on the little code button in the corner and say launch on Codespaces or whatever the button says right there.
[1418.84 --> 1418.98]  Yeah.
[1419.36 --> 1423.60]  And literally three to five minutes later, it's not, it's not, it's not immediate.
[1423.94 --> 1428.80]  It's, it's close because of course there's lots of stuff that has to get set up inside of that container, the first run experience, right?
[1428.86 --> 1430.92]  In order for it to do its thing.
[1430.92 --> 1440.70]  And all of a sudden, like, there you are, you're both looking at editing and can execute code inside of what you were just staring at.
[1441.48 --> 1443.58]  Like who doesn't want that for their project, right?
[1443.62 --> 1444.84]  Like it's awesome.
[1445.24 --> 1445.68]  Right, Adam?
[1445.90 --> 1446.38]  It's killer.
[1446.82 --> 1447.10]  For sure.
[1447.84 --> 1448.70]  It's a beautiful thing.
[1448.76 --> 1451.22]  I mean, you need this for open source in particular.
[1451.36 --> 1458.34]  Like it's what a, what a great thing for would be contributions that just get stopped because it's like, oh gosh, this contributing file.
[1458.72 --> 1459.02]  Yeah.
[1459.02 --> 1469.16]  I love your stack, but I don't want to mess my pristine, you know, machine up or I don't want to deal with any of this stuff or I want to, you know, whatever, for whatever reason, it's, it's just, there's a blocker there.
[1469.80 --> 1477.24]  Or even I think when I was watching your YouTube series, Bridget, one thing I thought was pretty interesting was being able to jump around tech stacks.
[1477.86 --> 1479.06]  That's kind of cool, right?
[1479.06 --> 1490.56]  Like if you are traditionally a web stack developer, but you want to jump into a, you know, a backend focused thing or something like that, or into a whole new Python world, you know, you can sort of move around different stacks.
[1490.56 --> 1497.12]  And so that kind of like encourages the possibility of polyglot to some degree, or at least contributions to polyglot worlds.
[1497.54 --> 1505.72]  You know, even if it's not something you're like a primary contributor to it, but you're able to put your own contribution in, whether you're a designer or documentation or whatever it might be.
[1505.80 --> 1513.66]  Like there's, to be able to move around like that, I think it's a pretty interesting and compelling reason to, to consider the possibility with dev containers.
[1513.66 --> 1515.68]  Yeah. I think that's a great point.
[1515.94 --> 1521.58]  So the contribution we have, it's got a dev container dot Jason file. It's got a dark compose dot YAML file.
[1522.26 --> 1527.04]  You know, what part of this is the dev container spec and what part of this is code spaces?
[1527.44 --> 1533.60]  Where is the line, I suppose, in that world? Is it like they adhere to or support your spec?
[1533.78 --> 1535.14]  Do they have their own spec?
[1535.14 --> 1545.16]  Like demystify, I guess, the ambiguity there between like where the dev container spec comes into play for us in regards to this contribution and then running that on code spaces?
[1545.68 --> 1550.72]  Yeah. So you can kind of think of the spec is essentially that dev container dot Jason file.
[1551.08 --> 1562.30]  So we're seeking to enrich other formats, whether it's a Docker file or a Docker compose or maybe potentially others over time with metadata from the dev container Jason.
[1562.30 --> 1565.66]  So it can include those tool specific things like we were mentioning.
[1566.12 --> 1574.00]  It can also be a spot where you can add or install other scripts or technology or parts of your tech stack there like you might do in a Docker file.
[1574.10 --> 1575.78]  You could instead do it in the dev container Jason.
[1576.08 --> 1579.26]  We have ways to kind of built in to make that easier for you to add more features.
[1580.12 --> 1586.34]  So really dev container Jason is going to be the core of, hey, like this is what is defined by the dev container spec.
[1586.34 --> 1597.82]  And then you can also then think of like a reference implementation for the spec or what is an example of how other tools could implement the spec over time is a dev container CLI that we open source.
[1598.16 --> 1602.12]  So go to github.com slash dev containers slash CLI.
[1602.12 --> 1608.46]  You'll see there's like, hey, that's the backing CLI that Codespaces uses and that the dev containers extension uses.
[1608.70 --> 1617.46]  And that CLI is then how those tools are able to read in a dev container Jason and build a dev container or dev environment from it and make sure that the spec is supported.
[1617.46 --> 1629.52]  So then if another tool or individual wanted to support the spec, they could use the CLI and whether they integrated it into an editor or just used it in a terminal, that'd be considering, hey, like I support the spec here.
[1629.60 --> 1631.46]  I'm using the reference implementation of the spec.
[1632.08 --> 1638.86]  But there could also be like if somebody wanted to make modifications to the CLI, they could contribute those back or just use their own modified version too.
[1638.86 --> 1643.86]  So these are the essential Lego, not the finalized Lego that you could build.
[1643.96 --> 1651.46]  These are the components that you could build, you know, to support essentially running code remotely or in a Codespaces.
[1652.08 --> 1656.48]  So if I was, you know, if I wanted to build my own Codespaces, I could use the CLI tool.
[1656.62 --> 1663.06]  I can use different things and leverage essentially what you built to adhere to that spec and be able to do all those different things.
[1663.06 --> 1674.30]  Yeah, if you want to build your own tool that supports dev containers like you're seeing in Codespaces, you're seeing the dev containers extension, you can then use that same exact CLI and then hook it up to specifically what your tool needs.
[1674.38 --> 1680.44]  So if your tool needed other kinds of things, like maybe you have your own settings or extensions or names for those things or other properties.
[1681.10 --> 1682.88]  Maybe you work with secrets in a certain way.
[1683.36 --> 1688.70]  You could then make sure, oh, like the version of the CLI you're using respects or adds those kinds of properties.
[1693.06 --> 1697.26]  This episode is brought to you by our friends at Square.
[1697.48 --> 1699.20]  Develop on the platform that sellers trust.
[1699.48 --> 1700.42]  Here's what you could do with Square.
[1700.52 --> 1701.98]  You could bridge more experiences.
[1702.16 --> 1707.86]  You could build online, mobile, and in-person commerce experiences that connect more customers and sellers.
[1708.22 --> 1710.04]  You can build custom booking solutions.
[1710.24 --> 1711.32]  You can create and track orders.
[1711.42 --> 1712.34]  You can accept payments.
[1712.56 --> 1714.44]  You can manage and curate inventory.
[1714.78 --> 1715.92]  You can organize customers.
[1716.04 --> 1716.94]  You can manage employees.
[1717.40 --> 1719.58]  You can extend Square gift cards to your app.
[1719.58 --> 1720.58]  You can use Afterpay.
[1720.58 --> 1730.78]  Afterpay and all this is powered by the world-class Square APIs and SDKs that enable you to build full-featured business apps for yourself or millions of Square sellers.
[1731.40 --> 1733.86]  So much is available as a Square Solutions partner.
[1734.30 --> 1736.92]  Learn more and get started at changelog.com slash Square.
[1737.06 --> 1739.66]  Again, changelog.com slash Square.
[1739.66 --> 1767.90]  What's the experience like as a user of VS Code today?
[1767.90 --> 1771.00]  Let's say I open up VS Code, a project.
[1771.30 --> 1774.54]  I've cloned a repository that has a dev container JSON file.
[1775.44 --> 1778.56]  What does that change about the VS Code environment?
[1778.96 --> 1780.86]  Which extra buttons do I get?
[1781.14 --> 1786.32]  Or what all does it do, assuming the dev container does what a typical dev container does?
[1786.74 --> 1788.42]  I'm sure there's atypical things, too.
[1788.52 --> 1792.24]  But just generally speaking, what does it do for the experience of VS Code?
[1792.24 --> 1802.90]  Yeah, so VS Code will detect if you have a .dev container folder or if you have a dev container JSON, which could be in that .dev container folder or at the root level of your project.
[1803.32 --> 1806.86]  And it'll recommend, hey, it looks like your project has a dev container configuration.
[1807.10 --> 1811.16]  Reopen in there to develop even more effectively or something along those lines.
[1811.16 --> 1817.20]  And then you'll have the option to reopen in that dev container, which will use the dev containers extension.
[1817.78 --> 1825.50]  So if you're familiar with the VS Code model of programming, it's essentially if you want different features, different functionality, you can install it through extensions.
[1825.50 --> 1829.86]  So we have a dev containers extension that then you can install from the VS Code marketplace.
[1830.38 --> 1837.60]  And that'll give you all the functionality to rebuild dev containers, reopen within them, add dev container configuration files.
[1837.80 --> 1845.88]  So it'll guide you through that process of creating a dev container JSON and adding things to it, adding the languages or tool sets that you need.
[1846.00 --> 1849.34]  So you don't have to look at me like, well, I've never used a dev container JSON.
[1849.62 --> 1851.22]  I don't know what to add or what to do.
[1851.22 --> 1855.36]  We try to guide you through that, through different quick picks and different checkboxes.
[1855.42 --> 1859.94]  You could be like, I want Git and I want Python and I want Node.
[1860.08 --> 1861.42]  You can just checkbox all of those.
[1861.86 --> 1864.04]  It'll be in your project and then you can just reopen in it.
[1864.76 --> 1869.76]  And the dev container JSON, at least the one that we got from Chris Eggert, is super basic.
[1869.98 --> 1878.86]  I mean, it's basically 10 lines and it's mostly setting up a workspace, a couple of port forwards, and then pointing to the Docker compose file that Adam was referencing.
[1878.86 --> 1885.90]  And the Docker compose file is the one that's actually doing the job of getting your container all set up for development.
[1886.44 --> 1897.68]  So if anybody's already using Docker compose for their own personal development environment, all they need to do is add the dev container JSON and point it to the right things.
[1897.84 --> 1900.10]  You know, a little bit of configuration goes a long way.
[1900.16 --> 1903.22]  And now all of a sudden you can run that same environment in code spaces.
[1903.22 --> 1912.50]  You can get the VS Code extras as well as hopefully as time passes other tooling that adopts this spec.
[1913.24 --> 1918.94]  So you're just you're really just a dev container JSON away from opening up that environment to lots more people.
[1919.50 --> 1920.48]  Yeah, I like that statement.
[1920.60 --> 1922.08]  You're a dev container JSON away.
[1922.38 --> 1924.10]  You can use that as a tagline.
[1924.76 --> 1925.42]  Oh, yeah.
[1925.82 --> 1926.44]  I like that, too.
[1926.54 --> 1930.26]  And you can even add you can even add more stuff to your dev container JSON.
[1930.26 --> 1936.94]  So I was mentioning like, oh, what if I'm thinking I really just need Python in this project?
[1937.14 --> 1938.64]  And like, how should I add it?
[1938.72 --> 1946.18]  I could install it in the command line, but then either I have to install it locally or if I install it in the command line in my container, it'll get lost eventually.
[1946.18 --> 1950.50]  If I kill this container, should I install it in the Docker file or somewhere else?
[1950.98 --> 1953.50]  So we have this concept called dev container features.
[1953.50 --> 1964.06]  So that's the steps that VS Code or code spaces or other tools can guide you through via checkboxes of, hey, here's a list of features and maybe just want to install one of them.
[1964.16 --> 1967.82]  Maybe you want to install a bunch of them and then it'll list those in your dev container JSON.
[1968.60 --> 1974.80]  And even if you're not using tooling like VS Code, you can just add those to your dev container JSON via a features property.
[1974.80 --> 1982.62]  So you can say features and then name whatever feature you want to use and could be one you create or one that the community or someone in your company created.
[1982.88 --> 1986.44]  And we have a list that community members contribute a feature.
[1986.60 --> 1991.00]  So that way it's like, hey, I wrote this really awesome feature for something I work on or something that I use.
[1991.02 --> 1992.34]  And I think other people want to use it.
[1992.64 --> 1994.00]  You can add it to the index, too.
[1995.16 --> 1996.68]  So how far do you go with that?
[1996.68 --> 2001.54]  Because I expect, you know, we have so many different ways of specifying, you know, like editor config.
[2002.42 --> 2004.06]  Then you got your VS Code config.
[2004.26 --> 2005.26]  Maybe you got your Vim config.
[2005.44 --> 2006.82]  Maybe you have your git ignore.
[2007.66 --> 2009.30]  Of course, that's just a file that's in your repo.
[2009.42 --> 2014.86]  But there's just so many different ways that we specify what how to configure our environments.
[2014.86 --> 2024.48]  And some of those we want to be global across the project, linters, et cetera, style rules, maybe requirements for documentation.
[2024.48 --> 2026.74]  I don't know, there's a thousand different things you can think of.
[2026.98 --> 2029.52]  Some of those things are like personalized to the developer.
[2029.74 --> 2032.06]  And then other things are like, no, this is the whole project.
[2032.20 --> 2033.40]  What do you guys have found?
[2033.88 --> 2040.18]  You probably have more experience with devcontainer.json files than anybody that are like smart things that people are doing to share.
[2040.56 --> 2043.72]  And like, hey, go ahead and put your editor config right here in your dev container.
[2043.72 --> 2046.74]  Or no, that should be a thing that lives somewhere else.
[2047.12 --> 2047.64]  What are you finding?
[2047.64 --> 2056.62]  I think the way you put it of is this something that the project really needs or is this something that I just like using or that I need is really a helpful distinction.
[2057.14 --> 2066.70]  So I think if it's something that's super specific, like, hey, I like this editor theme or I like my editor sidebar configured this way or this specific editor setting.
[2066.70 --> 2074.22]  If it's just a dev container that you're using for your own personal projects, then totally put UI and very specific things in it.
[2074.62 --> 2080.88]  But if it feels like, hey, like probably not everyone is going to love the same VS code theme that I do.
[2081.00 --> 2087.50]  It's like, OK, I can probably maybe not put that in a dev container that I'm sharing with my whole team or the open source community on this project.
[2087.50 --> 2102.92]  So thinking about like, hey, if this project really needs this language or if maybe this linting tool is really helpful or maybe there are certain editor extensions like language support extensions like a Python or Java or C++ language extension for an editor.
[2103.44 --> 2110.60]  Those are probably really helpful additions where, yeah, maybe for some development you wouldn't necessarily need it, but it's going to make the development experience a lot better.
[2110.60 --> 2116.48]  And people aren't probably going to like strongly disagree of, no, I think my development experience is way worse than them.
[2116.60 --> 2126.22]  Then I think adding those kinds of things in that feel like will be generally beneficial to open source community or the other teammates that you have on your project are great things to add.
[2126.32 --> 2127.58]  And there's so many things.
[2127.58 --> 2129.64]  So it can definitely be a lot of different options.
[2129.64 --> 2135.34]  But just think about how generally applicable they are, I think, is the really helpful first or fundamental step there.
[2135.98 --> 2138.86]  Is there room for a .local file for that in that case?
[2138.86 --> 2142.84]  So maybe Jared and I, you know, we this moves forward and we keep loving it.
[2142.88 --> 2145.84]  And there's a dev container.json in our repo.
[2145.98 --> 2150.50]  But let's say I like a special flavor of something whenever I spin up my personalized container.
[2150.58 --> 2152.58]  Can I have a dev container.local?
[2152.58 --> 2158.38]  Is that a bad idea to have sort of a localized version where it's like, here's the dev container and here's what it does normally.
[2158.50 --> 2162.32]  But after all that's done, give me this, this and this because I'm Adam.
[2162.72 --> 2164.68]  Yeah, there's a few different ways you can handle it.
[2164.78 --> 2168.10]  So depending on the editor environment you use.
[2168.10 --> 2170.06]  So let's say you're using VS Code.
[2170.30 --> 2176.12]  There's certain specific settings you may be able to take in your editor where then you don't even need to set certain things in your dev container.
[2176.12 --> 2179.40]  Like VS Code has extensions to always install.
[2179.56 --> 2188.06]  So you could like set a list of extensions that you always want there, which could include language extensions, but also include theming or other specific UI or key bindings or things like that.
[2188.06 --> 2192.18]  But then thinking about other editors or if you don't want to use those kinds of extensions.
[2192.18 --> 2193.42]  Think like it depends.
[2193.54 --> 2204.66]  Like there could be, you could actually have multiple dev container jasons in a project and then you can, depending on how the supporting tool implements it, they can guide you for, hey, which one do you want to use right now when you're working on it?
[2204.66 --> 2207.34]  So maybe you could have your own version that either.
[2207.42 --> 2213.24]  Yeah, maybe you're not checking into source code if you don't want to confuse other people or that's maybe on your own branch that you have a few.
[2213.24 --> 2217.64]  So that way you can kind of have it of, hey, like I specifically need this for this scenario.
[2217.78 --> 2221.62]  So I'm going to have this kind of dev container here, but then I need this other kind of scenario.
[2221.72 --> 2223.04]  So I'll have a secondary one.
[2223.42 --> 2229.70]  It can also be helpful for maybe if you're working on a monorepo that has different dependencies for different sub parts of the project.
[2229.82 --> 2236.32]  Then you can have multiple dev container jasons there depending on what you're specifically working on or what some of your other teammates are working on.
[2237.20 --> 2237.24]  Interesting.
[2237.90 --> 2239.08]  Keep my local flavors.
[2239.70 --> 2240.92]  I like my local flavors, you know.
[2241.00 --> 2241.98]  Gotta keep the local flavors.
[2241.98 --> 2242.94]  You're special, man.
[2243.24 --> 2244.72]  Keep it special.
[2245.46 --> 2254.06]  So when it comes to adoption, I'm Googling around frantically as we talk, like looking like, okay, is the Vim community trying to do some of this?
[2254.14 --> 2256.74]  Is the Emacs community trying to do stuff?
[2256.78 --> 2257.68]  Some people are just switching.
[2257.94 --> 2258.92]  They're just switching to VS Code.
[2259.40 --> 2265.76]  Other people are like, you know, here's an open source implementation of VS Code's dev container API.
[2266.98 --> 2271.84]  Here's a NeoVim thing that does some stuff with dev container.
[2271.84 --> 2280.04]  So it seems like they're out there, but they're not like established, you know, 30 people supporting this one plugin, etc.
[2280.96 --> 2287.56]  What do you think it's going to take to get more people on board and doing this and maybe even contributing to the spec?
[2287.56 --> 2291.34]  So you kind of have like the editor side, but then you also have like the cloud provider side.
[2292.12 --> 2295.14]  And you have two implementations, VS Code and Codespaces.
[2295.28 --> 2301.94]  But on both sides, you have like the open source, like Vim, Emacs, you know, integrated into small projects like Sublime Text.
[2301.94 --> 2304.66]  And then you have like Codespaces, Gitpod.
[2304.78 --> 2305.70]  I'm sure there's other ones.
[2307.06 --> 2307.46]  StackBlitz.
[2307.60 --> 2312.70]  Like there's a lot of cloud IDE things or, you know, web dev things in the cloud.
[2312.94 --> 2317.52]  And I'm just curious what adoption looks like or if there's a clear path to that.
[2317.96 --> 2324.34]  I just wonder as an author of a spec what it feels like to like put a spec out there and hope that people use it, you know?
[2324.34 --> 2334.14]  Yeah, when we first were announcing, hey, we're working on this spec and we open source this CLI, we announced it on, for instance, the VS Code blog or Codespaces channels too.
[2334.32 --> 2341.52]  But we wanted to emphasize, hey, like even if you're finding out about it on the VS Code blog or something, the whole point is it's not just VS Code.
[2342.06 --> 2350.36]  So I think like having that in our messaging has been really key because I think that since dev containers for a while were just a VS Code and a Codespaces thing,
[2350.36 --> 2357.50]  some folks still totally understandably think, hey, like, well, if I'm not using those tools, I don't need to add a dev container to my project.
[2357.62 --> 2363.56]  I don't really need to worry about it or it's not something for me to think about adopting in another tool or something like that.
[2363.76 --> 2368.68]  So I think like getting the word out more of like, hey, it's an open thing and you can check it out here.
[2368.80 --> 2372.78]  And we're super looking forward to like your feedback and we accept contributions.
[2372.78 --> 2376.82]  And we're happy to talk to you about questions, feedback, contributions and all that kind of stuff.
[2376.82 --> 2384.18]  Like I think just getting that open dialogue and awareness out there has been really helpful and chatting with folks who are part of different language communities
[2384.18 --> 2389.18]  or who use different tools or to drive different tools and kind of getting their feedback of like,
[2389.30 --> 2393.84]  what are gaps that maybe the spec is missing or that you feel like dev containers overall could be better at.
[2393.94 --> 2401.14]  So that way we can prioritize that in the work that our team does and also get like additional feedback and see how we should shape the future roadmap.
[2401.14 --> 2407.00]  And yeah, like we add, we have a section on the containers.dev site about supporting tools.
[2407.20 --> 2412.06]  So you'll see that it's like trickling out to some other like CLIs and projects and things like that.
[2412.16 --> 2420.26]  But I think also seeing more dev container JSON files or .dev container folders and other open source projects has been a huge help as well.
[2420.62 --> 2424.86]  So then it kind of shows like, hey, folks who are part of this community, you can check out dev containers.
[2424.86 --> 2432.98]  You can use them like getting the word there out more and getting like feedback from those users to like, hey, I'm using it for this kind of scenario and it doesn't work so great.
[2433.04 --> 2433.80]  It's like, OK, cool.
[2433.86 --> 2436.00]  Like tell us more about that and see how we can make it better.
[2436.14 --> 2440.56]  So that way it's better for this whole community and maybe other open source communities and projects over time.
[2441.56 --> 2446.06]  When you get this feedback, what are some of the, I guess, the biggest hurdles to get over?
[2446.20 --> 2450.42]  Like what are the things that really stop people or what are the things that really get people excited?
[2450.42 --> 2455.62]  Obviously, the usefulness, but like what are the things that really push back against using it?
[2456.32 --> 2465.32]  I think at the beginning, it was just them not feeling like a very open or like super adopted thing yet of like, OK, cool.
[2465.38 --> 2471.04]  Yeah, maybe there's good adoption and VS Code specific tooling, but like what other tools are using them?
[2471.12 --> 2476.26]  So sometimes it can be like a chicken or the egg problem of it's like, oh, like, should I support it or adopt it?
[2476.26 --> 2481.26]  And that'll like help other people adopt it or should I wait for other people to adopt it before I want to do it?
[2481.32 --> 2489.28]  So thinking about like, is this for sure something you all are investing in and going to keep open and going to keep freely available and no cost and that kind of stuff.
[2489.78 --> 2500.66]  So I think establishing that trust and awareness with folks is definitely something that isn't just like an easy formula of, oh, yeah, here's how we get the word out to everyone who might want to use this.
[2500.66 --> 2503.74]  And yeah, they're just going to like know and trust and understand that.
[2503.82 --> 2506.58]  Yeah, like we really want to prioritize and invest in this.
[2506.68 --> 2512.86]  But I think it's something you can just kind of show through continued action of, OK, we have an open community Slack channel.
[2513.08 --> 2517.10]  Hey, we have community discussions that we actually respond to and really want your feedback on.
[2517.10 --> 2523.94]  And so just slowly trying to build that trust and understanding and getting that open feedback channel over time has been really cool.
[2523.94 --> 2527.08]  But it's something that we kind of needed to just experiment with over time.
[2527.08 --> 2532.88]  And we're still figuring out like we're still figuring out, hey, what are some cool open source projects that this would make sense to you?
[2532.88 --> 2537.96]  And it doesn't feel like we don't want it to sound like, hey, we think dev containers are for sure the best thing for you.
[2538.06 --> 2540.64]  And we know everything about your developers or your community.
[2540.84 --> 2542.08]  So you have to take this PR.
[2542.26 --> 2545.04]  It's more, hey, like, here's what dev containers are.
[2545.32 --> 2546.72]  We think they could be a good fit.
[2546.72 --> 2550.08]  We'd love to know if you're open to this kind of PR, we can help you with it.
[2550.18 --> 2553.68]  Or is there something you feel like that we're missing that we could add or we could change?
[2553.74 --> 2555.40]  And like, what can we do to get there for you?
[2555.68 --> 2564.30]  I mean, it seems like to me the best pitch for cloud things is like, hey, here's an easy adoption avenue, right?
[2564.34 --> 2574.00]  Like you can be there with your deploy to cloud thing or develop in cloud thing X, just like the one Codespaces works on GitHub.com right now.
[2574.00 --> 2583.26]  And then on the indie side, like the developer side, I just feel like it's such an easy sell because it's like, hey, don't you want your your open source project to be immediately hackable?
[2583.56 --> 2583.78]  Yeah.
[2583.96 --> 2585.74]  Like more people can use it and contribute.
[2585.88 --> 2586.86]  That's awesome.
[2587.38 --> 2587.58]  Yeah.
[2587.62 --> 2589.18]  I mean, it's like, who doesn't want that?
[2589.18 --> 2590.70]  And I think the demystification.
[2591.00 --> 2600.50]  So for us specifically, I know we kind of wanted a Codespaces set up for a little while, but like Adam and I thought, well, we need to talk to Corey and the Codespaces team.
[2601.08 --> 2608.48]  You know, I don't think he's on the team anymore, but when he was, he came on the show and like get have them help us to set up a thing that makes it all happen.
[2608.48 --> 2617.86]  And just the knowledge of, no, you can just have a dev containers JSON on your repo and then it's, that's all you got to have is seven lines of code, you know, kind of a thing.
[2617.96 --> 2619.48]  Of course, different setups are going to be different.
[2619.66 --> 2621.40]  So we have a Docker Compose as well.
[2621.50 --> 2623.78]  You might have more stuff to do, but just like, oh, okay.
[2623.92 --> 2627.54]  And so I think that plays into this other thing you have on the website, which is the templates.
[2627.78 --> 2630.48]  You have kind of two subsections of the dev containers website.
[2631.28 --> 2637.76]  You have the features, which you talked about, but now you have the templates, which to me, I'm reading this and help me understand exactly what these are.
[2637.76 --> 2639.64]  It seems like these are like starter spots.
[2640.00 --> 2643.64]  So if you have a specific kind of project or what are these templates?
[2643.72 --> 2644.80]  Is that, am I thinking about it right?
[2644.86 --> 2646.58]  You can just kind of use one of these and take it started.
[2647.24 --> 2648.02]  Yeah, absolutely.
[2648.30 --> 2656.56]  And I think you also really nailed another challenge and something that I was kind of mentioning earlier of, hey, like, yeah, I don't know where to get started with containers.
[2656.56 --> 2663.12]  Or like maybe I've heard feedback from other folks that they're complex, confusing, time consuming, compute intensive.
[2663.42 --> 2666.80]  So is this something I want to invest in or like should I?
[2666.80 --> 2669.46]  Is this where the community or the market's going?
[2670.24 --> 2681.40]  So, yeah, we really try to make it easier to get started with dev containers and make it so that we're really taking out complexity where folks might have previously found complexity when doing containerized development.
[2681.40 --> 2686.32]  So, yeah, with templates, we have a set that we host as part of the specs.
[2686.32 --> 2693.16]  So for a variety of different languages or scenarios like Python or even just like base Ubuntu or something like that.
[2693.60 --> 2699.16]  And so it'll give you the dev container files necessary to kick off development for that kind of project.
[2699.40 --> 2705.92]  And from there, then you can totally customize it of, hey, I want to add other features or maybe I just want to add other settings or configuration.
[2705.92 --> 2707.68]  That's not in the future and that's totally OK.
[2708.08 --> 2710.76]  But we're trying to just give folks those building blocks.
[2710.86 --> 2715.40]  It doesn't feel like, hey, I'm starting from scratch and that's time consuming and that's intimidating.
[2715.40 --> 2719.96]  It's like, no, this can actually be a fun and even kind of straightforward process.
[2720.50 --> 2721.78]  Yeah, I think that's going to be key.
[2722.16 --> 2724.62]  I was looking at one of the templates there.
[2724.72 --> 2730.42]  It's Elixir Phoenix Node and Postgres, Jared, not MySQL, Postgres.
[2730.80 --> 2732.10]  So, hey, that's perfect.
[2732.20 --> 2732.70]  That's us.
[2733.00 --> 2734.18]  We need all those things.
[2734.52 --> 2736.30]  It doesn't look like ours, though.
[2736.54 --> 2742.48]  I mean, not that it has to be the same, but like there's obviously two different ways to roam in this case, at least.
[2742.48 --> 2746.58]  But I mean, so essentially what you're saying, Bridget, is this template exists there.
[2747.20 --> 2750.04]  You know, I could take the dev container dot JSON.
[2750.20 --> 2755.10]  I can take the Docker Compose YAML file, essentially pull that into my project or something like that.
[2755.14 --> 2761.12]  I haven't read the readme thoroughly, but I can essentially adopt this into my project or start a brand new one from it
[2761.12 --> 2767.42]  and have essentially the building blocks of what is our stack, Elixir, Phoenix, Node.
[2767.42 --> 2768.46]  We're not really using that.
[2768.56 --> 2772.36]  We're using NPM, of course, and different JavaScript things, but Postgres in that case.
[2772.44 --> 2776.72]  So that's essentially the building blocks of the majority of what our application stack is.
[2776.72 --> 2778.38]  Yep, for sure.
[2778.72 --> 2780.76]  And yeah, you can take it as inspiration.
[2781.08 --> 2783.12]  You could use it as your actual dev container.
[2783.42 --> 2785.18]  You can add things to it over time.
[2785.88 --> 2788.80]  And you'll see as well, we also publish a set of images.
[2789.24 --> 2792.64]  So those are going to be referenced in like our templates, for instance.
[2792.80 --> 2799.10]  And so you can kind of extract any of the things that we're publishing as, hey, maybe I can use some of this, all of this, take it as inspiration.
[2799.10 --> 2801.70]  And go from there for configuring my environment.
[2802.36 --> 2805.54]  And essentially you're spinning up a Docker image if you're doing local environment stuff.
[2805.66 --> 2812.92]  So if I'm doing this locally, this lets me spin up a Docker image that has this environment baked into it.
[2813.06 --> 2817.78]  When it comes to using VS Code or a different text editor, whether it's Vim or whatever,
[2817.90 --> 2822.66]  you have port forwarding for going into and out of the container so that I can run the application.
[2822.66 --> 2832.20]  Let's say it's on port 4000, like any typical web application that's a like 5432 or whatever for the SSL version of the application.
[2832.34 --> 2833.16]  So that's how that works.
[2833.22 --> 2833.96]  You spin up a container.
[2834.94 --> 2838.08]  Your editor is still editing the code, but it's inside.
[2838.76 --> 2840.42]  Is it inside that container?
[2840.56 --> 2841.42]  Is it just running it?
[2841.48 --> 2842.22]  Like, how does that work?
[2842.36 --> 2843.72]  Give me, break it down.
[2844.38 --> 2844.58]  Yeah.
[2844.84 --> 2849.84]  So essentially everything you're doing is living in that container you can view it as.
[2849.84 --> 2855.64]  So you could view it as like kind of our model for remote development and VS Code in general.
[2855.84 --> 2860.30]  Like you're really working in that remote environment, whether it is a dev container,
[2860.50 --> 2867.08]  whether it is the Windows subsystem for Linux, whether it is a remote VM or desktop machine via SSH or tunneling.
[2867.56 --> 2871.96]  And so that way you don't have to like copy code in and out or back and forth.
[2871.96 --> 2877.44]  Like you might have had to do in other environments or worry about, oh, like I know my remote environment,
[2877.44 --> 2881.48]  whether it's a dev container or one of the other options, like have this dependency I need it,
[2881.50 --> 2883.02]  but now I need to redownload it locally.
[2883.18 --> 2886.50]  It's like, no, you can just develop completely within that remote environment.
[2887.14 --> 2892.94]  And what's cool with dev containers too is there's a variety of ways that you can reference what you want to be set up or configured.
[2893.14 --> 2895.76]  So like you were saying, you could reference a Docker compose.yml.
[2896.12 --> 2897.68]  You could reference just a Docker file.
[2897.86 --> 2899.16]  You could reference just an image.
[2899.16 --> 2904.16]  It really depends on just like what you want to do, how you have your project set up.
[2904.30 --> 2905.80]  Are you pre-building images?
[2906.04 --> 2910.34]  So you could even have it where you're like publishing what you made in your image.
[2910.34 --> 2913.84]  So that way you can use it then in like dev container json's later.
[2914.06 --> 2916.56]  You don't have to redefine all that dev container json stuff.
[2916.68 --> 2918.72]  And other people and other projects can use them too.
[2919.26 --> 2922.46]  There's a ton of flexibility there just depending on like how your team works.
[2922.46 --> 2923.82]  And are you pre-building things?
[2923.92 --> 2925.68]  Or are you all using Docker compose.yml?
[2925.68 --> 2929.48]  So what happens whenever I spin that image down then?
[2929.62 --> 2931.96]  So if my code lives in there, my commits are in there.
[2932.02 --> 2935.76]  Does this thing have the keys to, you know, my GitHub essentially?
[2935.90 --> 2937.98]  Like how does that go one layer further?
[2938.08 --> 2940.04]  Like how am I building inside this container?
[2940.12 --> 2945.24]  And how is it ephemeral can go away, but yet I'm not losing my code like I'm five here?
[2945.54 --> 2949.56]  So yeah, essentially with containers, you have a couple of options.
[2949.56 --> 2953.72]  Or either you can mount your source code into the containers.
[2953.72 --> 2956.28]  You can use a bind mount or you can use a volume.
[2956.66 --> 2962.98]  And so then we have an option, for instance, in the dev containers extension where you can clone a repo into a volume.
[2963.48 --> 2972.00]  And so volumes are the recommended way to work with containers because then essentially it's like a little bit more optimized for how like Docker, for instance, is handling it.
[2972.54 --> 2975.68]  And so then you don't have it's like a little bit more efficient as well.
[2975.68 --> 2980.90]  So there's kind of a lot of things to get into, like volume, bind mounts, all those things.
[2981.30 --> 2983.64]  But yeah, I don't know if that's helpful.
[2984.04 --> 2985.28]  Well, I just think of like the resistance.
[2985.46 --> 2989.62]  I got to imagine part of the pushback is this confusion, I would say, right?
[2989.66 --> 2993.08]  Like, so I'm asking you to clarify it because I think there's a lot of at least it's confusing for me.
[2993.08 --> 2999.74]  So, you know, I would imagine like if you if I'm typically I'm Jared, I love my local machine.
[2999.98 --> 3002.78]  I don't mind dirtying it up, you know, however it is.
[3003.22 --> 3005.82]  Elixir, Node, NPM, install it all.
[3005.94 --> 3006.32]  I love it.
[3006.36 --> 3006.62]  Oh, yeah.
[3006.62 --> 3006.74]  Right.
[3007.04 --> 3007.66]  All the things.
[3007.76 --> 3010.40]  But then you go to the container and it's like, well, where does my code live?
[3010.48 --> 3010.62]  Sure.
[3010.64 --> 3013.16]  I understand volumes and I understand binding, you know.
[3013.16 --> 3017.50]  And if I'm developing in that container, is the code in that container?
[3017.76 --> 3019.32]  Is it still in the local repository?
[3019.90 --> 3023.10]  Does it simply just run the mirror image version of it?
[3023.40 --> 3029.34]  And I'm still essentially, you know, get committing to my directory right here on my box.
[3029.40 --> 3031.74]  And it's not remote, even though it's Docker local.
[3032.10 --> 3034.42]  You consider remote based upon what you just said there, right?
[3034.44 --> 3040.42]  Like it's still anytime it's not your actual machine and it's in an image, you're saying remote.
[3041.06 --> 3041.62]  Yeah, right.
[3041.62 --> 3045.74]  And so, yeah, if you have, like you mentioned, if I'm making like commits or something like that,
[3045.82 --> 3050.38]  like they're not going to be like, oh, these are just special commits that then got discarded
[3050.38 --> 3052.34]  outside of my container or something like that.
[3052.40 --> 3056.66]  It's going to be like, no, you can commit back to your GitHub repo and your changes are still
[3056.66 --> 3057.34]  going to be there.
[3057.62 --> 3060.76]  And so that's kind of the cool thing about having a dev container in a GitHub repo, for
[3060.76 --> 3061.94]  instance, is cool.
[3062.02 --> 3062.16]  Yeah.
[3062.24 --> 3067.00]  Then if I open code spaces or open anywhere else that's supporting dev containers, like I
[3067.00 --> 3070.60]  can just work on my code directly there with also the tools that I need.
[3070.60 --> 3072.86]  How do the credentials work?
[3073.32 --> 3077.24]  So if I open up, I'm logged into github.com.
[3077.36 --> 3078.12]  I'm looking at a repo.
[3078.32 --> 3079.46]  I open it in the code space.
[3079.62 --> 3085.08]  Now I'm logged into Jared Santo fictional journey P775G6, et cetera.
[3085.28 --> 3085.90]  Is that the URL?
[3086.50 --> 3087.60]  Well, that's part of the URL.
[3087.76 --> 3088.70]  It's a fictional journey.
[3089.00 --> 3090.34]  It's my current code space.
[3090.34 --> 3095.62]  And let's say I'm just, I'm hacking along inside my code space and I say, all right,
[3095.68 --> 3097.24]  I'm going to commit this code.
[3097.32 --> 3100.40]  I'm going to push it back to my repo.
[3101.14 --> 3102.46]  How does it know it's me?
[3102.68 --> 3106.60]  How are my security credentials injected into the code space?
[3107.14 --> 3107.48]  Do you know?
[3107.48 --> 3107.92]  Yeah.
[3108.10 --> 3114.00]  So with code spaces, so you can use code spaces in the browser or you could use a code spaces
[3114.00 --> 3115.98]  extension in desktop via code.
[3116.20 --> 3119.02]  And either way, code spaces is going to handle your GitHub off.
[3119.22 --> 3124.82]  So it's up to the code spaces extension or service to securely let you log in and make
[3124.82 --> 3126.44]  sure that it's really you logged in.
[3126.62 --> 3130.94]  So when you're working on that code space in the browser, it's tied to your GitHub account.
[3131.18 --> 3135.66]  So you can't use a code space anonymously or like at this point, it's just going to be
[3135.66 --> 3136.40]  tied to you.
[3136.40 --> 3141.78]  So as long as like you authenticated into GitHub.com or you authenticated into the extension,
[3142.02 --> 3143.68]  then you're going to be authed and secure.
[3144.24 --> 3146.66]  Speaking of that, are you too afraid to GitHub, Jared?
[3146.92 --> 3148.88]  Do you feel like you're social engineering me right now?
[3148.98 --> 3152.38]  I mean, I want to know because I mean, at this point, you're outing yourself to be maybe
[3152.38 --> 3153.38]  insecure potentially.
[3153.52 --> 3155.40]  So get secure if you're not too afraid.
[3155.92 --> 3157.02]  I'm not going to answer that question.
[3157.30 --> 3157.58]  Okay.
[3158.30 --> 3164.72]  So if you are working locally in VS Code inside a dev container, the code is in the container,
[3164.72 --> 3165.06]  right?
[3165.06 --> 3167.20]  And you can you mount it locally somehow.
[3167.52 --> 3169.90]  VS Code handles whatever dance that is.
[3169.90 --> 3175.16]  And then you as long as it has local credentials for SSH or however you're authoring against
[3175.16 --> 3180.66]  your remote origin, whether it's GitHub or some other provider, as long as you have access
[3180.66 --> 3184.92]  to that in your local system, it's just going to pass that through or use that directly.
[3185.06 --> 3187.04]  It should be pretty straightforward.
[3187.04 --> 3187.44]  Yep.
[3187.44 --> 3187.96]  Yep.
[3188.18 --> 3194.62]  And you can use the same if you're using Git or GitHub commands via terminal or via extensions
[3194.62 --> 3198.78]  in VS Code, then you can install or use the same ones in your container and get that same
[3198.78 --> 3199.82]  access and authentication.
[3200.56 --> 3200.84]  Okay.
[3201.54 --> 3203.16]  It's almost too good to be true, Adam.
[3203.42 --> 3203.76]  Almost.
[3203.76 --> 3205.48]  Is it not true?
[3205.48 --> 3207.34]  Because usually when it's too good to be true?
[3207.80 --> 3208.72]  Not true.
[3209.10 --> 3211.22]  Going back to these templates.
[3211.56 --> 3215.74]  So I'm looking at the Go one now in the official dev containers templates repo.
[3215.94 --> 3217.40]  The Go template.
[3217.40 --> 3222.46]  And it's pointing that there is no Docker composed.
[3222.66 --> 3224.20]  There's no Docker even in the template.
[3224.50 --> 3228.74]  It's just like pointing at variants of an image.
[3229.00 --> 3231.78]  There's no image URL that I can even see.
[3232.10 --> 3235.56]  Documentation URL, license URL, image variant.
[3236.04 --> 3240.94]  Does this have built into it knowledge of this default repository of images perhaps?
[3240.94 --> 3248.02]  Because it looks like it's going to be pulling from a Microsoft hosted thing.
[3248.62 --> 3254.50]  Image, mcr.microsoft.com slash devcontainer slash go, according to this.
[3254.80 --> 3258.30]  So I guess Microsoft is hosting a bunch of these images for people.
[3258.42 --> 3264.76]  And if you don't specify anything like specific image URL or a Docker file that grabs an image
[3264.76 --> 3268.06]  itself, it's just all falling back to Microsoft hosted stuff.
[3268.16 --> 3269.48]  Is that, am I reading this right?
[3269.48 --> 3275.22]  Yeah, so the set of templates that we host as part of the spec are all going to reference
[3275.22 --> 3277.86]  images that we're also publishing as part of the spec.
[3278.04 --> 3283.30]  So if you go to github.com slash devcontainers, then slash templates or slash images,
[3283.30 --> 3286.66]  you'll be able to see the corresponding templates and images that we're publishing.
[3287.56 --> 3290.34]  And in the templates, so for instance, the Go one that you pulled up,
[3290.72 --> 3294.94]  that image property is pointing to the Microsoft Container Registry or MCR,
[3294.94 --> 3298.58]  which is where we're publishing our first party spec images.
[3298.58 --> 3304.54]  And we try to just make it simpler of, hey, our templates just need to reference that image.
[3304.64 --> 3308.34]  That way you don't have to worry about like, oh, I need to manage additional files or like know how
[3308.34 --> 3309.88]  to work with or add a Docker file.
[3310.06 --> 3314.06]  But if you want to use a Docker file or your project already has a Docker file, you can totally
[3314.06 --> 3314.78]  use that too.
[3314.90 --> 3320.10]  You would just move that image property over to your Docker file instead of in the devcontainer.json
[3320.10 --> 3322.98]  and then have your devcontainer.json point over to your Docker file.
[3323.62 --> 3323.74]  Right.
[3324.44 --> 3325.26]  No, I mean, I love that.
[3325.34 --> 3326.52]  It's sensible defaults.
[3326.52 --> 3328.10]  You're actually providing a service here, right?
[3328.14 --> 3333.76]  Like you're providing an image repository that people can download images from in the case that
[3333.76 --> 3338.20]  they don't have their own or pointing at Docker Hub, which is what many images currently
[3338.20 --> 3345.84]  hosted on Docker Hub or elsewhere, that it makes the getting started for the simplest case is
[3345.84 --> 3346.84]  pretty straightforward.
[3347.00 --> 3353.92]  Like if you're at, if your code is just using go 1.19 or 1.18, you can just take this template,
[3354.12 --> 3359.84]  drop it in your folder, devcontainer.json, maybe add a customization or two, maybe not.
[3360.14 --> 3363.66]  And you can have a devcontainer with go installed ready to run your code.
[3364.38 --> 3365.22]  Yep, exactly.
[3365.22 --> 3369.86]  I mean, who doesn't want to have a go machine one click away a cent?
[3369.94 --> 3371.08]  I mean, that's, that's how you get there.
[3371.12 --> 3374.20]  It's like, is this, it's like, we had said that conversation with Matt, basically.
[3374.62 --> 3375.68]  We were talking about that though.
[3375.72 --> 3379.80]  We were just like saying how allergic we are to just rando installs to different things.
[3379.80 --> 3380.92]  And like, right.
[3381.02 --> 3385.96]  If I'm not, if I'm go curious, which a lot of the go time audiences, there's a lot of people
[3385.96 --> 3389.66]  who are in the go world and they just don't even mind, you know, they drop things on their
[3389.66 --> 3391.44]  path that whatever, go binary or whatever.
[3391.56 --> 3392.54]  Yeah, it's already set up.
[3392.68 --> 3392.84]  Yeah.
[3392.84 --> 3395.06]  But if you're go curious, you're like, how does this work?
[3395.06 --> 3399.32]  You can just spin up a go container via dev containers, play around.
[3399.32 --> 3403.40]  And like your local machine is the same as it was, you know, when you close that machine
[3403.40 --> 3406.78]  down, when you close that container down, it's, it's right there, which I think is super
[3406.78 --> 3407.08]  cool.
[3407.22 --> 3412.68]  I mean, I just love, you know, the ephemeralness of it, but also the permanence in how the dev
[3412.68 --> 3417.56]  container spec lets you specify so much to use it within teams and different organizations.
[3417.56 --> 3423.60]  I guess the real interesting thing is how is it when it goes beyond like us nerds, right?
[3423.64 --> 3425.68]  Like we geek out on this stuff, right?
[3425.70 --> 3426.86]  This is great to us.
[3427.18 --> 3431.08]  But what about when my son who's seven is at school, right?
[3431.08 --> 3434.42]  And he wants to go into this class, which he's now in some GT classes and they're doing
[3434.42 --> 3435.22]  computer things.
[3435.22 --> 3439.62]  Well, you know, I don't know if it's that mature yet, but I would have got, I got to
[3439.62 --> 3444.20]  imagine that like the teacher isn't going to want to have to set up every single machine
[3444.20 --> 3448.12]  and do all these different things for six or seven different computer environments that
[3448.12 --> 3449.60]  are all the same Go environment.
[3449.60 --> 3452.52]  For example, let's say they're learning Go or they're learning Python as their first
[3452.52 --> 3456.98]  language, you know, like wouldn't dev containers be amazing in that scenario where it's just
[3456.98 --> 3462.28]  like, well, if you have Docker installed and you can, you know, borrow this template, which
[3462.28 --> 3463.00]  is pretty easy, right?
[3463.02 --> 3464.42]  Like you just copy it down.
[3464.78 --> 3465.14]  Wow.
[3465.20 --> 3469.98]  That teacher or whoever's leading that class has just got like a star next to their name
[3469.98 --> 3475.22]  because wow, they got six machines up running a Go space or a Python space that a kid can
[3475.22 --> 3479.30]  play with essentially pretty quickly rather than the whole song and dance.
[3479.58 --> 3480.02]  Yeah.
[3480.14 --> 3484.56]  I love that you brought that up too, because education is the space that we've really identified
[3484.56 --> 3489.98]  too, that these could be super helpful in, especially in some of the more cloud powered
[3489.98 --> 3494.56]  or automated tools like Codespaces or other ones of like, I don't even have to like install
[3494.56 --> 3495.28]  anything locally.
[3495.28 --> 3498.12]  I can just go to the cloud and have everything that I need there.
[3498.50 --> 3502.32]  But I think that's an awesome opportunity in education because we've gotten feedback from
[3502.32 --> 3507.82]  educators and students alike that, hey, at the beginning of a new semester, I have to spend
[3507.82 --> 3511.26]  first few days or weeks just getting everything I need for this class.
[3511.44 --> 3515.46]  And if I'm maybe studying computer science, I have a bunch of different dependencies that I
[3515.46 --> 3517.18]  need across a bunch of different classes.
[3517.18 --> 3522.52]  So like, what if either my professor added a dev container or us as a class, we had some
[3522.52 --> 3524.44]  dev container configuration that we could share.
[3524.86 --> 3528.72]  So it's like, oh, don't even worry about like, which version of Python do I need for this
[3528.72 --> 3529.70]  class or that class?
[3529.78 --> 3530.52]  Like, hey, no worries.
[3530.54 --> 3531.52]  It's just in the dev container.
[3531.64 --> 3532.24]  Go grab it.
[3533.42 --> 3533.82]  Yeah.
[3534.02 --> 3535.24]  That's music to my ears.
[3535.74 --> 3536.14]  For sure.
[3536.38 --> 3541.70]  It's also roots from the original GitHub inception, which was permission to mess up.
[3542.30 --> 3544.62]  Like this is the ultimate permission just to play, right?
[3544.62 --> 3552.78]  Like if, if I'm go curious and this go container is, you know, one dev container dot json away,
[3552.88 --> 3554.84]  Jared, as you said before, that's so cool.
[3555.20 --> 3558.28]  Like just one dev container dot json away.
[3559.14 --> 3560.06]  That's so cool.
[3560.66 --> 3561.52]  A semi tangent.
[3561.60 --> 3563.72]  I've kind of played with this in my, in a different world.
[3563.80 --> 3567.44]  I've been tinkering with prox mox and containers and stuff like that.
[3567.44 --> 3569.74]  And I'm doing a lot of like home labby stuff.
[3569.74 --> 3575.70]  And like, I've been playing with true NAS and other things more so because prox mox makes it so
[3575.70 --> 3579.28]  easy to spin up a brand new Ubuntu image or a Debian image or whatever I want to do.
[3579.70 --> 3582.90]  And there's just a cool world out there where it's like the same thing, but in the
[3582.90 --> 3584.92]  developer environment space.
[3585.24 --> 3590.92]  And, you know, that to me is just like so awesome because you don't have to figure out how do I
[3590.92 --> 3593.72]  create a Go environment or a Python environment?
[3594.34 --> 3598.70]  I mean, you can, if you're going out your own route in your own bespoke way, but like you had
[3598.70 --> 3601.98]  said, for the most part, you've got a lot of templates that get you started or at least spark
[3601.98 --> 3604.38]  your curiosity to understand how can this be leveraged?
[3604.72 --> 3606.26]  It's just that easy.
[3606.70 --> 3607.36]  Yeah, absolutely.
[3607.66 --> 3609.56]  That's what we're hoping for to make it just that easy.
[3610.78 --> 3611.80]  Jared's just over here laughing.
[3612.10 --> 3612.54]  Come on, Jared.
[3612.54 --> 3614.50]  Well, Bridget, you turned us into salespeople for you.
[3614.56 --> 3616.38]  He's like, it's just that easy.
[3616.96 --> 3617.94]  Yeah, I love it.
[3618.02 --> 3620.90]  Like within an hour, I'm like, oh, I don't even have to be saying it.
[3621.10 --> 3621.88]  What are the pros?
[3622.14 --> 3622.80]  We're converted.
[3623.06 --> 3623.64]  We're converts.
[3624.00 --> 3624.56]  Anything like that.
[3624.70 --> 3625.14]  Thank you.
[3625.24 --> 3627.64]  Bridget just sits back and lets us get excited about it.
[3627.66 --> 3628.96]  She's like, yes, we've got it.
[3629.38 --> 3631.14]  This is your adoption strategy, isn't it?
[3631.14 --> 3631.44]  It works.
[3632.24 --> 3633.16]  This is good.
[3633.96 --> 3634.24]  Yeah.
[3634.40 --> 3635.64]  You just got to find the right podcast.
[3636.18 --> 3636.28]  Right.
[3636.76 --> 3642.28]  Let's reel back and do our job of being, you know, good interviewers and say, what's the
[3642.28 --> 3643.54]  downside?
[3643.86 --> 3644.78]  What's the cons?
[3644.94 --> 3645.94]  Where does it struggle?
[3646.58 --> 3649.10]  Help us get some balance back into this.
[3649.10 --> 3652.22]  We've been, we've been effusive for the last 10 minutes and we need to balance it out.
[3652.34 --> 3656.24]  What's, what's maybe left undone or, or painful today?
[3656.38 --> 3657.16]  Bridget, help us out.
[3657.62 --> 3662.86]  I think that some of the next things we're really thinking about is we've made a lot of
[3662.86 --> 3667.54]  changes over the past year from open sourcing the spec in the CLI to now moving to these
[3667.54 --> 3672.66]  new contribution models for templates and features and having indices for them and all
[3672.66 --> 3673.50]  that kind of stuff.
[3673.86 --> 3678.28]  And with that, now that it's like, feels like we have the major building blocks in place
[3678.28 --> 3679.68]  with the spec in the CLI.
[3679.68 --> 3683.82]  But it's like really getting more user feedback of like, for instance, some of the questions
[3683.82 --> 3685.54]  you both have posed of, oh, okay.
[3685.64 --> 3688.54]  So it looks like the templates are just referencing an image.
[3688.68 --> 3690.22]  Like, is that clear to folks?
[3690.24 --> 3695.70]  Because we hosted a previous set of dev container templates or we previously called them definitions
[3695.70 --> 3697.68]  and those had Docker files in them.
[3697.74 --> 3701.58]  But we thought that as part of like the spec here with some simplification and with these
[3701.58 --> 3705.66]  new images that were post publishing more publicly in this images repo.
[3706.16 --> 3707.82]  Hey, like, let's just reference an image there.
[3707.82 --> 3711.84]  It feels like that might be more straightforward, but that may not be everyone's scenario or
[3711.84 --> 3715.92]  expectation going in, especially for people who are already using dev containers and more
[3715.92 --> 3718.00]  familiar with the old model or the old rebuild.
[3718.34 --> 3723.80]  So I think getting feedback on some of those like key choices that we're starting to make
[3723.80 --> 3728.54]  and it's, we're really open to that feedback of, hey, like if this isn't clear to users,
[3728.54 --> 3730.04]  we want to make it a good experience.
[3730.14 --> 3732.28]  So we don't want to say, hey, well, like too bad.
[3732.36 --> 3733.80]  We thought this was clearest and simplest.
[3733.98 --> 3735.04]  So you need to live with it.
[3735.10 --> 3736.86]  It's like, no, that's why we want to make it an open spec.
[3736.86 --> 3738.52]  Like, what does the community think there?
[3739.04 --> 3739.78]  Sync with that.
[3740.04 --> 3744.92]  And then, yeah, I think it's cool to like seeing the other kinds of like templates and
[3744.92 --> 3746.40]  features that folks contribute.
[3746.80 --> 3750.72]  But like, for instance, is the contribution process clear for how I would publish?
[3750.98 --> 3754.82]  And is it clear that, hey, like I could totally choose to publish this for the whole community
[3754.82 --> 3758.26]  or I could also leave this private just to me or just to my company.
[3758.80 --> 3763.38]  So then getting feedback on those kinds of flows and what we have built into the CLI or into
[3763.38 --> 3765.18]  some of our other things that we offer.
[3765.32 --> 3769.80]  Like we have GitHub Actions or Azure DevOps Task to kind of help with some of those processes.
[3770.16 --> 3773.94]  Like, are these things working well for users or are there still some points to optimize?
[3774.20 --> 3778.14]  Because we'll get feedback of like, hey, like this command in the CLI wasn't really documented
[3778.14 --> 3781.66]  and it's because, oh, if like we just added it, then we got to make sure our docs are keeping up.
[3781.66 --> 3785.58]  So I think also just keeping like our docs going and updating and all that since things
[3785.58 --> 3788.66]  are moving so fast, making sure that then it's clear to people as well.
[3788.66 --> 3790.42]  So something we're always keeping in mind.
[3791.22 --> 3795.34]  So this Go template we're looking at, that's been the example we've used here.
[3795.44 --> 3798.50]  So on line six, it references an image, which I mentioned before.
[3799.06 --> 3802.66]  It's an mcr.microsoft.com slash whatever URL.
[3802.78 --> 3803.42]  And it's an image.
[3803.54 --> 3810.24]  So are you saying that because one line above that says or use a Docker file or Docker compose file.
[3810.34 --> 3813.04]  So essentially you've removed the step, right?
[3813.66 --> 3814.42]  Is that what happened here?
[3814.48 --> 3816.50]  This newer version is the template.
[3816.50 --> 3821.12]  It uses an image you've already sort of pre-baked with what would normally be in a Docker file.
[3821.58 --> 3821.94]  Correct.
[3822.10 --> 3822.28]  Yeah.
[3822.38 --> 3827.82]  And then if you go actually to the github.com slash devcontainers slash images, then you
[3827.82 --> 3829.80]  can see what's contained in that Go image.
[3830.32 --> 3832.34]  And you'll see, okay, there's an actual Docker file.
[3832.50 --> 3837.64]  So like ultimately there is one we're just saying, hey, maybe it'll be clearer, less cluttery
[3837.64 --> 3838.70]  if we don't have it there.
[3838.88 --> 3843.08]  And we also added that comment that you saw there in line five for or use a Docker file or
[3843.08 --> 3847.80]  Docker compose after we'd gotten some feedback of, hey, like, how can I use a Docker file?
[3847.80 --> 3851.04]  Or, hey, I used to know there were Docker files in your templates, but I'm not seeing
[3851.04 --> 3851.66]  them anymore.
[3851.80 --> 3854.92]  So it's cool that you saw the comment there and we're hoping things like that can help
[3854.92 --> 3855.28]  users.
[3855.28 --> 3858.98]  But seeing how we want to move forward with certain things like that.
[3859.60 --> 3859.72]  Yeah.
[3860.44 --> 3865.50]  Magic is good once you've to graduate into, you know, like magic isn't it's good, I guess,
[3865.54 --> 3866.02]  out the gate.
[3866.02 --> 3870.16]  But like, for the most part, your kind of primary target audience, at least right now,
[3870.72 --> 3875.16]  wants to know all the lines, you know, let me compose that Docker file for myself.
[3875.44 --> 3880.66]  Or at least tell me maybe there's two variants of this, this .json file where you've got like
[3880.66 --> 3885.46]  the full feature one, which doesn't reference the image and the opposite one, which was before
[3885.46 --> 3886.76]  the image was created, essentially.
[3887.18 --> 3888.00]  Give me both versions.
[3888.12 --> 3892.42]  So that way, if I'm, especially as you're sort of training wheelsing people into this world,
[3892.42 --> 3896.84]  it's like, well, you can go this simple if you've already pre-baked your images or you
[3896.84 --> 3901.60]  can do the full thing, Docker file, Docker compose and all to get to the end result.
[3901.60 --> 3903.88]  If you're familiar with that, because I mean, I would imagine a lot of people are pretty
[3903.88 --> 3907.30]  familiar with Docker and Docker compose to get to that world.
[3907.72 --> 3912.14]  But like Jared, even with line six kind of stumbled, him was like, well, what's happening
[3912.14 --> 3912.36]  here?
[3912.42 --> 3914.08]  Is there an image of you're hosting somewhere?
[3914.30 --> 3917.14]  And as you'd mentioned, you know, why your reasons why it makes sense.
[3917.14 --> 3923.18]  But I think if these are templates and they're, they're meant to be initial, you know, I guess
[3923.18 --> 3926.94]  initial exposure to how this works, like I want to write this myself.
[3927.44 --> 3928.16]  Would it be this simple?
[3928.24 --> 3928.74]  Probably not.
[3928.84 --> 3933.62]  I would probably reference similar to the way I would make a Docker compose file now, which
[3933.62 --> 3937.76]  is an image somewhere else and do all the different steps, that kind of thing.
[3938.62 --> 3940.62]  Anything left unsaid, Bridget?
[3940.70 --> 3944.98]  Anything you've been waiting for us to ask you and we just haven't got around to it because
[3944.98 --> 3947.34]  we're adults or have we covered it all?
[3947.66 --> 3954.06]  I feel like we covered all the key parts from, yeah, talking about what dev containers are,
[3954.34 --> 3959.46]  the open spec, of you getting excited about it and becoming endorsers for us here.
[3959.70 --> 3961.72]  So we've really come full circle.
[3962.84 --> 3966.58]  And put these sound bites on the homepage and really get people using it.
[3966.94 --> 3967.48]  Yeah, for sure.
[3968.48 --> 3969.54]  What's a good first step?
[3969.62 --> 3974.18]  If we're given the audience that maybe they've started out like us, you know, apprehensive at
[3974.18 --> 3977.14]  first and curious and learning and asking questions.
[3977.24 --> 3981.38]  And now we're sales folks for the dev containers spec.
[3981.58 --> 3982.64]  Now that's Jared and I.
[3983.08 --> 3983.88]  What about our listeners?
[3984.02 --> 3986.72]  So if they're new to this, they're like, OK, what's a good first step?
[3986.78 --> 3987.76]  Where do you tell people to go?
[3988.24 --> 3990.16]  Obviously, devcontainers.dev.
[3990.24 --> 3991.90]  But what's a good first step for someone to do?
[3992.02 --> 3995.62]  Would you say a template or will be a first try for someone?
[3995.62 --> 4000.38]  Yeah, I would say in an editor environment of your choosing.
[4000.78 --> 4002.60]  Talked about VS Code and Codespaces a lot.
[4002.68 --> 4004.26]  So those are great ones to start out with.
[4004.68 --> 4010.50]  Just try out adding a dev container and building within it and seeing like, hey, OK, like what,
[4010.64 --> 4013.08]  how does my interface look compared to what I'm used to locally?
[4013.64 --> 4018.52]  So we have commands for you to add dev container configuration files that should walk you through
[4018.52 --> 4022.82]  like, hey, the necessary steps and having those files in there and then kind of getting used
[4022.82 --> 4025.02]  to, OK, yeah, then I'll just reopen in my container.
[4025.22 --> 4028.84]  And then if I make a change to the configuration, I'll just make sure that I remember to rebuild.
[4029.10 --> 4033.20]  And like once you get up and running with it, just a couple of steps or commands there,
[4033.80 --> 4035.34]  it should hopefully be pretty straightforward.
[4035.68 --> 4038.60]  And then just from there, you can become even more productive in them.
[4038.78 --> 4041.86]  So recommend checking out with containers.dev.
[4041.94 --> 4044.54]  You can kind of get an overview of the things that we talked about today.
[4044.66 --> 4048.62]  And then also in our supporting tools page on there, you can see, oh, cool.
[4048.74 --> 4051.88]  Like here's where I can learn more about using it in VS Code or Codespaces.
[4051.88 --> 4052.94]  Or here's how I could use it.
[4052.98 --> 4054.92]  Maybe some of these other tools that I'm already using.
[4055.34 --> 4055.96]  Yeah, I messed up there.
[4056.04 --> 4057.34]  I said dev containers.dev.
[4057.46 --> 4058.26]  Sorry about that.
[4058.84 --> 4062.10]  Containers.dev for posterity and clarification.
[4062.30 --> 4064.74]  Say containers.dev.
[4065.44 --> 4065.86]  Just kidding.
[4066.28 --> 4067.22]  I had to say it really loud.
[4068.44 --> 4070.04]  Say it five times real fast.
[4071.46 --> 4072.66]  Maintainer, maintainer, maintainer.
[4073.32 --> 4074.02]  Bridget, it's been awesome.
[4074.18 --> 4076.72]  Thank you so much for joining us and taking us into this new world.
[4076.80 --> 4080.96]  We're going to explore it a bit ourselves and encourage those who we see to do so as well.
[4080.96 --> 4082.70]  Thank you for coming on the show.
[4082.82 --> 4083.28]  Appreciate you.
[4083.50 --> 4084.20]  Yeah, totally.
[4084.52 --> 4085.34]  Sounds great.
[4085.62 --> 4086.36]  Thank you so much.
[4089.42 --> 4089.86]  Okay.
[4090.02 --> 4093.04]  Coming to a dev container near you, your code base.
[4093.20 --> 4094.24]  It's just too easy.
[4094.58 --> 4096.40]  You got to laugh at moments like that in shows.
[4096.62 --> 4098.06]  Thank you for laughing with me.
[4098.52 --> 4099.30]  It's just too easy.
[4099.86 --> 4100.34]  Hey, don't forget.
[4100.44 --> 4104.50]  There is a bonus on this show for a plus plus subscribers.
[4104.82 --> 4105.58]  We have a membership.
[4105.58 --> 4107.76]  It is called changelog plus plus.
[4107.92 --> 4109.14]  We drop the ads.
[4109.52 --> 4112.56]  We bring you a little closer to the metal and then we give you bonus content.
[4113.08 --> 4113.64]  Check it out.
[4113.76 --> 4116.86]  Learn more at changelog.com slash plus plus.
[4117.16 --> 4123.58]  Thank you once again to our friends and our partners at Fastly, Fly, and TypeSense.
[4124.12 --> 4127.06]  And to the Beats Master in residence, Brake Master Cylinder.
[4127.56 --> 4129.26]  Those beats, they're banging.
[4129.74 --> 4133.58]  And to you, our listener, thank you for listening to the show every single week.
[4133.58 --> 4135.20]  Tell a friend if you love this show.
[4135.58 --> 4139.48]  Word of mouth is definitely by far the best way to help us.
[4139.68 --> 4142.66]  Tell a friend if you love this show and we appreciate you.
[4143.08 --> 4143.52]  That's it.
[4143.56 --> 4144.20]  This show's done.
[4144.36 --> 4146.04]  We will see you on Monday.
[4163.58 --> 4193.56]  We will see you on Monday.
[4193.58 --> 4223.56]  We will see you on Monday.
