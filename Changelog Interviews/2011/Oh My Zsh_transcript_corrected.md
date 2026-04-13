[0.00 → 18.26] Welcome to the Changelog episode 0.6.1.
[18.60 → 19.62] I'm Adam Stachowiak.
[19.92 → 20.78] And I'm Wynne Netherlands.
[20.98 → 21.98] This is the Changelog.
[22.02 → 23.60] We cover what's fresh and new in open source.
[24.04 → 26.96] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.06 → 28.08] We're also up on GitHub.
[28.08 → 29.98] Head to GitHub.com slash explore.
[30.06 → 34.50] You'll find some trending repos, some feature repos from the blog, as well as our audio podcasts.
[34.74 → 37.94] And if you're on Twitter, follow Changelog Show and me, Adam Stack.
[38.34 → 40.70] And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.20 → 43.10] This episode is sponsored by GitHub Jobs.
[43.54 → 46.10] A pair of jobs in the Seattle area from Uber Mind.
[46.54 → 51.12] They're an agency that builds mobile applications, both on Android and iOS.
[51.28 → 55.92] And they're looking for folks that can help make great mobile applications.
[55.92 → 59.64] So on the Android side, you need to know Java, of course.
[60.26 → 63.78] At least three years' experience with Java is a big plus.
[64.28 → 70.14] On the iOS side, you need to know Xcode, Objective-C, MVC, of course.
[71.10 → 74.08] Competitive salary and signing bonus with both of these jobs.
[74.66 → 79.58] If you're interested, short codes LG.Gd slash a and AZ.
[79.58 → 86.72] The other end of the continent, I Street Solutions in Leesburg, Virginia, outside the D.C. area.
[87.24 → 88.92] I was looking for a full-time software engineer.
[89.98 → 91.94] And I like their criteria here.
[92.68 → 98.74] So starting with the soft skills first, collaborates well with others, solves problems logically and efficiently,
[99.54 → 102.02] thrives in a self-managed agile environment.
[102.02 → 103.80] Start and the skills.
[104.06 → 115.66] You need to demonstrate skill and wisdom with Rails, iOS, OS X, Android, HTML5, CSS, AJAX, Flash, XML, AWS, Postgres, SQL, TDD, and Git.
[116.38 → 119.72] So looking for a full-stack developer on this one if you're interested.
[120.24 → 122.08] LG.Gd slash ad.
[122.08 → 124.22] And this week we had a fun episode.
[124.38 → 125.38] We talked to Robbie Russell.
[126.06 → 130.28] He's one of the partners and chief evangelist over at Planet Argon.
[130.40 → 136.20] But he's also pretty well known for Oh My ZSH, as Kenneth says it, or also Oh My ZOHO.
[137.30 → 138.50] Oh My ZOHO.
[138.74 → 139.62] So you're a convert.
[140.40 → 141.28] I'm a convert, yeah.
[141.28 → 147.76] I got, I wouldn't say bashed, but I got asked enough by you guys what I use, and I didn't have any good answers.
[148.64 → 150.48] You got bashed for not using ZOHO?
[150.60 → 151.18] There you go.
[152.08 → 153.30] But I like it.
[153.44 → 155.54] I think it was a fun conversation.
[155.66 → 160.38] I got to ask him a bunch about just in general open source, some of his Ruby history.
[162.08 → 166.60] He's got a long list of pull requests that he tries to maintain under about 100.
[166.60 → 172.02] So he's got his hands quite full of this community-driven framework that he started up.
[172.58 → 173.12] I'm a convert.
[173.60 → 177.68] Kenneth took me over to ZOHO a few months ago, and I haven't looked back.
[177.68 → 183.88] I really like the right-side prompt and some of the niceties of the Oh My ZOHO plug-in system.
[183.98 → 189.68] I can just go in, and every time there's a new plug-in, edit one file, and I get all that goodness right there in my terminal.
[189.68 → 194.36] We also got to give a nice little plug to our friend Matt Dieters and his new project.
[194.86 → 195.74] What's it called again?
[195.98 → 196.50] The Coder Wall?
[196.74 → 197.58] Coder Wall, yeah.
[197.66 → 201.74] And we just got this email from him with the change-logged badge.
[201.82 → 202.40] Did you see that?
[202.80 → 203.70] I have not seen this yet.
[203.76 → 206.24] So we got our own little badge on the Coder Wall.
[206.24 → 207.20] It's awesome.
[207.40 → 215.98] And we were touting the fact that Robbie's got about 11 achievements, one of which is having a project with over 1,000 watchers.
[216.12 → 217.14] That's pretty amazing.
[217.46 → 217.82] Indeed.
[218.42 → 221.94] Can't wait to see this monkey on the log on the Coder Wall.
[222.06 → 228.78] So if you haven't checked out your Coder Wall profile, be sure and do that at coderwall.com slash your username.
[229.10 → 229.64] There you go.
[229.64 → 236.24] And coming soon you'll see the fact that if you've been change-logged, you'll get your own change-log badge.
[236.90 → 237.66] Fun episode this week.
[237.70 → 238.22] Should we get to it?
[238.62 → 239.20] Let's do it.
[248.04 → 253.76] We're joined today by Robbie Russell, chief evangelist and partner at Planet Argonne.
[253.78 → 254.36] How are you doing, Robbie?
[254.96 → 255.74] I'm doing great.
[255.82 → 256.52] Thanks for having me on.
[256.86 → 259.00] I hear that you're an American in Paris.
[259.64 → 260.50] I am.
[260.58 → 261.90] I've been here for a few months now.
[262.24 → 272.02] I decided to venture this way for a few months for the spring just to see what spring in Paris would be like and try to manage the company remotely for a bit.
[272.30 → 273.76] So I head back next month.
[274.10 → 274.28] Next month.
[274.44 → 278.10] So what's it like being, I guess, a key person in the company and being remote like that?
[278.10 → 281.42] Well, I can only speak for myself.
[281.54 → 283.60] I can't speak on behalf of the rest of my team.
[283.60 → 297.74] But from my perspective, it's been interesting as I've been able to kind of take a step back and kind of get a bigger view of the company again since not being in the office day to day and kind of getting pulled into the little discussions that happen within the office.
[297.74 → 305.36] So I can start thinking about, you know, bigger picture type things and kind of relay those back to my partners and stuff and kind of see what happens next there.
[305.52 → 322.34] And I've also been able to work with clients that are located in Europe on their time zone, which has been quite helpful for them and me to kind of get a better feel for kind of what they're experiencing when we're sleeping usually on the Pacific side of the coast.
[322.34 → 327.22] Yeah, it's like 10 o'clock your time, almost 1030, and it's 3.30 p.m. my time.
[328.50 → 328.72] Yeah.
[330.06 → 332.02] So I usually work later in the day now.
[332.12 → 335.42] I usually start my day around noon and try to finish around 8 or so.
[335.52 → 337.94] So that way I have some overlap with my team.
[338.04 → 341.18] But then I also have several hours of overlap with my European clients.
[341.88 → 347.98] So you're the chief evangelist at Planet Argonne, and you've been in and around this space for quite a while.
[347.98 → 356.18] Well, before I kind of give your intro for you, can you tell the listeners, if they don't know who you are, kind of what you've been about for the past few years, and kind of give yourself a brief intro?
[357.20 → 357.44] Sure.
[357.90 → 360.40] Well, I am a co-founder of Planet Argonne.
[360.50 → 362.32] We are a web design and development agency.
[362.82 → 365.38] We've been around since, I guess, 2002.
[366.04 → 371.12] And around 2004 is when we – this actually became more of a full-time project for me.
[371.12 → 377.08] And one of my co-founders, Allison, we started doing design and development back then with PHP.
[377.96 → 382.06] And kind of about a year later, I ended up finding our way into Ruby on Rails as well.
[382.58 → 385.60] And then we started offering web hosting for the Ruby on Rails community.
[385.82 → 392.80] And then the kind of company kind of took off a little bit at that point because we were one of the first few companies to do that at the time.
[392.80 → 397.60] And then we started focusing more of our attention on the development side of web applications.
[397.92 → 413.82] And then through that, we've kind of built-up a small collection of clients that we've been working with for a number of years and kind of been very, very closely partnered with them and kind of continue to kind of work with them on web development and stuff.
[413.88 → 416.08] And also working with startups from time to time as well.
[416.08 → 427.10] So I guess in my capacity, I kind of focus a lot more on kind of being a technical lead on our projects while my business partner, Allison, she has more of a design perspective.
[427.32 → 436.50] And so together, we're kind of able to provide our clients with kind of more of a holistic view of solving problems rather than just being too development-focused or too design-focused.
[436.50 → 439.78] So we have a design and a development team on our staff.
[440.40 → 444.96] And like the Planet Oregon site, I actually was checking out your About page for yourself.
[444.96 → 448.98] And I see that you're sporting an Instagram-like photo of yourself.
[450.78 → 451.22] Yes.
[451.50 → 460.52] I think we kind of decided to make the process of getting new photos up on our website to be a little bit quicker as we're hiring new people this year.
[460.86 → 462.38] So we decided we would come up with a theme.
[462.50 → 464.16] And I think the last one we had was hats.
[464.16 → 469.80] So people bring in their favourite hat, and we take an Instagram photo and pop up on the website.
[469.80 → 476.36] It's a little bit quicker than someone bringing in their SLR one day and trying to get everybody coordinated for that.
[476.62 → 476.70] Right.
[476.92 → 477.14] Yeah.
[477.28 → 478.74] It tends to be a pain in the butt.
[478.78 → 481.00] I totally know what you're saying there on that part.
[481.48 → 486.66] And I like actually this quote about yourself in your About section where it says,
[486.66 → 490.66] your motivation is not about the technology itself.
[490.76 → 499.74] It's more about taking ideas and executing them online because you've done a lot of fun stuff and less about using programming as this very fun thing,
[499.80 → 502.22] but more of a tool and not just for its own sake.
[502.30 → 503.78] Can you kind of extrapolate on that a little bit?
[504.54 → 504.76] Sure.
[504.76 → 513.12] I think that over the years I've realized that I am not like a lot of other programmers that I've worked with in the sense that a lot of people are very passionate about programming.
[513.92 → 520.66] I'm more passionate about kind of getting things done in it necessarily.
[520.90 → 524.18] So I'm a little bit more of a hack when it comes to programming.
[524.68 → 528.26] I think that's quite often why I don't allow myself to do a lot of development.
[528.54 → 530.94] And that's why I have better programmers than me on my staff.
[530.94 → 536.50] But I'm kind of more of a focus on I have an idea and I can execute that.
[536.72 → 538.54] And programming is a way to help facilitate that.
[538.66 → 546.58] All my initial – the reason I got into programming in the first place is because I had other little web ventures or business ideas that I wanted to get posted.
[546.86 → 549.38] I wanted to do it on the Internet, so I learned how to make web pages.
[549.50 → 550.80] I learned how to make web pages dynamic.
[551.30 → 553.76] It was always to try to get something else done.
[553.84 → 558.00] It was never about I want to learn how to make websites, or I want to learn how to make web applications.
[558.00 → 564.68] So that was – that's all kind of came out of me having some other goal in mind like getting a product on the Internet.
[565.24 → 577.68] So – and I think that's why – to some extent that's why our company is kind of positioned the way we are now is that I can be more focused on helping our clients get their ideas and their products on the Internet.
[578.30 → 582.24] And the technical details of how we program that, that's an important part of it.
[582.26 → 585.96] But that's not what motivates me in the same way.
[585.96 → 596.30] I guess in about 2004, like most people, they started hearing about this cool thing called Ruby on Rails and you got excited about it, and you started a blog called Ruby – not Ruby, Robbie on Rails.
[596.98 → 599.92] I'm sure you probably maybe stumbled over that a couple of times yourself.
[600.06 → 601.50] But that's pretty wild.
[601.66 → 608.24] So how did this blog come about, and what was your excitement level with Ruby and Ruby on Rails as it relates to what you just said?
[609.00 → 609.36] Sure.
[609.54 → 613.68] I actually was introduced to Ruby on Rails from Derek Servers from CD Baby.
[613.68 → 615.20] I'm not sure if you know who that is.
[615.20 → 616.24] I do, yeah.
[616.34 → 616.74] I know, Derek.
[616.92 → 624.22] So he actually offered me a position in 2003 to be their lead PHP programmer.
[624.76 → 629.86] And then he went away on Christmas break and just came back and decided that he was actually going to use Ruby.
[630.16 → 633.94] And so he asked me to give him a call in a few months if I had picked it up by then.
[634.18 → 639.02] So he ended up hiring another Ruby developer instead of going with PHP 5.
[639.02 → 642.50] And then so I decided I was going to learn Ruby on Rails at that point.
[643.08 → 649.58] So he kind of provided me with a little bit of motivation because I was kind of doing freelance stuff and deciding if I wanted to do Planet Argonne more full-time or not.
[649.58 → 655.02] So at that point when I started getting Ruby on Rails, I did start blogging.
[655.02 → 659.28] And I actually had a – I think I had another name, domain name for about a week.
[659.90 → 665.36] And then I changed it to Robbie on Rails because I think one morning I had this idea like, oh, it rhymes with Ruby.
[665.50 → 668.74] So I'll just make that – just kind of play on the name a little bit.
[668.92 → 669.02] Yeah.
[669.02 → 669.68] So it kind of stuck.
[669.68 → 679.84] So – and then a few months later when I started talking to Derek from CD Baby, I was getting too much client work for me to really think about going to work for him.
[679.92 → 685.58] So I just ended up continuing on with Planet Argonne and then the company kind of took off from there.
[686.58 → 690.68] Which brings us actually to one of the bigger pieces of this conversation we want to talk about.
[690.70 → 691.74] We want to talk about Z-Shell.
[691.74 → 697.60] And one of the few last posts you've had on that blog is joined the Z-Shell revolution.
[697.60 → 703.98] And before we dive deep into that conversation, we're going to pull in Kenneth Ritz who's waiting patiently in the wings.
[704.24 → 707.38] He's just got back from a quick little trip, but he's going to join us on this call.
[707.56 → 709.14] So give me a moment.
[709.18 → 709.84] I'm going to pull him in.
[710.20 → 710.32] Great.
[710.86 → 712.60] So we actually have Kenneth on the call now.
[712.66 → 720.60] So we're going to dig into the conversation on Robbie and to his open source adventures and Oh My Z-Shell and a bunch of other fun stuff.
[720.72 → 722.96] So let's kick that off.
[723.04 → 725.80] So, Robbie, I guess you've been in this space for quite a while.
[725.80 → 726.68] It's 2010.
[727.38 → 730.04] What was your motivation to get into open source?
[730.16 → 731.68] What was some of the first projects you worked on?
[732.40 → 736.86] I think my first open source projects were actually back in maybe 2000, 2001.
[737.16 → 742.24] I was doing some PHP development back then, and I had a couple of projects back then up on SourceForge.
[743.10 → 747.22] Most of those have hopefully been deleted from there, so there's no evidence.
[747.22 → 750.86] But I have been working with open source and Linux for a number of years.
[751.04 → 758.16] And I think about 2004, 2005, whenever I caught the Rails bug, I ended up buying a MacBook and kind of forgot how to use a Linux machine.
[758.16 → 760.52] But, yeah.
[761.20 → 777.88] I think since then, though, I think I've been, you know, still been doing a lot of open source stuff, you know, working with Ruby on Rails, contributing there when I can, releasing plugins and helping out with Ruby Gems as well to help our team, you know, develop our projects and to see where anywhere else I can help within the community.
[777.88 → 781.40] So what spawned off OhMyZShell?
[781.50 → 782.66] It's a community-driven framework.
[782.80 → 785.76] But what exactly is this project, and what got you started on it?
[786.32 → 791.22] Well, I've been using Shell for about, I want to say, maybe four or five years.
[791.72 → 795.56] And I had a rather long Shell configuration.
[795.86 → 804.34] It was basically just one file with a bunch of stuff that I had taken from other people's Shell example files, either on blogs or people that I knew on IRC.
[804.34 → 808.14] And to make it do some of the stuff that I wanted it to do.
[808.52 → 811.04] And I found that I wanted to share it with some of my coworkers.
[811.86 → 816.76] And in order for me to do that, basically, I would just kind of copy the file over to them, and they would use it.
[817.06 → 829.70] But then I noticed that one of my employees, Carlos, he wanted to understand what it did, all the configuration changes, because he's more of a programmer and actually wants to understand how things work, where I just want to kind of get things done.
[829.70 → 834.66] And so he started trying to dissect things and sort of wanting documentation or explanation.
[834.92 → 838.08] So I decided that I would clean it up a bit for him.
[838.08 → 852.54] And one morning I ended up spending time and kind of reorganizing all the taking the file apart and breaking it up into multiple files that are a little bit more descriptive of what the different pieces were.
[852.80 → 857.72] And kind of put that up on a GitHub repository so that he could download that and then set it up himself.
[858.44 → 861.04] And then one of our other guys wanted to use it as well.
[861.04 → 864.64] And so within a few days, they started asking for more customization.
[865.24 → 869.14] They wanted to have the terminal prompt look a little bit different.
[869.38 → 873.12] So I started adding more and more functionality and it kind of spawned from there.
[874.32 → 887.68] It's pretty wild with Show, actually, because I think, Kenneth, you can probably back me up on this, but there's been a number of times on this podcast where Kenneth or Wynn or some other blend of people that's been on the call has been like, you know, Adam, what do you use?
[887.68 → 897.38] And I'm like, I have no idea because I'm just more or less a front end guy, someone who dabbles in HTML, CSS, JavaScript, you know, design front end stuff.
[897.50 → 900.96] And I've been on the command line for a while, but it's like I have no idea.
[900.96 → 904.78] So there's this big, I guess, debate between Bash versus Shell.
[905.02 → 908.62] And you said you started with Shell about four years ago.
[908.76 → 912.68] What was it that kind of made you want to go that direction, and why is this war going on?
[913.48 → 913.68] Sure.
[914.12 → 917.46] Well, I'm not sure that I would say that it was a war necessarily that prompted me.
[917.46 → 920.38] It was more, I mean, I guess there's some debate there.
[920.58 → 927.02] But for me, I saw someone, we used to do a lot of web hosting, I think, as I mentioned earlier.
[927.52 → 929.14] And I used to have to connect to a lot of servers.
[929.30 → 940.32] And one thing that a little piece of code that someone gave me for Shell allowed me to basically autocomplete server names and IP addresses based on servers that I had already connected to.
[940.32 → 950.78] And so that little piece of code that allowed me to basically start typing SSH, you know, my username, and then start typing an IP address and hit tab.
[950.88 → 958.58] And then it showed all the different servers or different host names and basically used my key cursor to select one and press enter and actually connect to it.
[958.58 → 961.90] And I was going to be, I was really impressed by that.
[962.04 → 967.44] And that was, so that was enough for me to start going, oh, this autocompletion stuff in Shell is quite interesting.
[967.86 → 970.42] And I hadn't seen anything like that in Bash.
[970.42 → 972.92] So for me, it was just about saving time.
[973.12 → 975.78] And it seemed a little bit more useful and interactive.
[975.78 → 976.56] And I like that.
[976.72 → 980.32] So from there, I just found more and more features that I liked over time.
[980.92 → 983.86] So what is the feature set when we look down on Oh My Shell now?
[983.94 → 986.94] What are some of the core features that people really cling to with this project?
[988.00 → 990.76] Well, the first major feature that I included was themes.
[990.76 → 1004.86] And it was more along the lines of allowing people to kind of show off how they would like their, you know, their prompt to look like, whether that be colours, show information like their Git prompt, or everybody has their own unique personal preferences.
[1005.40 → 1012.42] And so, I mean, just in the three people at the time in my team, we all had a different, you know, opinion of what it should look like.
[1012.48 → 1014.82] So we had our own little themes, and that's how it kind of started.
[1014.82 → 1027.04] And I was kind of using themes as kind of way to kind of jokingly promote the project when I blogged about it, because I was kind of being sarcastic about, oh, yeah, we've got like over 18 themes now.
[1027.62 → 1033.64] And I remember thinking that was like really impressive at the time, but like why anyone would want to sift through that many themes?
[1034.16 → 1039.66] But now, a couple of years later, we have like 80 themes, and that's kind of a chaos to go through.
[1039.66 → 1046.18] But we have a huge gallery of themes that people can look through, and people still send in their own version.
[1046.40 → 1062.56] So apparently having very customized and specific themes focus on kind of your preferences is kind of a very – I guess it's one thing that's – when it comes to terminal prompts, people are very opinionated about having their own little preferences and style there.
[1062.56 → 1072.44] So I think when you can look through all the people's stuff, you can kind of see what people are doing, kind of pick and choose things to kind of create your own and personalize your terminal experience.
[1072.98 → 1079.10] Yeah, speaking of themes in the Oh My Z Shell here in my root, I actually see one named Kenneth Ritz.
[1079.42 → 1080.54] Kenneth, you care to tell us about that?
[1081.18 → 1082.08] Yeah, it's pretty awesome.
[1082.08 → 1085.94] Well, I'm a big fan of Z Shell in general.
[1086.08 → 1096.68] I've been using – I had a lot of the features that Z Shell offered a couple of years ago with Bash, and I decided to move over to Z Shell when I had all the cool completion features and stuff like that.
[1097.02 → 1103.34] And I had my own that I maintained for a long time, and it was just the ugliest configuration file you've ever seen.
[1103.90 → 1104.66] There were like four of them.
[1104.68 → 1105.78] I didn't even know what half of it did.
[1106.56 → 1111.32] So funny, you know, Oh My ZSH was really extremely helpful for that.
[1111.32 → 1113.00] So the first thing I did was make a theme.
[1113.70 → 1121.08] And I think that's one of the worst things that happens when you have people who are using Bash a lot is you have people who do that double line prompt.
[1121.16 → 1121.74] Have you seen that?
[1122.46 → 1122.66] Yeah.
[1122.92 → 1128.40] And it was one of the beauty – you know, the beautiful features of Z Shell is having the right prompt.
[1128.54 → 1131.04] So I kind of tricked it out there.
[1131.26 → 1133.02] But it's a great tool.
[1133.22 → 1133.58] I love it.
[1134.08 → 1140.42] I was going to say pre me coming to Z Shell with my Bash, my Bash had some sort of weird if-then statement
[1140.42 → 1142.98] that I copied from somebody's blog like years ago.
[1142.98 → 1151.70] And because I'm not much of a geek in that sense to like to hack my Bash and stuff like that, I was like – I had no idea what it is.
[1151.74 → 1154.80] But it was doing some weird funky stuff with my prompt too.
[1154.90 → 1157.26] So I was really encouraged to check out Z Shell.
[1158.10 → 1161.24] And then Oh My Z Shell made it super easy to just jump into too.
[1161.76 → 1164.32] Yeah, and there's some really cool plugins that people are developing.
[1164.46 → 1165.66] Do you want to talk about some of those?
[1165.66 → 1166.66] Sure.
[1167.66 → 1173.10] Well, the funny thing is I only use about – I think I'm loading about four or five plugins myself.
[1173.24 → 1176.34] And I think there's approximately almost 40 plugins now.
[1176.94 → 1179.04] So a lot of those are things that people have contributed.
[1179.20 → 1182.52] They need it for their own, or they want to share it with their friends and such.
[1182.78 → 1187.18] So like I'm using – like one of the ones I think is the most useful is the Git one.
[1187.18 → 1194.14] I also use another one for Rails and one for RVM for stuff that's kind of focused on my Rails and Ruby development.
[1195.26 → 1197.28] I'm not even sure what else is being loaded in there right now.
[1197.34 → 1198.54] I have to go look at my configure.
[1199.36 → 1207.34] But yeah, I mean people keep – there's still like several plugins that are pending my approval to be pulled in.
[1207.40 → 1212.86] A lot of them I'm just kind of relying on other people to do testing and stuff for those because they're not things that I would use.
[1212.86 → 1217.00] And so I'm kind of doing my best to try to manage that.
[1217.14 → 1221.10] But I still kind of see it as a little bit of a more of a community free-for-all in some sense.
[1221.32 → 1224.12] I'm very open to people contributing things.
[1224.12 → 1231.90] And as long as it doesn't break my prompt, usually that I'm okay with trying it out for a bit and waiting for someone else to say, hey, that broke my thing.
[1232.06 → 1237.42] And then usually those people figure it out and fix it and come to a better solution, which I think is one of the beauties of open source.
[1237.42 → 1243.00] So I'm not trying to be a dictator on how things get approved and submitted.
[1243.28 → 1245.48] So I just don't have enough time to keep up with it all.
[1246.02 → 1251.20] But so yeah, I think the plugins is another nice thing.
[1251.48 → 1254.74] And we tried to – we actually used to load them all by default.
[1254.82 → 1262.80] But now we have a little thing where you can specify which ones you want to explicitly load, which helps speed up the prompt and such.
[1262.80 → 1266.54] But I do think things like the Git prompted one is one of the most useful ones.
[1266.60 → 1278.34] And a lot of themes have that enabled so that when you're looking – when you're working in your terminal, and you have changes in your Git repository that haven't been committed yet, it will actually indicate that, which is quite helpful.
[1278.74 → 1286.84] And a lot of people have different ideas and little creative little colour symbols or little characters that show up to kind of show that.
[1286.84 → 1302.60] So I think whatever helps people kind of makes people feel like they're – I think it all comes down to – I see Oh My Z Show as a tool that allows people to feel a little bit more at home when they're working in their terminal all day.
[1302.78 → 1308.12] And I think that's to make – if they have a little bit of personalization there, then I think they enjoy themselves a little bit more.
[1308.12 → 1314.96] One thing I did recently because I wanted to kind of see what people have been doing with themes is I added a feature for randomizing the theme.
[1315.78 → 1323.42] So if you just set your theme to random and just the word random instead of a specific name, every time you open up a new terminal, it will be a different theme.
[1323.92 → 1326.18] So that way you can kind of just explore and see what people are doing.
[1326.18 → 1341.78] So I'll have – I'm using – iTerm2 now is the terminal that I use on my Mac because you can have windows within windows like horizontal and vertical windows within one terminal, and I think that's quite helpful.
[1342.14 → 1346.64] But every single one of those looks different now because I have random themes on, which is a little chaotic at times.
[1346.64 → 1358.60] But it actually – I kind of like it to some extent as well because it just – I feel like it's the community has helped decide what my prompt is going to be like.
[1360.18 → 1364.32] And I kind of don't know if I actually like mine that much anymore because I've seen some other cool ones.
[1364.96 → 1367.80] Yeah, I just actually – I just edited mine to go to random.
[1368.00 → 1370.08] I just opened a bunch of tabs, and it's pretty wild.
[1370.60 → 1371.34] That's what I was using.
[1371.36 → 1372.02] I was using yours.
[1372.84 → 1373.18] Okay.
[1373.60 → 1375.40] So, yeah, there's some other really neat ones in there.
[1375.40 → 1378.76] And I think if you look at the – there's a themes page on the wiki up on GitHub.
[1379.50 → 1382.94] And I think – I try to get everybody to put a screenshot of theirs.
[1383.14 → 1387.48] I know that it doesn't have all of them there, but there are tons of screenshots there.
[1388.16 → 1394.20] So – and we're – there are some plans to hopefully build a kind of like gallery that's a little bit more interactive.
[1394.32 → 1402.28] You can kind of, you know, paginate through them all those images and stuff and hopefully find something and just tell you how to convert to that or something.
[1402.28 → 1406.12] Maybe like a little command you can copy and paste into your terminal.
[1406.12 → 1419.92] I think what I like most about this framework you've done for Shell is that it kind of levels the playing field for – just to use an extreme example like this where I'm a lot less geeky than maybe Kenneth is.
[1419.98 → 1420.62] He's a Pythons.
[1420.62 → 1422.48] He's, you know, done a lot of back-end stuff.
[1422.56 → 1427.30] He's really smart in those areas where I'm more of a front-end guy, but we kind of play in the same tools.
[1427.96 → 1439.88] And it was hard for me to relate to some of the things he and Won and others have done in regard to their terminal and, you know, command lines and aliasing and automating and different stuff like that.
[1439.88 → 1449.10] So I was like, this is really wild, so I can actually jump in here and just do some basic config or specify a new – like a new plug-in to pull into mine.
[1449.26 → 1458.18] Like some of the ones that I'm using are like Brew, Bundler, Git, the OSX one, Rails 3 because I do some Rails 3 projects and the Ruby one and TextMate.
[1458.18 → 1466.88] And I even really got excited about adding the alias of Hub, of actually doing Brew install Hub.
[1467.10 → 1467.78] So that was pretty cool.
[1468.08 → 1470.02] So that was a fun thing.
[1470.10 → 1470.34] I don't know.
[1470.38 → 1479.56] Is that directly involved with Shell or OhMyZShell or is that just something that's a byproduct of being able to simply add an alias and teach Git about GitHub?
[1481.52 → 1483.14] I'm trying to remember the Hub one.
[1483.24 → 1484.66] I don't recall that one.
[1484.70 → 1487.36] That's a wrapper function around Git.
[1487.36 → 1499.50] So really what that is, I think having something like, you know, Shell and OhMyZShell in particular really fosters – you know, it's a simple framework for the configuration for Shell, which before was all over the place.
[1499.60 → 1507.56] I think it really allows people to be able to create little things like that to, you know, just send a pull request to add it.
[1507.64 → 1512.60] And it really, you know, makes things a lot more collaborative, which is what you're talking about, Adam.
[1512.78 → 1516.34] Yeah, that's a product from the funk, Chris from GitHub.
[1516.34 → 1523.30] It's a command line utility which adds GitHub knowledge to Git, which is what the project says at least.
[1523.38 → 1525.58] And it's pretty easy to install if you're using Homebrew.
[1526.04 → 1528.52] Then it's just brewed install hub, I believe.
[1528.52 → 1535.08] And the next thing you know, as soon as you type Git, you can actually do, like, Git clone and specify username slash and repo.
[1535.56 → 1542.04] And you can actually pull down that person's repo without actually having to know the full string and stuff like that.
[1542.06 → 1543.42] So there's some other fun stuff you could do with it.
[1543.46 → 1548.22] But that's just pretty wild how you can start to, like, inject this stuff into your bash.
[1548.22 → 1551.10] So, Kenneth, you're a Vim user, though.
[1551.18 → 1556.32] So how does all of this stuff we're talking about relate to using Vim with Shell?
[1557.18 → 1557.88] Not at all.
[1558.10 → 1558.64] Not at all?
[1559.16 → 1561.80] Well, the Vim community has the same thing going on.
[1561.82 → 1562.70] It's kind of what Janus is.
[1562.78 → 1564.62] I don't really use Vim that much now.
[1564.84 → 1566.70] But it's the same type of thing.
[1566.70 → 1573.80] You know, the OMI ZSH is a fantastic community-driven standard configuration set.
[1574.40 → 1575.62] And that's like what Janus is.
[1575.70 → 1580.64] And it allows it to be really easy to configure and share little pieces of your configuration.
[1581.26 → 1588.08] Because before, you know, at the same way, my Vim file is, you know, a thousand lines long, and I don't even know half of it does.
[1588.50 → 1592.60] So I think, you know, frameworks like this are excellent.
[1592.72 → 1595.44] I think there should be many more of them for many other projects.
[1595.44 → 1597.80] So I have a question for you, Robbie.
[1598.22 → 1598.66] Sure.
[1600.38 → 1611.12] I'm not sure the statistics of this, but my impression is that OMI ZSH is one of the most contributed to projects on GitHub, probably, because of all the small contributions.
[1611.96 → 1613.66] Is that correct?
[1614.38 → 1615.50] I don't know.
[1615.62 → 1617.96] I don't know how we compare to a lot of other projects.
[1618.46 → 1619.96] I mean, I do have some stats.
[1619.96 → 1625.22] For example, you know, we have over 750 forks of the project.
[1625.64 → 1631.62] And I think that ranks us at about, it's definitely in the top 10 most forked project on GitHub.
[1631.96 → 1635.38] And I mean, and so I'm pretty proud of that.
[1635.38 → 1640.80] I don't know why people feel like they like the project so much, but that's great.
[1640.98 → 1644.22] I mean, it's kind of been kind of a shock to me.
[1644.50 → 1654.36] But we've had 115 people so far, maybe a little bit more, so I just accepted a few more pull requests a little while ago, contributors to the project.
[1654.36 → 1662.00] I mean, those are actual people that have sent a pull request or a code change that I've actually accepted into the McMaster branch.
[1663.32 → 1669.58] So out of 750 people, you know, approximately one out of seven of those have actually sent a pull request.
[1669.70 → 1671.82] And that's, I'm actually pretty impressed by that.
[1672.94 → 1682.24] We have, let's see, 100 or 355 total pull requests so far, over 100 pending pull requests in there.
[1682.24 → 1685.96] And as I mentioned, I think we have about 80 themes and 40 plugins at the moment.
[1686.26 → 1689.96] And I think we have almost 2,000 people following the project on GitHub as well.
[1690.26 → 1695.52] So I think it's a little bit premature for me to say it's been a success.
[1695.70 → 1703.88] But considering I only anticipated a few of my coworkers to use it, I'm kind of shocked by how many people are using it.
[1703.94 → 1707.90] I kind of wish I had more access to see how many people actually have installed it and are actually using it.
[1707.90 → 1713.76] But I think we have maybe over 400 people following us on Twitter now.
[1714.34 → 1723.80] And I don't really know how far that goes because unlike a traditional thing, you know, like a desktop software or something, it doesn't,
[1724.82 → 1729.40] I'm not requiring any licenses or anything or people to register or download it through some process.
[1729.40 → 1737.82] So I don't have any, you know, good download statistics there, which is unfortunate because I kind of wish I had a little bit more insight to see how,
[1738.00 → 1744.50] if I make some changes, like I actually have some ideas for some changes I might want to make for maybe release 2.0 or something,
[1745.06 → 1746.70] how many people might that impact?
[1747.18 → 1750.66] And, for example, if I want to make sure I have backwards compatibility.
[1750.66 → 1756.38] Well, I like the auto update, which is actually a post of the changelog a couple of days ago.
[1757.28 → 1759.36] I was pretty surprised by that.
[1759.54 → 1768.54] And it's actually that quick little post has actually prompted a couple of people to actually try out Shell and specifically Ohms.
[1770.14 → 1775.92] But I think about a week back I posted a post on the changelog called Hooray, Ohms has been updated,
[1776.00 → 1777.56] which I was like, that's pretty wild.
[1777.56 → 1784.56] I logged into my terminal for the first time that morning, and I was greeted by this pretty little message that says,
[1784.68 → 1786.40] hey, would you like to check for updates?
[1786.52 → 1792.66] Maybe you can tie in some sort of hook that counts people who are pulling updates or something.
[1793.52 → 1794.78] Yeah, I thought about that.
[1795.88 → 1805.22] That idea was basically because I was – when I first had that out of that little feature, it's not so much of a – I mean it's an auto updater, but it's not –
[1805.22 → 1812.90] I felt a couple of people have actually complained about it because they would say yes, check for updates, but then there would be no updates.
[1813.00 → 1814.36] And they're like, why isn't it smarter than that?
[1814.44 → 1818.06] But the problem is it's not like a typical desktop software where it's going.
[1818.06 → 1827.66] And I don't want to, without your permission, go and do a network query over Git to check to see if there are any changes in the repository that you need to pull down.
[1827.80 → 1829.74] So I kind of wanted to prompt people.
[1829.88 → 1834.46] And it only checks – it asks you once a day, and you can disable that in your config file as well.
[1834.60 → 1838.98] But for those people that are complaining about that.
[1838.98 → 1839.38] Yeah.
[1841.00 → 1843.14] So if you don't want that, you can disable it.
[1843.42 → 1845.76] Anyway, but I think it's quite useful.
[1845.90 → 1850.44] But yeah, one idea I've had is maybe setting up some sort of web service where it will do some sort of ping to it.
[1850.80 → 1855.38] But I don't want people to be concerned that I'm collecting any unnecessary data from people either.
[1855.60 → 1858.50] So I have to maybe think about that a little bit.
[1859.30 → 1863.76] Because right now I want people to know that you're just kind of mainly interacting with GitHub.
[1863.76 → 1866.08] So that's –
[1866.08 → 1867.20] That's pretty much it then.
[1867.54 → 1869.74] That's a trusted source hopefully for you.
[1869.90 → 1870.16] Right.
[1870.54 → 1874.60] And everything I've tried to do is I try to make it easy to install it and update it.
[1874.82 → 1882.30] So I want people that aren't that savvy – because we have our front-end developers, and they're slowly getting more and more comfortable with the command line.
[1882.64 → 1887.24] But I want to be able to say, hey, next time I come on your machine, I want to have Shell there.
[1887.34 → 1891.70] So if I come help you with anything in your machine, I also think it will be more helpful for you if you have this.
[1891.70 → 1898.78] I can just give them a one-line thing to copy and paste, and it will install it for them automatically, and they don't have to think about it.
[1899.40 → 1908.06] Because until they need to know how to customize them, it's just kind of like Bash, but there are more features when they need it, basically.
[1909.34 → 1910.76] And out of the box, it's identical.
[1911.86 → 1912.12] Yeah.
[1912.32 → 1913.26] Without any configuration.
[1914.02 → 1919.16] So being such a large GitHub project, have you found it difficult at all to manage all the contributions?
[1920.24 → 1921.16] Very much so.
[1921.70 → 1924.74] Now my threshold is to try to keep the pull requests under 100.
[1925.06 → 1925.34] Wow.
[1927.80 → 1932.32] But that just means that I have 100 things that I haven't got to really go through.
[1933.24 → 1940.98] So actually, my plans are hopefully in the next month or so to try to bring in one or two more people to help me with kind of overseeing and managing the project.
[1940.98 → 1948.22] I kind of have some very specific goals in mind for the project, and I want to kind of make sure that stays true before I bring anybody in.
[1948.30 → 1952.92] But that's kind of one of my goals is to hopefully bring in a couple of people to help me with those.
[1953.32 → 1955.02] And there's, I mean, not to dismiss it.
[1955.46 → 1960.74] There's several, like, you know, there's over 100 issues posted on GitHub as well.
[1960.74 → 1967.26] A lot of them are kind of feature requests or little changes more than people asking for changes more than reporting a real issue.
[1968.16 → 1971.04] But a lot of those, I don't really get time to look through those.
[1971.16 → 1975.18] And so, but there's people having conversations and kind of working out solutions themselves.
[1975.18 → 1984.48] And then someone sends a pull request, and I'm like, okay, you guys have had a what seems like a fairly intelligent conversation about this problem, and I'll just accept this in and hope it all works out for you.
[1984.72 → 1987.84] So I think that's been pretty successful so far.
[1987.96 → 1997.24] But I would like to increase, be able to get through those things faster because I know a lot of people have contributed stuff months ago, if not longer, and they want those things to end up in Shelf.
[1997.40 → 2000.44] But they also probably have those in their own fork as well.
[2000.44 → 2008.20] So they're able to do things themselves, but they want those contributions that kind of go out to the wider community, which is what I'm currently bottlenecking in that process.
[2009.22 → 2012.42] Yeah, Kenneth, you probably have a lot of projects to that have a lot of activity.
[2012.52 → 2018.72] It must be, I don't have that many, and I guess we'll probably get into achievements here in a second or two when we mention Coder Wall.
[2018.72 → 2032.20] But I'm kind of curious, though, what sort of process do you go through to manage all that, to deal with that many requests for pulls and contributions and stuff?
[2032.24 → 2035.68] What kind of processes do you have in place to, like, do you dedicate a whole day to it or what?
[2036.72 → 2037.50] You're asking me?
[2037.94 → 2039.08] I'm asking both of you.
[2039.08 → 2041.34] Personally, I just kind of go by that.
[2041.38 → 2043.92] I don't have a tremendous amount of activity.
[2043.98 → 2048.14] I might have, like, one or two pull requests a day on a pretty good day, which happens a couple of times a week.
[2048.46 → 2051.10] But I just try to, you know, take care of them as soon as I get them in.
[2051.32 → 2052.64] Because I welcome the contributions.
[2052.86 → 2058.52] And sometimes I've received a few that are bad, and that's always difficult to manage.
[2058.52 → 2065.76] But, you know, usually I have a pretty strict, well, it's a loose set of guidelines on, you know, how to do it.
[2065.88 → 2076.50] So I think if you document the process well enough, you know, on the standard of the code that needs to be submitted, and the test suite needs to be run and stuff like that, I think it makes things a lot easier.
[2077.36 → 2088.50] Yeah, I think that's one thing I don't have a very good grasp on is since I'm working with, you know, Show, I don't, there's not necessarily a good framework or testing framework kind of that we have kind of built into the project.
[2088.50 → 2091.96] So kind of testing very much is a very manual process.
[2092.08 → 2102.88] And maybe that's something, if any of the listeners out there want to help kind of come up with some idea on how we might be able to make Show, you know, a little bit more test-driven, that would be great.
[2103.06 → 2107.00] But it's a little bit of an awkward project to do that with in some capacity.
[2107.68 → 2114.42] Because I assume when you get a contribution, you have to pull it down locally and see if it just, you know, breaks the installation and the configuration, right?
[2115.12 → 2115.50] Yes.
[2116.50 → 2118.28] So there are some of those basic things.
[2118.52 → 2120.72] And I'm sure there are some things we can kind of do to automate that.
[2121.02 → 2124.34] But nobody's, I haven't spent the time to do that yet.
[2124.54 → 2130.80] And as far as how I'm handling projects, the project, I probably spend a few hours a week on it right now.
[2131.30 → 2134.76] And it might be maybe on a lazy Saturday or Sunday morning.
[2134.76 → 2144.16] Or maybe if I'm not sleeping one night or if I'm just kind of bored with getting client work for a few hours, I'll just dive over to that for a bit to the project.
[2144.36 → 2146.68] And so I try to work through a couple of things.
[2146.78 → 2153.10] And I think GitHub's helped out a lot in the sense that they've been able to provide the merge pull request stuff.
[2153.10 → 2164.86] So it makes it much quicker for me to do some change, test out a couple of things and just click a couple of buttons on the website and get those things pushed in and merged automatically without me having to do too much work from my command line, which is nice.
[2165.50 → 2170.82] So especially for things like themes and stuff, I can look through that and say, well, that looks pretty straightforward.
[2170.82 → 2175.56] I don't even need to test that because it's just someone's theme, and I'm assuming it works for them.
[2175.86 → 2177.20] So, yeah.
[2177.86 → 2179.96] So on a side note here, I have a question for you.
[2180.42 → 2183.88] I am a terrible, terrible, terrible bash programmer.
[2184.74 → 2189.50] And configuring my shell and things like this is pretty much all I ever need to use it for.
[2189.80 → 2196.78] And when you were building on my ZSH, was that something that you encountered a lot?
[2196.90 → 2199.22] Did you have experience with bash programming before?
[2199.22 → 2201.38] Do you know any good resources to point people to?
[2201.48 → 2212.56] Because you cannot Google this stuff because all you get are the people in the forums with the people trying to set up their PHP websites for eBay clones and stuff like that on hot scripts.
[2213.58 → 2213.68] Sure.
[2214.86 → 2215.30] Yeah.
[2215.64 → 2221.22] It was – I don't have an extensive experience with bash and ZSH scripting.
[2221.22 → 2236.72] I've written some basic scripts in the past and I think it was actually a learning experience for me because there's actually quite a number of differences between bash and ZSH and some stuff that I found examples of how to do things.
[2236.72 → 2247.54] Like, let's say, when I created the themes' directory, for example, to try to check to make sure the file exists and before loading it, for example.
[2247.70 → 2251.06] Like, trying to figure out how to do that in bash, I think it actually was a little bit different in ZSH.
[2251.06 → 2257.60] And so I had to figure out there were differences there, which was kind of weird because I was trying to design or build some sort of framework for ZSH,
[2257.60 → 2263.28] but I was having more often look at bash tutorials to do it, which was a little awkward.
[2263.28 → 2275.86] But I have found more ZSH tutorials, and they actually do have quite a bit of documentation if you're willing to spend the time digging through it.
[2275.96 → 2286.66] And a lot of it's a little cumbersome, but ZSH has a number of little interesting ways about how they go about their idiosyncrasies of their –
[2286.66 → 2289.86] I guess you want to call it their language or their scripting language.
[2289.86 → 2295.68] And I don't think that MYTH has that much complexity in it.
[2296.18 → 2299.86] I think a lot of programmers can probably look through it and see what kind of things are being done.
[2301.28 → 2304.94] And so if people want to take the time to do that.
[2305.26 → 2310.16] Which I think has also been why we've had so many contributions that people were able to dive in and say,
[2310.24 → 2312.08] oh, this isn't so complicated. I can make some changes.
[2312.54 → 2317.48] And we've actually been able to attract people that have a lot more experience and been able to help improve things.
[2317.48 → 2323.48] Like recently, people complained that the prompt was kind of slow when you open up a new terminal window.
[2323.96 → 2330.80] And so someone else was able to spend some time working on performance improvements, and we drastically improved the performance.
[2330.90 → 2334.14] Which is one reason why people didn't keep using the project after a while.
[2334.26 → 2337.52] They're like, well, it's a little slow at first, but we sped that up.
[2337.68 → 2339.62] And I wasn't able to figure that out.
[2339.68 → 2341.54] It took someone that had a lot more experience to do that.
[2341.60 → 2342.74] So that was good.
[2342.74 → 2344.82] I liked your disclaimer in the README.
[2344.90 → 2346.12] It says, disclaimer, help out.
[2346.48 → 2354.48] I'm by far being a Z shell expert, so I'm sure there are ways to improve, which probably encourages people to, one, look at you and say, okay, here's Robbie.
[2354.62 → 2355.66] He's a contributor.
[2355.78 → 2357.14] He's a starter of this kind of project.
[2357.26 → 2361.64] But he may not have all the chops to do this thing souped and nuts and make it perfect.
[2361.88 → 2363.22] But he's at least started the ball rolling.
[2363.22 → 2372.84] I think that's the cool thing about open source in general, and I think that's – Steve posted an article to the Change Law this past week or two about getting started in open source.
[2372.92 → 2377.68] And I think people are just sometimes just intimidated that you have to be some sort of quote-unquote expert.
[2378.08 → 2385.72] I think Chris and TPW from GitHub said it best way back in the day that GitHub gives you permission to mess up.
[2385.72 → 2392.50] And I think that's pretty much what people have to cling to is that if you're passionate about this kind of stuff, then start a project.
[2392.68 → 2395.72] Let people know about it, and if it catches on, it catches on.
[2395.80 → 2396.54] You don't have to be an expert.
[2397.62 → 2397.82] No.
[2397.98 → 2401.04] I think this project is a perfect example of that.
[2401.44 → 2408.80] I'm far from an expert at programming or knowing how to properly manage a Z shell configuration.
[2408.80 → 2416.88] But I've been able to pull a lot of different ideas from the Internet, things that I found or people, friends contributing things, and kind of package them up.
[2417.12 → 2423.42] And in a lot of ways, I was inspired by kind of how Rails sets up a project for you and how things are structured.
[2423.56 → 2429.94] And so I was like, well, if I kind of follow some of these patterns, kind of organize things a little bit cleaner in different directories and things,
[2429.98 → 2432.50] maybe this will be easier for other people to work with as well.
[2432.50 → 2447.32] And now it's being the I guess, most popular project on GitHub that deals with your terminal prompt or your shell environment.
[2447.98 → 2454.18] I don't know if that's what was missing, but I guess it was helpful for a lot of people.
[2454.18 → 2460.96] And if you're still really tied to Bash, someone actually created a clone of Mysia's shell called Bash It.
[2460.96 → 2466.08] And they basically took the same exact framework and just did it all in Bash.
[2466.36 → 2471.06] And so there's not as many, they don't have a lot of the features that we have at this point,
[2471.18 → 2477.96] but they have basically the same sort of framework set up so that people can contribute things, themes, and plugins in kind of similar way
[2477.96 → 2479.98] and still stick with Bash if you want.
[2481.12 → 2486.74] So Kenneth asked earlier about, I guess, achievements in terms of this project
[2486.74 → 2489.86] and what kind of stats it had in terms of GitHub as a whole.
[2490.56 → 2495.56] And this project, Myth, is sporting, I think, 99 pull requests right now,
[2496.18 → 2505.24] a number of issues that have been reported, over 1,800 watchers, and almost 800 forks.
[2505.24 → 2510.86] And I see that you actually have your profile up on our friend's website, Coder Wall,
[2511.20 → 2517.00] which we were kind of pinged by Matt Dieters about Coder Wall a little while ago.
[2517.44 → 2519.76] And I see that you have 11 total achievements.
[2519.86 → 2523.64] And one of the cool ones I think that Kenneth might be eyeing on is Lemmings 1000,
[2523.82 → 2531.04] which is if you establish a space in the Open Source Hall of Fame by getting at least 1,000 devs to watch a project.
[2531.04 → 2532.62] So that's probably the cool one there.
[2532.68 → 2536.54] So what do you think about Coder Wall and this achievement in Open Source
[2536.54 → 2543.14] and this kind of, I guess, just attaching badges and giving people kudos for doing good in the Open Source world?
[2544.26 → 2547.04] Well, I think it's kind of a cute idea.
[2548.26 → 2554.90] I signed up for Coder Wall a few days ago, and I had to wait to see what my achievements were.
[2556.12 → 2557.86] And so it was kind of neat to look at that.
[2557.86 → 2563.24] But I think there's kind of, I'm not sure how I feel about badges in general for stuff like this,
[2563.40 → 2565.30] but kind of more of a personal opinion.
[2565.86 → 2572.86] I feel like I'm not sure that achievements or badges are what people, developers are kind of working towards.
[2573.10 → 2574.86] Maybe that's going to motivate some people,
[2575.04 → 2579.10] but I think a lot of people that are already contributing to Open Source projects,
[2579.20 → 2582.28] they're doing it because that's what they love to do and that's what they want to do.
[2582.28 → 2586.32] And it's kind of nice to be reminded that you have these achievements, possibly,
[2586.50 → 2591.02] but that's not, I don't, like, I'm not sure if it's going to change my personal behaviour
[2591.02 → 2592.92] about how I'm approaching my Open Source projects
[2592.92 → 2596.12] because I'm already doing the things I do because I want to do them,
[2596.26 → 2599.88] and my achievement is seeing people use my projects.
[2600.06 → 2603.00] And so, but it's nice to get some badges, I suppose.
[2603.26 → 2604.48] It's kind of like a byproduct, right?
[2604.56 → 2605.78] I mean, you don't exactly say,
[2605.78 → 2610.52] hey, somebody developed this so I can get some credit here in my community
[2610.52 → 2611.98] because I want this stuff.
[2612.22 → 2613.60] But I guess on a side note, too,
[2613.68 → 2615.18] the reason I wanted to bring that up is,
[2615.46 → 2616.92] for one thing, it's kind of cool,
[2617.54 → 2619.50] this kind of project and what it does.
[2619.86 → 2623.24] And number two is that sometime this week,
[2623.90 → 2626.28] they'll be debuting a changelog badge.
[2626.36 → 2628.32] So if you've been, if you're listening to this podcast
[2628.32 → 2631.32] and you've been logged and or change logged,
[2631.34 → 2633.84] then you're going to get a badge that says you've been change logged.
[2633.84 → 2638.34] Yeah, then I'm going to hit the almighty 12 total achievements.
[2638.46 → 2638.96] That would be awesome.
[2639.10 → 2639.44] There you go.
[2639.50 → 2641.00] You have almost a full page then.
[2641.80 → 2644.56] I feel like they need to add another one for,
[2645.08 → 2649.80] I feel like there's a big difference between 100 forked projects.
[2650.02 → 2652.06] I'm guessing the next one doesn't go to 1,000.
[2652.26 → 2657.08] So since that's like another 250 approximately forks to go,
[2658.80 → 2662.08] I guess I'm going to have to encourage my users out there
[2662.08 → 2665.22] to get other people to use the project so I can hit 1,000.
[2665.44 → 2667.32] So I can hit magic 13.
[2668.08 → 2669.00] Any more than that, though,
[2669.02 → 2671.34] I think DHH says there are too many things on a page.
[2671.82 → 2672.80] Oh, there you go.
[2673.52 → 2676.00] So what open source are you really excited about right now?
[2676.06 → 2679.06] What projects are you really hoping to get into in the future?
[2679.66 → 2680.54] Good question.
[2680.92 → 2683.96] Well, actually, a lot of my time isn't spent doing development these days
[2683.96 → 2689.88] because I'm kind of working more on strategy-type issues with our clients and stuff.
[2690.68 → 2694.98] So, you know, OhMyZShout is one of the few times I actually get to do kind of more geeky stuff.
[2695.02 → 2697.44] And I do help out on some programming from time to time.
[2697.70 → 2701.20] So stuff that my people on my team are talking about, you know,
[2701.20 → 2704.16] they're quite interested in, I mean,
[2704.22 → 2707.48] we're always looking at different testing frameworks within Ruby and Rails and such.
[2707.48 → 2711.44] But, you know, we've been looking at NoSQL stuff for a while
[2711.44 → 2714.74] and trying to figure out when we can have time to actually work on some of the implementation
[2714.74 → 2715.94] for one of our projects.
[2717.34 → 2719.08] Otherwise, we're also looking at CoffeeScript
[2719.08 → 2724.38] since that looks like that's going to be bundled into Rails a little bit more in the future.
[2725.00 → 2726.66] Because we do quite a bit of JavaScript,
[2726.98 → 2730.12] and so none of us have had time to really experiment with it.
[2730.14 → 2733.34] So I think that's something we're going to be spending a little bit more time with soon as well.
[2733.34 → 2738.30] And when you experiment with some of these types of new tech, I guess you'd say,
[2738.40 → 2740.78] do you end up doing side projects for fun?
[2741.40 → 2744.00] Like, I guess, like Ruby URL or something like that?
[2744.08 → 2748.08] Is that how you tend to learn new things and have fun with it?
[2748.14 → 2749.76] Or do you actually go right into production with it?
[2751.58 → 2756.94] I think I haven't done any kind of fun little open source kind of Rails projects in a few years.
[2757.02 → 2761.44] I am usually more motivated by some sort of specific end goal
[2761.44 → 2762.78] and try to work my way towards that.
[2762.78 → 2767.86] And sometimes I'll use some new tools or technology to help get that, to try it out.
[2767.88 → 2772.76] Since I know it's kind of a there's a very low risk if I pick the wrong technology for that project
[2772.76 → 2774.40] that's not going to have a huge consequence.
[2775.28 → 2778.58] Which is, like, one of our projects we work with are clients.
[2778.66 → 2780.02] We've been working with them for four years.
[2780.20 → 2781.74] And so it's much riskier.
[2782.26 → 2785.72] There's a higher risk of, you know, problems if we introduce something new
[2785.72 → 2787.16] that we haven't had a lot of time to experiment with.
[2787.24 → 2789.30] So we do try to experiment.
[2789.30 → 2793.12] I think some of the other people on the team will try to experiment with smaller little side projects.
[2793.44 → 2798.00] I less myself because I'm usually focused on production code usually.
[2798.42 → 2800.90] So that brings in an interesting question there.
[2801.02 → 2806.42] From a business perspective, is there any open source that really works well for you?
[2806.42 → 2809.42] As opposed to, you know, because usually when we ask this question,
[2809.42 → 2812.00] it's more of a technical thing or someone wants to play around with.
[2812.12 → 2817.30] But from a business perspective, is there anything that really brings a lot of opportunity?
[2819.12 → 2827.42] Well, I mean, years ago, you know, I've been a big fan of PostgreSQL for maybe seven or eight years now.
[2828.04 → 2831.82] And early on, I remember one of the big reasons I liked the project so much,
[2831.86 → 2833.88] not just because I thought it was a great database.
[2833.88 → 2839.08] And it was a lot of, you know, at the time, you know, we used to get to tout asset compliance
[2839.08 → 2841.82] and used to be able to nitpick a lot of problems that MySQL had.
[2842.22 → 2847.08] But we didn't feel like MySQL had, I mean, was too tied to their commercial side of their business,
[2847.08 → 2848.54] and that was potentially problematic.
[2849.56 → 2854.36] You know, we, you know, the Postgres community foresaw years in advance that there were problems
[2854.36 → 2858.72] with the way MySQL was structured, and it could be potentially problematic for MySQL in the long run.
[2858.72 → 2865.08] And, you know, several years later, they get purchased by Oracle, and kind of the future of MySQL is still a little unclear.
[2866.16 → 2868.34] Postgres is still a community-run project.
[2868.50 → 2874.10] I think that's, you know, from us, we were always, we, we, I used to work on projects before Planet Argon,
[2874.26 → 2879.76] where I worked at a Postgres consulting company, actually, and we used to bundle Postgres into the products we developed.
[2879.76 → 2886.50] And sometimes they would get distributed as kind of a packaged product, and we didn't have to worry about any licenses with that,
[2886.56 → 2889.58] whereas MySQL, you actually had to worry about commercial licenses to do that.
[2889.66 → 2895.06] You couldn't actually distribute a commercial product with MySQL bundled into it, whereas we could with Postgres.
[2895.86 → 2899.44] Now, when we moved to Rails, everything's kind of hosted a little bit differently,
[2899.54 → 2904.88] and we're not really worrying about, you know, deploying or basically selling a product that includes the database itself.
[2904.88 → 2909.52] So that kind of problem kind of went away when I was focusing more on web products like this.
[2909.68 → 2913.70] But kind of get back to your question a little bit.
[2914.76 → 2921.22] I think from us, it's always, it's been an easy sell for us, because I think a lot of our clients want to keep, you know,
[2921.30 → 2924.86] their recurring costs down when it comes to licenses and such.
[2924.96 → 2932.02] And so, you know, they might see the, oh, well, you know, I think we're also seeing a lot less concern about,
[2932.02 → 2935.00] like, you know, we're comparing a .NET project to a Rails project.
[2935.14 → 2937.74] We just, we don't see those, we don't have those conversations anymore.
[2937.94 → 2940.02] We used to have that conversation four or five years ago.
[2940.32 → 2941.40] We don't have that anymore.
[2941.52 → 2944.90] Nobody's, nobody, no new projects are coming to us.
[2945.22 → 2947.58] And they're like, well, you know, we're kind of weighing these few options.
[2948.04 → 2952.94] They've already kind of made the decision that open source platform is what they're looking to work with,
[2953.08 → 2954.76] and which is kind of nice.
[2954.86 → 2957.72] That means, I don't want to say that the open source community has won the argument,
[2957.72 → 2961.66] but I think there's a lot more to show for it now, I think.
[2961.66 → 2964.82] Like, it's more trusted, I think, in the IT world.
[2965.70 → 2971.46] Seems like most of the agnostic projects really seem to offer a lot of possibilities in that area.
[2972.02 → 2975.16] Like, when you're working with Rails, you know, it's very database agnostic, right?
[2975.52 → 2975.78] Yes.
[2975.88 → 2979.28] So you can, I think that really, I don't know, it just seems like a great trend
[2979.28 → 2981.90] that every single individual technology always kind of goes towards.
[2981.94 → 2984.20] Like, with all this AWS outage we had recently,
[2984.20 → 2988.32] I think we're going to see a lot more, you know, cloud deployment systems
[2988.32 → 2992.50] that are designed to work with different providers and things like that.
[2992.80 → 2994.22] So it's an exciting future.
[2995.14 → 2995.36] Indeed.
[2996.76 → 2999.10] But I guess that leads us to the end of the call.
[2999.24 → 3000.78] Robbie, it was fun chatting with you.
[3000.92 → 3003.42] Thanks for taking the time to speak with us so late in your evening
[3003.42 → 3007.70] after getting up so early and having some fun over there in Paris
[3007.70 → 3010.12] and, I guess, seeing some culture and, you know,
[3010.20 → 3012.90] the occasional Frenchman walking by or something like that.
[3013.12 → 3015.02] So, yeah, thanks for having me on.
[3015.24 → 3019.00] I'm glad I was able to kind of share my experiences with the project so far
[3019.00 → 3020.78] and it was nice talking with you both.
[3021.06 → 3025.10] And thanks to Kenneth, too, for coming in to also join me on this call.
[3025.16 → 3025.74] I appreciate that, Kevin.
[3026.20 → 3026.52] Anytime.
[3026.52 → 3026.60] Anytime.
[3026.60 → 3026.64] Anytime.
[3026.64 → 3026.68] Anytime.
[3026.68 → 3026.72] Anytime.
[3026.72 → 3026.76] Anytime.
[3026.76 → 3027.18] Anytime.
[3027.18 → 3028.60] Anytime.
[3028.60 → 3028.64] Anytime.
[3028.64 → 3028.68] Anytime.
[3033.42 → 3034.42] Anytime.
[3034.42 → 3035.42] Anytime.
