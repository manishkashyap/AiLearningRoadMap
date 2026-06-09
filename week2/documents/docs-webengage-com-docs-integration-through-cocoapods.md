# Integration through CocoaPods

- URL: https://docs.webengage.com/docs/integration-through-cocoapods
- Publication Date: Not found
- Scraped At: 2026-06-02T14:01:04.875003+00:00

iOS
Getting Started
Integration through CocoaPods
🚧
Information
CocoaPods is being deprecated. WebEngage recommends using Swift Package Manager for all new integrations. For more information, refer here.
WebEngage SDK is distributed via
CocoaPods
and
Swift Package Manager
If you don't have CocoaPods installed, you can do it by executing the following line in your terminal.
Shell
sudo gem install cocoapods
If you don't have a
Podfile
, then create one by using the
pod init
command.
Add the following line to your
Podfile
:
Ruby
# Avoid use_frameworks! declaration in your Podfile. Contact us at
[email protected]
if you face any issue.

target 'YourAppTarget' do
 
 pod 'WebEngage/Core'

 #if using geofencing and location services use the below code else remove.
 pod 'WebEngage/Location' 

end
Then, install the SDK by running the following command in your terminal:
Shell
pod install
Now, open your project workspace and check if the WebEngage SDK is properly added.
Updated
about 2 months ago
Location Module
Migration Of WebEngage SDK From Cocoapods To SPM
Copy Page
