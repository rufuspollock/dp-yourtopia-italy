This is a dataset of social indicator time series for the regions of Italy including indicators on poverty, environment, and GDP. It was developed by the Open Knowledge Foundation working group on economics both for general use and as an input for the Open Knowledge Foundation's [YourTopia platform][yourtopia].

[yourtopia]: http://yourtopia.net/

The dataset was originally created during the [Open Economics Hackathon on January 28 2012][hackday]. It includes indicators of social progress on a regional level in Italy.

[hackday]: http://blog.okfn.org/2012/01/18/open-economics-hack-day-saturday-january-28th-2012/

### Data

The primary store of the data is a google docs spreadsheet found in this [DataHub resource](http://thedatahub.org/dataset/yourtopia-italy/resource/5f92c944-4e04-4e3a-8254-0138dd2daa21)

### Code

The github repo contains miscellaneous code for processing and using this data.

    # install DataStore client library
    pip install -e git+http://github.com/okfn/datastore-client    
    # run the script
    python data.py

