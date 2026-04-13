[0.00 → 2.04] Data prep is so challenging.
[2.18 → 4.60] It's probably the most challenging part of a project.
[4.96 → 8.96] And it's oftentimes because of the sheer volume of data that is required.
[9.36 → 15.20] Oftentimes, really highly paid and talented data scientists are managing projects in a
[15.20 → 19.48] highly manual way where their time and talent just isn't being utilized.
[20.08 → 24.18] And I'd say that's probably one of the biggest challenges we hear data scientists describe
[24.18 → 28.94] is that they're spending too much time manually managing project minutia.
[28.94 → 35.58] Oftentimes, it's the use of automation tools and projects management platforms that can
[35.58 → 43.22] help them to kind of refocus their energies on higher level priorities and allow the application,
[43.40 → 49.16] the software application or the platform to automate a lot of the workflow and allow other
[49.16 → 52.12] team members to manage a higher percentage of the workflow.
[58.94 → 68.90] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive
[68.90 → 70.22] and accessible to everyone.
[70.62 → 71.40] Subscribe now.
[71.58 → 75.38] If you haven't already, head to practicalai.fm for all the ways.
[75.74 → 80.72] Special thanks to our partners at Vastly for delivering our shows superfast to wherever
[80.72 → 81.36] you listen.
[81.70 → 83.52] Check them out at fastly.com.
[83.52 → 85.94] And to our friends at fly.io.
[86.28 → 89.88] We deploy our app servers close to our users and you can too.
[90.24 → 92.14] Learn more at fly.io.
[98.14 → 101.44] Well, welcome to another episode of Practical AI.
[101.82 → 103.52] This is Daniel Whiten ack.
[103.64 → 106.82] I'm a data scientist with SIL International.
[106.82 → 112.24] And I'm normally joined by Chris Benson, who is a tech strategist at Lockheed Martin, but
[112.24 → 117.62] he's doing great tech strategy things and travelling as part of those things.
[117.62 → 123.98] So he won't be joining today, but I've got a really, really wonderful guest and topic to
[123.98 → 124.80] talk about today.
[124.94 → 131.84] We've sort of been diving deep into a number of modelling related things in terms of stable
[131.84 → 134.00] diffusion and various things coming out.
[134.00 → 140.02] And I think it'd be good to kind of shift and talk about, again, we're practical AI.
[140.24 → 144.82] So talking about some practical data related things would be worthwhile.
[144.82 → 150.82] And I'm really pleased today to have the CEO of Ellis with me, Mark Christensen.
[151.30 → 159.68] His expertise is all in the area of data labelling and workflows around that and bespoke data processes.
[160.10 → 161.54] So welcome to the show, Mark.
[161.58 → 162.42] It's great to have you.
[162.94 → 163.34] Thanks, Dan.
[163.34 → 164.02] Glad to be here.
[164.02 → 164.54] Yeah.
[164.84 → 171.86] Well, could you give us a little bit of a background about how you kind of got interested
[171.86 → 180.30] in this space of data labelling and kind of producing custom training data sets and eventually
[180.30 → 182.76] kind of built a business around that?
[182.84 → 183.88] How did that happen?
[184.32 → 186.82] We didn't come out of a data science discipline, actually.
[186.82 → 188.10] We came out of healthcare.
[188.10 → 197.38] And we've spent the last 17 years managing healthcare data at scale, specifically in the area of dictation and transcription.
[197.38 → 200.12] So kind of entirely different field.
[200.12 → 204.76] But the thing we had in common was managing large amounts of data at scale.
[204.76 → 208.38] In healthcare, what we would do is we would record audio.
[208.38 → 219.18] And for 17 years, we recorded audio from healthcare providers and then move that audio through an enrichment workflow, which just essentially was transcription.
[219.18 → 228.68] So we'd have skilled medical transcriptionists in the States and around the world who would take the audio and transcribe it into the completed healthcare note.
[228.68 → 236.94] And a few years ago, we met with a friend of ours who was an owner of an NLP company, and he really liked our platform.
[237.10 → 240.26] We happened to be working with him on a speech recognition project.
[240.92 → 246.16] And we really have a need for this in managing trading data for NLP workflows.
[246.84 → 251.08] And so that launched a discovery process that took about two years.
[251.08 → 257.10] And we investigated the use case and determined that there was really a really neat fit.
[257.10 → 265.80] And so we modified the application for the next two years and then launched our training data services workflow called Well AI.
[266.44 → 267.86] So that's how we got into it.
[268.22 → 269.12] That's fascinating.
[269.12 → 286.82] And I know data specifically in the healthcare space, there's some very interesting restrictions and very specific processes that you have to make sure that you're following in that healthcare space.
[286.82 → 304.66] I'm wondering if you think that that perspective on data and like the security, the compliance things around that data, did that sort of shape maybe how you think about handling data for some of these use cases?
[304.82 → 305.74] Any thoughts there?
[306.34 → 308.86] Yeah, man, that's a great question.
[308.86 → 310.40] And you're totally right.
[310.40 → 314.46] Data security is so paramount in healthcare.
[315.10 → 326.08] And my colleague at the NLP company cited that as one of the specific reasons why the workflow that we had in healthcare was a great overlay for data training.
[326.56 → 327.84] The data has to be audited.
[328.52 → 331.44] So data should have a couple of different audit trails on it.
[331.54 → 335.06] Data should be encrypted both in transit and in rest.
[335.06 → 340.72] Data shouldn't reside on the devices of people that are involved in data labelling.
[340.90 → 348.08] So all those things were just a perfect fit and carry over between our healthcare workflow and an AI workflow.
[348.36 → 349.00] Yeah, you're right.
[349.34 → 349.68] Interesting.
[349.92 → 350.12] Yeah.
[350.62 → 363.48] I'm wondering as you, maybe it's as you talk to this NLP colleague or as you've worked with clients, you know, around the world working on data labelling projects.
[363.48 → 370.34] From your perspective, like how are data scientists most often labelling their data these days?
[370.52 → 375.54] And where do they encounter challenges because of how they're approaching data labelling?
[375.54 → 376.18] Yeah.
[376.18 → 396.62] I mean, the greatest challenge we always hear, and it's an obvious one, is about getting data that's accurate enough to improve the model, especially in specialty use cases or, you know, let's say new language modelling where a click worker approach doesn't hold up.
[396.62 → 426.60] It just doesn't work as well.
[426.62 → 442.94] For our purposes and the approach that we took, we decided that rather than commoditize the role of the editor or the annotator, we'd invest more in training and compensating our labels as a means of building long-term relationships.
[442.94 → 455.54] And for us, we found that's an essential part of maintaining the kind of the consistency of the data quality and making sure that the data quality remains at the accuracy levels our clients require.
[455.54 → 463.92] And that's to be able to be able to have those relationships with annotators that we can trust and that aren't just commoditized relationships.
[464.52 → 465.02] Interesting. Yeah.
[465.02 → 477.88] So have you encountered cases where maybe clients come to you, and they say, hey, we tried to throw up like a crowdsourced task and get a bunch of labels.
[477.88 → 507.86] We invested a lot in that.
[507.88 → 508.90] Yeah.
[508.90 → 509.88] Yeah.
[509.88 → 510.88] Yeah.
[510.88 → 511.88] Yeah.
[511.88 → 512.88] Yeah.
[512.88 → 513.88] Yeah.
[513.88 → 514.88] Yeah.
[514.88 → 517.88] The commoditization of the annotation workforce is, I think it can be a project killer.
[517.88 → 522.88] And a very high percentage of projects that launch stall and never complete.
[522.88 → 524.88] And that's one of the key reasons.
[524.88 → 531.90] We've talked with companies that try that approach and they wind up iterating the data
[531.90 → 538.48] so many times to try to get an accurate set of data that they can use that they ultimately
[538.48 → 546.84] wind up going to a more bespoke approach where the teams are more hand-picked and more highly
[546.84 → 552.00] trained, even though the costs are higher, in order to finally wind up with a data set that
[552.00 → 558.62] is useful. So yeah, I think that is one of the key problems that plague data aggregation projects,
[558.62 → 564.72] and that is to wind up with a clean set of data that can be done kind of on time and on budget.
[565.28 → 572.92] Yeah, I know, Mark, that in our projects, and we've done some speech projects as well,
[573.22 → 580.36] we've struggled with this also in terms of the data quality. And I remember in one case,
[580.36 → 588.54] like really, we were saying, well, we need five labels for each sample because like the variability
[588.54 → 595.48] between labels is such that like we need either a majority vote or we need to analyze how much they
[595.48 → 602.32] agree one label or to the other or something. And of course, that gets really expensive over time.
[602.84 → 609.24] Could you speak a little bit to like you mentioned this training, focusing on training and kind of
[609.24 → 618.28] bringing in this like upskilling these data labels? What does training annotators look like in your
[618.28 → 625.54] projects? And what maybe have you learned about what's important as you are training data labels?
[625.92 → 631.20] Yeah, I recently did a paper called Improving Model Accuracy Through Better Translation. And it was
[631.20 → 637.90] really just an attempt to lay out some tips for translating source text for natural language processing
[637.90 → 643.82] models. And one of the items I mentioned, and it's something that we've seen as we worked with
[643.82 → 649.90] teams around the world doing language projects, is that it's important for the editors and those
[649.90 → 657.22] involved to understand the use case. And that might seem like it's perhaps too much information or an
[657.22 → 664.96] unnecessary amount of information to share with the editors or the annotators. But once they understand
[664.96 → 670.70] the project description, or I should say the better they understand the project, oftentimes it really
[670.70 → 677.54] does translate into higher quality data. And so I encourage companies to share that information with
[677.54 → 685.26] annotators so that they are more vested in the work that they're doing. And as an example of how a project
[685.26 → 691.44] description might be written up as part of the guidelines for the annotators, it might be something
[691.44 → 697.62] like, this project involves, and this I'll just cite briefly a paragraph out of the document.
[698.08 → 703.16] This project involves training a software application to automatically assist call centre agents
[703.16 → 708.92] with their tasks and increase their efficiency. For example, if the customer says, I have a warranty issue,
[709.56 → 714.52] the agent's software application can respond by automatically opening the customer's warranty clause,
[715.22 → 718.36] reducing the time required for the agent to assist the customer.
[718.36 → 723.72] The translation project consists of a set of English language scripts that reflect some of the typical
[723.72 → 730.18] conversations that occur between call centre agents and customers. The purpose of this project is to
[730.18 → 735.98] translate those scripts into a target language in order to add NLP-driven process automation
[735.98 → 741.54] into the call centre's workflow, thereby adding new efficiencies to the agents and company.
[741.54 → 748.26] And so by giving that kind of insight and detail to the translators and the editors,
[748.66 → 755.06] it enables them to have more buy-in to the project and have a better understanding of how their work is
[755.06 → 755.80] going to be used.
[755.96 → 765.74] I think that there's a lot of content about hyped AI data science things, but in reality, what people are
[765.74 → 772.32] really wanting more content around is this sort of practical concerns of like, hey, my data labelling
[772.32 → 778.68] isn't actually working, right? Like how, how can I fix that problem? And so I think there's a
[779.38 → 785.10] from my perspective, at least there's an eagerness for this sort of conversation where people are
[785.10 → 791.38] actually, they have a lot of the other, but they don't have enough like practicality in their,
[791.38 → 797.88] in their content. So I, I think that that bodes well for the sort of conversation from my perspective.
[798.60 → 803.96] Okay. That's encouraging to know because we're the guys on the process side, you know, so the sexy
[803.96 → 809.58] work is being done by you and the data scientists. We're more of the guys down the boiler room.
[809.96 → 810.44] Yeah.
[810.58 → 817.54] You know, we're kind of the, the operations team that makes the process happen, but doesn't
[817.54 → 821.36] necessarily know a lot about the data science side of it.
[821.86 → 828.42] Yeah. I think that in reality though, the data side is what is driving things. So yeah, I think
[828.42 → 828.96] that's good.
[828.96 → 829.12] Yeah.
[847.54 → 876.48] Well, Mark,
[876.48 → 881.52] We've talked a little bit about the importance of training annotators.
[881.74 → 886.80] We've talked a little bit about kind of specific data concerns around health care and other things.
[886.96 → 897.92] I'm wondering from your perspective, since you're really plugged into the area around like how people are managing their data workflows, how they're managing their data labelling.
[898.16 → 905.78] From your perspective, what does the current data labelling sort of annotation and tooling landscape look like?
[905.78 → 910.24] What choices do people have, and what does that landscape look like right now?
[910.66 → 914.28] From my perspective, the landscape seems to be rapidly changing.
[914.54 → 918.68] But I would say that off-the-shelf models are being used more often.
[919.60 → 926.12] They continue to improve, and they're used either, I'd say, as is or with in-house tuning.
[926.12 → 936.44] The projects we see and the projects we're getting more involved in are kind of specialty applications where off-the-shelf models aren't accurate enough, or they don't exist.
[936.68 → 951.72] And cases might be places like medical documentation labelling, sentiment and intent projects that have a highly customer-specific language or vocabulary that can't be picked up by off-the-shelf models.
[951.72 → 962.86] And in specialty models, I'd say training data is needed in cases where unique vocabularies warrant kind of highly specialized bespoke model tuning.
[962.86 → 980.00] An example might be gathering business intelligence from call centre interactions, for example, where the client is seeking to obtain business intelligence through an NLP automation process, and they need a model to be custom-tuned.
[980.20 → 983.64] And they need the model to be custom-tuned to meet their business objectives.
[983.64 → 987.26] Another area would be, I guess, new language modelling.
[987.72 → 998.02] And that's exciting to me and encouraging because we're starting to see an uptick in interest in other major world languages where models don't exist in a production environment.
[998.30 → 1012.66] On the tooling side, I'd say we've seen companies both big and small relying on a hybrid of in-house data labelling and in-house plus click worker driven labelling and fully external third-party labelling.
[1012.66 → 1021.42] But what we're not seeing is AI companies that have systems in place to manage those different approaches in a cohesive way.
[1022.52 → 1024.90] So there's a lot of manual aggregation.
[1025.04 → 1031.02] There's a lot of one-off coding that gets done to unify the results from those hybrid sources.
[1031.62 → 1039.56] So to answer your question on the tooling side, this is one area where the tooling is broadly not keeping pace with the growth of the industry.
[1039.56 → 1043.48] And I know it's like one thing, and this comes from personal experience.
[1043.48 → 1048.60] It's one thing to get data labelled, like gather a label.
[1048.86 → 1056.32] It's another thing to develop like a workflow around that that's integrated into your systems, integrated into your backend.
[1056.32 → 1073.68] What do you think are the challenges facing data scientists around this workflow side of things and the bespoke sort of things that they have to do to integrate data labelling into the sort of wider set of things that they're doing?
[1074.10 → 1074.24] Yeah.
[1074.44 → 1076.50] Data prep is so challenging.
[1076.64 → 1079.08] It's probably the most challenging part of a project.
[1079.08 → 1083.64] And it's oftentimes because of the sheer volume of data that is required.
[1083.64 → 1102.66] And what we see not just at small companies, but even at big companies is that highly skilled and oftentimes really highly paid and talented data scientists are managing projects in a highly manual way where their time and talent just isn't being utilized as efficiently as it could.
[1102.66 → 1109.22] And senior data scientists are doing things like vetting samples from annotators and doing quality scoring on annotators.
[1109.22 → 1119.24] And I'd say that's probably one of the biggest challenges we hear data scientists describe is that they're spending too much time manually managing project minutiae.
[1119.24 → 1143.80] And oftentimes it's the use of automation tools and projects management platforms that can help them to kind of refocus their energies on higher level priorities and allow the application, the software application or the platform to automate a lot of the workflow and allow other team members to manage a higher percentage of the workflow.
[1144.32 → 1146.88] So I think that's one of the things we're seeing.
[1146.88 → 1154.66] And along with that, how does Ellis specifically approach the data labelling problems that you've described?
[1154.80 → 1156.28] We've talked about sort of workflows.
[1156.52 → 1161.32] We've talked about the custom setups that are needed for a certain task.
[1161.44 → 1163.14] We've talked about a variety of things.
[1163.30 → 1169.62] How has that filtered down into your approach specifically and the approach that Ellis takes?
[1169.62 → 1170.24] Yeah.
[1170.58 → 1180.16] Workflow platforms are all about moving off of spreadsheets and manual processes into processes that scale better.
[1180.60 → 1181.28] That's what we do.
[1181.40 → 1183.38] We're focused on the production process.
[1183.38 → 1193.80] Everything from training and managing the skilled labour to meeting deliverables on time and at quality levels that clients expect.
[1194.18 → 1196.04] I mean, keeping projects on budget.
[1196.24 → 1202.82] Those are all things that training data services companies like we do and that we bring to the table.
[1202.82 → 1206.00] Our focus is on making complex workflows easier.
[1206.20 → 1215.76] And another part, this was interesting that one of our clients said to us one time is that they needed all the stakeholders at the company to be able to see what was going on with the project.
[1215.76 → 1219.10] And the platform, our platform enabled them and other platforms too.
[1219.20 → 1221.56] It enables stakeholders to do that.
[1222.00 → 1227.28] And there are all kinds of stakeholders at the production level and the commercial level for projects.
[1228.00 → 1236.64] Because projects on the commercial side, you know, they're typically done on the request of a client and in service to a client.
[1237.16 → 1241.76] And so all kinds of different people outside the data science team are involved.
[1241.76 → 1247.38] You know, the sales team, the ops team, the procurement team, the quality assurance team.
[1247.90 → 1250.18] And everybody needs to know what's going on.
[1250.24 → 1251.94] They want to see if the project's on budget.
[1252.08 → 1254.26] They want to see if the project's on time.
[1254.66 → 1259.04] They want to see if the quality thresholds that the client has set are being met.
[1259.42 → 1262.82] And so a platform gives everybody that kind of visibility.
[1262.82 → 1272.94] And I really enjoy and appreciate being able to do that for a company because it does then keep all the stakeholders in the loop.
[1273.16 → 1279.90] At the same time, it allows the data science team to not get bogged down managing minutia manually.
[1280.46 → 1283.88] So that's one of the neat things that we like to deliver.
[1283.88 → 1290.10] And then on the services side, the approach that is always about managing the workforce successfully.
[1290.10 → 1312.08] And, you know, success in data sciences and in projects like this is measured in being able to deliver a project on time and on budget and at the accuracy levels that have been determined or set by the client and by the service provider as being the goals or the project's objectives.
[1312.08 → 1323.78] An example of this kind of how this can backfire is when service providers like us enter, let's say, a new language or a new project area.
[1324.30 → 1333.40] And, you know, maybe their client has come to them and said, you know, can you do this, or can you do a project in data labelling in this language?
[1334.06 → 1338.70] And, of course, the knee-jerk reaction is always, sure, we can do that.
[1338.70 → 1352.74] But if saying we can do that involves hiring a third-party vendor in that target country or target language to do the project, and it's done in a scramble, it can really backfire.
[1352.74 → 1371.32] And so hiring a third-party vendor in cases like that can result in kind of black box approach where you're unable to adequately measure quality and where you're unable to adequately manage deliverables so that projects wind up running late or projects are delivered with poor quality data.
[1371.32 → 1401.30] And then you're left kind of a third-party data.
[1401.32 → 1402.62] For that labelling effort.
[1403.10 → 1410.20] And that way, even though it's going to take us longer and the cost might be higher and there are cost sensitivities that are realities.
[1410.46 → 1421.16] But the truth is, if you're using a third-party vendor and working out of a black box, chances are you're not going to be able to deliver the project on time and at cost.
[1421.16 → 1424.78] And so your costs and timeline are going to be affected anyway.
[1425.26 → 1442.52] And so we've opted for taking an approach that's more expensive to our clients, but that ultimately delivers projects with a higher quality and consistently higher quality data that are on time that meet the turnaround deliverables, even though the price might be a little higher.
[1442.52 → 1451.82] Yeah, and I think that's a perfect and practical advice for the whole community that's trying to do a variety of these data labelling projects.
[1451.82 → 1465.02] Is really kind of at the start of these data labelling projects, not only thinking about gathering samples, but thinking about how is your workflow going to be managed, and how are your annotators going to be trained?
[1465.02 → 1480.70] Because thinking about that stuff up front and taking time or spending more money on getting that in place from the start might actually save money in the longer term if you're not doing as many iterations of labelling, right?
[1480.70 → 1493.62] If you start, and you do a bunch of labelling, and then you don't get the quality that you need, or you get some sort of unexpected biases or other things in your data, that could cause more problems down the line.
[1493.62 → 1523.52] And one of the things, maybe this isn't a specific, I guess it could lead to specific quality issues, but one of the things that is hard for me as a technical introvert person, who's not maybe the most people oriented person in the world is thinking about all the team dynamics that happen on a data labelling project and setting up like maybe a disparate and kind of distributed set
[1523.52 → 1528.52] of labels and vendors for a data labelling project.
[1528.52 → 1535.52] How can the problems associated with this sort of dynamics be addressed in this kind of online distributed labelling environment?
[1535.52 → 1537.52] Yeah, you're totally right.
[1537.52 → 1551.52] There are inherent challenges in managing an online workforce, but many of those can be mitigated through kind of well-developed, robust workflow application.
[1551.52 → 1560.52] You know, things like centralized controls, giving managers total visibility to what's happening in the workflow at any given moment.
[1560.52 → 1569.52] You know, the status of data objects as they're moving through the workflow and how you're doing against your timeline for deliverables.
[1569.52 → 1573.52] You know, those are the kinds of things that software is perfect at managing.
[1573.52 → 1581.52] As I mentioned earlier, we've seen cases even with really large companies where pretty complex projects were still being managed on a spreadsheet.
[1581.52 → 1586.52] And when you're doing that, there's almost no ability to manage the workflow effectively.
[1586.52 → 1591.52] Well, Mark, given the sort of team dynamics that can happen that we've been talking about, the sort of
[1591.52 → 1597.52] variety of tasks that Ellis is exploring and other people exploring in the workflow,
[1597.52 → 1603.52] the way that we've been talking about is that we've been talking about the sort of
[1603.52 → 1609.52] variety of tasks that Ellis is exploring and other people exploring in the workflow.
[1609.52 → 1627.52] From like standardized machine learning tasks to more custom ones.
[1627.52 → 1641.52] I'm wondering what sort of like would you say about kind of proper ways to set up maybe manual and or annotated QA type of workflows associated with your data labelling?
[1641.52 → 1643.52] Well, I can tell you a little bit about what we do.
[1643.52 → 1647.52] The first is to establish the ground truth version of the data object.
[1647.52 → 1650.52] And for all data objects as they're moving through the workflow.
[1650.52 → 1658.52] And once we establish the ground truth data object, then we're able to measure the distance between that and the work that the editors are doing.
[1658.52 → 1661.52] And that helps to generate a lot of different metrics for us.
[1661.52 → 1663.52] You know, who needs additional training?
[1663.52 → 1665.52] How pay might be affected?
[1665.52 → 1672.52] How our costs are effective if data objects are moving through the QA workflow more for some editors than others?
[1672.52 → 1678.52] The second thing that we do is a multi-level QA workflow so that work gets automatically routed.
[1678.52 → 1687.52] And that could be in cases where we've got new hires or maybe editors are being flagged via our auto check process for certain error types.
[1687.52 → 1701.52] And then thirdly, we run an error script that dynamically checks against the known error list so that those items are routinely kind of recycled through the workflow to be re-edited and re-QA.
[1701.52 → 1704.52] So those are kind of some of the typical things we do.
[1704.52 → 1712.52] Judgments, of course, and multiple judgments on data objects is really important to make sure that using multiple layers of judgments is also important.
[1712.52 → 1716.52] And we do that through the QA workflow process as well.
[1716.52 → 1724.52] It's been extremely helpful for me to think through some of the dynamics and the workflows associated with data labelling.
[1724.52 → 1728.52] I think it's its extremely practical and very useful.
[1728.52 → 1742.52] I'm wondering, as you kind of continue to be more and more involved in this space of data labelling and interacting with clients in the data science and AI space, what excites you about the future of sort of data science and AI practice?
[1742.52 → 1750.52] And, you know, what maybe within that, what could easier data labelling enable in the longer term?
[1750.52 → 1759.52] Well, when you look at the number of data sets that have been developed and models that have been developed so far, it's overwhelmingly all English based.
[1759.52 → 1764.52] And in that regard, probably largely focused on the U.S. market.
[1764.52 → 1770.52] And, you know, we're overwhelmingly the largest economy in the world, so that that makes sense that it would be that way.
[1770.52 → 1788.52] But what I'm excited about is seeing the tools and expertise that have been developed in English modelling to now be used in other major world languages and specifically in developing economies where AI can be used to help to develop economies move forward.
[1788.52 → 1808.52] All of those nations are generating customer and employee experience data in the form of things like, you know, like customer behaviour data and online reviews and, you know, sentiment and intent data and medical data, things that are in unstructured format where AI can be used beneficially.
[1808.52 → 1821.52] Well, Mark, I'm really happy that you brought up this side of the impact of data and NLP across the world's languages, as our listeners will know, I'm I'm very passionate about this topic.
[1821.52 → 1825.52] And I'm really excited any time we get to talk about that.
[1825.52 → 1828.52] It's something that excites me for the future as well.
[1828.52 → 1838.52] I really appreciated you taking time out of your work with Ellis to help us parse through some of these data labelling challenges and the workflows associated with them.
[1838.52 → 1850.52] And, yeah, really, really appreciate you taking time and looking forward to continuing our conversations over the coming months as I hit my own data labelling issues.
[1850.52 → 1852.52] So thanks, Dan, very much.
[1852.52 → 1853.52] I really enjoyed it.
[1853.52 → 1863.52] All right.
[1863.52 → 1865.52] That is our show for this week.
[1865.52 → 1867.52] If you dig it, don't forget to subscribe.
[1867.52 → 1870.52] Head to practicalai.fm for all the ways.
[1870.52 → 1876.52] And if practically I have benefited your life, pay it forward by sharing the show with a friend or colleague.
[1876.52 → 1880.52] Word of mouth is the number one way people find shows like ours.
[1880.52 → 1889.52] Thanks again to Vastly for fronting our static assets to fly.io for backing our dynamic requests to Break master Cylinder for the beats and to you for listening.
[1889.52 → 1890.52] We appreciate you.
[1890.52 → 1891.52] That's all for now.
[1891.52 → 1893.52] We'll talk to you again on the next one.
[1893.52 → 1905.52] We'll see you again on the next one.
[1905.52 → 1906.52] Game on.
