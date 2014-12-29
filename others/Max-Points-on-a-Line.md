# Max Points on a Line

题目来源：[Max Points on a Line](https://oj.leetcode.com/problems/max-points-on-a-line/)

> Given n points on a 2D plane, find the maximum number of points that lie on
the same straight line.

解题思路： 

一种解法是用map，斜率作为key，对每一个点，找过此点斜率相同的点数量。double数值作为map的key貌似不好，这样总感觉挺别扭的……。

注意，斜率不存在的情况，(所有)点重合的情况。
感觉还是用新写一个直线类比较好，下面的[方法二](#method2)就采取了一种类似的方法～或者用c++里的pair,
存斜率，不过得约下分。

第一种方法若用Java写就要注意了，Double作为key时得注意，*斜率+0和-0用Double作为key时不一样*。你可以试着输出Double +.0 和 Double -.0的hashcode，明显是不一样的。

```cpp
int maxPoints(vector<Point> &points) 
{
    int n = points.size();
    if(n <= 1) return n;
    unordered_map<double, int> slopes;
    int result = 1;
    for(int i = 0; i < n-1; i++)
    {
        slopes.clear();
        int dup = 1;
        for(int j = i+1; j < n; j++)
        {
            if(points[i].x == points[j].x && points[i].y == points[j].y)
            {
                ++dup;
                continue;
            }
            double deltaY = points[j].y - points[i].y; 
            double deltaX = points[j].x - points[i].x; 
            double slope = (deltaX == 0 ? INT_MAX: deltaY / deltaX); //yline's slope INT_MAX
            //if(deltaY == 0) // +0.0 != -0.0
            //    slope = .0;
            if(slopes.find(slope) != slopes.end())
                slopes[slope]++;
            else
                slopes.insert(std::pair<double, int>(slope, 1));
        }
        if(result < dup) //all point is the same
            result = dup;
        for(auto it = slopes.begin(); it != slopes.end(); ++it)
        {
            if(it->second + dup > result)
                result = it->second + dup;
        }
    }
    return result;
}
```

<span id = "method2">
方法二，自己新写一个类，科学的写法是斜率+斜率上一点构成直线，然后用另外的直线斜率相等且也过相同的一个点才判断两条直线是重合的，这里就偷懒了，构造直线的时候总用同一个点。
写Hash函数的时候得注意下, 相同的直线(斜率)映射的hash函数要一致才OK。即*== 为true时，hash必须一样*。
</span>

```cpp

struct DeltaPoint
{
    int xx;
    int yy;
    DeltaPoint(int x, int y):xx(x), yy(y)
    {}
    DeltaPoint():xx(0), yy(0){}
    bool operator == (const DeltaPoint &l) const
    {
        if(l.xx == 0 && xx == 0) return true;
        if(l.xx == 0 || xx == 0) return false;
        if(abs(l.yy * 1.0 / l.xx - yy * 1.0 / xx) < 1e-7)
            return true;
        return false;
    }
};

struct hash_func
{
    size_t operator()(const DeltaPoint &l) const
    {
        hash<int> h;
        if(l.xx == 0)
            return 1;
        return h(l.yy / l.xx);
    }
};

bool operator == (const Point &a, const Point &b)
{
    return a.x == b.x && a.y == b.y;
}

int maxPoints2(vector<Point> &points)
{
    int result = 0;
    int n = (int)points.size();
    if(n <= 1) return n;
    unordered_map<DeltaPoint, int,  hash_func> countMap;
    for(int i = 0; i < n-1; i++)
    {
        Point &p0 = (points[i]);
        int same = 1;
        countMap.clear();
        for(int j = i+1; j < n; j++)
        {
            Point &p1 = points[j];
            if (p1 == p0)
                {++same; continue;}
            DeltaPoint pp(p1.x - p0.x, p1.y - p0.y);
            countMap[pp]++;
        }
        result = std::max(result, same);//if only the same points
        for(auto it = countMap.begin(); it != countMap.end(); it++)
        {
            if(it->second + same > result)
                result = it->second + same;
        }
    }
    return result;
}


```

