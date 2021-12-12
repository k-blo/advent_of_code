


(def input (->> "./input/input-day-1.txt"
                (slurp)
                (clojure.string/split-lines)
                (map #(Integer/parseInt %))))
(def test-input [199 200 208 210 200 207 240 269 260 263])

(->> input
     (partition 2 1)
     (map (fn [[x y]] (< x y)))
     (filter true?)
     (count)
     (println))

(->> test-input
     (partition 3 1)
     (map #(apply + %))
     (partition 2 1)
     (map (fn [[x y]] (< x y)))
     (filter true?)
     (count)
     (println))


(->> input
     (partition 3 1)
     (map #(apply + %))
     (partition 2 1)
     (map (fn [[x y]] (< x y)))
     (filter true?)
     (count)
     (println))