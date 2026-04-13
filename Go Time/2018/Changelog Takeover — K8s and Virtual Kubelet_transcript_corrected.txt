[0.00 → 2.88] Bandwidth for Changelog is provided by Vastly.
[3.22 → 5.30] Learn more at Fastly.com.
[5.64 → 7.18] Error monitoring is provided by Rollbar.
[7.56 → 9.28] Check them out at Rollbar.com.
[9.58 → 11.56] And we're hosted on Linde servers.
[11.98 → 14.00] Head to linode.com slash changelog.
[26.96 → 28.12] It's go time.
[28.12 → 32.14] A weekly podcast where we discuss interesting topics around the Go programming language,
[32.40 → 34.14] the community, and everything in between.
[34.52 → 38.56] If you currently write Go or aspire to, this is the show for you.
[49.24 → 51.58] So we have a short time span here.
[51.72 → 52.16] We do.
[52.44 → 53.32] A very short time.
[54.88 → 57.74] Let's do it the right way, I guess, right?
[57.74 → 61.84] Do we need to give anyone the breakdown?
[62.50 → 63.08] We need to spiel.
[63.46 → 67.10] This is a crossover show, so Eric's still going to introduce it like normal, but then we're
[67.10 → 68.54] going to kind of interview you guys, right?
[68.66 → 69.10] Is that the idea?
[69.80 → 70.00] Yep.
[70.20 → 72.68] Okay, so I'll still do the intro.
[73.08 → 76.40] I was actually thinking about what if I did the intro and acted like I wasn't Jared.
[76.76 → 78.38] Or actually, I acted like I wasn't Eric.
[78.90 → 82.38] And I said that this actually wasn't go time, but it might be.
[82.94 → 85.06] And then, Jared, you say, I don't think it's really the changelog either.
[85.14 → 85.80] Which one is it?
[86.02 → 86.48] What do you think?
[86.48 → 87.30] Something like that.
[87.30 → 91.86] I think you guys should do the whole host thing for the whole show, right?
[92.02 → 94.40] Like, intro and all, we're taking over.
[95.26 → 95.54] Okay.
[95.98 → 96.14] Yeah.
[96.34 → 97.22] Go time, takeover.
[97.34 → 97.82] I like that.
[98.28 → 98.74] Go time.
[98.82 → 100.00] Go time, takeover.
[100.64 → 101.96] Go time, takeover.
[103.54 → 105.10] Well, we don't do an intro, though.
[105.50 → 106.14] No, we really don't.
[106.62 → 107.50] Our intro's in post.
[107.72 → 109.24] So we just start talking on our show.
[109.52 → 110.24] Technically, we do.
[110.42 → 111.50] This could be the show.
[112.06 → 112.74] This is the show.
[113.72 → 114.60] Which show is it, though?
[114.60 → 117.00] Is it go time or is it the changelog?
[117.28 → 117.66] It's both.
[118.96 → 119.16] Double.
[119.30 → 119.84] We're double-dipping.
[119.84 → 121.12] Simultaneously, both shows.
[122.32 → 123.42] I'm so confused.
[123.74 → 124.88] And we don't know where we're at.
[125.74 → 127.82] We should start at the beginning and work our way up.
[128.32 → 132.28] We should introduce Eric and Brian, or we should introduce Jared and Adam.
[132.28 → 135.28] It's quantum podcasting.
[135.40 → 135.62] Yeah.
[137.24 → 138.36] Quantum podcasting.
[139.36 → 145.14] Well, we're here today to talk about virtual cube let, which is something Eric and Brian,
[145.30 → 147.28] you all are both super excited about.
[147.62 → 150.42] And Adam and I are both super ignorant about.
[151.16 → 153.68] And so I'm excited to get schooled.
[153.68 → 154.62] Oh, you know all about this?
[154.72 → 155.56] I know all about it.
[155.60 → 156.62] I was part of the hack team.
[157.20 → 157.66] All right, Adam.
[157.74 → 158.30] Tell us a little bit.
[158.30 → 159.26] My name isn't in the list.
[159.36 → 160.22] Why is my name not there?
[161.70 → 162.60] Anyway, I'm getting around.
[163.10 → 164.64] I like taking credit for your work.
[164.72 → 165.06] That's right.
[165.88 → 166.52] You're right, Jared.
[166.60 → 167.16] I'm ignorant.
[167.34 → 167.70] Go ahead.
[169.28 → 173.86] Well, since we've established that, help us out here, guys.
[174.00 → 179.16] Help us understand virtual cube let, what it is, who built it, the whole spiel.
[179.16 → 185.72] And then I'm sure we'll pour into all sorts of questions and side conversations around it.
[185.78 → 188.18] But one of you two, give us the rundown.
[188.18 → 194.14] So I guess to kind of fully understand it, how familiar are you with Kubernetes itself?
[195.24 → 200.82] So we've done shows on Kubernetes, which means we've had smart people teach us about it.
[200.82 → 205.72] And we haven't actually used it for anything IRL.
[206.24 → 212.50] And so it's very much academic and somewhat transient knowledge that floats in and out between my ears.
[212.62 → 214.08] I don't know if that speaks for you, Adam.
[214.26 → 218.20] But very generic knowledge, no practical use of it.
[218.46 → 221.12] So a general rundown would be nice, too.
[221.12 → 222.12] Okay.
[222.12 → 229.34] So from a high level, Kubernetes is orchestration platform for containers.
[229.80 → 231.70] But really, it's more than that.
[231.86 → 238.40] And to fully understand how it works, you can think about there's an API server as part of the control plane for Kubernetes.
[238.40 → 243.50] So the control plane are all the components that Kubernetes kind of handles for you.
[243.86 → 246.00] And then you have your nodes with your logic.
[246.00 → 256.12] So you submit a spec for a resource that you would like, whether that's a service or you're trying to run a pod, which is really just a group of containers.
[257.08 → 265.44] And the API server kind of recognizes that as desired state, whether you're creating one or updating it or deleting it.
[265.74 → 272.56] And then there are other components like controllers and things like that that run within the system that are just constantly trying to reconcile the differences.
[272.92 → 273.04] Right.
[273.04 → 274.98] So you just submitted a pod.
[275.34 → 279.86] I see a pod in the API, but I don't see a pod running on any node.
[279.86 → 285.70] So I need to, you know, assign this to the node and the scheduler runs and things like that.
[286.80 → 291.22] So who decides what a reconciliation looks like?
[291.92 → 294.66] So that would be the job of the controller.
[295.24 → 296.36] So there are different controllers.
[296.54 → 300.30] There's a controller manager process that runs that kind of encompasses some of those.
[300.30 → 308.04] But in some cases, like with the operator pattern or like Prometheus and things, it has its own controller.
[308.64 → 316.70] And a controller's job is just to kind of look at what's in the API and watch it and monitor the thing that it controls and try to reconcile the differences.
[316.70 → 329.00] So in the case of a pod, there's a first the scheduler kind of jumps in and assigns a node through kind of looking at what else is running and available resources.
[330.32 → 334.76] But yeah, each resource type kind of works the same way.
[334.80 → 342.10] You're just kind of inserting it and some process or another within the system is monitoring that and then trying to reconcile the difference.
[342.10 → 344.34] So it's just kind of like a big reconciliation loop.
[344.74 → 344.96] Okay.
[345.24 → 351.12] So the subedit is actually the agent that runs on all your worker notes.
[351.12 → 360.28] And it looks at the things that the scheduler has assigned to it and looks at what's running in Docker and then reconciles the differences.
[360.62 → 363.26] You know, it sees a pod in the API that it does not have running.
[363.54 → 364.52] It starts it.
[364.88 → 371.14] If it sees something running that is no longer in Kubernetes API that's assigned to it, it deletes it.
[371.88 → 374.26] And that's sort of just rinse and repeat.
[374.36 → 376.04] That's how the process works.
[376.86 → 378.74] The subedit has a bunch of other jobs, too.
[378.74 → 383.28] And I actually wrote a blog post today that kind of points out some of that stuff.
[383.42 → 387.08] But, you know, it looks at the pod, and it tries to fetch the images from the image repo.
[388.22 → 390.66] It attaches volumes to the containers.
[391.18 → 395.98] It handles the kind of networking, setting up the interfaces and dropping them in the container.
[396.70 → 400.56] So it's kind of the workhorse for each node.
[401.50 → 402.54] What's the point of it?
[402.54 → 408.32] Is it supposed to, from my understanding, it's supposed to like to allow outside systems to call into the Kubernetes cluster?
[409.36 → 411.60] For the sublet or the virtual sublet?
[411.70 → 412.32] The virtual sublet.
[412.62 → 413.10] What's the point?
[413.18 → 413.28] Yeah.
[413.68 → 416.46] So and here's kind of where we get into the virtual sublet.
[416.86 → 423.74] So the virtual sublet is just a process, but it behaves the way the sublet does.
[423.84 → 426.10] So it just runs somewhere in your cluster as an application.
[426.10 → 431.64] But it connects to the Kubernetes API and adds a node resource to the cluster.
[431.90 → 435.90] So it just kind of hosts a spec saying, hey, here's a node.
[436.48 → 441.22] And Kubernetes thinks that that's a node, which means that the scheduler starts assigning work to it.
[441.22 → 448.60] So the virtual sublet just sits here and monitors the API for any pods or things like that that could assign to it.
[448.60 → 461.56] And then rather than kind of interacting with a physical host, we created this provider interface, which just really you implement a few methods like create, update, delete.
[461.56 → 479.20] The virtual sublet kind of does that reconciliation loop and populates the environment variables and volumes and things like that from your secrets and config maps so that you have to kind of do minimal work outside, you know, implementing how a pod gets deployed.
[479.50 → 479.58] Right.
[479.58 → 480.70] That's your job.
[481.14 → 496.54] The virtual sublet kind of runs and calls into the provider at lifecycle events like, hey, we know that this pod is in Kubernetes, and we've asked you about the pods that are running or whatever the equivalent is in your provider interface.
[497.00 → 498.10] What's running there?
[498.24 → 500.36] And we know that you don't have this.
[500.78 → 501.62] Please deploy it.
[502.66 → 504.34] And it kind of works in that way.
[504.42 → 504.60] Right.
[504.94 → 509.12] Or, hey, this is no longer here, or we received a delete event on this pod.
[509.12 → 510.70] And you're still running it.
[510.84 → 511.72] Please tear it down.
[512.86 → 515.00] So let me see if I'm tracking this here, Eric.
[515.14 → 526.28] So a sublet normally runs in the context of a node, and it speaks to the API server and vice versa, representing that node, so to speak.
[526.88 → 533.30] And then it kind of manages or handles that node specific context.
[533.72 → 534.62] What is a node usually?
[534.72 → 536.04] Is it like a network endpoint?
[536.04 → 539.00] Is it like an IP address on a network?
[539.24 → 540.94] Is it a virtual machine inside?
[541.04 → 542.06] What does a node represent?
[543.06 → 548.34] So a node's usually, in the Kubernetes context, it's either a physical or virtual machine.
[548.72 → 549.06] Okay.
[549.54 → 550.86] Yeah, it's a server.
[551.70 → 551.98] Okay.
[552.08 → 552.50] Very good.
[552.62 → 553.32] That clears that up.
[553.32 → 568.96] So then a virtual sublet is basically saying, hi, I'm a sublet and I have a node and I can answer all the same regular API calls that an API server would expect a sublet to respond to, only it's not really any of those things.
[569.32 → 570.44] It's just faking it.
[570.44 → 571.44] Exactly.
[571.54 → 572.16] Now it could be.
[572.26 → 582.94] You could use your virtual sublet to run Docker containers just like Kubernetes does, but you could also build a provider for the sublet that did completely different things.
[582.94 → 596.54] So one of the first providers we shipped was the ACI provider that lets us use Azure container instances to start work from a Kubernetes cluster without actually having a live node.
[596.96 → 599.80] Azure container instances are ephemeral.
[600.04 → 604.62] You start one, and it goes away when it's gone, and you don't need to restart it.
[604.62 → 611.00] And I think part of the confusion like we've had in conversations is the fact that it's like it's a node, but it's not a node.
[611.20 → 616.66] And people wonder like, is this a process that runs on a host instead of the sublet or things like that?
[617.10 → 625.56] And I think to kind of fully understand that you just think about a node in Kubernetes sense is just an entry in the API server.
[625.56 → 629.14] Like you just add yourself, and you're like, yes, there is.
[629.34 → 631.06] It's just something that gets registered into the server.
[631.06 → 635.82] It's like a line item in a database or something like it just knows about it.
[636.34 → 636.66] Exactly.
[636.90 → 639.86] And then the rest of the system reacts based on that.
[640.08 → 649.32] Like, okay, now I need to collect metrics from this or, you know, now the scheduler is allowed to schedule things to this.
[650.12 → 654.12] And or that I know that I signed this pod to this node.
[654.12 → 666.44] So when a subject exec comes in, I know I need to forward that request to that sublet because it's responsible for that container that you're trying to get in.
[666.76 → 668.38] So it's really just an entry.
[668.52 → 671.48] And then from there, you're interacting with the API.
[671.48 → 676.82] And it's fascinating because of the use cases.
[677.74 → 680.02] And we talked a bit about that.
[680.08 → 682.12] And I think that's the part that confuses people the most.
[682.22 → 687.42] You're like, okay, so you're like masquerading as a node, but why?
[687.96 → 688.10] You know?
[688.16 → 688.30] Right.
[688.30 → 692.76] So Brian pointed out like ACI.
[693.04 → 697.02] And I don't know how familiar you are with Azure Container Instances.
[698.30 → 702.02] But I know they're ephemeral because Brian just told me.
[703.30 → 705.50] So that's true in the middle of the way.
[705.50 → 716.52] So the best way to kind of think about Azure Container Instances is they're called a container group in the context of Azure Container Instances.
[716.86 → 719.66] But it's basically like pods as a service.
[719.98 → 725.02] So you're not really thinking about Kubernetes and the whole cluster and some of the other resource types that exist.
[725.46 → 730.52] You're just like, here's my group of containers that kind of share a namespace.
[730.78 → 732.34] Just deploy it, you know?
[732.38 → 734.10] And I want a public IP, right?
[734.10 → 737.66] You're only just trying to run this one pod or something like that.
[737.80 → 741.84] There's no kind of like service discovery and all of these things.
[742.12 → 752.32] And it makes it fascinating for people who just only have a couple of things to deploy or for kind of quick workloads.
[752.32 → 757.88] Like you just have workers and jobs and things like that are running that are fairly isolated.
[758.58 → 761.06] But you're only paying per second while these things run.
[761.06 → 764.18] And this is kind of where the power of virtual sublet comes in.
[764.18 → 773.18] Because now you can kind of have this node that exists in your cluster with endless capacity, right?
[773.48 → 781.06] So it could just kind of just burst out in parallel, and you could run 100 workers on ACI, pay per second.
[781.38 → 782.88] And then when they're done, they're done.
[782.88 → 791.04] And you don't have to have the spare capacity in your cluster to support all these batch jobs or CCD or things like that.
[791.10 → 794.18] They just kind of run out there in ACI and come back.
[794.26 → 799.44] But as far as like your infrastructure is concerned, you're just treating it the same way as your normal cluster,
[799.44 → 803.66] except, you know, maybe having some node selectors and things on there saying like,
[803.74 → 807.18] I would like these types of jobs to run out in ACI.
[809.68 → 811.08] It's like a temp agency.
[811.84 → 812.88] Like a temp agency.
[813.12 → 813.72] Yeah, there you go.
[814.00 → 817.64] I was going to say, I was going to ask permission to play the cynic here for a moment.
[818.06 → 818.46] Sure.
[818.46 → 826.34] Because so the cynic might say, OK, this is a hack so that you can run ACI with Kubernetes.
[827.20 → 832.20] Is there is like that and that's very much trying to get us to just use ACI.
[832.30 → 833.06] Are there other uses?
[833.16 → 834.12] Is this what it's for?
[834.54 → 840.66] Is this so is there is it going to be above and beyond or is that like the goal and now the goal is accomplished, and now we should go try it with ACI?
[841.22 → 847.16] No, we created it with kind of like the modular back end so that, you know,
[847.16 → 849.62] we want to encourage other people to implement these.
[849.78 → 855.30] And, you know, we've got companies like Hyper-SH jumping on to build a connector to their systems.
[855.80 → 858.72] So we'd like to see this expand out more.
[858.96 → 863.14] It's, you know, would we love you to use this with ACI?
[863.46 → 863.98] Absolutely.
[864.30 → 864.52] Right.
[864.82 → 871.14] But I think it's more important than that because we've got kind of like the Kubernetes landscape going on,
[871.22 → 873.28] but serverless is also catching on.
[873.28 → 873.52] Right.
[873.52 → 882.06] And I think that this type of virtual Sublet scenario is a really awesome bridge in between the two.
[882.16 → 882.38] Right.
[882.86 → 891.76] Where you have these workloads that are really intermittent, you know, whether that's a spike in traffic or a batch job or just CCD.
[891.76 → 892.08] Right.
[892.20 → 905.60] Like think about a commit heavy day in CCD and how long you might have to wait for your commit to run through CCD because you only have one virtual machine dedicated to that.
[905.80 → 909.98] So you only run, you know, five in parallel or whatever you have that configured for.
[909.98 → 915.52] Like this, you don't actually even have to have a VM for your CCD.
[915.80 → 915.98] Right.
[916.50 → 919.36] Like it doesn't matter whether there's one commit or 20.
[919.46 → 922.82] They just fan out in parallel and you just kind of pay per second while they're running.
[922.92 → 924.24] And when they're done, they're done.
[924.70 → 930.82] And, you know, in a lot of cases, it may actually be cheaper for you to do that because you're not paying for all that idle time.
[930.82 → 931.64] Mm hmm.
[932.68 → 942.30] To the note of the agnostics to this, you've got in this diagram in this post you mentioned, ACI, Azure Container Instances, AWS.
[942.88 → 944.78] And then, as you mentioned just before, Hyper.sh.
[944.98 → 955.76] Now, you got those in your examples there, but this is also, you know, Microsoft developers were a part of putting this together, but it's not under the Microsoft org on GitHub.
[955.96 → 957.58] Can you talk about why that is?
[958.56 → 958.74] Yes.
[958.92 → 959.30] So we.
[959.60 → 960.40] Oh, go ahead, Brian.
[960.82 → 973.78] I was just going to say, I think that we made a concerted decision to give this all the reality of being a community project, as opposed to this is a Microsoft thing.
[973.78 → 975.12] So you can run ACI.
[975.34 → 980.18] We want this to be a tool that people can use with ACI, but with anything else, too.
[980.82 → 987.64] And we've already had discussions with other major cloud providers that we can't name that are jumping on board to play, too.
[987.64 → 990.70] So there's its a community thing.
[990.74 → 993.26] And we didn't want the big Microsoft badge on the top of it.
[993.76 → 997.00] You know, we're happy to take the credit for building it because it's a really cool thing.
[997.40 → 1001.42] But at the end of the day, we want everybody to be able to use it and people to jump in and contribute.
[1001.42 → 1005.04] Can you talk about what the world was like before this virtual sublet?
[1005.16 → 1015.00] I'm imagining that often we, you know, produce projects like this or solutions that were at some point before duct tape and, you know, sort of band-aid.
[1015.16 → 1018.98] Was this possible prior to virtual sublet that people do this before?
[1019.16 → 1022.44] And what would how do they actually achieve these goals?
[1022.44 → 1039.32] So, you know, adding to Brian's point about the quickly about the community aspect, I think that, you know, we're trying to evolve our own products and make them more usable and offer things to help customers solve problems.
[1039.32 → 1042.10] And I think things like virtual sublet definitely do that.
[1042.54 → 1047.56] But I think more importantly, though, is the advancement of the community and the technology.
[1047.94 → 1058.68] And we're, you know, Kubernetes is so still new when we're trying to figure out, you know, innovative ways to use it and run it in different scenarios for different workloads and how to do that efficiently.
[1058.68 → 1066.92] So I think, you know, this is valuable for internally to Microsoft, but, you know, we could also see the value to the broader community.
[1067.14 → 1072.14] And I think that's why, you know, we decided that this should be done completely in the open.
[1072.14 → 1095.68] Now, as far as, as far as like did things like this exist, not to my knowledge, a few months ago, Brendan Burns and a couple of other people put together a prototype of something like this to connect ACI to Kubernetes.
[1095.68 → 1099.76] And to kind of prove that, proved out the concept.
[1100.24 → 1109.94] And then we kind of decided to take that and turn it into a much more like fledged out product with more features and like a community effort.
[1110.62 → 1113.58] I think there's some stuff for doing serverless with Kubernetes.
[1114.00 → 1116.94] Correct me if I'm wrong, Brian, but I can't remember the name of the project.
[1117.20 → 1118.28] There's one out there.
[1118.88 → 1121.04] But I think we saw this as kind of more of.
[1121.04 → 1127.02] So serverless, I think, with containers, you have the warm-up time of the container and stuff.
[1127.04 → 1137.22] And I don't I don't know whether we're quite there yet, but definitely the batch and CCD jobs and bursting into out into a cloud provider.
[1137.22 → 1142.74] Like, I think that that's the main appeal and the core use cases we're focusing on first.
[1144.18 → 1149.22] So James Lovato in the chat would like to know, does this mean that a virtual sublet will support PowerShell?
[1149.22 → 1151.90] And when you all answer that question for him.
[1152.92 → 1163.96] I'm not sure whether what that would mean, because the virtual sublet really is just an application that runs and behaves like it's the sublet on a node.
[1164.98 → 1165.22] Yeah.
[1166.84 → 1169.40] Kubernetes supports Windows workloads already.
[1169.40 → 1179.56] So if you deploy a Windows workload on a Kubernetes cluster that has Windows servers on it, then you can already do PowerShell.
[1180.04 → 1180.52] OK.
[1180.70 → 1180.82] Yeah.
[1180.88 → 1188.86] And we do have the ability to pass in a flag when the virtual sublet starts up to tell it that it should behave as if it's a Windows node.
[1188.86 → 1198.28] So you could definitely do that to throw your Windows workloads out into ACI or any other provider as those start getting implemented.
[1198.28 → 1201.80] Well, James, hopefully that answers your question.
[1201.98 → 1208.04] If not, reformat it and ask it another way, and maybe we'll, we'll address it if we have a more full understanding.
[1208.64 → 1214.92] Just going back to the Microsoft thing, I'd like to introduce a little bit of a meta conversation because it's something that Adam and I think about.
[1214.92 → 1227.40] And I'm sure you all have thought about and just trying to navigate life with a job, and also I'll just for lack of a better term, call a personal brand or like the person that you are.
[1228.12 → 1237.30] And both of you have recently joined Microsoft as employees, and you do a lot of your public speaking in that context here.
[1237.36 → 1241.36] You're doing open source in that context, you know, whether on the job, off the job.
[1241.36 → 1254.40] How do you deal with like putting on and taking off the quote unquote Microsoft hat and the way that that signals to your friends and followers online and whatnot?
[1255.56 → 1257.40] You go first, Eric. That's a tough question.
[1257.90 → 1269.16] OK. Yeah. So I think actually part of the appeal to this job was, you know, and a lot of the discussions early on was that, you know, we were to be ourselves, right?
[1269.16 → 1271.98] Like we were to be genuine and altruistic.
[1272.40 → 1283.22] And there's not really this push from executives or marketing for Brian and I to run around and shout from the rooftops like everybody use our stuff.
[1283.22 → 1283.66] Right.
[1284.76 → 1290.26] We get a lot of opportunity to contribute and things, but they just want us to be us.
[1290.26 → 1295.54] And, you know, if is I'm excited about a product, I'll talk about it.
[1295.64 → 1299.88] And if I'm not crazy about it, you know, I won't talk about it.
[1299.88 → 1304.26] But one of the interesting things, though, is that we get the opportunity to use a lot of this stuff.
[1304.26 → 1308.44] Right. You know, things that we didn't have time to play with when this wasn't our job.
[1308.44 → 1326.66] So AKS, which is our managed Kubernetes and like we got to play with that, like before it was announced to the world, and we got to offer perfect feedback to the product teams about, you know, things that we thought the community would want or need or questions that we have.
[1326.66 → 1334.82] And, you know, that's super appealing because you kind of get to Brian and I are more members of the community.
[1334.82 → 1342.44] Right. Like so, you know, we're advocates, but we advocate on behalf of the community to the product teams and documentation teams.
[1342.44 → 1348.76] Like we're deeply ingrained in these communities and this is what we think that they would want or these are the problems they're facing.
[1350.14 → 1352.90] So it goes both ways. Brian, we'd love to hear your thoughts on that.
[1352.90 → 1366.28] Yeah. Eric covered quite a bit of it. And I would just reiterate that the main focus of the conversations when we started was or at least when I started, I wasn't there when Eric had his conversations.
[1366.28 → 1378.48] But the main focus of them was just how much they wanted us to be ourselves and continue to be ourselves and not put on the Microsoft marketing hat.
[1378.48 → 1388.70] So all the things that I represent when I'm talking or online or in Twitter or blog posts or whatever, they're they're honest and not sponsored.
[1388.86 → 1394.16] You know, they're things that I've discovered, which are fun or things that I'm doing, which are interesting.
[1395.26 → 1402.28] And some of that is because, you know, Microsoft has allowed me the freedom to go play with things that I wouldn't have time to play with before.
[1402.28 → 1408.66] Right. Right. But yeah, I'm not going to talk to the public about Microsoft products I don't enjoy.
[1409.16 → 1419.90] Instead, I'll turn around and talk to those product teams and say, you know, the people that I know in the go or Kubernetes community would probably enjoy this particular thing a lot more if it did X, Y and Z.
[1419.90 → 1430.80] And that's that's that's a really nice place to be in, because the people internally in Microsoft are hungry for that kind of data and really want to build products that everybody loves.
[1431.50 → 1439.52] And, you know, it is allows me to keep a good conscience about the things that I'm talking about online.
[1439.52 → 1446.82] Yeah. And I think it's hard, too, because, you know, evangelism kind of got a bad name for so many years.
[1446.82 → 1452.44] Right. It was kind of by people with good names and have them talk about your stuff.
[1452.70 → 1455.68] And I think people kind of feel dirty when they hear that.
[1455.72 → 1458.16] And that's why there's a whole advocacy thing. Right.
[1458.58 → 1462.10] So I think it just takes time for people to kind of understand the difference.
[1462.10 → 1465.62] And I think different companies do advocacy differently, too.
[1465.62 → 1481.76] I know Google has, you know, a very similar advocacy program like we do, where it's its more about being genuine to the community and helping the product teams evolve products or create new product offerings that solve problems that you're aware of in your community.
[1481.76 → 1489.10] And I think when you think about like developing products like they want to you want to create good things that people use.
[1489.34 → 1493.68] You often get detached from the people who are using it. You're too busy building it.
[1493.68 → 1498.28] This episode is brought to you by our friends at Good.
[1498.88 → 1502.94] Good is an open source continuous delivery server built by ThoughtWorks.
[1503.28 → 1510.30] Good provides continuous delivery out of the box with its built in pipelines, advanced traceability and value stream visualization.
[1511.08 → 1516.68] With Good, you can easily model, orchestrate and visualize complex workflows from end to end.
[1516.68 → 1521.74] It supports modern infrastructure with elastic on demand agents and cloud deployments.
[1522.10 → 1526.00] And their plug in ecosystem ensures Good will work well in your unique environment.
[1526.50 → 1530.88] To learn more about Good, visit gocd.org slash changelog.
[1531.10 → 1536.04] It's free to use and has professional support for enterprise add-ons available from ThoughtWorks.
[1536.04 → 1539.32] Once again, gocd.org slash changelog.
[1541.82 → 1553.50] So Eric, when we were at Rubicon, you mentioned to me this project and sort of the backstory and how it came together was, I guess, being in Austin for a week or so prior to the actual conference.
[1553.50 → 1555.90] And you were sort of already there for a couple of weeks.
[1555.90 → 1563.22] Can you kind of talk about maybe the early process of like organizing that and maybe whatever the backstory might be to kicking off this project?
[1564.16 → 1567.16] Yeah, I mean, I didn't organize it per se.
[1567.56 → 1579.38] We had talked about rewriting this in Go because, you know, a lot of the people who are working on similar projects in Kubernetes itself, you know, that was the language it was written in.
[1579.38 → 1588.64] And then it sort of evolved into this like, well, you know, wouldn't it be cool if, you know, we didn't really dictate what the backend was, right?
[1588.64 → 1597.34] Like we just kind of provided this project where you can kind of invent what the node actually represents, right?
[1598.40 → 1602.36] So, yeah, we were all scheduled as a team to go out to Austin.
[1602.36 → 1615.40] And we're like, let's, you know, talking with Rhea, the PM and stuff on the project and Robbie from ACI team.
[1615.70 → 1619.78] Like, let's just get everybody to go out early and, you know, hack on it.
[1619.88 → 1623.78] And I think it might have been Brian Liston, who is Brian and I's manager.
[1624.54 → 1625.70] I think it might have been his idea.
[1626.38 → 1628.70] Yeah, we kind of all got together for a week.
[1628.70 → 1637.76] And it was actually, even internally to Microsoft, like it was a pretty big deal because, was it Brian, like eight different teams were involved?
[1638.66 → 1638.78] Yeah.
[1639.72 → 1643.70] So, yeah, we had, you know, some CDs, which were the Cloud Developer Advocates.
[1644.52 → 1648.90] We had some, I think it's called Customer Solutions Engineers.
[1649.26 → 1650.56] I forget what CSE means.
[1651.16 → 1656.70] We had some people from the ACI team, some people from the Azure Container Service team.
[1656.70 → 1665.86] We had people from the CLI team who built out stuff where there's now a command within the easy tool that Azure provides to just install it for you.
[1666.60 → 1670.08] We had people working on CI for it.
[1670.14 → 1672.02] We had people working on the actual implementation.
[1672.76 → 1685.10] It was just super cool to see like this big group of people from like different teams and even organizations within the company just kind of like all jumping in and making it happen.
[1685.10 → 1691.88] And it was one of those things we started working on it, you know, as we all had time, weeks leading up to Rubicon.
[1692.16 → 1697.50] But it really didn't start, didn't really kick off and start development until that week there.
[1697.64 → 1702.66] And it was just awesome to watch it get to the point where it's at in one week.
[1702.66 → 1706.54] That's interesting to hear that you were, you know, working on a prior to it.
[1706.62 → 1710.06] It would make sense, but wasn't really sure where the context began.
[1710.20 → 1720.48] What whose idea, I guess, was it was a way it a meeting and somebody's like, hey, we got this problem or, you know, how did the idea get formed, and who was sort of leading that?
[1720.48 → 1723.06] I'm actually not sure, Brian.
[1723.16 → 1730.86] Do you know, I know Brendan Burns was the first person to spike out a prototype of connecting these two.
[1731.72 → 1735.30] You know, I think in that case, it was just really they called it the ACI connector.
[1735.54 → 1740.34] Its job literally was just to bridge Kubernetes with ACI.
[1740.34 → 1744.42] I'm not really sure who had the idea.
[1744.56 → 1749.16] My assumption is it was Brendan, but it could have it could have been somebody else.
[1749.16 → 1754.08] As far as turning it into like a modular open source project, I don't really know either.
[1754.08 → 1763.28] We got together to talk about we got together to talk about like porting it to go and fixing a couple of issues and adding some needed features.
[1764.12 → 1770.32] And then I think it was just kind of like this collaborative brainstorm of, you know, well, we could do this, and we could do that.
[1770.34 → 1774.18] We could make it, you know, an interface that could be implemented.
[1774.18 → 1777.90] And it just sort of evolved organically through these discussions.
[1778.46 → 1780.12] Those things are usually hard to remember.
[1780.50 → 1789.46] I just scroll back through Slack, and it was Eric's idea to turn it into a Go interface that anybody could implement so that any provider would work.
[1789.80 → 1800.18] So Eric, once again, is being shy and humble, but it was absolutely his idea to turn this into more than just the ACI connector and turn it into something big.
[1800.74 → 1801.14] Wow.
[1801.92 → 1804.28] Can you recall that, Eric, or are you just being humble?
[1805.12 → 1807.40] No, I honestly can't recall it.
[1807.62 → 1814.12] Like, it's hard because a lot of people kicked out ideas, and it's really hard to remember where the ideas came from.
[1814.32 → 1815.48] Why do you think you felt that way?
[1815.90 → 1819.02] Just if you can is you can't really recall it, maybe you can't remember this part.
[1819.08 → 1823.88] But what do you what do you think motivated you to feel so, you know, so community oriented?
[1823.88 → 1827.64] Well, I think Microsoft is community oriented, too.
[1827.70 → 1827.84] Right.
[1827.86 → 1833.74] Like it was meant to be open source from the beginning when we started when we started building it.
[1834.74 → 1842.64] But I mean, as far as like other people implementing that stuff, it's fascinating because like what IP are you really protecting?
[1843.06 → 1843.24] Right.
[1843.24 → 1847.16] Look at all of us who came together in a week and kind of got to where we're at.
[1847.16 → 1856.18] So if is you hoard it to yourself and not to everybody else, like how long would it really take them to make something that's similar?
[1856.52 → 1856.88] Like so.
[1857.02 → 1857.78] So what's the point?
[1858.14 → 1858.44] Mm hmm.
[1858.44 → 1864.98] It was also self-evident to it at Rubicon just how much the community had grown.
[1864.98 → 1885.18] And it was all because of the original idea, which was to not keep Kubernetes a Google thing and make it more of a community thing and then ultimately be donated to, you know, the CNCF Cloud Foundation, you know, the Cloud Computing Foundation to have that as like a, you know, an underlying DNA was self-evident at that conference.
[1885.18 → 1895.14] So I would imagine that being there and once you got there and just kind of seeing how the community has grown, that it was a that that's the way things should operate in this community.
[1895.92 → 1897.44] It's always a juggle, right?
[1897.54 → 1911.74] Because on one hand, like you have to have your IP, you have products, and you want to evolve those, and you want to kind of keep stuff to yourself so that you have kind of these value adds over competitors, right?
[1911.96 → 1914.98] From a business perspective, like totally understandable.
[1915.18 → 1926.18] But I think on the other side of it, like all of the cloud giants and things like that, you know, see the value of working together to evolve the space.
[1926.70 → 1934.58] You know, like because from my perspective, right, like, you know, I don't know if this is Microsoft's view, but this is definitely mine.
[1934.58 → 1939.70] Like competing for customers is kind of a losing game, right?
[1939.76 → 1947.06] Like, I don't think if we offered Netflix free services forever that we could ever get them to convert over, right?
[1947.06 → 1956.64] Like, so the idea of trying to compete directly and steal customers, I think that you're putting in a lot more effort for little reward.
[1956.64 → 1971.74] But now building abstractions, virtual sublet, building things like Helm and Brigade and things like that, that help make the cloud and things like Kubernetes and containers more approachable to a broader audience.
[1971.74 → 1975.20] Because now you're creating more customers, right?
[1976.46 → 1980.76] Because there's more people that have not adopted the cloud than there are people there.
[1981.26 → 1994.74] And it makes far more sense for us to keep helping make it more approachable than it does sit here and try to compete feature for feature or hoard our knowledge and projects and stuff like that.
[1994.74 → 2001.16] Well, speaking of people, let's give some credit to those who are part of the team.
[2001.52 → 2009.88] But as a byproduct of that, can you kind of talk about something you said earlier was, you know, you all hacked on it prior to the conference.
[2009.88 → 2015.56] But, you know, the idea was spawned to go ahead of time and sort of time box some collected effort.
[2016.06 → 2019.02] You know, it seemed a little bit like tunnel vision to focus on it.
[2019.02 → 2024.96] And out, you know, the other end came this prototypical project, you know, in time for the conference.
[2024.96 → 2038.98] So can you kind of give some credit to the team that was involved and mention some names, but then also talk about what it, you know, what it was like to meet up ahead of time, where you met at, kind of like, what were some of the circumstances you were in to make sure that you were all very productive?
[2038.98 → 2052.36] Yeah, I mean, because we were all in different teams with our own priorities and, you know, the CDs travel a lot and speak and are creating content and, you know, the engineers on the product teams are busy with their own features and stuff.
[2052.36 → 2057.10] So it was one of those, like, jumping in and out as people had time.
[2057.26 → 2058.88] So it made a lot more sense, I think.
[2059.06 → 2067.78] And, you know, I give Brian and RIA a lot of credit for coming up with the idea of, like, let's get everybody there under the same roof for one week.
[2067.94 → 2072.42] And it's much easier to focus on it when that's literally what you're there for.
[2073.40 → 2079.44] I'm trying to determine the scope of this project in terms of, like, surface area, something that comes together so quickly.
[2079.44 → 2084.28] And I think it's interesting on GitHub, I tried to look at the dependencies.
[2085.10 → 2088.98] And it said there weren't any, but there's a vendor directory and there's a bunch of stuff in there.
[2089.02 → 2094.08] And then I ran a clock on it and there's, like, 1.8 million lines of code.
[2094.52 → 2096.12] So you guys definitely have some better dependencies.
[2096.72 → 2101.12] But maybe help us out with understanding, you know, you mentioned the effort that went into this.
[2101.18 → 2103.70] I think a lot of it is the idea, the design, conceptual.
[2104.70 → 2108.98] How much, you know, how much code was cranking, and who gets the props on that stuff?
[2109.44 → 2114.10] I think it was roughly, well, the end result, right?
[2114.20 → 2116.24] Because a lot of code was created and then deleted.
[2116.54 → 2119.80] So that is much harder to tell, like, exactly how many.
[2119.96 → 2126.68] But I think the end result, if you exclude vendor stuff, is, like, around 4,000 lines of credit.
[2127.68 → 2130.64] And, I mean, I can mention a few names.
[2130.78 → 2133.86] I hope I cover everybody, but they're all in the blog post.
[2133.86 → 2137.68] But Brian definitely contributed.
[2138.62 → 2139.14] Myself.
[2139.68 → 2140.82] Jesse Frizzell.
[2141.54 → 2144.10] I'm going to butcher some names.
[2144.36 → 2145.72] Julian Kronecker.
[2146.54 → 2147.58] Neil Peterson.
[2148.52 → 2149.48] Rhea Bhatia.
[2150.14 → 2151.12] Rita Zhang.
[2151.22 → 2151.88] Robbie Zhang.
[2152.20 → 2153.76] And Sure Mazurka.
[2154.20 → 2156.48] I wish I knew the last names here.
[2156.56 → 2157.92] You always know people by first name.
[2157.92 → 2158.48] Yeah.
[2158.82 → 2162.24] But I think that's everybody.
[2162.52 → 2164.46] And I'm sorry if I left anybody out.
[2164.90 → 2167.46] It was crazy and heads down coding.
[2168.74 → 2171.42] Let's talk a little bit more about the possibilities now.
[2171.50 → 2172.90] Because now you have this thing, right?
[2172.92 → 2178.04] You have this new opportunity, which are you can load up this virtual sublet inside of Kubernetes.
[2178.04 → 2182.40] And basically be a facade for all these other things behind it.
[2182.90 → 2184.06] First, ACI.
[2184.18 → 2190.68] And then also this hyper.sh, which I'm just learning is an on-demand container per second billing.
[2191.24 → 2192.26] Another provider.
[2193.46 → 2195.04] You list out a few things in the post.
[2195.30 → 2197.66] And you mentioned CI as one of them earlier in our conversation.
[2198.68 → 2200.14] But what are some other uses?
[2200.82 → 2204.18] I know serverless is a possibility, but potentially some drawbacks there.
[2205.30 → 2206.80] You have batch jobs.
[2206.80 → 2211.56] Open up into those and tell us why people might want to do this.
[2212.14 → 2213.46] I've got a perfect one.
[2213.96 → 2219.94] So Kubernetes itself is very much a container-focused, container-oriented workflow.
[2220.46 → 2223.88] But the sublet really doesn't care what it's starting.
[2224.50 → 2229.34] So it's entirely possible to register a virtual sublet on your Mac.
[2229.34 → 2240.44] And as the workload, give it the name of a bash script or some executable to run and have that be the thing that gets executed when Kubernetes tells it to.
[2240.94 → 2244.94] So you could do this in a container-free environment.
[2244.94 → 2249.20] And you would lose all the benefits of containers.
[2249.20 → 2254.36] But it's easily possible to do something really crazy like that.
[2254.36 → 2255.20] Yeah.
[2255.28 → 2260.32] And another one I list is kind of like a possibility in the post is virtual machines.
[2261.12 → 2261.22] Right?
[2261.32 → 2262.80] So the virtual sublet doesn't care.
[2262.92 → 2263.04] Right?
[2263.14 → 2268.22] Like Kubernetes only cares that this node exists and gives it work.
[2268.36 → 2270.90] It doesn't really care how it deploys it, things like that.
[2271.30 → 2273.10] The virtual sublet, same thing.
[2273.10 → 2276.16] It just calls out and says, I need you to create this pod or delete this pod.
[2276.24 → 2288.24] So you could have your provider provision a virtual machine and then run that pod inside the virtual machine in complete isolation, like if you were running a multi-tenant environment.
[2288.80 → 2290.60] So there's like all these creative things.
[2290.90 → 2293.70] And I'm really interested to hear other things people come up with.
[2293.70 → 2315.82] But I think the primary focus for at least like phase one of, you know, rolling this out to be production ready would probably be more along the lines of like your batch and CCD type stuff where, you know, your core cluster where you have your provision VMs that are just on 24-7.
[2315.82 → 2323.96] And, you know, they're kind of set up at a capacity to handle your normal workload, you know, with some headroom and things like that.
[2324.14 → 2331.04] But then allow you to run like your batch work that may be really intensive or takes a long time only running a single instance of.
[2331.30 → 2336.70] You could run as many as you want in parallel and batch CCD kind of, you know, think about the same way.
[2337.12 → 2341.16] But those can run out in this virtual node that's ACI.
[2341.54 → 2344.56] And you're only paying for kind of the time that they're running.
[2344.56 → 2347.28] And they don't have to be run serially, right?
[2347.32 → 2350.34] They can be run completely in parallel, and you're paying the same amount of money.
[2350.42 → 2351.12] It doesn't really matter.
[2351.66 → 2361.02] But then you're not paying for like this idle resources running so that you have leftover capacity for when your batch job runs at 3 a.m. or whatever.
[2362.40 → 2370.14] One thing you mentioned serverless, which definitely piqued my interest when I saw it, is that you may have issues with warm-up time.
[2371.10 → 2373.30] Basically, the containers need to spin up and spin down.
[2373.30 → 2381.12] Can you expand on that and tell me why that's different from like a Lambda, or I'm sure Azure has a serverless thing.
[2381.38 → 2381.98] What's Azure called?
[2382.92 → 2383.80] Azure Functions.
[2384.02 → 2384.66] Azure Functions.
[2384.78 → 2385.12] Thank you.
[2385.58 → 2390.56] And I'll leave this to Brian to describe because I'm newer to the serverless world.
[2390.90 → 2393.84] So I think he would have a much better explanation than me.
[2393.84 → 2401.66] First, I have to find that amusing if I'm the resident expert on services because that's just hilarious.
[2402.60 → 2411.82] But on the serverless side, when you're running a function, you generally are executing code live in some sort of environment.
[2411.82 → 2423.80] But if you were to use ACI or some other Kubernetes-inspired thing to do that, then you'd have to download a container from a container registry, a Docker container.
[2423.80 → 2441.54] And the time that it takes to download that container could impact your startup time, which would make your serverless function slower on the first run or on the first run in each node since that Docker container would be cached for the second runs.
[2441.54 → 2449.22] So there definitely would be an impact in startup time with a container versus not a container.
[2450.24 → 2455.66] Yeah, I was going to say, since you're the expert, Brian, how do they do it on like Azure Functions and AWS Lambda?
[2455.80 → 2460.68] Surely they have to spin up something on demand as well in order to get the environment ready for you.
[2461.26 → 2462.88] So there are two answers to that.
[2462.88 → 2473.46] Both Azure Functions and Lambda allow code execution in a sanitized environment, but it's not a container environment.
[2474.00 → 2475.72] So you're just executing a function.
[2475.92 → 2479.34] You know, it fires up Node.js and runs your JavaScript thing.
[2479.82 → 2480.00] Right.
[2480.06 → 2481.00] But that's not in a container.
[2481.00 → 2487.78] I can't answer for Lambda, but I know Azure Functions allows you to run a Docker container too.
[2487.78 → 2495.18] So if you're using the Voucherized workflow for either one of those, you're already paying that price in startup time.
[2495.48 → 2498.00] But if you're not, then it would be a big difference.
[2498.92 → 2499.36] Gotcha.
[2500.20 → 2502.42] Especially like in the Kubernetes environment too.
[2503.96 → 2511.10] It can be even more slowed if the container that needs to run hasn't run on that node before.
[2511.82 → 2513.58] Because then the image has to be pulled.
[2513.94 → 2517.06] And then depending on how large the image is, you have to wait for that.
[2517.78 → 2520.12] And that's sort of like even how Kubernetes works, right?
[2520.14 → 2522.08] It's an eventually consistent system.
[2522.54 → 2526.12] I use a declarative API to say, this is my intent.
[2526.54 → 2528.58] You know, this is the desired state.
[2528.88 → 2530.28] And then it evolves there.
[2530.38 → 2532.24] There's no guarantee that that's instant.
[2532.24 → 2536.32] The second that Kubernetes tells me, like, yay, I accepted your new pod.
[2536.38 → 2537.38] It doesn't mean it's running yet.
[2538.02 → 2542.66] And it could take, you know, who knows how long, depending on whether it needs to pull images and things like that.
[2542.66 → 2548.70] So the other thing that you're obviously very excited about this, but you want to see what other people can come up with.
[2548.74 → 2550.76] So these are just a few potential use cases.
[2551.24 → 2555.78] It's not quite production ready yet, or it's on its way to becoming production ready.
[2556.22 → 2562.04] What would be like a call to action for people beyond use cases, maybe providers, people writing interfaces, people trying it?
[2562.04 → 2566.26] What do you want from the community at large at this point with regard to Virtual Cuba?
[2567.26 → 2574.76] I mean, I'd like to see people actually using it in some real use cases and start fixing things that come up.
[2575.12 → 2581.84] You know, like we said, this was an effort where we all kind of came together and hacked on it for a week, you know, a little time leading into it.
[2581.84 → 2584.94] So it's very much still in its prototype phase.
[2585.50 → 2586.82] For the most part, it works.
[2586.82 → 2593.88] But, you know, I imagine there are some rough edges and, you know, there are different areas that we still need to solve for.
[2594.84 → 2598.10] But, yeah, I mean, mostly trying it out, reporting bugs.
[2598.56 → 2603.26] You know, I'd love to hear use cases people think of or different providers.
[2605.22 → 2608.26] It's working its way towards production.
[2608.26 → 2612.70] We've got some people using it internally and playing with it.
[2612.82 → 2614.44] So we've been fixing things that come up.
[2615.38 → 2624.06] I think one of the first providers that we'll see that has a generalized business use case is like a Jenkins worker,
[2624.06 → 2630.50] where you run Jenkins Master or whatever they're calling the Jenkins Master thing now.
[2630.50 → 2644.92] You run that, and then it spins up virtual sublet instances to do each one of the tests or the suite of deployment tasks.
[2645.30 → 2646.24] And then they go away.
[2647.10 → 2653.00] I think CI is probably going to be the earliest use case for something like this.
[2654.04 → 2655.92] But I also agree with Eric.
[2656.02 → 2658.20] We're going to see some fascinating stuff, too.
[2658.20 → 2662.36] I'm really surprised by the number of people who see the vision.
[2662.96 → 2671.44] Because, you know, like I knew for us and HyperSH, who had forked our original connector that Brendan Burns had written,
[2673.12 → 2675.20] like I knew those people would get it.
[2675.28 → 2677.34] Like, oh, yeah, you know, we can work on it together.
[2677.34 → 2683.70] But the number of people who kind of like saw the vision of like, oh, cool, like now we can use Kubernetes.
[2684.20 → 2686.68] And it doesn't actually have to be backed by a physical node.
[2686.90 → 2695.40] And use some of this like on-demand infrastructure as part of your normal cluster.
[2695.90 → 2700.34] Like it was actually really cool to see that and to see one of the keynote speakers mention it.
[2700.44 → 2701.24] And it was just like, whoa.
[2701.24 → 2712.90] Yeah, one of the things that I'd like to see, and I would write if I had any time, is something like a Zen hypervisor adapter for virtual sublet.
[2713.46 → 2716.56] Zen has an API, not a complicated one even.
[2716.56 → 2729.58] And it would be relatively painless to stand up a Zen node and use the virtual sublet to run workloads inside Zen virtual machines easily.
[2730.70 → 2736.18] That's another use case that would be really straightforward with virtual sublet.
[2737.20 → 2740.06] This episode is brought to you by Linde.
[2740.06 → 2742.88] Linde is our cloud server of choice.
[2743.18 → 2747.42] And everything we do here at Changelog is hosted on Linde servers.
[2747.84 → 2750.26] Pick a plan, pick a distro, and pick a location.
[2750.74 → 2752.82] And in seconds, deploy your virtual server.
[2753.18 → 2754.06] Dual-worthy hardware.
[2754.38 → 2755.94] SSD cloud storage.
[2756.26 → 2757.44] 40 gigabit network.
[2757.74 → 2759.38] Intel E5 processors.
[2759.94 → 2761.42] Simple, easy control panel.
[2761.88 → 2764.50] 99.9% uptime guaranteed.
[2765.04 → 2766.68] 24-7 customer support.
[2766.68 → 2767.84] Nine data centres.
[2767.96 → 2768.52] Three regions.
[2768.72 → 2770.14] Anywhere in the world they've got you covered.
[2770.46 → 2774.54] Head to lino.com slash changelog and get $20 in hosting credit.
[2776.54 → 2781.06] All right, so this is a hybrid show with Changelog and the Go Time FM crew.
[2781.20 → 2791.88] And in the Go Time podcast, we like to bring up interesting news and interesting projects that have come across our news desks over the course of the week.
[2791.90 → 2793.28] So we're going to kick that off now.
[2793.28 → 2798.12] Lots of interesting things have happened since the last time we gave out news.
[2798.26 → 2802.22] But probably the biggest is the Go 1.10 beta 1 release.
[2803.12 → 2805.70] And lots of things changed there behind the scenes.
[2805.84 → 2809.34] Not a lot changed that's visible, though, which is kind of nice.
[2810.14 → 2811.78] As per the Go usual.
[2813.06 → 2817.12] Eric, did you have any favourite feature of Go 1.10 that you wanted to hit?
[2817.12 → 2823.76] I mean, with every Go release, there's always performance improvements.
[2824.70 → 2833.70] And I know that there was some stuff in there about lowering allocation latency and improving on the garbage collector.
[2833.70 → 2837.50] But a lot of the stuff that I saw that was really cool was surrounding testing.
[2838.36 → 2840.80] It now supports caching your test results.
[2841.04 → 2850.66] If it knows that none of the code behind it has been changed, it just runs and then produces the output of the last run and says that it's cached.
[2851.22 → 2856.56] So that should make consistently running your unit tests, your whole suite, much faster.
[2856.56 → 2862.78] It also runs Covet before it does the tests, which is super cool.
[2863.90 → 2866.72] So it's interesting you mentioned the cached test results.
[2866.92 → 2871.80] That's actually a bonus side effect of the compiler changes that they made.
[2872.20 → 2880.68] So, you know, the Go test or the dash A flag that we have in the previous versions of Go that would force you to recompile everything.
[2880.68 → 2886.84] So if you did go test dash A or go build dash A, they would recompile all the things underneath the covers.
[2887.44 → 2888.76] That's no longer supported.
[2888.88 → 2896.54] It's no longer needed because the compiler now knows, based on the contents of the file, whether they've changed.
[2896.62 → 2898.30] And it doesn't use file timestamps.
[2898.44 → 2899.72] I think I have that the right way.
[2899.72 → 2915.32] So now we'll only compile the things that are absolutely necessary to compile, and that benefit will be mainly in compile times, but it also comes across in terms of tests, too.
[2915.88 → 2920.64] So we don't have to rerun tests that have already run successfully with the exact same code.
[2921.54 → 2926.06] So I'm looking forward to increased speed for compile times.
[2926.14 → 2926.60] That'll be fun.
[2927.46 → 2928.26] As always.
[2928.26 → 2945.20] So another exciting thing is if you're not watching the Gopher Academy blog, we started our annual Advent series, and there's a bunch of good articles in there already, like writing a Kubernetes-ready service from zero.
[2945.46 → 2947.44] There's a gRPC one in their in Go.
[2948.12 → 2952.60] Brian wrote one about repeatable and isolated development environments for Go.
[2954.00 → 2958.00] Damian Risky wrote one on minimal perfect hash functions.
[2958.26 → 2960.06] So there are a bunch of good ones in there already.
[2961.10 → 2963.26] That's not like all the ones I say are good.
[2963.42 → 2968.26] I just, these are the ones I could think of off the top of my head, and there are still a couple of weeks left.
[2968.56 → 2970.58] So definitely follow that if you're not already.
[2970.88 → 2972.76] We'll drop a link in the show notes.
[2974.00 → 2975.80] Yeah, it's a perfect series this year.
[2975.86 → 2977.08] Lots of really great articles.
[2977.08 → 2982.46] So I came across something that should inspire the hackers in all of us.
[2982.96 → 2990.00] Everybody who has anything close to a modern car has that ODB2 port underneath the dash.
[2990.32 → 2998.14] And I've always wanted to play with it, you know, interface my computer with the car and just do something super hacky and fun and awesome.
[2998.14 → 3005.88] Well, somebody on GitHub released a Go driver or a Go interface to the ODB2 system.
[3006.54 → 3008.88] And he called it, they called it Elmo DB.
[3010.14 → 3015.12] So I'm assuming that Elmo is like the Sesame Street Elmo, but it's Elmo DB.
[3015.52 → 3017.64] And that's at GitHub.com.
[3017.78 → 3018.10] Elmo BD.
[3018.98 → 3019.62] Elmo BD.
[3020.08 → 3020.96] It's a database?
[3021.02 → 3021.28] Right.
[3021.44 → 3022.50] Or what's going on?
[3023.26 → 3024.86] Oh, it's OLD.
[3025.54 → 3026.70] Oh, OLD, not DB.
[3026.82 → 3028.36] I said ODB.
[3028.92 → 3029.92] I said that wrong.
[3030.58 → 3031.52] The old dirty database.
[3032.20 → 3034.52] Yeah, it's the Go adapter to that.
[3034.68 → 3039.50] So in theory, you could bring the laptop into the car and really start hacking into stuff.
[3040.10 → 3044.00] And I intend to do that at some point really soon because that just sounds fun.
[3044.66 → 3050.42] Is there any way, Brian, that you could somehow hook your car up to your Go-based barbecue system?
[3050.42 → 3055.70] And maybe, I don't know, like when you rev the motor or something, it barbecues better?
[3055.88 → 3056.22] I don't know.
[3056.36 → 3057.06] Just spitballing here.
[3057.30 → 3057.92] What can you do?
[3059.36 → 3062.46] These are good questions that I should probably...
[3062.46 → 3063.00] I like that.
[3063.28 → 3064.16] It barbecues better.
[3064.28 → 3065.40] It barbecues better somehow.
[3065.52 → 3065.86] I don't know.
[3066.50 → 3067.28] That's a good question.
[3067.48 → 3068.48] I don't know the answer to that.
[3068.56 → 3072.78] I can't think of an immediate application, but that doesn't mean that one doesn't exist.
[3072.78 → 3083.56] Just real quick, Brian, for the changelog side of listeners who haven't heard about your barbecue system, probably most of the Go Time listeners have, but maybe there are new ones who haven't.
[3083.64 → 3086.30] Can you just tell us about this?
[3086.48 → 3087.94] Because it's so awesome.
[3088.66 → 3088.86] Sure.
[3089.00 → 3093.62] It's a Raspberry Pi setup that Eric and I have been building for just a little over a year.
[3093.62 → 3106.52] It includes some hardware pieces, electronic pieces that control the airflow into a fire-driven barbecue, so a real old-school barbecue with a fire pit.
[3107.02 → 3111.82] We use a Raspberry Pi that has a relay.
[3112.34 → 3120.94] The relay turns on or off a fan, which feeds the air into the fire pit, which either dampens or increases the fire temperature.
[3120.94 → 3132.74] And then there are temperature sensors that determine the temperature of the smoke box, so we know whether we need to increase the temperature of the fire or just let it smolder for a while.
[3133.30 → 3146.44] And the whole thing feeds MQTT data off to a Grafana dashboard, so we've got gorgeous graphs that show us how hot the food is and how hot the fire box is.
[3146.44 → 3151.30] And it's just a great big IoT barbecue blast.
[3152.76 → 3153.30] That's beautiful.
[3153.46 → 3160.16] Is any of that, like, does the charts go online somewhere, so people can, like, remotely participate in your cooking session?
[3160.68 → 3162.14] You know, it's funny you should ask that.
[3163.24 → 3168.44] So Brian was going to do a whole pig one weekend, and this is, like, when we really, like, threw it together.
[3168.44 → 3173.06] Like, together, like, okay, we need, like, graphs and charts and stuff with Grafana.
[3174.18 → 3182.06] And, yeah, I think it was me who came up with the domain name, but, like, happened to search, and barbecue.live was available.
[3182.32 → 3183.96] And we were both like, yes.
[3185.04 → 3185.90] So it is live.
[3186.54 → 3187.22] You got it?
[3188.34 → 3189.64] I'm loading it up right now.
[3189.64 → 3193.18] Yeah, so you won't see any data there right now because nobody's barbecuing.
[3193.38 → 3202.80] But if you were barbecuing, if one of us were, you'd be able to pick which of the two grills at the top of the screen where it says home.
[3203.26 → 3206.80] Pick either Brian or Eric's, and you could see the feeds from our barbecues.
[3207.42 → 3208.56] Well, what are you guys waiting for?
[3208.60 → 3209.70] I want to see these charts move.
[3209.80 → 3211.44] Run out there and start barbecuing something.
[3211.76 → 3213.04] I've got a job, man.
[3214.06 → 3215.44] Can't barbecue every day.
[3215.66 → 3217.70] Aren't you usually barbecuing on Thursdays, though?
[3217.70 → 3220.56] Thursday is a pretty big day for barbecuing, yes.
[3220.64 → 3225.76] But tonight we're going to get a Christmas tree and stuff that's going to take me away from the house.
[3226.10 → 3228.36] So no queue today.
[3229.24 → 3235.40] Our OBD2 thing, like, is this where we insert the legal disclaimer that we are not responsible for you damaging your car?
[3236.02 → 3238.12] Yes, that's probably a perfect place for that.
[3238.52 → 3240.60] I had no idea this port actually even existed.
[3241.22 → 3244.24] I mean, I know there are ports, but I didn't know it was a certain port.
[3244.24 → 3250.34] And I didn't consider the idea of plugging something into it and, like, port scanning it or finding ways to hack it.
[3250.90 → 3252.02] Doesn't it just do metrics?
[3252.02 → 3253.30] It just does metrics, though, right?
[3253.98 → 3254.16] Yeah.
[3254.40 → 3255.96] There's no writeability.
[3256.62 → 3256.86] Can you?
[3257.52 → 3257.92] Yes.
[3257.92 → 3258.12] Yes.
[3258.62 → 3272.38] So if you go to, you know, a mechanic or, you know, you go to AutoZone or Advanced Auto or wherever and, like, you have a diagnostic light on, that's what they're connecting their little machine to tell you what the code means.
[3272.38 → 3272.56] Okay.
[3273.20 → 3273.52] Okay.
[3273.76 → 3282.20] So it kind of connects to the cam bus and stuff that goes throughout the car where all the messages from the internal computers kind of share.
[3282.72 → 3286.82] So, yeah, you do have the ability to sometimes change stuff.
[3287.16 → 3293.82] But, yeah, I mean, you can definitely pick up the speed of the car and the RPMs and things like that through that port.
[3294.02 → 3294.78] Remove the governor.
[3294.78 → 3298.84] Well, yeah, how much you can change really depends on the car manufacturer.
[3299.28 → 3299.40] Yeah.
[3299.52 → 3305.16] Some manufacturers have a decently secure system and some are wide open.
[3305.40 → 3308.52] I mean, you could literally do things like turn on the turn signals from your computer.
[3308.74 → 3309.94] What's security like, though?
[3309.98 → 3313.12] I mean, how secure do they make this thing?
[3313.18 → 3315.18] I mean, I don't know anybody who's hacking cars.
[3315.18 → 3318.32] People have done it.
[3318.32 → 3329.54] Yeah, if they use TLS or encryption, then it would be really difficult to send messages to systems that required the encryption bits.
[3330.20 → 3335.88] But if they don't use any encryption, then you just need to know what to send, what message to send, because it's a giant bus.
[3336.40 → 3339.68] So you send a message out on the bus and anybody who cares about it will do something.
[3339.68 → 3347.54] And that's why some actions that you perform while you're driving cause other things to happen.
[3347.64 → 3353.54] You turn on the turn signal, but it turns off the left front headlight because the left turn signal's on.
[3353.64 → 3354.68] You've seen that in the new cars.
[3354.80 → 3356.08] That's all bus-driven.
[3357.22 → 3366.50] I wonder if there's a database or an index out there of, like you had said, cars or trucks or vehicles that use or don't use TLS or encryption.
[3366.50 → 3372.34] That way it might give you a leg up like, oh, I have a Ford Explorer.
[3372.68 → 3373.46] I can hack that.
[3374.54 → 3375.68] I'm sure there is.
[3376.34 → 3381.18] Yeah, there's a lot of people who have reverse engineered some of the messages on the cam bus and things like that.
[3381.26 → 3387.20] There's lots of people apparently tearing apart their cars and reverse engineering them, surprisingly.
[3387.70 → 3390.02] I'm like, hey, honey, I just bricked the truck.
[3390.16 → 3391.26] You know, it's no longer a truck.
[3391.38 → 3392.26] Now it doesn't move.
[3392.84 → 3394.08] We're going to need a new truck.
[3394.08 → 3396.62] And the manufacturer's like, what are you doing with the ODB?
[3397.04 → 3397.52] What is it?
[3397.58 → 3399.34] ODB2 port?
[3399.86 → 3400.46] OLD.
[3401.54 → 3401.78] OLD.
[3401.78 → 3403.80] I said it wrong the first couple of times.
[3403.86 → 3404.62] Does it mean something?
[3404.70 → 3405.64] Is it short for something?
[3406.34 → 3406.74] OLD?
[3407.88 → 3409.70] Yeah, it's onboard diagnostics.
[3409.78 → 3410.10] Okay.
[3410.30 → 3410.98] That makes sense.
[3411.12 → 3413.92] And it's version two, I'm assuming, because it's two.
[3413.92 → 3426.32] It just reminds me of a changelog we did back in the summer, Adam, with Tim Heckled, who first engineered the blood glucose monitor for diabetics and with Elixir.
[3426.32 → 3437.20] And basically was able to build interfaces into that to get the data off and then eventually to run the what's it called?
[3437.30 → 3437.66] The insulin?
[3438.74 → 3439.36] I forget.
[3439.56 → 3439.90] The loop.
[3440.38 → 3441.06] Yeah, the loop.
[3441.14 → 3442.50] The loop was the term that I remember.
[3442.68 → 3442.80] Yeah.
[3442.80 → 3451.48] Anyway, just thinking about reverse engineering things and devices that should be and have encrypted communications between parts that don't.
[3452.14 → 3454.78] Well, it kind of reminds me, too, of the movie The Martian.
[3454.78 → 3478.18] And there was one point where Johanna, I forget the girl's name now that I think about it, but she had to be tasked with hacking the computer to essentially override the ability for NASA to course correct, essentially.
[3478.66 → 3479.06] Right.
[3479.06 → 3493.26] And it kind of reminds me of that, is like, you know, she is like, she hacks into the code real quickly and determines that because it's not a secure type of thing, it's just meant to be a nice to have, not a need to have.
[3493.32 → 3497.98] They never really intended to put security on it because they never considered that there would be mutiny.
[3498.20 → 3506.12] But of course, anytime you have a ship or, in this case, a spaceship, you know, in space, it's still a ship, but it's a spaceship.
[3506.12 → 3514.08] You got to prefix it, you know, that the crew may go against the will of its originator, which is NASA.
[3516.56 → 3518.20] Well, let's not get Adam too far.
[3518.24 → 3519.58] Don't get me into the movies, man.
[3519.76 → 3525.20] But that's fun stuff to think about to like to have, you know, everybody typically has a vehicle outside their house.
[3525.20 → 3535.02] And most people listening to either the changelog or go time would be the type of people that would go out, you know, and find a way to hack this thing.
[3535.08 → 3541.20] And I think it's pretty interesting to think about all the listeners somehow bricking and or interestingly hacking their vehicle.
[3542.70 → 3548.16] Or maybe, just maybe they're running buzzers against BBQ.live trying to ruin Brian's dinner.
[3548.16 → 3553.54] Luckily, that is only push.
[3553.68 → 3559.86] There's nothing on BBQ live that actually like pushes down to the controller.
[3560.92 → 3562.18] It's only metrics.
[3563.40 → 3565.88] If you find a way, I will be impressed.
[3567.82 → 3569.46] Any more fun news to cover?
[3569.46 → 3572.84] I mean, there was the Joy compiler.
[3573.10 → 3573.84] Oh, gosh.
[3574.22 → 3579.08] Yeah, which is the new GoToJavaScript compiler that recently came out.
[3579.18 → 3582.30] I haven't had a chance to play with it, so I don't know how it compares to Gopher.js.
[3583.08 → 3587.30] I don't know whether you have, Brian, but it seemed cool, and it's something I will probably try to play with.
[3587.94 → 3588.98] Yeah, it's not complete enough.
[3589.16 → 3594.56] So in terms of completeness, Gopher.js is close to 100% or at 100%.
[3594.56 → 3598.00] Joy, I think they claim roughly 80% complete.
[3598.00 → 3602.06] There are several things that don't compile from GoToJavaScript yet.
[3602.76 → 3604.28] So it's not quite there.
[3606.64 → 3610.02] Honestly, it was one of those things that I'm glad they did it because it's awesome.
[3610.32 → 3619.38] But I wondered why they didn't spend the time on changing something in Gopher.js if there was something missing in Gopher.js.
[3619.38 → 3633.48] I always wonder what happens there whenever you have a fork or a very parallelled project that's got similar motives, similar goals, and they intend, or they go on their own, essentially.
[3634.50 → 3635.88] It's confusing sometimes.
[3636.42 → 3639.60] What usually happens is people get confused and then create a third option.
[3639.94 → 3640.22] Right.
[3640.22 → 3640.52] Yeah.
[3641.84 → 3643.38] Rails and Mere.
[3645.64 → 3650.38] There's a section on the website that says, how does Joy compare to Gopher.js?
[3650.60 → 3653.12] So he does answer some of these things.
[3653.54 → 3654.06] Oh, awesome.
[3654.26 → 3655.30] So you can read that.
[3655.40 → 3656.34] We'll link to it in the show notes.
[3656.46 → 3659.52] But the overall thing is there are two different approaches to the same goal.
[3659.64 → 3665.00] So apparently just wanting to take a different angle at a similar end, which I think is worthwhile.
[3665.34 → 3665.84] Touché then.
[3665.84 → 3668.96] I think it's worth mentioning, too, the design of this page.
[3669.08 → 3674.98] I mean, going back to some things we tend to, we just had a conversation on, which is a future episode of the Teams.
[3675.04 → 3677.18] It's just like this intention behind your design.
[3677.98 → 3681.28] This page does instill some joy into me.
[3683.06 → 3695.28] And for those going to mat.TM slash joy, which is the URL to go to check it out, it says the Joy Compiler, and it's beautiful clouds, vanilla skies, and an air balloon.
[3695.84 → 3697.30] Pretty pastel colours.
[3697.42 → 3697.60] Yeah.
[3698.26 → 3699.06] It's very joyous.
[3699.58 → 3699.74] Yeah.
[3700.98 → 3702.04] I'll agree with that.
[3702.80 → 3706.78] So, I mean, outside of that, we can kick off Free Software Friday, too.
[3707.48 → 3707.96] Let's.
[3708.36 → 3709.00] Let's do it.
[3709.12 → 3710.12] So I'll go first.
[3710.12 → 3722.20] So at Rubicon, Brendan Burns, who works at Microsoft with us as one of the co-creators of Kubernetes, announced kind of like this new effort he created, which is called Metaparticle.
[3722.20 → 3724.60] So metaparticle.io.
[3724.98 → 3727.00] And this is like fascinating.
[3727.42 → 3745.38] Basically, what it is, is this idea that through annotations in code or actually almost like a DSL within the language, just basically libraries that you could include that you wouldn't have to be familiar with, you know, a Docker file and Kubernetes spec.
[3745.38 → 3757.14] And whatever you're writing your stuff in and maintain properties like what port is bound to and then the container and making sure it exposes it and then making sure the pod spec has that in there.
[3757.24 → 3762.06] And then making sure that service that load balances between the instances of it also have that.
[3762.06 → 3772.00] And there's kind of like this disconnect where if you change things and just it's a lot for people to understand, you know, four or five languages to be able to build an application and deploy it to the cloud.
[3772.20 → 3780.66] So there's like this experiment of like this grand vision of what would it be like if it was just part of writing code, like it was a library within your code.
[3780.88 → 3785.84] And when you compiled it, it just knew how to containerize itself and deploy it.
[3785.84 → 3788.84] And it's really worth a look.
[3789.08 → 3794.98] And I'm interested to see these abstractions because I think, you know, Kubernetes is an awesome abstraction over infrastructure.
[3795.34 → 3805.30] But I think we still haven't got to like what's the abstraction over that that makes it just seamless to build an application and have it deploy for most use cases anyway.
[3806.16 → 3813.28] Yeah, and this reminds me deeply of a Twitter conversation I had maybe a month or two ago where I said something similar to this.
[3813.28 → 3816.94] You know what kind of abstractions are we going to build on top of Kubernetes?
[3817.14 → 3819.20] What are we going to build on top of distributed systems?
[3819.58 → 3827.14] And somebody that I remember respecting said something to the effect of, no, there will be no more abstractions.
[3827.24 → 3832.62] We've made all the abstractions we can, and we're not going to make any more on top of the stuff that we have.
[3833.12 → 3833.76] You know, this is it.
[3833.80 → 3837.14] And I thought, well, that is just the most closed-minded thing I've ever heard.
[3837.54 → 3839.04] Of course, we're going to abstract more.
[3839.04 → 3842.80] If we didn't abstract more, we'd all be writing assembly language.
[3843.24 → 3845.54] You know, we'll always continue to grow like that.
[3845.60 → 3858.76] And I think Metaparticle is a great step in that direction of really putting the complexity of distributed systems aside and just allowing you to code intent.
[3858.76 → 3870.12] And I forget exactly how Brendan worded it, but it was something along the lines of, you know, he wants to empower developers to build systems they wouldn't normally build.
[3870.66 → 3873.42] And, you know, learning distributed systems is a challenge.
[3873.62 → 3884.32] You know, it's more things, you know, as developers, we're having to know and learn and understand a lot more things just to participate in the current way things are done.
[3884.32 → 3890.92] And I don't know who coined this, but, you know, having conversations with Joseph Jax, he talks about it.
[3891.32 → 3894.88] You know, when you think about this, it's like a pendulum, right?
[3895.24 → 3898.80] First, we swing kind of up and out, right?
[3899.22 → 3903.10] And that's kind of like what we're doing with some of the Kubernetes stuff, right?
[3903.10 → 3909.24] And then next, we're kind of down and in where it's sort of like embedded within the language.
[3910.10 → 3916.84] And, you know, Metaparticle and things like that are partly kind of like the down and inside of that.
[3919.24 → 3923.94] I don't think we're going to be done abstracting until we recreated the helideck from Star Trek.
[3923.94 → 3927.46] At that point, like that's a good abstraction.
[3927.68 → 3931.64] We can just take a break after that and just enjoy the fruits of our labours.
[3931.72 → 3933.88] But until then, more abstractions.
[3934.46 → 3936.42] I want like almost Matrix style.
[3936.56 → 3939.20] Like I just want to think it and for it to be, right?
[3939.76 → 3940.16] Exactly.
[3941.68 → 3942.80] Who would like to go next?
[3943.80 → 3944.22] So I will.
[3944.34 → 3947.40] I've got an interesting terminal emulator that I found.
[3947.40 → 3953.12] It's at GitHub.com slash Eugenie, E-U-G-E-N-Y slash terminus.
[3953.56 → 3960.84] And it's yet another Electron app that you can install on Windows, Mac, or Linux.
[3961.10 → 3967.86] And I'm using it on Windows because it's actually a really nice Linux feeling terminal emulator,
[3968.12 → 3970.48] which is something that's missing in the Windows world.
[3970.94 → 3976.40] So it's a perfect emulator for that Linux feel, but on Windows.
[3977.40 → 3982.62] Well, I'll go next to a project that I love, and I'm thankful for.
[3982.88 → 3988.58] And one that probably everybody has heard of, but still worth shout-outs, all the shout-outs,
[3988.72 → 3996.80] because Jack Music's semantic UI is a beautiful system akin to a bootstrap or a foundation,
[3996.80 → 4002.68] but one that just really speaks to my both design sensibilities and really just the way that you use it
[4002.68 → 4004.98] once you get used to the semantics of it.
[4004.98 → 4014.92] It just allows for very quickly cranking out admins and prototypes and stuff like that in a way that saved me lots of time
[4014.92 → 4019.68] and also made me look not too bad with clients and whatnot over the years.
[4019.68 → 4024.88] So if you don't know about semantic UI, you probably do though, because it's one of those, you know,
[4025.12 → 4027.24] 100,000 stars on GitHub type of projects.
[4028.14 → 4029.00] Check that out.
[4029.26 → 4032.26] And thanks, Jack, for all the work you put into it.
[4032.32 → 4033.08] I know he has.
[4033.88 → 4041.88] He's been on the show a few times, and he has a ton of people bugging him all the time about bugs and fixes and improvements.
[4041.88 → 4047.36] And it's like a huge, massive undertaking and a huge boon to the open source community.
[4047.56 → 4048.94] So check out semantic UI.
[4049.86 → 4051.72] Surprisingly, I had not heard of that.
[4051.88 → 4054.14] I've been disconnected from the front end space.
[4054.64 → 4055.94] So there you go.
[4057.16 → 4058.76] Adam, is it my turn?
[4059.28 → 4060.12] It is your turn.
[4060.78 → 4062.54] Well, it's a little meta here.
[4062.54 → 4074.32] I'm going to mention our transcripts because it was a participant in Hacktoberfest and then also 24 pull requests.
[4074.86 → 4082.58] So if you go to GitHub.com slash the changelog slash transcripts, we have all of our episode transcripts in Markdown format, open source,
[4082.72 → 4090.20] meaning that not only can you read them, you know, as a Markdown file if you wanted to, but you can contribute to them.
[4090.20 → 4097.16] So that means that if you want to help clean up unintelligible, which is super easy to find just by literally searching the repository for unintelligible,
[4097.88 → 4104.72] and you want to listen to episodes and hack, you can easily contribute to open source by fixing those kinds of things.
[4104.72 → 4108.58] And I love that they're open source because that was a dream of mine.
[4108.68 → 4116.68] And Jared, you made it a reality, which I think, you know, it pays in spades when you don't really consider the impact of it.
[4116.68 → 4122.02] But like, you know, rewinding, you know, if we didn't do it like this, you know, we would miss out on community.
[4122.46 → 4128.18] And Chris48S and many others have submitted pull requests to improve these transcripts.
[4128.18 → 4129.64] And I think it's just it's phenomenal.
[4129.70 → 4131.72] We got 28 closed pull requests.
[4133.18 → 4134.20] None of them by me.
[4134.50 → 4135.66] None of them by Jared.
[4136.00 → 4136.48] You know what I mean?
[4136.48 → 4138.94] Does that mean people actually listen to this stuff?
[4139.12 → 4139.44] Yeah.
[4140.06 → 4141.46] I'm going to just say a few names.
[4141.46 → 4152.76] You got Jay Dillard, Share ANG, some usernames, of course, Shari Hunt, Chris48S, Dot, and I Met, Matt Warren.
[4152.86 → 4155.36] These are all obviously usernames.
[4155.60 → 4156.16] Sure, cool.
[4157.54 → 4158.84] Which was a self-correction.
[4158.98 → 4160.04] That was a Go Time episode.
[4160.50 → 4166.04] Commando Hacker, Commando Hacker, Birdies, sorry.
[4167.54 → 4168.82] Mira can, many others.
[4168.82 → 4172.06] It's KCW, listener at Go Time here in chat, obviously.
[4172.50 → 4172.94] Maybe this time.
[4172.96 → 4173.34] I'm not sure.
[4173.58 → 4174.16] Usually is.
[4175.14 → 4176.12] A couple others.
[4176.36 → 4177.64] Peter Mortensen.
[4178.10 → 4181.56] But the point is, is that we ship these shows.
[4182.00 → 4187.06] We transcript them so that they're accessible to anybody as best we can.
[4187.12 → 4190.48] Not only in audio format, but also type format, text format.
[4190.90 → 4196.98] And, you know, we have a human behind the scenes, Alexander, who helps us make sure that
[4196.98 → 4200.78] every single episode we produce is transcribed to make it accessible.
[4201.30 → 4202.58] But he's not perfect.
[4202.94 → 4205.44] And the community can step in and help.
[4205.64 → 4206.40] And we appreciate it.
[4207.00 → 4212.32] You know, I think even outside accessibility, it's nice for discoverability, right?
[4212.32 → 4213.02] Reading along.
[4213.54 → 4214.90] You know, Command F.
[4214.90 → 4218.04] It doesn't hurt for SEO for sure.
[4218.18 → 4220.54] But I'll tell you where it really helps is in the off chance.
[4220.62 → 4221.72] And this happens once in a while.
[4222.28 → 4226.82] That somebody submits one of our shows to Hacker News, which is just the loveliest group of
[4226.82 → 4228.06] hackers in the world.
[4228.34 → 4228.50] Yes.
[4228.50 → 4230.36] Every single time.
[4230.40 → 4230.90] They're so sweet.
[4230.90 → 4233.24] Somebody would say, you know, TLD, listen.
[4233.58 → 4233.96] TLD.
[4234.04 → 4234.38] I don't know.
[4234.70 → 4236.00] They're like, why aren't there transcripts?
[4236.06 → 4236.32] Blah, blah, blah.
[4236.40 → 4237.42] They've always complained.
[4237.48 → 4238.34] I wouldn't just read this.
[4238.38 → 4238.98] I don't want to listen.
[4239.08 → 4239.70] It takes too long.
[4240.08 → 4245.38] And finally, finally, we can hear silence as there's a transcript right there for you.
[4245.60 → 4247.00] And there's nothing to complain about.
[4247.08 → 4249.06] That's my own personal enjoyment.
[4249.42 → 4249.80] Yes.
[4250.62 → 4251.94] They can complain about the content, finally.
[4252.62 → 4253.04] Mm-hmm.
[4253.18 → 4256.66] And on that note, I got to go in like one.
[4256.66 → 4258.32] It's a tight close of the show.
[4258.72 → 4263.94] But Eric, it wouldn't be a go time or a changelog if you didn't take us out.
[4265.26 → 4266.48] If I didn't take us out?
[4266.62 → 4267.42] What do you normally say?
[4267.50 → 4269.66] You normally say, thank you, everybody, for...
[4270.20 → 4273.48] Well, thank Brian and me for being on the show.
[4274.52 → 4279.42] Real quick, let's give a shout-out to the missing voice on the show, Carissa.
[4279.52 → 4280.36] Yes, of course.
[4280.44 → 4282.96] Who is an awesome panellist on go time.
[4283.22 → 4283.76] Good job, Jared.
[4283.90 → 4285.98] Unfortunately, not here today, but we're thankful for her.
[4285.98 → 4289.46] She's a pillar in the Go community and the open source community.
[4289.56 → 4292.02] She's been a huge part of our community for a long time.
[4292.56 → 4294.46] And Carissa, we love you, and we miss you today.
[4295.24 → 4296.74] And we hope that she feels better.
[4297.90 → 4299.16] Okay, now you can take us out.
[4299.62 → 4299.90] Okay.
[4300.22 → 4302.20] So thank you, everybody, for being on the show.
[4302.78 → 4306.78] Love the fact that Jared and Adam came in and took over.
[4307.36 → 4311.58] So it was kind of fun, especially getting to talk about something that Brian and I have worked on recently.
[4312.72 → 4314.44] Huge thank you to all of our listeners.
[4314.44 → 4315.86] You keep the show going.
[4316.42 → 4318.88] Definitely share the show with friends and coworkers.
[4319.80 → 4324.54] You can find us at gotime.fm or at gotime.fm on Twitter.
[4325.10 → 4332.20] If you want to be on the show, have suggestions for topics, hit us up on GitHub.com slash gotime.fm slash ping.
[4332.84 → 4334.44] And I think I covered everything.
[4334.44 → 4341.72] We've got a short holiday break, so we may skip a couple of episodes for the holidays, but we'll see you in a couple of weeks.
[4342.16 → 4343.02] See you, everybody.
[4343.34 → 4343.80] Thank you.
[4344.04 → 4344.34] Bye.
[4344.54 → 4345.08] Bye, everybody.
[4345.46 → 4345.80] Bye.
[4345.80 → 4347.80] Bye.
[4347.80 → 4348.68] All right.
[4348.68 → 4350.80] That's it for this episode of Go time.
[4350.94 → 4353.76] Tune in live on Thursdays at 3 p.m.
[4354.12 → 4354.58] U.S.
[4354.70 → 4357.02] Eastern at changelog.com slash live.
[4357.56 → 4360.28] Join the community and Slack with us in real time during the shows.
[4360.38 → 4362.66] Head to changelog.com slash community.
[4363.18 → 4363.92] Follow us on Twitter.
[4364.24 → 4365.82] We're at gotime.fm.
[4366.26 → 4368.62] Special thanks to Vastly, our bandwidth partner.
[4369.08 → 4370.46] Head to fastly.com to learn more.
[4370.90 → 4371.68] Also, Linde.
[4371.80 → 4374.20] We host everything we do on Linde servers.
[4374.60 → 4376.46] Head to linode.com slash changelog.
[4376.88 → 4378.94] Go time is edited by Jonathan Young blood.
[4378.94 → 4382.62] And the theme music for Go time is produced by the mysterious Break master Cylinder.
[4383.02 → 4384.08] We'll see you again next week.
[4384.36 → 4384.94] Thanks for listening.
[4395.82 → 4402.60] Remember, pronounce, pronounced, Burr A, ertime.
[4402.70 → 4403.56] Bye.
[4403.56 → 4404.76] You got to see you again next week.
[4404.82 → 4405.32] Take care.
[4405.48 → 4408.34] See you again next week.
[4408.44 → 4411.16] Combine, Poor techno, Burr ALO, Brunt, Myself.
[4411.42 → 4412.60] Pepper is working.
[4412.60 → 4413.94] You got to see you again next week.
[4413.94 → 4416.64] Burr to find out through, obil, contributed, refy, видели, registration or,
[4416.66 → 4417.78] are fans and logon.
[4418.20 → 4419.72] Besides being pushed by the new reality track,
[4420.00 → 4422.82] I spent at the 때는 a place that police neckline has though
[4422.94 → 4424.44] to be aенная court Smackdown,
