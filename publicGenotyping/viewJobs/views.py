from django.shortcuts import render
from django.http import HttpResponse
import paramiko

# Create your views here.
def home_page(request):
    def get_job_data():
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect('peregrine.hpc.rug.nl', username='umcg-ndeklein', key_filename='/Users/NPK/.ssh/id_rsa')
        stdin, stdout, stderr = ssh.exec_command('squeue -u umcg-ndeklein -o "%.7i %.30j %.25u  %.10M %R %l %L" -a')
        job_data = [x.strip().split() for x in stdout.readlines()]
        assert all(len(i) == len(job_data[0]) for i in job_data)
        ssh.close()
        return job_data
    job_data = get_job_data()


    return render(request, 'home.html')
