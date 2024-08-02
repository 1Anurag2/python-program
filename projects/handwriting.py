import pywhatkit as pw
txt = """The present paper is an attempt to explore the importance of human values in the
global society. Human society may not significantly sustain without human values. Hence, it
is necessary to talk on the subject and bring about awareness of human values into the
modern society. There is no denying the fact that the present global society is facing a lot of
crises. Human value crisis is a known fact of the modern society. Indeed, humans are aware
of the global and national problems which they are currently facing. The impact of human
activities on the earth in various ways is placing a significant amount of stress. For instance,
the climate change due to global warming. There seems to be a significant link between the
remedial measures and various solutions to climate change and the practice of human values.
It is believed that at the end of the day, it is the human values which will save the mankind.
If any ethics are primarily to help a person to live a just and righteous life with
him/her and in relation to others, ethics too is similarly oriented towards a righteous life. The
personal and social life of every individual is permeated by a great sense of righteousness.
Without this possibility of constituting the world-view of the community and the possibility
of the individuals striving to achieve it, a value system can only be either an item in the
“thought-museum” of cultural artifacts or a fantasy. It is perpetual preparedness to make
cultural changes with a view to obtaining this balance (Anthony Giddens, 2011)."""
pw.text_to_handwriting(txt,"Human_values.png",[0,0,138])
print("Handwriting convert successful")