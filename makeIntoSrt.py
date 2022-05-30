textArray = []

with open("./transcript.txt","r") as f:
    textArray = f.readlines()

class srtDetails:
    def __init__(self,sequenceNumber,startTime:str,caption:str,endTime:str) -> None:
        self.sequenceNumber = sequenceNumber
        self.startTime = startTime.strip()
        self.caption = caption.strip()
        self.endTime = endTime.strip()
        self.fullTime = ""
        self.fullText = ""
    
    def setupData(self):
        if(len(self.startTime) == 3):
            self.startTime = "00:0"+self.startTime+",000"
        if(len(self.startTime) == 4):
            self.startTime = "00:"+self.startTime+",000"
        if(len(self.endTime) == 3):
            self.endTime = "00:0"+self.endTime+",000"
        if(len(self.endTime) == 4):
            self.endTime = "00:"+self.endTime+",000"    
        
        self.fullTime = f"{self.startTime} --> {self.endTime}"
        self.fullText = f"{self.sequenceNumber}\n{self.fullTime}\n{self.caption}\n\n"
        return self
    
    def __repr__(self) -> str:
        return self.fullText

srtElementsArray:list[srtDetails] = []

print("2")
iSequence = 0
for i in range(0,len(textArray)-2,2):
    print(textArray[i])
    iSequence += 1
    temp = srtDetails(iSequence,textArray[i],textArray[i+1],textArray[i+2])
    srtElementsArray.append(temp.setupData())


print("3")
for i in srtElementsArray:
    print(i)

with open("./transcript.srt","w") as f:
    for i in srtElementsArray:
        f.write(i.fullText)