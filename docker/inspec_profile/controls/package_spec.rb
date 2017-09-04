control "package-01" do
  impact 1.0
  title "Python should be installed"
  describe package('python') do
    it { should be_installed }
  end
end
