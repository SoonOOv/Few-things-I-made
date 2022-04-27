local function splitByCount(s, count) -- S is the string you want to split
    local t = {}
    for i = 1, #s - (#s % count == 0 and 0 or count), count do
        if i == 1 and #s % count > 1 then
            table.insert(t, string.sub(s, i, #s % count))
        end
        table.insert(t, string.sub(s, i + #s % count, i + (count - 1) + #s % count))
    end
    return t
end
