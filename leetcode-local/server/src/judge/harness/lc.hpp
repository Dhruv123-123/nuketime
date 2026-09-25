// ---- leetcode-local C++ harness (auto-generated, not part of your solution) ----
#pragma once
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

namespace lc {

struct Json {
    enum Type { Null, Bool, Num, Str, Arr, Obj } type = Null;
    bool b = false;
    double d = 0;
    long long i = 0;
    bool isInt = false;
    std::string s;
    std::vector<Json> a;
    std::vector<std::pair<std::string, Json>> o;

    bool isNull() const { return type == Null; }
    const std::vector<Json>& arr() const { static std::vector<Json> e; return type == Arr ? a : e; }
    const std::string& str() const { return s; }
    long long ival() const { return isInt ? i : (long long)d; }
    double num() const { return isInt ? (double)i : d; }
    const Json& operator[](size_t k) const { static Json n; return (type == Arr && k < a.size()) ? a[k] : n; }
    const Json& operator[](const std::string& k) const { static Json n; if (type != Obj) return n; for (auto& p : o) if (p.first == k) return p.second; return n; }
};

struct Parser {
    const std::string& s; size_t p = 0;
    Parser(const std::string& str) : s(str) {}
    void ws() { while (p < s.size() && isspace((unsigned char)s[p])) p++; }
    Json parse() {
        ws(); Json j;
        if (p >= s.size()) return j;
        char c = s[p];
        if (c == '{') {
            j.type = Json::Obj; p++; ws();
            if (s[p] == '}') { p++; return j; }
            for (;;) { ws(); Json k = parse(); ws(); p++; /* : */ Json v = parse(); j.o.push_back({k.s, v}); ws(); if (s[p] == ',') { p++; continue; } p++; break; }
        } else if (c == '[') {
            j.type = Json::Arr; p++; ws();
            if (s[p] == ']') { p++; return j; }
            for (;;) { j.a.push_back(parse()); ws(); if (s[p] == ',') { p++; continue; } p++; break; }
        } else if (c == '"') {
            j.type = Json::Str; p++;
            while (p < s.size() && s[p] != '"') {
                if (s[p] == '\\') {
                    p++; char e = s[p++];
                    switch (e) { case 'n': j.s += '\n'; break; case 't': j.s += '\t'; break; case 'r': j.s += '\r'; break; case 'b': j.s += '\b'; break; case 'f': j.s += '\f'; break;
                        case 'u': { unsigned cp = std::stoul(s.substr(p, 4), nullptr, 16); p += 4;
                            if (cp < 0x80) j.s += (char)cp; else if (cp < 0x800) { j.s += (char)(0xC0 | (cp >> 6)); j.s += (char)(0x80 | (cp & 0x3F)); }
                            else { j.s += (char)(0xE0 | (cp >> 12)); j.s += (char)(0x80 | ((cp >> 6) & 0x3F)); j.s += (char)(0x80 | (cp & 0x3F)); } break; }
                        default: j.s += e; }
                } else j.s += s[p++];
            }
            p++;
        } else if (c == 't') { j.type = Json::Bool; j.b = true; p += 4; }
        else if (c == 'f') { j.type = Json::Bool; j.b = false; p += 5; }
        else if (c == 'n') { j.type = Json::Null; p += 4; }
        else {
            size_t st = p; bool isInt = true;
            while (p < s.size() && (isdigit((unsigned char)s[p]) || s[p] == '-' || s[p] == '+' || s[p] == '.' || s[p] == 'e' || s[p] == 'E')) { if (s[p] == '.' || s[p] == 'e' || s[p] == 'E') isInt = false; p++; }
            std::string t = s.substr(st, p - st);
            j.type = Json::Num; j.isInt = isInt;
            if (isInt) { try { j.i = std::stoll(t); } catch (...) { j.isInt = false; j.d = std::stod(t); } }
            else j.d = std::stod(t);
        }
        return j;
    }
};
inline Json parse(const std::string& s) { Parser pr(s); return pr.parse(); }

// ---------- JSON -> C++ ----------
template <class T> struct Conv;
template <> struct Conv<int> { static int from(const Json& j) { return (int)j.ival(); } };
template <> struct Conv<long long> { static long long from(const Json& j) { return j.ival(); } };
template <> struct Conv<long> { static long from(const Json& j) { return (long)j.ival(); } };
template <> struct Conv<double> { static double from(const Json& j) { return j.num(); } };
template <> struct Conv<float> { static float from(const Json& j) { return (float)j.num(); } };
template <> struct Conv<bool> { static bool from(const Json& j) { return j.type == Json::Bool ? j.b : j.ival() != 0; } };
template <> struct Conv<std::string> { static std::string from(const Json& j) { return j.type == Json::Str ? j.s : std::string(); } };
template <> struct Conv<char> { static char from(const Json& j) { return j.s.empty() ? '\0' : j.s[0]; } };
template <> struct Conv<Json> { static Json from(const Json& j) { return j; } };
template <> struct Conv<ListNode*> {
    static ListNode* from(const Json& j) {
        ListNode dummy; ListNode* cur = &dummy;
        for (auto& x : j.arr()) { cur->next = new ListNode((int)x.ival()); cur = cur->next; }
        return dummy.next;
    }
};
template <> struct Conv<TreeNode*> {
    static TreeNode* from(const Json& j) {
        const auto& a = j.arr();
        if (a.empty() || a[0].isNull()) return nullptr;
        TreeNode* root = new TreeNode((int)a[0].ival());
        std::queue<TreeNode*> q; q.push(root); size_t i = 1;
        while (!q.empty() && i < a.size()) {
            TreeNode* n = q.front(); q.pop();
            if (i < a.size() && !a[i].isNull()) { n->left = new TreeNode((int)a[i].ival()); q.push(n->left); }
            i++;
            if (i < a.size() && !a[i].isNull()) { n->right = new TreeNode((int)a[i].ival()); q.push(n->right); }
            i++;
        }
        return root;
    }
};
template <class T> struct Conv<std::vector<T>> {
    static std::vector<T> from(const Json& j) { std::vector<T> v; for (auto& x : j.arr()) v.push_back(Conv<T>::from(x)); return v; }
};
template <class T> T from(const Json& j) { return Conv<T>::from(j); }

// ---------- C++ -> JSON ----------
inline std::string esc(const std::string& s) {
    std::string o = "\"";
    for (unsigned char c : s) {
        switch (c) { case '"': o += "\\\""; break; case '\\': o += "\\\\"; break; case '\n': o += "\\n"; break; case '\r': o += "\\r"; break; case '\t': o += "\\t"; break;
            default: if (c < 0x20) { char b[8]; snprintf(b, sizeof b, "\\u%04x", c); o += b; } else o += (char)c; }
    }
    return o + "\"";
}
inline std::string dump(const Json& j);
// forward declarations so nested containers resolve inside dump_iter
template <class T> std::string dump(const std::vector<T>& v);
template <class T> std::string dump(const std::deque<T>& v);
template <class T> std::string dump(const std::list<T>& v);
template <class T> std::string dump(const std::set<T>& v);
template <class T> std::string dump(const std::unordered_set<T>& v);
template <class A, class B> std::string dump(const std::pair<A, B>& p);
template <class K, class V> std::string dump(const std::map<K, V>& m);
inline std::string dump(ListNode* n);
inline std::string dump(TreeNode* r);
inline std::string dump(bool b) { return b ? "true" : "false"; }
inline std::string dump(char c) { return esc(std::string(1, c)); }
inline std::string dump(const std::string& s) { return esc(s); }
inline std::string dump(const char* s) { return esc(s); }
template <class T> typename std::enable_if<std::is_integral<T>::value && !std::is_same<T, bool>::value && !std::is_same<T, char>::value, std::string>::type dump(T x) { return std::to_string(x); }
template <class T> typename std::enable_if<std::is_floating_point<T>::value, std::string>::type dump(T x) {
    if (std::isnan(x) || std::isinf(x)) return "\"" + std::to_string(x) + "\"";
    char b[64]; snprintf(b, sizeof b, "%.10g", (double)x); return b;
}
inline std::string dump(ListNode* n) { std::string o = "["; int k = 0; while (n && k < 100000) { if (k++) o += ","; o += std::to_string(n->val); n = n->next; } return o + "]"; }
inline std::string dump(TreeNode* r) {
    std::vector<std::string> v; std::queue<TreeNode*> q; q.push(r);
    while (!q.empty() && v.size() < 200000) { TreeNode* n = q.front(); q.pop(); if (!n) { v.push_back("null"); continue; } v.push_back(std::to_string(n->val)); q.push(n->left); q.push(n->right); }
    while (!v.empty() && v.back() == "null") v.pop_back();
    std::string o = "["; for (size_t i = 0; i < v.size(); i++) { if (i) o += ","; o += v[i]; } return o + "]";
}
template <class It> std::string dump_iter(It b, It e) { std::string o = "["; bool f = true; for (auto it = b; it != e; ++it) { if (!f) o += ","; f = false; o += dump(*it); } return o + "]"; }
template <class T> std::string dump(const std::vector<T>& v) { return dump_iter(v.begin(), v.end()); }
template <class T> std::string dump(const std::deque<T>& v) { return dump_iter(v.begin(), v.end()); }
template <class T> std::string dump(const std::list<T>& v) { return dump_iter(v.begin(), v.end()); }
template <class T> std::string dump(const std::set<T>& v) { return dump_iter(v.begin(), v.end()); }
template <class T> std::string dump(const std::unordered_set<T>& v) { return dump_iter(v.begin(), v.end()); }
template <class A, class B> std::string dump(const std::pair<A, B>& p) { return "[" + dump(p.first) + "," + dump(p.second) + "]"; }
template <class K, class V> std::string dump(const std::map<K, V>& m) { std::string o = "{"; bool f = true; for (auto& p : m) { if (!f) o += ","; f = false; o += esc(dump(p.first)) + ":" + dump(p.second); } return o + "}"; }
inline std::string dump(const Json& j) {
    switch (j.type) {
        case Json::Null: return "null"; case Json::Bool: return dump(j.b); case Json::Num: return j.isInt ? std::to_string(j.i) : dump(j.d);
        case Json::Str: return esc(j.s); case Json::Arr: return dump_iter(j.a.begin(), j.a.end());
        case Json::Obj: { std::string o = "{"; bool f = true; for (auto& p : j.o) { if (!f) o += ","; f = false; o += esc(p.first) + ":" + dump(p.second); } return o + "}"; }
    }
    return "null";
}

// ---------- protocol ----------
inline double ms_since(std::chrono::steady_clock::time_point t0) { return std::chrono::duration<double, std::milli>(std::chrono::steady_clock::now() - t0).count(); }
inline void begin(size_t i) { fflush(stdout); std::cout << "\x1e\x1eLC_BEGIN " << i << "\n" << std::flush; }
inline void result(size_t i, const std::string& out, const std::string& mut, std::chrono::steady_clock::time_point t0) {
    fflush(stdout); std::cout << "\n\x1e\x1eLC_RESULT {\"i\":" << i << ",\"ok\":true,\"out\":" << out << ",\"mut\":" << mut << ",\"ms\":" << ms_since(t0) << "}\n" << std::flush;
}
inline void error(size_t i, const std::string& msg, std::chrono::steady_clock::time_point t0) {
    fflush(stdout); std::cout << "\n\x1e\x1eLC_RESULT {\"i\":" << i << ",\"ok\":false,\"error\":" << esc(msg) << ",\"ms\":" << ms_since(t0) << "}\n" << std::flush;
}
} // namespace lc
// ---- end harness ----
