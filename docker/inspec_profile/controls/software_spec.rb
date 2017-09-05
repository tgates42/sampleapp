control "software-01" do
  impact 1.0
  title "Python should be available"
  describe command('python2 --version') do
    its('stdout') { should eq '' }
    its('stderr') { should match /Python 2\.7\.[0-9]+/ }
    its('exit_status') { should eq 0 }
  end
end
