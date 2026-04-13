[0.00 --> 14.20]  Welcome back everyone. This is the change log and I'm your host Adam Stachowiak. This is episode
[14.20 --> 19.54]  155 and on today's show I'm joined by Scott Hammond, the CEO of Joyent, to talk about the
[19.54 --> 25.40]  future of Node.js. We talked about everything, the past, the present, the future, Node.js,
[25.40 --> 32.20]  the I.O.J.S., Node.js, the Convergence, lots of history, lots of things going on there.
[32.84 --> 37.44]  We even had to come back and record more because the original part of this was recorded before
[37.44 --> 43.82]  I.O. announced this week, the IOTC announced joining Node.js, so we had to come back and
[43.82 --> 49.54]  record even more to cover that piece as well. And great show today. So just when you think this
[49.54 --> 54.68]  show's over, stick around for an extra 10 or 15 minutes for even more with me and Scott talking
[54.68 --> 60.82]  about the recent news of I.O. joining Node.js Foundation, we have three awesome sponsors,
[61.40 --> 68.64]  CodeShip, Tatao, and DigitalOcean. Our first sponsor is CodeShip. CodeShip is a hosted continuous
[68.64 --> 74.92]  delivery service focusing on speed, security, and customizability. You can set up continuous
[74.92 --> 80.38]  integration in a matter of seconds and automatically deploy your code when your tests have passed.
[80.38 --> 85.98]  CodeShip supports your GitHub and your Bitbucket projects, and you can get started with CodeShip's
[85.98 --> 93.14]  free plan today. Should you decide to go with a premium plan, you can save 20% off any plan you
[93.14 --> 99.04]  choose for the next three months by using our code, TheChangelogPodcast. Again, that code is
[99.04 --> 106.16]  TheChangelogPodcast. Head to CodeShip.com slash TheChangelog to get started. And now on to the show.
[106.16 --> 118.04]  Hey everyone, Adam here with Scott Hammond, the CEO of Joyent. For those who know, Joyent has been
[118.04 --> 124.32]  the steward of Node.js for quite some time now. So we're talking to Scott today about the future of
[124.32 --> 129.50]  Node. Scott, welcome to the show. Thanks, Adam. It's great to be here. Well, Scott, when you're in front
[129.50 --> 136.38]  of an audience like you are today, just so you know, our audience is very nerd to the core, as my
[136.38 --> 144.00]  co-host Jared says. Very hacker. They're the people who are forking, committing, contributing, leading.
[145.26 --> 153.38]  In many ways, the technology itself and highly influencing the applications inside of companies
[153.38 --> 158.58]  that get built with Node.js and technologies like it. So when you're in front of that kind of audience,
[158.76 --> 159.74]  how do you introduce yourself?
[161.36 --> 168.34]  Great question. So, you know, my sense of open source, I've been at Joyent for just a little
[168.34 --> 176.06]  under a year now. And open source is, it is the right model to go develop software now. So
[176.06 --> 182.62]  it's a great model for tapping into the energy and passion that people have to go get involved with
[182.62 --> 191.00]  projects and contribute new ideas and vet things in the public. And so I would maybe introduce myself
[191.00 --> 197.42]  as a huge advocate of the open source model, although I've only been at Joyent now for probably
[197.42 --> 204.50]  nine or 10 months. One of the first things that I did was work with the team and work with our board to
[204.50 --> 211.30]  take our entire software portfolio and open source it. So although most people in the open source
[211.30 --> 216.56]  community probably know Joyent for our role and our relationship with Node over the last five years,
[217.12 --> 223.30]  we are all in on open source and really see that as the model for developing software going forward.
[223.92 --> 229.92]  Yeah, I know that I've heard that you're all in. So in what ways is doing it all in on open source?
[230.04 --> 234.36]  I can, beyond the efforts and stewardship you've done of Node over the last five years,
[234.50 --> 237.48]  and what other ways are you breaking into open source?
[238.04 --> 242.74]  So we have, you know, the other part of our business, well, you, I'm not sure how familiar
[242.74 --> 250.66]  you are with the history of Node and Joyent, but we started using Node. We met Ryan Dahl probably five
[250.66 --> 258.84]  years ago. People in Joyent started working with Ryan, loved the Node project. And at that time,
[258.84 --> 264.72]  we were looking for a new technology platform to build out our next generation cloud management
[264.72 --> 270.88]  platform. And we looked at a lot of different technologies. And Node was one that we just kept
[270.88 --> 274.84]  coming back to and really fell in love with and loved what Ryan was doing with it. And it turned
[274.84 --> 282.04]  out to be the perfect platform for us, the perfect technology for us to go write our next generation
[282.04 --> 287.38]  cloud management platform in. So if you go to the Joint Public Cloud, it's a infrastructure
[287.38 --> 293.46]  as a service public cloud platform. It's rolled out in data centers all around the world. That's
[293.46 --> 302.80]  all, everything you see there is written in Node. We also built a big data store, an object management
[302.80 --> 309.24]  store called Manta. That is a converged compute and storage solution that allows you to spin up your compute
[309.24 --> 313.78]  jobs in containers right on your object store. So you don't have to move your data all around.
[314.30 --> 321.08]  And that's written in Node as well. So those two platforms were proprietary software. You could
[321.08 --> 328.36]  use them, sort of pay by the drink up in our public cloud. But we also took those and
[328.36 --> 336.26]  distributed those on memory sticks so people could deploy them on-prem. So you could deploy a private
[336.26 --> 344.18]  cloud or you could deploy an object store on-prem into proprietary products, one called Smart Data
[344.18 --> 352.10]  Center, one called Manta. And in November, I think it was November 4th, we open sourced both of those
[352.10 --> 358.74]  products and all the related tools that go with them. So you can now go to GitHub and download those
[358.74 --> 362.82]  products and roll them up. And if you follow along those on Twitter, you'll see that a lot of people have
[362.82 --> 370.58]  done so. So we don't have anything that's closed source anymore. Everything that we do in the
[370.58 --> 371.86]  market today is open source.
[371.86 --> 379.86]  So being all into open source now, the new efforts that you mentioned with your public cloud,
[379.86 --> 386.10]  is that because of the wins and strides of your Node stewardship and what's happened with the Node
[386.10 --> 390.58]  community over the years of this past year, is it because of that progress that's sort of led you into
[390.58 --> 398.58]  believing that open source is the way? Certainly Node was a great example. But I think Node is one
[398.58 --> 406.98]  example of many of how most software now, most system software now is being built in an open
[406.98 --> 411.38]  source model. You look at all layers of the stack, whether it's the database layer, you look at the OS
[411.38 --> 417.46]  layer, you look at the PaaS layer. All of that is now being written and delivered in an open source
[417.46 --> 425.62]  model. And it's great to see a couple of forces come together to support that model. One is certainly
[425.62 --> 433.06]  the open source community. You get to tap into a broad set of individuals who share your passion on
[433.06 --> 439.22]  a specific topic area and you can collaborate together and they can contribute to the project
[439.22 --> 445.54]  in a lot of ways. They can contribute code, they can contribute ideas, contribute use cases, contribute with
[445.54 --> 453.62]  evangelism. There's a lot that can be done and open source is a great development model that allows
[453.62 --> 461.14]  you to engage with a very energized community to help move the project forward. So that's one vector on
[461.14 --> 466.34]  sort of developing software. The other is from the consumer perspective or the user perspective,
[466.34 --> 474.42]  a lot of a lot of people who are consuming technology are looking for an open source way. You have
[474.42 --> 479.70]  certainly some people in the market. I think Martin Mikos has a pretty famous blog where he talked about
[479.70 --> 490.98]  cutting the market up into organizations that will always want to find a way to expend all energy to
[490.98 --> 496.98]  to consume software in a free model. And they'll never pay for anything, but they will use the software.
[496.98 --> 502.58]  They want to use it and they want to then contribute back. And then you have other organizations that
[503.14 --> 511.06]  will pay any amount of money to save time. And those organizations tend to buy enterprise licenses.
[511.06 --> 516.66]  They buy a lot of tooling around, services around. So you have two different markets there, but both of them
[516.66 --> 521.14]  are going to be able to pay for them to benefit from an open source model where it's much easier for them to
[521.14 --> 527.86]  consume technology and consume software. And then in most cases they're not only consuming, but they're
[527.86 --> 536.90]  contributing back. So you see a big push on the side of developing the software by sort of energizing
[536.90 --> 542.18]  that community. And then you see a lot of pull from the consumer side, the customers and users who
[542.18 --> 547.62]  want an open source model, they either want a free version that they can then bring in and add on to,
[547.62 --> 552.26]  or they want an enterprise version that they can bring in and open in a sort of free version,
[552.26 --> 559.14]  evaluate. And then when they start to deploy, they want to buy the tooling and buy the enterprise grade
[559.14 --> 564.26]  functionality or enterprise level functionality that comes along with a set of other tools and
[564.26 --> 566.82]  capabilities around it. So big push on both sides.
[566.82 --> 570.66]  Yeah, it's definitely, I mean, on the commercial side, you have a lot of
[571.38 --> 576.26]  ways where companies can start to start to take part and be a part of the community and
[576.98 --> 581.22]  support the community, not only financially, but also with, you know, paying developers to be a part
[581.22 --> 588.02]  of it. I know that both Isaac Schluter and Ryan Dahl, big contributors to Node and obviously the evolution
[588.02 --> 595.14]  to NPM with where Ryan or with where Isaac's at now, that's all been because of companies like yours
[595.14 --> 599.62]  supporting those developers to be a part of it over those years. And you take that and you
[599.62 --> 604.50]  multiply it across other companies that have influences into Node and other ecosystems as well.
[604.50 --> 608.50]  This isn't a new thing, but it's definitely a trend across open source.
[609.78 --> 615.14]  You know, one thing, one reason why I wanted to have this call with you is that the title that I'm,
[615.14 --> 619.78]  at least the working title, and you tell me if you think this is a good title for it or not for this
[619.78 --> 624.26]  show is I wanted to talk to you about the future of Node.js. So I thought it'd be good to call it
[624.26 --> 629.46]  the future of Node.js with Scott Hammond, sort of break down what the history of Node has been,
[629.46 --> 633.06]  where your placement, you personally, as well as Joient has been into Node's history,
[634.18 --> 638.02]  what your involvement has been over these years, where it's, how it's shifting and changing,
[638.02 --> 642.58]  what you see, where you see it's going. And I really want to hope, I really hope to,
[642.58 --> 648.42]  to sort of pull out of this conversation, a perspective for the community who cares about Node.
[648.42 --> 652.50]  And then subsequently, IOJS, because of the fork most recently,
[653.78 --> 659.38]  I hope to sort of get a snapshot of Joient's perspective and your feelings about where Node is
[659.38 --> 664.90]  going and your participation in making that happen and letting go in areas where you need to and
[664.90 --> 670.10]  supporting other areas. Do you think that's fair to say that's what this conversation should be about?
[670.10 --> 676.66]  Yeah, I think that's great. The timing is perfect. This is a big transition period for Node.
[676.66 --> 683.54]  Node.js and a lot of questions out there. But we have, you know, some pretty good answers that
[683.54 --> 687.70]  we're forming with the help of the community and a lot of help from the community around the
[687.70 --> 691.46]  direction, the future of Node. So the topic is perfect.
[691.46 --> 699.22]  So what do you know then about the history and only, only just to mention it, not so much to go deep
[699.22 --> 705.94]  into it, but the history of how Ryan and how things got started with Node and then Joient's support of
[705.94 --> 710.58]  that and then ultimate stewardship of that. And then even some of the copyright parts of that. What do you
[710.58 --> 713.46]  know about Joient's history and Node's history?
[713.46 --> 719.94]  You know, I know a decent amount, but I wasn't here firsthand. So I have secondhand reports in a
[719.94 --> 725.62]  fair amount of detail. But as I said, about five years ago, we started working with Ryan and
[727.38 --> 733.06]  believed in Ryan and believed in his vision around Node and loved what he was doing around this
[733.06 --> 741.70]  real low latency platform. So when we started using it and building out our products internally
[741.70 --> 751.38]  using Node, we decided that we really wanted to sponsor your Ryan and sponsor his vision. So we hired
[751.38 --> 758.74]  Ryan and we provided a lot of funding, a lot of resources, a lot of additional headcount and resources to
[758.74 --> 768.26]  to invest in him and his vision on where he wanted to take Node. And that really began the chapter of
[768.26 --> 777.22]  Joient as the steward of the project and really let him go drive the direction of Node and provide
[777.22 --> 780.98]  support and resources and technology to help him go drive that.
[780.98 --> 786.98]  So do you think it's safe to say or fair to say on your part what you know with the history? Do you think
[786.98 --> 793.14]  do you think Node would be where it's at today without that event, without joint support?
[793.14 --> 801.14]  You know, hard to say because I wasn't here, but I would say there was a good intersection there that
[802.34 --> 808.90]  we bought in, you know, we believed, we bought in and we believed in Ryan's vision. And I think our
[808.90 --> 816.50]  sponsorship and the funding and resourcing that we provided really was a good assist for Ryan.
[816.50 --> 822.26]  You know, if we weren't here, maybe he would have, I mean, the project was great. So maybe he would
[822.26 --> 828.50]  have found another organization to provide the resources that we provided. That could be
[830.02 --> 836.34]  hard to tell, but certainly I know that we did play a big role in helping him get established and
[836.34 --> 841.54]  helping the project get built out and really get lift off. So I'd like to say we played a good,
[841.54 --> 847.30]  a very positive part in that. We feel really good about our contribution there in support of Ryan
[847.30 --> 848.50]  and getting that project going.
[848.50 --> 853.70]  So you took the CEO role, well, you were, I guess you didn't take it. You were invited to take it,
[853.70 --> 855.30]  right? And then you said, yeah, I'll take it. Sure. Why not?
[856.58 --> 862.90]  At joint. So last year, June 2014, almost a year ago, just shy of a year, you took over the CEO role at
[862.90 --> 868.58]  joint. What's been, you know, at what point were you exposed to node? What, what, at what point were
[868.58 --> 874.10]  you exposed to what node meant to joint? And then at what point where are you thinking about
[875.46 --> 879.62]  the stewardship, the direction, and at what point did you sort of deal with, I guess, the,
[880.50 --> 882.98]  let's start there. We'll kind of cover some other things after that.
[882.98 --> 889.94]  Well, I'd say, but before I came to joint, I was well aware of the, the popularity and the success
[889.94 --> 897.14]  of node, uh, in the user base. Um, you know, the organizations and individuals who are, who are
[897.14 --> 903.30]  using node love it and they love to talk about it and they're having huge success. So, um, so I,
[903.30 --> 908.98]  I was well aware of that. Um, what I was not quite aware of was some of the challenges that node was
[908.98 --> 914.26]  facing and sort of had been facing for, you know, really ever since Ryan, uh, moved off the project.
[914.26 --> 922.10]  So, um, that I, I had a pretty, a pretty fast ramp on, uh, you know, once I got to joint and really
[922.10 --> 927.46]  dove in to see what was going on. So some would say, well, I don't know if it would be some,
[927.46 --> 932.26]  I think it would pretty much majority, but Ryan stepping away was mainly because of burnout.
[932.82 --> 937.10]  And that happens a lot. We've talked about burnout. Uh, you know, as you go back and listen to the
[937.10 --> 943.18]  history of this show and maybe pick some, um, Capistrano reminds me, uh, of some burnout.
[943.18 --> 949.46]  We talked about that, but, um, I think it was Lee Hanley, um, was on that show there.
[950.14 --> 954.98]  But, um, you know, now with node being more popular, it's spread across more people. It's,
[955.08 --> 959.58]  you know, it's sort of taken this new life. So it's less likely to be, for people to be burnt out.
[959.58 --> 964.58]  But, you know, I have conversations with like Michael Rogers or others in the community. I can just see
[964.58 --> 971.08]  them, like I can feel their pain with how much effort they're putting in towards, um, the fork
[971.08 --> 976.50]  of node, which is IOJS. And then ultimately the reconciliation, this node foundation. So I want
[976.50 --> 985.08]  to get into some of that, um, here in a bit, you came on board in June at one point did IO fork
[985.08 --> 987.26]  node and become, that was about nine months ago, right?
[987.26 --> 996.52]  No, uh, no IO Fedor forked right at Thanksgiving time. So end of, end of November.
[997.64 --> 1003.18]  Okay. So we're six months ago. Yeah. Okay. You got six months ago. So that was, was that a surprise
[1003.18 --> 1012.12]  to you? Um, I think it was a surprise to everybody. Uh, so yeah. Why do you think it was a surprise?
[1012.12 --> 1020.16]  Yes. So when I, uh, when I, when I first came to joint and first started to get steeped in,
[1020.32 --> 1026.92]  into what was going on with node, I spent a lot of time talking to everybody I could in,
[1026.92 --> 1033.96]  in the community, big customers, small customers, uh, the, the vendor, the node specific vendors,
[1033.96 --> 1040.80]  uh, developers, there were people, uh, who were starting to push this agenda around, uh, a node
[1040.80 --> 1045.18]  forward organization, which were some, you know, early discussions around a different governance
[1045.18 --> 1050.74]  model for node. Um, really spent some time with them and said, all right, there, there is some
[1050.74 --> 1056.06]  strife in the community. Uh, I think the best thing to do is let's get everybody together. Let's get a
[1056.06 --> 1062.04]  group of people together who can broadly represent, uh, the different constituents, uh, the, the users,
[1062.22 --> 1068.18]  the developers, uh, the vendors, uh, other contributors, other open source people. And so I started the,
[1068.18 --> 1073.64]  the node advisory board and got that group together and we, you know, we've been meeting once a week
[1073.64 --> 1081.66]  or every other week ever since probably the middle of October. And it seemed like, uh, at the time,
[1081.66 --> 1091.70]  uh, everybody was, was very much, uh, opposed to a fork that, uh, they were concerned that a fork
[1091.70 --> 1096.34]  would create a lot of disruption in the market. It would create a lot of risk in the, in the eyes of the
[1096.34 --> 1101.32]  users, uh, it would fracture the community that there would really not be any good come from it.
[1101.48 --> 1108.60]  So that seemed to be a fairly unanimous, uh, you know, opinion. So, um, when the fork did happen,
[1108.60 --> 1113.56]  uh, I think everybody seemed to be surprised and we had an advisory board meeting right after that.
[1113.56 --> 1121.06]  And everybody certainly was surprised. Um, so I, it seemed at that time that we were on a path to
[1121.06 --> 1128.74]  work through, to work through a whole set of, uh, items together, uh, that we're going to, uh, really
[1128.74 --> 1134.50]  understand what the, where the issues were and then go address them, go make the right changes.
[1135.04 --> 1141.50]  Um, as I said, I came in fairly, uh, you're fairly late in the node game after, you know,
[1141.50 --> 1147.30]  node has been out for about five years. So I, I, I had a set of fresh eyes to bring to the problem,
[1147.30 --> 1153.30]  to bring to the situation. I wasn't encumbered by any of the, uh, maybe emotional issues of the
[1153.30 --> 1157.32]  past or relationships or actions or anything in the past. So I felt like I could be pretty
[1157.32 --> 1161.16]  objective. And it was clear to me that I wanted to get a group of people together that broadly
[1161.16 --> 1165.68]  represented the community and work with them to go drive a bunch of changes. And it seemed like
[1165.68 --> 1169.42]  we're on that path. We worked through governance issues, we worked through community issues,
[1169.42 --> 1173.92]  we worked through IP issues, and we came up with some really good recommendations on that.
[1173.92 --> 1178.54]  So it looked like we're headed down the right path that, uh, you know, ultimately has led
[1178.54 --> 1184.32]  to a foundation. Uh, but it seemed like we're on a good path to all work together to go do
[1184.32 --> 1189.28]  that. So when Fedora hit the fork button, uh, and then, you know, IO, you went off, that
[1189.28 --> 1191.84]  was a surprise to me. It was a surprise to everybody, I think.
[1192.56 --> 1199.76]  So Fedora hit the fork button, um, back in December and the, and from the community's
[1199.76 --> 1203.90]  perspective, like there's two sides of this. You got, um, as you may,
[1203.92 --> 1208.50]  mentioned earlier, the, the vested interests, the interests of open source and how these
[1208.50 --> 1212.82]  communities prop up and technologies move forward is that you've got company issue interests.
[1213.26 --> 1218.46]  You've got the, you know, sort of the bare metal, uh, level interest, which is the developers
[1218.46 --> 1223.54]  moving things along. And some of those developers are sponsored by companies, though they are
[1223.54 --> 1227.12]  the developers interest, putting them in the place. Um,
[1227.12 --> 1235.16]  when you, when you see for, you know, Fedora hit that fork button and IO, um, get a lot of,
[1236.12 --> 1240.60]  I wouldn't, I wouldn't, I would say right away, the biggest thing they started to do was to
[1240.60 --> 1247.82]  organize the community and, and actually submit some releases to move things forward. They adopted
[1247.82 --> 1252.46]  V8 pretty, the next release of V8 pretty quickly and various things started to happen. And the reason
[1252.46 --> 1257.98]  why they had done that was mainly because of stagnation and with node being stewarded by
[1257.98 --> 1265.90]  joint, um, how was joint leading node was node in, was node being led by joint was, or was node
[1265.90 --> 1270.24]  being, um, led by the community whenever that fork button was, was pushed.
[1270.24 --> 1281.54]  So, you know, when Ryan started the project, uh, it was run, he ran it as a typical BDFL model. And then, uh,
[1281.54 --> 1290.80]  when he turned over the reins to Isaac, uh, Schluter, Isaac continued to run that in a BDFL model. Um, and then
[1290.80 --> 1299.62]  he left, uh, went over to NPM and, uh, and then, uh, TJ took over as the BD. Um, TJ,
[1299.62 --> 1306.54]  TJ is, so I say while, while joint has been running it, it was a fairly typical BDFL model. Uh, TJ
[1306.54 --> 1314.02]  really started to relax the constraints around that last summer and started to really make sure he had
[1314.02 --> 1318.60]  buy-in from people of what, what people wanted to do, what the different contributors wanted to do.
[1319.26 --> 1325.72]  Um, but my, you know, I think at that point, uh, most of the people in the community had, uh,
[1325.72 --> 1332.64]  determined that it was going to be a BDFL model forever. And I know that was, uh, some of the, the frustrations of,
[1332.64 --> 1339.84]  of the, uh, the, some of the developers who were trying to get changes in and didn't feel like they were, uh,
[1339.84 --> 1345.64]  getting them in as fast as they wanted to get in and didn't feel like they, they really had a strong enough voice in the
[1345.64 --> 1354.16]  direction of the project. Um, uh, so, um, so yeah, I think that that's how the project was run. Uh, that was one of the things that we,
[1354.16 --> 1359.28]  we started to address immediately with the advisory board. I'd say that was the biggest issue that was on the
[1359.28 --> 1365.50]  table was how to open up the governance model and the organization model to make it easier to bring,
[1365.50 --> 1375.72]  uh, more collaborators into the project and, uh, to, to migrate away from, uh, BDFL model and migrate into,
[1375.72 --> 1382.30]  uh, more of a consensus driven model. And, uh, there was a working group in the advisory board that spent a bunch
[1382.30 --> 1387.18]  of time hashing through that and, uh, came up with some really good recommendations and, you know,
[1387.18 --> 1392.50]  we've started to adopt them, those recommendations, you know, that, that model that, that's what, uh,
[1392.50 --> 1400.48]  I, O has gone on to, to, to, to start with and then iterate on. And, and then ultimately, uh, I think if,
[1400.48 --> 1406.06]  if, if, uh, your audience has been following along with what's going on on GitHub, uh, with the foundation,
[1406.06 --> 1412.36]  we've had a lot of discussions and iterated around, uh, the governance model and the dev policies that
[1412.36 --> 1418.30]  we're going to deploy and we're going to use in the foundation. And, uh, you know, that we, that's all
[1418.30 --> 1424.34]  based on that same, the same thread. So, you know, we, we came up with some good ideas, uh, you know,
[1424.34 --> 1430.38]  in the advisory board, we, uh, then the IO guys, the IO team iterated on them. And now, you know,
[1430.38 --> 1436.34]  that became the, the initial basis for what the foundation is going to use. So, you know, that's,
[1436.52 --> 1442.30]  that, that's been a big push to allow a broader contribution and broader input from the, from
[1442.30 --> 1446.20]  the community around, uh, you know, the direction of the project. So it truly is community driven.
[1447.42 --> 1451.62]  That's probably a good place to take a break real quick. We'll, uh, take a break, listen to a sponsor.
[1452.14 --> 1457.54]  And then when we come back, we'll talk a bit about, uh, the deeper parts of node foundation and what's
[1457.54 --> 1462.94]  happening there as it becomes a potential reconciliation with IO joining that. I know
[1462.94 --> 1466.30]  there's an invitation out there, so let's break real quick. And when we come back, we'll talk about
[1466.30 --> 1473.78]  that. You've heard me talk about top towel several times in this podcast and top towel is by far the
[1473.78 --> 1478.50]  best place to work as a freelance software developer. Well, they have this term elite
[1478.50 --> 1484.74]  engineer, and that defines the kind of software developer that works at top towel. I had a chance
[1484.74 --> 1490.18]  to sit down and talk to Brendan Beneshawn, the co-founder and COO of top towel. And I asked him,
[1490.24 --> 1493.16]  Brendan, what is an elite engineer? Take a listen.
[1493.76 --> 1499.08]  An elite engineer for us is somebody who satisfies all the technical requirements, um, that you would
[1499.08 --> 1504.34]  need in a, in a great developer. If you're working at like, uh, like a Google or Facebook, but then at
[1504.34 --> 1510.22]  top towel, you have to add this extra layer on top of it to make sure that people are, uh, mature
[1510.22 --> 1514.50]  enough and professional enough to be totally self-directed. And so making sure that they
[1514.50 --> 1519.74]  take a tremendous amount of, uh, pride in their work and that they're accountable and very,
[1519.84 --> 1525.42]  very communicative because in remote freelancing, that's sometimes just as important as being
[1525.42 --> 1529.70]  technically competent. All right. If Brendan got you excited about being an elite engineer at top
[1529.70 --> 1537.68]  towel, head to top towel.com slash developers. That's T O P T A L.com slash developers to learn more
[1537.68 --> 1543.06]  and tell them the cheese load sent you. All right, Scott, we're back. Um,
[1544.56 --> 1547.12]  so note foundation, whose idea was the foundation?
[1549.76 --> 1559.76]  Um, so the, I started talking to the Linux foundation last summer. Um, uh, Jim Zemlin reached
[1559.76 --> 1565.92]  out to me and we sat down and started talking about what a foundation would look like. Um, I met with
[1565.92 --> 1570.70]  the IBM team last summer, met with some folks from PayPal last summer and you know, all of them
[1570.70 --> 1577.80]  started, uh, really advocating that we consider a foundation. Um, so I spent some time starting to
[1577.80 --> 1581.64]  work with, with Jim Zemlin to come up to speed with it, to see what it would look like, to understand
[1581.64 --> 1588.54]  the impact on the project. Um, and, uh, spent a lot of time working through the fall is probably last
[1588.54 --> 1595.08]  December where I felt comfortable enough with it that I, uh, recommended it to, uh, to our board of
[1595.08 --> 1601.28]  directors, uh, and then started working with the advisory board on a, you know, path to go get that
[1601.28 --> 1608.08]  set up. Um, but we looked at a couple of different options. It wasn't always a foundation. Um, you know,
[1608.08 --> 1612.52]  foundation can be good. It can be bad as well. Uh, I wanted to make sure I personally had some
[1612.52 --> 1618.98]  reservations that I had, that I had to get over. Um, to me, it was very important that we wind up
[1618.98 --> 1625.88]  in a place where it's not a pay to play model, where there's, uh, where the technical direction
[1625.88 --> 1632.52]  of the project is truly driven by the people who are using the project and the people who are,
[1632.58 --> 1636.88]  uh, who are contributing to and developing to the project, developing, uh, you know, code on the
[1636.88 --> 1641.72]  project. So I want to make sure that it was that, that technical, that the project direction was being
[1641.72 --> 1647.74]  driven by the technical direction and the market direction, not by a vendor direction or people who
[1647.74 --> 1653.14]  are the sponsors. So I want to make sure that we could set a model up like that. Um, you know, some,
[1653.32 --> 1658.22]  some foundations, uh, have managed to adhere well to that and others haven't. So I had to make sure
[1658.22 --> 1664.34]  that there was a way for us to do that. Um, I also want to make sure that there's a model in place
[1664.34 --> 1670.32]  where we could make sure there was not only a strong technical independence, but we're, we're, we're,
[1670.32 --> 1677.90]  we're, we're really having, um, a function that is very close to the market and what the users want
[1677.90 --> 1683.82]  to have. So not only technical, you know, input, but market input to this, uh, you know, and most
[1683.82 --> 1689.36]  organized, most soft organizations, you have product managers who sort of play that role. Um, you know,
[1689.36 --> 1694.10]  they understand, you know, the use cases and the pain points and the market opportunities and, and they,
[1694.20 --> 1698.42]  they provide a lot of input and guidance around where the product should go. Uh, they work very closely
[1698.42 --> 1702.42]  with the engineering team who's obviously bring technical, you know, innovation to, to play.
[1702.58 --> 1707.42]  And that tends to be a good partnership. Um, so I want to make sure that we have, uh, though,
[1707.62 --> 1713.30]  those functions, uh, in place in the foundation that, that I think that's the only way to drive
[1713.30 --> 1721.18]  a healthy project. Uh, if you look at, um, uh, you look at OpenStack, uh, OpenStack has been very
[1721.18 --> 1727.00]  successful getting vendor support. Uh, there's a lot of contributions around it. Uh, but they have
[1727.00 --> 1733.80]  really struggled with, uh, having a, uh, a vision and a product management vision around it. I think
[1733.80 --> 1738.64]  there've been some blogs, uh, Randy Bias has put some blogs out around that. Uh, you know,
[1738.64 --> 1744.88]  they've really struggled with, with how to make sure they get that singular vision, uh, to drive the
[1744.88 --> 1749.84]  project forward. Uh, so yeah, that, that's very important to me and I'm sure, you know, everybody
[1749.84 --> 1756.94]  else who's, uh, who's really engaged with the project. So it sounds like Joanne's efforts will,
[1757.04 --> 1764.08]  will be to continue to be, uh, uh, at the forefront of what Node is. Is it at all a desire to step back
[1764.08 --> 1770.72]  as the core steward or the, you know, the stewardship of Node? Is that part of any plan as you move into a
[1770.72 --> 1775.12]  foundation effort? Is it something where, you know, Joanne will still play a part and still play a role,
[1775.12 --> 1780.16]  of course, but it, you're sort of like handing it off to the foundation and, and playing a part in
[1780.16 --> 1784.70]  the foundation rather than, uh, being the core steward as you have been over these last years,
[1784.70 --> 1788.70]  because Joanne's name has pretty much been synonymous with Node and it's because of the
[1788.70 --> 1793.92]  stewardship that you've done. Is that a plan to step back from that? So this, yeah, no, great question.
[1794.00 --> 1800.94]  So, so we love Node and when a project is early, like Node has been over the last few years, uh,
[1800.94 --> 1808.88]  it's, it's important to have maybe a tighter reign around, uh, how, around the project direction
[1808.88 --> 1815.62]  and, uh, where it's going and how it's going. Um, it's been very important for us as well to make
[1815.62 --> 1822.98]  sure that we have stable releases that, because we're, we're, we're a little different than most
[1822.98 --> 1829.14]  open source companies, uh, with respect to Node, we're not the Node company to say where we're,
[1829.14 --> 1834.14]  we don't have, we don't sell an enterprise version of Node. We don't build a bunch of tooling around
[1834.14 --> 1838.38]  Node that we go sell around Node. You know, we don't have the typical business model that other
[1838.38 --> 1843.96]  open source companies do who do tend to, you know, be the stewards of projects. Um, we do provide,
[1843.96 --> 1849.86]  uh, support services to, to companies who also have adopted Node, but we're not in the business of
[1849.86 --> 1855.02]  building this tooling or selling enterprise, enterprise, you know, versions of, of, of Node.
[1855.02 --> 1862.50]  So we have a little bit of a different perspective or a different role. So Node is important to us,
[1862.50 --> 1867.48]  uh, and will continue to be important to us because our products are based on Node, our public cloud,
[1867.86 --> 1874.94]  our object store, that's all, that's all based on Node. So it has to be highly performant. It has to be
[1874.94 --> 1879.90]  production grade. It has to be low latency. It has to be highly scalable. So that's, that's very
[1879.90 --> 1884.76]  important to us. And in the early days of the project, you know, with those constraints or
[1884.76 --> 1889.36]  those objectives, it was very important for us to maintain sort of tighter control around that.
[1889.36 --> 1897.42]  So we could ensure that we could run our business on it. Um, but really that was it. And now I think
[1897.42 --> 1903.82]  with the success of Node, it has transcended, you know, any individual, certainly when Ryan moved off
[1903.82 --> 1909.10]  the project that was proven, uh, it's transcended any individual and it's clearly transcended, you
[1909.10 --> 1914.24]  know, any individual organization or company as well. Um, and so it's, it's really time for the
[1914.24 --> 1919.42]  next stage of maturity around the project. And, you know, one of the things that was very obvious to
[1919.42 --> 1927.78]  me is there is, uh, a very energized community around Node. Uh, the, the customers, the users of Node,
[1927.86 --> 1933.60]  the developers, the contributors around Node, the vendors of Node are very, they're very engaged. They feel
[1933.60 --> 1938.74]  a very strong sense of ownership and they want to contribute. They want to be engaged. They want
[1938.74 --> 1944.90]  to have a say. They want to contribute value back to the project. And so I think, you know, this is
[1944.90 --> 1951.62]  a really good time in the project's life cycle to now, uh, help the project move to another stage of
[1951.62 --> 1958.10]  maturity. Um, and let's, let's bring in, let's sort of loosen the reins, if you will, and let the project
[1958.10 --> 1963.40]  be really driven by the community and open it up to collaboration and contribution by a much broader
[1963.40 --> 1970.08]  set of people in the, in the industry. Um, let, let's, let's, let's make it more community driven
[1970.08 --> 1976.62]  where we can have a good balance of, of, uh, you know, great innovation and, uh, high quality,
[1976.80 --> 1982.08]  you know, stable releases. And it's, uh, the foundation is the best way to go, to go do that.
[1982.62 --> 1986.48]  So the state of the foundation is it's in place now or is still in formation?
[1986.48 --> 1992.14]  So the, the great question. So the foundation is in the formation stages. We announced at
[1992.14 --> 1997.78]  Node Summit that we were forming a foundation and that we're going to work with the Linux
[1997.78 --> 2003.60]  foundation to help us go do that. Um, you can either roll your own foundation, you can join
[2003.60 --> 2008.54]  an existing one, or, you know, in this case of the Linux foundation, they have a foundation as a
[2008.54 --> 2014.04]  service where, you know, they, they know how to run these community driven projects and they know
[2014.04 --> 2018.36]  how to work with the community. They know how to, to, to run the infrastructure and provide
[2018.36 --> 2023.34]  your financial management and legal advice and your organizational structures and documents. So,
[2023.60 --> 2027.70]  so they have a lot of expertise and a lot of, you know, great track record with what they've done
[2027.70 --> 2033.38]  with all their projects. So, uh, we're working with them. And so a group of organizations stood up
[2033.38 --> 2038.20]  and said, yeah, let, let's go move this to a foundation. We're in support of it. Let's go do it.
[2038.20 --> 2045.06]  So, uh, that was in probably February when it node summit. And what we announced was it would take
[2045.06 --> 2052.12]  several months to go stand the foundation up. And in terms of, uh, the legal work,
[2052.22 --> 2058.40]  getting the bylaws together, getting the membership agreements together, uh, getting the IP policies in
[2058.40 --> 2064.74]  place, uh, and then set up the organizational structure. So you have, you have, um, a board of
[2064.74 --> 2069.00]  directors that works on the business and legal issues. And then you have a technical steering
[2069.00 --> 2074.74]  committee, uh, that drives the technical direction of the project. And we've spent a lot of time,
[2074.74 --> 2080.38]  uh, and I can, I can send you the links if you want to post them on your site to the GitHub
[2080.38 --> 2085.80]  discussions on GitHub, on GitHub, where we have, uh, you know, iterated through the dev policies,
[2085.80 --> 2092.06]  uh, the governance model. And it's, it's, uh, it's not just us, but it's members from the node
[2092.06 --> 2096.82]  community, members from the IO community, people who sit in both communities, uh, vendors, your
[2096.82 --> 2102.52]  customers, your users, uh, who've, who've contributed a lot of thinking to this. So it's sort of formalizing
[2102.52 --> 2107.06]  that documenting it, you know, getting input and directions from the community on, on how that's
[2107.06 --> 2114.24]  going to be run. And so we've been moving down that path. And so all those documents are up for
[2114.24 --> 2122.42]  public comment, um, and feedback. And the, the goal would be to officially publicly announce the,
[2122.58 --> 2128.16]  the, that the foundation is up and running probably the last week of May or first week of June, I think
[2128.16 --> 2133.74]  is the current timeframe. And then we'll hold the first board meeting by the end of June and get
[2133.74 --> 2138.86]  everything sort of ratified and, uh, the, the different positions voted on and in place. You have
[2138.86 --> 2144.50]  to go through a period to, to get that, uh, sort of stood up as well. So, so that's the status. And
[2144.50 --> 2150.94]  there's been a lot of work by a lot of people, uh, to get, uh, to get all those threads and all those
[2150.94 --> 2156.30]  tracks pulled together. You mentioned IO and that mention there, and we've talked about it a bit
[2156.30 --> 2162.82]  during the call so far, but I'm curious to know what, what your thoughts are on not just the fork
[2162.82 --> 2168.82]  itself, but the, both the good, um, and what you might think the bad might be that came to
[2168.86 --> 2173.64]  the good that came from, um, essentially fraction the community, forking it. There's a lot of good
[2173.64 --> 2177.58]  that came from it. I'm curious to know what you think the good has been and what potentially you
[2177.58 --> 2183.64]  think, uh, the bad has been from this IO fork and where, how it's sort of forced node to change.
[2184.36 --> 2191.26]  Uh, so I, I, yeah, I think there's, there's both as you say. So the good is, um, that, that,
[2191.26 --> 2198.48]  that group of people have done a really phenomenal job of iterating on and running, um, a model,
[2198.48 --> 2205.32]  a governance model and a contribution model that, um, has been pretty innovative and allowed for
[2205.32 --> 2211.08]  a lot of new innovation, a lot of new contributions, a lot of new collaborators to come into the project.
[2211.08 --> 2216.20]  So they've done a phenomenal job of engaging the community and, and driving some pretty
[2216.20 --> 2222.62]  interesting innovation. Uh, and you know, I, I will learn from that. And I think as you, if you dive
[2222.62 --> 2226.72]  into the dev policies and the governance model that we're going to, you, we're going to use in the
[2226.72 --> 2232.86]  foundation, you know, we're, we're taking lessons directly from that. So, um, we, we want to bring
[2232.86 --> 2238.84]  that community engagement and, uh, the community, uh, you know, interaction and leadership positions,
[2238.84 --> 2246.20]  uh, into the project and the foundation. Uh, so, uh, that there's a lot of great stuff done there.
[2246.56 --> 2252.98]  Um, on the bad side, I think, you know, what, what I've, the, the feedback that I get from,
[2252.98 --> 2257.98]  um, you know, a lot of, uh, organizations and I've actually got a blog coming out on this
[2257.98 --> 2263.42]  over the next few days. Um, if you look at the, the enterprise market and a lot of people,
[2263.42 --> 2267.82]  a lot of different market segments use node, you see it in IOT, you see it in the robot space. Uh,
[2268.18 --> 2274.42]  uh, you, you see it in a small organization, you see it in large enterprises. Um, and the,
[2274.56 --> 2282.00]  the enterprise users have been pretty vocal and that they want a foundation because they want to
[2282.00 --> 2290.00]  de-risk the project. Um, and if you're, I was just talking to one of the, a big node user yesterday,
[2290.00 --> 2294.88]  I said, you know, one of the issues here is if, if you personally are betting your career
[2294.88 --> 2299.10]  on a technology that you're bringing into your organization to roll out a whole bunch of
[2299.10 --> 2306.12]  applications on and potentially be the next platform for your new applications, you want to
[2306.12 --> 2313.22]  de-risk that you want to make sure that it, it is D it's de-risked from, uh, an individual, the,
[2313.22 --> 2320.14]  the, the, the imperatives or, uh, goals or, uh, financial model of any individual company.
[2320.60 --> 2325.82]  So they don't want to be tied specifically to joint. Uh, they also want, they also want to make
[2325.82 --> 2331.02]  sure that, that there's, you know, no risk around the project itself. They want to make sure that there's,
[2331.02 --> 2335.88]  um, you know, that any strife is gone. They don't like to see infighting. They don't see bickering.
[2336.00 --> 2339.78]  They don't like to see dilution of technical resources. This whole fork has been a big boon
[2339.78 --> 2344.96]  in it then, huh? I mean, this fork of Iowa has been basically like, Oh, we got to stop this,
[2344.96 --> 2349.48]  like from all sorts of angles. It's been, it's been frustrating, you know, and they were very,
[2349.48 --> 2354.68]  the users were very vocal before the fork and, you know, through the advisory board meeting saying,
[2354.68 --> 2362.22]  yeah, don't fork, please. We just make, find a way to sort of unite the community and get the
[2362.22 --> 2367.40]  community more engaged, but a fork would be terrible. And, um, so there's been a lot of,
[2367.40 --> 2372.30]  a lot of, so I'd say that's, that's the fallout is that it, it, it, it, it, it injects,
[2372.30 --> 2379.00]  injects a lot of risk into the project. And if you are in the enterprise segment of the node community,
[2379.00 --> 2385.66]  uh, you know, that that's problematic. And, um, what it does from the project's perspective is
[2385.66 --> 2392.62]  it makes the project itself risky. And that opens the door for other projects to come in and take
[2392.62 --> 2398.22]  its place. You know, who knows what the next cool, you know, server side JavaScript platform is that
[2398.22 --> 2402.84]  somebody is working on right now that, you know, could come to, come to bear. It's like when you saw,
[2402.84 --> 2407.50]  you know, Oracle, you know, Sun buying MySQL, then Oracle buying them. And that created a lot of,
[2407.50 --> 2412.40]  you know, angst in the community. And then, uh, you had Mario DB fork and go out, you know,
[2412.40 --> 2418.30]  that was supposed to be, you know, the savior, but in reality, it just created a lot of angst in
[2418.30 --> 2424.90]  the market. And then Postgres came out. So, uh, you know, I think, um, you know, we need as, as
[2424.90 --> 2431.68]  looking broadly across all the communities wanted to know, you know, we need to be very, uh, cognitive,
[2431.68 --> 2438.24]  cognizant of that and, uh, find a way to, uh, work together and have, you know, an energized
[2438.24 --> 2443.42]  project that is de-risked for, you know, if, if we care about the enterprise market, which I think
[2443.42 --> 2447.96]  most people do, then we've got to find a way to de-risk it for them and, uh, find a way to, to,
[2447.96 --> 2453.74]  to innovate and, uh, deliver, you know, quality, stable production code and engage the community
[2453.74 --> 2459.54]  so that they're really driving the project. And that's, that, that's what my, my, my hope is.
[2459.54 --> 2465.34]  And my goal is in the foundation. So answering the, the good side was that there's a lot of
[2465.34 --> 2470.72]  innovation, a lot of progress, a lot of adoption, a lot of, um, bringing the community in and, and
[2470.72 --> 2475.50]  sort of bolstering the, the progress of the, of the project and organizing their tentative
[2475.50 --> 2480.74]  committees and, and different things to sort of bring the community better in stewardship,
[2481.00 --> 2485.42]  to use that word, because that's where doing has sort of been sitting for it. And that's why the
[2485.42 --> 2492.14]  fork happened was sort of to take the stewardship back from, um, from you to sort of give it back
[2492.14 --> 2497.30]  to the community and better drive it with new releases and things. And then the bad, um, has
[2497.30 --> 2502.92]  been this confusion that's put in the marketplace, the, of node, the, the node marketplace. And I guess
[2502.92 --> 2507.30]  the fear that some companies might have, would you, is that fair to sort of summarize what you just
[2507.30 --> 2507.66]  said there?
[2507.66 --> 2508.98]  Yeah, sure.
[2509.62 --> 2515.06]  So just yesterday, um, kind of coming into some currents, we talked about node foundation,
[2515.06 --> 2520.16]  where that's at. It's, it's still in progress. It's not quite there yet. There's probably in the
[2520.16 --> 2525.44]  final stages of it, considering the, um, the, the governance working groups, development and
[2525.44 --> 2531.32]  convergence policies, uh, being ready now. Um, just yesterday, Michael Rogers, who was recently on the
[2531.32 --> 2537.68]  show episode one 39. Um, and this was back in January 30th, 30th. And that show was titled
[2537.68 --> 2547.06]  the rise of IOJS. Just, uh, just, uh, put a, put a note on there. Um, so he said IO is, you know,
[2547.06 --> 2552.00]  in a recent article, he just said, I was, uh, is growing up and it needs a foundation. He didn't
[2552.00 --> 2556.88]  say it needs node foundation. So I'm curious to, to get some thoughts on your side about that,
[2556.88 --> 2560.52]  but some other things he mentioned in this article that he posted a medium, we'll put in the show
[2560.52 --> 2567.48]  notes. Uh, are you familiar with this article by any chance, Scott? Uh, I, I saw an article about
[2567.48 --> 2574.12]  a new release V2, but I didn't see any comments about the foundation. Yeah. This one here is
[2574.12 --> 2579.10]  specifically called growing up and it's subtitled IOJS needs a foundation. And he's laying out a
[2579.10 --> 2582.90]  couple of things. I think he's talking specifically to the IO community, not so much that it doesn't
[2582.90 --> 2587.08]  include the node community because they sort of both sort of converge at some point. But one thing he
[2587.08 --> 2591.82]  said is that it's owned by the community, uh, but that requires a legal entity and it's hard to do
[2591.82 --> 2595.26]  things without the formation of a foundation, which I know you're aware of cause you've been
[2595.26 --> 2600.42]  talking about all this, but, uh, and then something else he said was we did, we need to end the split
[2600.42 --> 2607.36]  and confusion in the community who are still torn between IOJS and node JS. So you see this,
[2607.44 --> 2612.40]  this change there and you got the, the node foundation sort of in place, the governance model,
[2612.40 --> 2616.90]  uh, that the working groups, the development convergence policies are all in place. Uh,
[2616.90 --> 2622.30]  is there an open invite to IO and is it your desire? Is it joyous desire? Is it node foundations
[2622.30 --> 2627.04]  desire to have IO? Obviously they've been a part of it, but is it, is it their desire to have them
[2627.04 --> 2633.82]  join? Uh, yeah, absolutely. Um, you know, we, we do want to have one unified, uh, energized community.
[2633.82 --> 2643.62]  Um, when we first started, actually after the fork first happened, I was, um, I was at a node day
[2643.62 --> 2651.18]  event, uh, in the Valley here and, uh, Disha from node source and I were both on this panel. And, uh,
[2651.18 --> 2657.76]  that was one of the questions was, you know, will, will this fork heal, you know, do both, you know,
[2657.76 --> 2662.58]  groups want to come back together? Is there a path? And I think, you know, that was probably the first
[2662.58 --> 2667.52]  time that question was asked. And, uh, I think, you know, we both, you know, I think we both at that
[2667.52 --> 2673.50]  time believed that the right path is to have, uh, a single community working around node, uh, for all
[2673.50 --> 2681.42]  the reasons I just articulated a few minutes ago. Um, and so we've been working very closely with a lot
[2681.42 --> 2688.82]  of people from the IO community on this foundation and making sure that, uh, they have, uh, a lot of
[2688.82 --> 2697.18]  input into it around the dev policies, the governance models, uh, the, the, the org structure. So, um,
[2697.40 --> 2702.46]  yeah, I think, uh, I think we, we, the foundation will be the right vehicle. And, and I think it would
[2702.46 --> 2705.74]  make a lot of sense to, uh, to, to unite the community and the foundation.
[2707.10 --> 2711.28]  And something else I think that should be mentioned too, is just that the, the policies,
[2711.28 --> 2715.60]  and this is just pulling some, some thoughts right from Michael's, uh, article. He said,
[2715.60 --> 2718.80]  the policies of the foundation, meaning node foundations, he's talking about that in the
[2718.80 --> 2725.10]  article are designed to preserve the progress we've made in IOJS. So that means that, um,
[2725.10 --> 2730.64]  and he also goes on to say that, uh, they're pretty much taken verbatim to back up what IOJS
[2730.64 --> 2736.58]  has sort of built and some things you've credited them for earlier, um, to, to sort of, you know,
[2737.34 --> 2743.56]  provide that progress that IOJS is already doing. It's so they seem like they want to as well,
[2743.56 --> 2749.62]  uh, to, to sort of, you know, reconcile and finally become back to, to the, to the mothership,
[2749.66 --> 2755.74]  so to speak, you know? So what is that process? Like, how does that, how does that change things
[2755.74 --> 2759.32]  for you guys? Like, when can we expect this to happen? Do you expect this to happen?
[2760.32 --> 2767.50]  Um, I do expect it to happen. Um, but what's, you know, what's going to happen or how, maybe,
[2767.62 --> 2773.34]  maybe it's how, how the next steps are going to unfold is, you know, Michael's comments about
[2773.34 --> 2779.56]  the, the documentation and the policies, uh, around the foundation coming from IO is, as I said,
[2779.60 --> 2784.26]  they've done a great job of engaging the community. Uh, they've done it and expanded the role,
[2784.40 --> 2788.00]  the number of, uh, collaborators and the role of collaborators and contributors,
[2788.00 --> 2793.32]  and they've done a great job around innovating in some, in some new areas. So I love that stuff.
[2793.40 --> 2796.62]  That's, that's great. And I want to, I want to make sure we're, you know, we're bringing that into
[2796.62 --> 2803.58]  the foundation. And when we first got together to set up, uh, you know, and, and start to define
[2803.58 --> 2809.26]  what, what the starting point would be for those policies and, and governance models in the
[2809.26 --> 2815.32]  foundation, we, we, Michael just submitted, uh, everything that he had been working on,
[2815.32 --> 2820.80]  he and the team and the community and IO has been working on and iterating on. And that was the
[2820.80 --> 2825.96]  starting point. Right. Yeah. So, uh, it's a, I think, I think that trajectory, I'm sure that
[2825.96 --> 2830.72]  trajectory will continue. Uh, so that was the starting point. And then, uh, a lot of people,
[2830.72 --> 2834.80]  you know, joined in to iterate and refine and, you know, lessons learned that they had and some
[2834.80 --> 2838.32]  other ideas that other people brought to the table. So that was sort of the, the, the starting point.
[2839.00 --> 2844.94]  Um, so in the node advisory board, we meet every other week and we have a big, we have an open
[2844.94 --> 2851.70]  public session there. Uh, you know, Mike, Michael has been, uh, on, you know, he's been attending the
[2851.70 --> 2855.88]  last few advisory board meetings and we've been talking a lot about, you know, updates on the
[2855.88 --> 2862.84]  foundation, the progress and, um, and then, you know, what, what, uh, what the position is of IO
[2862.84 --> 2867.30]  and the IO, you know, community, what they want to do. And I, I, I believe, and certainly Mike will be a
[2867.30 --> 2873.94]  better source and, uh, but I believe that, that, that there have been a lot of discussions around this,
[2873.94 --> 2881.00]  uh, on in, in, in, in the IO community around whether or not they should, uh, come and join
[2881.00 --> 2885.36]  the foundation and what that would look like. And there's been some good, healthy discussions on
[2885.36 --> 2890.16]  that. Uh, and I believe that there's going to be. Are there open discussions on that right now?
[2890.16 --> 2894.80]  Like, are there actual open discussions between what is node foundation? Cause they're obviously
[2894.80 --> 2900.02]  being a part of putting it together, uh, in terms of planning and what they've been doing and all,
[2900.04 --> 2903.44]  but is there an open conversation about the reconciliation process? Yes.
[2903.94 --> 2910.32]  Yeah. Yeah. Uh, you know, a lot, a lot of questions, people not sure what it means and,
[2910.32 --> 2914.02]  uh, you're having a lot of questions and really trying to get that, that answered. So,
[2914.02 --> 2918.94]  yeah, that's all, uh, I think there's a whole, you know, a very long thread that
[2918.94 --> 2926.40]  probably Rod Vag started a while ago. Uh, but it's up on GitHub. Um, and so good, good conversations.
[2926.40 --> 2932.08]  And I believe that, you know, there was, that Michael made a motion to, uh, sort of formally
[2932.08 --> 2941.18]  discuss it in their TSC and then move towards a vote on whether, you know, the TSC wanted to come,
[2941.30 --> 2948.40]  wanted to come join the foundation. Uh, and I'm, I'm not sure how, you know, the, the rest of the
[2948.40 --> 2953.98]  working groups are organized or, uh, you know, what, you know, how that, that broader, you know,
[2953.98 --> 2958.14]  decision would be or whether, you know, I, I, I'm not familiar with all the details of that,
[2958.14 --> 2963.70]  but it's my, my understanding is it's heading toward a vote in their technical steering committee.
[2965.02 --> 2968.70]  So since we're also being current with what's going on, I guess, as of yesterday with that
[2968.70 --> 2975.58]  article I mentioned from Michael, titled growing up, um, TJ Fontaine, uh, some news came out today,
[2975.58 --> 2981.48]  just a couple hours before this call, actually, uh, that, that, uh, TJ Fontaine is stepping away from,
[2981.48 --> 2987.38]  from node. Uh, he'd given a lot of congratulations to those who've been involved and sort of painted a
[2987.38 --> 2993.04]  picture for what the next chapter of node is. He talked a lot about, um, you know, how it's a good
[2993.04 --> 2996.34]  place. It's a good time for node. And we've mentioned that earlier in the call too, with the
[2996.34 --> 3001.08]  foundation. And, um, even though there's the fork of IO, there's a lot of progress happening, a lot
[3001.08 --> 3007.48]  of good direction and that this is a really good time, um, for node. What, what do you think about
[3007.48 --> 3011.82]  TJ stepping away? Were you surprised by this? What else can you, can you add to that? Um, yeah,
[3011.88 --> 3017.08]  you know, TJ will be missed. TJ's, TJ has contributed a lot to the project over the last year,
[3017.08 --> 3024.74]  year, probably year and a half. Um, uh, so his, he's technically very strong. Um, you talked about
[3024.74 --> 3032.42]  the burnout factor, uh, you know, earlier about, uh, project leads and, uh, you certainly, you, you
[3032.42 --> 3039.88]  speculated around that with Ryan, uh, you, uh, when, when Ryan moved off the project, then Isaac moved
[3039.88 --> 3045.56]  on, he was on the project for about a year and a half or so. And so, and then, you know, TJ following him.
[3045.56 --> 3053.96]  So that, that position is a pretty challenging position. Um, and its role is changing. Uh, so as we
[3053.96 --> 3063.18]  move into the foundation, there is no BD. The, the technical steering committee is, uh, is, is a group of,
[3063.18 --> 3069.64]  uh, of developers and contributors and collaborators who, uh, will be driving the technical direction,
[3069.64 --> 3076.78]  uh, based on a consensus, uh, consensus model. So, um, you know, there's, there's no longer,
[3076.78 --> 3083.46]  you know, that, that role going forward. So, um, we'll definitely miss TJ's technical contributions.
[3083.98 --> 3089.80]  Uh, but you know, the project's changing and the project is, uh, maturing to the next stage of its
[3089.80 --> 3095.40]  growth. And if they're not that there ever is a good time for anybody to, to leave the project,
[3095.40 --> 3099.78]  but if there is one that's better than others, this is actually a, you know, pretty good time
[3099.78 --> 3106.96]  for TJ to move on. And, um, uh, as we're really, you know, changing the way that the, the whole
[3106.96 --> 3108.64]  project runs and move it to a foundation.
[3109.64 --> 3113.72]  And I guess really the, the future of Node.js is really pinning around,
[3113.72 --> 3121.84]  I would think the, the convergence, the reconciliation, uh, of these two, the, the fork and,
[3121.84 --> 3127.56]  and, you know, mainline, so to speak, um, although there's been some progress on the fork, uh, ahead
[3127.56 --> 3133.04]  of the mainline, which would be considered Node. Um, what do you think, what do you think Node would
[3133.04 --> 3137.96]  gain from the reconciliation process? What do you think it would gain from IO and, and Node
[3137.96 --> 3145.50]  reconciling and how could that, um, I guess, how could that reinstate some trust and reinstate
[3145.50 --> 3150.84]  some security back into the marketplace of, of what is Node? Yeah, great question. So I, I,
[3150.90 --> 3155.78]  I think it would be a big, a big win for everybody, uh, you know, from the macro level, certainly you
[3155.78 --> 3162.62]  want to have a healthy project. Uh, so you want to have a very, uh, satisfied and successful,
[3162.62 --> 3169.70]  your user base. You want to have, uh, a vibrant, uh, community eco of ecosystem partners who are
[3169.70 --> 3174.02]  building, you know, tools and services that, that surround the project. Then you want to have an
[3174.02 --> 3178.90]  energized, you know, large energized group of, uh, developers and contributors who are, who are
[3178.90 --> 3186.44]  writing the code and contributing to the project. Um, so from the user perspective, the users want to
[3186.44 --> 3191.68]  have, uh, they want to de-risk the project. They want to have a single project. They want to get the
[3191.68 --> 3197.04]  confusion out of the way. Uh, they want to have a single community working together, sort of pulling
[3197.04 --> 3203.12]  the oars in the same direction. Um, the vendors, uh, certainly want to have stability. It's much
[3203.12 --> 3208.54]  easier for them to support, you know, a single project than multiple and not have to be in a
[3208.54 --> 3215.20]  position of, of, um, trying to explain and help position, you know, different forks in the, in the
[3215.20 --> 3220.86]  community to, to their customer base and, and accommodate those. And then from the contributor side,
[3220.86 --> 3228.20]  it would be a big, uh, a big win to have a single, you know, energized group of people, uh, working
[3228.20 --> 3234.00]  together to drive node in the, in the future for the future direction. So I, I, I think it's a big
[3234.00 --> 3240.06]  win, uh, all around to have a, a single combined project. You know, as I said to somebody, uh, when we,
[3240.22 --> 3244.82]  when this topic first came up around the fork last fall or fork potential forks, there's been
[3244.82 --> 3251.24]  discussions of forks for several years now. Um, I said, I'd, I'd rather have a slice of watermelon
[3251.24 --> 3257.58]  than a whole grape, right? Let's, if we can work together across all constituents in the community,
[3257.58 --> 3264.54]  then we can, we can really accelerate the adoption of node. We can drive it forward. We can innovate.
[3264.54 --> 3271.36]  We can go and we can serve multiple market segments. Um, we, we can do great things for the
[3271.36 --> 3276.12]  project and we're barely scratching the surface around a lot of the market segments where node
[3276.12 --> 3284.10]  has a lot of success today. So, uh, I, I think we can build a really big market and, uh, a real broad
[3284.10 --> 3290.90]  adoption across a lot of different segments. And, uh, that, that kind of success is, uh, will,
[3291.46 --> 3297.02]  we'll make, uh, it will be very gratifying for everybody. And that, that's really what I'm after.
[3297.02 --> 3302.24]  Let's take a break real quick. Uh, we'll come back for a couple more, uh, final thoughts as we
[3302.24 --> 3307.78]  taper off, but, uh, we'll take a quick break. We'll come right back. Digital ocean opened up a
[3307.78 --> 3314.10]  brand new European region in Frankfurt in Germany, FRA one. So when you're creating new droplets,
[3314.10 --> 3320.66]  if you need support for European locations, FRA one is now opened up to you. They announced the
[3320.66 --> 3325.84]  new German region about five months ago. And after about a month of build out, they're finally excited
[3325.84 --> 3331.78]  to open up FRA one. So you can use it today. And due to its placement on the German commercial
[3331.78 --> 3336.84]  internet exchange, which is the largest internet exchange point worldwide by peak traffic.
[3336.84 --> 3342.94]  This region also serves Germany's neighboring countries with unparalleled connectivity and
[3342.94 --> 3348.28]  speed. And like other European locations, this German region meets the safe harbor regulations
[3348.28 --> 3352.96]  needed for storing data. The story of the German startup community is tremendous and digital
[3352.96 --> 3358.16]  oceans as excited as they can be to be playing a part and launching this new region, uh, to support
[3358.16 --> 3364.20]  the innovation happening in Germany. So if you can try a server today in FRA one, use the code
[3364.20 --> 3371.46]  change log. When you sign up to get a $10 hosting credit again, go to digital ocean.com use change
[3371.46 --> 3379.52]  log. When you sign up and you'll get a $10 hosting credit. Enjoy. All right, Scott, we're, we're back.
[3379.52 --> 3387.78]  You talked a lot about the future of the past reconciliation, uh, putting some faith back into
[3387.78 --> 3393.82]  the community, both from those companies who would invest by building their applications on top of
[3393.82 --> 3401.94]  node. Um, the foundation, obviously, what does it take to run a foundation successfully? You said you
[3401.94 --> 3407.54]  talked to Linux foundation about putting this together, you know, aside of just organizing it,
[3407.54 --> 3411.80]  running it, like these things cost money. So how, and you said there's no pay to play model.
[3412.16 --> 3417.70]  How, how will node function as a foundation? Where does the money come from? How does that work out?
[3417.74 --> 3419.48]  And what part does joint play in that?
[3420.58 --> 3427.80]  Right. So, so the, there are two organizations, there's the board of directors, and then there's
[3427.80 --> 3433.42]  the, uh, the technical steering committee and the board of directors is responsible for the legal
[3433.42 --> 3437.96]  aspects, the financial aspects. Uh, so those are paid seats, right? Pardon me?
[3438.02 --> 3443.72]  Board of directors, board of directors are paid seats. Uh, not all of them are paid seats. So, uh,
[3443.72 --> 3449.06]  you, you, you, you can join the foundation. You can become a member of the foundation. Either you can be
[3449.06 --> 3456.34]  an individual community member who can join the foundation. Um, you can also join at various funding
[3456.34 --> 3463.26]  levels. So we have a platinum, silver, and gold level. Uh, if you're a platinum level member, then you,
[3463.50 --> 3468.24]  with your annual sponsorship of the foundation, you automatically get a seat on the board.
[3469.24 --> 3476.94]  Uh, with the silver members, the silver membership as a, as a group gets together and elects members,
[3477.10 --> 3484.54]  uh, board members from the silver membership. And one, you know, a third of the silver members will be,
[3484.54 --> 3489.70]  uh, elected on the board and the gold level. Uh, you know, the same thing, they get together and
[3489.70 --> 3494.62]  vote as a group and what they're a 10th of the gold members will have a seat in the board. Um,
[3494.62 --> 3498.84]  also on the board of directors will be a representative from the technical steering committee.
[3499.44 --> 3505.50]  Um, we're also, it just, we're just discussing now, um, love to get some feedback on it of,
[3505.50 --> 3511.72]  of having a, potentially having a seat in the board for, uh, a, a general community member. So,
[3511.72 --> 3517.12]  uh, you know, we want to make sure that we, we engage the community at this level too,
[3517.54 --> 3522.46]  um, might not be the most interesting things to talk about. Uh, and we're certainly not talking
[3522.46 --> 3527.64]  about the technology or, you know, latest releases or roadmap. So that might not be interesting to a
[3527.64 --> 3533.30]  lot of people, but it's more of, uh, you know, overall, uh, sort of business and financial legal
[3533.30 --> 3540.08]  management side of the foundation. So the funding comes in from people who join at various paid
[3540.08 --> 3545.00]  levels and you're based on what level you're in that, then you are either voted on your,
[3545.08 --> 3551.40]  you're voted onto the board of directors. Um, and then that funding is used to then fund the project.
[3551.74 --> 3557.04]  And, uh, that funding has a lot of value to the technical team, to the, to the project in the
[3557.04 --> 3563.98]  whole. So that's used to fund, uh, the website hosting it's used to fund, uh, technical, you know,
[3563.98 --> 3570.76]  uh, education, training, skill development. It's used to fund, um, paid work that needs to be done
[3570.76 --> 3577.70]  to build out, uh, even more rigorous test harnesses, uh, build out API testing and API management,
[3577.84 --> 3582.30]  additional platform testing, and all the, all the infrastructure that's required to go do that
[3582.30 --> 3588.68]  has to get paid for. Um, so that, that gets funded for that. Um, uh, that the, we'll also be
[3588.68 --> 3593.48]  organizing, you know, the, the trade shows. If you look around your Linux foundation, it's a trade show,
[3593.98 --> 3600.92]  um, you see, uh, other foundations like, uh, you know, uh, open stack and the cloud foundry and
[3600.92 --> 3606.42]  your other projects like that have, have their, their, their big, uh, you know, their big, uh,
[3606.42 --> 3612.66]  meetups as well. So we'll, we'll be doing those as well. So that that's, uh, we'll also fund,
[3612.66 --> 3621.18]  um, at least one full-time technical person, uh, to go, you sit independently on, on the technical
[3621.18 --> 3627.88]  team or, or full-time, you know, write, write code for the project. Um, often you find there's, um,
[3628.52 --> 3634.18]  work on the project that's being done. Uh, people come in and they, they, the, the contributors,
[3634.42 --> 3639.82]  collaborators have in mind something specific that they want to do. Uh, and they go build that and
[3639.82 --> 3644.72]  submit that as a pull request or go put that in the, in the project. Uh, there's, there's other work
[3644.72 --> 3649.36]  that, uh, you know, just needs to be done and needs to be funded that may not be sponsored by,
[3649.36 --> 3654.52]  you know, individual customers or users or members of the community. So, you know, we want to make
[3654.52 --> 3659.12]  sure that the, that the broader community by contributing to the foundation can then go fund,
[3659.12 --> 3664.68]  uh, some full-time developers, uh, to go build out, you know, additional work that needs to be done
[3664.68 --> 3670.92]  on the project as well. Well, great. I, uh, I'm certainly looking forward to, to the future of it. I,
[3671.00 --> 3677.24]  I'm looking forward to the day when IO and Node actually reconcile. I know that, uh, some of the ways you
[3677.24 --> 3682.44]  mentioned funding will be used. There is some actual, um, you know, pain points that Michael
[3682.44 --> 3688.14]  has mentioned either in articles or in passing. Um, you know, Michael Rogers being the person that's
[3688.14 --> 3693.12]  sort of helping lead most of what, uh, IO is doing, not so much the leader of it all, but he's been
[3693.12 --> 3698.20]  sort of the, the main spokesperson to sort of give an update back to the community and sort of helping
[3698.20 --> 3703.26]  lead things. So one thing he's mentioned, um, I think in that article actually, in growing up was
[3703.26 --> 3708.62]  the fact that they can't spend any money to, you know, send a developer to a conference and represent
[3708.62 --> 3714.38]  IO or, you know, do any advertising. And that's sort of things that requires an organization.
[3714.48 --> 3720.56]  And he's talked about how, um, IO needs a home and there's the neutral organization that can support
[3720.56 --> 3725.86]  it, uh, is the node foundation and how that can sort of play back. So I can see how obviously having
[3725.86 --> 3729.82]  money coming into it is going to pay people to be there, legal fees, things like that hosting.
[3729.82 --> 3734.00]  And then also just in general, uh, you know, marketing, you know, everybody needs marketing.
[3734.00 --> 3738.06]  I mean, there's, there's always some, some level of cost that come into play. And until you have
[3738.06 --> 3743.54]  an actual organization to, to fund these things, it's, you can't do it. Right. That's right.
[3743.60 --> 3748.70]  Marketing, community development, uh, training, trade shows, uh, technical meetups. You,
[3748.70 --> 3755.84]  you, you want to have, uh, even stickers, right? I mean, something simple like stickers you can't get.
[3755.84 --> 3762.12]  Yeah. Well, uh, Scott, I guess in closing, let's, let's taper off the call. I think we've definitely
[3762.12 --> 3768.58]  covered as much as I want to cover, but is there anybody, um, that you want to personally thank for
[3768.58 --> 3775.12]  the work done at IO, the work done at node, wherever in the foundation, things that are, uh, uh, taking
[3775.12 --> 3779.00]  place. Is there anyone you want to call out that we haven't mentioned today that definitely needs a pat
[3779.00 --> 3782.48]  on the back or some encouragement that they're doing a great job? Anybody want to highlight?
[3782.48 --> 3791.32]  Uh, boy, there's a long list. Um, I think that the folks who, uh, the team that is continuing to,
[3791.32 --> 3798.74]  to move node JS forward are doing a phenomenal job. Um, the, it's great to see, you know, the
[3798.74 --> 3803.32]  innovation around everything from technology to governance models over at IO. And there, there are
[3803.32 --> 3808.98]  a lot of people who've been involved there, uh, as we've been moving towards the foundation,
[3808.98 --> 3814.68]  has been very helpful to get, you know, the Linux foundation engaged. Uh, you know, IBM has been
[3814.68 --> 3821.68]  very helpful. Uh, Denise Cooper, who's over at PayPal has been helpful. She, she's, she spans,
[3821.68 --> 3827.36]  uh, you know, a lot of projects over a lot of times. So she's been, you know, a great source to help,
[3827.44 --> 3833.28]  uh, you know, to help bounce ideas off and provide perspective. You know, that's that of how other
[3833.28 --> 3839.04]  projects have, uh, have evolved over the years. So there's a long list of people, but, uh, I think
[3839.04 --> 3845.40]  the community is moving in the right direction. Um, and, uh, I'm excited to see, uh, how the next
[3845.40 --> 3847.56]  couple of years, uh, really grow for node.
[3848.68 --> 3853.98]  And so for those who want to sort of, I know you mentioned there's topics on GitHub, there's
[3853.98 --> 3859.42]  comments on GitHub, where is a central place we can send some people to, um, to sort of keep up
[3859.42 --> 3864.08]  to date with what's happening? Is it nodejs.com or, you know, where is it? .org, isn't it?
[3864.32 --> 3872.46]  So, yeah, so it's nodejs.org. Uh, there is, we're putting up another page on nodejs.org
[3872.46 --> 3878.84]  that should be coming up online. I saw, I've seen drafts of it coming together and that will be
[3878.84 --> 3884.84]  kind of a one-stop shop, a one-stop location for updates on the foundation. And there are links
[3884.84 --> 3892.20]  there from there to blogs, to the dev policies, to all the, the, um, governance models, to all
[3892.20 --> 3898.22]  the foundation documents we've been iterating on. Um, so I would point people to that and
[3898.22 --> 3905.30]  that will be right on the nodejs.org, uh, website. Uh, there's also a website called, uh, node,
[3905.42 --> 3913.88]  uh, node advisory board, um, that, uh, Chris Williams, uh, put together and that has all the updates
[3913.88 --> 3918.66]  on the advisory board. It has, uh, the, the schedule for upcoming meetings and how to join
[3918.66 --> 3924.74]  in and how to engage, uh, the Slack channel. It has, uh, a compilation of all of the notes,
[3924.74 --> 3929.88]  uh, from all of the, the prior note advisory board meetings. And there's, there's a wealth
[3929.88 --> 3935.78]  of information there. Um, and then as I said, you know, the ongoing conversations, uh, you know,
[3935.78 --> 3941.62]  so really I, I, I, I invite everybody to come in and, you know, view and participate and express
[3941.62 --> 3947.00]  your opinion and, you know, be heard and, and then engage and act, uh, on, on the future.
[3947.82 --> 3951.44]  Well, all right, Scott. Well, thank you so much for taking the time to talk with me through this.
[3951.52 --> 3956.46]  I know that, uh, the last several years, um, have been a rollercoaster, especially this last six
[3956.46 --> 3961.38]  months, uh, with node. And we've been closely watching things, uh, here at the change log to,
[3961.48 --> 3966.84]  to keep up with what's going on there. Uh, certainly looking forward to the future. Um, yeah,
[3966.88 --> 3969.96]  thanks for coming on the show. And I guess now's a good time to say goodbye. So let's say goodbye.
[3969.96 --> 3973.86]  Great. All right. Thanks a lot for having me on the show. No problem, Scott. Thank you.
[3991.30 --> 3997.26]  All right. As promised, I got Scott back on the line. You know, I was kind of bummed because we
[3997.26 --> 4004.06]  did the show last Friday. So the record date for the show was May 8th and the planned release date
[4004.06 --> 4009.72]  was May 15th. We usually have a week to week schedule for the show. And I was kind of bummed
[4009.72 --> 4015.06]  when yesterday, you know, when yesterday occurred. So May 13th, yesterday, we're recording this right
[4015.06 --> 4021.34]  now on May 14th. Um, I was kind of bummed, happy, you know, for the news, but I was like, man, I,
[4021.34 --> 4027.44]  we speculated so much in that conversation with Scott that I was like, we may not be able to
[4027.44 --> 4032.92]  release that episode. It may just be obsolete or stale, but having edited it and having listened
[4032.92 --> 4038.72]  to it, it's a great show. Uh, a lot of details in there shared about joint and node and notes,
[4038.72 --> 4046.24]  history and IO and IO's history and this convergence. That's speculative. Uh, and now as of yesterday is,
[4046.24 --> 4053.36]  is going to happen. So IO has agreed and in their TC, they've agreed to join node foundation. And so
[4053.36 --> 4059.08]  take a listen. This is me and Scott diving deep into that news from yesterday. And that's, it's just
[4059.08 --> 4066.36]  great. So take a listen. So Scott, we're back. Uh, those who are listening to us right now, just
[4066.36 --> 4074.20]  listen to roughly an hour of me and you talking about joint IO node, the history, and a lot of
[4074.20 --> 4080.60]  speculation about some recent news, whether IO would converge with, uh, with node JS and ultimately
[4080.60 --> 4083.76]  joined node foundation. So what do you think about the news we just got yesterday?
[4085.12 --> 4090.70]  Well, I think it's great news. Um, you know, the, we've spent a lot of time working on the foundation
[4090.70 --> 4097.44]  and, uh, I think the foundation has been the vehicle and probably the best, maybe the only vehicle
[4097.44 --> 4104.58]  for providing the neutrality and providing, you know, the open governance policies and sort of a neutral
[4104.58 --> 4111.38]  ground to get the communities working together again. Um, I think one of the things I, I said earlier
[4111.38 --> 4118.54]  is I've been very focused on doing the right thing for node. And, uh, even if that means that your joint
[4118.54 --> 4124.44]  as a company has to compromise on some things around, uh, you know, how the project was run, um,
[4124.44 --> 4130.06]  it's a small compromise that we have to make in order to, you know, to benefit the greater community
[4130.06 --> 4135.52]  and the project in the whole, you know, the project is, is really transcended any one company and any
[4135.52 --> 4142.96]  one individual. And, um, it's a very, uh, energized, very passionate, uh, community out there. And it,
[4142.96 --> 4147.92]  it split into two. And, uh, you know, one of the reasons why I wanted to get the foundation together
[4147.92 --> 4155.58]  was to establish a vehicle to, uh, give, uh, probably the best option and the best path to,
[4155.70 --> 4164.84]  to having a single community, uh, working together on a single project. And, um, and I think the vote
[4164.84 --> 4169.74]  yesterday from the IO community showed that they, you know, they, they see, uh, sort of similar,
[4169.74 --> 4176.56]  similar perspective. Um, you know, Michael and, uh, Bert and, you know, the rest of the, the,
[4176.56 --> 4181.92]  the folks who are really helping to work on the foundation and then help evangelize that,
[4181.92 --> 4188.06]  uh, and explain the value and the benefits to the IO community. They did a great job, uh,
[4188.06 --> 4194.14]  communicating with that group and, uh, you know, a lot, lots of notes and lots of issues,
[4194.24 --> 4198.96]  lots of conversations on GitHub going through, you know, a lot of details to help explain that
[4198.96 --> 4204.70]  to everybody. And I think they did a great job of that. And now, so, uh, you know, or I'd say an early
[4204.70 --> 4209.08]  win for the foundation and validating that the foundation is the right thing to go do.
[4209.56 --> 4215.28]  And, uh, so I'm, I, I think it's a good news. It's a good vote, a good outcome. And we're,
[4215.36 --> 4218.58]  we're now, you know, we're now moving forward on the, on the right path.
[4219.08 --> 4223.18]  And for those listening, just to establish some timelines here, we originally recorded the call
[4223.18 --> 4228.30]  that they just listened to on May 8th. We have a week to week schedule when we release episodes.
[4228.30 --> 4235.86]  So we were planning releasing this on May 15th and May 13th comes around and, you know, good news,
[4235.98 --> 4241.74]  of course, but, uh, you and I weren't quite sure when it would happen. Uh, maybe you had a bit more
[4241.74 --> 4247.24]  information than I did, but nonetheless, uh, today's May 14th. And so just to kind of establish some
[4247.24 --> 4252.54]  timeline there for people to kind of catch up with, um, back and forth there. But so yesterday,
[4252.54 --> 4259.82]  May 13th, uh, the IOJS TC voted to join node foundation. And I think, um, some questions
[4259.82 --> 4263.08]  that probably come up initially, maybe you have some answers to these and maybe you don't,
[4263.08 --> 4269.58]  but, uh, what does it mean for IOJS? Does it mean that they'll join and operate under node
[4269.58 --> 4275.50]  foundation as node JS and sort of begin this convergence process and others, uh, a convergence
[4275.50 --> 4280.64]  repo, the two individual repos now, and there's lots of conversation happening there, but what
[4280.64 --> 4285.24]  ultimately is happening right now as of, as of this vote to join node foundation?
[4286.44 --> 4291.98]  So, uh, you know, great questions. Uh, funny, we, we had an, an all hands meeting inside
[4291.98 --> 4297.48]  joint this morning and those exact questions came up. Uh, I say, well, you know, some of them we have
[4297.48 --> 4301.22]  answers to, and some of them were, we will, we'll all work together to figure out the right answer
[4301.22 --> 4306.28]  to, and then go execute on them. Uh, but from a high level, you know, the idea is that the foundation
[4306.28 --> 4312.28]  is set up so that we have one community. We have a unified project, uh, that's here to help
[4312.28 --> 4317.36]  establish the neutrality, uh, establish the openness, really broader engagement with the
[4317.36 --> 4323.64]  community, uh, great neutrality for, for vendors. We, it's very important. We have a healthy ecosystem
[4323.64 --> 4329.30]  of vendors to provide additional tools and technologies and services around node to accelerate
[4329.30 --> 4335.90]  its adoption and increase the value of it. And then, you know, real good, um, uh, sort of de-risking
[4335.90 --> 4342.90]  of the project for the users who want, you know, who really do want a single project, um, and want to
[4342.90 --> 4348.50]  be able to have a trusted foundation that they can turn to, to help, uh, you know, find the right
[4348.50 --> 4354.14]  outcomes for all the different members of the community. Um, and so I think as we move forward,
[4354.14 --> 4359.98]  what, you know, we, we do have a community that's working together now under the node.js foundation.
[4360.70 --> 4367.42]  And, um, and so we'll all be working together under that, uh, under that umbrella. Um, and then as we
[4367.42 --> 4371.70]  move forward, then the technical details that everybody's working through is I think we have a
[4371.70 --> 4379.20]  pretty good handle now on the development policies and the governance models and all that's still open
[4379.20 --> 4383.42]  for a public comment, a lot of good work and your comments have come in under that, but
[4383.42 --> 4388.38]  always looking for more. Um, and then, you know, then it's getting in, getting down to the,
[4388.70 --> 4393.98]  you know, what do we do with the code base and the code bases? And, uh, you know, we're still working
[4393.98 --> 4398.32]  through a lot of that, but we want to, want to make sure that we come up with the right outcome that,
[4398.32 --> 4405.70]  that, uh, really benefits the, the, the users of this, that they, they get, how they get, uh,
[4405.82 --> 4410.36]  you know, healthy innovation and they get, uh, they can get access to the latest and greatest,
[4410.36 --> 4414.98]  but also, you know, certainly heard loud and clear from the enterprise customers that they want,
[4414.98 --> 4420.10]  uh, slower release cadence. They want, you know, let's say a six to nine month release cadence,
[4420.10 --> 4425.18]  uh, sort of faster than what we've seen over the last few years, but, uh, they want something maybe
[4425.18 --> 4430.08]  once a year or six to nine months. They want a new release. They want to, they want a publicized,
[4430.08 --> 4436.30]  uh, LTS policy. They want, you know, good visibility around, uh, testing and API compatibility
[4436.30 --> 4443.50]  and backwards compatibility and EOL. So, um, we are, uh, hashing through all of that now and
[4443.50 --> 4448.40]  absolutely want input on those issues. So we, we capture, you know, user requirements and,
[4448.52 --> 4455.00]  and, uh, you know, customer and user issues into that. Uh, so I'd say, uh, there's, we've done a lot
[4455.00 --> 4459.18]  of work, but there's still a lot of work ahead of us. And, you know, now we have an opportunity to
[4459.18 --> 4465.40]  work together, uh, to, to get the details right. And, uh, it's going to take a while to work through
[4465.40 --> 4470.50]  those, but, um, uh, I'm, I'm optimistic. We're on the right path to get them solved now.
[4472.08 --> 4476.44]  We have a developer centric audience that listens to this show quite a bit. So at least one of the
[4476.44 --> 4480.28]  questions I have and the questions we tend to have tend to be the questions of the community.
[4480.62 --> 4485.98]  Uh, not all of them, but some of them, um, right now node lives at joint slash node on GitHub and
[4485.98 --> 4494.56]  IO lives at IOJS slash IO.js. Well, will node ultimately, since it's now node foundation, will it move from
[4494.56 --> 4500.70]  under joint to its own organization in terms of, are you, are you privy to that information or is this too
[4500.70 --> 4508.58]  early to tell that kind of information? No, that, that's moving out from under, uh, joint node.
[4508.58 --> 4516.50]  And that's going to be the, the, the node JS foundation. Okay. Um, so, you know, we're, I think there's
[4516.50 --> 4523.00]  already a repo set up for that and we'll be, you know, moving stuff over there. Uh, I've seen one from, uh,
[4523.00 --> 4528.00]  from, I think it was, uh, Jason Snell. Is that, is that the fellow's name? I can't like,
[4528.32 --> 4531.88]  there's so many names. James. Yeah. James Snell. Yeah. Yeah. There's a Jason out there,
[4531.90 --> 4538.32]  I'm sure. But, uh, James Snell. Sorry about that, James. Um, yeah, James has a fork right now.
[4538.36 --> 4542.16]  It's the convergence repo. I think they're sort of testing whether or not they're going to do a
[4542.16 --> 4547.52]  get rebase or do a straight up merge and do cherry picking back and forth, uh, to sort of bring the
[4547.52 --> 4552.46]  repos together. So behind the scenes code wise, there's some things happening that, uh, that I'm curious
[4552.46 --> 4558.22]  about. And so I see that, but I haven't seen an organization on GitHub emerge yet that I'm aware
[4558.22 --> 4564.04]  of. So I wondered if you, if you knew about that, but. Well, the, the foundation hasn't been
[4564.04 --> 4572.62]  technically stood up yet. Um, but you know, it, it will be, I think we'll announce that as I said
[4572.62 --> 4579.62]  before sometime end of May, early June, uh, when it's officially formed, uh, and come, it comes to
[4579.62 --> 4585.88]  stand up as an official legal entity. Uh, and, and so, uh, you know, we'll, we'll see, we'll see
[4585.88 --> 4590.42]  those repos come together and this stuff, uh, uh, as we work through that timeline.
[4590.42 --> 4596.82]  So what we can expect now is essentially a unified front when it comes to node, uh, the IO name may
[4596.82 --> 4603.86]  or may not, uh, be to akin to MIRB as it is to rails for those who followed that, uh, saga probably
[4603.86 --> 4610.18]  five years ago, just before rails three came out. Um, you know, in our call before this,
[4610.24 --> 4614.76]  everyone just listened to, um, you and I speculated when it might've happened, you know, when this,
[4614.76 --> 4620.12]  this, uh, this joining of the node foundation might or might not happen. Uh, and as I said,
[4620.14 --> 4625.04]  you probably have a bit more information that you can't maybe share, um, you know, during the
[4625.04 --> 4629.22]  previous call, but was this a surprise to you? Were you expecting this to happen sometime soon?
[4629.22 --> 4633.98]  Uh, I know I was pretty surprised that, uh, that it happened. I mean, obviously we're back
[4633.98 --> 4637.02]  on this call again and I don't want to release the episode until you haven't had this conversation.
[4637.02 --> 4641.92]  So I wanted to make sure that, uh, that the community that listens to the change log understood
[4641.92 --> 4645.34]  that, uh, you know, we like to stay fresh and new. So we had to get you back on the call, Scott.
[4646.20 --> 4651.52]  Yeah, this is about as fresh as it happened. I don't think the ink is dry on that announcement,
[4651.52 --> 4658.84]  but usually you make your predictions in January and you don't know, you know, you cut,
[4658.84 --> 4662.74]  you're back on the show the following January, you get a year to see how things play out. But
[4662.74 --> 4668.48]  in this case, things, things are moving pretty fast. We talked last Friday today is Thursday. So,
[4668.48 --> 4673.70]  uh, we've had six days, a lot has happened. And I, you know, I don't recall exactly what the
[4673.70 --> 4679.24]  prediction was, but, uh, I, you know, at that point, you know, my expectation was that it was going to
[4679.24 --> 4686.24]  be sometime over the next two weeks that, um, that there was going to be a vote in the IOTSC,
[4686.24 --> 4693.20]  uh, to see, uh, to see where people sat on this topic and what they wanted to do. And, um, so,
[4693.20 --> 4699.16]  uh, it looks like, uh, it happened in the very early part of that timeframe. So I was expecting it,
[4699.16 --> 4705.66]  you know, probably more likely to be next week than this week. Um, but it looks like, uh, the, uh,
[4705.66 --> 4710.80]  they went through the vote, uh, you know, next week. In fact, uh, I think I told you is when I got your
[4710.80 --> 4715.34]  note today, I was in the middle of editing a blog post that was supposed to go out tomorrow
[4715.34 --> 4723.68]  about, uh, why, uh, the foundation makes a lot of sense for, you know, the IO community and for the,
[4724.10 --> 4729.36]  uh, to help, uh, solve some of the issues that, that we've seen over the last couple of years
[4729.36 --> 4737.82]  in the node.js community and the way the project was run. And, um, I, I'm busy editing it. So we'll,
[4737.82 --> 4744.88]  we'll see what, how that turns out for my blog post tomorrow. Uh, well, we certainly appreciate
[4744.88 --> 4749.00]  you taking the time to come back and, and, uh, just play a little catch up here. I know that,
[4749.00 --> 4755.42]  uh, um, your opinion matters. So I wanted to make sure that, uh, you know, it's just proof how fast
[4755.42 --> 4761.44]  open source moves. You know, our tagline around here is open source moves fast, keep up. And, uh,
[4761.44 --> 4766.98]  it just proves how fast it moves because six days ago, this news we had was just stale. So
[4766.98 --> 4771.76]  I was concerned that, that our show just would be obsolete, but it wasn't went back and listened
[4771.76 --> 4777.32]  to it during the edit process. And it's a great show. So I really enjoyed, uh, going back and
[4777.32 --> 4782.54]  taking a deeper listen to some of the things that you had to share about Joanne's history and the
[4782.54 --> 4788.16]  history with node and just how much is involved here. And I think people can't quite grasp that.
[4788.20 --> 4796.14]  And even sometimes, uh, Joanne takes a black eye sometimes because of the history of, of node,
[4796.14 --> 4800.46]  not so much, maybe not a black eye, maybe a, maybe a little punch here and there, you know,
[4800.46 --> 4805.00]  something like that, that, that you kind of get the bad name, but really all this while you've been
[4805.00 --> 4809.14]  supporting node and the community and just wanting the best that node could be.
[4810.40 --> 4815.36]  Yeah. You know, it's hard to please everybody. And we definitely took some body blows. Uh, and
[4815.36 --> 4819.90]  there, there was a lot of frustration in the community. They release their frequency of releases
[4819.90 --> 4824.60]  really slowed down. Um, you know, there were a lot of people in the community who wanted to
[4824.60 --> 4832.34]  participate, uh, more than they were. And there was a pretty rigorous, it was pretty hard to get
[4832.34 --> 4838.00]  onto the core team. There were a lot of pull requests that, um, you know, weren't getting
[4838.00 --> 4842.94]  the responses that some, some people wanted to get and weren't getting responded to as quickly as
[4842.94 --> 4847.42]  people wanted. So, so, you know, there was definitely some criticism coming Joanne's way.
[4847.42 --> 4853.28]  Um, and, but yeah, I don't know, you can't, you, you cannot please everybody. But as I said earlier,
[4853.28 --> 4858.42]  I, you know, I've only been enjoying it now for about nine months and I really want to do the
[4858.42 --> 4867.40]  right thing for node. And, um, this, this, I, I've believed since I first started working with our
[4867.40 --> 4875.24]  board of directors last October, November timeframe to, uh, convince them that this was the right thing to
[4875.24 --> 4883.44]  go do, um, that it really, it was the right thing for the project and it's truly transcended joint.
[4883.80 --> 4888.12]  And, um, I think this is the right thing. And I think we're starting to see that play out. I,
[4888.22 --> 4896.38]  I think the vote yesterday to, uh, have the IO TSC, uh, vote to, to work with the node foundation,
[4896.38 --> 4903.84]  uh, is an, or I call, I call it an early win for, for the foundation and the, the, the, you know,
[4903.84 --> 4909.72]  the, the motivations behind it to, you know, to, to rally the community together and seek that common
[4909.72 --> 4916.00]  ground. So, um, I'm, I'm happy. That's, it's great, uh, validation that the strategy is, uh,
[4916.30 --> 4920.74]  is playing out and getting some early wins for, for the overall project.
[4920.90 --> 4926.08]  I can definitely see that the future is getting more straight and more narrow for node and a lot
[4926.08 --> 4931.60]  more clear and a lot more accessible to those who felt, uh, like outsiders definitely having the
[4931.60 --> 4935.40]  governance and all the things we've talked about in place. But, uh, thank you so much,
[4935.46 --> 4939.72]  Scott, for taking the time to come back and have this quick chat. So let's, let's end here and let's
[4939.72 --> 4945.02]  everybody, uh, uh, I don't know, this may have been roughly an hour and 25 minutes. So thanks for
[4945.02 --> 4949.54]  listening to everybody. And, uh, we'll say goodbye. Thanks a lot, Adam. Take care.
[4949.54 --> 4951.54]  Bye.
