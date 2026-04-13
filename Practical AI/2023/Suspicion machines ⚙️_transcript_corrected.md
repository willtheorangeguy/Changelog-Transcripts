[0.00 → 8.58] Welcome to Practical AI.
[9.16 → 18.72] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies are changing the world, this is the show for you.
[19.18 → 24.62] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you listen.
[24.88 → 26.70] Check them out at Fastly.com.
[26.70 → 31.96] And to our friends at Fly, deploy your app servers and database close to your users.
[32.40 → 36.02] No ops required. Learn more at fly.io.
[42.92 → 46.10] Welcome to another episode of Practical AI.
[46.48 → 51.56] This is Daniel Whiten ack. I am the founder and CEO at Prediction Guard.
[51.68 → 55.04] We have some really exciting stuff to discuss today.
[55.04 → 66.80] So thankful to have my guests with us today because there's a lot of talk about the dangers of AI or potential risk associated with AI, which we've talked about on the show.
[66.96 → 80.32] But I think maybe that kind of misses some of the actual real world problems that are happening with deployed machine learning systems that maybe have been going on for longer than some people might think.
[80.32 → 91.66] And maybe we can learn some things from those deployed machine learning systems that would help us create better and more trustworthy AI systems moving towards the future.
[92.08 → 103.42] So I'm really pleased to have with me today Justin Braun, who is a data journalist at Lighthouse Reports, and Gabriel Geiger, who is an investigative journalist at Lighthouse.
[103.42 → 106.02] Thank you both for joining me so much.
[106.46 → 107.16] Thanks for having me.
[107.52 → 108.58] Thanks so much for having us.
[109.08 → 109.76] Yeah, yeah.
[109.90 → 121.12] Well, like I mentioned, I kind of teed us up to talk a little bit about maybe risks or kind of downsides of deployed machine learning systems.
[121.34 → 129.06] And you both have done amazing journalism related to what you've kind of titled here suspicion machines.
[129.06 → 135.72] And I think it would be worth before we kind of jump into all the details of that, which is just incredibly fascinating.
[135.94 → 146.40] If you could give us a little bit of context for both what you mean by suspicion machines and how this topic came across your desks, and you started getting interested in it.
[146.94 → 147.92] Sure, I can start with that.
[147.92 → 159.70] I mean, the reason that we chose the suspicion machine as a title for our series is its kind of a driving metaphor for what these specific machine learning models are doing within the welfare context.
[160.02 → 168.34] So a while ago, we wanted to investigate the deployment of machine learning in one specific area, but we're not sure which one yet.
[168.34 → 175.08] So in the US, there's been a lot of reporting about the use of machine learning or predictive risk assessments within the criminal justice system.
[175.40 → 183.42] Also in facial recognition and us over in Europe looked at that reporting and noticed that there's a big lack of it over here in Europe.
[183.42 → 193.20] And so we were exploring different realms and settled on looking at welfare systems, which is the sort of quintessentially European issue, if you want to say.
[193.38 → 199.72] And in the last decade, welfare systems have become this sort of polarizing political battleground within Europe.
[199.88 → 201.56] How much welfare should we be giving out?
[201.66 → 203.06] Are people defrauding the state?
[203.16 → 203.82] How much money?
[204.38 → 207.90] And so we wanted to hone in on this one area to make it sort of manageable.
[207.90 → 215.02] And we decided to investigate the deployment of predictive risk assessments across European welfare systems.
[215.60 → 222.00] And basically what these systems do, I mean, they vary in sort of size and colour, but the basic sort of mechanics remain the same,
[222.36 → 232.10] is that they assign a risk score between zero and one to individual welfare recipients and rank them by their alleged risk of committing welfare fraud.
[232.10 → 240.08] And the people with the highest scores are then flagged for investigations, which can be quite punitive and where their benefits can be stopped.
[240.24 → 254.18] So we landed on this metaphor of the suspicion machine because we felt that these systems were oftentimes essentially laundering or generating suspicion of different groups who were trying to receive welfare benefits that they needed to pay rent every month.
[254.18 → 261.28] And when you all started thinking about these suspicion machines, these deployed machine learning systems,
[261.28 → 270.88] were there existing examples, like concrete examples of how these suspicion machines were being punitive,
[271.46 → 282.98] maybe in either biased ways or just like in a kind of false positive error sort of way that's creating problems for people that it doesn't need to create?
[282.98 → 290.04] Were there, was there actual evidence at the time or was it just a big question because there wasn't any sort of quantitative measurement?
[290.74 → 293.30] So there were signs of it.
[293.70 → 300.98] So in the Netherlands specifically, there was a case where 30,000 families were wrongly accused of welfare fraud
[300.98 → 305.90] and it turned into this huge scandal called the childcare benefits scandal and eventually led to the fall of the government.
[305.90 → 313.76] And it turned out that the way that these parents were wrongly flagged for investigation was because of a machine learning model that the agency had deployed.
[314.20 → 318.40] But there was no sort of quantitative measure of what that model was actually doing.
[318.76 → 323.34] Nobody took it apart and actually looked inside and saw, okay, well, why was it making these decisions?
[323.66 → 329.34] Which is, you know, a huge reason why we as Lighthouse decided and were so adamant about the idea of,
[329.34 → 336.96] we're not just going to investigate these systems or the classical journalist methods, you know, call people up sources, you know, getting contracts.
[337.14 → 340.04] But we actually wanted to take one of these systems apart.
[340.22 → 342.98] And that was sort of the big challenge or hurdle in our reporting.
[343.10 → 348.68] And I think Justin can maybe talk to what's sort of the existing literature on these predictive risk assessments.
[348.68 → 364.12] Yeah, I think my interest in the topic comes kind of from the broader discussions about AI fairness that really started after ProPublica published its machine bias piece six or seven years ago.
[364.90 → 372.68] And in the aftermath of that, there were a bunch of systems that worked similarly that were kind of discovered in various contexts.
[372.68 → 375.50] I myself worked a little bit on predictive grading systems.
[376.10 → 386.76] So during the COVID pandemic, some school systems replaced their previous, you know, handwritten exams with an algorithm that tried to predict based on previous exams, how well somebody was scoring their final exam.
[387.56 → 392.86] And with each of these systems, the issue that emerges is essentially similar.
[392.86 → 408.30] Once you try to classify people according to risk, and you have a training set that's not a perfect representation of the true population, you'll start running into issues like disparate impact for different groups, which is kind of the most hot button issue.
[408.36 → 412.44] But you'll also start running into how representative is your fairness data.
[412.60 → 416.68] In general, you'll start running into issues with, you know, where do you set the threshold?
[416.80 → 419.52] What values are you trading off when you set the threshold higher or lower?
[419.52 → 431.22] And so I was generally interested in that and then kind of joined Lidos at a point when Gabriel and some others had done a lot of the groundwork already to see whether there was something there in welfare risk assessments and then kind of took on the technical work from there.
[431.90 → 437.94] One question I have just like even as a data scientist, just thinking like, okay, where do I start with this?
[438.38 → 441.70] This model is deployed by some entity.
[441.70 → 449.30] In theory, it's been developed by some group of technical, either engineers or data scientists or whoever it is.
[449.52 → 455.76] Where do you go about actually starting to find out, like, where does this model exist?
[455.92 → 461.02] Who has the serialized version of this model sitting on some disk somewhere in some cloud?
[461.28 → 464.36] Or like, yeah, where do you even start with something like that?
[464.84 → 472.60] So now there's a sort of trend of having algorithm registers where public agencies across Europe publish what different types of algorithms or models they're using.
[472.60 → 475.02] But that didn't exist when we started this reporting.
[475.70 → 480.18] So what we did was we made use of freedom of information laws in the U.S.
[480.20 → 481.54] I think they're called sunshine laws.
[481.76 → 488.86] And we started sending in these requests trying to figure out at least where are you using predictive modelling within this sort of welfare system?
[489.20 → 492.82] Because, you know, you could be using it to look for fraud, but you could be using it for other things as well.
[492.82 → 502.38] And we started sort of slowly building out this picture of which countries were using predictive modelling at different places in their welfare system.
[502.56 → 505.80] And then sort of start slowly building a document base.
[505.92 → 512.94] So maybe we'd ask them for we didn't start by asking a lot of times for like source code or final model files or training data.
[512.94 → 520.30] But we'd start by asking for can you give me like the manual for your data scientists for retraining the model every year?
[520.60 → 533.34] And now it allows us to ask for more specific documents and more specific questions like, OK, we know that there's a document called performance report 2023 dot HTML because we see it referenced in your manual for your data scientists.
[533.34 → 541.92] So we can request that and then sort of built-up to this place of, OK, now let's request the final model file, the source code to train it.
[541.92 → 547.36] Ask for the training data, which we can get into because there are some prickly things there around data protection laws in Europe.
[547.56 → 568.88] So we kind of tried to do this tiered approach to sort of build for that final ask for asking for the model once we could make sure that our request was specific, because oftentimes agencies would try to resist our requests saying they were too broad, or we weren't being too specific enough or trying to argue that disclosing certain documents could allow potential fraudsters to game the system.
[568.88 → 594.20] I've got to ask, like, as you kind of did this sweeping look at how predictive analytics was actually deployed across Europe, even before we get into the specific case that you studied, are there any kind of takeaways or trends that you saw in terms of how machine learning is actively being deployed by government entities or by welfare entities across Europe?
[594.20 → 600.20] Yeah, so I think it started essentially a bit later than in the United States.
[600.56 → 606.22] You kind of have this trend in policing, in kind of risk analysis.
[606.22 → 623.32] I would say that begins in the early 2000s, where you kind of have, I mean, semi-governmental organizations doing credit risk scoring, the first kind of instances of predictive policing, also more serious thinking around big data mining for some risk analytics in the welfare context.
[623.32 → 626.18] And then I would say there's a bit of a bifurcation.
[626.38 → 633.84] So you kind of see some instances where big industry players, Accenture, the volunteers of the world, right?
[633.90 → 642.94] Like these big, big companies hype up the case for big data analytics to be deployed across different sectors.
[643.58 → 646.82] And at the same time, you have a lot of failures when those tools are deployed.
[647.18 → 648.12] They often don't work very well.
[648.24 → 651.70] People who have to use them in the agencies don't know how to use them.
[651.70 → 656.22] you see some agencies that drop those systems and at the same time you see other agencies
[656.22 → 661.84] that kind of build up internal capacity and build those tools themselves sometimes in collaboration
[661.84 → 669.02] with universities or smaller startups but you kind of have these two pathways that continue to
[669.02 → 674.84] coexist at the same time I would say in terms of the systems that we looked at most of them
[674.84 → 681.86] were developed kind of from the early 2010s onwards it's definitely gotten a lot more in the
[681.86 → 687.88] last five or six years and across the eight or maybe nine countries now I'm not quite sure how
[687.88 → 693.22] many we've looked at but I think we've only seen a single country where we did not see evidence of
[693.22 → 699.06] predictive analytics being used to assess risk and welfare interesting so I guess on the other side
[699.06 → 705.56] I asked about evidence of these systems prior to your reporting evidence or cases
[705.56 → 712.10] where these systems maybe behaved in ways that caused harm or issues on the other side you mentioned
[712.10 → 718.78] this kind of hyped perception potentially hyped perception of what these systems could do in a
[718.78 → 726.42] positive way I mean the main case for using these systems as you mentioned is to kind of catch fraudsters
[726.42 → 732.98] from my understanding on that side of things is there evidence that hey yes this type of fraud is a
[732.98 → 740.86] huge problem that we need to invest kind of advanced technology in solving or is that also kind of up in
[740.86 → 747.22] the air in terms of the I guess I'm getting at the justification for using these types of systems on this
[747.22 → 752.52] sort of scale this is one of the questions we try to address in our reporting a little bit first
[752.52 → 758.14] distinguishing between deliberate fraud and unintentional error is really messy and difficult
[758.14 → 763.34] I mean how do you prove intent how do you prove that someone intentionally didn't report something
[763.34 → 768.12] I mean there's clear-cut cases where it's like criminal enterprises defrauding the welfare state
[768.12 → 773.02] using identity fraud okay that's pretty cut and clear but when it's individuals or family and they
[773.02 → 777.16] didn't report 200 euros you know is that intentional is that unintentional how do you prove it
[777.16 → 782.24] that's already a challenge what we did see is evidence of a lot of the larger consultancies
[782.24 → 787.84] tending to overhype the scale of welfare fraud and these estimations being criticized by let's say
[787.84 → 793.58] like academic studies, and you know when national auditors like the national audit office of France
[793.58 → 798.94] for example actually did you know random surveying to try to estimate the true scale of welfare fraud
[798.94 → 806.30] they estimated at about 0.2 percent of all benefits paid whereas consultancies will estimate it at about
[806.30 → 811.42] five to six percent of all benefits paid um, so there's something a little bit of this situation where
[811.42 → 816.92] you know they're hyping up estimates to sort of sell the solution you know at the same time as fraud
[816.92 → 822.08] does happen within the system, and you know our reporting isn't meant to try to dispel the notion that
[822.08 → 827.92] fraud doesn't exist but I think there's its definitely still unsettled science on what the actual scale
[827.92 → 834.20] a welfare fraud is and whether these systems that are being deployed in places like the case study
[834.20 → 839.84] we looked at are actually catching fraud or just catching people who have made unintentional mistakes
[839.84 → 845.54] and that these unintentional mistakes are being treated as fraud to add on to that a little bit I think
[845.54 → 850.46] the added justification that is often being used is that actually these systems are more fair than
[850.46 → 856.94] analog equivalents that by using a machine you get rid of biases and that they're better at detecting
[856.94 → 862.46] fraud than people are and I think as we'll probably get into later there are good reasons to doubt both
[862.46 → 869.20] of those propositions all of that was perfect setup for this particular case study that I think
[869.20 → 875.76] you've highlighted in some of your recent work I'm wondering if you could kind of set the context for
[875.76 → 882.02] the particular case study that you focused on the particular model that you focused on in light of
[882.02 → 887.42] what you were just talking about kind of scanning the environment I guess through
[887.42 → 894.62] through information requests and freedom of information requests to understand where things
[894.62 → 900.30] were deployed all the way down to like getting your hands on a model so how did that how did that
[900.30 → 906.66] transition happen and tell us a little bit about the use case that you studied more deeply as I mentioned
[906.66 → 910.90] earlier we started by sending these freedom information requests across Europe eight or nine
[910.90 → 917.14] countries, and we started receiving a patchwork of responses back, so some places just said no we're not
[917.14 → 921.36] going to give you anything at all some places would be like okay we'll give you the manual but then when
[921.36 → 927.02] you tried to ask for anything like technical like code or a list of variables they shot it down
[927.02 → 932.18] but there's this kind of one exception in all of this and that was the Dutch city of Rotterdam
[932.18 → 938.54] and Rotterdam had deployed one of these predictive models to try to flag people as potential fraudsters
[938.54 → 945.48] and investigate them and right off the bat Rotterdam sent us the source code for the training
[945.48 → 950.34] process for their model awesome, and we got really excited at first we were like wow this is great
[950.34 → 956.14] we started looking through the code, and we noticed that when you know the scoring function in the code
[956.14 → 961.42] goes to load something called the final model.RDS file, and we go looking through the directory
[961.42 → 968.44] and we notice huh wait a second this final model that RDS file you know the actual model file that
[968.44 → 974.06] can be imported the score isn't in the directory so we email them back we say hey, hey guys I think you
[974.06 → 979.18] made a mistake like there's this final model.RDS file missing in the code directory so we can't
[979.18 → 985.16] actually run anything they go oh well yeah psych but uh that you're not getting that one um and
[985.16 → 990.48] and their justification for this was that if uh this was made public potential fraudsters would be able
[990.48 → 996.92] to gain the system so you know long story short we went on this year-long battle with um to attempt
[996.92 → 1005.06] to get this model file and um eventually the city to their credit decided to disclose this model file
[1005.06 → 1010.38] to us so we could actually run it and what does this model do I think Justin can do a good uh explanation
[1010.38 → 1017.68] of what this model actually does and how it works yeah so it's um a grading boosting machine model it's a
[1017.68 → 1024.92] pretty standard machine learning model it ingests 314 variables, and it outputs a score the issue that
[1024.92 → 1030.98] we ran into very quickly once we had access to this model is well what does this actually tell us right
[1030.98 → 1039.04] okay we can make up a bunch of people now and score them but how do we then know what that means for
[1039.04 → 1044.94] those people and so there were kind of two things that became important to figure out at that point
[1044.94 → 1054.08] one was what do realistic people look like and the second was what is the boundary at which a person
[1054.08 → 1059.18] is considered high risk the second one was relatively easy to figure out we kind of had some
[1059.18 → 1064.00] broad estimations of how many people are flagged each year we could run some simulations and kind of
[1064.00 → 1069.36] see the distribution of risk scores and at that point we could take a good guess for what the
[1069.36 → 1077.24] threshold would be getting access to realistic testing data was a lot more challenging and for a
[1077.24 → 1082.62] while we thought we would have to just simulate a bunch of people you know take guesses but actually
[1082.62 → 1087.76] Gabriel had requested some basic stats about the training data at an earlier stage he essentially
[1087.76 → 1092.96] asked look can you like tell us give us like a histogram for each of the variables so we can see
[1092.96 → 1099.02] what the broad distribution in the training data you know for ages for instance or for gender and so on
[1099.02 → 1106.54] and our idea was to use those basic distributions to sample new people but when I was meant to you
[1106.54 → 1111.70] know type all of this stuff down into like a file so we could then run those simulations I got lazy and
[1111.70 → 1116.86] I wanted to just scrape the document, and so i it was a HTML file so I opened it up and inspected it and
[1116.86 → 1121.78] it turned out that the entire training data was contained in this file which happens when you create
[1121.78 → 1127.52] plots with plot quite often um so if you know want to leak something to a journalist that's a good way to do it
[1127.52 → 1133.46] there you go yeah so we kind of back stead and got access to the entire training data at that point
[1133.46 → 1139.62] the question became okay now we know what realistic people look like what tests can we actually run in
[1139.62 → 1144.76] terms of figuring out who does this model flag at higher rates does it have justification to do so
[1144.76 → 1148.62] and so on and the one thing that was missing from the training data was that we didn't have access to
[1148.62 → 1154.06] the labels itself so we knew you know your age your family background your job history that kind of
[1154.06 → 1159.04] stuff, but we did not know if you had actually committed fraud or not and that meant that and
[1159.04 → 1164.06] this is the big limitation of our story, but that meant that we could essentially only understand
[1164.06 → 1170.14] which characteristics lead to higher or lower scores, but we wouldn't know if those scores are
[1170.14 → 1175.08] erroneous at higher rates for one group rather than another so I just want to be very open about that
[1175.08 → 1179.72] that is a limitation of the design but having access to the training data having access to the source
[1179.72 → 1183.82] code being able to see how the training data is constructed having access to the final model file
[1183.82 → 1189.32] all of that allowed us to investigate a bunch of aspects with the system which I think still made
[1189.32 → 1194.60] for a very valuable story both in terms of explaining how this stuff works but then also in terms of
[1194.60 → 1198.94] showing that there are likely consequences which seem to be discriminatory against certain groups
[1198.94 → 1205.02] probably a lot of our listeners will be familiar with what a gradient boosting machine is and sort of
[1205.02 → 1210.92] like maybe this is one of the tutorials that you ran on uh on a Jupiter notebook when you're
[1210.92 → 1217.60] first taking your kind of data science 101 so the model I think is very familiar I think a lot of the
[1217.60 → 1223.74] interesting things here are related probably to the model features and that sort of thing did anything
[1223.74 → 1231.20] jump out to you maybe even before you kind of ran a kind of larger scale analysis in terms of like
[1231.20 → 1239.78] the features that were included in the data set and how those may or may not like intuitively be
[1239.78 → 1246.32] connected to this sort of welfare fraud situation did anything jump out when you were kind of doing
[1246.32 → 1253.22] your initial discovery and kind of exploratory data analysis on this data yeah for sure though I think
[1253.22 → 1258.92] it's maybe important to preface this with saying that including features that seem discriminatory
[1258.92 → 1264.30] does not automatically lead to discriminatory outcomes and I think that is sometimes being
[1264.30 → 1269.58] confused right you can get discriminatory outcomes without features that look bad like I don't know
[1269.58 → 1274.38] racial or gender or racial background or gender or something like that, but it's also it also works
[1274.38 → 1278.30] the other way you can include a bunch of these features and not get any discriminatory outcomes right
[1278.30 → 1284.06] both of these things are possible that being said there were a bunch of features that seemed perfectly
[1284.06 → 1289.52] reasonable you know contact with the welfare agency how often have you been there have you missed any
[1289.52 → 1293.26] of your appointments that kind of stuff there were a lot of demographic features and I think those get
[1293.26 → 1300.74] into trickier territory some like age are maybe justifiable on some level gender gets a bit harder and then
[1300.74 → 1307.58] a lot of features measuring through proxy but measuring ethnic background through language skills I think
[1307.58 → 1312.48] there was 10 or 12 Gabriel correct me if I'm wrong but definitely a lot of variables on language skills no I think
[1312.48 → 1318.84] 30 or something oh 30 yeah yeah um because it measured everything from like your Dutch uh like spoken Dutch
[1318.84 → 1324.52] fluency you know like writing Dutch fluency the actual language you spoke, so there was like a
[1324.52 → 1329.88] categorical variable with like 200 values or something so it got as granular as the specific language you
[1329.88 → 1336.54] spoke whether you speak more than one language but anyway continue Justin yeah and then I think in some way
[1336.54 → 1345.70] the weirdest set of variables were essentially behavioural assessments by the caseworkers so we
[1345.70 → 1350.50] actually got access to some of the variable code books and in there it said that you know there was a
[1350.50 → 1355.76] variable that essentially where people were meant to judge how somebody was wearing makeup especially
[1355.76 → 1360.82] for women so you know stuff that just seems really sexist so those variables were included which is
[1360.82 → 1366.12] problematic in and of itself but then the way they were transformed in the pre-processing steps was that
[1366.12 → 1372.64] essentially this textual data was just transformed into a zero one variable depending on whether there
[1372.64 → 1377.74] was anything in this field or not which is also I mean you just lose a bunch of maybe the more
[1377.74 → 1381.80] interesting information if you do that but I think that set of variables because it's just based on
[1381.80 → 1387.40] individual caseworker assessments if your claim is that the system should lead to reduction in bias and
[1387.40 → 1394.42] then you include these variables that are so obviously subjective I think that kind of undermines your claim
[1394.42 → 1400.94] right away and in the data set like in terms of the label and the output were you able to understand
[1400.94 → 1409.84] at all like oh these are investigations that happened that actually were verified to be fraud or not
[1409.84 → 1416.80] essentially like a one or zero type of label or how is that set up yeah so we did not have access to
[1416.80 → 1423.36] the label which is again the big drawback so we could only score people who we know they had labels but we
[1423.36 → 1427.84] didn't have that label ourselves gotcha, but we did a bunch of ground reporting to essentially work
[1427.84 → 1432.48] around that and maybe Gabriel can speak a bit to that yeah I mean two things first I mean just to
[1432.48 → 1438.28] talk about how the training gate is constructed first it's um you know over 12 000 past investigations
[1438.28 → 1443.12] that the city has carried out and these past investigations are not a random sample, so there's
[1443.12 → 1448.20] some subset within there that's random if I think about a thousand but all the rest of the cases are just
[1448.20 → 1452.32] where investigators have looked at the past either through anonymous tips or through this kind of
[1452.32 → 1457.98] theme studies that they do where they say this year we're going to check every man living in this
[1457.98 → 1462.18] neighbourhood so it's not a random subset of people that they're training this model on which is
[1462.18 → 1468.24] problematic in first place the second thing is that this label yes fraud no fraud doesn't distinguish
[1468.24 → 1474.96] between intentional fraud and unintentional mistakes right, so these are flattened into the same thing
[1474.96 → 1480.26] when labelling the training data set, so those are I think two problematic things right off the bat I think
[1480.26 → 1486.42] even third more complicated thing is that the law for what is considered fraud has actually changed
[1486.42 → 1492.52] over time and this training data spans back 10 years but all that aside you know one of the things that
[1492.52 → 1498.60] we wanted to do with this reporting was to look at the impact of being flagged for investigation
[1498.60 → 1504.66] you know what does that mean for a person, and you know how are they treated by the system, and so we did a
[1504.66 → 1509.50] bunch of ground reporting in Rotterdam and we sort of used the results from our experiment to build
[1509.50 → 1514.58] profiles who would be considered some of the most high risk people, and we saw that it was you know
[1514.58 → 1521.42] one of them at least would be like single mothers of a migration background who don't have a lot of
[1521.42 → 1527.58] money financially struggling living in certain majority ethnic neighbourhoods so we did a bunch of
[1527.58 → 1532.14] ground reporting those places and found people it was quite challenging people were quite afraid to talk
[1532.14 → 1538.26] people who had been investigated in the time span that the model was active and what we found was that
[1538.26 → 1543.34] they were treated incredibly punitively by these investigations from the city where fraud controllers
[1543.34 → 1550.28] are empowered to raid your house at 5 a.m in the morning unannounced count your toothbrushes sift through
[1550.28 → 1557.96] your laundry go through all your bank statements and that even the smallest mistakes like forgetting to
[1557.96 → 1566.24] report 100 euros could leave you landed as an alleged fraudster so I think there's even you know based on
[1566.24 → 1570.82] reporting this do we just even question the validity of the label and the consistency of the label
[1570.82 → 1577.02] but beyond that I think what we established for the reporting is that the consequences of being flagged
[1577.02 → 1582.64] even if in the end you're found to be completely innocent just having people you know raiding your
[1582.64 → 1587.06] house at 5 a.m asking you questions about your romantic life in front of your children I mean that's a
[1587.06 → 1591.08] negative consequence in of itself even if you're found to have done nothing wrong
[1591.08 → 1621.06] this is a changelog news break the biggest product news out of open
[1621.06 → 1628.78] AI recently is gets custom versions of ChatGPT that you can create and sell for specific purposes
[1628.78 → 1635.28] you build these gets by crafting special prompts that are fed to ChatGPT prior to it interacting with
[1635.28 → 1642.62] a user is it any surprise that crafty technologists have convinced ChatGPT to spit out a bunch of these
[1642.62 → 1648.98] custom prompts via prompt injection I wasn't surprised but I was a bit delighted to read through the
[1648.98 → 1655.32] collection of GPT prompts to see what they're made of this gen z 4 memes prompt which helps you
[1655.32 → 1662.24] understand the lingo and latest meme that gen z are into is kind of hilarious quote speak like a gen z
[1662.24 → 1667.96] the answer must be an informal tone use slang abbreviations and anything that can make the
[1667.96 → 1674.06] message sound hip especially use gen z slang as opposed to millennials the list below has a list of
[1674.06 → 1682.78] gen z slang also speak in low caps end quote low caps more like no cap am I right I'm so old fair
[1682.78 → 1687.28] warning though from the collector of these leaked prompts who says quote there is no guarantee that
[1687.28 → 1693.54] these prompts are the original prompts and these leaked prompts are for reference only you just heard
[1693.54 → 1700.18] one of our five top stories from Monday's changelog news subscribe to the podcast to get all the
[1700.18 → 1706.24] week's top stories and pop your email address in at changelog.com slash news to also receive our free
[1706.24 → 1714.20] companion email with even more developer news worth your attention once again that's changelog.com slash news
[1714.20 → 1718.74] you
[1730.18 → 1735.94] all of this is very interesting to me from a data science perspective because a lot of these things
[1735.94 → 1742.32] are kind of yeah things that I know we've talked about you know on this podcast but also in my day-to-day
[1742.32 → 1748.22] work things that have come up that you sort of establish as you know best practices around how you
[1748.22 → 1754.44] construct your label how you construct your features like responsibly to do well at your data
[1754.44 → 1760.40] science problem I do want to get to the actual like model performance here in a second which is
[1760.40 → 1766.48] one question is like well all of we see all of these flaws in the data does the model actually work or
[1766.48 → 1772.38] have all of this kind of underlying problems poison the output but I think before then I'm just
[1772.38 → 1779.20] wondering like as a person who provides occasionally consulting services to other people in data science
[1779.20 → 1786.08] did you get a sense at all for like the city of Rotterdam hired x consultancy to give them the
[1786.08 → 1793.02] model that they deployed and are using is just sort of like the consultancy through the model over the
[1793.02 → 1800.84] fence and like here use this or how much interaction was there with actual Rotterdam employees and how
[1800.84 → 1807.16] deep was the understanding of how this model was built and deployed or was it just a sort of contract
[1807.16 → 1812.18] here's money here's the model all right let's put it into production what was the interaction like
[1812.18 → 1819.32] there were you able to discern any of that not super deeply but from what we do know the city put
[1819.32 → 1824.74] out a tender asking for someone to come in and build a predictive model for this purpose Accenture won
[1824.74 → 1832.24] that tender put someone on it and there was a Rotterdam data scientist involved but who presumably or
[1832.24 → 1836.08] from what I can tell didn't have any sort of machine learning background I'm just
[1836.08 → 1843.28] normal famous scientists at the city Rotterdam set up the whole code base train the model develop all
[1843.28 → 1848.20] the code for the pre-processing train the model handed it over to the city and kind of went by
[1848.20 → 1853.62] like we're gone now and from that point on Rotterdam took full control of the model like they would
[1853.62 → 1860.64] retrain it every year they made like adjustments to like for features and also decided to exclude some
[1860.64 → 1867.02] cheap features like nationality but I do think that during that time Rotterdam upgraded its own data science
[1867.02 → 1873.02] capacity so by the time we got there they did have like two people who were specialized in machine learning
[1873.02 → 1879.92] that were looking over the model that's my understanding of the basic setup yeah fascinating I do want
[1879.92 → 1886.50] to get to the kind of model performance I guess because i I know this is something that I've got asked when I've done
[1886.50 → 1892.34] workshops and I talk about either like fairness or bias and models there's always someone that kind of comes up
[1892.34 → 1898.18] with the question of like well if the data is biased but I'm still like the model's accurate and I'm predicting
[1898.18 → 1905.92] accurate results is that a problem I think there are problematic things about that how you might answer that question
[1905.92 → 1914.88] in and of itself but in your case was the model actually helping in any way or was it were the problems
[1914.88 → 1921.54] kind of so deep in the data and the way that the labels were generated such that the majority
[1921.54 → 1928.02] of what it was producing was maybe more chaos or issues so in the test set that the city used, and we have
[1928.02 → 1933.56] kind of they're the documentation of that even though we don't have the labels ourselves we see that in the set
[1933.56 → 1942.40] there is a 21 percent baseline rate of fraud or some kind of wrongdoing and the model kind of depending
[1942.40 → 1948.58] on where you set the threshold but the model um essentially has a hit rate of 30 percent so out of
[1948.58 → 1954.48] the people selected around 30 percent of them are labelled within the positive class so it's a 10 percent
[1954.48 → 1960.60] improvement above random is that good is that bad the roc curve looks absolutely terrible Margaret
[1960.60 → 1965.80] Mitchell um who many listeners probably know uh called it essentially random guessing I'm not quite
[1965.80 → 1972.86] sure if I would go that far, but it's certainly not anything to write home about, and we see that
[1972.86 → 1977.60] there are huge disparities in who's getting flagged in their characteristics does the label data show that
[1977.60 → 1984.10] there's a reason for that maybe but because we have some idea about how the training data was constructed
[1984.10 → 1989.40] specifically through these theme investigations there's a very strong probability that a lot of these
[1989.40 → 1994.52] patterns that we see in terms of who's getting flagged is a function of the selection process
[1994.52 → 1998.74] that leads to somebody being included in the training data rather than of actual fraud being
[1998.74 → 2003.58] committed I can give an example of how that that might work most of the men in the training data
[2003.58 → 2008.76] very likely were selected through one of these investigations where you know all men in a certain
[2008.76 → 2013.42] neighbourhood were investigated which have a pretty low likelihood of actually finding fraud that kind of
[2013.42 → 2017.56] implies that most women were selected by you know anonymous tips or random sampling
[2017.56 → 2023.50] and those things have somewhat higher probabilities of detecting fraud and so if your you know your
[2023.50 → 2029.08] method of selection impacts how likely it is that the person who you investigate has actually done
[2029.08 → 2035.62] something wrong then the training set that you train your model on will contain patterns that are a
[2035.62 → 2039.56] function of your selection method rather than of the real world and how fraud patterns look in the real
[2039.56 → 2046.50] world, and so we couldn't conclusively prove this because we didn't have access to who was labelled
[2046.50 → 2051.20] or who was selected like within the training set we couldn't say who came from which source but we
[2051.20 → 2057.58] we know that these different sources fed into the training set, and it seems very probable that this type of
[2057.58 → 2063.64] selection method would lead to these kinds of disparate outcomes I think there are all sorts of things to learn
[2063.64 → 2074.12] in this story as even just a data scientist setting up data sets and trying to train models you know i I come of course
[2074.12 → 2080.50] from a certain perspective in kind of what touches me about this story and I'm so glad that it's out there
[2080.50 → 2086.54] and there's some transparency around this I'm wondering could you speak a little bit to the reception of this
[2086.54 → 2095.98] story maybe more widely by non-technical audiences in terms of realizations that people were coming to or responses
[2095.98 → 2104.70] that came out of people realizing how these systems were constructed and how they perform in reality
[2104.70 → 2111.40] versus maybe what their perception was prior kind of to answer to that question I think first one
[2111.40 → 2116.06] of the big goals of this project and the piece that we published with wired where we kind of take
[2116.06 → 2121.24] leaders through the model how it works was to have it be an educational piece of journalism too like you've been
[2121.24 → 2126.66] hearing about machine learning and the sort of impact has on your lives but very few stories actually
[2126.66 → 2131.42] take you through like the full life cycle of model what does it look like quote-unquote inside the
[2131.42 → 2136.66] machine so we really wanted to make an educational piece in that sort and also talk about you know
[2136.66 → 2141.10] what justice covered what are the different sorts of problems or flaws in the system what are the
[2141.10 → 2147.12] consequences of those flaws, and you know I think normal people of course found the sort of
[2147.12 → 2152.82] discriminatory angle or the fact that for example like single mothers are penalized more, or you know
[2152.82 → 2158.16] I think that was something that they took away from but surprisingly one area that people that
[2158.16 → 2164.16] surprised me a bit that people seem quite fixated or curious by was the decision trees portion um so
[2164.16 → 2168.78] what we try to do in that portion of the piece for people listeners haven't read it yet is we take some
[2168.78 → 2174.68] decision trees from the model from this gradient boosting model we show how this creates non-linear
[2174.68 → 2180.64] interactions right, so teachers have sort of relation in effect each other differently relationally so
[2180.64 → 2185.70] you know in decision tree x if you're a man you might go down the right side of the tree and if
[2185.70 → 2189.24] you're a woman you might go down the left side, and you will be evaluated by different characteristics
[2189.24 → 2193.70] so that would seem to be something that really like to seem to resonate with leaders like questioning
[2193.70 → 2199.54] like okay well that's this is how it works, and you know is that fair to me, or you know it makes it
[2199.54 → 2204.12] difficult for me to understand how these interactions work on a political level you know
[2204.12 → 2210.94] Rotterdam to their credit uh was quite graceful when we presented them with the results, and they sent
[2210.94 → 2217.42] back the statement saying essentially like they called our results uh informative educational which
[2217.42 → 2223.80] in the field of investigative journalism never happens like someone say you know the subject of your
[2223.80 → 2229.18] investigation saying it's informative and educational is I think never happened when they're the subject
[2229.18 → 2236.58] yeah yeah um and called on other cities to do what they had done to be transparent I mean I found
[2236.58 → 2244.08] that incredibly brave and elegant response to what we've done, and they were sort of debating whether
[2244.08 → 2249.62] to continue the use of this model and then it decided that they weren't going to use it anymore
[2249.62 → 2254.66] that the sort of ethical risks were too high and then I think I mean elsewhere I don't know Justin if
[2254.66 → 2259.16] you have any reactions that stuck out to you yeah maybe the one thing that I would add
[2259.16 → 2264.92] is that I think this field of like algorithmic accountability reporting but even the academic
[2264.92 → 2269.68] discussions about it has I don't want to say suffered but it has been kind of constrained a
[2269.68 → 2273.54] little bit by a streetlight effect following machine bias right you had this big story coming
[2273.54 → 2277.60] out and then afterwards for years everybody was talking about these various outcome fairness
[2277.60 → 2282.94] definitions and I think that's a very valuable debate i myself and almost enjoy it like I think it's
[2282.94 → 2288.36] some of it is just mathematically very interesting it's really difficult ethical questions that it
[2288.36 → 2293.54] brings up but I think a bunch of the other dimensions of fairness in the life cycle of the
[2293.54 → 2298.88] system have been neglected and Gabriel and i in the past year have kind of been making the rounds and
[2298.88 → 2303.94] the cases to people that we should be looking at algorithmic fairness more holistically we should
[2303.94 → 2308.84] look at the training data we should look at the input features we should look at yeah the type of
[2308.84 → 2312.94] model that is being used and how that maps onto our understanding of the process and then we should also
[2312.94 → 2317.48] look of course at the outcome fairness stuff but I actually think and i at your reaction kind of
[2317.48 → 2321.76] spoke to that I think this training data bit is probably the most interesting one and one that i
[2321.76 → 2326.20] I have both academic training as a computer scientist and also as a political scientist and
[2326.20 → 2331.08] when I took my computer science classes nobody ever talked about how do you set up you know a
[2331.08 → 2334.40] representative sample I was kind of like you know we take whatever data we have and then we
[2334.40 → 2340.88] try to run as many models over it use it all in all features right and well that might kind
[2340.88 → 2345.84] of up your performance along certain metrics right on some level if the data doesn't contain
[2345.84 → 2351.16] the functional relationship that you're trying to model you can't get there and I think that's a
[2351.16 → 2357.40] lesson that I hope some of the yeah maybe practitioners who read RPS also take away from it
[2357.40 → 2363.54] yeah that's super helpful I think you got to where I wanted to ask anyway because I know our we have
[2363.54 → 2370.66] listeners that are practitioners and are probably thinking to themselves like what is a kind of takeaway
[2370.66 → 2378.08] that I can take away from this because I would say from my experience at least most data practitioners
[2378.08 → 2384.86] are not intentionally trying to create harmful outcomes from their systems they do actually want
[2384.86 → 2391.22] to be responsible it's just sometimes they might be somewhat confused or constrained in certain ways
[2391.22 → 2396.46] that don't allow them to spend time thinking about those things but um yeah I really appreciate you
[2396.46 → 2402.34] bringing us around to that as we kind of close out here, and we look maybe to the future um we started
[2402.34 → 2407.02] out this conversation i kind of mentioned you know there's all of this talk of course constantly
[2407.02 → 2412.96] swirling around us about the dangers of AI and all of that stuff which is operating on multiple
[2412.96 → 2417.92] levels some of which are useful and some of which aren't probably but I want to ask both of you
[2417.92 → 2425.12] maybe as you look towards the future post this project what you've done here um what's on your mind
[2425.12 → 2432.72] as you look towards the future of how this technology is ever expanding what gives you pause what gives
[2432.72 → 2438.58] you hope what do you hope people are thinking about as we kind of look to the future in how this
[2438.58 → 2446.26] technology is developing, so there are two things I would respond to that one is that I hope we'll have
[2446.26 → 2451.16] more discussions about transparency around these systems I think that's a precondition for anything else
[2451.16 → 2457.00] and for that to happen there is an argument that needs to be dispelled, and that argument is that
[2457.00 → 2463.98] making these systems public allows people to gain them one I think it's really, really hard and there's
[2463.98 → 2470.34] some very good academic research that shows how hard it would be and two well these systems operate
[2470.34 → 2475.30] essentially like by laws right they're essentially administrative guidelines encoded in a model file
[2475.30 → 2480.66] for how a decision is being made in some bureaucracy and I think it's really hard to make the case
[2480.66 → 2486.62] that such guidelines should be secret and so yeah I think we need to have a discussion and make the
[2486.62 → 2493.72] case proactively that transparency in this space and encouraging people to learn how they work is a
[2493.72 → 2496.94] good thing and encouraging people to game those systems is probably a good thing because that means
[2496.94 → 2502.82] you're probably closer to abiding by the law and um if you can game the systems then you know maybe
[2502.82 → 2508.26] they aren't very good that's the first thing I want to say the second one is that most of the systems
[2508.26 → 2512.88] we've looked at are pretty terrible in most ways I think they don't work very well they have
[2512.88 → 2517.62] either you know use features that are absolutely terrible or have training data construction that
[2517.62 → 2522.80] is really problematic, or you know have disparate impacts on various groups almost every single
[2522.80 → 2528.68] system we've looked at so far has one or multiple of these features, but there are some systems that
[2528.68 → 2533.84] maybe are better, and it's possible I think if you think very seriously about how you do each of these
[2533.84 → 2538.44] the feature selection the training data and then constructing the model and then evaluate for bias
[2538.44 → 2542.18] and then potentially retrain relay your training data and so on you know maybe it's possible to
[2542.18 → 2547.42] get to a better place um technically it certainly is and I think then you get to a different set of
[2547.42 → 2554.50] questions and I hope that the conversation at some point can move beyond kind of the know gross
[2554.50 → 2559.72] incompetence in a way which we are showcasing um across the board but can move to a place where we can
[2559.72 → 2564.70] discuss okay let's take this best case scenario we have a system that doesn't have obvious bias and
[2564.70 → 2570.94] so on that was constructed carefully should we do this is it a good idea is a machine making the
[2570.94 → 2576.56] decision removing something inherently kind of valuable from the type of interaction is the machine
[2576.56 → 2581.62] actually more explainable than a human is and is that a good thing is it you know equal treatment
[2581.62 → 2585.96] because everybody's being scored by the exact same system and not by individual caseworkers or is it
[2585.96 → 2589.36] not equal treatment because the know the tool contains a decision tree based model
[2589.36 → 2593.72] and so different people are based on different characteristics how do we think about systems
[2593.72 → 2599.88] that include some level of probabilistic assessment is that something that we think a administrative
[2599.88 → 2605.78] decision should do and then of course we can also have the maybe fun for some people discussions
[2605.78 → 2610.94] around like which fairness definition is the best whether we should seek to minimize or equalize
[2610.94 → 2615.22] false positive rates across different groups and so on I think there's a bunch of really important
[2615.22 → 2621.54] questions that society has to grapple with here but I don't think we're there quite yet in most cases
[2621.54 → 2626.86] and so long as we aren't um I think Gabriel and I will have plenty of work showcasing incompetence and
[2626.86 → 2631.82] all that stuff um but I hope that at some point we can move beyond that yeah anything to add
[2631.82 → 2636.96] Gabriel no I think Justin summed it up really well I'll just kind of tease that we do have some reporting
[2636.96 → 2641.36] that comes that's coming up in the coming year that will I think grapple with some of these
[2641.36 → 2647.58] thorny or ethical issues um you know ask questions like when and if ever is it okay to use these
[2647.58 → 2654.92] systems I think maybe one thing that I will add though is I think it is important for people like
[2654.92 → 2660.22] practitioners that are listening to your audience to also take a step back and to maybe not always see
[2660.22 → 2664.86] the deployment of these systems or this sort of thorny fairness questions as like a math problem but
[2664.86 → 2671.00] it can also be a sort of wider societal problem as well so for example in the European welfare
[2671.00 → 2677.82] context we've seen in everywhere we're looking models that attempt to detect fraud but what we
[2677.82 → 2683.42] don't see is models that try to find people who are eligible for welfare benefits who aren't using
[2683.42 → 2687.20] them because they're afraid of the system, and we know this is a huge problem in places like France
[2687.20 → 2692.68] 30 percent of people eligible for welfare don't use it because they're scared of the system this has
[2692.68 → 2699.26] consequences for people not using welfare but also has consequences downstream for society so imagine
[2699.26 → 2704.16] families that aren't able to feed their kids developmental issues that come from that so i
[2704.16 → 2708.10] think it's always important and something we try to raise in our important reporting to kind of take
[2708.10 → 2713.34] a step back and ask you know should we be doing this to think about the premise of why are we actually
[2713.34 → 2719.00] deploying this model and to rethink that and at some points and think about you know is there a
[2719.00 → 2724.34] better way to use this technology or are we only kind of narrowing in on one piece of this picture
[2724.34 → 2728.76] yeah that's great I think that's a really wonderful encouragement to end things with
[2728.76 → 2735.32] we will certainly be on the edge of our seats looking for your future work and I encourage everyone
[2735.32 → 2741.40] we'll include the links to Gabriel and Justin's work in our show notes so I encourage you go and
[2741.40 → 2747.30] explore it there's lots of great graphs and references and even more technical description of
[2747.30 → 2752.62] the methodology than we had time to go into here so dig in and learn about what they're doing its
[2752.62 → 2757.26] really wonderful and yeah, thank you for your work Justin and Gabriel, and thank you for taking time to
[2757.26 → 2760.44] join us thanks so much thanks so much for having us
[2760.44 → 2775.94] thank you for listening to practical AI your next step is to subscribe now if you haven't already
[2775.94 → 2781.26] and if you're a long-time listener of the show help us reach more people by sharing practical AI
[2781.26 → 2786.14] with your friends and colleagues thanks once again to fast and fly for partnering with us
[2786.14 → 2793.10] to bring you all changelog podcasts check out what they're up to at fastly.com and fly.io and to our
[2793.10 → 2797.62] beat freaking residents break master cylinder for continuously cranking out the best beats in the
[2797.62 → 2800.66] biz that's all for now we'll talk to you again next time
[2800.66 → 2813.54] you
