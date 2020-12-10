import json
class Job(object):

    def __init__(self, jobCreator, jobName, numOfSeekers, targetIP, targetPort):

        self.JobCreator = jobCreator
        self.JobName = jobName
        self.NumOfSeekers = numOfSeekers
        self.targetIP = targetIP
        self.targetPort = targetPort
        self.jobParameters = [jobCreator, jobName, numOfSeekers, targetIP, targetPort]
        self.FullJob = jobCreator+" "+" "+jobName+" "+" "+numOfSeekers
        self.JobSeekerList = []

    def __iter__(self):
        yield self.JobCreator
        yield self.JobName
        yield self.NumOfSeekers
        yield self.targetIP
        yield self.targetPort

    def addSeekerList(self, SeekerName):
        self.JobSeekerList.append(SeekerName)

    '''
    Getter Functions
    '''
    def getJobCreator(self):
        return self.JobCreator

    def getJobName(self):
        return self.JobName

    def getNumOfSeekers(self):
        return self.NumOfSeekers

    def getFullJob(self):
        return self.FullJob

    def getJobSeekerList(self):
        return self.JobSeekerList

    def getJobSeekerListSize(self):
        return len(self.JobSeekerList)

    '''
    Setter Functions
    '''

    def setJobCreator(self, JobCreator):
        self.JobCreator = JobCreator

    def setJobName(self, JobName):
        self.JobName = JobName

    def setNumOfSeekers(self, NumOfSeekers):
        self.NumOfSeekers = NumOfSeekers

    def setFullJob(self, FullJob):
        self.FullJob = FullJob

    def setJobSeekerList(self, JobSeekerList):
        self.JobSeekerList = JobSeekerList

    def __str__(self):
            d = dict()
            d['CreatorNamed'] = self.JobCreator
            d['JobType'] = self.JobName
            d['NumofSeekers'] = self.NumOfSeekers
            d['targetIP'] = self.targetIP
            d['targetPort'] = self.targetPort
            print(d)

            return json.dump(d)
