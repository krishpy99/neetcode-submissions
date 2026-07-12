class KthLargest {
public:
    multiset<int> s;
    int k;
    KthLargest(int k, vector<int>& nums) {
            this->k = k;

            for(auto i: nums){
                s.insert(i);
            }
            for(auto i: s){
                cout<<i<<" ";
            }
            cout<<"\n";
            while(s.size() > k){
                s.erase(s.begin());
            }
    }
    
    int add(int val) {
        s.insert(val);
        if(s.size() > k){
            s.erase(s.begin());
        }
        cout<<val<<": ";
        for(auto i: s){
            cout<<i<<" ";
        }
        cout<<"\n";
        return *s.begin();
    }
};
